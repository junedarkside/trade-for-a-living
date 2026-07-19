---
title: Dynamic Hedging
type: source
tags: [options, derivatives, greek/delta, greek/gamma, risk]
---

# Dynamic Hedging

**Dynamic hedging** is the process of continuously adjusting a hedge (usually with
the underlying asset or futures) to keep an options position **delta-neutral** as
the market moves. It's how professional traders and dealers isolate **volatility
risk** and manage non-linear exposure from options.

Companion to `raw/futures-basics.md` (term structure), `raw/greeks-overview.md`
(theory), and `raw/greeks-trading-practice.md` (applied). Operational follow-up
to `raw/options-risk-management.md` (practical playbook).

## 1. Core idea in plain language

- You hold an options position that has some **delta** (directional exposure).
- You take an opposite position in the **underlying** (stock, index, or futures)
  so that **total delta ≈ 0**.
- As the underlying price moves, the option's delta changes (because of
  **gamma**).
- You **rebalance** the hedge: buy or sell more of the underlying to bring net
  delta back to zero.

This repeated adjustment is why it's called **dynamic** (vs. a static hedge you
set once and forget).

## 2. Why traders do dynamic hedging

### For market makers / dealers
- They often hold large books of short options.
- By dynamically delta-hedging, they:
  - Neutralize directional risk.
  - Turn their position into primarily a **volatility trade** (long or short
    vega/gamma).
- Their P&L then depends more on:
  - Realized vs. implied volatility
  - Hedging costs (transaction costs, slippage)

### For directional / vol traders
- To **isolate specific risks** — remove delta so you're mainly betting on
  volatility or time decay.
- To **reduce large directional losses** while keeping convexity (gamma) benefits.
- To implement **gamma scalping**:
  - Long options (positive gamma) + dynamic delta hedge.
  - Profit from "buy low, sell high" in the underlying as it oscillates.

## 3. Mechanics: a simple example

- Buy 10 call options. Each has delta = **0.40**. Contract size = 100 shares.

**Initial delta**:
```
Δ_total = 10 × 0.40 × 100 = +400
```
To be delta-neutral, **short 400 shares** (or equivalent futures).

### Underlying rises
- Call delta rises from 0.40 → 0.55 (gamma effect).
- New delta = 10 × 0.55 × 100 = +550.
- You were short 400; now need short 550.
- → **Sell an additional 150 shares** to re-hedge.

### Underlying falls
- Call delta falls from 0.40 → 0.30.
- New delta = 10 × 0.30 × 100 = +300.
- → **Buy back 100 shares** to re-hedge.

This "sell into strength, buy into weakness" is the essence of **gamma
scalping** when you're long options and dynamically hedged.

## 4. What dynamic hedging does (and doesn't) hedge

### It primarily targets
- **Delta risk** — first-order sensitivity to underlying moves.
- To some extent, **gamma risk** — by frequent rebalancing (more frequent →
  closer to continuous hedging).

### It does NOT fully eliminate
- **Vega risk** — sensitivity to changes in IV.
- **Theta risk** — time decay still affects P&L.
- **Higher-order risks** — vanna, volga, jump risk, gap risk.
- **Transaction cost risk** — frequent trading can erode profits.

So dynamic hedging **transforms your risk profile** but doesn't make the
position risk-free.

## 5. Link to options pricing theory

Dynamic hedging is central to **Black-Scholes** and related models:
- The model assumes you can form a **replicating portfolio** — a combination of
  the underlying and a risk-free asset, continuously rebalanced to match the
  option's payoff.
- If such dynamic replication is possible and markets are arbitrage-free, the
  option's fair price = cost of maintaining the replicating portfolio.

This is why:
- Dealers think of options as **volatility products**, not pure directional bets.
- Implied volatility is the key quoted parameter — it reflects the market's view
  of future realized vol and hedging costs.

## 6. Practical implementation choices

### How often to rebalance?
- **Continuously** — theoretical ideal, impossible in practice.
- **Discrete intervals** — every X minutes/hours, OR when:
  - Delta drifts beyond a threshold (e.g., ±0.05 or ±0.10).
  - Underlying moves by a set % or number of ticks.

