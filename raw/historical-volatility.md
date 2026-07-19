---
title: Historical Volatility
type: source
tags: [options, derivatives]
---

# Historical Volatility (HV)

**Historical volatility** is the standard deviation of an underlying's
log returns over a fixed lookback window in the past, annualised. [^1]

It's the "what happened" measure of vol — distinct from
[[Implied Volatility|Implied Volatility]] (IV), which is the market's
forward-looking estimate priced into options.

## Formula

```
HV = std(ln(S_t / S_{t-1})) over N trading days × √(annualisation_factor)
```

Identical to [[Realized Volatility]] calculation. The two terms describe the
same measurement; the distinction is usage:

- **HV** = standalone "how volatile has this been historically" — often a
  single number over a chosen lookback.
- **RV** = realised vol used in IV − RV comparisons (VRP).

## Common lookbacks for HV reads

| Window | Use |
|--------|-----|
| 10-day | Recent regime |
| 20-day | Standard (matches ~1 month option tenor) |
| 30-day | Monthly options |
| 60-day | Smooth regime read |
| 90-day | Quarter cycle |
| 1-year | Long-term "normal" |

HV(20) and HV(30) are the most cited for individual-option tenor matching.

## Why HV matters

1. **IV-HV comparison** = is the market pricing more or less vol than
   actually occurred? Basis for [[Volatility Risk Premium]] strategies.
2. **Regime context** = is current vol elevated or depressed vs history?
   Helps judge whether a given IV number is high or low in absolute terms.
3. **Backtest input** = HV feeds historical-vol-based pricing models and
   strategy backtests.
4. **Strike selection** = realised-vol-driven strike distances (1-sigma,
   2-sigma OTM) for short-premium strikes.

## Volatility cones

**Vol cones** show how HV varies with lookback window. Different windows
give different "normal" HV ranges — typically:

- 10-day HV is more variable than 90-day HV.
- Short windows have wider cones.
- Long windows converge toward "structural" vol.

Use cones to flag when current HV is at the extremes of its own history —
informs whether a move up or down is more likely.

## SET50 HV — practical ranges

SET50 long-term HV typically sits in the **15–25% annualised** range:

| Regime | HV range |
|--------|----------|
| Calm | 10–15% |
| Normal | 15–25% |
| Stressed | 25–40% |
| Crisis | 40%+ (e.g., political shocks, COVID-19 spikes) |

Compare to current IV to gauge cheap/expensive.

## Sources

[^1]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 14.
[^2]: CBOE — Realized Volatility methodology.
    https://www.cboe.com/tradable_products/vix/
[^3]: Investopedia — Historical Volatility.
    https://www.investopedia.com/terms/h/historicalvolatility.asp
