# TODO: SQLite read/write operations.
# - Apply migrations/0001_init.sql on first run
# - add_receipt(record: dict) -> bool — insert or skip (SHA-256 dedup), returns True if inserted
# - list_receipts(filters: dict) -> list[dict] — query with optional vendor/since/until filters
# See CLAUDE.md Conventions section for deduplication rules.
# No network calls in this file.
