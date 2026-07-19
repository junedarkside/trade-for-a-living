---
title: SET50 Futures & Options
type: source
tags: [futures, options, derivatives, market/thailand]
---

# SET50 Index Futures (S50) — Flagship derivative on TFEX

**Underlying:** SET50 Index — Thailand's 50 largest, most liquid stocks.
Market-cap weighted, recalculated continuously during trading hours.

Major constituents: PTT, AOT, ADVANC, DELTA, CPALL, SCB, KBANK. [^1]

## Contract Specification

| Item       | Value                       |
| ---------- | --------------------------- |
| Symbol     | S50                         |
| Underlying | SET50 Index                 |
| Multiplier | **฿200 per index point**    |
| Settlement | Cash                        |
| Tick Size  | **0.1 point**               |
| Tick Value | **฿20**                     |
| Exercise   | N/A (Futures)               |

Worked: SET50 = 820 → contract value = 820 × 200 = **฿164,000**. Each
1-point move = ฿200 / contract; each tick = ฿20.

## Contract Months

Always available: 3 nearest monthly + next 3 quarterly.

Example (current + next 3 quarters):

```
Jul  Aug  Sep  Dec  Mar  Jun
```

## Trading Hours

- Morning: **09:45–12:30**
- Afternoon: **13:45–16:55**
- Pre-open auctions before each session.
- **No night session** for S50 futures (unlike USD/THB futures).

## Expiration

Last trading day = business day immediately preceding the last business day
of the contract month. Trading stops at **16:30** on expiration day. [^1]

## Final Settlement

- Cash only — no stock delivery.
- Final settlement = average SET50 over last 15 minutes **plus** the closing
  index, **highest 3 and lowest 3 values removed**, rounded to 2 decimals.
- This trims end-of-day manipulation.

## Margin

SPAN methodology. Typical **฿15,000–฿30,000** depending on vol + broker.

## What moves SET50

- **Global markets** — S&P 500, Nasdaq, Nikkei, Hang Seng (overnight).
- **Foreign fund flow** — biggest single driver. Foreign buying supports;
  heavy selling pressures.
- **Thai macro** — GDP, inflation, BOT rates, gov policy, tourism, exports.
- **Constituent earnings** — PTT, AOT, DELTA, ADVANC moves the index.
- **Political events** — Thai political developments shift foreign sentiment.

## Common futures strategies

| Family | Examples |
|--------|----------|
| Trend following | EMA crossover, Donchian breakout, ADX filter, MA |
| Swing | Support/resistance, prior-day H/L, weekly breakout |
| Mean reversion | Range oscillation in low-vol regimes |
| Calendar spread | Long Sep / Short Dec — trade spread, not direction |

---

# SET50 Options (S50C / S50P)

| Spec | Value |
|------|-------|
| Tickers | S50C (call), S50P (put) |
| Underlying | SET50 Index |
| Multiplier | **฿200 / index point** (same as futures) |
| Style | **European** (exercise only at expiry) |
| Strike interval | **10 index points** |
| Tick size | 0.1 point |
| Tick value | ฿20 |
| Settlement | Cash |
| Listed months | 3 nearest monthly + 1 quarterly |

## Strike grid example (SET50 = 820)

760, 770, 780, 790, 800, 810, 820, 830, 840, 850. TFEX maintains **at least
5 ITM + 5 OTM + 1 ATM** strikes per expiry.

## Worked example — long 820 call

- Buy 1 contract **820 Call** at **15 points** premium.
- Cost = 15 × 200 = **฿3,000**.
- At expiry SET50 = 845 → intrinsic = 25 → option value = 25 × 200 = **฿5,000**.
- Net profit = ฿5,000 − ฿3,000 = **+฿2,000 / contract**.

## Popular strategies

- **Directional** — Long Call, Long Put.
- **Income** — Covered Call on futures, Short Put (margin-aware).
- **Volatility** — Long Straddle, Long Strangle, Short Straddle, Iron Condor.
- **Trend following** — Calls in uptrends, Puts in downtrends, Bull Call
  Spread, Bear Put Spread, Ratio Backspread (vol expansion expected).

## Liquidity profile

- **S50 Futures** — most liquid TFEX derivative. Intraday / swing /
  systematic all viable.
- **S50 Options** — concentrated at near-month expiry, ATM strikes, popular
  strikes. Deep ITM/OTM and longer-dated = wider bid/ask.

## Suggested workbench model (S50 Futures)

```yaml
Exchange: TFEX
Asset Class: Equity Index Futures
Underlying: SET50 Index
Symbol: S50
Multiplier: ฿200
Tick Size: 0.1
Tick Value: ฿20
Settlement: Cash
Margin: SPAN
Trading Sessions: [Morning, Afternoon]
Contract Months: 3 monthly + 3 quarterly
Last Trading Day: Business day before last business day of contract month
```

## Suggested workbench model (S50 Options)

```yaml
Asset Class: Equity Index Option
Underlying: SET50 Index
Style: European
Multiplier: ฿200
Strike Interval: 10 points
Settlement: Cash
Option Types: [Call, Put]
Contract Months: 3 monthly + 1 quarterly
```

## Sources

[^1]: TFEX — SET50 Index Futures Contract Specification.
    https://www.tfex.co.th/en/products/equity/set50-index-futures/contract-specification
[^2]: TFEX — SET50 Index Options Contract Specification.
    https://www.tfex.co.th/en/products/equity/set50-index-options/contract-specification
