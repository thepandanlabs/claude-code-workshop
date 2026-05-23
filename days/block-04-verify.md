# Block 4 — Verify

**Time:** 01:25 – 01:40
**Goal:** Every attendee sees a test fail, watches Claude read the failure, and watches the test pass. This is the workshop's central beat.

<!-- participant-start -->
## Block 4 — What to do

This block makes the work real. Follow these steps in order.

1. Run `pytest` — note which tests pass and which fail
2. If a test fails: paste the error into Claude Code and run `/verify`
3. Watch Claude read the failure and propose a fix — approve it
4. Run `pytest` again — all tests should pass now
5. Run `receipts add inbox/` twice — confirm zero new rows the second time
6. Run `receipts export` and open `dashboard.html` in your browser — your ledger should appear
<!-- participant-end -->

## Why this block exists

A chat-tab user shows you something that "works" by running it once. A builder shows you something that works by running a test suite. The difference between the two is the difference between "looks right" and "is right."

For a business: a demo that worked once is not a guarantee. A new hire changes one line of code — you don't know what broke. A model update changes Claude's output format — you don't know until a client complains. The eval suite is your early warning system: it runs after every change and tells you immediately whether anything broke. **That's what this block builds.**

This block is 15 minutes, not 5. Don't shortcut it.

## The shape

| Time | Activity |
|---|---|
| 01:25 – 01:28 | Run the harness for the first time. |
| 01:28 – 01:33 | A test fails. Paste the failure into Claude. |
| 01:33 – 01:37 | Claude fixes it. Re-run. Green. |
| 01:37 – 01:40 | Talk through the three layers of the harness. |

## Step 1 — Run the harness

In every attendee's repo:

```bash
pytest tests/ -v
```

What's in `tests/`:

- `test_ledger.py` — checks that adding the ten sample receipts twice produces exactly ten rows (not twenty).
- `test_report.py` — checks that `receipts report --month 2026-05 --format csv` matches `tests/golden/may.csv` character for character.
- `test_schema.py` — checks that each extracted receipt contains all required fields in the right format (date as YYYY-MM-DD, amount as a positive number, currency as a 3-letter code, etc.).

At least one will fail on the first run. That's by design — the seed `golden/may.csv` is intentionally one row short of what the ten samples should produce. The test exists to fail the first time.

## Step 2 — Read the failure

```text
FAILED tests/test_report.py::test_may_report_matches_golden
AssertionError: assert csv_output == golden_content
  - 2026-05-12,Jarir,office,189.00,SAR,sample-04.pdf
```

Don't tell the room what's wrong. Ask:

> *"What's the failure telling us?"*

Wait for an answer. Someone in the room — often a salesperson, not a developer — will say *"the golden file is missing a row."* That's the moment the workshop unlocks: a non-developer just read a test failure correctly.

## Step 3 — Paste the failure into Claude

Verbatim. Don't paraphrase. Don't summarise.

```text
The test test_may_report_matches_golden is failing with this diff:

  - 2026-05-12,Jarir,office,189.00,SAR,sample-04.pdf

Investigate whether the issue is in the golden file or in our report
output. Do not guess. Read both files. Tell me what you find, then
propose a fix.
```

Claude will read `tests/golden/may.csv` and the actual report output, find that the golden file is the one missing a row, and propose regenerating the golden — but only after asking for confirmation, because the `CLAUDE.md` says: *"if and only if the spec change was intentional — and tell me in the plan before regenerating golden files."*

That last bit is the discipline. Golden files don't get "fixed" on a hunch.

## Step 4 — Re-run

```bash
pytest tests/ -v
```

Green. Hold the moment. This is the entire workshop in 30 seconds: structured intent produced code, a test produced a failure signal, the failure signal produced a targeted fix, the test produced a confirmation.

## The three layers of verification (talk through, 3 minutes)

**Layer 1 — Deterministic golden tests.** The CSV matches the golden file or it doesn't. No human judgment. These tests never call Claude or the internet — they use pre-recorded responses stored in `tests/fixtures/`. A setup file called `conftest.py` swaps the real Claude API for these recordings before any test runs, so tests are fast, free, and produce the same result every time.

**Layer 2 — Schema validation.** Every receipt extraction passes through a strict format check. If Claude returns a negative price, a date in the wrong format, or a spending category that isn't in the approved list, the check rejects it before it touches the database — like a strict receptionist who won't file a form with missing or invalid fields, regardless of how confidently it was submitted.

**Layer 3 — Optional LLM-as-judge.** A 30-line script that asks a separate Claude call: *"Given this receipt, is the assigned category correct? Answer PASS or FAIL."* Binary, not a 1–5 scale. Hamel Husain — one of the leading practitioners of LLM evaluation, and the source of the eval thinking in this workshop — is direct: binary scoring is reliable, scales produce noise. We don't run this in the workshop — but the file is in the repo as a starting point for anyone who wants to add it.

## What to call out from the front of the room

> *"Prompts come and go. Models change. The eval suite is the asset that compounds. If you remember nothing else from today, remember that the verification harness is the product."*

## Outputs from this block

- Every attendee has watched a real test fail with a real diff.
- Every attendee has pasted the failure into Claude and watched it diagnose.
- Every attendee has run `pytest tests/` and seen all green.
- The three layers of verification are named and understood.

[← Back to home](index.html)
