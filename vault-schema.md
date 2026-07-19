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
3. **Max Loss** — formula + whether capped. **Always state max loss explicitly** before max profit (risk-first principle).
4. **Max Profit** — formula + whether capped.
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
| PPF | Protective Put on Future |
| CCF | Covered Call on Future |
| PCSF | Protective Call on Short Future |
| CPSF | Covered Put on Short Future |
| FC | Futures Collar |
| RR | Risk Reversal |
| SynF | Synthetic Futures |
| PCP | Put-Call Parity |
| USDTHB | USD/THB Futures |
| S50 | SET50 Futures |
| S50C | SET50 Options (call) |
| S50P | SET50 Options (put) |
| MLO | Multi-Leg Order |
| BM | Black Model |
| DNH | Delta-Neutral Hedging |
| PM | Portfolio Margin |
| C | Contango |
| B | Backwardation |
| RY | Roll Yield |
| Bs | Basis |
| Cal | Calendar Spread |
| Diag | Diagonal Spread |
| LC | Long Call |
| SC | Short Call |
| LP | Long Put |
| SP | Short Put |
| K, strike | Strike Price |
| Prem | Premium |
| ITM, ATM, OTM | Moneyness |
| EV, time-value | Intrinsic and Extrinsic Value |
| NVDR | Non-Voting Depository Receipt |
| TSD | Thailand Securities Depository |
| GTC | Good-Till-Cancelled |
| MTM | Mark-to-Market |
| SSF | Single-Stock Future |
| VRP | Volatility Risk Premium |
| RV | Realized Volatility |
| HV | Historical Volatility |
| GEX | Gamma Exposure |
| IM | Initial Margin |
| MM | Maintenance Margin |
| OI | Open Interest |
| GTC | Good-Till-Cancelled |
| TSD | Thailand Securities Depository |
| Δ, delta | Delta |
| Γ, gamma | Gamma |
| Θ, theta | Theta |
| ν, vega | Vega |
| ρ, rho | Rho |
| GiP | Greeks in Practice |
| ORM | Options Risk Management |
| PTC | Pre-Trade Checklist |
| DH | Dynamic Hedging |
| OFA | Options Flow Analysis |
| UOA | Options Flow Analysis |
| Flow Analysis | Options Flow Analysis |
| PCR | Options Flow Analysis |
| EE | Edge & Expectancy |
| Expectancy | Edge & Expectancy |
| SSFw | Strategy Selection Framework |
| Regime Matrix | Strategy Selection Framework |
| Exec | Execution & Slippage |
| Slippage | Execution & Slippage |

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
