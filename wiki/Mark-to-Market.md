---
title: Mark-to-Market
type: concept
status: learning
tags: [futures, options, derivatives]
aliases: [MTM, Mark to Market]
---

# Mark-to-Market (MTM)

**Mark-to-market** is the **daily (often intraday) revaluation** of open
derivative positions to current market prices. Gains and losses are
**realised into cash** in the trader's account each session — without
closing the position. This is the fundamental cash-flow distinction between
futures and spot.

## How it works (futures example)

- Long 1 S50 future at **25,500** (contract value ฿5,100,000).
- Settlement at session close: SET50 at **25,580**.
- MTM gain = (25,580 − 25,500) × 200 = **+฿16,000** credited to your account.
- Account equity increased by ฿16,000 without closing the position.

Next session, SET50 drops to 25,500:
- MTM loss = (25,500 − 25,580) × 200 = **−฿16,000** debited from your account.
- Account equity back to original.

Net result over 2 sessions: zero. But the **+฿16,000 was usable,
withdrawable capital** during the holding period — that's the MTM cash flow
edge.

## MTM vs unrealised P&L (equities)

| | MTM (futures) | Unrealised P&L (spot) |
|---|---|---|
| Cash impact | **Yes** — settled daily | No — only on close |
| Margin | Adjusted daily | n/a (full notional) |
| Counterparty | Clearinghouse | Broker |

Equity holders can sit on +50% unrealised gains indefinitely without cash
impact. Futures traders see cash move every day — which is **why margin
calls can trigger liquidation cascades in crashes** (see [[Margin
Mechanics]]).

## MTM in options

Options on futures are **MTM'd daily on the option premium**, not the
underlying. Option value recalculated to current mid; gains/losses settled
into account. The option's [[Delta|delta]] and [[Gamma|gamma]] drive
next-session value changes.

For Thai options on futures (e.g., S50 options), MTM happens at session close
per TFEX rules.

## Why MTM matters

1. **Liquidity** — daily cash settlement frees margin for redeployment.
2. **Counterparty risk** — clearinghouse collects MTM losses immediately;
   no build-up of uncollectible exposure.
3. **Crisis dynamics** — fast MTM losses force margin calls, which force
   liquidation, which forces more losses (death spiral). This is what
   regulators fear and what circuit breakers try to dampen.
4. **Performance attribution** — daily MTM lets you track realised vs
   unrealised P&L cleanly.

## Related

- [[Futures — Basics]] · [[Margin Mechanics]] · [[Settlement]] ·
  [[Position Greeks]] · [[Risk Management]] · [[Delta]] · [[Gamma]] ·
  [[SET50 Futures]]

## Sources

[^1]: `raw/mark-to-market.md`
[^2]: CME Group — Mark-to-Market mechanics.
    https://www.cmegroup.com/education/courses/introduction-to-futures/mark-to-market.html
[^3]: Hull, *Options, Futures, and Other Derivatives*, 10th ed., Ch. 1.
[^4]: Investopedia — Mark to Market.
    https://www.investopedia.com/terms/m/marktomarket.asp
