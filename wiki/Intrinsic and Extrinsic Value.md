---
title: Intrinsic and Extrinsic Value
type: glossary
status: learning
aliases: [IV, EV, time-value]
tags: [options, derivatives]
---

# Intrinsic and Extrinsic Value

**Every option premium decomposes into two pieces: intrinsic value (immediate
exercise value) and extrinsic value (everything else — time, volatility, rates).**

```
Premium = Intrinsic value + Extrinsic value
```

## Intrinsic value

**The amount the option would pay if exercised right now.** Only ITM options
have intrinsic value; ATM and OTM have intrinsic = 0.

| Type | Intrinsic value |
|------|-----------------|
| Call | max(Spot − Strike, 0) |
| Put | max(Strike − Spot, 0) |

**Example**: call with spot ฿200, strike ฿180 → intrinsic = ฿20. Put with spot
฿150, strike ฿160 → intrinsic = ฿10.

## Extrinsic value (time value)

**Premium minus intrinsic.** Driven by:
- **Time to expiry** — more time = more extrinsic (more time for the option
  to become profitable). Decays to zero at expiry.
- **Implied volatility** — higher IV = higher extrinsic (wider distribution of
  possible outcomes).
- **Rates & carry** — minor effect.
- **Distance from the money** — extrinsic peaks near ATM (where gamma is highest).

**Example**: the same call above (intrinsic ฿20) trades at ฿25 → extrinsic = ฿5.

## Behavior through the option's life

| State | Intrinsic | Extrinsic |
|-------|-----------|-----------|
| **Deep ITM** | Most of premium | Small |
| **ATM** | Zero | Most of premium (peaks) |
| **OTM** | Zero | All of premium |
| **At expiry** | = spot-strike (or 0) | **Always zero** |

At expiry, an option is worth **exactly its intrinsic value** — no time left,
no future uncertainty.

## Why it matters

- **Time decay ([[Theta]]) only eats extrinsic.** When you hold an ITM option,
  theta only chips away at the time-value portion; intrinsic is locked in.
- **Volatility ([[Vega]]) only moves extrinsic.** A jump in IV raises the price
  of an ATM option more than a deep ITM one.
- **Early-exercise decisions** hinge on whether extrinsic > 0
  (see [[Assignment]]).

## Related
- [[Premium]] · [[Strike Price]] · [[Moneyness]] · [[Theta]] · [[Vega]] ·
  [[Options — Basics]]

## Sources
[^1]: `raw/options-basics.md`
[^2]: investopedia.com — options basics tutorial.
[^3]: optionseducation.org — options basics.