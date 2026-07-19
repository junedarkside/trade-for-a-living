---
title: Edge & Expectancy
type: concept
status: learning
tags: [derivatives, risk]
aliases: [Expectancy, Trading Edge, R-Multiple, WFE]
---

# Edge & Expectancy

**Edge** = strategy generates positive expected value per trade, net of all costs.
**Expectancy** = numerical measure of that edge per trade.

Without edge, no position sizing saves you. With edge, poor sizing still ruins
you. Edge is necessary but not sufficient.

## Expectancy formula

```
Expectancy = (Win% × Avg Win) − (Loss% × Avg Loss)

R-multiple form: Expectancy(R) = Σ(all R-multiples) / total trades
```

**Example:** Win% 40%, Avg Win ฿6,000, Avg Loss ฿2,500
→ (0.40 × 6,000) − (0.60 × 2,500) = **+฿900/trade**

Expectancy describes **long-run average only** — not the path. Two strategies
with identical expectancy can have radically different equity curves. Expectancy
stabilises only after **200+ trades**; < 30 trades = unreliable regardless of P&L.

## R-Multiples (Van Tharp)

**R** = initial risk per trade = entry price − stop-loss.

| Outcome | Meaning |
|---------|---------|
| +3R | Profit = 3× initial risk |
| −1R | Full stop hit |
| +0.5R | Partial win |

R-multiple expectancy normalises for position size variation — cleaner than raw
฿. Viable system benchmark: **mean +0.5R to +2.0R** per trade.

Critical: two systems with identical +0.5R expectancy can differ dramatically in
drawdown if one has a tight bell curve vs one with frequent −1R and rare +10R wins.

## Win rate vs Reward-to-Risk (R:R)

Win rate and R:R trade off — both must combine to positive expectancy:

| Win% | Min R:R for breakeven |
|------|----------------------|
| 70% | 0.43 |
| 50% | 1.00 |
| 40% | 1.50 |
| 30% | 2.33 |
| 20% | 4.00 |

**Critical:** a butterfly with **48% win rate outearned an iron condor with 83%
win rate** by $53/trade on expectancy ($105.60 vs $52.28). Win rate alone is
meaningless — expectancy is the real measure.[^5]

## Empirical win rates (backtested)

Source: TastyTrade 4,872-trade SPY iron condor study (2005–2019); ApexVol.

| Strategy | Entry win% | Managed win% | Rule |
|----------|-----------|-------------|------|
| Iron condor (15–20Δ, 30–45 DTE) | 65–70% | **82%** | Close at 50% profit |
| Short strangle (16Δ, 45 DTE) | 60–65% | **75–80%** | 50% profit / 200% loss stop |
| Short straddle (50% mgmt) | 55–65% | varies | Close at 50% profit |
| Put credit spread (15–20Δ) | 60–70% | ~75% | Close at 50% profit |
| Calendar spread (stable IV) | 55–70% | ~85% | Double calendar variant |

**Closing at 21 DTE** (not expiry) improved Sharpe by ~15–20% across 200,000+
trades.[^2] Avoids gamma risk in the final week.

## VRP edge magnitude

| Metric | Value |
|--------|-------|
| Long-term avg VRP (SPX) | 3–5 vol points |
| Post-2020 avg VRP | 6.5+ vol points |
| Frequency IV > RV (since 1990) | **~85% of observations** |
| VRP half-life (mean reversion) | ~3.1 days |

VRP thresholds for strategy selection:

| VRP | Signal |
|-----|--------|
| > 6 pts | Wide — strong premium-sell |
| 3–6 pts | Normal |
| 0–3 pts | Narrow — poor risk/reward |
| Negative | Buy vol |

VRP is **structurally persistent across decades** — unlike most technical trading
edges which are transient. Most robust single-source options edge available. See
[[Volatility Risk Premium]].

## Sample size requirements

| Trades | Reliability |
|--------|------------|
| < 30 | Unreliable regardless of P&L |
| 30–100 | Rough directional signal only |
| 100 | Edge trend visible |
| **200** | Expectancy stabilises — convincing |
| 500+ | Strong across regimes |

**Formula:**
```
Required n ≈ (1.96 × σ_trade / target_edge)²
```

**Trades-per-parameter rule:** minimum 30 trades per free parameter. 3-parameter
strategy needs ≥ 90 trades minimum. Alternative: ≤ 1 parameter per year of data.

## Walk-forward validation (Pardo)

Split data in-sample / out-of-sample (70/30 or 80/20). Run 20–40 rolling windows.

**Walk-Forward Efficiency (WFE) = OOS return / IS return:**

| WFE | Verdict |
|-----|---------|
| > 70% | Robust |
| 50–70% | Acceptable — passes |
| < 30% | Curve-fitted — discard |

**Acceptable degradation:** Sharpe drops 33–50% IS → OOS is normal.
IS Sharpe 1.5 → OOS ≥ 0.75 acceptable. If OOS < 50% of IS: fail.

**Red flags:**
- IS Sharpe > 3.0 → suspect overfitting (institutional live Sharpe = 1.0–2.5)
- Win rate > 80% → overfitting flag
- CXO Advisory 888-strategy study: IS performance explains only **1–2% of OOS
  behavior** (R² = 0.01–0.02). Intensive backtesting increases overfitting, not robustness.[^9]

## Data-snooping correction

Testing many strategy variants before picking the "best" one inflates the reported expectancy. The more variants tested, the higher the probability of a false positive.

