---
title: Black Model
type: concept
status: learning
aliases: [BM]
tags: [options, futures, derivatives]
---

# Black Model

**Pricing model.** Black-76 (the "Black model for options on futures") prices
European options on a futures contract. The standard model for TFEX S50 options
and most commodity/equity-index options on futures.

## Overview
A normal-distribution-based formula taking the **futures price** as the
underlying input rather than spot. Derived from Black-Scholes by substituting
forward (F) for spot (S) and accounting for the absence of a stock-like carry
cost.

## Inputs

| Symbol | Meaning |
|--------|---------|
| `F` | Current futures price |
| `K` | Strike price |
| `T` | Time to expiry (in years) |
| `r` | Risk-free rate (continuously compounded) |
| `σ` | Implied volatility |

## Formulas (European options on futures)

```
d1 = [ ln(F/K) + (σ²/2) · T ] / (σ · √T)
d2 = d1 − σ · √T

Call price = e^(−rT) · [ F · N(d1) − K · N(d2) ]
Put  price = e^(−rT) · [ K · N(−d2) − F · N(−d1) ]
```

Where `N(x)` is the standard normal CDF.

## Put-call parity (futures variant)
```
C − P = e^(−rT) · (F − K)
```
This is the foundation of [[Synthetic Futures]] — long call + short put
replicates a long futures position.

## Greeks (Black model)
- **Delta_call** = `e^(−rT) · N(d1)`
- **Delta_put** = `−e^(−rT) · N(−d1)`
- **Gamma** = `e^(−rT) · n(d1) / (F · σ · √T)` (same for call and put)
- **Vega** = `e^(−rT) · F · √T · n(d1)` (same for call and put)
- **Theta** = derived from F, σ, T, r — same shape as Black-Scholes theta.
- **Rho** — minor; longer-dated options have meaningful rate sensitivity.

Where `n(x)` is the standard normal PDF.

Key point: **futures options have delta bounded by ±e^(−rT)** (not ±1), because
delta is the sensitivity to futures price, not spot.

## Limitations
- Assumes **constant volatility** and **log-normal returns**.
- European exercise only (early-exercise premium must be added heuristically for American).
- No discrete dividends (handled via futures price, which absorbs carry).

## When to use
- Pricing European options on futures (TFEX S50 options, CME equity-index options, commodities).
- Computing Greeks for a futures-options position (see [[Delta-Neutral Hedging]]).
- Identifying **forward-starting** or **futures-style** option structures.

## Related
- [[Greeks]] · [[Delta-Neutral Hedging]] · [[Synthetic Futures]] · [[Contango]] ·
  [[Backwardation]] (forward vs spot drives parity deviations)

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: fxoptions.com — managing multi-leg options positions.
[^3]: fidelity.com — one-leg or two learning center.