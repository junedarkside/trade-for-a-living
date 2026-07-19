---
title: Pre-Trade Checklist
type: reference
status: learning
tags: [options, derivatives, risk]
---

# Pre-Trade Checklist

**One-page quick reference.** Run through before every options trade. Companion
to [[Options Risk Management]] (full playbook).

## The 7 questions

1. **Market view?** — direction, vol, time.
2. **Strategy fits view with defined risk?** — prefer spreads/condors/collars over naked shorts.
3. **Max profit / max loss / break-evens?** — known before entry.
4. **Capital risked?** — % and absolute (e.g., "1% = ฿5,000").
5. **Exit rules?** — price level, time stop, Greeks threshold, P&L target.
6. **Fit with other open positions?** — no correlated blow-ups.
7. **Stress scenario outcome?** — survives ±5–10% gap, ±20–30% IV shock, flat 5–10 days?

## Sizing quick-formula

```
Lots = risk_per_trade ÷ max_loss_per_lot,  rounded down
```

If result is < 1 → trade smaller, reduce risk budget, or skip.

## Default risk budgets

- **Per trade**: 0.5–2% of equity.
- **Portfolio**: total max loss across all positions ≤ 5–10% of equity.

## Stop-loss quick reference

| Position | Stop anchor | Adjustment |
|----------|-------------|------------|
| Long options | Premium drop 40–60% OR underlying break | Tighter near expiry |
| Short options / spreads | Net debit/credit OR underlying invalidation | Wider in high vol; tighter near expiry for short premium |

## Time exit

- Exit before known events (earnings, policy).
- Exit X days before expiry — gamma blows up near the pin.

## Pass / no-pass rule

- "**If you can't answer all 7 questions clearly, the trade isn't ready.**"
- "**If you wouldn't take it at half size, don't take it at all.**"

## Related
- [[Options Risk Management]] · [[Risk Management]] · [[Greeks in Practice]]

## Sources
[^1]: `raw/options-risk-management.md`