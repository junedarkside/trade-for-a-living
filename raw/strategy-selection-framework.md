---
title: Strategy Selection Framework
source: Deep research — Wysocki (2025) arXiv:2508.16598, TastyTrade backtested thresholds (595 symbols), CME Group education, Euan Sinclair "Volatility Trading" 2nd ed., Ilmanen AQR 2012, Vortex Capital Hurst exponent analysis, RegimeForecast S&P 500 base rates, Chulalongkorn University Thai election study, NYU V-Lab SET50 AGARCH, Wilder ADX original, SpotGamma GEX methodology
date: 2026-07-19 (deep research upgrade)
---

# Strategy Selection Framework — Deep Research Notes

## The core question

Which strategy to trade = function of the current regime. Three dimensions:
1. **Direction** — up / down / neutral / unknown
2. **Volatility** — IV cheap or expensive relative to history (VRP)?
3. **Trend regime** — trending or mean-reverting?

Regime misalignment is the primary source of strategy losses — even a correct strategy in the wrong regime loses.

---

## Dimension 1: Volatility Regime

### IV Rank vs IV Percentile — they are NOT the same

**IV Rank:**
```
IV Rank = (Current IV − 52w Low) / (52w High − 52w Low) × 100
```
- Range: 0–100
- Fast, reactive — responds quickly to new extremes
- Weakness: one extreme high can skew the range for 52 weeks; current "middle" reading looks low even if IV is historically high

**IV Percentile (IVPCT):**
```
IV Percentile = % of trading days in past 252 days where IV was below today's IV
```
- Range: 0–100
- Slower, more robust — counts actual frequency
- Weakness: can be slow to signal after sustained vol regime change
- Strength: not distorted by single vol spike

**Why both matter:**
- After a vol spike: IV Rank may read 40 (seems neutral), IVPCT may read 75 (still historically elevated). IVPCT is correct signal.
- In calm markets: both converge. Single signal reliable enough.
- **Confirmation rule:** use BOTH > 50 for premium-selling entry, not just one.

### Quantitative thresholds (backtested)

Source: TastyTrade backtested 595 symbols across multiple years.

| IV Rank | IV Percentile | Reading | Strategy |
|---------|--------------|---------|----------|
| > 70 | > 70 | Very rich — premium-selling peak | Short strangle / condor; quarter-Kelly sizing |
| > 50 | > 50 | Elevated — premium-selling zone | Iron condor, CSP, covered call; half-Kelly |
| 30–50 | 30–50 | Neutral | Light sizing or wait |
| < 30 | < 30 | Cheap vol | Long straddle/strangle with catalyst; larger Kelly fraction |

**Backtested result:** iron condors entered when BOTH IV Rank > 50 AND IV Percentile > 50 produced 56.8% win rate vs 48.2% without the vol filter. Above 50 threshold produces 73% win rate on strangles (TastyTrade published data).

**Academic thresholds:** CBOE-cited research uses trailing 252d VIX distribution: 33rd percentile = low, 67th = high, 90th ≈ crisis (historically ~29.1 VIX).

### VRP structural edge

IV overstates realized volatility approximately 85% of the time (structural premium). This is the basis of premium-selling edge. NOT a guarantee of quiet markets — the 15% of the time IV is too low includes crashes. See [[Volatility Risk Premium]] for full framework.

---

## Dimension 2: Trend Regime

### ADX (Average Directional Index)

**Industry standard thresholds (Wilder, modernized):**
- ADX > 25: strong trending
- ADX 20–25: transition / weakening
- ADX < 20: range-bound / mean-reverting

**Origin:** Wilder (1978) introduced ADX but did not specify 25 as the threshold — this emerged as practitioner consensus. Some use ADX > 20 as stricter mean-reverting cutoff to reduce whipsaws.

**Limitation:** ADX is lagging. It confirms a trend already established, not one starting.

### Hurst Exponent (H) — statistical classifier

The Hurst exponent measures the degree of long-range dependence in a time series:

```
H < 0.45  →  Mean-reverting (strong statistical signal)
0.45–0.55 →  Random walk / indeterminate (reduce size or stand aside)
H > 0.55  →  Trending (persistent momentum)
```

**Empirical reality for equity indices (Vortex Capital Group analysis, 2018–2026):**
- SPY: H = 0.451 (barely statistically distinguishable from random walk)
- QQQ: H = 0.462 (same)

Implication: **major equity indices are near-random walk long-term.** Short-term (rolling 20–60 day windows) H fluctuates more meaningfully and gives actionable reads. Use rolling H, not static.

### ADF Test (Augmented Dickey-Fuller)

