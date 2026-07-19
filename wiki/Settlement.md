---
title: Settlement
type: glossary
status: learning
tags: [spot, futures, options, market/thailand]
---

# Settlement

**Settlement** is the moment cash and the underlying change hands. Different
instruments settle on different cadences and on different underlyings.

## Spot equities (SET)

- **T+2** — cash and shares settle two business days after the trade.
- Routed through **TSD** (Thailand Securities Depository).
- Selling on trade day does **not** free the cash until T+2; intraday buying
  power = settled cash + new sales proceeds available only after T+2.

## Futures (TFEX)

- **Daily mark-to-market** — every end-of-day, gains/losses are realised and
  paid in cash. This is the "settlement" most traders care about — you can lose
  or gain money without closing the position.
- **Final settlement** at expiry: depends on contract.
  - **SET50 futures**: cash-settled to the SET50 closing value.
  - **Single-stock futures (SSF)**: physical delivery of 1,000 shares.
  - **USD/THB futures**: physical delivery in USD/THB.
- **Margin** is re-collected daily; failure to meet maintenance margin triggers
  a margin call (see [[Margin Mechanics]]).

## Options (TFEX / SET warrants)

- **TFEX S50 options** = **European**, cash-settled at expiry.
- **SET-listed equity options** = typically **American** (exercisable any time
  to expiry), with physical delivery on exercise.
- Exercising early triggers T+2 delivery; selling-to-close before expiry
  avoids the delivery leg entirely (almost always preferable — see
  [[Assignment]]).

## Why settlement rules matter

- **Liquidity planning** — selling Monday to fund a Tuesday buy needs
  intraday/short-limit accommodation; otherwise wait until Thursday.
- **Pin risk** — being short an option that expires at-the-money means you
  don't know until Saturday whether you'll be assigned. See [[Assignment]].
- **Currency risk on FX futures** — physical delivery on USD/THB means you need
  USD in a USD account at expiry if long, or THB if short.

## Related
- [[Spot — Basics]] · [[Futures — Basics]] · [[Options — Basics]] ·
  [[Assignment]] · [[Margin Mechanics]]

## Sources
[^1]: `raw/spot-basics.md`
[^2]: TFEX — settlement rules per contract.
