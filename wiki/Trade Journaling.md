---
title: Trade Journaling
type: concept
status: learning
tags: [risk, derivatives]
aliases: [Trade Journal, Journal, Trade Log]
---

# Trade Journaling

A trade journal is the **feedback loop** that converts execution into
improvement. Without one, you repeat mistakes and lose the ability to
diagnose what's working.

## Minimum data schema (per trade)

| Field | What to capture |
|-------|-----------------|
| Date / time entry + exit | Exact timestamps |
| Instrument | Ticker / contract |
| Direction | Long / short |
| Size | Contracts or shares |
| Entry price + exit price | Per unit |
| Stop + target | Pre-trade plan |
| Setup type | Tagged (e.g., "IV rank > 70 short strangle") |
| Market regime | Tagged (trending / range-bound / high vol) |
| Rationale | 1–2 sentences |
| Greeks at entry | Delta, gamma, theta, vega |
| Emotion pre/during/post | 1–5 scale |
| Screenshot | Chart at entry |
| Result | P&L in THB and R-multiples |

## Logging cadences

| When | Action | Time |
|------|--------|------|
| **Pre-trade** | Log setup type, stop, target, size | ≤ 30s |
| **During-trade** | Note execution quality + emotion shift | as it happens |
| **Post-trade** | Log full schema + screenshot | ≤ 5 min |

## Review cadence

| Cadence | Time | Purpose |
|---------|------|---------|
| **Daily** | 5 min | Catch discipline violations |
| **Weekly** | 30–60 min | Strategy-level performance review |
| **Monthly** | 2–3 hours | Edge health, regime fit, rule audit |
| **Quarterly** | Full audit | Strategy retire / promote decisions |

## Common mistakes

1. **Rationalisation** — rewriting the rationale after the trade.
2. **Hindsight bias** — "I knew it" when you didn't.
3. **Survivorship** — only logging interesting trades, skipping losers.
4. **Quantity over quality** — logs without structure or review.

## Key metrics

```
Win Rate = winners / total trades
Loss Rate = losers / total trades
Avg Win = mean(P&L | P&L > 0)
Avg Loss = mean(P&L | P&L < 0)
Payoff Ratio = Avg Win / |Avg Loss|
Profit Factor = sum(wins) / sum(|losses|)
Expectancy = (Win Rate × Avg Win) − (Loss Rate × |Avg Loss|)
```

**Example:** 40% win rate, 3:1 R:R → Expectancy = +0.6R per trade.
Positive expectancy → long-run profitable even with sub-50% win rate.

## Tools

| Tool | Strength |
|------|----------|
| **Edgewonk** ($169/yr) | Deep analytics, R-multiple tracking |
| **Tradervue** | Broker integration, social/journal community |
| **TraderSync** | Modern UI, broker auto-sync |
| **Obsidian** (this vault) | Free, full markdown, integrates with knowledge base |

## Obsidian integration (this vault)

The vault's `master-state.md` records session-level progress; per-trade
journal entries can live as standalone notes (e.g., `journal/2026-07-19-
short-strangle-s50.md`) and link to the relevant strategy article (e.g.,
[[Short Strangle]]). Tag with `#status/reviewed` once trade is closed and
reviewed.

## Related

- [[Daily Routine & Market Prep]] · [[Position Sizing Frameworks]] ·
  [[Backtesting & Forward Testing]] · [[Options Risk Management]] ·
  [[P&L Attribution]] · [[Volatility Risk Premium]]

## Sources

[^1]: `raw/trade-journaling.md`
[^2]: Tharp, *Trade Your Way to Financial Freedom*, 2006.
[^3]: Edgewonk — journaling methodology.
[^4]: Steenbarger, *The Psychology of Trading*, 2003.
[^5]: Douglas, *Trading in the Zone*, 1990.
