---
title: Historical Volatility
type: concept
status: learning
tags: [options, derivatives]
aliases: [HV, Hist Vol]
---

# Historical Volatility (HV)

**Historical volatility** is the standard deviation of an underlying's log
returns over a fixed lookback window in the past, annualised. The "what
happened" measure of vol — distinct from [[Implied Volatility|IV]] which
is the market's forward-looking estimate priced into options.

Calculation is identical to [[Realized Volatility]]; usage differs:

- **HV** = standalone "how volatile has this been" — single fixed lookback.
- **RV** = realised vol used in IV − RV comparison (VRP).

## Common lookbacks

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
   occurred? Basis for [[Volatility Risk Premium]] strategies.
2. **Regime context** = current vol elevated or depressed vs history?
3. **Backtest input** = feeds historical-vol-based pricing and strategy
   backtests.
4. **Strike selection** = 1-σ / 2-σ OTM strike distances for short-premium.

## Volatility cones

**Vol cones** show HV ranges per lookback window. Different windows have
different "normal" ranges:

- 10-day HV more variable than 90-day HV.
- Short windows have wider cones.
- Long windows converge toward structural vol.

Use cones to flag when current HV is at extremes of its own history.

## SET50 HV — practical ranges

SET50 long-term HV typically sits in the **15–25% annualised** range:

| Regime | HV range |
|--------|----------|
| Calm | 10–15% |
| Normal | 15–25% |
| Stressed | 25–40% |
| Crisis | 40%+ (political shocks, COVID-19 spikes) |

Compare to current IV to gauge cheap/expensive.

## IV rank and IV percentile (HV-derived)

Two common IV-context reads derived from HV history:

- **IV rank** = (current IV − 52w low) ÷ (52w high − 52w low). Where is IV
  in its own range?
- **IV percentile** = % of past trading days where IV was lower than today.
  More robust to outliers.

Both use HV data as the denominator; both feed short-premium selection rules
(see [[Volatility Risk Premium]]).

## Related

- [[Realized Volatility]] · [[Implied Volatility]] · [[Volatility Risk
  Premium]] · [[IV Skew, Smile & Surface]] · [[Black Model]] ·
  [[Options Strategy]]

## Sources

[^1]: `raw/historical-volatility.md`
[^2]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 14.
[^3]: CBOE — Realized Volatility methodology.
    https://www.cboe.com/tradable_products/vix/
[^4]: Investopedia — Historical Volatility.
    https://www.investopedia.com/terms/h/historicalvolatility.asp
