# Earnings Volatility Crunch (`4EVC`) - Strategy Documentation & Overview

This directory contains the strategy code, configuration, research notebooks, and logic documentation for the **Earnings Volatility Crunch (4EVC)** option strategy ([`main.py`](file:///c:/Users/bryan/QuantConnectProjectGit/4_EarningsVolatilityCrunch/main.py)).

- **Full Execution Logic Flowchart & Detailed Architecture Document**: [`4EVC_Logic.md`](file:///c:/Users/bryan/QuantConnectProjectGit/4_EarningsVolatilityCrunch/4EVC_Logic.md)
- **Interactive Research & BigQuery Audit Notebook**: [`research.ipynb`](file:///c:/Users/bryan/QuantConnectProjectGit/4_EarningsVolatilityCrunch/research.ipynb)

---

## Part 1: Strategy Overview & Core Mechanics

The **Earnings Volatility Crunch (4EVC)** strategy exploits the structural **Implied Volatility (IV) Crush** that occurs immediately after a company reports quarterly earnings. Pre-earnings uncertainty expands option implied volatility to peak levels. Post-announcement, this uncertainty collapses rapidly within the first 60 minutes of market trading.

To capture this IV collapse while hedging against underlying price moves, the algorithm enters **Long Calendar Spreads** on call options:

* **Short Leg (Near Expiry)**: Sold ATM call option expiring shortly *after* the earnings date. This contract suffers the maximum IV crush and time decay ($\Theta$).
* **Long Leg (Far Expiry)**: Bought call option at the exact same strike price with a later expiration date ($\ge 45$ days gap). This contract acts as a price hedge and retains far-term Vega.
* **Net Position Profile**: Net debit entry, positive Theta ($\Theta$), short net Vega ($\nu$), and near-delta-neutral ($\Delta$) at entry.

---

## Part 2: Strategy Configuration & Parameter Matrix

All strategy parameters are loaded dynamically from `AlgoConfig.yaml` via QuantConnect's `GetParameter()` framework:

| Parameter Key                     | Default Value         | Description                                                                                         |
| :-------------------------------- | :-------------------- | :-------------------------------------------------------------------------------------------------- |
| `exec.initial_amount`           | `$100,000,000.0`    | Initial backtest portfolio cash balance                                                             |
| `univ.coarse.max_symbols`       | `1000`              | Maximum liquid stocks selected from Coarse Fundamental universe                                     |
| `univ.coarse.min_price`         | `$15.00`            | Minimum equity stock price                                                                          |
| `univ.coarse.max_price`         | `$500.00`           | Maximum equity stock price                                                                          |
| `univ.coarse.dollar_volume`     | `$500,000`          | Minimum daily dollar volume requirement                                                             |
| `algo.min_days_before_earnings` | `1`                 | Min days prior to BMO earnings date for entry scan                                                  |
| `algo.days_before_earnings`     | `3`                 | Max days prior to earnings date for entry scan                                                      |
| `algo.days_after_earnings`      | `0`                 | Days post-earnings to hold position before Time Exit                                                |
| `algo.entry_hour`               | `14` (2:00 PM EST)  | Afternoon window start hour for trade entry scan                                                    |
| `algo.exit_hour`                | `10` (10:00 AM EST) | Post-market open hour for Time Exit execution                                                       |
| `algo.slope_threshold`          | `0.001`             | Minimum required IV term structure slope$(\sigma_{\text{near}} - \sigma_{\text{far}}) / \Delta t$ |
| `algo.volume_threshold`         | `1.00`              | Minimum required volume ratio ($\text{Volume}_{\text{recent}} / \text{Volume}_{\text{30d avg}}$)  |
| `algo.ivrv_threshold`           | `1.00`              | Minimum required near-IV to 30-day realized volatility ratio ($\sigma_{\text{near}} / RV$)        |
| `algo.min_iv_ratio`             | `1.15`              | Minimum ratio of Near IV to Far IV ($\sigma_{\text{near}} / \sigma_{\text{far}}$)                 |
| `algo.max_spread_threshold`     | `$2.00`             | Maximum combined bid-ask spread threshold across option legs                                        |
| `risk.max_loss_pct`             | `70.0%`             | Stop-loss percentage on trade debit cost                                                            |
| `risk.itm_safety_pct`           | `1.5%`              | ITM safety guard: flattens spread if short leg goes$\ge 1.5\%$ ITM                                |
| `risk.kelly.factor`             | `0.35`              | Fractional Kelly sizing multiplier                                                                  |
| `risk.max_combo_contracts`      | `10`                | Hard cap on maximum combo spread contracts per trade                                                |
| `algo.is_hdbt`                  | `false`             | Heavy Duty Backtest toggle (`true` forces `pass_all=True`, `max_symbols=1000`)                |

---

## Part 3: Algorithmic Execution Pipeline & Safety Liquidators

### 1. Daily Universe Selection

* **Coarse Fundamental Universe**: Selects top 1,000 liquid equities by dollar volume ($\ge \$500\text{k}/day$, price $\$15-\$500$).
* **Upcoming Earnings Selection**: Scans `EODHDUpcomingEarnings` announcements matching active coarse tickers within 1–3 days.

### 2. Pre-Execution Safety Liquidators (`OnData` Slice)

* **Equity Assignment Liquidator**: Flattens any stock holdings caused by option assignment.
* **Synchronous Pair Expiry Liquidator**: Liquidates calendar pairs if any leg reaches $\text{DTE} \le 1$.
* **Orphaned Leg Sweeper**: Liquidates any unhedged single option leg not tracked in `active_spreads`.

### 3. Open Position Management (`ManageOpenPositions`)

* **Time-Based Exit**: Exits post-earnings at 10:00 AM EST (1 hour after open).
* **Stop-Loss Guard**: Liquidates if unrealized trade loss $\ge 70\%$.
* **Pre-Assignment ITM Safety Guard**: Liquidates if stock price moves $\ge 1.5\%$ ITM past short strike.

### 4. 3-Tier Short-Circuit Entry Filtering

* **Tier 1 (Stock Level)**: Volume Ratio $\ge 1.0$ ($\text{Volume}_{\text{recent}} / \text{Volume}_{30\text{d}}$).
* **Tier 2 (Near Option)**: Solve Near IV using Newton-Raphson BSM; verify $\text{IV/RV} \ge 1.0$.
* **Tier 3 (Far Option & Pair)**: Solve Far IV; verify Slope $\ge 0.001$, Near/Far IV Ratio $\ge 1.15$, Combined Spread $\le \$2.00$.

### 5. Candidate Ranking & Kelly Position Sizing

* **Ranking Score**: $\text{Score} = \frac{\text{Slope}}{1 + 10 \times \text{StrikeDist}_{\%}}$.
* **Kelly Sizing**: Computes win-rate & win-loss ratio from trade history, applies $0.35 \times \text{Kelly}$, caps allocation at $\$1,000$ and max 10 combo contracts.

---

## Part 4: BigQuery Integration & Data Warehouse Schema

All trade execution events emit structured JSON records tagged with `[BIGQUERY_TRADE_RECORD]`:

```json
{
  "pk": "EVC_20260809_163852_AAPL_1",
  "backtest_run_id": "EVC_20260809_163852_76cbbc56",
  "algo_code": "4EVC",
  "timestamp": "2020-01-28T19:00:00Z",
  "underlying": "AAPL",
  "action": "OPEN",
  "qty": 10,
  "strike": 320.0,
  "near_expiry": "2020-02-07",
  "far_expiry": "2020-03-20",
  "earnings_date": "2020-01-28",
  "vol_ratio": 1.4521,
  "slope": 0.01235,
  "ivrv_ratio": 1.3412,
  "entry_price": 1.45,
  "exit_price": 0.0,
  "pnl": 0.0,
  "exit_reason": "",
  "parameters": "{\"vol_ratio\":1.4521,\"slope\":0.01235,\"ivrv_ratio\":1.3412,\"comb_spread\":0.15,\"exit_reason\":\"\"}"
}
```

These records are streamed directly into Google BigQuery table `bav-personal-cloud.develop.BTOPTrades`.

---

## Part 5: Critical Research & Adversarial Audit Questions

Operating under the **Prejudicial Skepticism Model (Zero-Edge Default Hypothesis)**:

1. **Call vs. Put vs. Double Calendars**: Why trade Call calendars exclusively? How does the algorithm perform during severe downside earnings gaps ($-10\%$ to $-20\%$)?
2. **Pre-Earnings Skew Difference**: Does evaluating Call IV vs. Put IV skew prior to entry improve directional expected returns?
3. **Entry Window Timing (2:00 PM vs. 3:45 PM EST)**: Does entering 2 hours before market close introduce unnecessary delta drift compared to entering in the final 15 minutes?
4. **Post-Earnings Exit Timing**: Is 10:00 AM EST optimal compared to 9:31 AM EST (market open) or 3:55 PM EST (end of post-earnings day)?
5. **Macro VIX Filtering**: Should entries be suppressed when broad market VIX $> 30$ when post-earnings IV crush is muted?