**White's Reality Check (2000):** bootstrap 1,000+ randomised versions. Best real
strategy must beat > 95% of random curves (p < 0.05) to claim true edge.[^10]

**Hansen's SPA Test (2005):** stronger than White's RC — adjusts for correlation
across strategies. Use for comparing multiple candidates.[^11]

**Aronson finding:** in his empirical test of many technical rules, **zero strategies
survived SPA at p < 0.05**. 5+ parameters × 3 years data → 95% probability of
false positive.[^12]

**Practical rule:** if you tested > 20 strategy variants before selecting one, your
reported expectancy is likely inflated.

## Drawdown math

Recovery is non-linear:

```
Required recovery % = Drawdown / (1 − Drawdown)
25% drawdown → need 33% gain to recover
50% drawdown → need 100% gain
75% drawdown → need 300% gain
```

**Triple Penance Rule (Bailey & López de Prado, 2014):** recovery period typically
**2–3× longer** than the drawdown period. 6-month drawdown → 12–18 months to recover.[^13]

**MDD from short history is unreliable:** need 1–2+ years (multiple market cycles)
to estimate true max drawdown.

## Monte Carlo for edge confidence

Randomise: (a) trade sequence — shuffle 1,000–5,000 times; (b) bootstrap with
replacement — resample to new equity curves; (c) timing randomisation — shift
entries ±N days.

**Measures:** median max drawdown (5th/50th/95th percentile), net profit stability,
recovery factor (profit ÷ max drawdown).

Strategies passing 1,000–5,000 Monte Carlo runs show **30–50% lower live failure
rates**.[^8]

## Kelly criterion in practice

```
Kelly fraction f = edge / variance of trade P&L
```

| Fraction | Max drawdown risk | Growth captured |
|----------|-----------------|-----------------|
| Full (100%) | 50–80% | 100% |
| Half (50%) | ~25% | ~75% |
| Quarter (25%) | ~15% | ~55% |

**Thorp (2008):** professional traders almost never use full Kelly. Use ½ to ¼
Kelly as practical compromise. Full Kelly produces catastrophic drawdowns through
normal variance even with genuine edge.[^14]

From expectancy to sizing:
- Compute Kelly f = expectancy / variance
- Apply fractional Kelly (typically ¼ to ½)
- Cross-check against regime sizing rules (see [[Strategy Selection Framework]] — high IV → smaller size)

## Continuous edge tracking

Rolling 30-trade expectancy. Two consecutive negative windows → **stop and review**
before continuing.

**Sharpe ratio of trade P&L stream:**
```
Sharpe = Mean(trade P&L) / StdDev(trade P&L)
```
- > 1.0: good
- > 2.0: very good
- > 3.0: exceptional (or overfit — investigate)

Do NOT add size or change strategy during drawdown — masks edge degradation.

## Edge decay

Options VRP edge: structurally persistent decades-long. Theta decay captures 30–35%
of total premium in the first third of contract life (45→21 DTE). Gamma risk
dominates final third.

Technical/trend edges: regime-dependent, decay faster during strong mean-reversion
periods. No published half-life equivalent to VRP.

TFEX-specific: fill quality degrades as position size grows relative to SET50 options
market depth (< 50-contract single-leg threshold). Monitor actual vs theoretical fill.

## Professional edge validation gate

| Stage | Requirement |
|-------|------------|
| In-sample | WFE > 50%; IS Sharpe < 3.0 |
| Out-of-sample | ≥ 100–200 OOS trades; OOS Sharpe ≥ 50% of IS |
| Snooping test | Passes Hansen's SPA / White's RC at p < 0.05 |
| Regime stability | Consistent across bull/bear/ranging windows |
| Paper trading | Execution validation before live capital |
| Staged deployment | Micro → half → full size |

## Related

- [[Backtesting & Forward Testing]] · [[Position Sizing Frameworks]] ·
  [[Trade Journaling]] · [[Volatility Risk Premium]] ·
  [[Options Risk Management]] · [[Strategy Selection Framework]] ·
  [[Iron Condor]] · [[Short Strangle]]

## Sources

[^1]: `raw/edge-and-expectancy.md` (deep research version, 2026-07-19)
[^2]: TastyTrade — 4,872-trade SPY iron condor study (2005–2019); 200,000+ trade DTE study.
[^3]: Van Tharp Institute — R-multiple system and expectancy definition.
[^4]: Pardo, *Design, Testing, and Optimization of Trading Systems*; bettersystemtrader.com ep. 60.
[^5]: OptionsPilot — butterfly vs iron condor expectancy comparison ($105.60 vs $52.28).
[^6]: ApexVol — iron condor and credit spread win-rate data (2026).
[^7]: Moontower Meta + SpotGamma — VRP magnitude; IV > RV 85% of observations; VRP half-life 3.1d.
[^8]: BacktestBase — Monte Carlo 30-point robustness system; 30–50% failure rate reduction.
[^9]: CXO Advisory — 888-strategy IS vs OOS study (R² = 0.01–0.02).
[^10]: White (2000), "A Reality Check for Data Snooping," *Econometrica* 68(5), 1097–1126.
[^11]: Hansen (2005), "A Test for Superior Predictive Ability," *Journal of Business & Economic Statistics* 23(4).
[^12]: Aronson, *Evidence-Based Technical Analysis* (2006), Ch. 6 — SPA test application.
[^13]: Bailey & López de Prado (2014), "The Deflated Sharpe Ratio" + Triple Penance Rule.
[^14]: Thorp (2008), "The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market."
