---
title: Strategy Selection Framework
source: Claude-draft from Hull Ch. 10/11 (option strategy selection), CBOE volatility regime framework, Sinclair "Volatility Trading", Augen "Trading Options at Expiration", VRP literature (Ilmanen 2012), TFEX market regime patterns
date: 2026-07-19
---

# Strategy Selection Framework

## The fundamental question

Which strategy to trade is determined by **what you expect** in the next holding period:
1. **Direction** — up / down / neutral (or unknown)
2. **Volatility** — IV cheap / expensive? (VRP high or low)
3. **Regime** — trending or mean-reverting market?

Get the regime wrong → even a technically correct strategy loses.

## The 2×2 regime matrix

```
                    VOL REGIME
                  Low IV       High IV
               (options cheap) (options expensive)
              ┌──────────────┬──────────────────────┐
  TRENDING    │  Buy options  │ Sell premium +       │
              │  directionally│ tight stop, or wait  │
              │  (long calls/ │ for vol to compress  │
              │  puts / vert  │ then buy spread      │
              │  spreads)     │                      │
              ├──────────────┼──────────────────────┤
  MEAN-       │  Long straddle│ Short premium:       │
  REVERTING   │  / strangle   │ Iron condor, short   │
              │  (vol cheap,  │ strangle, calendar   │
              │  big move     │ spread, covered call │
              │  underpriced) │ — HIGHEST EDGE here  │
              └──────────────┴──────────────────────┘
```

**Highest-edge quadrant:** Mean-reverting + High IV = premium-selling strategies. This is where VRP is harvested and dealers are positioned to dampen moves.

**Second-best:** Trending + Low IV = buy directional options cheap, ride the move.

## Regime indicators for SET50

### Volatility regime
| Indicator | High IV signal | Low IV signal |
|-----------|---------------|---------------|
| VRP (IV − RV) | VRP > 5 pts (options expensive) | VRP < 2 pts or negative |
| VSETSI (Thai VIX equivalent) | Above 3-month percentile 70+ | Below 30th percentile |
| IV percentile rank | >60th | <40th |
| Post-event | After earnings season, large geo event | In calm inter-event periods |

### Trend regime
| Indicator | Trending | Mean-reverting |
|-----------|----------|----------------|
| 20-day ADX | > 25 | < 20 |
| SET50 vs 20-day MA | >2% above/below | Within 1% of MA |
| OI pattern | Rising OI in trend direction | Large OI walls at ATM strikes (pinning setup) |
| GEX sign | Negative GEX (amplifying) | Positive GEX (suppressing) |

### Practical composite check (daily pre-trade)
1. What is current VSETSI / SET50 ATM IV vs 30-day average? → vol regime
2. Where is SET50 vs 20-day MA? → trend/mean-reverting
3. What is GEX sign today? → confirms regime
4. Where are the large OI walls? → defines range for condor/strangle, breakout level for directional

## Strategy families by quadrant

### Quadrant A: Mean-reverting + High IV (premium-sell)
- [[Iron Condor]] — defined risk, collect both wings
- [[Short Strangle]] — higher premium, undefined risk (advanced)
- [[Calendar Spread]] — sell near-term high theta, buy back-month
- [[Covered Call]] / [[Cash-Secured Put]] — income against existing holdings

Entry rule: IV rank > 60, ADX < 20, GEX positive.

### Quadrant B: Trending + Low IV (buy directional)
- [[Vertical Spread]] (bull call / bear put) — directional with defined cost
- [[Long Call]] / [[Long Put]] — when vol is cheap; risk = premium only
- [[Protective Put on Future]] — hedge existing futures position cheaply

Entry rule: IV rank < 40, ADX > 25, position in trend direction.

### Quadrant C: Trending + High IV (difficult)
- Avoid undefined-risk premium selling (vol can spike further).
- Prefer vertical spreads (defined risk, some premium offset).
- Wait for vol to compress then switch to directional.
- Or use [[Risk Reversal]] — sell OTM put (finance) + buy OTM call.

### Quadrant D: Mean-reverting + Low IV (speculate on vol expansion)
- [[Long Straddle]] / [[Long Strangle]] — buy vol cheap, profit from big move.
- Condition: expect a catalyst (event, macro, technical breakout).
- Risk: IV crush after catalyst = loss even if price moves.

## Adjusting for VRP specifics

VRP is the best regime indicator for options strategies (see [[Volatility Risk Premium]]):

| VRP | Reading | Strategy |
|-----|---------|----------|
| Very high (>8 pts) | Strong premium-sell signal | Short condor/strangle with proper sizing |
| High (5–8 pts) | Mild premium-sell signal | Covered call, CSP, calendar |
| Low (1–4 pts) | Neutral | Light sizing, or wait |
| Negative | Cheap options, expect larger move | Long straddle/strangle if catalyst visible |

## Expiry selection

| DTE range | Best for |
|-----------|---------|
| 7–21 DTE | Short premium (collect theta fast, close at 50% profit) |
| 30–45 DTE | Condors, strangles (sweet spot: theta + room to manage) |
| 60–90 DTE | Calendar spreads, diagonals (back month) |
| >90 DTE | Long options when vol is cheap and you want leverage |

## Pre-trade checklist integration

Before entering any position, the [[Pre-Trade Checklist]] should confirm:
1. Regime identified (trending vs mean-reverting; high vs low IV)
2. Strategy matches quadrant
3. OI walls identified for strike selection
4. GEX checked for regime confirmation
5. Max loss calculated and within sizing rules

## Sources

- Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 10 (strategy selection), Ch. 11 (properties of stock options)
- Sinclair, *Volatility Trading*, 2nd ed. (regime-conditional strategy selection)
- Augen, *Trading Options at Expiration* (near-expiry regime dynamics)
- Ilmanen, AQR, "Understanding the Volatility Risk Premium" (2012)
- CBOE volatility regime classification methodology