Formal statistical test for stationarity (mean-reversion):
- p-value < 0.05 → reject null → stationary → **mean-reverting**
- p-value > 0.10 → accept null → non-stationary → **trending**

Practical use: run on rolling 60-day window of SET50 index. More rigorous than ADX but requires statistical software. Use for confirming a period's regime classification in backtesting.

### GEX sign (Gamma Exposure)

- **Positive GEX:** dealers net long gamma → buy dips, sell rallies → **suppresses** moves → mean-reverting regime
- **Negative GEX:** dealers net short gamma → forced to buy/sell in trend direction → **amplifies** moves → trending regime
- **Zero / flip level:** regime transition marker. Crossing negative → positive = suppression begins.

GEX is **leading or coincident** (vs ADX which is lagging). High actionability for short-term regime identification.

### Bollinger Band width

Narrow band (squeeze) = low realized vol = mean-reverting conditions forming.
Band expansion = trending. Expansion breaking 2nd band (2σ) = trend signal.

### Regime base rates (S&P 500, 2000–2024)

Source: RegimeForecast.com / published regime analysis.

| Regime | % of time |
|--------|-----------|
| Trending low-vol | 38% |
| Choppy elevated-vol | 29% |
| Crisis/high-vol trend | 14% |
| Range-bound low-vol | 19% |

Trending total: ~52%. Mean-reverting/choppy: ~48%. **Not 80/20 as commonly assumed.** QE era (2010–2019) was unusually trend-dominated — backtest results from that period overstate trend-following edge.

**Strategy Sharpe ratio by regime:** momentum strategy showed Sharpe 1.82 in trending vs −0.41 in choppy conditions (RegimeForecast). This magnitude of difference explains why regime identification matters more than strategy selection within a regime.

---

## Regime Transition Signals

### Trending → Mean-reverting
- ADX declining from 40+ toward 25 (momentum fading)
- Volume declining on trend continuation (weakening conviction)
- Momentum oscillators diverging from price (RSI/MACD divergence)
- GEX shifting from negative toward zero or positive
- Bollinger bands contracting after expansion

### Mean-reverting → Trending
- ADX breaking above 20–25 with volume confirmation
- GEX flipping from positive to negative (dealers switch to amplifying)
- Price breaking outside 2nd Bollinger Band with expanding ATR
- Rolling Hurst rising above 0.55 on 60d window
- OI shift: large OI walls breached + new OI building in trend direction

**Critical limitation:** all indicators are lagging. Regime is recognized after the shift, not before. Use transition signals to adjust, not to predict.

---

## Position Sizing by Volatility Regime

### The counterintuitive rule

**High IV → SMALLER contracts, not larger.**

High IV means:
- Higher premium per contract (good)
- Wider expected moves (bad — risk increases proportionally)
- Higher max loss if breached

**CME principle:** "When implied volatility is high, the number of contracts must be reduced" to maintain consistent VaR (Value at Risk) limits. This is a portfolio management rule, not a preference.

### Kelly-IV hybrid framework (Wysocki 2025)

Source: Wysocki (2025), "Sizing the Risk: Kelly, VIX, and Hybrid Approaches in Put-Writing on Index Options," arXiv:2508.16598.

Dynamic Kelly fraction scaling by IV rank:
- Full Kelly: 50%+ drawdowns → unacceptable
- **Half-Kelly:** captures ~75% of full Kelly growth with ~50% of drawdown
- **Quarter-Kelly:** conservative starting point for retail
- **IV Rank > 70 → quarter-Kelly or stand-down from new positions**

VIX-rank scaling rule: as IV rank rises, fraction shrinks. At IV rank 80, use ¼ to ⅓ of normal position size. At IV rank 30, can use up to full normal size.

### ATR-based adjustment rule

Source: ITI (International Trading Institute).

When 14-day ATR > 6-month median ATR → elevated realized vol → **reduce trade risk by 25–50%**.
When 14-day ATR < 6-month median ATR → compressed vol → can increase to normal or slightly above.

### Position sizing by quadrant

| Quadrant | Vol | Trend | Sizing rule |
|----------|-----|-------|-------------|
| **A** (mean-rev + high IV) | High | Range | Fewer contracts; half-Kelly. ATR check: reduce 25% if elevated. |
| **B** (trending + low IV) | Low | Trending | Standard sizing; IV cheap so risk limited; let winners run |
| **C** (trending + high IV) | High | Trending | Smallest size; defined-risk only; half-Kelly or less |
| **D** (mean-rev + low IV) | Low | Range | Standard size; catalyst required; don't force entry |

**TastyTrade rule:** size so the expected move (1 std dev in IV terms) does NOT exceed your planned max loss per trade.

