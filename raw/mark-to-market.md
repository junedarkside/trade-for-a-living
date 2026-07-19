---
title: Mark-to-Market
type: source
tags: [futures, options, derivatives]
---

# Mark-to-Market (MTM)

**Mark-to-market (MTM)** is the daily (often intraday) revaluation of open
derivative positions to reflect current market prices. Gains and losses are
**realised into cash** in the trader's account each session. [^1]

## How it works (futures example)

- Long 1 S50 future at 25,500 (contract value ฿5,100,000).
- Settlement at session close: SET50 settles at 25,580.
- MTM gain = (25,580 − 25,500) × 200 = **+฿16,000** credited to your account.
- Account equity increased by ฿16,000 **without you closing the position**.

Next session, if SET50 drops to 25,500:
- MTM loss = (25,500 − 25,580) × 200 = **−฿16,000** debited from your account.
- Account equity back to original.

Net result: zero. But the **cash flow** during the holding period was real —
the +฿16,000 was usable, withdrawable capital.

## MTM vs unrealised P&L

| | MTM (futures) | Unrealised P&L (equity) |
|---|---|---|
| Cash impact | **Yes** — settled daily | No — only on close |
| Margin | Adjusted daily | n/a (full notional) |
| Counterparty | Clearinghouse | Broker |

This is the fundamental difference between futures and spot. Equity holders
can sit on +50% unrealised gains indefinitely without cash impact. Futures
traders see cash move every day — which is why margin calls can trigger
liquidation cascades in crashes.

## MTM in options

Options on futures are **MTM'd daily on the option premium**, not the
underlying. The option's value is recalculated to current mid; gains/losses
settled into account. The option's delta/gamma still drive next-session
value changes.

## Why MTM matters

1. **Liquidity** — daily cash settlement frees up margin for redeployment.
2. **Counterparty risk** — clearinghouse collects MTM losses immediately;
   no build-up of uncollectible exposure.
3. **Crisis dynamics** — fast MTM losses force margin calls, which force
   liquidation, which forces more losses (death spiral). This is what
   regulators fear and what circuit breakers try to dampen.

## Sources

[^1]: CME Group — Mark-to-Market mechanics.
    https://www.cmegroup.com/education/courses/introduction-to-futures/mark-to-market.html
[^2]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 1.
[^3]: Investopedia — Mark to Market.
    https://www.investopedia.com/terms/m/marktomarket.asp
