---
title: Edge & Expectancy
source: Deep research — Van Tharp R-multiples (vantharpinstitute.com); TastyTrade 4,872-trade iron condor study; ApexVol strategy win-rate data; Pardo walk-forward rules (bettersystemtrader.com); Aronson "Evidence-Based Technical Analysis" SPA test; White (2000) Reality Check; Kelly criterion (Thorp 2008); Bailey & López de Prado Triple Penance Rule (2014); Monte Carlo methodology (BacktestBase 30-point system); VRP half-life (SpotGamma); CXO Advisory 888-strategy study
date: 2026-07-19 (deep research upgrade)
---

# Edge & Expectancy — Deep Research Notes

## Definition

**Edge** = strategy generates positive expected value (EV) per trade, net of all costs.
**Expectancy** = numerical measure of that edge per trade.

Without edge, no position sizing saves you. With edge, poor sizing still ruins you.

---

## Expectancy formula

Standard formulation (all rigorous sources converge on same 4-variable form):

```
Expectancy = (Win% × Avg Win) − (Loss% × Avg Loss)

Equivalent in R-multiple form:
Expectancy(R) = Σ(all R-multiples) / total trades
```

Key: expectancy describes **long-run average only** — not the path. Two strategies with identical expectancy can have radically different equity curves based on result distribution. Expectancy stabilises only after 200+ trades; <30 trades = variance too high for reliable inference.

---

## R-Multiples (Van Tharp)

**R** = initial risk per trade = entry price − stop-loss level.

An outcome of +3R = profit equals 3× initial risk. −1R = full stop hit.

R-multiple expectancy = sum of all R outcomes ÷ number of trades. Cleaner than raw ฿ because it normalises for position size variation.

**Viable system benchmarks:**
- +0.5R to +2.0R per trade mean → viable directional edge
- Positive expectancy with Sharpe > 1.0 on R-stream → strong system

Key insight: the R-multiple distribution shape matters, not just the mean. Two systems with +0.5R expectancy: one with tight bell curve vs one with frequent −1R and rare +10R have identical expectancy but completely different drawdown profiles.

---

## Empirical win rates (backtested)

Source: TastyTrade 4,872-trade SPY iron condor study (2005–2019); ApexVol; OptionsPilot backtests.

| Strategy | Entry win rate | Managed win rate | Management rule |
|----------|---------------|-----------------|-----------------|
| Iron condor (15–20Δ, 30–45 DTE) | 65–70% | **82%** | Close at 50% profit |
| Short strangle (16Δ, 45 DTE) | 60–65% | **75–80%** | Close at 50% profit, 200% loss stop |
| Short straddle (50% mgmt) | 55–65% | varies | Close at 50% profit |
| Put credit spread (15–20Δ) | 60–70% | ~75% | Close at 50% profit |
| Calendar spread (stable IV) | 55–70% | ~85% | double calendar variant |

**Critical finding:** a butterfly with 48% win rate outearned an iron condor with 83% win rate on per-trade expectancy ($105.60 vs $52.28). Win rate alone is meaningless. Expectancy is the real measure.

**Closing at 21 DTE** (not expiry): improved Sharpe by ~15–20% across 200,000+ trades (TastyTrade). Avoids gamma risk in final week.

---

## VRP edge magnitude

Source: Moontower Meta, SpotGamma, SSRN empirical papers.

| Metric | Value |
|--------|-------|
| Long-term average VRP (SPX) | 3–5 vol points |
| Post-2020 average VRP | 6.5+ vol points |
| Frequency IV > RV (since 1990) | ~85% of observations |
| VRP half-life (mean reversion) | ~3.1 days |

**Regime thresholds:**
- VRP > 6 pts: wide — high short-vol hit rate
- VRP 3–6 pts: normal
- VRP 0–3 pts: narrow — poor risk/reward for premium selling
- VRP negative: buy vol

VRP is structurally persistent across decades (unlike most technical trading edges which are transient). Most robust option-selling edge source available.

---

## Sample size requirements

| Trades | Reliability |
|--------|------------|
| < 30 | Statistically unreliable regardless of P&L |
| 30 | Rough directional signal only |
| 100 | Data usable; edge trend visible |
| 200 | Convincing evidence; expectancy stabilises |
| 500+ | Strong statistical significance across regimes |

**Formula:**
```
Required n ≈ (Z_α × σ_trade / target_edge)²
Z_α = 1.96 for 95% confidence
```

**Practical:** most retail traders never reach n=200 in a single strategy with consistent setup/sizing. This is why walk-forward testing and OOS validation are critical — don't rely on live-trading sample alone.

**Trades-per-parameter rule (overfitting guard):** minimum 30 independent trades per free parameter. A 3-parameter strategy needs ≥90 trades. Alternative: 1 parameter per year of historical data.

---

## Walk-forward validation (Pardo)

In-sample / out-of-sample split rules:
- Standard ratio: 70/30 or 80/20 IS:OOS
- Run 20–40 rolling windows
- Preferred: rolling (not anchored) windows to test across multiple regimes

**Walk-Forward Efficiency (WFE) = OOS return / IS return:**

| WFE | Interpretation |
|-----|---------------|
| > 70% | Strong robustness |
| 50–70% | Acceptable — passes |
| < 30% | Strong curve-fitting evidence — discard |

**Acceptable OOS degradation:** expect Sharpe to drop 33–50% from IS to OOS. IS Sharpe 1.5 → OOS ≥ 0.75 acceptable. If OOS < 50% of IS: fail.