---

## Thai SET50 Market Specifics

### Volatility index

No official government-published VSETSI exists. Two researcher-developed alternatives:
- **TVIX** — adapted from CBOE VIX methodology using Black-76 model for European SET50 options. Better for option pricing.
- **SEV (Simple Expected Volatility Index)** — uses 8 near-ATM SET50 options (4 calls, 4 puts). Simpler, but better at forecasting expected volatility.

Source: Chulalongkorn University / NIDA Finance research.

**SET50 vol levels as of July 2026 (NYU V-Lab AGARCH):**
- 1-day: 13.42%
- 1-week: 13.99%
- 1-month: 16.09%

### Vol persistence — AGARCH model finding

SET50 exhibits non-stationary volatility persistence (AGARCH persistence parameter > 1.0). Meaning:
- Volatility shocks do NOT decay quickly to baseline — they persist
- Negative returns amplify volatility asymmetrically (leverage effect)
- Implication for strategy selection: after a vol spike (negative shock), remain in "high vol" positioning longer than you might with US indices. Don't rush back to premium-selling after a drop.

Source: NYU Stern Volatility Lab, SET50 AGARCH model.

### Election cycle regime shifts

Source: Chulalongkorn University study on Thai elections and stock market.

| Event | Average SET50 return |
|-------|---------------------|
| Parliament dissolution day | +0.9% |
| 1 month after dissolution | −4.6% average |
| Max drawdown after dissolution | 6.4% |

**Implication:** dissolution is a regime shift trigger. Switch from premium-selling to smaller size or defined-risk structures. High-vol, trending conditions likely for 4–8 weeks post-dissolution.

### BoT rate decisions

Bank of Thailand rate decisions are typically well-telegraphed (unanimous votes, policy guidance). As of June 2026: 1.00% hold, expected to hold through 2026. Low-surprise events in normal conditions → minimal regime shift. **Exception:** unexpected cut/hike creates trending vol-spike regime (Quadrant C).

### Quarter-end LTF/RMF flows

Institutional mutual funds (LTF/RMF) hedge equity positions via puts near quarter-end (March, June, September, December). Creates systematic put OI buildup → VRP signal may spike briefly → premature premium-selling entry. Wait for post-quarter-end settlement before entering short-vol positions in these months.

---

## The 2×2 Regime Matrix (Calibrated)

```
                    VOLATILITY REGIME
               Low IV (IVR<30, IVPCT<30)    High IV (IVR>50, IVPCT>50)
              ┌──────────────────────────┬──────────────────────────────┐
  TRENDING    │ Buy directional (Q-B)    │ Smallest size (Q-C)          │
  ADX>25      │ Vert spread, Long call/  │ Defined-risk only            │
  GEX neg     │ put, Long futures         │ Risk reversal; wait for      │
              │ Standard sizing           │ vol compression              │
              ├──────────────────────────┼──────────────────────────────┤
  MEAN-REV    │ Long vol/catalyst (Q-D)  │ SHORT PREMIUM ★ (Q-A)        │
  ADX<20      │ Long straddle/strangle   │ Iron condor, strangle,       │
  GEX pos     │ Standard size            │ calendar, covered call       │
              │ Catalyst required        │ Half-Kelly, ATR-adjusted     │
              └──────────────────────────┴──────────────────────────────┘
                                           ★ Highest-edge quadrant
```

---

## Sources

- Wysocki (2025), "Sizing the Risk: Kelly, VIX, and Hybrid Approaches in Put-Writing on Index Options," arXiv:2508.16598
- TastyTrade — IV Rank backtested thresholds (595 symbols, published 2022–2024)
- CME Group — "Volatility in the Crosshairs: Aligning Volatility and Strategies" (education)
- Euan Sinclair, *Volatility Trading*, 2nd ed. (2013), Chapters 3, 9
- Ilmanen, AQR — "Understanding the Volatility Risk Premium" (2012)
- Vortex Capital Group — "The Hurst Exponent: What H Actually Measures" (2024)
- RegimeForecast.com — "Why Your Strategy Has a 1.8 Sharpe in Trending Markets and -0.4 in Everything Else" (2024)
- Wilder, J.W., *New Concepts in Technical Trading Systems* (1978) — original ADX
- NYU Stern Volatility Lab — SET50 AGARCH model, July 2026 data
- Chulalongkorn University Digital — National Elections and Volatility of Stock Returns: Thailand Case Study
- Volatility Box — "IV Rank vs IV Percentile: The Definitive Comparison"
- SpotGamma — GEX Methodology White Paper
- ITI (International Trading Institute) — Dynamic Position Sizing in Volatile Markets
