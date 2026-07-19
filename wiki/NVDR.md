---
title: NVDR
type: concept
status: learning
tags: [spot, market/thailand]
aliases: [Non-Voting Depository Receipt, Thai NVDR]
---

# NVDR — Non-Voting Depository Receipt

A **Non-Voting Depository Receipt** is a Thai-market wrapper issued by the
**Thailand Securities Depository (TSD)** that lets investors (foreign or
otherwise) hold **economic exposure** to a SET-listed company **without the
voting rights** of the underlying shares.

## Why NVDRs exist

Some SET companies restrict **foreign ownership** at the board-meeting level
(voting rights), not at the economic level. NVDRs give foreign investors the
**cash-flow and price exposure** without breaching those limits. The Thai
capital-gains and dividend-withholding tax treatment differs from ordinary
shares — typically **dividends are WHT-exempt on NVDRs** vs ordinary shares.

## Mechanics

- NVDRs trade on the SET under a separate ticker suffix (typically **"-NVDR"**)
  and follow the same price band and [[Board Lot]] rules as the underlying.
- They can be **converted into ordinary shares** if the foreign-ownership cap
  is not yet hit — this is a one-way door (NVDR → share) used to remove the
  wrapper.
- Settle T+2 via TSD, same as ordinary shares (see [[Settlement]]).

## Trading implications

- **Price** — NVDRs usually trade at a small discount to the underlying ordinary
  share, reflecting the lack of voting rights. The discount widens when voting
  matters (M&A, takeover defense) and narrows otherwise.
- **Dividends** — no WHT on NVDR dividends for most investors (a pro for
  long-only foreign income strategies).
- **Tax** — capital gains on NVDRs are taxed under Thai personal income tax
  rules, same regime as ordinary shares. Confirm with a tax advisor.

## For derivatives traders

- NVDRs are **not deliverable** into single-stock futures (SSF) or single-stock
  options in most cases — SSF delivers ordinary shares. Owning NVDRs of the
  underlying does not let you short the SSF for arbitrage coverage without
  first unwinding.
- For index products (S50 futures, S50 options) the underlying basket is
  ordinary shares — NVDR exposure does not give you index hedge exposure
  one-for-one.

## Related
- [[Spot — Basics]] · [[Settlement]] · [[Board Lot]]

## Sources
[^1]: `raw/spot-basics.md`
[^2]: SET / TSD — NVDR program documentation.
