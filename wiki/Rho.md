---
title: Rho
type: greek
status: learning
aliases: [ρ, rho]
tags: [options, derivatives, greek/rho]
---

# Rho

**ρ — sensitivity to interest rates.** How much the option's price changes for
a **1% change in the risk-free rate**. Usually the smallest of the five Greeks
for short-dated options.

## Definition
```
ρ = ∂P / ∂r
```
Where r = risk-free rate (decimal, e.g. 0.025 for 2.5%).

## Sign convention
- **Long call**: **positive rho** — higher rates raise call value (cost-of-carry
  raises the forward).
- **Long put**: **negative rho** — higher rates lower put value.
- **Stock / futures**: zero rho (no expiration).

## Long-holder meaning

Rho mostly matters in **rate-sensitive environments**:
- Long-dated options (LEAPS, 1+ year to expiry).
- Environments with **big rate moves** (Fed hikes/cuts, central bank policy changes).
- **Futures options** (Black model) — rates directly enter pricing.

For short-dated equity options (≤ 60 days), rho is typically tiny — a few cents
per 1% rate move on a $3 premium. Often ignored in day-to-day decisions.

## Behavior over time and with spot

| Time to expiry | |Rho| |
|----------------|---------|
| Short dated (≤ 30d) | **small** |
| Medium (30–180d) | moderate |
| Long dated (LEAPS, 1y+) | **largest** — most sensitive to rate moves |

ATM options have the highest |rho|; deep ITM/OTM less so.

## Practical use

1. **LEAPS pricing** — when pricing or hedging long-dated options, rho matters.
2. **Rate-regime trades** — if you expect the Fed to hike rates significantly,
   long calls benefit (positive rho); long puts hurt (negative rho).
3. **Index options** — more rate-sensitive than single-stock options because
   the carry component (no dividends but financing cost) is meaningful.
4. **Ignoring rho** — usually fine for short-dated equity/futures options. Don't
   over-engineer; focus on delta, gamma, theta, vega first.

### Trading-focused rho ranking

- **Mostly relevant for long-dated options (LEAPS)** and environments with
  large or fast rate moves. For short-dated equity/index options, rho is
  typically small (a few cents per 1% rate move on a $3 premium).
- **Index options > single-stock options** for rho sensitivity — the carry
  component (financing cost) is meaningful; single-stock dividends absorb some
  of the rate effect.
- **Practical ranking** (most to least impact for typical retail traders):
  delta → gamma → theta → vega → **rho last**. Focus your mental model on the
  first four; only re-engage rho for LEAPS or rate-regime trades.

For the trader-focused framework (where rho fits in the practical checklist): see [[Greeks in Practice]].

## Related
- [[Greeks]] (hub) · [[Delta]] · [[Theta]] · [[Vega]] ·
  [[Position Greeks]] · [[Black Model]] (rho enters pricing)

## Sources
[^1]: `raw/greeks-overview.md`
[^2]: learnsignal.com — Greeks options trading.
[^3]: wealthsimple.com — option Greeks.