---
title: Options Risk Management
type: concept
status: reviewed
tags: [options, derivatives, risk]
---

# Options Risk Management

**Practical playbook for managing risk on options trades.** Companion to
[[Risk Management]] (conceptual hub: risk hierarchy, drivers). This article is
the **HOW** — sizing formulas, exit-rule taxonomy, hedging toolkit, pre-trade
checklist.

## Overview
Managing risk on options = **controlling max loss per trade** + using
**defined-risk structures** + sizing positions conservatively + having clear
**exit and hedging rules** before entry. No strategy survives without these.

## Risk per trade & per portfolio

**Per trade**: fixed % of equity, **0.5–2%**. Measure as **max possible loss**
of the strategy, not premium or margin.

**Worked example**:
- Account: ฿1,000,000. Risk: 1% = **฿10,000/trade**.
- Strategy max loss: ฿2,000/lot.
- Allowed size: 10,000 ÷ 2,000 = **5 lots**.

**Portfolio cap**: total max loss across all open trades ≤ **5–10% of equity**.
Avoid correlated blow-ups (all short premium on the same event, all long calls
on tech earnings, etc.).

## Prefer defined-risk structures

| Structure | Max loss | Notes |
|-----------|----------|-------|
| [[Vertical Spread]] | Defined | Bull call, bear put; cheapest directional. |
| [[Iron Condor]] / [[Iron Butterfly]] | Defined | Range-bound income; spread margin. |
| [[Butterfly Spread]] | Defined | Pin to middle strike. |
| [[Calendar Spread]] / [[Diagonal Spread]] | Defined | Time-decay / skew plays. |
| [[Collar]] | Defined | Long + long put + short call; zero-cost variant. |

**Avoid / strictly limit**: naked short calls/puts (unlimited or very large
risk), oversized directional bets without stops.

**Before entering, always know**:
- Max profit
- Max loss
- Break-even points
- What market view the trade expresses

## Position sizing formula

```
Lots = risk_per_trade ÷ max_loss_per_lot,  rounded down
```

**Worked example**:
- Account: ฿500,000. Risk: 1% = ฿5,000.
- Iron condor max loss: ฿8,000/lot.
- 5,000 ÷ 8,000 = 0.625 → **0 lots** (trade smaller, reduce risk, or skip).

This rule alone prevents most account-killing trades.

## Exit rules (3 types — set BEFORE entry)

**Price-based**:
- Underlying hits technical level (support/resistance, trendline break).
- Option premium stop (e.g., −50%) or profit target (+50–100%).

**Time-based**:
- Close before known events (earnings, policy decisions).
- Exit X days before expiry to avoid gamma blow-up (especially 0DTE).

**Greeks-based**:
- Delta too large → position has become more directional than intended.
- Theta too costly → holding period exceeds thesis horizon.
- Vega too high in a vol regime → exposure you can't monitor.

**Write the rules down.** Verbal-only rules get abandoned under stress.

## Stop-losses by position type

| Position | Stop-loss anchor | Adjustment |
|----------|------------------|------------|
| Long options | Premium drop 40–60% OR underlying technical break | Tighter for high-theta near expiry |
| Short options / spreads | Net debit/credit level OR underlying level invalidating thesis | Wider in high vol; tighter near expiry |
| Multi-leg | Net package level (mental stops + alerts if broker doesn't support conditional orders) | Adjust per vol regime |

## Hedging toolkit

- **[[Protective Put]]** — own stock/future + long put. Caps downside; cost = premium. For high-conviction longs you don't want to sell.
- **[[Covered Call]]** — own stock/future + short call. Income; caps upside.
- **[[Collar]]** — long + long put + short call. Floor + ceiling; often low net cost.
- **Convert naked → spread** (the most powerful risk tool):
  - Long call → **bull call spread** (sell higher-strike call). Reduces net premium and max loss.
  - Naked short call → **call spread** (buy higher-strike call). Caps otherwise-unlimited risk.
  - Long put → **bear put spread**. Same idea on the put side.
  - Naked short put → **put spread**. Caps strike-side risk.

## Diversification

| Dimension | What to vary |
|-----------|--------------|
| **Strategy** | Mix income (covered calls, condors), directional (spreads), hedging (protective puts). |
| **Underlying** | Different sectors, indices, asset classes — one event doesn't wipe the book. |
| **Expiry** | Stagger weekly/monthly so all positions don't decay or pin at once. |

## Leverage & overtrading

- Limit lots by formula above.
- Avoid 0DTE unless you fully understand gamma risk.
- Avoid impulse trades; focus on quality setups.
- Rule: **"if you wouldn't take the trade at half size, don't take it at all."**

## Scenario & stress tests

Before entry, run through:

| Scenario | Question |
|----------|----------|
| Large gap | What if underlying moves ±5–10% overnight? |
| Vol shock | What if IV spikes or collapses by 20–30%? |
| Time bleed | What if market stays flat 5–10 days? |

Use option calculators + Greeks ([[Delta]], [[Gamma]], [[Theta]], [[Vega]]).
If the worst-case outcome is unacceptable → reduce size or skip.

## Pre-trade checklist

Before every options trade, answer:

1. **Market view** (direction, vol, time)?
2. **Strategy** fits view with **defined risk**?
3. **Max profit, max loss, break-evens**?
4. **Capital risked** (% and absolute)?
5. **Exit rules** (price, time, Greeks, P&L)?
6. **Fit** with other open positions?
7. **Stress scenario** outcome acceptable?

If you can't answer clearly → the trade isn't ready.

See [[Pre-Trade Checklist]] for a printable one-page reference.

## Related
- [[Risk Management]] (conceptual hub) · [[Pre-Trade Checklist]] (quick reference) ·
  [[Options Strategy]] · [[Multi-Strategy Options]] ·
  [[Greeks]] · [[Greeks in Practice]] · [[Position Greeks]] ·
  [[Vertical Spread]] · [[Iron Condor]] · [[Covered Call]] · [[Protective Put]] ·
  [[Collar]] · [[Long Straddle]]

## Sources
[^1]: `raw/options-risk-management.md`
[^2]: capmint.com — options risk management.
[^3]: insiderfinance.io — mastering risk management in options trading.
[^4]: wrightresearch.in — risk management in options trading.
[^5]: moomoo.com — risk management in options trading.
[^6]: tradingpartner.in — options trading risk management strategies.