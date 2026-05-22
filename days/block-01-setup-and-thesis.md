# Block 1 — Setup & The Thesis

**Time:** 00:00 – 00:20
**Goal:** Everyone has a working tool, knows the workshop's three claims, and has watched the bad-vs-good prompt demo land.

## What happens in this block

1. **00:00 – 00:05 — Soft start.** People settle in, order coffee, find power. No content. Late arrivals join.
2. **00:05 – 00:10 — Tool check.** Each attendee runs `claude --version` and `claude doctor`. The facilitator walks the room. Anyone broken gets paired with a working neighbour. Don't fix laptops now — fix at the break.
3. **00:10 – 00:15 — The three claims.** State them out loud, and explain each one:
   - **Structured intent beats clever prompting.** The model fills every gap with an assumption — language, schema, architecture, what "done" looks like. A `CLAUDE.md` and a one-page PRD fill those gaps before the first token of code is generated. Once they do, the good prompt can be *short*, because the structure carries the load. You'll see this in five minutes.
   - **Verification is what makes the demo real.** An eval is a saved input, the known-right answer, and an automated check that they match. Nothing more. That check turns "it looks right in the demo" into "the same behaviour is guaranteed on every input, every model update, every refactor." A demo that isn't tested is just a demo.
   - **Claude Code is a collaborator, not a wish-granting genie.** It arrived this morning with no context about your project. Given a clear brief — `PRD.md`, `CLAUDE.md`, a plan — it does exceptional work. Given a vague wish, it makes reasonable guesses that compound into a codebase you didn't want. The workshop teaches you to brief it, read the plan, and correct it via files.

   > **Before the session:** Share **[How Claude Code Works](viewer.html?file=resources/how-claude-code-works.md)** at T-24 hours. Attendees who read it arrive with the mental model in place; Block 1 reinforces it rather than introducing it cold.
4. **00:15 – 00:20 — The bad-prompt-vs-good-prompt demo.** Live, from the facilitator's laptop. Both prompts on the screen or in the handout. Run the bad one. Watch it produce something that compiles and is wrong. Stop. Don't rescue. Ask: *"What's missing?"* Wait for the answer.

## The script for the bad-vs-good demo

Open a fresh terminal in an empty folder. Run `claude`. Paste verbatim:

```text
build me a receipts tool
```

What you'll see: Claude infers a stack, picks a name, makes up a schema, drops a single Python file with everything in it, no tests, no `CLAUDE.md`, no PRD. It might even run. It will not be the thing you wanted, and you cannot tell why — because you never said what you wanted.

Stop. Open a new terminal in the seed repo (which has `PRD.md` and `CLAUDE.md` already). Activate Plan Mode with **Shift + Tab** twice. Paste:

```text
Read PRD.md and CLAUDE.md. Plan the minimum implementation that
satisfies the v0.1 acceptance criteria. Do not write code in this turn.
Produce a numbered plan listing the files you will create or modify,
in the order you will modify them, and the test you will run after
each step to verify. Stop after the plan and wait for my approval.
```

What you'll see: Claude reads both files, produces a 6–10 step plan that names the files it will touch in order, with a test gate after each step. Nothing is written to disk.

**The teaching beat:** the difference between these two prompts is not prompt engineering. It is the presence of `PRD.md`, `CLAUDE.md`, and Plan Mode. The good prompt is *short* because it can be — the structure carries the load.

## What to do if things go wrong

- **Wi-Fi craters during the demo.** Talk through both prompts from the printed handout instead. The point lands without a live run; the contrast is in the prompts themselves.
- **`claude` won't start for someone.** Pair them with a neighbour for now. Note their name. Fix at the break.
- **Someone interrupts to argue.** Welcome the disagreement. The argument *is* the thesis. Park it for Block 5 Q&A.

## Outputs from this block

- Every attendee can run `claude` and reach a prompt.
- Every attendee has seen, in a single room, the audible difference between a one-line prompt and a structured-intent prompt.
- The three claims are on the table.

[← Back to home](index.html)
