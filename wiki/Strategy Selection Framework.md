---
title: Strategy Selection Framework
type: concept
status: learning
tags: [options, futures, derivatives, risk, market/thailand]
aliases: [SSF, Strategy Framework, Regime Matrix]
---

# Strategy Selection Framework

**Which strategy to trade is determined by the regime.** Get the regime wrong
and even a technically correct strategy loses. The framework maps two regime
axes to the strategy family with the highest expected edge.

Two axes:
1. **Volatility regime** — is IV cheap or expensive relative to history?
2. **Trend regime** — is the market trending or mean-reverting?

## The 2×2 regime matrix

```
                    VOLATILITY REGIME
               Low IV (IVR<30, IVPCT<30)    High IV (IVR>50, IVPCT>50)
              ┌──────────────────────────┬──────────────────────────────┐
  TRENDING    │ Buy directional (Q-B)    │ Smallest size (Q-C)          │
  ADX>25      │ Vert spread, Long call/  │ Defined-risk only            │
  GEX neg     │ put, Long futures        │ Risk reversal; wait for      │
              │ Standard sizing          │ vol compression              │
              ├──────────────────────────┼──────────────────────────────┤
  MEAN-REV    │ Long vol / catalyst (Q-D)│ SHORT PREMIUM ★ (Q-A)        │
  ADX<20      │ Long straddle/strangle   │ Iron condor, strangle,       │
  GEX pos     │ Standard size            │ calendar, covered call       │
              │ Catalyst required        │ Half-Kelly, ATR-adjusted     │
              └──────────────────────────┴──────────────────────────────┘
                                           ★ Highest-edge quadrant
```

**Highest edge:** Q-A (mean-reverting + high IV). VRP harvested; dealer
hedging suppresses realised vol; IV overstates RV ~85% of the time.

**Base rates (S&P 500, 2000–2024):** trending ≈ 52% of time, mean-reverting
≈ 48%. Momentum strategy Sharpe: 1.82 trending, −0.41 mean-reverting —
regime identification matters more than strategy selection within a regime.[^8]

---

## Vol regime indicators

### IV Rank vs IV Percentile — use both

> **These are different metrics.** Using only one gives false signals.

| Metric | Formula | Strength | Weakness |
|--------|---------|---------|---------|
| **IV Rank (IVR)** | (IV − 52w Low) / (52w High − 52w Low) × 100 | Fast, reactive | One spike distorts the range for 52 weeks |
| **IV Percentile (IVPCT)** | % of past 252 trading days where IV < today | Robust to spikes | Slow after sustained regime change |

**Confirmation rule:** require both above threshold before entering. After
a vol spike, IVPCT may read 75 (historically elevated) while IVR reads 40
(seems neutral) because the spike reset the 52w high. IVPCT is correct in
that case.

### Calibrated vol thresholds (backtested)

Source: TastyTrade backtested across 595 symbols. Iron condors entered with
both IVR > 50 AND IVPCT > 50 → **56.8% win rate** vs 48.2% without filter.
Strangles at IVR > 50 → 73% win rate.

| IVR | IVPCT | Reading | Strategy lean |
|-----|-------|---------|---------------|
| > 70 | > 70 | Very rich — peak premium-selling | Short strangle / condor; quarter-Kelly |
| > 50 | > 50 | Elevated — premium-selling zone | Iron condor, CSP, covered call; half-Kelly |
| 30–50 | 30–50 | Neutral | Light sizing or wait for confirmation |
| < 30 | < 30 | Cheap vol | Long straddle/strangle (with catalyst); larger Kelly fraction |

---

## Trend regime indicators

### Primary: ADX

ADX > 25 = trending; ADX < 20 = mean-reverting (industry standard; ADX 20
as stricter cutoff reduces whipsaws). **Wilder (1978) never specified 25 —
emerged as practitioner consensus.** ADX is lagging: confirms trend already
established, not one starting.

### Secondary: GEX sign (leading/coincident)

- **Positive GEX** → dealers net long gamma → suppress moves → mean-reverting
- **Negative GEX** → dealers net short gamma → amplify moves → trending
- **GEX flip zero-crossing** → regime transition marker

GEX is actionable as a leading signal; ADX is the lagging confirmation.
Use GEX for entry timing, ADX for regime classification.

### Quantitative classifier: Hurst Exponent (H)

Measures long-range dependence in a price series:

| H value | Regime | Signal |
|---------|--------|--------|
| H < 0.45 | Mean-reverting | Strong statistical signal |
| 0.45–0.55 | Random walk / indeterminate | Reduce size; no regime bet |
| H > 0.55 | Trending | Strong statistical signal |

**Empirical reality:** SPY (2018–2026) H = 0.451; QQQ H = 0.462 — both
barely distinguishable from random walk long-term. Use **rolling 20–60 day
H** for actionable regime reads, not static calculation.

