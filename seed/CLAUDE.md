# CLAUDE.md — receipts CLI

## What this is

A local Python CLI that reads receipt files from a folder, extracts structured fields via the Claude API, and maintains a SQLite ledger. See PRD.md for the full spec — read it before planning anything.

## Stack

- Python 3.11+
- Click for the CLI surface (handles command-line arguments and subcommands)
- SQLite via the stdlib `sqlite3` module (no ORM)
- `anthropic` Python SDK for extraction
- `pytest` for tests
- `uv` for dependency management

## Layout

- `src/receipts/cli.py`     — Click entry points
- `src/receipts/ledger.py`  — SQLite read/write, idempotency, inline schema creation
- `src/receipts/extract.py` — Claude API call, JSON schema validation
- `src/receipts/report.py`  — deterministic CSV emitter
- `inbox/`                  — sample receipts shipped with the repo
- `dashboard.html`          — visual viewer, reads `data.json` produced by `receipts export`

## Conventions

- All public functions get type hints.
- Stdout is for data. Logs go to stderr.
- Exit code 0 on success, 1 on any failure, 2 on user error (bad flag).
- No network calls in `ledger.py` or `report.py`. Ever.

## Determinism

The report command output must be byte-identical for a fixed ledger. Sort by `(date ASC, source_file ASC)`. Use `csv.writer` with default dialect. No timestamps in output.

## When you change behaviour, also update

- `PRD.md` acceptance criteria, if scope shifted
- `README.md` usage section

## What to ask me about, never assume

- Anything that adds a new dependency
- Anything that touches `migrations/` after the initial one
- Anything that changes the JSON schema returned by `extract.py`