### Trade-offs
| Frequency | Hedging error | Transaction cost | Delta drift |
|-----------|---------------|------------------|-------------|
| More often | Lower | Higher | Smaller |
| Less often | Higher | Lower | Larger |

### Choice factors
- Liquidity and transaction costs.
- Gamma of the position (higher gamma → more frequent rebalancing needed).
- Trader's tolerance for delta drift.

## 7. Gamma scalping as a dynamic hedging strategy

**Common setup**: long straddle/strangle (or any long-gamma position) +
dynamically delta-hedge with the underlying.

**Mechanics**:
- Price rises → net delta becomes positive → **sell underlying** to re-hedge.
- Price falls → net delta becomes negative → **buy underlying**.

If underlying oscillates enough, you repeatedly **buy low, sell high**.
Those scalping profits can offset theta decay and potentially generate net profit
even if the underlying ends near where it started.

**Key risks**:
- Market trends strongly in one direction → fewer mean-reversion trades.
- Transaction costs eat scalping profits.
- Volatility crush can still hurt long vega positions.

## 8. Costs and risks of dynamic hedging

### Transaction costs
Each rebalance incurs:
- Commissions/fees
- Bid-ask spread
- Market impact (especially for large orders)

In high-gamma, short-dated positions, rebalancing can be frequent → costs matter
a lot.

### Jump and gap risk
- Dynamic hedging assumes relatively continuous price moves.
- In reality, markets gap on news, earnings, macro data.
- You may be unable to rebalance at expected prices → large hedging errors and
  losses, especially for short options.

### Model and parameter risk
- Delta depends on model inputs (vol, rates, etc.).
- Wrong model or vol estimate → "delta-neutral" hedge isn't truly neutral →
  hidden directional risk.

## 9. Dynamic hedging vs. static hedging

| | Static hedge | Dynamic hedge |
|---|--------------|----------------|
| Setup | Set once | Actively adjusted |
| Adjustments | Manual | Continuous/threshold-based |
| Transaction cost | Lower | Higher |
| Complexity | Simpler | More complex |
| Delta control | Drifts with market moves | Stays near zero |

**Professionals often combine both**:
- Static structures (spreads, collars) to limit extreme risk.
- Dynamic hedging to fine-tune delta and manage day-to-day exposure.

## 10. How to apply dynamic hedging in practice (simplified)

For advanced retail traders:

1. **Start with simple delta hedging** — compute net delta of options book,
   hedge with underlying or futures to bring net delta close to zero.
2. **Define rebalancing rules** — rebalance when:
   - Net delta exceeds a threshold (e.g., ±0.10 per option or ±X% of notional).
   - Underlying moves by a set amount (e.g., ±2%).
   - Or at fixed intervals (e.g., end of day).
3. **Track hedging performance** — record options P&L, hedge trades P&L, and
   transaction costs. Analyze whether frequency and thresholds are optimal.
4. **Be cautious with short gamma** — short straddles/strangles + dynamic
   hedging can be dangerous in fast markets (negative gamma → you buy high,
   sell low). Many traders avoid dynamically hedging large short-gamma positions
   unless very experienced.

## Sources

[^1]: `raw/dynamic-hedging.md` (this file).
[^2]: pomegra.io — chapter 8: hedging with options / dynamic hedging. https://pomegra.io/learn/library/track-e-trading-risk/risk-management/chapter-08-hedging-with-options/dynamic-hedging
[^3]: medium.com / FMZQuant — deribit options delta dynamic hedging strategy. https://medium.com/@FMZQuant/deribit-options-delta-dynamic-hedging-strategy-ca8f86a06c74
[^4]: youtube.com/watch?v=Q_Qrw-OH6yE — dynamic hedging + Black-Scholes link.
[^5]: academic.oup.com — dynamic hedging (Hull-style text excerpt). https://academic.oup.com/book/35149/chapter/299357920
[^6]: cs.uwaterloo.ca — transaction costs in dynamic hedging. https://cs.uwaterloo.ca/~paforsyt/transact.pdf