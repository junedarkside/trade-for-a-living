---
title: Risk Reversal
type: strategy
status: learning
aliases: [RR]
tags: [futures, options, derivatives, strategy/speculation, market/thailand]
---

# Risk Reversal

**Speculative strategy.** Long a futures contract, sell a put, buy a call — both
options typically struck around current price (often OTM). Creates a leveraged
directional view with the short put financing the long call.

## Overview
A way to express a directional view on the underlying using options where the
short put's premium offsets the long call's cost (the classic "zero-cost" or
low-cost entry, if strikes are equidistant OTM). Adding the future leg amplifies
directional delta.

## Legs

| Leg | Action | Instrument | Contract | Strike | Expiry |
|-----|--------|-----------|----------|--------|--------|
| 1 | Long | Future | e.g. S50U26 | — | Same as options |
| 2 | Short | Put option | e.g. S50U26 | Below spot (OTM) | Same as future |
| 3 | Long | Call option | e.g. S50U26 | Above spot (OTM) | Same as future |

## Max loss
**(Future entry − Put strike) − (Call premium − Put premium)**, per contract
(× multiplier).
- Capped: yes — short put creates a floor.

## Max profit
**Uncapped** above the call strike, net of (Call premium − Put premium received).

## Breakeven
**Future entry + (Call premium − Put premium received)** if the net cost is a debit;
or **Future entry − (Put premium − Call premium)** if a credit.

## Greeks behavior
- **Delta**: positive and amplified (long future + long call + short put).
- **Gamma**: roughly flat (long call + short put offset).
- **Theta**: roughly flat (offsetting time decay).
- **Vega**: roughly flat (long call + short put offset).

## Payoff shape (at expiry)
```
P&L
 │        /  ← unlimited upside past call strike (modest slope)
 │      /
 │    /  ← between put and call strikes: future leg dominates (steep slope)
 ┼──────────── Put strike ... Call strike
 │  ← floor: capped downside at put strike (net of option cost)
```

## When to use
- Directional speculation with a leveraged view; willing to pay via reduced net premium.
- Useful when implied vol is **rich** (sell put, buy call benefits from elevated skew).
- Mirrors a long forward/future plus a synthetic long strangle (short put + long call).

## Risks
- **Capped downside** — sharp sell-offs hurt exactly like a short put.
- **Margin on short put** — meaningful; broker may require full naked-put margin
  unless booked as a spread (see [[Portfolio Margin]]).
- **Skew risk** — if put skew widens, your short put becomes expensive to close.
- **Liquidity** — OTM strikes may be thin; check bid/ask and OI.

## Example — SET50 / TFEX
- Long 1 S50 future at 950. Sell 1 put strike 920 @ ฿6. Buy 1 call strike 980 @ ฿6.
  **Net cost: ~฿0** (equidistant OTM, similar IV).
- **Max profit**: uncapped above 980.
- **Max loss**: (950 − 920) × 200 = ฿6,000 (zero-cost variant).
- **Breakeven**: ~฿950.

## Related
- [[Synthetic Futures]] (the underlying equivalence) · [[Protective Put on Future]] (with long put, no short put) ·
  [[Protective Call on Short Future]] (the bearish mirror) · [[Greeks]] ([[Delta]])

## Sources
[^1]: `raw/multi-leg-futures-options.md`
[^2]: `raw/futures-basics.md`
[^3]: Hindu Business Line — Mastering derivatives: how to optimally combine futures and options.