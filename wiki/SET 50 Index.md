---
title: SET 50 Index
type: concept
status: learning
tags: [spot, derivatives, market/thailand]
aliases: [SET50, SET 50, SET50 Index, S50 Index]
---

# SET 50 Index

The **SET 50 Index** is Thailand's flagship equity index — the 50
largest, most liquid stocks on the SET, market-cap weighted. It's the
underlying of [[TFEX Market Structure|TFEX]]'s most-traded derivatives:
[[SET50 Futures|S50 futures]] and [[SET50 Options|S50 options]].

## Index mechanics

| | |
|---|---|
| **Base date** | **August 16, 1995** at **1,000 points** [^1] |
| **Recalculation** | Continuous during SET trading hours |
| **Weighting** | Market-cap weighted (legacy SET50) |
| **Rebalancing** | Semi-annual (March + September), reviewed by SET Index Committee |
| **Constituents** | 50 |
| **Free-float variant** | **SET50FF** — launched December 28, 2023 at initial value 875.25 |

> **Fact correction**: many retail sources incorrectly quote SET50's
> base as "1996" — that refers to the **Total Return Index (TRI)**. The
> price-index base is August 16, 1995. [^1]

## Top constituents (illustrative)

| Sector | Major names |
|--------|-------------|
| Energy | PTT, PTTEP, TOP |
| Communications | ADVANC, TRUE |
| Banking | KBANK, SCB, TTB, KKP, BBL |
| Retail / commerce | CPALL, CRC, BJC |
| Materials | SCC |
| Transport | AOT, BTS |
| Healthcare | BDMS |

Top 10 names typically = ~50% of index weight. Weights shift at each
semi-annual rebalance.

## Free-float variant (SET50FF)

Launched December 2023 to reflect **investable float**:

- Excludes strategically-held / non-floating shares.
- Different weights from legacy SET50 — typically lower concentration
  in strategically-held names.
- TFEX S50 futures/options priced off legacy SET50 by default.

## Why SET50 drives TFEX

1. **High liquidity** in top constituents → tight spreads in basket
   replication.
2. **Foreign flow sensitivity** → large directional moves.
3. **Established derivatives market** (S50 futures since 2006, options
   since 2007).
4. **Institutional benchmarks** track SET50 → institutional hedging
   demand.

## Historical volatility

SET50 long-term HV typically sits in **15–25% annualised** range — see
[[Historical Volatility]] for regime breakdowns.

- Calm: 10–15%
- Normal: 15–25%
- Stressed: 25–40%
- Crisis: 40%+

## Index arbitrage / basis

SET50 spot basket vs S50 futures basis sits in the cost-of-carry band:

```
S50_futures ≈ SET50_spot × exp((r - q) × T)
```

Where `q` = SET50 implied dividend yield (typically 2–3% annualised) and
`r` ≈ BOT policy rate proxy.

Divergences beyond carry + transaction costs = arbitrage opportunity.
See [[Basis]] / [[Contango]] / [[Backwardation]].

## Relationship to underlying derivatives

| Derivative | Underlying |
|------------|-----------|
| [[SET50 Futures]] | SET50 (legacy) |
| [[SET50 Options]] | SET50 (legacy) |
| [[USD/THB Futures]] | USD/THB spot (different) |
| Sector index futures | Sector baskets (subset of SET) |

## Sources

[^1]: `raw/set50-index.md`
[^2]: SET — SET 50 Index Ground Rules.
    https://www.set.or.th/en/market/index/set50
[^3]: TFEX — SET 50 Index Futures.
    https://www.tfex.co.th/en/products/equity/set50-index-futures/contract-specification
[^4]: SET — Index Series Methodology (SET50FF).
    https://www.set.or.th/en/market/index/set50ff