**Suspicious signals:**
- IS Sharpe > 3.0 → almost certainly overfit (institutional quant benchmark: live Sharpe 1.0–2.5)
- Win rate > 80% → overfitting flag
- P&L explained: CXO Advisory 888-strategy study: in-sample performance explains only 1–2% of out-of-sample behavior (R² = 0.01–0.02). Intensive backtesting increases overfitting, NOT robustness.

---

## Data-snooping bias correction

**White's Reality Check (2000):** bootstrap 1,000+ randomised versions of the tested strategy. Best real strategy should beat >95% of random curves to claim true edge (p < 0.05).

**Hansen's SPA Test (2005):** superior to White's RC. Adjusts for correlation between strategies; avoids least-favorable configuration bias. Identifies genuine outperformers after multiple comparisons.

**Aronson finding (EBTA):** testing many rules with 5+ parameters across 3 years of data → 95% probability of false positive. In his empirical test of multiple technical rules, zero strategies survived SPA at p < 0.05.

**Practical rule:** if you tested more than 20 strategy variants before picking the "best" one, your reported expectancy is likely inflated by data-snooping.

---

## Drawdown math

**Recovery is non-linear:**
```
Required recovery = Drawdown / (1 − Drawdown)
Example: 50% drawdown → need 100% gain to recover
         25% drawdown → need 33% gain
```

**Triple Penance Rule (Bailey & López de Prado, 2014):** recovery period typically 2–3× longer than the drawdown period. A 6-month drawdown may take 12–18 months to recover.

**MDD from short history is unreliable:** 6 months of data underestimates true max drawdown. Need 1–2+ years (multiple market cycles) for reliable MDD estimate.

---

## Monte Carlo for edge confidence

Randomize: (a) trade sequence — shuffle historical trades 1,000–5,000 times; (b) resampling with replacement — bootstrap new equity curves; (c) entry/exit timing — randomise by N days.

**Metrics measured:**
- Median max drawdown + 5th/50th/95th percentile
- Net profit stability across runs
- Recovery factor (profit ÷ max drawdown)

**BacktestBase 30-point robustness system:**
- Drawdown 0–25% = 3–5 pts; 25–50% = 1–3 pts; >50% = <1 pt
- Recovery factor ≥ 4.0 = 5 pts
- A+ grade ≥ 28/30; F ≤ 9.9/30; Auto-fail = median drawdown >100%

**Industry standard:** strategies passing 1,000–5,000 Monte Carlo runs show 30–50% lower live failure rates.

---

## Kelly criterion in practice

```
Kelly fraction f = edge / variance of trade P&L
```

| Kelly fraction | Max drawdown risk | Growth captured |
|---------------|------------------|-----------------|
| Full (100%) | 50–80% | 100% |
| Half (50%) | ~25% | ~75% |
| Quarter (25%) | ~15% | ~50–60% |

**Thorp (2008) recommendation:** use ½ to ¼ Kelly. Professional traders almost never use full Kelly. At full Kelly, even genuine edge produces catastrophic drawdowns through normal variance.

**Practical:** with iron condor expectancy ฿200/trade and σ = ฿2,000, Kelly f = 200/4,000,000 = 0.005% per unit of capital. Scale to account risk accordingly; this naturally produces very small position sizes relative to capital.

---

## Continuous edge tracking

Rolling 30-trade expectancy. If negative for 2+ consecutive windows → stop and review.

Do NOT add size or change strategy during drawdown — masks edge degradation vs normal variance.

**Sharpe ratio of trade stream:**
```
Sharpe = (Mean trade P&L − risk-free rate) / StdDev(trade P&L)
```
- > 1.0: good
- > 2.0: very good
- > 3.0: exceptional (or possibly overfit)

---

## Professional edge validation gate (quant standard)

| Stage | Requirement |
|-------|------------|
| In-sample | WFE > 50%; Sharpe < 3 (not suspicious) |
| Out-of-sample | ≥ 100–200 OOS trades; OOS Sharpe ≥ 50% of IS |
| Data-snooping | Passes SPA/White's RC at p < 0.05 |
| Regime stability | Consistent across bull/bear/ranging windows |
| Capacity | Edge persists at intended position size |
| Paper trading | Full execution validation, latency benchmarks |
| Staged deployment | Micro → half → full size |

---

## Sources

- Van Tharp Institute — R-multiple system (vantharpinstitute.com)
- TastyTrade — 4,872-trade iron condor study (SPY, 2005–2019); 200,000+ trade DTE study
- ApexVol — iron condor, credit spread win-rate data (2026)
- Pardo, *Design, Testing, and Optimization of Trading Systems* + bettersystemtrader.com podcast
- White (2000), "A Reality Check for Data Snooping," Econometrica 68(5)
- Hansen (2005), "A Test for Superior Predictive Ability," Journal of Business & Economic Statistics
- Aronson, *Evidence-Based Technical Analysis* (2006) — SPA test application, multiple rules study
- CXO Advisory — 888-strategy IS vs OOS study (R² = 0.01–0.02)
- Bailey & López de Prado (2014), "The Deflated Sharpe Ratio" + Triple Penance Rule
- Thorp (2008), "The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market"
- BacktestBase — Monte Carlo 30-point robustness system
- SpotGamma — VRP half-life (~3.1 days)
- Moontower Meta — VRP magnitude (IV overstates RV 85% of time)
- OptionsPilot — calendar/butterfly/condor expectancy comparison ($105.60 vs $52.28)
