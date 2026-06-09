# Prerequisites

**Read this before you arrive. Plan 30 minutes of setup at home.**

Two hours in a coffee shop is not enough time to debug a broken install. Everyone needs the four things below working *before* walking in.

## 1. A paid Claude subscription

The $20/month Claude Pro plan is enough for this workshop. Monthly billing is fully supported as of May 2026 — annual is optional ($17/month if you prefer to pre-pay).

- Subscribe at `claude.com/pricing` → pick **Pro**.
- Claude Code is included with Pro at no extra cost.
- The free claude.ai plan will **not** work — Claude Code requires a subscription or API key.
- **No subscription?** An API key costs ~SAR 0.40 per session — [see free and low-cost options](free-options.md).

For Saudi Arabia specifically: Anthropic officially supports Saudi Arabia for both Claude.ai and the API. No VPN needed. See the [KSA payment notes](ksa-payments.md) page if your card is declined.

## 2. Claude Code installed

Two install paths. Pick one. The native installer is the current recommendation.

**Native installer (no Node.js needed):**

```bash
# macOS / Linux / WSL (Windows Subsystem for Linux)
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex
```

The `curl` / `irm` commands download and run the installer automatically — same idea as a web-based setup wizard, just in the terminal.

**npm fallback (if you prefer Node.js):**

```bash
npm install -g @anthropic-ai/claude-code
```

`npm` is the package manager that comes with Node.js — a way to install command-line tools with one command.

If you hit `EACCES` errors on npm (a permission error meaning "this installer doesn't have write access to the system folder"), **do not use `sudo`**. Set up a user-local prefix instead — this tells npm to install tools into your own home folder where it has permission:

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc   # or ~/.zshrc
source ~/.bashrc
```

Then retry.

**Verify it works:**

```bash
claude --version    # should print 2.x or higher
claude doctor       # should show green checkmarks
```

Run `claude` once in any folder. You'll be prompted to log in via browser. Use your paid Claude account.

## 3. Python 3.11 or higher

The workshop's anchor project is a Python CLI. Check:

```bash
python --version   # or: python3 --version
```

If you're below 3.11, install via [python.org](https://www.python.org/downloads/), Homebrew (`brew install python@3.12` — Homebrew is a popular tool installer for macOS), or your operating system's package manager.

## 4. The seed repo cloned

Don't try to clone at the coffee shop on shared Wi-Fi — do this at home.

The seed lives inside the workshop repo, in the `seed/` subfolder. Clone the workshop repo and navigate into it:

```bash
git clone https://github.com/thepandanlabs/claude-code-workshop.git
cd claude-code-workshop/seed
```

Then confirm the test harness loads:

```bash
uv sync                        # or: pip install -e .
pytest tests/ --collect-only   # should list 3 tests
claude /prime                  # should read the PRD back to you
```

If `pytest --collect-only` lists three tests and `/prime` reads the PRD back to you, you're ready.

The seed folder ships with:

- `PRD.md` — the one-page spec for the receipts CLI.
- `CLAUDE.md` — the codebase conventions.
- `.claude/commands/` — the four slash commands (`/prime`, `/plan`, `/implement`, `/verify`).
- `inbox/` — ten sample receipt files for the build.
- `src/receipts/` — stub source files (empty — Claude builds the implementation during the workshop).
- `tests/` — the starter automated test suite, including golden fixtures (saved examples of correct output that every future run is compared against).

## Also helpful

- **Git installed.** Windows: install [Git for Windows](https://git-scm.com/download/win) so Claude Code's Bash tool works correctly.
- **A code editor.** VS Code, Cursor, or whatever you already use. Not strictly required — Claude Code edits files for you — but useful for reading diffs.
- **A real meeting transcript or two pages of work notes** (anonymised) if you want to try the receipts CLI on something other than the supplied samples. Optional.

## Day-of setup

Arrive at 100% battery. Coffee-shop power outlets are unreliable. A 2-hour workshop running an agent on Sonnet 4.6 will drain a laptop to ~30%.

Bring your phone, with mobile hotspot ready. Coffee-shop Wi-Fi is the single most common failure mode.

## If something is broken the morning of the workshop

Run `claude doctor` and read the output. If it doesn't fix itself, message the facilitator with the **exact** error text — not a paraphrase. Don't show up with nothing installed; the room has 6–12 people and one facilitator, and one broken laptop can swallow ten minutes.

[← Back to home](index.html)
