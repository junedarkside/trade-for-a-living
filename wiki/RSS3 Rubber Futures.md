---
title: RSS3 Rubber Futures
type: concept
status: learning
tags: [futures, commodities, market/thailand]
aliases: [RSS3, RSS3D, JRF, Rubber Futures, Japanese Rubber]
---

# TFEX Rubber Futures

TFEX lists **3 agricultural contracts**: JRF (Japanese Rubber Futures,
cash-settled OSE-referenced), RSS3 and RSS3D (both physical delivery).
**No rice, palm oil, or tapioca contracts exist.**

## RSS3 vs RSS3D

Functionally identical contracts — same specs, same physical delivery, same
expiry rules. "D" likely denotes a different delivery series / month
offset.

| Field | Value |
|-------|-------|
| Ticker | RSS3 / RSS3D |
| Underlying | RSS3 (Green Book standard); must be from TCH-approved producer |
| Contract size | **5,000 kg** (5 tons) per contract |
| Delivery size | **20,000 kg** (4 contract units) |
| Quotation | THB / kg |
| Tick size | THB 0.05 |
| Tick value | **฿250 / contract** |
| Listed months | **7 nearest consecutive** months |
| Trading hours | Day only — pre-open 09:15–09:45; trading 09:45–16:55 |
| Last trading day | Bus day before last bus day of month |
| Settlement | **Physical delivery** (F.O.B. Bangkok/Laem Chabang or approved warehouse) |
| Final settlement price | VWAP on last trading day (if volume threshold met) |
| Daily price limit | ±5% → ±10% |
| Position limit | **1,000 contracts** (nearest month); **10,000 contracts** (all months combined) |
| Exchange fee | Max **฿40 / side** |

## JRF — Japanese Rubber Futures (cash-settled)

| Field | Value |
|-------|-------|
| Ticker | JRF |
| Underlying | Japanese Natural RSS3 |
| Contract size | 300 × reference price multiplier |
| Quotation | **JPY per kg** |
| Tick size | JPY 0.10 per contract unit |
| Price limit | ±10% → ±20% |
| Listed months | **6 nearest consecutive** months |
| Trading hours | Day only — pre-open 09:15–09:45; trading 09:45–16:55 |
| Last trading day | **4th business day before** last bus day of month; ends **13:15** |
| Settlement | **Cash in THB** |
| Final settlement | **OSE RSS3 settlement price**; no FX adjustment |
| Exchange fee | Max **฿4 / side** |

> JRF launched 30 Nov 2020 via a TFEX-OSE (Osaka Exchange) agreement; lets
> Thai traders take RSS3 exposure using the more liquid OSE reference
> price, settled in THB without FX leg.

## Which contract for which use?

| Use case | Best contract |
|----------|---------------|
| **Hedger with physical rubber** | RSS3 or RSS3D (physical delivery) |
| **Trader / speculator on rubber price** | JRF (cleaner, OSE-referenced, no delivery) |
| **Lowest margin / fee** | JRF (4 baht / side vs 40 baht for RSS3) |

## Liquidity caveat

RSS3 / RSS3D volume has historically been **thin** relative to OSE/TCE
rubber. Most professional rubber exposure via TFEX is through **JRF**
(cash-settled, OSE-referenced) rather than physical RSS3.

## Sources

[^1]: `raw/rss3-rubber-futures.md`
[^2]: TFEX — RSS3 Futures Contract Specification.
    https://www.tfex.co.th/en/products/agriculture/rss3-futures/contract-specification
[^3]: TFEX — RSS3D Futures Contract Specification.
    https://www.tfex.co.th/en/products/agriculture/rss3d-futures/contract-specification
[^4]: TFEX — Japanese Rubber Futures (JRF) Spec PDF.
    https://media.tfex.co.th/tfex/Documents/2023/Mar/JRF_EN_21092021.pdf
[^5]: JPX/TFEX RSS3 Cross-listing Agreement (2020).
    https://www.jpx.co.jp/english/corporate/news/news-releases/0060/20201125-01.html
[^6]: Bangkok Post — TFEX rubber liquidity (2018).
    https://www.bangkokpost.com/business/general/1420811/tfex-deal-to-stretch-rubber-trade-liquidity
