---
title: Strike Price
type: glossary
status: learning
aliases: [K, strike]
tags: [options, derivatives]
---

# Strike Price

**The fixed price at which the option holder can buy (call) or sell (put) the
underlying if they exercise.** Denoted **K** in option-pricing formulas.

## Overview
Every option contract specifies a strike. Multiple strikes trade for each
underlying/expiry pair — see [[Options Chain]].

## Strike vs. spot (moneyness)

| Relationship | Call | Put |
|--------------|------|-----|
| Spot > K | **In-the-money** (ITM) | Out-of-the-money (OTM) |
| Spot ≈ K | **At-the-money** (ATM) | At-the-money (ATM) |
| Spot < K | Out-of-the-money (OTM) | **In-the-money** (ITM) |

See [[Moneyness]] for full definitions.

## Strike selection — what traders look at

- **Open interest (OI)** — strikes with high OI are more liquid (tighter bid/ask).
- **Round numbers** — strikes at "clean" levels (e.g. 950, 1,000 for S50) often
  have more flow.
- **Distance from spot** — ATM has highest gamma/time decay; OTM is cheaper and
  more speculative; ITM is more directional with higher delta.
- **Implied vol skew** — puts and calls at the same distance OTM often price
  differently (puts usually richer).

## Strike spacing (TFEX S50 example)
- S50 index options: strikes typically spaced **2.5 or 5 points** apart near the money,
  wider farther out.

## Related
- [[Options — Basics]] · [[Options Chain]] · [[Moneyness]] ·
  [[Premium]] · [[Intrinsic and Extrinsic Value]]

## Sources
[^1]: `raw/options-basics.md`
[^2]: optionseducation.org — options basics.