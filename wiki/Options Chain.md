---
title: Options Chain
type: concept
status: learning
tags: [options, derivatives, market/thailand]
---

# Options Chain

The **options chain** is the matrix of every strike — calls and puts — for one
underlying and one expiry, with price, volume, open interest, IV, and Greeks for
each. It is the core **tool for selecting strikes and expiries** when building
any [[Options Strategy|options strategy]].

## What the chain shows

For each strike (calls on the left, puts on the right, centered on the current
spot/futures price):

| Field | Meaning |
|-------|---------|
| **LTP / bid-ask** | Last price + current quotes (spread = liquidity proxy) |
| **Volume** | Contracts traded today |
| **Open Interest (OI)** | Contracts currently open — clusters act as support/resistance |
| **Implied Volatility (IV)** | Market's expected volatility priced into that option |
| **Greeks** | Delta, gamma, theta, vega per strike (see [[Greeks]]) |

## Key signals

- **OI clusters**: heavy **call OI at a strike → resistance**; heavy **put OI →
  support**. The market often defends these levels into expiry.
- **IV skew**: OTM puts with much higher IV than OTM calls → market pricing more
  downside risk. Skew tells you which side is cheap/expensive.
- **Liquidity**: trade strikes with tight bid-ask and real volume — wider spreads
  bleed edge on entry and exit.

> See [[Open Interest]] for the positioning read and [[IV Skew, Smile &
> Surface]] for skew/surface mechanics.

## View → strategy mapping

| Outlook | Strategy families |
|---------|-------------------|
| Bullish, moderate move | Bull call spread, bull put spread, long call, [[Cash-Secured Put]] |
| Bearish, moderate move | Bear put spread, bear call spread, long put |
| Neutral, low volatility | [[Iron Condor]], short strangle/straddle (advanced), [[Covered Call]] |
| Neutral, expect high volatility | [[Long Straddle]], long strangle, butterfly, iron butterfly |
| Hedging an existing position | [[Protective Put]], [[Collar]], put spread |

## Selecting strikes & expiries
- **Bull call spread** ([[Vertical Spread]]): buy ITM/ATM call near spot; sell OTM
  call where call OI marks resistance and premium is attractive.
- **Collar** (on stock owned): put strike defines max loss (often high put-OI
  strike); call strike finances the put (often near call-OI resistance).

## Greeks & breakeven
- **Delta** ≈ probability of expiring ITM + hedge ratio.
- **Theta** = how fast time decay hurts (long) or helps (short).
- **Breakeven** by structure — e.g. [[Long Straddle]]: strike ± total premium.

## Worked example — range play from the chain
Index at **25,450**. Chain shows highest put OI at **25,400**, highest call OI at
**25,500**, high IV (slightly higher on puts).[^1]

- Read: market brackets **25,400–25,500** as the expiry range; put-side skew =
  downside hedging demand.
- Range-bound trade → **iron condor** just outside the range (sell 25,400P +
  25,500C, buy OTM wings), or a **short strangle** at 25,400/25,500 for higher
  risk tolerance.
- The chain gave: OI support/resistance, premium collectable, and the implied
  range width.

> SET50 / TFEX equivalent: read the **S50 option chain** the same way — put/call
> OI walls bracket the expected SET50 range into settlement.

## Related
- [[Options Strategy]] — what to build. · [[Greeks]] — what each column means.
- Strategies selected via the chain: [[Covered Call]], [[Vertical Spread]],
  [[Long Straddle]], [[Collar]], [[Protective Put]], [[Cash-Secured Put]],
  [[Iron Condor]], [[Strangle]].

## Sources
[^1]: `raw/options-chain.md`
