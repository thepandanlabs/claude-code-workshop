# Block 2 — Structured Intent

**Time:** 00:20 – 00:40
**Goal:** Everyone has read and understood the PRD, the `CLAUDE.md`, and the slash commands. No code is written yet.

## What happens in this block

1. **00:20 – 00:25 — Walk the PRD aloud.** Open `PRD.md` from the seed repo on the facilitator's laptop. Read it section by section. Pause at *In scope* and *Out of scope* — these are the lines that prevent scope drift.
2. **00:25 – 00:32 — Walk the `CLAUDE.md` aloud.** Same drill, different file. Highlight the *Conventions*, the *Determinism* section, and the *When you change behaviour, also update* checklist. State the rule: **"if removing a line wouldn't cause a mistake, cut it."** Sub-100 lines is not aesthetics — it's the model's effective instruction budget.
3. **00:32 – 00:36 — Tour the slash commands.** Open `.claude/commands/` in the seed repo. The four commands ship in the repo:
   - `/prime` — read the PRD and `CLAUDE.md` and confirm you understand the project shape.
   - `/plan` — produce a written plan against the PRD, do not write code.
   - `/implement` — execute the approved plan, step by step.
   - `/verify` — run `pytest`, paste any failures back, fix, re-run.
4. **00:36 – 00:40 — Q&A.** Take three questions. No more. Anything bigger goes to Block 6.

## What the room walks away with

The two files and the four commands are the entire structured-intent stack for this workshop. There is nothing else to learn. The build block runs on this surface.

## The PRD in 60 seconds

The PRD says: a CLI called `receipts` that takes a folder of receipt files, calls Claude to extract structured fields, appends them to a SQLite ledger, dedupes by file hash, and emits deterministic CSV reports. Three subcommands: `add`, `list`, `report`. Out of scope: auth, cloud sync, currency conversion, anything web or mobile.

The acceptance criteria are testable:

- `pytest tests/` is green.
- `receipts add inbox/` on the ten supplied samples produces ten rows.
- Re-running it adds zero rows and reports ten duplicates.
- `receipts report --month 2026-05 --format csv` is byte-identical to `tests/golden/may.csv`.
- `--help` is informative on every subcommand.

That last bullet — byte-identical CSV output — is the thing that makes verification possible. It's the load-bearing constraint of the whole project.

## The `CLAUDE.md` in 60 seconds

The `CLAUDE.md` tells Claude:

- The stack (Python 3.11+, Click, sqlite3 stdlib, anthropic SDK, pytest, uv).
- The file layout (`src/receipts/cli.py`, `ledger.py`, `extract.py`, `report.py`, plus `migrations/`, `tests/`, `inbox/`).
- The conventions (type hints, stdout for data, stderr for logs, exit codes).
- The determinism contract (sort by `date ASC, source_file ASC`, no timestamps in output).
- What to ask the human about before doing (new dependencies, schema changes, migrations).

Open the file. Read it. That's the brief.

## Common questions in this block

- **"Why not put all this in the prompt?"** Because every new session would need the same essay. The PRD and `CLAUDE.md` are *re-read on every turn* once they exist. The prompt becomes short because the context is durable.
- **"Why both? Isn't a PRD enough?"** The PRD describes *what* the user wants. The `CLAUDE.md` describes *how this codebase prefers to work*. Same project, two audiences.
- **"What if I disagree with the spec?"** Edit it. The PRD and `CLAUDE.md` are yours. The discipline is that you change them deliberately, not that you obey them.

[← Back to home](index.html)
