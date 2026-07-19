---
title: SET50 Futures
type: concept
status: learning
tags: [futures, derivatives, market/thailand]
aliases: [S50, S50 Futures, SET50 Index Futures]
---

# SET50 Futures (S50)

The **flagship derivative on [[TFEX Market Structure|TFEX]]**. Tracks the
**SET50 Index** — Thailand's 50 largest, most liquid stocks, market-cap
weighted, recalculated continuously during trading hours.

Major constituents: PTT, AOT, ADVANC, DELTA, CPALL, SCB, KBANK. [^1]

## Contract specifications

| Spec | Value |
|------|-------|
| Symbol | **S50** |
| Underlying | SET50 Index |
| Multiplier | **฿200 / index point** |
| Tick size | **0.1 point** |
| Tick value | **฿20** |
| Settlement | Cash |
| Margin | SPAN (฿15,000–฿30,000 typical) |

**Worked:** SET50 at 820 → contract value = 820 × 200 = **฿164,000**. Each
1-point move = ฿200 / contract; each tick = ฿20.

## Contract months

Always listed: **3 nearest monthly** + **next 3 quarterly** (Mar/Jun/Sep/Dec).

```
Example: Jul Aug Sep Dec Mar Jun
```

## Trading hours

| Session | Time (Bangkok) |
|---------|----------------|
| Morning | **09:45–12:30** |
| Afternoon | **13:45–16:55** |
| Pre-open | before each session |

**No night session** (unlike USD/THB futures). Daily close is hard — no
overnight S50 quote.

## Expiration

- Last trading day = business day immediately preceding the last business
  day of the contract month.
- Trading stops at **16:30** on expiration day.
- Cash settlement — no stock delivery.

## Final settlement price

Average SET50 over the **last 15 minutes** + the closing index, **highest 3
and lowest 3 values removed**, rounded to 2 decimals.

This trim reduces end-of-day manipulation. **Pin risk** is real for anyone
holding positions straddling the settlement window — see [[Expiration]].

## What moves SET50

| Driver | Weight |
|--------|--------|
| **Foreign fund flow** | Largest single driver. Foreign net buy/sell on SET = direct SET50 pressure |
| **Global markets** | S&P 500, Nasdaq, Nikkei, Hang Seng overnight |
| **Thai macro** | GDP, inflation, BOT policy rate, fiscal policy, tourism, exports |
| **Constituent earnings** | PTT, AOT, DELTA, ADVANC = large index weight |
| **Political events** | Thai political shifts move foreign sentiment fast |

## Common strategies

| Family | Examples |
|--------|----------|
| Trend following | EMA crossover, Donchian breakout, ADX filter, MA |
| Swing | Support/resistance, prior-day H/L, weekly breakout |
| Mean reversion | Range oscillation in low-vol regimes |
| Calendar spread | Long Sep / Short Dec — trade spread, not direction. See [[Calendar Spread]]. |

## Worked example — long S50

- SET50 = **820**. Buy 1 S50 future at **822**.
- Contract value = ฿164,400. Initial margin ≈ ฿20,000.
- SET50 rises to **835** (+13 points):
  - MTM gain = 13 × 200 = **+฿2,600**.
  - On ฿20,000 margin = **+13% return on margin** for a 1.6% underlying move.
- SET50 drops to **802**:
  - MTM loss = 20 × 200 = **−฿4,000**. **Margin call** (full margin gone on
    −2.4% underlying move). Liquidated at broker discretion.

> Leverage ~25× at typical margin. Small moves = large P&L. **Always know
> IM / MM before sizing.** See [[Margin Mechanics]].

## Related

- [[TFEX Market Structure]] · [[Futures — Basics]] · [[SET50 Options]] ·
  [[USD-THB Futures]] · [[Contango]] · [[Backwardation]] · [[Basis]] ·
  [[Calendar Spread]] · [[Margin Mechanics]] · [[Expiration]] · [[Tick Size]]

## Sources

[^1]: `raw/set50-futures-and-options.md`
[^2]: TFEX — SET50 Index Futures Contract Specification.
    https://www.tfex.co.th/en/products/equity/set50-index-futures/contract-specification
