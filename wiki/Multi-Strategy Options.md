---
title: Multi-Strategy Options
type: concept
status: learning
tags: [options, derivatives, risk, market/thailand]
---

# Multi-Strategy Options

**Multi-strategy options** = running several distinct options strategies at once
(or switching between them) to match your market view, risk tolerance, and
capital. Most pros combine **multi-leg** building blocks into a multi-strategy
portfolio.[^1]

## Multi-leg vs multi-strategy

| | Multi-leg | Multi-strategy |
|---|-----------|----------------|
| What | One trade, 2+ option legs | Many distinct trades running in parallel |
| Example | [[Vertical Spread]], [[Iron Condor]], [[Butterfly Spread]] | Covered calls + condors + straddles across a book |
| Purpose | Define risk/reward, cut cost, target a scenario | Diversify P&L drivers, smooth returns |

You need both: legs are the atoms; the multi-strategy book is the molecule.

## Building-block families

| Family | Blocks | Role |
|--------|--------|------|
| **Directional** (moderate move) | [[Vertical Spread\|bull call / bull put / bear put / bear call spreads]] | Cheap, defined-risk directional bets |
| **Volatility / event** | [[Long Straddle]], [[Strangle\|long strangle]] | Long convexity into catalysts |
| **Range-bound / income** | [[Covered Call]], [[Cash-Secured Put]], [[Iron Condor]], [[Iron Butterfly]], [[Butterfly Spread]] | Collect premium in quiet markets |
| **Hedge** | [[Protective Put]], [[Collar]] | Define downside on holdings |

## Portfolio-level example (Thailand)
A SET/SET50 book might run simultaneously:
- **Covered calls** on long Thai tourism stocks → income.
- **Cash-secured puts** on names you'd buy on a dip → funded entry.
- **Iron condors** on SET50 → range income.
- **Long straddles** before earnings / policy events → vol speculation.

Each leg of the portfolio answers a different question; together they diversify
*why* you make or lose money.[^1]

## Dynamic / regime switching
Rather than one fixed approach, deploy the strategy that fits the regime:[^3]
- **High IV / event-rich** → tilt to long vol (straddles/strangles); trim short premium.
- **Low IV / trending** → directional spreads.
- **Range-bound / high IV** → iron condors, covered calls (sell the richness).

Signals can be systematic (RSI, Bollinger, volume) with an options overlay: sell
OTM when IV high + theta favorable; buy OTM when expecting vol expansion.[^3]

## Why multi-strategy
- **P&L diversification** — trend vs mean-reversion vs vol drivers are uncorrelated.[^1]
- **Smoother returns** — short premium bleeding in a vol spike can be offset by
  long-vol gains.[^1]
- **Capital efficiency** — split capital across risk profiles (conservative income
  vs aggressive directional).[^4]

## Design framework
1. **Define views** — direction, volatility regime, horizon.
2. **Assign roles** — income / directional / vol-event / hedge (families above).
3. **Size each book** — e.g. 50% income, 30% directional, 20% vol/event.
4. **Monitor & rotate** — vol spike → cut short premium, add long vol; calm trend
  → favor directional + income.

## Related
- [[Options Strategy]] (single-strategy selection) · [[Options Chain]] (strike
  picker) · [[Greeks]] (book-level risk = sum of leg Greeks) · every building
  block above.
- [[Risk Management]] (position sizing, leverage control, scenario testing across the book).
- [[Options Risk Management]] (sizing formula, exit rules, hedging toolkit) ·
  [[Pre-Trade Checklist]] (one-page reference).

## Sources
[^1]: `raw/multi-strategy-options.md`
