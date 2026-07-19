---
title: Strategy Selection Framework
type: concept
status: learning
tags: [options, futures, derivatives, risk, market/thailand]
aliases: [SSF, Strategy Framework, Regime Matrix]
---

# Strategy Selection Framework

**Which strategy to trade is determined by the regime.** Get the regime wrong
and even a technically correct strategy loses. The framework maps market
conditions to the strategy family with highest expected edge.

Two regime axes determine strategy choice:
1. **Volatility regime** — is IV cheap or expensive? (VRP high or low)
2. **Trend regime** — is the market trending or mean-reverting?

## The 2×2 regime matrix

```
                    VOLATILITY REGIME
               Low IV (cheap)    High IV (expensive)
              ┌─────────────────┬────────────────────────┐
  TRENDING    │ Buy directional │ Sell premium + tight   │
              │ Vert spread,    │ stop; or wait for vol  │
              │ Long call/put   │ to compress, then buy  │
              │                 │ spread                 │
              ├─────────────────┼────────────────────────┤
  MEAN-       │ Long straddle / │ SHORT PREMIUM ★        │
  REVERTING   │ strangle        │ Iron Condor, Strangle  │
              │ (buy cheap vol, │ Calendar Spread,       │
              │ expect big move)│ Covered Call / CSP     │
              └─────────────────┴────────────────────────┘
                                  ★ Highest edge here
```

**Highest edge quadrant:** Mean-reverting + High IV. This is where VRP is
harvested and dealer hedging flow suppresses realised volatility.

## Regime indicators for SET50

### Volatility regime

| Indicator | High IV (sell premium) | Low IV (buy options) |
|-----------|----------------------|---------------------|
| VRP = IV − RV | > 5 vol pts | < 2 pts or negative |
| ATM IV percentile (30d) | > 60th | < 40th |
| Post-event flag | After earnings season / large macro event | Calm inter-event period |

### Trend regime

| Indicator | Trending | Mean-reverting |
|-----------|----------|----------------|
| 20-day ADX | > 25 | < 20 |
| SET50 vs 20d MA | > 2% above/below | Within 1% of MA |
| OI pattern | Rising OI in trend direction | Large OI walls at ATM → pinning |
| GEX sign | Negative (amplifying) | Positive (suppressing) |

## Strategy families by quadrant

### Quadrant A: Mean-reverting + High IV (premium-sell) ★

Best edge. Sell premium with defined risk; collect VRP; let time decay work.

- [[Iron Condor]] — defined risk, sell both wings outside OI walls.
- [[Short Strangle]] — higher premium, undefined risk (advanced, strict sizing).
- [[Calendar Spread]] — sell near-term high theta, buy back-month.
- [[Covered Call]] / [[Cash-Secured Put]] — income against holdings.

**Entry filter:** VRP > 5, ADX < 20, positive GEX, large OI walls at ATM.

### Quadrant B: Trending + Low IV (directional long)

Cheap options; buy direction; IV can only go up (long vega helps too).

- [[Vertical Spread]] (bull call / bear put) — defined risk, directional.
- [[Long Call]] / [[Long Put]] — when IV cheap; risk = premium only.
- [[Futures — Basics|Long futures]] — when trend is clear and IV not a factor.

**Entry filter:** IV percentile < 40, ADX > 25, entry in trend direction.

### Quadrant C: Trending + High IV (difficult — avoid undefined risk)

Worst quadrant for premium sellers. IV can spike further; stops can be hit.
- Prefer [[Vertical Spread]] (defined risk absorbs further IV spike).
- [[Risk Reversal]] — sell OTM put to finance OTM call in direction of trend.
- Do **not** sell naked strangles/condors here.

### Quadrant D: Mean-reverting + Low IV (long vol / catalyst play)

Buy cheap volatility; profit from move in either direction.
- [[Long Straddle]] / [[Strangle]] — buy low IV, profit from big move.
- Works best into known catalysts (earnings, BoT rate decision, SET revision).
- **Risk:** IV crush after event; price may move but premium drops → loss.

## Daily pre-trade regime check

1. **VRP** = SET50 ATM IV − 30-day RV → vol regime.
2. **SET50 vs 20d MA** → trend/mean-reverting.
3. **GEX sign** → confirms (positive = suppression = favor sell-premium).
4. **OI walls** → define strikes for condor/strangle wings or breakout target.
5. **PCR trend** → sentiment context (see [[Options Flow Analysis]]).

All 5 checks take < 5 minutes at session open (see [[Daily Routine & Market Prep]]).

## Expiry selection by strategy

| DTE | Best use |
|-----|---------|
| 7–21 | Short premium (collect theta fast, close at 50% profit) |
| 30–45 | Condors, strangles (sweet spot: theta + room to manage) |
| 60–90 | Calendar spread back month; diagonal |
| > 90 | Long options when IV cheap + directional |

## Related

- [[Volatility Risk Premium]] · [[Options Strategy]] · [[Options Flow Analysis]] ·
  [[Gamma Exposure]] · [[Open Interest]] · [[Greeks]] ·
  [[Iron Condor]] · [[Vertical Spread]] · [[Long Straddle]] ·
  [[Pre-Trade Checklist]] · [[Edge & Expectancy]] · [[Daily Routine & Market Prep]]

## Sources

[^1]: `raw/strategy-selection-framework.md`
[^2]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 10–11.
[^3]: Sinclair, *Volatility Trading*, 2nd ed. (regime-conditional strategy selection).
[^4]: Ilmanen, AQR, "Understanding the Volatility Risk Premium" (2012).
[^5]: CBOE — volatility regime classification methodology.
