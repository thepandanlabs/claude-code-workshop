# Free and Low-Cost Options for Claude Code

**You do not need a $20/month subscription to follow this workshop.**

All you need is an API key and SAR 20 of credit. That covers 50+ workshop sessions.

---

## The quick answer

Claude Code works in two modes:

1. **Linked to your Claude.ai account** (Pro plan, $20/month) — the default
2. **Linked to an API key** (pay-as-you-go) — what this page covers

Mode 2 requires no subscription. You create a free account at `console.anthropic.com`, add a small credit balance, and Claude Code works exactly the same way.

---

## Option 1: Anthropic API key — Recommended (~SAR 0.40 per session)

Full Claude Code functionality. Same experience as a Pro subscriber. Cost per 2-hour workshop session: $0.10–0.20 using Claude Haiku 4.5.

**Setup (5 minutes):**

1. Go to `console.anthropic.com` → create a free account
2. Click **API Keys** → **Create key** → copy the key
3. Add credit: **Billing** → **Add credits** → minimum $5 (covers 25–50 sessions)
4. Set the key in your terminal:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

Add that line to your `~/.zshrc` or `~/.bashrc` so it persists across sessions:

```bash
echo 'export ANTHROPIC_API_KEY=sk-ant-...' >> ~/.zshrc
source ~/.zshrc
```

5. Open Claude Code: `claude`

That's it. Claude Code will use Haiku 4.5 by default (cheap, fast). For longer or more complex sessions, specify a stronger model:

```bash
claude --model claude-sonnet-4-6
```

**For Saudi Arabia:** Anthropic fully supports KSA for API billing. No VPN needed. If your card is declined, try a Visa/Mastercard issued by a local bank or use a virtual card via your bank's app.

---

## Option 2: OpenRouter free models — Zero cost

OpenRouter is a model gateway that offers free daily quotas on several capable models including Google Gemini 2.5 Flash and DeepSeek. Claude Code can route through it using its base URL override.

**Limitations vs. Option 1:**
- Model quality is lower — adequate for spec-writing and basic Python, weaker on complex multi-file reasoning
- Rate limits apply (varies by model — typically 50–200 requests/day free)
- Plan Mode may behave slightly differently on some models
- Not all Claude Code features are guaranteed to work

**Setup (10 minutes):**

1. Go to `openrouter.ai` → sign up (free, no credit card needed)
2. **Keys** → **Create key** → copy it
3. In your terminal:

```bash
export OPENROUTER_API_KEY=sk-or-...
export ANTHROPIC_BASE_URL=https://openrouter.ai/api/v1
export ANTHROPIC_API_KEY=$OPENROUTER_API_KEY
```

4. Open Claude Code with a free model:

```bash
claude --model google/gemini-2.5-flash:free
```

Or add the model to your Claude Code settings so you don't have to specify it each time:

```bash
# In your project, create or edit .claude/settings.json:
{
  "model": "google/gemini-2.5-flash:free",
  "env": {
    "ANTHROPIC_BASE_URL": "https://openrouter.ai/api/v1"
  }
}
```

**Note:** OpenRouter free model availability changes. If `gemini-2.5-flash:free` isn't listed, check `openrouter.ai/models?q=free` for current free options.

---

## Option 3: Gemini CLI — Zero cost, different tool

Google's Gemini CLI is a free alternative that teaches the same methodology — write a spec, plan before coding, implement, verify. It is not Claude Code and the interface differs, but the discipline transfers 1:1.

If your goal is learning the workflow rather than specifically learning Claude Code, this is a solid zero-cost path.

**Setup:**

```bash
# Requires Node.js
npm install -g @google/gemini-cli
gemini auth   # prompts you to sign in with a Google account
gemini        # opens the CLI
```

Free quota: Gemini 2.5 Flash at 60 requests/minute, generous daily limit (covers a full 2-hour workshop comfortably).

---

## Cost comparison

| Option | Cost | Model quality | Setup | Full Claude Code? |
|---|---|---|---|---|
| Claude Pro subscription | $20/month | Sonnet / Opus | Already have it | Yes |
| Anthropic API key | ~$0.10–0.20/session | Haiku 4.5 | 5 min | Yes |
| OpenRouter free tier | $0 | Gemini 2.5 Flash | 10 min | Yes (with caveats) |
| Gemini CLI | $0 | Gemini 2.5 Flash | 5 min | No — different tool |

---

## Which option for which workshop?

| Workshop | Recommendation |
|---|---|
| Getting Real with Claude Code | API key — you're learning API patterns, so having a real key is part of the lesson |
| From Meetings to Decisions | API key — extraction + ledger work benefits from Claude's reasoning quality |
| Customer Intelligence & Pitch Suite | API key — complex extraction rules and pitch generation need Claude quality |
| Find Any Deal | Either — deals comparison works fine on Gemini via OpenRouter |

[← Back to home](../index.html)
