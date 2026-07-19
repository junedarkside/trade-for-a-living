---
title: Diagonal Spread
type: strategy
status: learning
aliases: [Diag]
tags: [options, futures, derivatives, strategy/speculation, market/thailand]
---

# Diagonal Spread

**Vol/time + direction strategy.** A [[Calendar Spread]] with **different strikes**
on the two legs. Combines the time-decay harvesting of a calendar with a
**directional bias** from the strike selection.

## Overview
Sell a near-dated option at one strike; buy a longer-dated option at a
**different strike** (typically the long leg is further OTM for a call diagonal,
or closer to spot for a put diagonal). You get paid theta on the short leg while
expressing a directional view via the long back-month option.

## Legs — Call Diagonal (bullish bias)

| Leg | Action | Instrument | Contract | Strike | Expiry |
|-----|--------|-----------|----------|--------|--------|
| 1 | Short | Call option | e.g. S50U26 | ATM or near (closer to spot) | Near (e.g. 30 days) |
| 2 | Long | Call option | e.g. S50U26 | OTM (higher strike) | Far (e.g. 90 days) |

Mirror for **Put Diagonal** (bearish bias): short near ATM put + long far lower-strike put.

## Max loss
**Net debit paid** (long back-month premium − short near-month premium received),
realized in adverse paths.
- Capped: yes — at the net debit (assuming both legs are options).

## Max profit
Path-dependent. Achieved when the underlying is **between the two strikes** at
short-leg expiry — the short expires worthless, and the long retains time value.
Beyond the long strike → unlimited (long call) but locked by short expiry.
Below the short strike → capped loss.

## Breakeven
Multiple break-even zones; depends on strike spacing and IV. Path-dependent.

## Greeks behavior
- **Delta**: directional — positive for a call diagonal, negative for a put diagonal.
- **Gamma**: long (long back-month dominates).
- **Theta**: **positive** at entry (short near decays faster than long far).
- **Vega**: **long** (long back-month has more vega).

## Payoff shape (at short-leg expiry, in P&L)
```
P&L
 │           /          ← long call upside past long strike
 │         /
 │       /    ___        ← profit zone between strikes
 │     /    /     \
 ┼───/────/───────\─────  Short strike ... Long strike
 │  /  /
 │ /                 ← losses capped at net debit (below short strike)
```

## When to use
- **Directional view** + want to be paid theta while waiting.
- **Earnings / event** — sell near-dated premium, keep longer-dated exposure to the move.
- **Rolling hedged positions** — the diagonal can replace a futures + short-call package.

## Risks
- **Vol crush** on the long back-month — hurts the long leg.
- **Strike selection** — wrong spacing leaves the trade either too directional or too flat.
- **Liquidity** — far-dated OTM strikes often thin; check OI.
- **Path dependency** — break-evens depend on how price moves through time.

## Example — SET50 / TFEX
- Short 1 S50 call strike 950, 30 days, collect ฿12 × 200 = ฿2,400.
- Buy 1 S50 call strike 1,000, 90 days, pay ฿6 × 200 = ฿1,200.
- **Net credit**: ฿1,200 (paid to enter).
- If S50 stays 950–1,000 at short expiry → short expires near worthless, long
  retains extrinsic → profit > ฿1,200.
- If S50 > 1,000 → both ITM; long gains offset by short being exercised.
- If S50 < 950 → keep full ฿1,200 credit (short expires worthless, long still OTM).

## Related
- [[Calendar Spread]] (same strikes; pure time-decay play) · [[Synthetic Futures]] ·
  [[Risk Reversal]] (similar diagonal geometry) · [[Greeks]] · [[Multi-Leg Order]]

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/greeks-overview.md`
[^3]: youtube.com — payoff diagrams reference.
[^4]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.