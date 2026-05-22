# Block 6 — Wrap

**Time:** 01:50 – 02:00
**Goal:** Close cleanly. Every attendee names one thing they'll do differently. The room remembers what it just built and why.

## The shape

| Time | Activity |
|---|---|
| 01:50 – 01:55 | One-line takeaways from around the room. |
| 01:55 – 01:58 | The four files that mattered. |
| 01:58 – 02:00 | Where to read next. Open Q&A while people finish coffee. |

## Takeaways — go around the room

Read aloud:

> *"In one sentence: what's the thing you're going to do differently the next time you open Claude?"*

No editorialising. Just listen. Most answers will land in one of three buckets:

- *"I'm going to write a PRD before I prompt."*
- *"I'm going to use Plan Mode."*
- *"I'm going to actually write a test."*

That's the workshop. If a third of the room says one of those three things, the session worked.

## The four files that mattered

Hold this slide (or page in the handout) up:

```
PRD.md
CLAUDE.md
.claude/commands/plan.md
tests/test_report.py
```

> *"Everything you did today rotates around these four files. The PRD says what we're building. The `CLAUDE.md` says how this codebase prefers to work. The plan command says think before you type. The test says you're not done until I am green. That's the whole methodology. Steal it for the next thing you build."*

## Where to read next

Point at three things, no more:

1. **Anthropic's official Claude Code Quickstart** — `code.claude.com/docs/en/quickstart`.
2. **Hamel Husain's "Your AI Product Needs Evals"** — `hamel.dev/blog/posts/evals/`. The single best 30-minute read on verification.
3. **Boris Cherny + Alex Albert, "A conversation on Claude Code"** — YouTube, ~21 minutes. The creator of Claude Code on how he uses it.

These three things, together, are about 90 minutes of reading and watching. That's a Saturday morning. Encourage it.

## Open Q&A — until coffee is finished

Take any question that didn't fit earlier. Some that will land here:

- **"What about Cursor / Windsurf / Aider?"** Same workflow, different chrome. The discipline is the same.
- **"How do I convince my team?"** Show them the test going green. Don't argue.
- **"What models do I use for what?"** Sonnet for the build, Opus for the planning of anything ambitious, Haiku for cheap and fast. Switch with `/model`.
- **"How much will this cost me in API calls?"** Pro covers it for projects this size. The 5-hour rolling window is the real constraint, not dollars.

If a question is too big — *"how do I build my company's internal RAG?"* — defer to follow-up. *"That's a different workshop. Come to the next one."*

## The send-off

Read aloud, then stop:

> *"You came in this morning with a chat tab. You're leaving with a CLI that has state, tests, and a workflow. From Pandan Labs — go build something."*

Photos. Done.

## Outputs from this block

- Every attendee has spoken one sentence aloud.
- Every attendee leaves with three reading recommendations.
- The room has a shared memory of the four files that anchored the work.

[← Back to home](index.html)
