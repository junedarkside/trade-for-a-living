---
title: TFEX Market Structure
type: concept
status: learning
tags: [futures, options, derivatives, market/thailand]
aliases: [TFEX, Thailand Futures Exchange, SET Derivatives]
---

# TFEX Market Structure

**TFEX** = **Thailand Futures Exchange**, part of the SET group. It is the
Thai venue for listed derivatives on Thai underlyings. Every Thai-market
strategy in this vault ([[Futures — Basics|futures]], [[Options — Basics|options]],
multi-leg, vol-selling) executes here.

## Core products

| Product | Underlying | Settlement | Notes |
|---------|-----------|------------|-------|
| **S50 futures** | SET50 Index | **Cash** to SET50 close | Workhorse Thai large-cap directional / hedge tool |
| **S50 options** | SET50 Index | **Cash**, European-style | Index options, [[Volatility Risk Premium\|VRP]] harvesting |
| **Single-stock futures (SSF)** | Major SET names | Physical (1,000 shares) | Listed on selected large-caps |
| **Single-stock options** | Selected SET names | Physical, American-style | Availability varies |
| **USD/THB futures** | FX | Physical (USD) | Currency exposure / carry |
| **Gold / oil / agri futures** | Commodities | Physical or cash per spec | Smaller liquidity |
| **Sector index futures** | Sector baskets | Cash | For sector rotation |

> Always confirm current product lineup on the TFEX website — additions and
> removals happen.

## Trading mechanics

- **Exchange-traded, centrally cleared.** All contracts standardised.
  Counterparty risk sits with the TFEX clearinghouse — not your broker's
  broker's hedge fund.
- **Trading hours.** Day session + (for most contracts) an evening / night
  session. S50 and S50 options have the longest hours; SSF follows the SET
  cash session. Exact hours per product — check TFEX rulebook.
- **Participants.** Local brokers, proprietary traders, institutions (asset
  managers, insurance, mutual funds), retail via brokers, foreign via licensed
  intermediaries.
- **Settlement.**
  - Index products → **cash-settled** to official index close on expiry.
  - Single-stock products → physical delivery per contract specs.
  - USD/THB → physical FX delivery.
  - See [[Settlement]] for cadence (T+2 spot, daily MTM futures, expiry
    options).

## Contract specs you must check per product

| Spec | Why it matters |
|------|---------------|
| **Tick size** | Minimum price increment. Wrong tick = rejected orders. See [[Tick Size]]. |
| **Tick value** | Tick size × multiplier = money per tick. S50 = ฿2 / contract. |
| **Contract multiplier** | S50 = ฿200 / index point. SSF = 1,000 shares. USDTHB = ฿500,000 notional. |
| **Expiry cycle** | Monthly, quarterly, weekly — affects premium and time decay. |
| **Margin (IM / MM)** | Determines capital required. See [[Margin Mechanics]]. |
| **Daily price limit** | Cap on intraday move; halt trigger if hit. |
| **Exercise style** | American vs European — see [[Assignment]]. |
| **Last trading day** | When you can no longer open/close the contract. |

Specs change. **Re-check before sizing any new strategy.**

## Market-microstructure notes for Thai traders

- **Index arbitrage** links SET50 spot basket to S50 futures. Basis (see
  [[Basis]]) sits within the cost-of-carry band; divergences = trade.
- **OI clusters** in S50 options act as support / resistance — see
  [[Options Chain]] for the read.
- **Foreign flow** is meaningful on S50; large foreign trades can move the
  near contract. Track via SET / TFEX daily reports.
- **Cash settlement at expiry** means S50 short / long positions **do not
  force delivery** of a basket — they cash out. Practical for portfolio
  hedging without unwanted stock delivery.

## Common strategy applications

- **Directional S50** — long/short S50 futures for SET50 view.
  - See [[Futures — Basics]] for mechanics.
- **S50 vol-selling** — short OTM S50 options ([[Covered Call]] on long
  futures, short strangle, [[Iron Condor]]) harvesting [[Volatility Risk
  Premium|VRP]].
- **Portfolio hedging** — short S50 futures against long SET stock book;
  ratio depends on beta and target beta (see [[Delta-Neutral Hedging]]).
- **Single-stock carry** — SSF to capture basis (rare) or short equity hedge.
- **FX overlay** — USD/THB futures to hedge baht exposure on foreign holdings.

## Related

- [[Futures — Basics]] · [[Options — Basics]] · [[Options Strategy]] ·
  [[Margin Mechanics]] · [[Settlement]] · [[Tick Size]] · [[Board Lot]] ·
  [[NVDR]] · [[Spot — Basics]] · [[Basis]] · [[Contango]] · [[Backwardation]]

## Sources

[^1]: `raw/iv-and-market-mechanics.md` (section 4).
[^2]: TFEX — product specifications and rulebook (current edition).
[^3]: SET — derivatives market overview.
[^4]: AQR — Understanding the Volatility Risk Premium (TFEX / SET50 context).
