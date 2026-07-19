---
title: SET50 Options
type: concept
status: learning
tags: [options, derivatives, market/thailand]
aliases: [S50C, S50P, S50 Options, SET50 Index Options]
---

# SET50 Options (S50C / S50P)

**European-style index options** on the [[SET50 Futures|SET50 Index]] traded
on [[TFEX Market Structure|TFEX]]. Tickers **S50C** (call) and **S50P** (put).
Cash-settled. Same multiplier as the underlying future.

## Contract specifications

| Spec | Value |
|------|-------|
| Tickers | **S50C** (call), **S50P** (put) |
| Underlying | SET50 Index |
| Multiplier | **฿200 / index point** (same as futures) |
| Style | **European** — exercise only at expiry |
| Tick size | 0.1 point |
| Tick value | **฿20** |
| Settlement | Cash |
| Strike interval | **10 index points** |
| Listed months | **3 nearest monthly** + **1 quarterly** |
| Strike coverage | At least **5 ITM + 5 OTM + 1 ATM** per expiry |

## Strike grid example (SET50 = 820)

```
760  770  780  790  800  810  820  830  840  850
```

TFEX lists wider grids around events. At expiry, ATM shifts to whatever the
near-month underlying price is.

## Why European matters

- **No early assignment** — see [[Assignment]]. Short positions can be held
  through to expiry without dividend-timing surprises.
- **Clean parity** — [[Put-Call Parity]] holds as equality (mod rates +
  dividends), enabling synthetic construction.
- **Cleaner risk management** — no need to monitor early-exercise value
  decay.

## Worked example — long 820 call

- Buy 1 contract **820 Call** at **15 points** premium.
- **Cost** = 15 × 200 = **฿3,000**.
- At expiry SET50 = 845 → intrinsic = 25 → option value = 25 × 200 =
  **฿5,000**.
- **Net profit** = ฿5,000 − ฿3,000 = **+฿2,000 / contract**.

Counter-example: at expiry SET50 = 810 → option OTM → expires worthless →
**max loss = ฿3,000** (the premium).

## Popular strategies

| Family | Strategies |
|--------|-----------|
| Directional | [[Long Call]], [[Long Put]] |
| Income | [[Covered Call]] on futures hedge, [[Short Put]] (margin-aware) |
| Volatility | [[Long Straddle]], [[Strangle]], short variants, [[Iron Condor]] |
| Trend | Calls in uptrend / puts in downtrend, [[Vertical Spread\|Bull Call / Bear Put]] spreads, **ratio backspread** for vol expansion |
| Premium selling | [[Iron Condor]], [[Short Strangle]], [[Risk Reversal]] — all leverage [[Volatility Risk Premium\|VRP]] on Thai market |

## Liquidity profile

- **S50 Futures** — most liquid TFEX derivative. Intraday, swing, systematic
  all viable.
- **S50 Options** — concentrated at:
  - **Near-month expiry** (most volume rolls off 2 weeks before expiry)
  - **ATM strikes** (10 delta each side)
  - **Popular strikes** — heavy [[Options Chain\|OI walls]] at the round
    numbers the market defends
- **Deep ITM / OTM and longer-dated** = wider bid/ask → bleed edge on entry
  and exit. Skip these for trading; reserve for hedging only.

## Greeks context

S50 options have full Greek profile — see [[Greeks]]:

| Greek | Long ATM call | Short OTM put |
|-------|---------------|---------------|
| Delta | +0.5 | −0.2 |
| Gamma | high ATM, decays OTM | high near short strike |
| Theta | negative (you pay) | positive (you collect) |
| Vega | positive | positive |
| Rho | small positive | small negative |

For multi-leg structures (spreads, condors) use [[Position Greeks]] to read
the combined exposure.

## Related

- [[SET50 Futures]] · [[TFEX Market Structure]] · [[Options — Basics]] ·
  [[Implied Volatility]] · [[IV Skew, Smile & Surface]] · [[Put-Call Parity]]
  · [[Options Strategy]] · [[Options Chain]] · [[Volatility Risk Premium]] ·
  [[Black Model]] · [[Options Risk Management]] · [[Assignment]] ·
  [[Expiration]] · [[Position Greeks]]

## Sources

[^1]: `raw/set50-futures-and-options.md`
[^2]: TFEX — SET50 Index Options Contract Specification.
    https://www.tfex.co.th/en/products/equity/set50-index-options/contract-specification
