---
title: Multi-Leg Order
type: concept
status: learning
aliases: [MLO]
tags: [options, futures, derivatives, risk]
---

# Multi-Leg Order

**Execution concept.** A single order ticket that contains two or more legs
(typically options, or futures + options) intended to execute together as a
package. The unit of trade is the **package**, not the leg.

## Overview
Most multi-leg strategies ([[Collar]], [[Futures Collar]], [[Risk Reversal]],
[[Calendar Spread]], iron condors, etc.) work because the legs are priced as a
single structure. Submitting each leg separately exposes you to **legging risk**
and usually worse fills.

## Multi-leg vs multi-strategy
- **Multi-leg order** — one instrument strategy with many legs (this article).
- **Multi-strategy** — many separate option strategies combined in a portfolio
  (see [[Multi-Strategy Options]]).

## Key properties

| Property | Multi-leg order | Leg-by-leg |
|----------|----------------|------------|
| Execution | Atomic (all legs fill together) | Sequential |
| Legging risk | None | Real (price moves between legs) |
| Net price | Quoted as a package | Computed after the fact |
| Commission | Often reduced | Full per leg |
| Margin | Often **spread margin** (lower) | Each leg margined separately |

## Advantages
1. **No legging risk** — atomic fill, no partial state.
2. **Net pricing clarity** — see one debit/credit for the structure.
3. **Lower commission** — most brokers bundle multi-leg tickets.
4. **Better margin** — package often gets spread-margin treatment
   (see [[Portfolio Margin]]).

## Legging risk (the danger of leg-by-leg)
If you leg in one at a time, the market can move between fills:
- First leg fills at your price.
- Market moves against you before the second leg fills.
- You end up with a **partial position** carrying unintended Greek exposure
  (often unwanted [[Delta]]) until the second leg lands.

This is amplified for:
- Illiquid strikes/expiries (wider bid/ask).
- Fast markets (open, events, news).
- Wider packages (3+ legs).

## Practical habits
- **Always check before entry:**
  - Net debit/credit for the package.
  - Max loss, max profit, break-evens.
  - Liquidity of **each** leg (bid/ask, volume, OI).
- **Prefer liquid strikes/expiries** — avoid illiquid strikes unless you truly need them.
- **Avoid market orders on wide packages** — use limit with reasonable net price.
- **One cancel-other (OCO)** for hedge legs you may want to bail on.

## When NOT to use multi-leg
- Leg-1 has good liquidity, leg-2 is illiquid — atomic ticket may not fill.
- You want to scale in over time (deliberately accept legging risk for better avg).
- You're legging out of an existing position where the remaining leg is the new "structure".

## Related
- [[Multi-Strategy Options]] (combining strategies) · [[Portfolio Margin]] (margin efficiency) ·
  [[Risk Reversal]] · [[Calendar Spread]] · [[Futures Collar]] · [[Greeks]]

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: investopedia.com — multi-leg order definition.
[^3]: asx.com.au — implementing multi-legged strategies.
[^4]: fxoptions.com — managing multi-leg options positions.