---
title: Cash-Secured Put
type: strategy
status: learning
aliases: [CSP]
tags: [options, derivatives, strategy/income, market/thailand]
---

# Cash-Secured Put

**Income strategy.** You sell (write) a put while holding the full cash needed
to buy the shares if assigned. You collect premium now; in exchange you oblige
yourself to buy the stock at the strike if it falls below it.

## Overview
Neutral-to-mildly-bullish income or "get paid to wait" play. Use it on a stock
you **want to own** at a lower price — if assigned, you buy at the strike (minus
premium); if not, you keep the premium.

## Legs

| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | Short (write) | Put | Below spot (OTM) | 30–45 days typical |
| — | Hold cash | = strike × 100 per contract | — | — |

## Max loss
**(Strike − Premium) × 100** per contract (if stock → 0).
- Capped only at zero. Being assigned at the strike above a crashed market is
  the real risk — the stock can keep falling after you own it.

## Max profit
**Premium received.**
- Capped: yes — the premium is the most you earn.

## Breakeven
**Strike − Premium.**

## Greeks behavior
- **Delta**: positive (short put) — want stock up or flat.
- **Gamma**: short — delta grows against you as stock falls.
- **Theta**: **positive** — time decay is your income.
- **Vega**: short (negative) — rising IV hurts the short put.

## Payoff shape (at expiry)
```
P&L
 │________________  ← flat profit = premium (stock ≥ strike)
 │
 │\
 │ \  ← below strike, losses grow like long stock
 ┼──────────── Strike − Premium (breakeven)
```

## When to use
- Neutral to mildly bullish; willing to own the stock at the strike.
- Want income in a flat/slowly-rising market.
- Targeting a lower entry price than today's spot.

## Risks
- **Downside large** — you own the stock at the strike if it dumps; only the
  premium cushions.
- **Early assignment** — puts can be assigned early (American style), especially
  deep ITM or near dividend.
- **Opportunity cost** — cash tied up as collateral.

## Example — SET50 / SET
- Want to buy a SET stock now at ฿100, willing to own at ฿95.
- Write 1 put, strike ฿95, 35 days out, collect ฿2.00/share = ฿200 premium,
  hold ฿9,500 cash.
- **Max profit**: ฿200.
- **Max loss**: (95 − 2) × 100 = ฿9,300 (stock to zero).
- **Breakeven**: 95 − 2 = ฿93.
- Stock > 95 → keep premium. Stock ≤ 95 → assigned at 95, cost basis ฿93.

## Related
- [[Options Strategy]] · [[Covered Call]] (the call-side income twin) ·
  [[Options Chain]] (pick the strike) · [[Greeks]] ([[Theta]], [[Delta]], [[Vega]])

## Sources
[^1]: `raw/options-strategies-overview.md`
[^2]: `raw/greeks-overview.md`
