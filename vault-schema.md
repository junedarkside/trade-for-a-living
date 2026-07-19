# Vault Schema — Trading Knowledge Base

> This file is **LLM context**. `olw` injects it into the compile prompt so generated
> articles match this vault's domain and conventions. Edit freely — the next
> `olw compile` picks up changes. Keep it human-readable.

## Domain

Personal learning vault for **derivatives trading**: spot (cash equities), futures,
and options. Goal: build toward professional, risk-first trading. Primary market
focus is **Thailand (SET, SET50 index, TFEX)** with market-neutral explanations
and Thai examples called out where relevant.

## Concept granularity

One wiki article per discrete concept. Do NOT produce mega-articles.

- **One article per strategy**: Covered Call, Cash-Secured Put, Protective Put,
  Collar, Long Straddle, Vertical Spread (Bull Call Spread, Bear Put Spread), etc.
- **One article per Greek**: Delta, Gamma, Theta, Vega, Rho.
- **One article per instrument**: Options, Futures, Spot, plus sub-concepts
  (Strike Price, Expiration, Assignment, Margin, Contango, Backwardation).
- **Overview / index articles** (e.g. "Options Strategy", "Greeks") are allowed
  as navigation hubs that link the per-concept articles.

## Strategy article structure

Every strategy article follows this order:

1. **Overview** — one-paragraph plain-English description + market outlook it fits.
2. **Legs** — markdown table: `| Leg | Action | Type | Strike | Expiry |`.
3. **Max Profit** — formula + whether capped.
4. **Max Loss** — formula + whether capped. **Always state max loss explicitly.**
5. **Breakeven(s)** — formula(s).
6. **Greeks behavior** — net delta/gamma/theta/vega sign and how it evolves.
7. **Payoff shape** — short description or ASCII sketch at expiry.
8. **When to use** — outlook, volatility regime, objective (income/hedge/speculate).
9. **Risks** — early assignment, pin risk, gap risk, liquidity.
10. **Example** — concrete SET50 / SET stock illustration with sample strikes/expiry.
11. **Related** — `[[wikilinks]]` to instruments, Greeks, sibling strategies.
12. **Sources** — `[^n]` footnote references back to `raw/` notes.

## Greek article structure

Definition → mathematical sign convention → what a positive/negative value means
for a long holder → how it decays/changes over time and with spot → practical use
(hedging, position sizing, trade selection).

## Aliases (link repair)

Map short forms to canonical article names so broken `[[wikilinks]]` self-heal:

| Alias | Canonical |
|-------|-----------|
| SET50, S50, SET 50 Index | SET 50 Index |
| TFEX | Thailand Futures Exchange |
| CSP | Cash-Secured Put |
| CC | Covered Call |
| PP | Protective Put |
| OI | Open Interest |
| IV | Implied Volatility |
| IC | Iron Condor |

## Tag taxonomy

Hierarchical, lower-case, slash-nested:

- Instrument: `#spot`, `#futures`, `#options`
- Family: `#derivatives`
- Strategy class: `#strategy/income`, `#strategy/hedge`, `#strategy/speculation`
- Greek: `#greek/delta`, `#greek/gamma`, `#greek/theta`, `#greek/vega`, `#greek/rho`
- Risk: `#risk`
- Market: `#market/thailand`
- Lifecycle: `#status/learning`, `#status/reviewed`, `#status/mastered`

## Tone & principles

- **Risk-first.** Max loss stated before max profit. No strategy described as "safe".
- **Practitioner, not academic.** Explain why a trader would use it, not just the math.
- **Concise.** Prefer tables and bullets over prose walls.
- **Cite sources.** Every claim sourced from a `raw/` note gets a `[^n]` footnote.
- **Link liberally.** Every article links its instrument, relevant Greeks, and
  sibling concepts via `[[wikilinks]]`. No orphans.

## Frontmatter

olw-managed; do not strip. Seed/hand-authored articles use:

```yaml
---
title: Covered Call
type: strategy        # strategy | concept | greek | reference | glossary
status: learning      # learning | reviewed | mastered
tags: [options, strategy/income, market/thailand]
---
```
