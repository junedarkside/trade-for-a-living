---
title: Put-Call Parity
type: source
tags: [options, derivatives]
---

# Put-Call Parity

**Put-Call Parity** is a fundamental **no-arbitrage relationship** that links
European call and put prices (same strike, expiry, underlying) to spot and the
risk-free rate. Two portfolios with identical payoffs must have the same price —
otherwise risk-free arbitrage exists. [^1]

## Core idea

Two portfolios with **identical expiry payoff**:

1. **Protective put** — long underlying + long put.
2. **Synthetic long via options** — long call + risk-free bond with face value
   equal to strike.

Same payoff in every future state → same price today (ignoring frictions). If
not, arbitrage. [^2]

## Formula (European, no dividends)

```
C + PV(K) = P + S
```

Where:
- `C` = European call price (strike K, expiry T)
- `P` = European put price (same K, T)
- `S` = current spot
- `PV(K) = K × e^(-rT)` (continuous compounding) or `K / (1+r)^T` (discrete)
  [^3]

Rearranged:
```
C − P = S − PV(K)
```

Synthetic identities:
- **Synthetic long stock**: `C − P ≈ S − PV(K)`
- **Synthetic long call**: `C = P + S − PV(K)`
- **Synthetic long put**: `P = C + PV(K) − S`

## Economic interpretation

> Long call + cash (PV of strike) ≈ long put + stock.

Both deliver at expiry:
- If `S_T > K`: stock worth `S_T`.
- If `S_T < K`: cash `K`.

Identical payoffs → parity equation. [^4]

## Dividends / carry adjustment

With PV of dividends `PV(D)` during option life:

```
C + PV(K) = P + S − PV(D)
C − P = S − PV(K) − PV(D)
```

Continuous dividend yield `q`:

```
C − P = S × e^(-qT) − K × e^(-rT)
```

Used for index options where the underlying pays continuous yield. [^5]

## European vs American

- **European** — parity is an **equality** (mod dividends, rates). [^1]
- **American** — parity is an **inequality** because of early exercise:
  ```
  S − K ≤ C − P ≤ S − PV(K)
  ```
  Deep ITM Americans may deviate (early exercise value, esp. around
  dividends). [^2]

## Arbitrage when parity violated

If `C + PV(K) < P + S`:

1. **Buy** cheap: long call + bond (`PV(K)`).
2. **Sell** rich: short put + short stock.

Combined payoff identical → lock in upfront profit. Reverse if inequality
flips. [^6]

Real markets: rare on liquid instruments, exploited fast, often below retail
costs.

## Synthetic positions

| Structure | Replicates |
|-----------|------------|
| Long call + short put (same K, T) | Long stock/forward |
| Short call + long put | Short stock/forward |
| Long put + long stock − bond | Long call |
| Long call − long stock + bond | Long put |

Used when: underlying restricted/expensive, options-only mandate, complex
structures, book hedging. [^6]

## Practical trader uses

- **Price check** — if call "too cheap" vs put, parity flags mispricing.
- **Structure choice** — long stock + put vs long call + bond?
- **Conversions/reversals** — market-maker tool to capture tiny mispricings:
  - **Conversion**: long put + short call + long stock ≈ bond.
  - **Reversal**: short put + long call + short stock ≈ short bond.
- **Implied forward** — back out market-implied forward from `C − P`. Compare
  to futures / your view.

## Relation to Greeks, IV, futures

- **Greeks**: `Δ_call − Δ_put = 1` (non-dividend) — parity-consistent.
- **IV / skew**: large parity deviations = illiquidity / data issue, not
  tradeable arb.
- **Options on futures**: parity uses forward/future price, not spot.

## Sources

[^1]: en.wikipedia.org — Put-call parity.
[^2]: macroption.com — Put-call parity formula.
[^3]: youtube.com — Put-call parity derivation (continuous vs discrete).
[^4]: tastylive.com — Put-call parity concepts.
[^5]: it.wikipedia.org — Put-call parity (continuous dividend yield version).
[^6]: optionalpha.com — Put-call parity and arbitrage.
[^7]: optionseducation.org — Put-call parity advanced concepts.
