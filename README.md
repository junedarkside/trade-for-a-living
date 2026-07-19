# Trade For A Living

Personal knowledge base for learning **derivatives trading** — spot, futures,
options — and progressing toward professional, risk-first trading. Thailand
market focus (SET, SET50, TFEX) by default; market-neutral explanations throughout.

**How it works:** drop raw notes in `raw/`, tell Claude **process** / **ingest**,
and Claude turns them into structured, interlinked `wiki/` articles following a
fixed playbook. (An optional `olw` auto-compiler exists — see the bottom — but it
is not required.)

---

## Open in Obsidian

1. Open Obsidian → **Open folder as vault**.
2. Select `trade-for-a-living/`.
3. Start at `wiki/index.md` (or `wiki/Options Strategy.md`).

Graph-view filter (paste into the graph filter bar) — hides raw sources and the
index so the concept graph stays clean:

```
-path:raw -path:wiki/sources -path:wiki/.drafts -path:_resources -file:index
```

---

## Daily workflow

1. **Drop** any note (web clip, book note, your writeup) into `raw/`.
2. **Tell Claude** *"process"* / *"ingest"* (or *"process `<file>`"*).
3. Claude runs the [Ingest SOP](CLAUDE.md) — classifies, normalizes frontmatter,
   writes the `wiki/` article(s) from the template, tags, cross-links, updates
   `wiki/index.md`, and appends a row to `wiki/log.md`.
4. **Review** the new article in Obsidian; refine wording anytime — Claude
   preserves your edits on the next pass.

That's it. No background services, no model install.

### Seed content already present

`raw/` source notes:
- `options-strategies-overview.md` — core options strategies reference.
- `options-basics.md` — calls, puts, strike, expiration, ITM/ATM/OTM.
- `greeks-overview.md` — delta, gamma, theta, vega, rho.
- `futures-basics.md` — contract specs, margin, contango/backwardation.
- `spot-basics.md` — cash market, order types.

`wiki/` articles (hand-authored seeds, readable now):
- `Options Strategy.md`, `Greeks.md`, `Strategy Payoff Table.md`, `Covered Call.md`.

---

## Folder map

```
raw/        ← YOUR notes (immutable). Drop here, never rewrite.
wiki/       ← Compiled concept articles (one concept per file, Title Case).
  index.md  ← Navigation hub.
  log.md    ← Audit trail / "what's been processed".
  sources/ queries/ synthesis/ .drafts/  ← used only if olw is enabled.
vault-schema.md  ← Domain conventions + templates + tag taxonomy (source of truth).
CLAUDE.md        ← Vault rules + the Ingest SOP Claude follows.
wiki.toml        ← Config for the optional olw auto-compiler.
```

---

## Conventions

See [`vault-schema.md`](vault-schema.md) (templates, taxonomy, aliases) and
[`CLAUDE.md`](CLAUDE.md) (vault rules + full Ingest SOP).

Key points:
- One wiki article per concept / strategy / Greek.
- Risk-first: max loss stated before max profit.
- `[^n]` footnotes cite back to `raw/` source notes.
- Tags: `#options`, `#futures`, `#strategy/income|hedge|speculation`, `#greek/*`,
  `#market/thailand`, `#status/learning|reviewed|mastered`.

---

## Optional: olw auto-compile (advanced, not required)

The vault layout matches [obsidian-llm-wiki](https://github.com/kytmanov/obsidian-llm-wiki-local)
so you *can* swap Claude hand-processing for an automated local-LLM pipeline
later. Skip this entirely unless you want it.

```bash
pip install obsidian-llm-wiki                      # or: uv tool install obsidian-llm-wiki
ollama pull gemma4:e4b                             # https://ollama.com/download
olw setup                                          # pick provider/models
cd /Users/charuwatnaranong/Desktop/Fin/trade-for-a-living
olw init --existing .
olw run                # or: olw watch   (auto-process anything dropped into raw/)
```

Provider-flexible: Ollama (default, offline), Groq, LM Studio, vLLM, Azure, etc.
See `wiki.toml` for the `[provider]` block. If you enable olw, prefer its
`olw review`/`olw lint` over hand-editing `wiki/.drafts/`.

---

*Reference: [obsidian-llm-wiki-local](https://github.com/kytmanov/obsidian-llm-wiki-local)*
