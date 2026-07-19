---
title: Single-Stock Futures
type: source
tags: [futures, derivatives, market/thailand]
---

# TFEX Single-Stock Futures (SSF) — Research Notes

**Single-stock futures (SSF)** on TFEX are futures contracts on individual
SET-listed equities. Used for single-name directional exposure, hedging
existing equity positions, and basis trades against the underlying stock.

## Contract specifications

| Spec | Value |
|------|-------|
| Underlying | Individual SET-listed common shares |
| Contract size | **1,000 shares** per contract |
| Multiplier | 1,000 |
| Tick size | **฿0.01** |
| Tick value | **฿10** (1,000 shares × ฿0.01) |
| Settlement | **Cash** at expiry (per TFEX spec) [^1] |
| Settlement currency | THB |
| Margin | SPAN-equivalent (per TFEX / broker) |
| Listed names | ~50 SET large-caps (subject to TFEX listing policy) |

> **Settlement clarification**: TFEX product spec describes SSF as
> cash-settled at expiry; equity delivery is not the standard mechanic.
> Check current TFEX rulebook for confirmation as contracts update. [^1]

## Major underlyings (typical)

- **Banking**: KBANK, SCB, TTB, KKP, BBL
- **Energy**: PTT, PTTEP, TOP
- **Communications**: ADVANC, TRUE, DTAC (subject to mergers)
- **Retail / commerce**: CPALL, CRC, BJC
- **Materials**: SCC, BANPU
- **Transport**: AOT, BTS, BEM
- **Property / construction**: CPN, AP, LH

Full list on TFEX product page; new names added as liquidity permits.

## Trading hours

Per TFEX — typically SET cash session alignment. Check current TFEX rules
per contract; some SSF may have extended hours.

## Expiration

- **Listed months**: 6 nearest serial months + next 2 quarter months
  (Mar/Jun/Sep/Dec), depending on underlying liquidity.
- **Last trading day**: business day preceding last business day of
  contract month.
- **Final settlement**: cash (per TFEX rulebook — verify against latest spec).

## Margin

- **Maintenance margin**: typically **1.75×** of standard IM (local retail)
  or **1.35×** (institutional). [^1]
- TFEX publishes margin schedules via Thailand Clearing House (TCH).
- IM/MM vary by underlying volatility.

## Daily price limits

Some SSF contracts carry daily price limits tied to the underlying SET
ceiling/floor. Confirm per contract — not all SSF have hard limits.

## Corporate actions

- **Cash dividends** — standard TFEX adjustment applies (price
  adjusted down by dividend amount on ex-date).
- **Special dividends / capital actions** — TFEX issues adjustment
  notice. Example: Feb 2026 ADVANC SSF adjustment for special
  dividend. [^2]
- **Stock splits / bonus issues** — contract size or strike adjusted per
  TFEX rules.

## NVDR interaction

NVDRs track the **ordinary share**, but TFEX SSF delivers/settles based
on the **common share**. NVDR holders can't use NVDRs to deliver into SSF.
For dividend tax, NVDR holders face 10% WHT (no Thai dividend-tax
exemptions available to ordinary shares — BOI exemption, inter-corporate
5% rate do not apply to NVDRs). [^3]

## Worked example — long KBANK SSF

- KBANK spot = **฿150**.
- Buy 1 KBANK SSF at **฿150.50**.
- Contract value = ฿150.50 × 1,000 = **฿150,500**.
- Initial margin ≈ ฿15,000 (variable).
- KBANK rises to **฿160**:
  - MTM gain = (160 − 150.50) × 1,000 = **+฿9,500**.
  - On ฿15,000 margin ≈ **+63% return on margin** for a 6.3% underlying
    move.
- KBANK drops to **฿140**:
  - MTM loss = (140 − 150.50) × 1,000 = **−฿10,500**. Margin call;
    liquidation risk if not topped up.

## Strategy uses

| Use | Example |
|-----|---------|
| **Single-name directional** | Long KBANK SSF instead of buying KBANK shares (margin leverage) |
| **Hedge existing stock position** | Short KBANK SSF against long KBANK shares (delta hedge) |
| **Basis trade** | Long KBANK shares + short KBANK SSF when SSF trades above fair carry-adjusted value |
| **Pair trade** | Long KBANK SSF + short SCB SSF on relative-value view |
| **Index arbitrage building block** | Long basket of SSFs vs short S50 futures |

## Sources

[^1]: TFEX — Single-Stock Futures.
    https://www.tfex.co.th/en/products/equity/single-stock-futures
[^2]: TFEX — Contract Adjustment Notice (ADVANC SSF, Feb 2026).
    https://www.tfex.co.th/en/
[^3]: SET — NVDR Tax Treatment.
    https://www.set.or.th/en/products/nvdr/nvdr-tax
[^4]: Thailand Clearing House (TCH) — Margin schedules.
    https://www.tch.or.th/
