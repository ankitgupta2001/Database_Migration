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

1. **System Core**: `python3 db_migration/migrate_core.py`
2. **IAM App Data**: `python3 db_migration/migrate_iam.py`
3. **Spine Data**: `python3 db_migration/migrate_spine.py`

## Monitoring & State

- **Console**: Real-time progress with formatted table spacing for easy reading.
- **File**: Detailed records are saved to `db_migration/migration.log`.
- **State**: Progress is tracked per-table in `db_migration/migration_state.json`.

## Troubleshooting

- **Packet Error**: If you see "Got a packet bigger than 'max_allowed_packet'", decrease the `batch_size` in the specific table configuration (e.g., `iam_tables.py`).
- **Lost Connection**: The script retries automatically. If persistent, increase `NET_READ_TIMEOUT` in `.env`.
- **Resetting Progress**: Delete the table's entry in `migration_state.json` to restart it.
