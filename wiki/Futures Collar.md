---
title: Futures Collar
type: strategy
status: learning
aliases: [FC]
tags: [futures, options, derivatives, strategy/hedge, strategy/income, market/thailand]
---

# Futures Collar

**Hedge + income hybrid.** Long a futures contract, buy a protective put (floor),
sell a covered call (cap) to fund the put. Defined downside AND upside — often
near-zero net cost.

## Overview
Same logic as the equity [[Collar]], but with a futures leg instead of stock.
You trade away upside above the call strike to pay for downside protection at the
put strike.

## Legs

| Leg | Action | Instrument | Contract | Strike | Expiry |
|-----|--------|-----------|----------|--------|--------|
| 1 | Long | Future | e.g. S50U26 | — | Same as options |
| 2 | Long | Put option | e.g. S50U26 | Below spot (floor) | Same as future |
| 3 | Short | Call option | e.g. S50U26 | Above spot (cap) | Same as future |

## Max profit
**(Call strike − Future entry) − Net debit** (or + Net credit).
- Capped at the call strike.

## Max loss
**(Future entry − Put strike) + Net debit** (or − Net credit).
- Capped at the put strike.

## Breakeven
**Future entry + Net debit** (− Net credit if structure is done for a credit).

## Greeks behavior
- **Delta**: positive but muted — bullish with a leash.
- **Gamma**: small (long put + short call partly offset).
- **Theta**: roughly flat to slightly positive (short call funds the put).
- **Vega**: roughly flat (offsetting legs).

## Payoff shape (at expiry)
```
P&L
 │__________  ← flat cap at call strike
 │        /
 │      /
 ┼──────/───── Put strike ... Call strike
 │  ← floor: flat loss at put strike
```

## When to use
- Long futures position you want to protect without paying full put premium.
- Willing to cap upside (you'd happily close at the call strike anyway).
- Common into volatile periods.

## Risks
- **Upside capped** — rallies past the call strike are given away.
- **Early assignment** — on the short call (American style), esp. deep ITM.
- **Margin on short call** — adds to the long future's margin; check spread margin.

## Example — SET50 / TFEX
- Long 1 S50 future at 950. Buy 1 put strike 920 @ ฿8 × 200 = ฿1,600.
  Sell 1 call strike 980 @ ฿8 × 200 = ฿1,600. **Net: ฿0 (zero-cost).**
- **Max profit**: (980 − 950) × 200 = ฿6,000.
- **Max loss**: (950 − 920) × 200 = ฿6,000.
- **Breakeven**: ฿950.

## Related
- [[Collar]] (stock variant) · [[Protective Put on Future]] · [[Covered Call on Future]] ·
  [[Portfolio Margin]] (spread offsets) · [[Greeks]]

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/futures-basics.md`
[^3]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.