---
title: Dynamic Hedging
type: concept
status: learning
tags: [options, derivatives, greek/delta, greek/gamma, risk]
---

# Dynamic Hedging

**The operational practice of continuously rebalancing a hedge (usually with
the underlying or futures) to keep an options position delta-neutral as the
market moves.** How professional traders and dealers isolate volatility risk and
manage non-linear exposure.

Companion to [[Delta-Neutral Hedging]] (theory + position-Greek framework).
This article is the **operational playbook** — worked mechanics, rebalancing
rules, gamma scalping, costs/risks, retail implementation.

## Overview
- Hold an options position with some [[Delta]] (directional exposure).
- Take an opposite position in the underlying (stock, index, or futures) so
  **total delta ≈ 0**.
- As underlying moves, option delta changes ([[Gamma]] effect).
- **Rebalance** the hedge: buy or sell more underlying to bring net delta back
  to zero.
- Repeated adjustment = "dynamic" (vs. a static hedge you set once).

## Why traders do it

| Trader type | Goal | Resulting P&L depends on |
|-------------|------|---------------------------|
| **Market makers / dealers** | Neutralize directional risk from large short-option books | Realized vs. implied vol; hedging costs |
| **Vol traders** | Isolate volatility or time-decay bets; gamma scalping | Vol regime + path of underlying |
| **Directional traders** | Reduce large directional losses while keeping convexity | Mostly gamma + path, less delta |

In all cases, the **result is a transformed risk profile**: less directional,
more vol/path-dependent.

## Worked mechanics

Setup: buy 10 calls, each delta = **0.40**, contract size 100 shares.

**Initial delta**:
```
Δ_total = 10 × 0.40 × 100 = +400
```
→ **Short 400 shares** (or equivalent futures) to be delta-neutral.

**Underlying rises — delta goes from 0.40 → 0.55**:
- New delta = 10 × 0.55 × 100 = +550.
- Need short 550; was short 400 → **sell 150 more shares**.

**Underlying falls — delta goes from 0.40 → 0.30**:
- New delta = 10 × 0.30 × 100 = +300.
- Need short 300; was short 400 → **buy back 100 shares**.

"Sell into strength, buy into weakness" — the essence of **gamma scalping** for
long-option holders.

## What it does (and doesn't) hedge

### Targets
- **Delta risk** — first-order sensitivity to underlying moves.
- **Gamma risk** — partially, via frequent rebalancing (more frequent → closer
  to continuous hedging).

### Does NOT eliminate
- **[[Vega]] risk** — IV changes still hit P&L.
- **[[Theta]] risk** — time decay continues.
- **Higher-order risks** — vanna, volga, jump risk, gap risk.
- **Transaction cost risk** — frequent trading erodes profits.

Dynamic hedging **transforms** your risk profile; it doesn't make the position
risk-free.

## Link to options pricing theory

Central to [[Black Model]] / Black-Scholes:
- The model assumes you can form a **replicating portfolio** — underlying +
  risk-free asset, continuously rebalanced to match the option's payoff.
- If dynamic replication is possible and markets are arbitrage-free, the
  option's **fair price = cost of maintaining the replicating portfolio**.

This is why dealers price options as **volatility products**, not directional
bets. Implied vol reflects the market's view of future realized vol plus
hedging costs.

## Implementation choices

### Rebalance triggers (pick one or combine)
- **Threshold**: net delta exceeds ±0.05 or ±0.10 (or ±X% of notional).
- **Move-based**: underlying moves by ±2% or N ticks.
- **Time-based**: end of day, every X hours, every X minutes.
- **Continuous**: theoretical only.

### Frequency trade-off

| Frequency | Hedging error | Transaction cost | Delta drift |
|-----------|---------------|------------------|-------------|
| More often | Lower | Higher | Smaller |
| Less often | Higher | Lower | Larger |

Choose based on:
- Liquidity / transaction costs.
- **Gamma of the position** (higher gamma → rebalance more often).
- Tolerance for delta drift.

## Gamma scalping (the classic dynamic-hedge strategy)

**Setup**: long [[Long Straddle]] / strangle (or any long-gamma position) +
dynamically delta-hedge with the underlying.

**Mechanics**:
- Price rises → net delta positive → **sell underlying**.
- Price falls → net delta negative → **buy underlying**.
- Oscillating underlying → repeatedly **buy low, sell high**.

The scalping profits can offset [[Theta]] decay and potentially generate net
profit even if the underlying ends where it started.

**Key risks**:
- Strong directional move → fewer mean-reversion trades → scalping fails.
- Transaction costs eat profits (especially in high-gamma short-dated options).
- [[Vega|Vega crush]] still hurts long vega positions even with good scalping.

## Costs and risks

### Transaction costs
Each rebalance incurs:
- Commissions/fees
- Bid-ask spread
- Market impact (large orders move the market)

In high-gamma, short-dated positions → frequent rebalancing → costs matter a lot.

### Jump and gap risk
- Dynamic hedging assumes relatively continuous prices.
- Reality: markets gap on news, earnings, macro data.
- Cannot rebalance at expected prices → large hedging errors, especially for
  short options.

### Model and parameter risk
- Delta depends on model inputs (vol, rates).
- Wrong model or vol estimate → "delta-neutral" isn't actually neutral → hidden
  directional risk.

## Dynamic vs. static hedging

| | Static hedge | Dynamic hedge |
|---|--------------|----------------|
| Setup | Set once | Actively adjusted |
| Adjustments | Manual | Threshold/continuous |
| Cost | Lower | Higher |
| Complexity | Simpler | More complex |
| Delta control | Drifts with market | Stays near zero |

**Professionals combine both**:
- **Static** (spreads, collars) to limit extreme risk.
- **Dynamic** to fine-tune delta day-to-day.

## Practical steps for advanced retail

1. **Start with simple delta hedging** — compute net delta of the options book,
   hedge with underlying/futures to bring net delta ≈ 0.
2. **Define rebalancing rules** — threshold (e.g., ±0.10 per option OR ±X%
   notional), move-based (±2%), or time-based (EOD).
3. **Track performance** — record options P&L, hedge-trade P&L, transaction
   costs. Analyze whether frequency/thresholds are optimal.
4. **Be cautious with short gamma** — short straddles/strangles + dynamic hedging
   is dangerous in fast markets (negative gamma → buy high, sell low). Many
   experienced traders avoid dynamically hedging large short-gamma books.

## Related
- [[Delta-Neutral Hedging]] (theory + position-Greek framework) ·
  [[Position Greeks]] (Taylor expansion, position-Greek formulas) ·
  [[Greeks in Practice]] (trader-focused Greek framework) ·
  [[Delta]] · [[Gamma]] · [[Theta]] · [[Vega]] ·
  [[Black Model]] (pricing/replication theory) ·
  [[Long Straddle]] (gamma scalping setup) ·
  [[Risk Management]] · [[Options Risk Management]] · [[Pre-Trade Checklist]]

## Sources
[^1]: `raw/dynamic-hedging.md`
[^2]: pomegra.io — chapter 8: hedging with options / dynamic hedging.
[^3]: medium.com / FMZQuant — Deribit options delta dynamic hedging strategy.
[^4]: youtube.com/watch?v=Q_Qrw-OH6yE — dynamic hedging + Black-Scholes link.
[^5]: academic.oup.com — dynamic hedging (Hull-style text).
[^6]: cs.uwaterloo.ca — transaction costs in dynamic hedging.