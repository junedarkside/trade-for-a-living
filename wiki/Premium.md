---
title: Premium
type: glossary
status: learning
aliases: [Prem]
tags: [options, derivatives]
---

# Premium

**The price of an option.** What the buyer pays upfront; what the seller (writer)
collects. Quoted per share; total contract cost = premium × shares-per-contract.

## Per-share vs per-contract
- **Equity options**: premium quoted per share; 1 contract = 100 shares.
  Premium ฿3.50 → contract cost = 3.50 × 100 = **฿350**.
- **TFEX S50 index options**: premium quoted per index point; 1 contract =
  ฿200 multiplier. Premium 6.0 → contract cost = 6.0 × 200 = **฿1,200**.

## What determines the premium

| Driver | Effect on premium |
|--------|-------------------|
| **Spot price** | Determines [[Moneyness]] (ITM/ATM/OTM). |
| **Strike price** | Distance from spot (see [[Strike Price]]). |
| **Time to expiry** | More time → higher premium (more extrinsic). |
| **Implied volatility** | Higher IV → higher premium (more extrinsic). |
| **Risk-free rate** | Minor effect; raises calls, lowers puts. |
| **Dividends** | Expected dividends lower call premium, raise put premium. |

## Buyer's vs seller's max P&L

- **Long (buyer)**: max loss = premium paid. Max profit = unlimited (call) or
  large (put).
- **Short (seller)**: max gain = premium received. Max loss = unlimited (naked
  call) or capped (put, cash-secured).

## Premium decomposition

```
Premium = Intrinsic value + Extrinsic value
```

- **Intrinsic** = immediate exercise value (ITM only).
- **Extrinsic** = the rest — driven by time, volatility, rates.
- See [[Intrinsic and Extrinsic Value]] for the full breakdown.

## Related
- [[Options — Basics]] · [[Strike Price]] · [[Moneyness]] ·
  [[Intrinsic and Extrinsic Value]] · [[Theta]] · [[Vega]] ·
  [[Black Model]] (pricing)

## Sources
[^1]: `raw/options-basics.md`
[^2]: optionseducation.org — options basics.