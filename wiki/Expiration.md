---
title: Expiration
type: concept
status: learning
tags: [options, derivatives]
aliases: [Expiry, Expiration Date, Last Trade Date]
---

# Expiration

The **expiration date** is the **last day** the option can be exercised.
Past expiry, the contract ceases to exist.

## Exercise style

| Style | Can be exercised | Examples |
|-------|------------------|----------|
| **American** | **Any time** up to and including expiry | Most equity options (US, SET-listed) |
| **European** | **Only at expiry** | TFEX S50 options, most index options globally |

For Thai traders: **TFEX S50 options are European**. This means **no early
assignment risk** on S50 short positions — assignment only happens at expiry.

## What happens at expiry

| Option status at expiry | Outcome |
|-------------------------|---------|
| **ITM** by ≥ ฿0.01 | Typically **auto-exercised** (you can override at your broker) |
| **OTM** | **Expires worthless** — contract gone, no settlement |
| **Exactly ATM** (pin risk) | Clearinghouse randomly assigns; usually ITM by settlement calc |

> **Auto-exercise policy** varies by broker. Most auto-exercise any ITM
> option by ≥ ฿0.01. Confirm with your broker; if you want a different
> behaviour, submit a "do not exercise" instruction before close on expiry
> day.

## Pin risk

When the underlying **closes very near the strike** on expiry day:

- Option may be ITM by a few cents → **auto-exercised** → forced into
  delivery.
- Or OTM by a few cents → **expires worthless** → no assignment.
- Difference is which side of the strike the **official settlement price**
  lands on. For TFEX S50 options, the official settlement uses the SET50
  **closing value** (and sometimes an intraday auction — check specs).

**Managing pin risk:**
- **Close** short ITM options before expiry (don't wait for the close).
- **Hedge** the position (delta-neutral or full) into the close.
- **Avoid holding** large short option positions through expiry when the
  underlying is at the strike.

## Last trading day conventions

| Product | Last trade |
|---------|-----------|
| SET-listed equity options | Expiry day (typically a Friday, sometimes 3rd Friday of month) |
| TFEX S50 options | Same as expiry |
| TFEX S50 futures | Same as expiry (cash settlement) |
| SSF | Expiry day; physical delivery on T+2 |
| USD/THB futures | Expiry day |

Check TFEX rulebook per product — last-trade dates vary (some products stop
trading a few days before final settlement).

## Time decay into expiry

Theta (see [[Theta]]) **accelerates** in the final 30–45 days as expiration
approaches. Long options lose value fastest in the final two weeks. **Short
option sellers harvest this** — see [[Volatility Risk Premium]] for the
premium-selling context.

A rough rule of thumb:
- DTE > 60: theta ≈ linear, slow bleed.
- DTE 30–60: theta picks up.
- DTE 7–30: theta sharp.
- DTE < 7: theta explosive; long options decay fast, short options profit
  fast (or pin risk explodes).

## Calendar spread angle

A [[Calendar Spread]] exploits the difference in time-decay rates between
near and far expiries. Selling the near (high theta) and buying the far (low
theta) collects the theta differential. Risks: pin risk on the short leg at
near expiry, IV term structure shifts.

## Related

- [[Assignment]] · [[Options — Basics]] · [[Theta]] · [[Calendar Spread]] ·
  [[Settlement]] · [[Options Strategy]] · [[Options Risk Management]] ·
  [[SET50 Futures]] · [[SET50 Options]]

## Sources

[^1]: `raw/iv-and-market-mechanics.md` (section 5).
[^2]: optionseducation.org — Options basics (American/European, expiration).
[^3]: TFEX — expiry and settlement rulebook per contract.
[^4]: CBOE — auto-exercise policy and pin risk.
