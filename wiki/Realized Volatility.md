---
title: Realized Volatility
type: concept
status: learning
tags: [options, derivatives]
aliases: [RV, Realised Volatility, Realized Vol]
---

# Realized Volatility (RV)

**Realized volatility** is the **actual historical volatility** of an
underlying's returns over a specified lookback window, computed as the
standard deviation of log returns and annualised. The "what actually
happened" measure of vol — used as the right-hand side of the IV − RV
calculation in [[Volatility Risk Premium|VRP]].

## Formula (log returns, annualised)

```
RV = std(ln(S_t / S_{t-1})) × √(annualisation_factor)
```

`annualisation_factor` = trading days per year (252 US, ~245 SET).

## Worked — S50 30-day realized vol

1. Take 30 daily SET50 closes.
2. Compute log returns: `r_i = ln(S_i / S_{i-1})`.
3. Compute standard deviation of returns.
4. Multiply by `√252` to annualise.

Output: 30-day RV = **16% annualised** = SET50 moved ~16%/yr on a
daily-realised basis over the past month.

## Common lookback windows

| Window | Use |
|--------|-----|
| 10-day RV | Short-term vol — recent regime |
| 20-day RV | Standard short lookback for IV-RV comparisons |
| 30-day RV | Monthly options tenor |
| 60–90-day RV | Longer-term regime; smoother |

Compare IV and RV with **matching tenors** (30-day IV vs 30-day RV) for
cleanest apples-to-apples.

## Estimator choices

| Estimator | Notes |
|-----------|-------|
| **Close-to-close** | Standard; ignores intra-range |
| **Parkinson** | Uses high-low range; more efficient |
| **Garman-Klass** | OHLC; even more efficient |
| **Yang-Zhang** | Overnight + intraday components |

Close-to-close is the practical default. Range-based estimators give marginal
extra signal at higher complexity cost.

## RV vs IV (the core relationship)

- **RV** = backward-looking, fixed window.
- **IV** = forward-looking, priced into options.

`IV − RV` = the [[Volatility Risk Premium]]. Positive VRP = options "expensive"
relative to what happened.

## Worked VRP — S50 example

- S50 30-day ATM option IV = **22%**.
- 30-day RV (rolling, annualised) = **16%**.
- VRP = 22% − 16% = **+6 vol points** (~27% of IV) → elevated; options
  richly priced. Lean short-premium (see [[Volatility Risk Premium]] for
  strategy guidance).

## Related

- [[Historical Volatility]] · [[Implied Volatility]] · [[Volatility Risk
  Premium]] · [[IV Skew, Smile & Surface]] · [[Black Model]]

## Sources

[^1]: `raw/realized-volatility.md`
[^2]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 14.
[^3]: CBOE — VIX White Paper (realised vol methodology).
    https://www.cboe.com/tradable_products/vix/
[^4]: Investopedia — Historical Volatility.
    https://www.investopedia.com/terms/h/historicalvolatility.asp
