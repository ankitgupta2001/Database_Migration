import os
import json
import time
import functools
from typing import List, Optional
from common.db import SRC_POOL, TGT_POOL
from common.logger import get_logger
from configs.migration_settings import DISABLED_TABLES
from mysql.connector import Error, OperationalError

logger = get_logger("BatchMigrator")
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 5000))
STATE_FILE = "migration_state.json"
MAX_ALLOWED_PACKET = int(os.getenv("MAX_ALLOWED_PACKET", 1073741824))
NET_READ_TIMEOUT = int(os.getenv("NET_READ_TIMEOUT", 3600))
NET_WRITE_TIMEOUT = int(os.getenv("NET_WRITE_TIMEOUT", 3600))

def load_state(table_name: str) -> Optional[str]:
    if not os.path.exists(STATE_FILE):
        return None
    try:
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
            return data.get(table_name)
    except Exception as e:
        logger.warning(f"Failed to load state: {e}")
        return None

def save_state(table_name: str, last_id: str):
    data = {}
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                data = json.load(f)
        except Exception:
            pass

    data[table_name] = last_id
    with open(STATE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def retry_db_operation(max_retries=5, delay=2, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            current_delay = delay
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except (OperationalError, Error) as e:
                    # Do not retry for certain errors (like Table/Column Doesn't Exist)
                    # 1146: Table doesn't exist, 1054: Unknown column
                    if hasattr(e, 'errno') and e.errno in (1146, 1054):
                        raise e
                    logger.error(f"Database error: {e}. Retrying in {current_delay}s... ({retries + 1}/{max_retries})")
                    time.sleep(current_delay)
                    retries += 1
                    current_delay *= backoff
            raise Exception(f"Operation failed after {max_retries} retries")
        return wrapper
    return decorator

@retry_db_operation()
def fetch_batch(src_conn, select_sql, params):
    cursor = src_conn.cursor(dictionary=True)
    try:
        cursor.execute(select_sql, params)
        rows = cursor.fetchall()
        return rows
    finally:
        cursor.close()

@retry_db_operation()
def insert_batch(tgt_conn, insert_sql, values):
    cursor = tgt_conn.cursor()
    try:
        cursor.executemany(insert_sql, values)
        tgt_conn.commit()
    except Exception:
        tgt_conn.rollback()
        raise
    finally:
        cursor.close()

def migrate_table(
    table_name: str,
    select_fields: List[str],
    insert_fields: List[str],
    where: str = "1=1",
    batch_size: int = BATCH_SIZE,
    target_table_name: Optional[str] = None,
    order_by: Optional[str] = "name"
):
    # Use table_name as default for target if not provided
    tgt_table = target_table_name or table_name

    # CHECK IF TABLE IS DISABLED
    if table_name in DISABLED_TABLES:
        logger.info(f"Table {table_name} is disabled in settings. Skipping.")
        return

    # Try to load previous state
    last_migrated_id = load_state(table_name)
    if last_migrated_id:
        logger.info(f"Resuming {table_name} -> {tgt_table} from ID: {last_migrated_id}")
    else:
        logger.info(f"Starting {table_name} -> {tgt_table} migration from scratch")

    src_conn = SRC_POOL.get_connection()
    tgt_conn = TGT_POOL.get_connection()

    # CHECK TABLE EXISTENCE
    try:
        cursor = src_conn.cursor()
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        if not cursor.fetchone():
            logger.warning(f"Table {table_name} does not exist in source. Skipping.")
            return
        cursor.close()

        cursor = tgt_conn.cursor()
        cursor.execute(f"SHOW TABLES LIKE '{tgt_table}'")
        if not cursor.fetchone():
            logger.warning(f"Table {tgt_table} does not exist in target. Skipping.")
            return
        cursor.close()
    except Exception as e:
        logger.error(f"Error checking table existence for {table_name}: {e}")
        # We continue anyway if check fails, fetch_batch will catch it if it's a real issue

    try:
        total = 0

        # KEYSET PAGINATION LOGIC
        # We assume 'name' is the primary key and sortable
        # Query: SELECT ... FROM table WHERE (cond) AND name > last_id ORDER BY name LIMIT batch_size

        def wrap_backticks(fields):
            wrapped = []
            for f in fields:
                upper_f = f.upper()
                if " AS " in upper_f:
                    # Find split point while preserving original case
                    idx = upper_f.find(" AS ")
                    col_part = f[:idx].strip()
                    alias_part = f[idx+4:].strip()
                    wrapped.append(f"`{col_part}` AS `{alias_part}`")
                else:
                    wrapped.append(f"`{f.strip()}`")
            return ",".join(wrapped)

        base_select = f"""
            SELECT {wrap_backticks(select_fields)}
            FROM `{table_name}`
            WHERE {where}
        """

        insert_sql = f"""
            INSERT IGNORE INTO `{tgt_table}`
            ({",".join([f"`{f.strip()}`" for f in insert_fields])})
            VALUES ({",".join(["%s"] * len(insert_fields))})
        """

        while True:
            # Construct dynamic WHERE clause for pagination
            pagination_clause = ""
            params = []

            if order_by and last_migrated_id:
                pagination_clause = f" AND `{order_by}` > %s"
                params.append(last_migrated_id)

            # Finalize query with ORDER BY and LIMIT
            if order_by:
                final_select_sql = f"{base_select} {pagination_clause} ORDER BY `{order_by}` LIMIT %s"
                params.append(batch_size)
            else:
                final_select_sql = base_select

            # Fetch batch
            rows = fetch_batch(src_conn, final_select_sql, tuple(params))

            if not rows:
                break

            # Prepare values for insertion
            values = [
                tuple(row[col.split(' AS ')[-1]] if ' AS ' in col else row[col] for col in insert_fields)
                for row in rows
            ]

            # Insert batch
            insert_batch(tgt_conn, insert_sql, values)

            # Update state (only if order_by is provided)
            if order_by:
                last_migrated_id = rows[-1][order_by]
                save_state(table_name, last_migrated_id)

            batch_count = len(rows)
            total += batch_count

            logger.info(
                f"{table_name.ljust(30)} | PROGRESS: {str(total).rjust(8)} rows migrated | BATCH: {str(batch_count).rjust(5)} | LAST ID: {last_migrated_id if order_by else 'N/A'}"
            )

            # If no order_by, we finish after one batch
            if not order_by:
                break

        logger.info(f"{table_name} | migration completed | total {total}")

    except Exception:
        logger.exception(f"{table_name} | migration failed")
        raise
    finally:
        if src_conn.is_connected():
            src_conn.close()
        if tgt_conn.is_connected():
            tgt_conn.close()

def execute_session_setup():
    """Sets session variables for safety and performance."""
    logger.info(f"Setting session variables: FK Checks=0, Max Packet={MAX_ALLOWED_PACKET}, Timeouts={NET_READ_TIMEOUT}s")
    tgt_conn = TGT_POOL.get_connection()
    try:
        cursor = tgt_conn.cursor()
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        # Use SESSION scope so it affects the current connection immediately
        # Note: Some servers require GLOBAL for max_allowed_packet, but SESSION is what affects the current connection.
        try:
            cursor.execute(f"SET SESSION max_allowed_packet = {MAX_ALLOWED_PACKET}")
        except Exception:
            cursor.execute(f"SET GLOBAL max_allowed_packet = {MAX_ALLOWED_PACKET}")

        cursor.execute(f"SET SESSION net_read_timeout = {NET_READ_TIMEOUT}")
        cursor.execute(f"SET SESSION net_write_timeout = {NET_WRITE_TIMEOUT}")
        cursor.execute("SET GROUP_CONCAT_MAX_LEN = 1024000")
        tgt_conn.commit()
    except Exception as e:
        logger.warning(f"Could not set some session variables: {e}")
    finally:
        tgt_conn.close()

def execute_session_teardown():
    """Restores session variables."""
    logger.info("Restoring session variables: FK Checks=1")
    tgt_conn = TGT_POOL.get_connection()
    try:
        cursor = tgt_conn.cursor()
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        tgt_conn.commit()
    except Exception as e:
        logger.warning(f"Failed to restore session variables: {e}")
    finally:
        tgt_conn.close()
