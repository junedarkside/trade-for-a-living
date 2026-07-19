# Trade For A Living — Vault Rules

Obsidian + [obsidian-llm-wiki (olw)](https://github.com/kytmanov/obsidian-llm-wiki-local)
knowledge base for learning derivatives (spot / futures / options) toward
professional trading. Thailand market focus (SET, SET50, TFEX) by default.

## Directory contract

| Folder | Purpose | Edit policy |
|--------|---------|-------------|
| `raw/` | Source notes — web clips, book notes, your writeups | **Immutable.** Add freely; never rewrite olw-ingested notes. |
| `wiki/` | Compiled concept articles | Hand-edits OK and **preserved** by olw on recompile. Don't blindly overwrite — olw may have newer drafts. |
| `wiki/.drafts/` | Pending review | Don't hand-edit; use `olw review`. |
| `wiki/sources/`, `wiki/queries/`, `wiki/synthesis/` | olw-generated | Auto-managed; safe to read, don't hand-author. |
| `vault-schema.md` | LLM context for compile | Edit to change article conventions. |
| `wiki.toml` | olw config | Edit then `olw compile --force` to apply. |
| `.olw/` | Runtime DB, locks, compare reports | **Never touch.** Ask user before any change. |

## Naming

- `raw/` notes: `kebab-case.md` (`options-strategies-overview.md`).
- `wiki/` articles: Title Case (`Covered Call.md`) — matches olw concept naming.
- One concept per article (see `vault-schema.md`).

## Frontmatter (hand-authored / seed notes)

```yaml
---
title: Covered Call
type: strategy        # strategy | concept | greek | reference | glossary
status: learning      # learning | reviewed | mastered
tags: [options, strategy/income, market/thailand]
---
```
olw adds its own metadata fields to compiled articles — don't strip them.

## Tags

`#spot` `#futures` `#options` `#derivatives`
`#strategy/income` `#strategy/hedge` `#strategy/speculation`
`#greek/delta` `#greek/gamma` `#greek/theta` `#greek/vega` `#greek/rho`
`#risk` `#market/thailand` `#status/learning|reviewed|mastered`

## Links

- Obsidian wikilinks: `[[Covered Call]]`, `[[Delta]]`.
- Every strategy article links its instrument + relevant Greeks + sibling strategies.
- Every concept article links back to source `raw/` notes via `[^n]` footnotes.

## Working in this vault (Claude guidance)

- **Claude processes notes by hand** (olw pipeline is optional, see `wiki.toml`).
- New source material → drop in `raw/` (kebab-case) → tell Claude **process** / **ingest** (see SOP below).
- Fix/expand a concept → edit `wiki/<Article>.md` directly.
- Don't run `olw` commands unless the user explicitly asks — they're interactive and need a provider.
- Before deleting or moving any `wiki/` article, grep for backlinks first.
- Risk-first: when describing a strategy, state max loss before max profit.

## Ingest workflow

- New notes → drop in `raw/`, then run **`/ingest`** (or say "process" / "ingest").
- Skill: `.claude/skills/ingest/SKILL.md` — runs the 10-step SOP, reads
  `vault-schema.md` for templates/taxonomy/aliases.

## See also

- `vault-schema.md` — full domain conventions (injected into olw compile prompts).
- `README.md` — setup & daily workflow for the human user.
