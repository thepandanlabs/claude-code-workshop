# The Seed Repository

The seed repo is the starting point for the workshop's build block. Everyone clones it before arriving and runs the workshop from this folder.

## What's in it

```
workshop-seed-repo/
├── PRD.md                      # The one-page spec — read it
├── CLAUDE.md                   # The codebase conventions — sub-100 lines
├── README.md                   # Quick orientation
├── pyproject.toml              # Python project metadata (uv-ready)
├── .claude/
│   ├── commands/
│   │   ├── prime.md            # /prime — read PRD + CLAUDE.md, confirm understanding
│   │   ├── plan.md             # /plan — produce a written plan, no code
│   │   ├── implement.md        # /implement — execute the approved plan
│   │   └── verify.md           # /verify — run pytest, fix failures, re-run
│   └── settings.json           # Permissions and model preferences
├── src/
│   └── receipts/
│       ├── __init__.py         # Empty — to be filled
│       ├── cli.py              # Empty — to be filled
│       ├── extract.py          # Empty — to be filled
│       ├── ledger.py           # Empty — to be filled
│       └── report.py           # Empty — to be filled
├── migrations/
│   └── 0001_init.sql           # Initial SQLite schema (provided)
├── inbox/
│   ├── sample-01.txt           # Ten sample receipts in mixed formats
│   ├── sample-02.txt
│   ├── ...
│   └── sample-10.txt
├── tests/
│   ├── conftest.py             # Mocks the Claude API call, replays fixtures
│   ├── test_ledger.py          # Idempotency test (provided)
│   ├── test_report.py          # Byte-identical CSV test (provided)
│   ├── test_schema.py          # Pydantic schema validation (provided)
│   ├── fixtures/
│   │   └── extractions/        # Recorded JSON outputs for the ten samples
│   │       ├── sample-01.json
│   │       └── ...
│   └── golden/
│       └── may.csv             # Golden monthly report — intentionally one row short
└── .gitignore
```

## How to get it

```bash
git clone <facilitator-provided-url>
cd workshop-seed-repo
```

The facilitator will share the exact URL ahead of the workshop. Until then, the contents above tell you what shape to expect.

## How to confirm it's healthy

After cloning, run:

```bash
# Install dependencies (uv if you have it, pip otherwise)
uv sync                          # OR: pip install -e .

# Confirm the test harness loads (everything will fail — that's expected)
pytest tests/ --collect-only

# Confirm Claude Code can see the slash commands
claude /prime
```

If `pytest --collect-only` lists three tests and `/prime` reads the PRD back to you, you're ready.

## What's deliberately not in it

- **Working source files.** `src/receipts/*.py` are stubs. The whole point of the workshop is that Claude Code fills them in based on the PRD and `CLAUDE.md`.
- **A `.env` file.** Claude Code uses your authenticated session — no API key juggling.
- **Auth, persistence beyond SQLite, anything cloud.** The PRD explicitly puts these out of scope.

## Why the tests ship pre-built

Because the workshop's central beat is *watching a test fail and then pass*. If attendees write the tests themselves, the harness shows up at 01:35 instead of 01:25, and the verification block runs out of time. Pre-built tests + empty source files = the right balance.

The golden CSV (`tests/golden/may.csv`) is intentionally one row short of what the ten samples should produce. The first run of `pytest` will fail. That failure is the teaching moment of Block 4.

[← Back to home](index.html)
