---
title: Open Interest
type: source
tags: [options, futures, derivatives]
---

# Open Interest (OI)

**Open Interest** is the total number of **outstanding (unclosed) derivative
contracts** for a given underlying instrument at the end of each trading day.
Each contract = one long + one short. [^1]

## Mechanics

- **New contract opened** (buyer + seller matched for the first time) → OI
  increases by 1.
- **Existing contract closed** (buyer sells to close OR seller buys to close)
  → OI decreases by 1.
- **Trade between two existing participants** (buyer closes, seller opens new
  position OR vice versa) → OI **unchanged** (pass-through).

OI differs from **volume**:
- **Volume** = number of contracts traded today (reset each day).
- **OI** = number of contracts still open (cumulative, only resets when
  contracts close).

## How OI is read

| OI signal | Interpretation |
|-----------|----------------|
| **Rising OI + rising price** | New longs + new shorts entering → strong trend |
| **Rising OI + falling price** | New shorts entering → strong downtrend |
| **Falling OI + rising price** | Shorts covering + longs exiting → weak rally, may reverse |
| **Falling OI + falling price** | Longs liquidating → weak sell-off, may reverse |

In Thai market (SET50 options / futures), OI clusters at specific strikes
act as **support / resistance** because market makers and institutions often
hedge or roll at those strikes. The Options Chain (see [[Options Chain]])
displays OI per strike.

## OI vs volume

| | Volume | Open Interest |
|---|--------|---------------|
| Resets each day | Yes | No (cumulative) |
| Counts new contracts | Yes | Only when OI changes |
| Use | Daily liquidity gauge | Positioning + support/resistance read |

Both shown on standard option chain displays. Volume gives "how much traded
today"; OI gives "how much is still on the books."

## OI at expiry

For monthly options, OI collapses into expiry as positions close. The **peak
OI strikes** often pin the underlying into expiry. See [[Expiration]] for
pin risk.

## Sources

[^1]: CBOE — Options Open Interest definition.
    https://www.cboe.com/education/glossary
[^2]: CME Group — Understanding Open Interest (PDF).
    https://www.cmegroup.com/education/files/Understanding-Open-Interest.pdf
[^3]: Investopedia — Open Interest.
    https://www.investopedia.com/terms/o/openinterest.asp
