# Getting Real with Claude Code

A 2-hour, coffee-shop-friendly Claude Code workshop for builders ready to move past the chat box.

**Live site:** `https://thepandanlabs.github.io/claude-code-workshop/`
**Audience:** Mixed-skill (ex-techies, PMs, BDMs, some developers). Workshop run in English.
**Anchor project:** `receipts` — a Python CLI that extracts structured data from a folder of receipt files, maintains a SQLite ledger, and emits deterministic CSV reports.
**Pedagogy:** structured intent (PRD + `CLAUDE.md` + Plan Mode) plus a small verification harness, demonstrated by experience rather than asserted.

From Pandan Labs with ♥.

## Running locally

```bash
git clone https://github.com/thepandanlabs/claude-code-workshop.git
cd claude-code-workshop

# Any static HTTP server works
python3 -m http.server 8080
# or
npx http-server -p 8080 -c-1

# Open in browser
open http://localhost:8080
```

That's it. No build step. The site is plain HTML + Tailwind via CDN + marked.js + highlight.js. Markdown files load on demand.

## Project structure

```
claude-code-workshop/
├── index.html                          # Landing page
├── viewer.html                         # Markdown renderer (?file=path.md)
├── README.md                           # This file
├── days/                               # The six workshop blocks
│   ├── block-01-setup-and-thesis.md
│   ├── block-02-structured-intent.md
│   ├── block-03-plan-build.md
│   ├── block-04-verify.md
│   ├── block-05-pick-track.md
│   └── block-06-wrap.md
├── resources/                          # Templates, demos, references
│   ├── how-claude-code-works.md
│   ├── prerequisites.md
│   ├── seed-repo.md
│   ├── ksa-payments.md
│   ├── prd-template.md
│   ├── claude-md-template.md
│   ├── bad-vs-good-prompts.md
│   ├── plan-mode.md
│   ├── eval-harness.md
│   ├── facilitator-notes.md
│   └── further-reading.md
├── tracks/                             # Post-workshop extension tracks
│   ├── track-a-cli.md
│   ├── track-b-web.md
│   ├── track-c-agent.md
│   └── track-d-mcp.md
├── appendix/
│   └── gcc-reskin.md                   # Future-workshop sketch
├── .nojekyll                           # GitHub Pages: don't run Jekyll
└── scripts/
    └── verify-links.sh                 # Sanity check that all linked files exist
```

## Deploying to GitHub Pages

This site is configured for GitHub Pages from the `main` branch.

1. **Create the repo** at `github.com/thepandanlabs/claude-code-workshop`.
2. **Push this directory** to the new repo:

   ```bash
   git init
   git add .
   git commit -m "Initial workshop site"
   git remote add origin git@github.com:thepandanlabs/claude-code-workshop.git
   git branch -M main
   git push -u origin main
   ```

3. **Enable Pages** in the repo settings:
   - Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main` / `(root)`
   - Save

4. **Wait ~2 minutes.** The first deploy lives at `https://thepandanlabs.github.io/claude-code-workshop/`.

5. **Verify deployment:** Actions tab → look for "pages build and deployment" → green check = live.

Every subsequent push to `main` redeploys automatically.

## Updating content

```bash
# Edit any markdown file in days/, resources/, tracks/, or appendix/
vim resources/eval-harness.md

# Test locally
python3 -m http.server 8080
# Visit http://localhost:8080/viewer.html?file=resources/eval-harness.md

# When happy, commit and push
git add resources/eval-harness.md
git commit -m "Clarify Layer 3 LLM-as-judge example"
git push
# Live in ~2 minutes
```

Adding a new resource card to the landing page:

1. Create the markdown file under the right folder (`resources/`, `tracks/`, etc.).
2. Open `index.html`.
3. Find the relevant `<section>` and copy an existing card.
4. Update the title, description, and `viewer.html?file=...` href.
5. Test locally. Push.

## Workshop materials versioning

The current version is **v1.0 — Riyadh edition (May 2026)**.

Future revisions should land in a sibling folder (e.g. `revisions/20260601/`) before being merged.

## Design system

Design palette:

- **Primary orange:** `#D17D59`
- **Dark background:** `#262624`
- **Card background:** `#2e2e2c`
- **Border:** `hsl(240 3.7% 15.9%)`
- **Foreground:** `hsl(0 0% 98%)`

Font stack: system fonts (`-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, ...`). Monospace for the ASCII logo and code blocks.

## Sanity check links

```bash
bash scripts/verify-links.sh
```

Confirms every `viewer.html?file=...` link in `index.html` points to an existing markdown file.

## Credits

- **Verification pyramid pedagogy:** Cole Medin's [ai-transformation-workshop](https://github.com/coleam00/ai-transformation-workshop).
- **Spec-driven scope discipline:** Beck Source's [inventory-management](https://github.com/beck-source/inventory-management).
- **Eval thinking:** Hamel Husain's posts on `hamel.dev/blog`.
- **Plan Mode workflow:** Boris Cherny, creator of Claude Code.
- **Coffee:** Brew92, Camel Step, Half Million — Riyadh.

## License

The workshop content is MIT-licensed. Run this workshop in your own city. Tell us how it went.

From Pandan Labs with ♥.
