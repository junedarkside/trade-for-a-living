---
title: SET Circuit Breakers
type: concept
status: learning
tags: [spot, futures, options, derivatives, market/thailand]
aliases: [Circuit Breaker, Price Band, Daily Limit, Ceiling, Floor]
---

# SET Circuit Breakers

SET and TFEX enforce multiple circuit-breaker layers:
1. **Per-stock daily price bands** (cash equities)
2. **Index-level circuit breaker** (market-wide)
3. **Per-product price limits** (TFEX derivatives)

## 1. Cash equity daily price bands [^1]

| Price range (Baht) | Ceiling / Floor |
|--------------------|-----------------|
| < 2 | **±30%** |
| 2 to < 5 | ±20% |
| 5 to < 10 | ±15% |
| 10 to < 25 | ±10% |
| 25 to < 50 | ±7% |
| 50 to < 100 | ±5% |
| ≥ 100 | **±4%** |

Reference price for first trading day of newly listed security = IPO
offering price; otherwise prior close. [^1]

## 2. Halt mechanics

- Stock hits ceiling/floor → trading halted.
- Resume typically via **call auction re-open** after short cooling-off.
- Specific cooling-off duration not codified in public docs; varies by
  trigger.

## 3. Index-level (market-wide) circuit breaker [^2]

- **Level 1 trigger**: SET Index down **10%** from previous close → halt
  equities for ~30 minutes.
- Historical triggers (~7 occurrences):
  - **2006** capital controls
  - **2014** political turmoil (Reuters: 7 August 2014)
  - **2020 March** COVID crash
  - **2025** global tensions

## 4. TFEX-side price limits

| Product | Price limit rule |
|---------|------------------|
| **[[SET50 Futures]]** | +30% of latest settlement (one-sided — leveraged long-bias) |
| **[[USD/THB Futures]]** | ±2% initial → halt → ±4% expanded |
| **Gold Futures (GF / GF10)** | ±10% initial → halt → ±20% expanded |
| **Sector Index Futures** | +30% of latest settlement |

> Direct quote (USD/THB spec): *"Initial limit is ±2% of the latest
> settlement price. If hit, trading halts, then resumes with an expanded
> limit of ±4% of the latest settlement price."* [^3]

## 5. Special event circuit breakers

SET retains the right to apply **additional measures** during
high-volatility periods. Specific event-driven halts are not codified —
decided ad hoc by the SET Board.

## Practical trader implications

- **Daily**: watch your stock's tier — penny stocks (< ฿2) have ±30%
  bands; blue chips ±5–7%.
- **Monthly**: index-level circuit breakers rare (~7 historical); coincide
  with macro shocks (capital controls, COVID, geopolitics).
- **Annual**: SET Board can amend trigger thresholds; no formal schedule.

## Related

- [[Spot — Basics]] · [[SET50 Futures]] · [[USD/THB Futures]] ·
  [[Margin Mechanics]] · [[Risk Management]] · [[Volatility Risk Premium]] ·
  [[TFEX Market Structure]]

## Sources

[^1]: `raw/set-circuit-breakers.md`
[^2]: SET — Price Bands & Tick Sizes.
    https://www.set.or.th/en/market/information/trading-procedure/price-bands-and-tick-sizes
[^3]: Bangkok Post — Circuit breaker triggered on SET index (2020).
    https://www.bangkokpost.com/business/general/1877359/circuit-breaker-triggered-on-set-index
[^4]: Reuters — Thailand's SET triggers second market-wide circuit breaker (Aug 2014).
    https://www.reuters.com/article/idUSL3N0GL4AC20140807/
[^5]: TFEX — USD/THB Futures Contract Specification.
    https://www.tfex.co.th/en/products/currency/usd-futures/contract-specification
