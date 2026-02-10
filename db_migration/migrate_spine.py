from common.batch_migrator import migrate_table, execute_session_setup, execute_session_teardown
from configs.spine_tables import SPINE_TABLES
from common.logger import get_logger

logger = get_logger("SPINE-Migration")

def main():
    try:
        execute_session_setup()
        for cfg in SPINE_TABLES:
            migrate_table(**cfg)
    finally:
        execute_session_teardown()

if __name__ == "__main__":
    logger.info("Starting Spine migration")
    main()
    logger.info("Spine migration finished")
