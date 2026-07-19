---
title: Single-Stock Futures
type: concept
status: learning
tags: [futures, derivatives, market/thailand]
aliases: [SSF, Single Stock Futures, Stock Futures]
---

# Single-Stock Futures (SSF)

**Single-stock futures (SSF)** on [[TFEX Market Structure|TFEX]] are futures
contracts on individual SET-listed equities. Used for single-name
directional exposure, hedging existing equity positions, and basis trades
against the underlying stock.

## Contract specifications

| Spec | Value |
|------|-------|
| Underlying | Individual SET-listed common shares |
| Contract size | **1,000 shares** per contract |
| Multiplier | 1,000 |
| Tick size | **฿0.01** |
| Tick value | **฿10** (1,000 shares × ฿0.01) |
| Settlement | **Cash** at expiry (per TFEX spec) [^1] |
| Margin | SPAN-equivalent (per TFEX / broker) |
| Listed names | ~50 SET large-caps (subject to TFEX listing policy) |

> Confirm current settlement mechanic in TFEX rulebook — historically
> cash-settled, with delivery rules for special cases.

## Major underlyings (typical)

| Sector | Names |
|--------|-------|
| **Banking** | KBANK, SCB, TTB, KKP, BBL |
| **Energy** | PTT, PTTEP, TOP |
| **Communications** | ADVANC, TRUE |
| **Retail / commerce** | CPALL, CRC, BJC |
| **Materials** | SCC, BANPU |
| **Transport** | AOT, BTS, BEM |
| **Property** | CPN, AP, LH |

Full list on TFEX product page; new names added as liquidity permits.

## Margin

- **Maintenance margin**: typically **1.75×** standard IM (local retail)
  or **1.35×** institutional. [^1]
- TFEX publishes margin schedules via Thailand Clearing House (TCH).
- IM/MM vary by underlying volatility.

## Daily price limits

Some SSF contracts carry daily price limits tied to the underlying SET
ceiling/floor. **Confirm per contract** — not all SSF have hard limits.

## Corporate actions

- **Cash dividends** — standard TFEX adjustment (price adjusted down by
  dividend amount on ex-date).
- **Special dividends / capital actions** — TFEX issues adjustment
  notice (e.g., Feb 2026 ADVANC SSF). [^2]
- **Stock splits / bonus issues** — contract size or strike adjusted per
  TFEX rules.

## NVDR interaction

NVDRs track the **ordinary share**, but TFEX SSF settles based on the
**common share**. NVDR holders can't use NVDRs to deliver into SSF.

For dividend tax: NVDR holders face **10% WHT** (no Thai dividend-tax
exemptions available to ordinary shares — BOI exemption, inter-corporate
5% rate do not apply to NVDRs). [^3]

## Worked example — long KBANK SSF

- KBANK spot = **฿150**.
- Buy 1 KBANK SSF at **฿150.50**.
- Contract value = ฿150.50 × 1,000 = **฿150,500**.
- Initial margin ≈ ฿15,000 (variable).
- KBANK rises to **฿160**:
  - MTM gain = (160 − 150.50) × 1,000 = **+฿9,500**.
  - On ฿15,000 margin ≈ **+63% return on margin** for a 6.3% move.
- KBANK drops to **฿140**:
  - MTM loss = (140 − 150.50) × 1,000 = **−฿10,500**. Margin call.

## Strategy uses

| Use | Example |
|-----|---------|
| **Single-name directional** | Long KBANK SSF instead of buying KBANK shares |
| **Hedge existing stock position** | Short KBANK SSF against long KBANK shares |
| **Basis trade** | Long KBANK shares + short KBANK SSF on mispriced basis |
| **Pair trade** | Long KBANK SSF + short SCB SSF on relative view |
| **Index arb building block** | Long basket of SSFs vs short [[SET50 Futures]] |

## Risks

- **Single-name concentration** — diversifies nothing vs long stock.
- **Corporate action risk** — adjustments can catch traders off-guard.
- **Liquidity varies by name** — not all SSF trade actively.
- **Margin call risk** — same as any futures, but single-name moves can
  be larger % than index moves.
- **Dividend timing** — if you're hedged long stock + short SSF, dividend
  passes from long holder to you.

## Related

- [[TFEX Market Structure]] · [[Futures — Basics]] · [[SET50 Futures]] ·
  [[NVDR]] · [[Margin Mechanics]] · [[Settlement]] · [[Basis]] ·
  [[Delta-Neutral Hedging]] · [[Risk Management]]

## Sources

[^1]: `raw/single-stock-futures.md`
[^2]: TFEX — Single-Stock Futures.
    https://www.tfex.co.th/en/products/equity/single-stock-futures
[^3]: TFEX — Contract Adjustment Notice (ADVANC SSF, Feb 2026).
    https://www.tfex.co.th/en/
[^4]: SET — NVDR Tax Treatment.
    https://www.set.or.th/en/products/nvdr/nvdr-tax
[^5]: Thailand Clearing House (TCH) — Margin schedules.
    https://www.tch.or.th/
