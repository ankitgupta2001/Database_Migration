# Database Migration Tool (Core)

This subdirectory contains the core logic and configurations for the migration tool.

## Features

- **Keyset Pagination**: Constant performance for large tables.
- **Resumability**: Progress tracked in `migration_state.json`.
- **Fault Tolerance**: Automatic retries with exponential backoff.
- **Session Safety**: Dynamic adjustment of packet sizes and timeouts.
- **Table-Specific Tuning**: Custom batch sizes and filters.

## How to Run

From the root directory of the repository:
```bash
python3 db_migration/migrate_core.py
python3 db_migration/migrate_iam.py
python3 db_migration/migrate_spine.py
```

Or from within this directory:
```bash
python3 migrate_core.py
python3 migrate_iam.py
python3 migrate_spine.py
```

## Structure

- `/common`: Database connection pooling and the batch migrator engine.
- `/configs`: Table schemas and migration filters.
- `.env`: Database credentials and tuning.
- `migration_state.json`: Auto-generated progress tracker.
- `migration.log`: Auto-generated audit log.

## Quick Reset

- To reset a specific table: Delete its key in `migration_state.json`.
- To reset everything: Delete `migration_state.json`.
