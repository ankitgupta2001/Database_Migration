import os
import sys

# Add the parent directory (db_migration root) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from common.batch_migrator import migrate_table, execute_session_setup, execute_session_teardown
from configs.core_tables import CORE_TABLES
from common.logger import get_logger

logger = get_logger("Core-Migration")

def main():
    try:
        execute_session_setup()
        for cfg in CORE_TABLES:
            migrate_table(**cfg)
    finally:
        execute_session_teardown()

if __name__ == "__main__":
    logger.info("Starting Core migration")
    main()
    logger.info("Core migration finished")
