# Track A — Polished CLI

**Goal:** Take `receipts` from "works on my laptop" to "I'd put this on PyPI." An evening of work.

## What changes

Add a `rich`-formatted output mode, a `--dry-run` flag, proper structured logging, shell completion for bash and zsh, and packaging metadata so `uv build` produces a wheel you could actually publish.

## Starting prompt

Paste into a fresh Claude Code session in your repo, with Plan Mode on (Shift+Tab twice):

```text
Read PRD.md and CLAUDE.md. We're polishing the receipts CLI for
publication.

Plan the changes to add:
1. `rich`-formatted tables for `list` and `report` when stdout is a TTY,
   keeping deterministic CSV/TSV output when piped (this matters — the
   golden tests must still pass).
2. A `--dry-run` flag for `add` that shows what would be added without
   touching the ledger.
3. Click-based shell completion for bash and zsh.
4. Structured logging behind a `--verbose` flag (logs to stderr only).
5. A `pyproject.toml` ready for `uv build`, with proper entry points.

Constraints:
- Do not regress any existing test in tests/.
- Stdout-when-piped output must remain byte-identical to current behaviour.
- Keep CLAUDE.md updated with any new conventions you introduce.

Plan first. Do not write code yet.
```

## Milestones

1. **Rich tables that don't break golden tests.** Verify with `pytest tests/ -v` after the change. The tests pipe stdout, which triggers the non-TTY path — they should still be green.
2. **`--dry-run` for `add`**, with a new test that confirms zero ledger writes.
3. **`pyproject.toml` and `uv build`** produces a wheel in `dist/`.

## Definition of done

- `uv tool install ./dist/receipts-*.whl` installs `receipts` globally on your machine.
- `receipts --help` is readable and complete.
- All original tests still pass.
- `receipts list` in your terminal produces a coloured table; `receipts list | cat` produces tab-separated plain text.
- (Stretch) A GitHub Actions workflow runs `pytest` on every push.

## Useful libraries

- **Click** — already in the seed repo, the CLI framework.
- **Rich** — for the table formatting.
- **uv** — Python package manager. Faster than pip, currently the recommended choice for new Python CLIs.

## Things to watch for

- **The dual-mode output.** This is where most polish attempts fail — they make the tables pretty and break the pipe-to-CSV behaviour. Use `sys.stdout.isatty()` to decide.
- **Shell completion installation.** Click can generate completion scripts but the user still has to source them. Document this in the README, don't try to auto-install.
- **Don't add features the PRD doesn't have.** A polished CLI is the same CLI with better UX, not a different CLI.

## Read next

- The [Click documentation](https://click.palletsprojects.com/) — specifically the sections on auto-environment-variable expansion and shell completion.
- The Rich docs — `rich.readthedocs.io`. Use `rich.console.Console`, not the auto-import patterns. Determinism matters.
- The `uv` docs — `docs.astral.sh/uv/`. The publish flow is `uv build` then `uv publish`.

[← Back to home](index.html)
