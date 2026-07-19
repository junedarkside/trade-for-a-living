---
title: Edge & Expectancy
source: Claude-draft from Pardo "Design, Testing, Optimization of Trading Systems"; Aronson "Evidence-Based Technical Analysis"; Van Tharp "Trade Your Way to Financial Freedom"; Kelly criterion literature; basic statistics
date: 2026-07-19
---

# Edge & Expectancy

## What is edge?

**Edge** = a trading strategy generates positive expected value (EV) per trade, net of all costs (commissions, slippage, bid-ask spread).

Without edge, no position sizing system can save you. With edge, poor sizing can still ruin you. Edge is necessary but not sufficient.

## Expectancy formula

```
Expectancy = (Win% × Avg Win) − (Loss% × Avg Loss)

Where:
  Win%      = fraction of trades that close profitable
  Avg Win   = average P&L of winning trades (absolute value)
  Loss%     = 1 − Win%
  Avg Loss  = average P&L of losing trades (absolute value)
```

**Example:**
- Win% = 40%, Avg Win = ฿6,000
- Loss% = 60%, Avg Loss = ฿2,500
- Expectancy = (0.40 × 6,000) − (0.60 × 2,500) = 2,400 − 1,500 = **+฿900 per trade**

Positive expectancy = edge. Negative = no edge, don't trade this strategy.

## Reward-to-Risk ratio (R:R)

```
R:R = Avg Win / Avg Loss
```

R:R and Win% trade off. Low win rate requires high R:R to maintain positive expectancy:

| Win% | Required R:R for breakeven |
|------|---------------------------|
| 70%  | 0.43 |
| 50%  | 1.00 |
| 40%  | 1.50 |
| 30%  | 2.33 |
| 20%  | 4.00 |

Premium-selling strategies (short condors, short strangles) tend toward high win%, low R:R. Directional long options tend toward low win%, high R:R. Both can have edge — the ratio matters, not either number alone.

## Strategy-specific edge sources

| Strategy | Edge source | Edge condition |
|----------|-------------|----------------|
| Short premium (condor, strangle) | Volatility Risk Premium (IV > RV) | High VRP regime; managed exits |
| Directional options | Correct direction + IV timing | Edge collapses if IV-crushed after entry |
| Calendar spread | Theta differential between expiries | Stable underlying, no large vol moves |
| Futures trend | Price momentum persistence | Trending market regime |
| Delta-neutral hedging | Gamma scalping | Realised vol > IV (long options) |

## Edge decay

Edges erode over time as:
1. Market participants learn the pattern.
2. Market structure changes (new products, regulation, liquidity shifts).
3. Your own execution changes (position size affects fill quality at TFEX liquidity levels).

Test for edge decay: divide backtest data in halves (in-sample / out-of-sample). If expectancy drops sharply on out-of-sample, the edge may be curve-fitted.

## Statistical significance — sample size

How many trades before you can trust a positive expectancy?

Rule of thumb: **min 30 trades**, ideally 100+, with consistent setup and sizing.

More rigorous:
```
Required n ≈ (Z_α × σ / target_edge)²

Where:
  Z_α = 1.96 for 95% confidence
  σ   = standard deviation of trade P&L
  target_edge = the edge per trade you want to detect
```

**Practical shortcut:** if your backtest has < 30 trades, the edge estimate is unreliable regardless of the P&L. Run forward tests, increase sample size, or accept that you don't know yet.

## Common statistical traps

1. **Overfitting** — too many parameters optimized to historical data → in-sample edge ≠ out-of-sample edge. Use walk-forward optimization (see Backtesting & Forward Testing).
2. **Selection bias** — only trading setups that "look good" in hindsight. Every setup must be logged before outcome is known.
3. **Survivorship bias** — if you stopped trading a strategy after losing streaks, your logged results overstate actual edge.
4. **Small sample delusion** — 8 wins in a row on 10 trades is not evidence of 80% win rate; it's within noise of a 50% strategy.

## Translating edge into sizing

Once you have a statistically significant edge estimate:
- Use Kelly fraction or fractional Kelly for optimal sizing (see [[Position Sizing Frameworks]]).
- If expectancy per trade = ฿900 and σ = ฿3,000, Kelly % = edge/variance = 900/9,000,000 ≈ 0.01% of capital per unit — then scale to your risk tolerance.
- Conservative traders use ¼ Kelly or fixed fractional (risk 1–2% per trade regardless).

## Continuous edge tracking

Every trade goes into your journal (see [[Trade Journaling]]). Run rolling 30-trade expectancy. If expectancy flips negative for 2+ rolling windows → **stop and review** before continuing.

## Sources

- Pardo, *Design, Testing, and Optimization of Trading Systems* (expectancy, out-of-sample testing)
- Van Tharp, *Trade Your Way to Financial Freedom* (expectancy formula, R-multiples)
- Aronson, *Evidence-Based Technical Analysis* (statistical hypothesis testing for traders)
- Kelly, J.L. (1956), "A New Interpretation of Information Rate" (Kelly criterion)
- Vince, *The Handbook of Portfolio Mathematics* (optimal f, position sizing math)
