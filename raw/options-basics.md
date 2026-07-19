---
title: Options — Basics
type: source
tags: [options, derivatives]
---

# Options — Basics

Options are standardized contracts that give the buyer the **right** (but not the
obligation) to buy or sell an underlying asset at a fixed price before or on a
set date; the seller has the **obligation** to fulfill that right if the buyer
exercises.

## 1. What an option is

- **Underlying**: stock, index, ETF, future, commodity, etc.
- **Contract size**: for equity options, 1 contract usually = **100 shares** of
  the underlying.
- **Expiration**: last day the option can be exercised (for many equity options,
  the **3rd Friday** of the month; many products also have weekly expiries).
- **Style**:
  - **American**: can be exercised any time up to expiration (most equity options).
  - **European**: can be exercised only at expiration (many index options).

## 2. Calls vs. Puts

### Call option
- Gives the holder the **right to buy** the underlying at the **strike price**
  before/at expiration.
- Buyer: expects price to go **up**.
- Seller (writer): obligated to **sell** if assigned; collects premium, takes on risk.

### Put option
- Gives the holder the **right to sell** the underlying at the **strike price**
  before/at expiration.
- Buyer: expects price to go **down** or wants protection.
- Seller: obligated to **buy** if assigned; collects premium, takes on risk.

## 3. Key terms you must know

- **Strike price**: fixed price at which the underlying can be bought (call) or
  sold (put) if the option is exercised.
- **Premium**: price of the option, quoted per share; total cost = premium × 100
  shares (for standard equity options).
  - Example: premium = ฿3.50 → contract cost = ฿350.
- **Moneyness**:
  - **In-the-money (ITM)**:
    - Call: spot > strike
    - Put: spot < strike
  - **At-the-money (ATM)**: strike ≈ spot
  - **Out-of-the-money (OTM)**:
    - Call: spot < strike
    - Put: spot > strike
- **Intrinsic vs extrinsic value**:
  - **Intrinsic**: immediate exercise value (e.g., call with spot 200, strike 180
    → intrinsic = 20).
  - **Extrinsic (time value)**: premium − intrinsic; reflects time, volatility,
    rates, etc.

## 4. Basic payoff ideas

### Long call (buy a call)
- Max loss: **premium paid**.
- Profit if underlying rises well above strike + premium.
- Limited downside, theoretically unlimited upside.

### Short call (sell a call)
- Max gain: **premium received**.
- Loss if underlying rises sharply; for naked calls, loss can be very large.

### Long put (buy a put)
- Max loss: **premium paid**.
- Profit if underlying falls below strike − premium.

### Short put (sell a put)
- Max gain: **premium received**.
- Loss if underlying falls sharply; you may be forced to buy at strike.

These four basic positions are the building blocks for all more complex strategies.

## 5. Why people use options

Common objectives:

- **Speculation**: take a directional view with limited capital (e.g., long call
  instead of buying stock).
- **Hedging**: protect an existing position (e.g., own stock + buy put as
  "insurance").
- **Income**: sell options (e.g., covered calls, cash-secured puts) to collect
  premium.
- **Leverage**: control more exposure with less cash than buying the underlying
  outright.

## 6. Simple numerical example (long call)

Assume:
- Stock price: 170
- Buy 1 call, strike 170, 1 month to expiry
- Premium: 3.50 per share → total cost = 3.50 × 100 = **350**

At expiry:
- If stock = 180:
  - Intrinsic = 180 − 170 = 10 per share
  - Option value = 10 × 100 = 1,000
  - Profit = 1,000 − 350 = **650** (ignoring fees)
- If stock = 165:
  - Option expires worthless
  - Loss = **350** (the premium)

This shows limited loss (premium) and leveraged upside.

## 7. Risks you must respect

- Options can expire **worthless**; you can lose 100% of the premium quickly.
- **Time decay (theta)** works against long options; every day that passes tends
  to reduce extrinsic value.
- **Volatility changes** can dramatically affect option prices even if the
  underlying doesn't move much.
- Short options can have **large or undefined losses**; they require margin and
  strict risk control.

Regulators require brokers to give you an options risk disclosure (e.g., OCC's
"Characteristics and Risks of Standardized Options") before you trade.

## 8. Minimal study checklist

To be solid on basics, make sure you can:

1. Explain in your own words:
   - What a call and a put are
   - Rights vs obligations of buyer and seller
2. Define: strike, premium, expiration, ITM/ATM/OTM, intrinsic vs extrinsic.
3. Draw simple payoff diagrams for:
   - Long call, short call, long put, short put
4. Compute:
   - Break-even for long call: strike + premium
   - Break-even for long put: strike − premium
5. Describe at least one use case each for:
   - Speculation, hedging, income.

## Sources

[^1]: `raw/options-basics.md` (this file).
[^2]: investopedia.com — options basics tutorial. https://www.investopedia.com/options-basics-tutorial-4583012
[^3]: optionseducation.org — options basics. https://www.optionseducation.org/optionsoverview/options-basics
[^4]: optionsplaybook.com — options introduction. https://www.optionsplaybook.com/options-introduction/options-basics
[^5]: youtube.com/watch?v=3vnexB9QmHI — long-call payoff example.
[^6]: youtube.com/watch?v=6zBylFzpKaU — options risks (OCC disclosure).