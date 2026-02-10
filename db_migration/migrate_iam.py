from common.batch_migrator import migrate_table, execute_session_setup, execute_session_teardown
from configs.iam_tables import IAM_TABLES
from common.logger import get_logger

logger = get_logger("IAM-Migration")

def main():
    try:
        execute_session_setup()
        for cfg in IAM_TABLES:
            migrate_table(**cfg)
    finally:
        execute_session_teardown()

if __name__ == "__main__":
    logger.info("Starting IAM migration")
    main()
    logger.info("IAM migration finished")