### Supporting indicators

| Indicator | Mean-reverting signal | Trending signal |
|-----------|----------------------|-----------------|
| SET50 vs 20d MA | Within 1% | > 2% above/below |
| Bollinger Band width | Squeeze (narrow) | Expansion (wide), price outside 2σ |
| OI pattern | Large walls at ATM → pinning | Rising OI in trend direction |
| RSI zone | 40–60 (oscillating) | Consistently > 60 or < 40 |

---

## Strategy families by quadrant

### Q-A: Mean-reverting + High IV ★ — Premium-selling

Best edge. Collect VRP; dealer flow suppresses realized vol.

- [[Iron Condor]] — defined risk, sell both wings outside OI walls.
- [[Short Strangle]] — higher premium, undefined risk (advanced; strict sizing).
- [[Calendar Spread]] — sell near-term high theta, buy back-month.
- [[Covered Call]] / [[Cash-Secured Put]] — income against holdings.

**Entry filter:** IVR > 50 AND IVPCT > 50, ADX < 20, GEX positive, large
OI walls visible at ATM strikes. **Size:** half-Kelly; reduce 25% if
14d ATR > 6-month median ATR.

### Q-B: Trending + Low IV — Directional long

Cheap options; IV can only go up (long vega works for you); ride the move.

- [[Vertical Spread]] (bull call / bear put) — defined risk, directional.
- [[Long Call]] / [[Long Put]] — when IV cheap; max loss = premium only.
- Long futures — when trend confirmed, IV not a factor.

**Entry filter:** IVR < 40, ADX > 25, GEX negative, entry in trend
direction. **Size:** standard; IV is low so option risk is bounded.

### Q-C: Trending + High IV — Difficult; smallest size

IV can spike further; stops hit harder; undefined risk catastrophic here.

- Prefer [[Vertical Spread]] (absorbs further IV spike with defined loss).
- [[Risk Reversal]] — sell OTM put to finance OTM call in trend direction.
- Do **not** sell naked strangles/condors here.

**Size:** quarter-Kelly or less. Only defined-risk structures. Consider
waiting for vol compression before entering directional.

### Q-D: Mean-reverting + Low IV — Long vol / catalyst play

Buy cheap vol; profit from a big move in either direction. Requires a
visible catalyst — without one, you bleed theta for no move.

- [[Long Straddle]] / [[Strangle]] — buy low IV, profit from big move.
- Works into known events: BoT rate decision, SET50 rebalancing, elections.
- **Risk:** IV crush post-event; price may move but premium collapses → loss.

**Size:** standard; but only enter with identified catalyst.

---

## Position sizing by regime

> **Counterintuitive rule:** High IV = SMALLER contracts, not larger.

High IV means wider expected moves → higher risk per contract → must
reduce quantity to maintain consistent dollar risk per trade.

**CME principle:** "When implied volatility is high, the number of contracts
must be reduced" (VaR-based portfolio management rule).

### Kelly-IV hybrid (Wysocki 2025)

Scale Kelly fraction dynamically by IV rank:

| IV Rank | Kelly fraction to use |
|---------|----------------------|
| > 70 | Quarter-Kelly or stand-down from new positions |
| 50–70 | Half-Kelly |
| 30–50 | Half-to-full Kelly (depends on edge confidence) |
| < 30 | Standard Kelly fraction (within risk limits) |

Full Kelly produces 50%+ drawdowns — unacceptable. Half-Kelly captures
~75% of full growth at ~50% of drawdown.

### ATR size adjustment

When 14-day ATR > 6-month median ATR: reduce trade risk by 25–50%.
When 14-day ATR < 6-month median: can use standard or slightly larger size.

### TastyTrade sizing rule

Size each position so the expected move (1 IV standard deviation over the
holding period) does NOT exceed your max planned loss per trade. This
automatically scales down as IV rises.

---

## Regime transition signals

### Trending → Mean-reverting

- ADX declining from 40+ back toward 25 (momentum fading)
- Volume declining on trend continuation (weakening conviction)
- Momentum divergence (RSI / MACD diverging from price direction)
- GEX shifting from negative toward zero or positive
- Bollinger bands contracting after sustained expansion

### Mean-reverting → Trending

- ADX breaking above 20–25 with volume confirmation
- GEX flipping positive → negative (amplification begins)
- Price breaking outside 2nd Bollinger Band with expanding ATR
- Rolling Hurst rising above 0.55 on 60d window
- OI walls breached AND new OI building in breakout direction

> **Warning:** all signals are lagging. Recognition follows the shift.
> Use signals to adjust existing positions; do not use as predictive entry signals.

---

## Thai SET50 market notes

