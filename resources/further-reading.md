# Further Reading

Curated. Current as of May 2026. Each link is something I'd send to a friend, not a comprehensive index.

## The official sources

- **Claude Code documentation** — `code.claude.com/docs`
- **Claude Code Quickstart** — `code.claude.com/docs/en/quickstart`
- **Claude Code Best Practices** — `code.claude.com/docs/en/best-practices`
- **Anthropic engineering blog** — `anthropic.com/engineering`
- **Anthropic Cookbook (now "Claude Cookbooks")** — `github.com/anthropics/claude-cookbooks`
- **Claude Code 101 free course** — `anthropic.skilljar.com/claude-code-101`
- **Pricing (Pro $20/month verified May 2026)** — `claude.com/pricing`
- **Supported countries (Saudi Arabia listed)** — `anthropic.com/supported-countries`

## On structured intent

- **"Best practices for Claude Code"** by Anthropic. Read it once. Then read it again after you've built three projects — different sentences land the second time.
- **"A conversation on Claude Code"** — Boris Cherny (the creator) and Alex Albert. YouTube, June 2025, ~21 minutes. Watch this. He describes the Plan Mode workflow in his own words: *"If my goal is to write a Pull Request, I will use Plan mode, and go back and forth with Claude until I like its plan. From there, I switch into auto-accept edits mode and Claude can usually 1-shot it. A good plan is really important."*

## On evals and verification

The canonical reading is Hamel Husain. Don't read everything — read these two, in order:

- **"Your AI Product Needs Evals"** — `hamel.dev/blog/posts/evals/`. Thirty minutes. Read first. Read once a quarter.
- **"Using LLM-as-a-Judge For Evaluation: A Complete Guide"** — `hamel.dev/blog/posts/llm-judge/`. Read second, when you start needing Layer 3 in your harness.

For a longer treatment: **"A Field Guide to Rapidly Improving AI Products"** (Hamel Husain, O'Reilly, July 2025). Two hours. Read when you're past your second project and want to invest in the workflow.

Also worth reading: **Anthropic Cookbook's `misc/building_evals.ipynb`** — code-based grading first, model-based grading second. The notebook walks through actual examples.

## On agents

- **"Building effective agents"** (Schluntz and Zhang, Anthropic, December 2024) — `anthropic.com/engineering/building-effective-agents`. The single best summary of the patterns: prompt chaining, routing, parallelisation, orchestrator-workers, evaluator-optimiser. Read before starting Track C.
- **"Building agents with the Claude Agent SDK"** (Anthropic, September 2025) — `anthropic.com/engineering/building-agents-with-the-claude-agent-sdk`. Useful context on why the SDK was renamed from "Claude Code SDK" and what shape it's converging toward.
- **Claude Agent SDK overview** — `code.claude.com/docs/en/agent-sdk/overview`. The current source of truth.

## On MCP

- **MCP spec home** — `modelcontextprotocol.io`
- **MCP TypeScript SDK** — `github.com/modelcontextprotocol/typescript-sdk`. v1.x is current stable as of May 2026; v2 docs are live at `ts.sdk.modelcontextprotocol.io/v2/` but v2 hasn't shipped as a stable npm release yet. Pin to v1 for the workshop's Track D.
- **MCP Python SDK** — `github.com/modelcontextprotocol/python-sdk`
- **Official MCP server registry** — `github.com/modelcontextprotocol/servers`

## Community deep-dives worth your time

- **"A Complete Guide to Claude Code — Here are ALL the Best Strategies"** by Cole Medin. YouTube, August 2025, ~50 minutes. Slash commands, MCP, PRP framework (Plan-Review-Prompt: a structured prompting workflow), subagents, hooks. The best single overview if you're past the first project.
- **Forrest Chang's "andrej-karpathy-skills" CLAUDE.md template** — `github.com/forrestchang/andrej-karpathy-skills`. Inspired by an Andrej Karpathy X post; ~70 lines. A useful comparison template.
- **The Claude Code Handbook** — freeCodeCamp. Comprehensive intro, free.

## Reference workshops (the ones this kit was calibrated against)

- **coleam00/ai-coding-summit-workshop-2** — `github.com/coleam00/ai-coding-summit-workshop-2`. A 2-hour live build with a poll/survey app.
- **coleam00/ai-transformation-workshop** — `github.com/coleam00/ai-transformation-workshop`. The PIV (Plan/Implement/Validate) pyramid is worth borrowing.
- **ssthakuraa/claude-code-workshop** — `github.com/ssthakuraa/claude-code-workshop`. The 4-day enterprise version with Spring Boot + React.
- **beck-source/inventory-management** — `github.com/beck-source/inventory-management`. A small, intentionally scarce example app for workshop extension.
- **Deway-AI/claude-code-pm-agents** — `github.com/Deway-AI/claude-code-pm-agents/blob/main/docs/architecture.md`. PM-agent architecture as a structured intent example.

## The reading order if you have one weekend

1. Watch **Cherny + Albert "A conversation on Claude Code"** (21 min).
2. Read **Hamel's "Your AI Product Needs Evals"** (30 min).
3. Read **Anthropic's "Best practices for Claude Code"** (20 min).
4. Watch **Cole Medin's "Complete Guide to Claude Code"** (50 min).
5. Pick one of the four extension tracks. Build it.

That's a Saturday. By Sunday evening, you have a project.

[← Back to home](index.html)
