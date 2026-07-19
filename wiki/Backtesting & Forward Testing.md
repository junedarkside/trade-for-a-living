---
title: Backtesting & Forward Testing
type: concept
status: learning
tags: [risk, derivatives]
aliases: [Backtest, Walk-Forward, Out-of-Sample, Forward Test, OOS]
---

# Backtesting & Forward Testing

Backtesting validates a trading idea against historical data. Forward
testing validates it in live (or simulated) execution. Most ideas that
look great in backtests fail live. **Methodology matters more than the
strategy itself.**

## Pardo Walk-Forward Procedure

The gold-standard for validating systematic strategies.

### Steps

1. **Initial split**: choose in-sample (IS) and out-of-sample (OOS) ratio.
   Default 70/30.
2. **Optimise** strategy parameters on IS data.
3. **Test** parameters on OOS data, record return.
4. **Roll** forward (anchored or rolling). Repeat steps 2–3.
5. Run **20–40 iterations** total.
6. **Compute efficiency ratio** = walk-forward return / in-sample return.
   Robust: **> 50–60%**.

### Anchored vs rolling

- **Anchored**: IS window grows from fixed start date. Long IS data.
- **Rolling**: IS window slides forward at fixed length. Adapts to regime
  change but loses old data.

**Rule of thumb:** IS:OOS ratio 5:1; 20+ iterations for statistical signal.

## Out-of-Sample Testing

- **Hold out** 30% of data the strategy has **never seen**.
- **Never re-optimise** after looking at OOS results.
- If OOS is bad, the strategy fails. Don't tweak to fit.

## Look-Ahead Bias — 5 forms

| Form | Mitigation |
|------|-----------|
| Using today's close to trade today's open | Trade on next bar |
| Using revised data | Use point-in-time raw data |
| Survivorship (using current SET50 to backtest 1995) | Use point-in-time constituent list |
| Indicator that uses future values (RSI of close[t+1]) | Lag all inputs |
| Quarterly rebalance assumes you know quarter-end prices | Use end-of-day snapshot only |

## Survivorship Bias — Thai Market

For SET50 backtests, use the **historical constituent list** at each
rebalance date, not the current SET50. Constituents drop in / out at
semi-annual rebalances (March + September). See [[SET 50 Index]].

## Realistic Fills

| Cost | Typical TFEX/SET value |
|------|------------------------|
| Commission | THB 10–50 / side |
| Bid-ask spread | ฿0.01–฿0.10 per unit for liquid options |
| Slippage | ฿0.05–฿0.20 for fast-market entries |
| Partial fills | Common in illiquid strikes |

Add these to every backtest fill. Backtests without them **overstate
performance**.

## Monte Carlo Robustness

Methods to stress-test:

- **Trade-order shuffle**: randomise trade sequence, re-compute equity curve.
- **Block bootstrap**: resample contiguous return blocks.
- **Parametric GBM**: simulate price paths from estimated parameters.
- **Sensitivity perturbation**: vary parameters ±N%, check stability.

## Pardo's 7 Core Principles

1. **Test on out-of-sample data, not in-sample.**
2. **If walk-forward fails, walk away — don't tweak.**
3. **More data > more parameters.**
4. **Realistic fills are non-negotiable.**
5. **Optimisation bias is the silent killer.**
6. **In-sample efficiency is meaningless alone.**
7. **Survivorship bias inflates historical results.**

## Aronson's Evidence-Based TA

For statistical validation:

- **White's Reality Check** — tests whether a strategy's OOS performance is
  better than chance, accounting for data-snooping.
- **Hansen's SPA Test** — Superior Predictive Ability; more powerful than
  White's RC for multiple strategies.

## Forward Testing Ladder

| Stage | Capital | Purpose |
|-------|---------|---------|
| **Paper / sim** | 0 | Verify execution + discipline |
| **Micro-lots** | 1 contract / 100 shares | Real fills, real emotions |
| **Half-size** | 50% target | Live but reduced |
| **Full-size** | 100% target | Final validation |

## Common Backtest Pitfalls

1. **Overfitting** — too many parameters fit noise.
2. **Data snooping** — testing many strategies until one wins.
3. **Survivorship bias** — see above.
4. **Ignoring transaction costs**.
5. **Curve-fitting** — parameters tuned to history, not robust to future.
6. **Sample too small** — 30 trades tells you nothing.

## Related

- [[Position Sizing Frameworks]] · [[Trade Journaling]] ·
  [[P&L Attribution]] · [[Volatility Risk Premium]] ·
  [[Options Risk Management]] · [[Risk Management]]

## Sources

[^1]: `raw/backtesting.md`
[^2]: Pardo, *Design, Testing, and Optimization of Trading Systems*, 2008.
[^3]: Aronson, *Evidence-Based Technical Analysis*, 2007.
[^4]: López de Prado, *Advances in Financial Machine Learning*, 2018.
[^5]: Bailey, Borwein, López de Prado, Zhu, *Pseudo-mathematics and
    financial charlatanism*, 2014.
