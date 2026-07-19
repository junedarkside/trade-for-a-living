---
title: Assignment
type: concept
status: learning
tags: [options, derivatives]
aliases: [Option Assignment, Early Assignment, Exercise Notice]
---

# Assignment

**Assignment** happens when the **option writer (seller)** is required to
fulfill the contract — sell the underlying (call writer) or buy the
underlying (put writer) at the strike price. The clearinghouse / broker
randomly allocates exercise notices among short open positions. **You can be
assigned even if you didn't "choose" to be.**

## Mechanics

| Writer position | If assigned, you must |
|-----------------|-----------------------|
| **Short call** | **Sell** underlying at strike |
| **Short put** | **Buy** underlying at strike |

Assignment is per-contract. A short straddle of 10 contracts can be assigned
on either leg, partially or fully, in any combination — there's no "all or
nothing".

## Early assignment risk

| Higher when | Why |
|-------------|-----|
| Option is **deep ITM** | Intrinsic value dominates; time value minimal |
| **American-style** option | Can be exercised any time to expiry |
| **Upcoming dividend** (short calls) | Holder exercises to capture dividend |
| Rates / dividends make early exercise economically attractive | Time-value arbitrage |

**European-style options** (e.g., TFEX S50 options) **cannot be assigned
early** — only at expiry. This eliminates the dividend-timing risk for S50
short calls. Equity options on US names are American-style and do carry
this risk.

## Practical implications

- **Short ITM calls near ex-div** — likely early assignment. Roll or close
  before ex-div date to avoid forced stock sale at strike.
- **Short ITM puts** — assignable any time, esp. after sharp drops. If you
  don't want to take delivery of the underlying, close or roll before close
  to expiry.
- **Naked short strangle / straddle** — pin risk at expiry if the underlying
  is exactly at the short strike. See [[Expiration]] for pin risk mechanics.
- **Cash-secured put** writers (see [[Cash-Secured Put]]) expect potential
  assignment — they have the cash ready to take 100 shares per contract.

## Managing assignment risk

1. **Monitor days to expiry** — risk concentrates in the final week / final day.
2. **Monitor moneyness** — short ITM options = elevated assignment risk.
3. **Track ex-div dates** for short calls on dividend-paying underlyings.
4. **Roll or close** short ITM positions before risky windows.
5. **Prefer European-style** index options (e.g., TFEX S50 options) when
   early assignment is a concern.
6. **Have the cash or shares ready** if you're running naked short positions
   into expiry — assignment is mandatory, not optional.

## Worked example — short ITM call near ex-div

- Long 1,000 shares XYZ @ ฿100 (cost ฿100K).
- Short 10 contracts XYZ **฿105 calls** (American-style, 1 week to expiry,
  ex-div ฿2 in 3 days).
- ITM by ฿5. Time value minimal. **High early assignment probability.**
- If assigned early: you sell 1,000 shares @ ฿105 = ฿105K cash, **miss the
  ฿2 dividend** (₿2,000 to the option holder who exercises).
- Fix: **buy back** the calls **before ex-div** or **roll forward** to the
  next monthly expiry.

## Worked example — short put

- Short 10 SPY **฿450 puts** (American-style, 1 day to expiry).
- SPY closes at ฿445. Put ITM by ฿5.
- **Pin risk** — assignment possible but not guaranteed (depends on
  holder's exercise notice). If assigned, you **buy** 1,000 SPY shares @
  ฿450 = **฿450K cash outflow**, market value ฿445K.
- Fix: close the short put **before market close** to avoid assignment
  entirely.

## Related

- [[Expiration]] · [[Options — Basics]] · [[Options Risk Management]] ·
  [[Cash-Secured Put]] · [[Covered Call]] · [[Short Call]] · [[Short Put]] ·
  [[Multi-Leg Order]] · [[Settlement]]

## Sources

[^1]: `raw/iv-and-market-mechanics.md` (section 5).
[^2]: optionseducation.org — Options basics (assignment mechanics).
[^3]: CBOE — exercise and assignment rules.
