---
title: Short Strangle
type: strategy
status: learning
tags: [options, derivatives, strategy/income, strategy/speculation, market/thailand]
aliases: [Short Strgl, Sell Strangle]
---

# Short Strangle

A **short strangle** is an advanced **non-directional** options strategy:
sell an OTM call + an OTM put at the same expiry (different strikes). You
collect premium and profit if the underlying stays in a range AND/OR
implied volatility falls. Time decay works in your favor.

This is one of the canonical structures for harvesting the
[[Volatility Risk Premium]] on index options.

## Overview

| | |
|---|---|
| **Outlook** | Neutral — expect low realised vol, range-bound |
| **Vol view** | IV high → expected to fall |
| **Objective** | Income / VRP harvest |
| **Risk profile** | Defined-profit, undefined-risk |
| **Complexity** | Advanced |
| **Best on** | Liquid index options (S50 / SPX / NDX) |

## Legs

| Leg | Action | Type | Strike | Expiry |
|-----|--------|------|--------|--------|
| 1 | **Sell** | Call | `K_c` (OTM, above spot) | T |
| 2 | **Sell** | Put | `K_p` (OTM, below spot) | T |

Both options OTM at entry. `K_p < spot < K_c`.

## Max Loss

- **Upside**: theoretically **unlimited** (short call exposure).
- **Downside**: up to `K_p − (C + P)` if underlying → 0.
- This is a **short premium, short gamma, short vega** position. Big moves
  and vol spikes hurt. See [[Options Risk Management]] for sizing rules.

## Max Profit

- Occurs if both options expire worthless (underlying ends between `K_p`
  and `K_c`).
- **Max profit = total premium received = C + P.** Capped but reachable.

## Breakeven(s)

```
S_BE_up   = K_c + (C + P)
S_BE_down = K_p − (C + P)
```

Profit if underlying ends between breakevens; loss otherwise.

## Greeks behavior

| Greek | Sign | Evolution |
|-------|------|-----------|
| **Delta** | ~0 at entry | Becomes positive if spot falls toward `K_p`, negative if spot rises toward `K_c` |
| **Gamma** | **negative** | Delta accelerates against you as spot moves; risk builds fast in big moves |
| **Theta** | **positive** | Time decay works for you daily; accelerates in final 30 days |
| **Vega** | **negative** | Falling IV = mark-to-market gain. Rising IV = loss even if spot unchanged |

Best in **calm, range-bound markets with stable or falling vol**.

## Payoff shape (at expiry)

```
P&L
 │       \              /
 │        \    K_p / K_c range
 │         \          /     ← max profit zone (flat)
 │          \        /
 │           \______/
 │       K_p − (C+P)      K_c + (C+P)
 │           ↑               ↑
 │           loss            loss
 spot ────────────────────────────►
```

- Between strikes at expiry → flat max profit (the premium).
- Outside strikes → loss accelerates 1:1 with spot move.

## When to use

- **Range-bound index / stock** — underlying bracketed by support/resistance.
- **High IV, expected to fall** — event-driven fear normalising.
- **Income overlay** — harvesting VRP across the book; pairs with delta hedges.

Strike selection guidance:
- Technical levels (support / resistance).
- Expected move (from [[Implied Volatility|IV]] or [[Historical Volatility|HV]]
  range).
- Target probability of expiring OTM (commonly 16–25 delta shorts).

## Risks

| Risk | How it hits |
|------|-------------|
| **Unlimited upside** | Short call has no cap |
| **Near-total downside** | Short put assigns ~full loss if underlying → 0 |
| **Gamma blow-up** | Delta accelerates against you in fast markets |
| **Vega blow-up** | Vol spike (event) causes mark-to-market loss even if spot unchanged |
| **Early assignment** | Possible on American-style short call near ex-div or short put in sharp selloff (TFEX S50 options are European → no early assignment) |
| **Margin call** | Large mark-to-market losses can force liquidation |

## Example — S50 short strangle

- SET50 = **25,500**. 30 days to expiry.
- Sell **25,800 call** at ฿18 (≈ 14-delta OTM).
- Sell **25,200 put** at ฿17 (≈ 14-delta OTM).
- Net credit per leg = ฿18 + ฿17 = **฿35 / index point** (before fees).
- Per contract (multiplier ฿200): ฿35 × 200 = **฿7,000 credit**.
- Breakevens:
  - Up: 25,800 + 35 = **25,835**.
  - Down: 25,200 − 35 = **25,165**.
- Profit zone: **25,165 – 25,835** at expiry.
- **Max profit** = ฿7,000 if SET50 between 25,200 and 25,800 at expiry.
- **Max loss** — if SET50 rallies to 26,500 → loss on call = (26,500 −
  25,800) × 200 = ฿140,000 − ฿7,000 credit = **−฿133,000**.
- **Margin** — naked short strangle on S50: margin typically ฿40,000–฿80,000
  per strangle (per broker). **Leverage ~10–25×** vs collected premium.

> Compare to [[Iron Condor]] on the same strikes + wings at 25,900 / 25,100:
> max loss capped at wing width × 200 − credit. Defined risk, lower premium.

## Adjustments

| Situation | Adjustment |
|-----------|-----------|
| Tested on one side | Roll that leg to next expiry (more time, possibly different strike) |
| Tested both sides (range about to break) | Convert to [[Iron Condor]] by buying OTM wings |
| Large IV spike | Close whole position (vega pain) |
| Pre-event (BOT / earnings / data) | Close or reduce ahead of catalyst |

## Related

- [[Strangle]] (parent — long/short overview) · [[Iron Condor]] ·
  [[Long Straddle]] · [[Volatility Risk Premium]] ·
  [[Options Strategy]] · [[Options Risk Management]] ·
  [[Margin Mechanics]] · [[Assignment]]

## Sources

[^1]: `raw/short-strangle.md`
[^2]: optionseducation.org — Short Strangle.
    https://www.optionseducation.org/strategies/all-strategies/short-strangle
[^3]: optionalpha.com — Short Strangle strategy guide.
    https://optionalpha.com/strategies/short-strangle
[^4]: optionsplaybook.com — Short Strangle mechanics.
    https://www.optionsplaybook.com/option-strategies/short-strangle
[^5]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 12.
