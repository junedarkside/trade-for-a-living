---
title: TSD Settlement
type: concept
status: learning
tags: [spot, derivatives, market/thailand]
aliases: [TSD, Thailand Securities Depository, T+1, T+2, Settlement Cycle]
---

# TSD Settlement

The **Thailand Securities Depository (TSD)** is the central scripless
securities depository for SET and mai-listed securities. It also handles
bonds, government bonds, and certain derivatives settlement flows.

## Role [^1]

> *"TSD acts as a central scripless securities depository and registration
> for listed securities in SET and mai. Including unlisted securities such
> as Bond and Government Bond."* [^1]

## Settlement cycle (cash equities)

- **Old cycle**: **T+2** (long-standing).
- **New cycle**: **T+1 effective Monday, 2 June 2025**. SET announcement
  id=5340 confirmed. Aligns Thailand with US (May 2024), India; ahead of
  EU (Oct 2027 planned). [^2]

> Implication: foreign trade settlement completes **one business day
> after execution** since 2 June 2025 — broker cash debits/credits move
> one day earlier than under T+2.

## Settlement modes

TSD offers:

- **Delivery vs Payment (DvP)** — atomic cash + securities exchange.
- **Gross Settlement** — trade-for-trade.
- **Net Settlement** — netting by participant / account. [^3]

## Corporate actions

Standard TSD capabilities include processing:

- Dividends
- Stock splits
- Rights / warrants
- Capital actions

Specific cut-off times not publicly listed on the TSD landing page (gated);
broker confirmation typically required.

## NVDR settlement

NVDR is a TSD-issued trading instrument allowing foreign investors to
hold Thai securities using the same trading and settlement procedures as
ordinary shares **without voting rights**. Settles in the same **T+1**
cycle post-2 June 2025. See [[NVDR]].

## Derivatives settlement

TFEX-traded derivatives settle through Thailand Clearing House (TCH), not
TSD directly. Cash settlement for index options/futures happens through
the clearing member's account daily (MTM) and at expiry.

## Practical trader implications

| Cadence | Action |
|---------|--------|
| **Daily** | Foreign trade settlement now completes T+1 — broker cash debits/credits move one day earlier than under T+2 |
| **Monthly** | Track ex-dividend dates relative to T+1 record dates — sell-side traders trading through XD cannot capture dividend after record date |
| **Annual** | If using a global custodian on legacy T+2 SLA — contract renegotiation required |

## Related

- [[Spot — Basics]] · [[NVDR]] · [[Settlement]] · [[Single-Stock Futures]] ·
  [[Thai Derivatives Tax]] · [[SET50 Index]]

## Sources

[^1]: `raw/tsd-settlement.md`
[^2]: TSD — Post-Trade Services.
    https://www.set.or.th/tsd/en/products-services/post-trade.html
[^3]: SET — T+1 Announcement (id=5340).
    https://www.set.or.th/en/announcement/set-announcement/announcement-detail?id=5340
[^4]: TSD — Settlement Services.
    https://www.set.or.th/tsd/en/products-services/settlement.html
[^5]: ICE — Thailand Settlement Cycle.
    https://www.ice.com/equities/us-equities/market-structure/foreign-listing/thailand-settlement-cycle
