import os
import sys

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from common.index_replicator import replicate_all_module_indexes
from configs.iam_tables import IAM_TABLES
from configs.core_tables import CORE_TABLES
from configs.spine_tables import SPINE_TABLES
from common.logger import get_logger

logger = get_logger("IndexMigration-Main")

def main():
    logger.info("Starting Index Replication across all modules")

    logger.info("--- Replicating Core Table Indexes ---")
    replicate_all_module_indexes(CORE_TABLES)

    logger.info("--- Replicating IAM Table Indexes ---")
    replicate_all_module_indexes(IAM_TABLES)

    logger.info("--- Replicating Spine Table Indexes ---")
    replicate_all_module_indexes(SPINE_TABLES)

    logger.info("Index Replication completed")

if __name__ == "__main__":
    main()
