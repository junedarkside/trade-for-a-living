---
title: IV & Market Mechanics — Source Bundle
type: source
tags: [options, futures, derivatives]
---

# IV & Market Mechanics — Source Bundle

Source material covering five Tier 1 pro-trader foundational topics.
Each section feeds a dedicated wiki article (one concept per article per
vault-schema.md).

## 1. Implied Volatility (IV)

**Definition.** IV = market's forward-looking estimate of how much the
underlying will move over the option's life, expressed as annualised standard
deviation. Backed out from option prices using a pricing model (Black-Scholes
for equities, Black for futures). [^1]

**Forward vs historical.**
- HV (historical volatility) = how volatile the underlying *has been*.
- IV = how volatile the market *expects* it to be. [^2]

**Price impact.** Higher IV → higher option premiums. IV is the "price of
volatility". [^3]

**Standard read.** Spot 100, IV 20% → ~68% probability price is in [80, 120]
over one year (one σ). [^4]

**IV crush.** IV typically rises before known events (earnings, policy), then
collapses after as uncertainty resolves → long option holders can lose even if
direction was right. [^5]

**Trader use.** Gauge cheap/expensive vs history (IV rank / IV percentile) and
vs RV (VRP). High IV → favor short premium; low IV → favor long options. [^3]

## 2. IV Skew and Volatility Surface

**Skew.** In Black-Scholes (constant vol) all strikes share one IV. In reality
IV varies by strike → **skew** (smile/smirk). [^6]

**Equity index pattern.** OTM puts >> OTM calls in IV → "negative skew" =
crash fear + downside hedging demand. Single stocks similar. Commodities/FX
vary. [^6]

**Why skew matters.**
- OTM puts more expensive than OTM calls at same distance from spot.
- Selling OTM puts in steep skew = rich premium + tail risk.
- Buying OTM puts for protection = expensive; put spreads often preferred.
- Skew can widen in stress → position value moves even with spot unchanged.

**Volatility surface.** Skew × expiry = 3D surface IV(strike, expiry).
- ATM IV term structure across expiries.
- Skew slices at key expiries (monthly, weekly).
- Calibrated by local-vol / stochastic-vol models for exotic pricing.

## 3. Margin Mechanics

**Futures.** Initial margin to open; maintenance margin as floor. MTM daily
(±intraday) — losses reduce equity; equity < maintenance = margin call. [^7]
Leverage: small % moves can wipe equity.

**Options.**
- **Long** — no margin beyond premium. Max loss = premium. [^8]
- **Short naked** — substantial margin; risk can be very large/unlimited
  (esp. naked short call). Calculated on adverse-move + vol-shift scenarios.
  [^9]
- **Multi-leg** (spreads, condors, butterflies) — get margin offsets because
  risk is defined. Bull call spread margin ≈ net debit; iron condor margin ≈
  max loss of structure.

**Portfolio margin.** Net risk across portfolio (with hedges) rather than
per-leg. Can dramatically reduce margin for hedged multi-leg books. Requires
approval + higher minimums in most jurisdictions.

**Practical.** Always know initial/maintenance margin + how far equity can
drop before margin call. Size to avoid frequent calls. Defined-risk structures
= predictable margin.

## 4. TFEX Market Structure (Thailand Futures Exchange)

**Core products.**
- **Index futures** — SET50 (S50) is the workhorse for Thai large-cap
  directional exposure and hedging.
- **Index options** — SET50 + related indices.
- **Single-stock futures (SSF)** on major SET names (single-stock options on
  selected names, when listed).
- FX, commodities per TFEX lineup.

**Structure.** Exchange-traded, centrally cleared. Day session + (for many
contracts) evening session. Local brokers, prop traders, institutions, foreign
via licensed intermediaries.

**Settlement.**
- Index contracts → mostly **cash-settled** to official index value.
- Single-stock products → physical or cash per contract specs.

**Must-check per product.** Tick size + tick value, contract multiplier,
expiry cycle (monthly / quarterly / weekly if available), margin requirements,
daily price limits, exercise style (Am/Eu) for options.

Specs change — always re-check TFEX rulebook before sizing.

## 5. Assignment and Expiration

### Expiration

Last day the option can be exercised.
- **American** — exercise any time to expiry.
- **European** — exercise only at expiry. [^10]

At expiry:
- ITM options typically auto-exercised (override possible).
- OTM options expire worthless.

### Assignment

Clearinghouse/broker randomly assigns exercise notices to short writers.
- Call writer → must **sell** underlying at strike.
- Put writer → must **buy** underlying at strike.

**Early assignment risk** (American options).
- Higher when option deep ITM.
- Higher when there's an upcoming dividend (calls).
- Higher when rates/dividends make early exercise economically attractive.
  [^10]

**Implications.** Short ITM calls near ex-div can be assigned early. Short ITM
puts assignable any time, esp. after sharp drops.

**Managing.**
- Roll or close short ITM options before ex-div.
- Be ready to take/deliver if running shorts into expiry.
- Prefer European-style index options (assignment only at expiry).

## Sources

[^1]: en.wikipedia.org — Implied volatility.
[^2]: ig.com — "What is implied volatility and how to use it".
[^3]: tastylive.com — Implied volatility concepts.
[^4]: fool.com — Implied volatility definition.
[^5]: quantt.co.uk — IV crush explained.
[^6]: sciencedirect.com — Implied volatility topic page (skew / surface).
[^7]: ampfutures.com — Educational guide to futures and options.
[^8]: cmegroup.com — Options on futures for equity traders.
[^9]: samco.in — Risk factor: futures vs options trading.
[^10]: optionseducation.org — Options basics (American/European, assignment).
