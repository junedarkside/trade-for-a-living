---
title: Bid-Ask Spread
type: glossary
status: learning
tags: [spot, options, derivatives]
---

# Bid-Ask Spread

The **bid-ask spread** is the gap between the best **buy** (bid) and best
**sell** (ask) price. It is the **dealer compensation** for providing
liquidity, and the **first cost** every trader pays.

## Formula

```
spread = ask − bid
spread (bps) = (ask − bid) / mid × 10,000
```

## What it tells you

- **Tight spread (≤ 10 bps)**: liquid market, professional flow, easy entry/exit.
- **Wide spread (> 50 bps)**: thin book, retail-heavy, every trade is expensive.
- **Spread skew**: bid > ask in absolute terms but proportionally different —
  watch for one-sided inventory.

## Cost on a round trip

```
round-trip cost = (entry spread + exit spread) × contracts × multiplier
                 ≈ 2 × spread × contracts × multiplier (worst case, full cross)
```

For a Thai equity option with mid ฿1.00 and spread ฿0.10, you pay ฿0.20 per
share × 100 shares = **฿20 round-trip** before any underlying move.

## Use in trade selection

- **Filter**: skip strikes where spread > 10–15% of mid. Edge disappears.
- **Liquidity ranking**: rank candidates by `volume / spread` — high volume +
  narrow spread = tradeable.
- **Execution**: use **limit orders** at the bid (buy) / ask (sell) to avoid
  paying the spread twice.

## Related
- [[Spot — Basics]] · [[Options Chain]] · [[Tick Size]] · [[Options Risk Management]]

## Sources
[^1]: `raw/spot-basics.md`
