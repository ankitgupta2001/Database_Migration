from common.db import SRC_POOL, TGT_POOL
from common.logger import get_logger
from configs.migration_settings import DISABLED_TABLES
from typing import List, Optional

logger = get_logger("IndexReplicator")

def replicate_table_indexes(table_name: str, migrated_fields: List[str], target_table_name: Optional[str] = None):
    """
    Fetches indexes from source, filters for migrated fields,
    and applies them to the target if they don't exist.
    """
    tgt_table = target_table_name or table_name
    src_conn = SRC_POOL.get_connection()
    tgt_conn = TGT_POOL.get_connection()

    try:
        # 1. Fetch Source Indexes
        src_cursor = src_conn.cursor(dictionary=True)
        src_cursor.execute(f"SHOW INDEX FROM `{table_name}`")
        src_indexes = src_cursor.fetchall()
        src_cursor.close()

        if not src_indexes:
            return

        # Group indexes by name
        index_map = {}
        for idx in src_indexes:
            key_name = idx['Key_name']
            if key_name == 'PRIMARY':
                continue

            if key_name not in index_map:
                index_map[key_name] = {
                    'unique': idx['Non_unique'] == 0,
                    'columns': []
                }
            index_map[key_name]['columns'].append(idx['Column_name'])

        # 2. Fetch Target Indexes (to avoid duplicates)
        tgt_cursor = tgt_conn.cursor(dictionary=True)
        tgt_cursor.execute(f"SHOW INDEX FROM `{tgt_table}`")
        tgt_indexes = tgt_cursor.fetchall()
        tgt_cursor.close()

        tgt_key_names = {idx['Key_name'] for idx in tgt_indexes}

        # 3. Filter and Apply
        for key_name, info in index_map.items():
            cols = info['columns']
            is_unique = info['unique']

            # Check if all columns in source index are being migrated
            if not all(col in migrated_fields for col in cols):
                logger.debug(f"Skipping index {key_name} on {table_name}: uses non-migrated fields {set(cols) - set(migrated_fields)}")
                continue

            # Check if index already exists on target (by name)
            if key_name in tgt_key_names:
                logger.info(f"Index {key_name} already exists on target {tgt_table}. Skipping.")
                continue

            # Build and execute CREATE INDEX
            unique_str = "UNIQUE" if is_unique else ""
            cols_str = ", ".join([f"`{c}`" for c in cols])

            # We use a generic name if the original name exists but with different definition?
            # For now, we trust the key_name is unique or will fail safely if it exists with different def.
            create_sql = f"CREATE {unique_str} INDEX `{key_name}` ON `{tgt_table}` ({cols_str})"

            logger.info(f"Replicating index {key_name} on {tgt_table} -> {cols}")

            tgt_cursor = tgt_conn.cursor()
            try:
                tgt_cursor.execute(create_sql)
                tgt_conn.commit()
            except mysql.connector.Error as e:
                if e.errno == 1061: # Duplicate key name
                    logger.info(f"Index {key_name} already exists (errno 1061).")
                else:
                    logger.error(f"Failed to create index {key_name} on {tgt_table}: {e}")
            finally:
                tgt_cursor.close()

    except Exception as e:
        logger.error(f"Error replicating indexes for {table_name}: {e}")
    finally:
        src_conn.close()
        tgt_conn.close()

def replicate_all_module_indexes(tables_cfg: List[dict]):
    """Helper to run replication for a list of table configs."""
    for cfg in tables_cfg:
        table_name = cfg['table_name']

        # CHECK IF TABLE IS DISABLED
        if table_name in DISABLED_TABLES:
            logger.info(f"Table {table_name} is disabled in settings. Skipping index replication.")
            continue

        migrated_fields = cfg['insert_fields']
        target_table_name = cfg.get('target_table_name')

        # We skip tabSingles as it doesn't have standard indexes on its fields
        if table_name == 'tabSingles':
             continue

        replicate_table_indexes(table_name, migrated_fields, target_table_name)
