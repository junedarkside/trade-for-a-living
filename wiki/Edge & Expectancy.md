---
title: Edge & Expectancy
type: concept
status: learning
tags: [derivatives, risk]
aliases: [Expectancy, Trading Edge, R-Multiple]
---

# Edge & Expectancy

**Edge** = a trading strategy generates positive expected value (EV) per trade,
net of all costs. **Expectancy** is the numerical measure of that edge per trade.

Without edge, no position sizing system saves you. With edge, poor sizing can
still ruin you. Edge is necessary but not sufficient.

## Expectancy formula

```
Expectancy = (Win% × Avg Win) − (Loss% × Avg Loss)
```

**Example:**
- Win% = 40%, Avg Win = ฿6,000
- Loss% = 60%, Avg Loss = ฿2,500
- Expectancy = (0.40 × 6,000) − (0.60 × 2,500) = **+฿900 per trade**

Positive = edge. Negative = no edge — do not trade this strategy.

## Win rate vs Reward-to-Risk (R:R)

Win rate and R:R trade off. Both must combine to positive expectancy:

| Win% | Min R:R for breakeven |
|------|----------------------|
| 70% | 0.43 |
| 50% | 1.00 |
| 40% | 1.50 |
| 30% | 2.33 |
| 20% | 4.00 |

**Premium-selling** strategies (Iron Condor, Short Strangle): high win%, low R:R.
**Directional options** (long calls/puts): low win%, high R:R.
Both can have edge — what matters is the product `Win% × Avg Win`.

## Edge sources by strategy

| Strategy | Edge source | Condition |
|----------|-------------|-----------|
| Short premium (condor, strangle) | Volatility Risk Premium (IV > RV) | High VRP regime; managed exits |
| Directional options | Correct direction + IV timing | Collapses if IV-crushed post-entry |
| Calendar spread | Theta differential between expiries | Stable underlying; no large vol shift |
| Futures trend | Price momentum persistence | Trending regime |
| Gamma scalping | Realised vol > IV | Realised vol > what you paid for |

## Sample size requirements

How many trades before trusting a positive expectancy?

**Minimum:** 30 trades. **Reliable:** 100+, with consistent setup and sizing.

```
Required n ≈ (1.96 × σ_trade / target_edge)²
```

Where σ_trade = standard deviation of individual trade P&L. If your
backtest has < 30 trades, the edge estimate is statistically unreliable —
regardless of P&L.

## Edge decay

Edges erode as:
1. Market participants learn the pattern.
2. Market structure changes (liquidity, regulation, new participants).
3. Your own position size grows and impacts your fill quality.

**Test for decay:** split backtest into in-sample / out-of-sample halves. If
expectancy drops sharply on the out-of-sample half, the edge may be
curve-fitted to noise. See [[Backtesting & Forward Testing]] for the
walk-forward methodology.

## Common statistical traps

| Trap | Description |
|------|-------------|
| **Overfitting** | Too many parameters optimized to history → no real edge |
| **Selection bias** | Only logging setups that "looked good" in hindsight |
| **Survivorship bias** | Stopped trading after losing streaks → overstated track record |
| **Small sample delusion** | 8 wins in 10 trades ≠ 80% win rate; within noise of a 50% strategy |

## Continuous edge tracking

Every trade goes to journal (see [[Trade Journaling]]). Run rolling 30-trade
expectancy. If expectancy flips negative for 2+ rolling windows → **stop and
review** before continuing. Do not add size or change strategy while in
drawdown — this masks edge degradation.

## From expectancy to sizing

Once expectancy is statistically significant, use it to calibrate sizing:
- Kelly fraction ≈ edge / variance of trade P&L (see [[Position Sizing Frameworks]]).
- Conservative traders use ¼ Kelly or fixed-fractional (risk 1–2% per trade).
- A positive expectancy of ฿900/trade with σ = ฿3,000 supports modest sizing — do not over-lever.

## Worked example — Thai SET50 Iron Condor

Backtest (100 trades, 45 DTE, managed at 50% profit / 200% loss):
- Win% = 68%, Avg Win = ฿1,800, Avg Loss = ฿3,200 (net debit including commissions).
- Expectancy = (0.68 × 1,800) − (0.32 × 3,200) = 1,224 − 1,024 = **+฿200/trade**.
- Annualized at 12 condors/year = ฿2,400 expected profit on this sample.
- Confidence interval at n=100: ±฿2 standard errors — edge is real but modest; size conservatively.

## Related

- [[Backtesting & Forward Testing]] · [[Position Sizing Frameworks]] ·
  [[Trade Journaling]] · [[Volatility Risk Premium]] ·
  [[Options Risk Management]] · [[Strategy Selection Framework]]

## Sources

[^1]: `raw/edge-and-expectancy.md`
[^2]: Pardo, *Design, Testing, and Optimization of Trading Systems* (expectancy, walk-forward).
[^3]: Van Tharp, *Trade Your Way to Financial Freedom* (expectancy formula, R-multiples).
[^4]: Aronson, *Evidence-Based Technical Analysis* (statistical hypothesis testing for traders).
[^5]: Kelly, J.L. (1956), "A New Interpretation of Information Rate" (Kelly criterion).
