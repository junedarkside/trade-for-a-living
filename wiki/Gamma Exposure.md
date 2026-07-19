---
title: Gamma Exposure
type: concept
status: learning
tags: [options, derivatives]
aliases: [GEX, Dealer Gamma, Net Gamma]
---

# Gamma Exposure (GEX)

**Gamma Exposure** is the **net gamma** of all open options positions held
by **dealers / market makers** — proxied by sign and magnitude of aggregate
gamma exposure on the underlying. The direction of GEX predicts whether
dealers will **stabilise or amplify** spot moves.

It's the dominant short-term flow signal for systematic options traders.

## Concept

- Every option has a [[Gamma|gamma]] — sensitivity of delta to spot moves.
- Dealers (market makers, liquidity providers) typically **short options to
  clients**. They're short gamma.
- **Short gamma** = dealers must **buy high / sell low** to hedge (delta
  becomes more negative as spot rises; they buy to neutralise, then sell as
  spot drops).
- **Long gamma** = opposite. Dealers buy low / sell high → stabilising flow.

## GEX sign and market behaviour

| GEX sign | Dealer position | Hedging flow | Market impact |
|----------|---------------|--------------|---------------|
| **Negative GEX** | Short gamma | Buy high, sell low | **Amplifies** moves → higher realised vol |
| **Positive GEX** | Long gamma | Sell high, buy low | **Suppresses** moves → lower realised vol |
| **GEX flip point** | Net gamma = 0 (near ATM strikes) | Vol regime change likely |

## How GEX is calculated

1. Pull OI per strike + per expiry from the options chain.
2. Compute gamma per contract using [[Black Model]].
3. Multiply by dealer position estimate (typically: customer long option →
   dealer short → use negative of customer gamma).
4. Sum across all strikes/expiries → aggregate GEX in underlying-point terms.

Tools: SpotGamma, Menthor Q, Unusual Whales (US), Volland (Thai). Manual
calculation is possible but tedious for SET50 chain (100+ strikes × 4
expiries).

## Practical use for Thai SET50 trader

- Track daily GEX sign on SET50 options.
- **Negative GEX days** → expect wider intraday ranges; size directional
  trades smaller or wait for confirmation.
- **Positive GEX days** → favor premium-selling ([[Iron Condor]],
  short strangle) because dealers will dampen moves.
- **GEX flip zone** (around net-zero gamma strikes) → expect vol expansion
  if broken.

## Pitfalls

1. **OI-based GEX is an estimate** — assumes dealer positioning is the
   inverse of customer positioning, only approximately true.
2. **Intraday GEX changes** — fast option flow can flip the sign within
   hours.
3. **Concentration at near expiry** — weekly options dominate the GEX
   picture; longer-dated OI is a slower-moving signal.
4. **No Thai-specific historical GEX data** — must calculate from TFEX-
   published OI + chain pricing.

## Relationship to [[Options Chain]]

GEX combines [[Open Interest]] + [[Implied Volatility]] + [[Gamma|gamma]]
across the [[Options Chain]] into a single directional read on dealer
positioning. Daily GEX sign is the most actionable summary of an otherwise
dense options market.

## Related

- [[Gamma]] · [[Open Interest]] · [[Implied Volatility]] · [[Options Chain]]
  · [[Delta]] · [[Position Greeks]] · [[Volatility Risk Premium]] ·
  [[Delta-Neutral Hedging]]

## Sources

[^1]: `raw/gamma-exposure.md`
[^2]: SpotGamma — GEX methodology white paper.
    https://www.spotgamma.com/
[^3]: SqueezeMetrics — "The Implied Order Book" (GEX framework).
    https://squeezemetrics.com/
[^4]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 19
    (dealer hedging, gamma).