### Volatility index

No official government-published VSETSI. Two research alternatives:
- **TVIX** — CBOE VIX methodology adapted via Black-76 for SET50 European options. Better for option pricing.
- **SEV (Simple Expected Volatility)** — uses 8 near-ATM options. Better for vol forecasting.

**SET50 vol (July 2026, NYU V-Lab AGARCH):** 1d = 13.4%, 1w = 14.0%, 1m = 16.1%.

### Vol persistence — AGARCH finding

SET50 AGARCH persistence parameter > 1.0 = **shocks do not decay quickly.**
Negative returns amplify vol asymmetrically (leverage effect). After a
negative shock, remain in "high IV" positioning longer than US indices
would suggest. Do not rush back to premium-selling after a market drop.

### Election cycle regime shifts

| Event | Average SET50 |
|-------|--------------|
| Parliament dissolution day | +0.9% |
| 1 month post-dissolution | −4.6% avg |
| Max drawdown post-dissolution | 6.4% |

Dissolution = regime shift trigger. Switch to Q-C positioning (smaller size,
defined-risk) for 4–8 weeks post-dissolution. Source: Chulalongkorn University.

### BoT rate decisions

Well-telegraphed; 2026 rate held at 1.00%. Low-surprise events → minimal
regime shift. **Exception:** unexpected cut/hike → trending vol-spike (Q-C).
Watch 5-year Thai government bond yield for rate expectation signals.

### Quarter-end LTF/RMF put flows

Institutional funds hedge via puts in March, June, September, December →
temporary put OI surge → VRP may spike briefly → **false premium-selling
signal.** Wait until 1–2 weeks after quarter-end settlement before entering
short-vol positions.

---

## Daily pre-trade regime check (5 minutes)

1. **IVR and IVPCT** → vol regime classification.
2. **ADX** → trend strength.
3. **GEX sign** → confirms regime; leading signal.
4. **OI walls** → strike selection for condor/strangle, or breakout level for directional.
5. **PCR trend (5d)** → sentiment context (see [[Options Flow Analysis]]).
6. **Calendar check** → BoT meeting, SET rebalancing, election news → adjust regime read.

Cross-reference with [[Daily Routine & Market Prep]] for full session workflow.

---

## Expiry selection by strategy

| DTE | Rationale | Best use |
|-----|-----------|---------|
| 7–21 | Maximum theta decay rate; close at 50% profit | Short premium (condor, strangle) |
| 30–45 | Sweet spot: theta accelerating + room to manage adjustments | Condors, strangles, CSP |
| 60–90 | Back month for calendar; front to back theta differential maximized | Calendar spread (short near, long far) |
| > 90 | Cheap vol budget; vega leverage if vol expands | Long options when IV cheap + directional |

---

## Related

- [[Volatility Risk Premium]] · [[Options Flow Analysis]] · [[Gamma Exposure]] ·
  [[Open Interest]] · [[Edge & Expectancy]] · [[Greeks]] ·
  [[Iron Condor]] · [[Vertical Spread]] · [[Long Straddle]] ·
  [[Pre-Trade Checklist]] · [[Daily Routine & Market Prep]] ·
  [[Position Sizing Frameworks]] · [[Options Strategy]]

## Sources

[^1]: `raw/strategy-selection-framework.md` (deep research version, 2026-07-19)
[^2]: Wysocki (2025), "Sizing the Risk: Kelly, VIX, and Hybrid Approaches in Put-Writing," arXiv:2508.16598.
[^3]: TastyTrade — IV Rank backtested thresholds, 595 symbols (published 2022–2024).
[^4]: CME Group — "Volatility in the Crosshairs: Aligning Volatility and Strategies."
[^5]: Sinclair, *Volatility Trading*, 2nd ed. (2013), Ch. 3 (regime), Ch. 9 (Kelly sizing).
[^6]: Ilmanen, AQR — "Understanding the Volatility Risk Premium" (2012).
[^7]: Vortex Capital Group — "The Hurst Exponent: What H Actually Measures" (2024). SPY/QQQ H values.
[^8]: RegimeForecast.com — "Why Your Strategy Has a 1.8 Sharpe in Trending Markets" (2024). S&P 500 base rates.
[^9]: Wilder, *New Concepts in Technical Trading Systems* (1978) — original ADX.
[^10]: NYU Stern Volatility Lab — SET50 AGARCH model, July 2026 data.
[^11]: Chulalongkorn University — "National Elections and Volatility of Stock Returns: Thailand Case Study."
[^12]: Volatility Box — "IV Rank vs IV Percentile: The Definitive Comparison."
[^13]: SpotGamma — GEX Methodology White Paper.
[^14]: ITI — "Dynamic Position Sizing and Risk Management in Volatile Markets."
