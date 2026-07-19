---
title: Realized Volatility
type: source
tags: [options, derivatives]
---

# Realized Volatility (RV)

**Realized volatility** is the **actual historical volatility** of an
underlying's returns over a specified lookback period — usually computed as
the standard deviation of log returns, annualised. [^1]

## Formula (log returns, annualised)

```
RV = std(ln(S_t / S_{t-1})) × √(annualisation_factor)
```

Where `annualisation_factor` = trading days per year (252 for US equities,
~245 for SET).

## Worked — S50 30-day realized vol

- Take 30 daily SET50 closes.
- Compute log returns: `r_i = ln(S_i / S_{i-1})`.
- Compute standard deviation of returns.
- Multiply by `√252` to annualise.

Example output: 30-day RV = **16% annualised** → market moved ~16% per year
on a daily-realised basis over the past month.

## Common lookback windows

| Window | Use |
|--------|-----|
| **10-day RV** | Short-term vol — recent regime |
| **20-day RV** | Standard short lookback for IV-RV comparisons |
| **30-day RV** | Monthly comparison for options expiring in 30 days |
| **60-day / 90-day RV** | Longer-term regime; smoother |

The right window depends on the option's tenor. Comparing 30-day IV to
30-day RV is the cleanest apples-to-apples for [[Volatility Risk Premium]]
calculations.

## RV vs HV (Historical Volatility)

These terms are often used interchangeably. Strictly:
- **Historical volatility (HV)** = past realised vol, often a single fixed
  lookback (e.g., "30-day HV").
- **Realised volatility (RV)** = realised over a specific period, often used
  in the IV − RV comparison.

In practice both refer to the same calculation. The IV − RV spread is the
[[Volatility Risk Premium]].

## Estimator choices

| Estimator | Notes |
|-----------|-------|
| **Close-to-close** (standard) | Simplest; ignores intra-range |
| **Parkinson** | Uses high-low range; more efficient when range info available |
| **Garman-Klass** | Open-high-low-close; even more efficient |
| **Yang-Zhang** | Overnight + intraday components; handles drift |

For Thai market, close-to-close is the practical default. Range-based
estimators give a few hundred bps of additional signal at the cost of
complexity.

## Sources

[^1]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 14.
[^2]: CBOE — VIX White Paper (realised vol methodology).
    https://www.cboe.com/tradable_products/vix/
[^3]: Investopedia — Historical Volatility.
    https://www.investopedia.com/terms/h/historicalvolatility.asp
