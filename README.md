# Database Migration Tool

A robust, resumable Python-based mini-ETL designed to handle large-scale MariaDB/MySQL data transfers (TB scale) without OOM errors. It ports logic from SQL migration scripts into a manageable Python framework.

## Features

- **Keyset Pagination**: Uses Seeking (seek by ID) instead of Offset for constant performance regardless of table size.
- **Resumability**: Saves progress to `migration_state.json`. If interrupted, it continues exactly from the last successful batch.
- **Fault Tolerance**: Automatic reconnection and retry logic with exponential backoff for database operations.
- **Safety**: Automatically disables `FOREIGN_KEY_CHECKS` and increases timeouts/packet sizes during migration, restoring them safely on completion.
- **Table-Specific Tuning**: Supports custom `batch_size`, `order_by`, and `where` filters per table.
- **Improved Logging**: Clean, readable console progress updates and dedicated `migration.log` for auditing.

## Installation

1. **Clone the Repository**:
   If the repository is private, use your username and Personal Access Token (PAT) or Password in the URL:

   ```bash
   git clone https://username:password-or-token@github.com/your-org/Database_Migration.git
   cd Database_Migration
   ```
2. **Setup Virtual Environment** (Optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install Dependencies**:

   ```bash
   pip install mysql-connector-python python-dotenv

   sudo apt update && sudo apt-install get vim -y
   ```

## Configuration

1. Locate the `db_migration` directory.
2. Create a `.env` file inside `db_migration`:

```ini
# Source DB
SRC_DB_HOST=your-source-host
SRC_DB_NAME=source_db

# Target DB
TGT_DB_HOST=your-target-host
TGT_DB_NAME=target_db

# Migration tuning
BATCH_SIZE=5000
LOG_LEVEL=INFO
MAX_ALLOWED_PACKET=1073741824
NET_READ_TIMEOUT=3600
NET_WRITE_TIMEOUT=3600
```

## How to Run

The migration is organized into three distinct modules. You can run them using the `run.py` script within each folder.

1. **System Core**: `python3 db_migration/core/run.py`
2. **IAM App Data**: `python3 db_migration/iam/run.py`
3. **Spine Data**: `python3 db_migration/spine/run.py`

## Monitoring & State

- **Console**: Real-time progress formatted for easy reading.
- **File**: Detailed records are saved to `db_migration/migration.log`.
- **State**: Progress is tracked per-table in `db_migration/migration_state.json`.
- **Disabling Tables**: You can skip specific tables by adding them to `DISABLED_TABLES` in `db_migration/configs/migration_settings.py`.

## Structure

- `/core`: Scripts for roles, users, and auth.
- `/iam`: Scripts for IAM masters and audit logs.
- `/spine`: Scripts for document mapping and spine logs.
- `/common`: Database connection pooling and the batch migrator engine.
- `/configs`: Table schemas and the global `migration_settings.py`.
