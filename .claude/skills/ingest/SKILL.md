---
name: ingest
description: Ingest a raw note into the Trade For A Living Obsidian vault. Use when the user says "process", "ingest", "process <file>", or invokes /ingest. Classifies the note, normalizes/writes raw/ + wiki/ articles per vault-schema.md, tags, cross-links, updates index/log. Accepts an optional target file path as the argument.
---

# Ingest — raw note → vault article

CWD = vault root (`/Users/charuwatnaranong/Desktop/Fin/trade-for-a-living`).

`$ARGUMENTS` = optional target file (e.g. `raw/options-strategies-overview.md`).
If empty, scan `raw/` for any `.md` not yet recorded in `wiki/log.md`.

## SOP — run steps in order

1. **Find target.**
   - If `$ARGUMENTS` given → use that file.
   - Else → scan `raw/*.md`; pick any whose filename does not appear in `wiki/log.md`.
   - Process one file per invocation. If multiple unlogged files, ask which.

2. **Read + classify.**
   - Source material (web clip, book note, raw writeup) → stays in `raw/`, **kebab-case**.
   - Ready concept / strategy / Greek → promote to `wiki/`, **Title Case**.
   - Typical flow: source note remains in `raw/`; derived article(s) published to `wiki/`.

3. **Normalize the `raw/` note.**
   - Kebab-case filename.
   - Frontmatter: `title`, `type: source`, `tags`.
   - Web clips get `[^n]` source footnotes (URL, book chapter, etc.).

4. **Write/update `wiki/` article(s)** per `vault-schema.md`:
   - One concept per article.
   - Strategy → 12-section template (Overview → Legs → Max Profit → Max Loss →
     Breakeven → Greeks → Payoff → When to use → Risks → Example → Related → Sources).
     Max loss always stated before max profit.
   - Greek → Definition → sign convention → long-holder meaning → decay →
     practical use.
   - Frontmatter: `title`, `type` (strategy|concept|greek|reference|glossary),
     `status: learning`, `tags`, `aliases`.
   - Cite the `raw/` source via `[^n]` footnotes (Sources section).

5. **Tag strictly** from `vault-schema.md` taxonomy. Do not invent tags.

6. **Cross-link.**
   - Add `[[wikilinks]]` to existing concepts (grep `wiki/` titles + check `wiki/index.md`).
   - Add the new article to `wiki/index.md` under the correct section.
   - Update backlinks from sibling articles when relevant.

7. **Aliases.** If the note introduces a new short form (e.g. "iron condor" → IC),
   append it to the alias table in `vault-schema.md`.

8. **Dedupe/merge.** Grep `wiki/` for an existing similar concept first; if one
   exists, merge into it rather than creating a duplicate. Report any near-match.

9. **Log.** Append one row to `wiki/log.md` — `date | action | files touched`.

10. **Report.** Short summary to user: files created/updated, merge candidates,
    content gaps or red-links flagged.

## Pointers (do not duplicate — read at runtime)

- Templates + tag taxonomy + alias table → `vault-schema.md`
- Processed-set audit trail → `wiki/log.md`
- Always-current nav → `wiki/index.md`
- Frontmatter convention → `vault-schema.md` "Frontmatter" section

## Safety

- Do not delete or rename any `wiki/` article without grepping backlinks first.
- Do not modify `.olw/` runtime files. Ask user first.
- Do not run `olw` commands — they're interactive and need a provider.
