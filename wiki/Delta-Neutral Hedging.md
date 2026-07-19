---
title: Delta-Neutral Hedging
type: concept
status: learning
aliases: [DNH]
tags: [futures, options, derivatives, greek/delta]
---

# Delta-Neutral Hedging

**Risk management technique.** Set up a multi-leg options position and adjust the
underlying (or futures) leg so the **net delta of the whole structure is zero**.
Profit then depends on **gamma, theta, vega** — not direction.

## Overview
The core of "market-making" and many professional option books. The idea: sell
(or buy) an option, then trade the underlying to lock in a delta-neutral state.
As the underlying moves, delta drifts (via gamma) → re-hedge.

## Net delta formula

```
Δ_total = Σ (leg quantity) × Δ_leg
```

For a multi-leg structure (see [[Multi-Strategy Options]], [[Risk Reversal]],
[[Synthetic Futures]]): sum each leg's delta × quantity.

**Delta-neutral** means Δ_total ≈ 0.

## Example: short straddle on S50

- Sell 1 ATM call (delta ≈ +0.5) → Δ = −0.5
- Sell 1 ATM put (delta ≈ −0.5) → Δ = −(−0.5) = +0.5
- **Net delta = 0** — delta-neutral at entry.

If S50 rises 10 points:
- Call delta → +0.6 (sold), your exposure = −0.6
- Put delta → −0.4 (sold), your exposure = −(−0.4) = +0.4
- **New net delta = −0.2** — slightly bearish delta exposure.
- **Re-hedge**: buy 0.2 S50 futures (or 0.2 × contract units) to restore Δ = 0.

## Greeks framework

| Greek | Role in delta-neutral book |
|-------|---------------------------|
| **[[Delta]]** | Hedges the **first-order** directional move. |
| **[[Gamma]]** | Determines how fast delta drifts — bigger gamma = more frequent re-hedging. |
| **[[Theta]]** | Daily time decay earned/paid. The "edge" in a market-making book. |
| **[[Vega]]** | P&L from changes in implied vol. |
| **[[Rho]]** | P&L from rate moves (minor for short-dated). |

## Mechanics

1. **Open** the option position; immediately hedge with futures to Δ = 0.
2. **Mark-to-market** each session (futures settle daily — see `raw/futures-basics.md`).
3. **Re-hedge** when `|Δ_total|` exceeds a threshold (often 0.05–0.10 × contracts).
4. **Close** the position either by reversing all legs or letting options expire.

## Operational playbook

For worked mechanics (the 10-call × 0.40-delta example showing re-hedge math),
rebalance threshold/frequency choices, gamma scalping, costs/risks, and retail
implementation steps — see [[Dynamic Hedging]]. This article covers the theory
and frameworks; the companion covers the day-to-day operation.

## Re-hedging frequency trade-off
- **Frequent re-hedges** → lock in gains on gamma (good in volatile, oscillating markets).
- **Infrequent re-hedges** → keep more directional exposure (good in trending markets).
- Discrete re-hedging creates **gamma scalping** P&L:
  - Re-buy hedge after an up-move, sell after a down-move → captures path.

## Practical issues
- **Transaction costs** — each re-hedge incurs commission; threshold matters.
- **Liquidity** — futures must be liquid enough to hedge without moving the market.
- **Margin** — see [[Portfolio Margin]] for combined option + futures treatment.
- **Skew/smile** — delta-neutral ≠ vega-neutral; you may need additional vega hedges.

## When to use
- **Sell options for income** without taking directional risk.
- **Market-making** in listed options (S50 options, single-stock options).
- **Convert a directional view** into a gamma/vol play.

## Related
- [[Greeks]] ([[Delta]], [[Gamma]], [[Theta]], [[Vega]]) · [[Black Model]] (pricing/Greeks source) ·
  [[Synthetic Futures]] (linear exposure without options Greeks) · [[Portfolio Margin]]

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/greeks-overview.md`
[^3]: fxoptions.com — managing multi-leg options positions.
[^4]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.