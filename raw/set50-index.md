---
title: SET 50 Index
type: source
tags: [spot, derivatives, market/thailand]
---

# SET 50 Index — Research Notes

The **SET 50 Index** is the flagship Thai equity index — the underlying of
TFEX's most-traded derivatives (S50 futures, S50 options). Thailand's 50
largest, most liquid stocks, market-cap weighted.

## Index mechanics

- **Base date**: **August 16, 1995** at **1,000 points**. [^1]
- **Recalculation**: continuous during SET trading hours.
- **Weighting**: market-cap weighted (legacy SET50); a free-float variant
  **SET50FF** launched **December 28, 2023** at computed initial value
  **875.25**. [^1]
- **Rebalancing**: semi-annual (March + September), with constituent
  review by SET Index Committee.
- **Number of constituents**: 50.

> **Fact correction**: many retail sources incorrectly quote SET50's base
> as "1996" — that refers to the **Total Return Index (TRI)**. The
> price-index base is August 16, 1995. [^1]

## Top constituents (illustrative, weights vary by rebalance)

Major SET50 names include:

- PTT (energy)
- AOT (aviation)
- ADVANC (telecom)
- DELTA (electronics)
- CPALL (retail)
- SCB (banking)
- KBANK (banking)
- TTB
- BDMS (healthcare)
- SCC (materials)

Weights shift each rebalance. At any time, **top 10 names typically
account for ~50% of index weight**.

## Free-float variant (SET50FF)

Launched Dec 2023 to reflect investable float:

- Excludes strategically-held / non-floating shares.
- Different weights from legacy SET50 — generally lower concentration in
  strategically-held names.
- TFEX S50 futures and options are priced off the **legacy SET50** as
  default; SET50FF feeds certain index-tracking products.

## Why SET50 drives TFEX

- High liquidity in top constituents → tight spreads in basket replication.
- High foreign ownership / flow sensitivity → large directional moves.
- Established derivatives market (S50 futures since 2006, options since
  2007).
- Most institutional Thai benchmarks track SET50.

## Historical volatility

SET50 long-term HV typically sits in **15–25% annualised** range — see
[[Historical Volatility]] for regime breakdowns.

## Liquidity profile

- Top 10 names = bulk of daily volume.
- Concentrated trading during SET day session.
- Lower volume in mid/small cap SET50 names — basket replication
  becomes expensive.

## Index arb / basis

SET50 spot basket vs S50 futures basis sits in the cost-of-carry band:

- `S50_futures ≈ SET50_spot × exp((r - q) × T)`
- `q` = SET50 implied dividend yield (typically 2–3% annualised).
- `r` ≈ BOT policy rate proxy.

Divergences beyond carry + transaction costs = arbitrage opportunity.
See [[Basis]] / [[Contango]] / [[Backwardation]].

## Sources

[^1]: SET — SET 50 Index Ground Rules (March 2026).
    https://www.set.or.th/en/market/index/set50
[^2]: SET — SET Index Methodology.
    https://www.set.or.th/th/market/index/set50
[^3]: TFEX — SET 50 Index Futures.
    https://www.tfex.co.th/en/products/equity/set50-index-futures/contract-specification
[^4]: SET — Index Series Methodology (SET50FF).
    https://www.set.or.th/en/market/index/set50ff
