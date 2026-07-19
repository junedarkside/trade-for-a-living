---
title: Open Interest
type: concept
status: learning
tags: [options, futures, derivatives]
aliases: [OI, Open Int]
---

# Open Interest (OI)

**Open Interest** is the total number of **outstanding (unclosed) derivative
contracts** for an underlying at the end of each trading day. Each contract =
one long + one short. Distinct from **volume** (which resets daily).

OI is the primary positioning read for option chains — clusters at strikes
act as support / resistance because market makers and institutions hedge or
roll there.

## Mechanics

| Event | OI change |
|-------|-----------|
| New contract opened (new long + new short) | **+1** |
| Existing contract closed (buyer sells-to-close OR seller buys-to-close) | **−1** |
| Trade between two existing participants (one closes, other opens) | **No change** |

## OI vs volume

| | Volume | Open Interest |
|---|--------|---------------|
| Resets each day | Yes | No (cumulative) |
| Counts new contracts | Yes | Only when OI changes |
| Use | Daily liquidity gauge | Positioning + support/resistance |

## How OI is read

| OI signal | Interpretation |
|-----------|----------------|
| **Rising OI + rising price** | New longs + new shorts entering → strong trend |
| **Rising OI + falling price** | New shorts entering → strong downtrend |
| **Falling OI + rising price** | Shorts covering + longs exiting → weak rally |
| **Falling OI + falling price** | Longs liquidating → weak sell-off |

## SET50 / TFEX usage

In Thai market, **OI clusters at specific strikes act as support /
resistance**. See [[Options Chain]] for the read:

- Heavy **call OI at a strike → resistance** (market makers hedge calls
  sold by selling underlying; that supply caps rallies).
- Heavy **put OI at a strike → support** (market makers hedge puts sold by
  buying underlying; that bid floors declines).

This is why the "OI walls" concept is daily-critical for S50 options.

## OI trend signals

| Signal | Interpretation |
|--------|----------------|
| Rising OI + rising price | New longs + new shorts entering → **strong trend**, conviction |
| Rising OI + falling price | New shorts entering → **strong downtrend** |
| Falling OI + rising price | Shorts covering → weak rally, likely fading |
| Falling OI + falling price | Longs liquidating → weak sell-off, potential base forming |

## Roll OI (near-to-far migration)

In the final 2 weeks before expiry, large positions **roll** — close the
near-month contract and reopen in the next expiry:

- Near-month OI falls sharply (roll-out).
- Next-month OI rises sharply (roll-in).
- This is **not** a directional signal — it's position maintenance.

**How to distinguish roll from real new positioning:**
- Roll = simultaneous OI drop in near + OI rise in far, flat total.
- New positioning = total OI across all expiries rises.

Watch for roll acceleration starting 10–14 days before SET50 options expiry
(third Thursday). Near-month liquidity thins → spreads widen → execution cost rises.

## OI at expiry

For monthly options, OI collapses into expiry as positions close. The
**peak OI strikes** often **pin** the underlying into expiry (dealers defend
those strikes with delta hedges). See [[Expiration]] for pin risk mechanics.

## Worked example — S50 chain

- SET50 = 25,500.
- Highest put OI = **25,400** (5,000 contracts).
- Highest call OI = **25,600** (4,500 contracts).
- Read: market **defends 25,400–25,600** into expiry.
- Trade implications:
  - Bullish bias: buy 25,500 call (slightly ITM, leverage to upside).
  - Range bias: sell iron condor outside 25,400 / 25,600 walls
    (dealers defend the walls → premium collection likely).
  - Breakout bias: buy strangle just outside the walls (cheap premium, big
    payoff if walls fail).

## Related

- [[Options Chain]] · [[Gamma Exposure]] · [[Expiration]] ·
  [[Position Greeks]] · [[Volatility Risk Premium]] ·
  [[Options Flow Analysis]] · [[Strategy Selection Framework]] ·
  [[SET50 Futures]] · [[SET50 Options]]

## Sources

[^1]: `raw/open-interest.md`
[^2]: CBOE — Options glossary (Open Interest definition).
    https://www.cboe.com/education/glossary
[^3]: CME Group — Understanding Open Interest (PDF).
    https://www.cmegroup.com/education/files/Understanding-Open-Interest.pdf
[^4]: Investopedia — Open Interest.
    https://www.investopedia.com/terms/o/openinterest.asp
