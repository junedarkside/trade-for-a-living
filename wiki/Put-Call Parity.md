---
title: Put-Call Parity
type: concept
status: learning
tags: [options, derivatives, market/thailand]
aliases: [PCP, Put Call Parity]
---

# Put-Call Parity

**Put-Call Parity** is the fundamental **no-arbitrage relationship** that links
European call and put prices (same strike, expiry, underlying) to spot and the
risk-free rate. Two portfolios with identical expiry payoffs must cost the same
today — otherwise risk-free arbitrage exists.

This is the **pricing backbone** behind every synthetic, every conversion /
reversal, and every cross-check between related option strikes.

## Core formula (European, non-dividend)

```
C + PV(K) = P + S
```

| Variable | Meaning |
|----------|---------|
| `C` | European call price (strike K, expiry T) |
| `P` | European put price (same K, T) |
| `S` | spot price of underlying |
| `PV(K)` | `K × e^(-rT)` (continuous) or `K / (1+r)^T` (discrete) |

Rearranged:
```
C − P = S − PV(K)
```

> **Interpretation:** long call + cash (PV of strike) is **economically
> equivalent** to long put + underlying. Same payoff in every state → same
> price today (mod frictions).

## Why it matters

1. **Pricing backbone** — every synthetic relationship derives from this.
2. **Cross-check** — if a call looks "too cheap" vs the put at the same
   strike/expiry, parity tells you the size of the mispricing.
3. **Implied forward** — back out the market's forward from
   `C − P = F − PV(K)`. Compare to actual futures / your view.
4. **Conversions / reversals** — market-maker trades that capture tiny
   mispricings without directional exposure.

## With dividends / carry

When underlying pays known dividends `PV(D)` or continuous yield `q`:

```
C + PV(K) = P + S − PV(D)
C − P = S × e^(-qT) − K × e^(-rT)
```

Index options (e.g., SET50) typically use the continuous-yield version
because SET50 dividends are paid throughout the year.

## Synthetic positions

| Construct | Legs | Replicates |
|-----------|------|------------|
| **Synthetic long stock** | Long call + short put (same K, T) | Long stock / long forward |
| **Synthetic short stock** | Short call + long put | Short stock / short forward |
| **Synthetic long call** | Long put + long stock − bond | Long call |
| **Synthetic long put** | Long call − long stock + bond | Long put |

These show up throughout the vault:
- [[Synthetic Futures]] = long call + short put (or vice versa) at same strike
  / expiry ≈ long/short future.
- [[Risk Reversal]] = long OTM call + short OTM put (or reverse) — a skewed
  synthetic forward.
- [[Collar]] = long stock + long put + short OTM call — bond-like from
  parity's perspective.
- [[Protective Put]] = long stock + long put — the classic "parity stock leg".

## Worked example — SET50 (European, continuous dividend yield)

- SET50 spot `S = 25,500`.
- Strike `K = 25,500` (ATM), `T = 30/365` years.
- Risk-free rate `r = 2.0%` (Thai policy rate proxy).
- Continuous dividend yield `q ≈ 2.5%` (SET50 historical average).
- 30-day ATM call mid = **฿95** / contract (multiplier ฿200 → underlying price
  ≈ 95/200 = **฿47.5 / index point**).
- 30-day ATM put mid = **฿42** / contract → **฿21 / index point**.

Parity check:
```
PV(K) = 25500 × e^(-0.02 × 30/365) ≈ 25,458
S × e^(-qT) = 25500 × e^(-0.025 × 30/365) ≈ 25,448

C − P (index points) = 47.5 − 21 = 26.5
S × e^(-qT) − K × e^(-rT) ≈ 25,448 − 25,458 ≈ −10 (per index point)
```

Hmm — this would imply arb. **Reality check:** the ATM call/put **mid** rarely
shows parity cleanly because bid-ask, dividends-timing mismatch, and IV
differences across strikes (skew) all move the prices. Use **synthetic-forward
construction** instead:

```
Synthetic forward = C − P (same K, T)
                   = 47.5 − 21 = +26.5 index points (i.e., forward > spot)
```

That means **synthetic long via call-spread-and-short-put** is ฿26.5 × 200 =
**฿5,300** richer than spot — i.e., the options market implies a contango of
roughly 26.5 / 25,500 ≈ **0.10% over 30 days** (annualised ≈ **1.2%**). Check
vs actual S50 futures curve: if front-month is at 25,520 vs spot 25,500, the
contango is ~0.08% — synthetic and futures are within friction. **No arb.**

If the gap widens materially (> transaction costs), box-spread arbitrage opens.

## Arbitrage when violated

```
if (C + PV(K)) < (P + S):
    buy cheap side  = long call + bond
    sell rich side  = short put + short stock
    # locked-in risk-free profit
```

Liquid markets: these opportunities close in seconds. Retail traders rarely
capture them after costs.

## European vs American parity

| Style | Parity form | Reason |
|-------|-------------|--------|
| **European** (e.g., TFEX S50 options) | Strict equality (mod div, rates) | No early exercise |
| **American** | Inequality `S − K ≤ C − P ≤ S − PV(K)` | Early exercise value (esp. deep ITM near div) |

For Thai S50 options (European), parity is **equality** — cleaner arb math.
For SET-listed equity options (American), use the inequality bounds.

## Relation to Greeks

Parity implies:
```
Δ_call − Δ_put = e^(-qT) ≈ 1 (non-dividend)
```

So delta of a synthetic long stock (long call + short put) ≈ 1 — same as
stock. Confirms the synthetic replicates the underlying's risk profile.

## Related

- [[Synthetic Futures]] · [[Risk Reversal]] · [[Collar]] · [[Protective Put]]
  · [[Black Model]] · [[Implied Volatility]] · [[IV Skew, Smile & Surface]] ·
  [[Delta]] · [[Gamma]] · [[Delta-Neutral Hedging]] · [[Options Chain]] ·
  [[Futures — Basics]]

## Sources

[^1]: `raw/put-call-parity.md`
[^2]: en.wikipedia.org — Put-call parity.
[^3]: macroption.com — Put-call parity formula.
[^4]: tastylive.com — Put-call parity concepts.
[^5]: optionalpha.com — Put-call parity and arbitrage.
[^6]: optionseducation.org — Put-call parity advanced concepts.
[^7]: it.wikipedia.org — Put-call parity (continuous dividend yield).
