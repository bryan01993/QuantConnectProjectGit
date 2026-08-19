# Earnings Volatility Crunch (EVC) Option Strategy

This document details the architecture, design, pseudocode, implementation tasks, and test cases for the **Earnings Volatility Crunch (EVC)** option strategy, migrated and optimized under the folder `6_EarningsVolatilityCrunch`.

---

## 1. Strategy Mechanics

The strategy is designed to exploit the **Implied Volatility (IV) Crush** that occurs immediately following a scheduled earnings announcement.

```mermaid
graph TD
    A[Upcoming Earnings Announcement] --> B[High Uncertainty / High Option Demand]
    B --> C[Implied Volatility (IV) Inflates]
    C --> D[Enter Long Calendar Spread: Sell Front Call, Buy Back Call]
    D --> E[Earnings Release / Uncertainty Resolved]
    E --> F[IV Collapses - IV Crush]
    F --> G[Front Call Value Drops Rapidly / Back Call Value Drops Slower]
    G --> H[Exit Spread for Profit]
```

### Position Details: Long Calendar Spread
*   **Front Leg (Near-Expiry Call)**: Sell at-the-money (ATM) or near-ATM call option expiring shortly *after* the earnings date. Because this contract captures the bulk of the earnings uncertainty, its IV is highly elevated. Selling this leg allows us to capture the sharpest drop in IV.
*   **Back Leg (Far-Expiry Call)**: Buy a call option with the same strike price but expiring further in the future. Because its expiration is distant, its IV is less affected by the immediate earnings event, providing a hedge against adverse price movements while maintaining a net-short Vega exposure.
*   **Net Position**: Net debit (or small credit depending on pricing), net-short Vega, net-positive Theta (time decay), and relatively neutral Delta (near the strike price).

### Position Duplication & Single-Ticker Controls
To prevent over-exposure, maintain capital limits, and avoid redundant transactions as time passes, the strategy implements strict checks to avoid duplicating trades:
*   **Duplicate Prevention**: If a position in the calendar spread already exists for a ticker, no new entries are analyzed or executed for that ticker.
*   **Single-Ticker Exclusivity**: The algorithm guarantees that only a single option calendar spread (one near leg, one far leg) is active per ticker. It is prohibited to invest in different strikes, rights, or other contract pairs simultaneously for the same underlying ticker.
*   **Safety Guards**: The check scans active tracking structures, the active portfolio option holdings, the pending execution queue, and open brokerage orders.

### Parameter Tracking & Mapability
To enable detailed post-trade analysis, parameter optimization, and Kelly sizing calibration, every trade must be mapable to the key parameters (IV slope, Volume ratio, IV/RV ratio) at the moment of opening:
*   **Active Spreads State**: The active positions state tracker caches the initial parameters (`slope`, `vol_ratio`, `ivrv_ratio`) alongside the entry price and quantity.
*   **Closed Trade Performance History**: Upon liquidation of a position, a performance dictionary containing the final realized PnL percentage, the opening parameters, and the exit timestamp is appended to the localized history DB (`self.trade_history`).
*   **Order Leg Tagging**: Each Combo Order leg is tagged with a JSON string containing the underlying symbol, leg side, strike, expirations, slope, volume ratio, IV/RV ratio, and opening timestamp.

---

## 2. Configuration Parameters

The strategy utilizes the following configuration parameters, defined in `config.json`:

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `exec.initial_amount` | Float | `10,000,000` | Initial capital for backtesting. |
| `exec.start_date` | String | `2023-01-05` | Start date of backtest (`YYYY-MM-DD`). |
| `exec.end_date` | String | `2023-12-10` | End date of backtest (`YYYY-MM-DD`). |
| `univ.coarse.dollar_volume` | Integer | `1,000,000` | Minimum dollar volume for coarse selection. |
| `univ.coarse.min_price` | Integer | `30` | Minimum price for underlying stocks. |
| `univ.coarse.max_price` | Integer | `500` | Maximum price for underlying stocks. |
| `univ.coarse.max_symbols` | Integer | `5000` | Maximum symbols to return from coarse universe. |
| `algo.days_before_earnings` | Integer | `5` | Scan window for upcoming earnings (enter `N` days before). |
| `algo.days_after_earnings` | Integer | `2` | Exit window (liquidate positions `M` days after earnings). |
| `algo.slope_threshold` | Float | `0.01` | Minimum IV slope `(near_iv - far_iv) / diff_days` to trigger trade. |
| `algo.option.upper_filter` | Integer | `2` | Maximum strikes above ATM to include (+2 strikes). |
| `algo.option.lower_filter` | Integer | `-2` | Minimum strikes below ATM to include (-2 strikes). |
| `algo.option.max_exp_days` | Integer | `45` | Maximum days to expiration for back contract. |
| `algo.option.min_exp_days` | Integer | `5` | Minimum days to expiration for front contract. |
| `risk.max_loss_pct` | Float | `1.5` | Stop-loss percentage relative to portfolio value. |
| `risk.kelly.factor` | Float | `0.35` | Kelly Criterion scaling factor. |
| `risk.kelly.period` | Integer | `30` | Lookback period in days for Kelly ratio calculations. |

---

## 3. Core Algorithm Pseudocode

The following pseudocode outlines the implementation structure for `6_EarningsVolatilityCrunch/main.py`.

### 3.1 Main Algorithm Class
```python
class EarningsVolatilityCrunch(QCAlgorithm):
    # Initialize state variables
    earnings_calendar = {}          # Cache for upcoming earnings: {Symbol: report_date}
    symbol_states = {}              # Active tracking states: {Symbol: SymbolState}
    pending_option_orders = []      # Queue for option orders waiting for execution
    active_spreads = {}             # Tracked calendar spreads: {underlying_symbol: SpreadPosition}
    
    def Initialize(self):
        # 1. Setup execution dates, initial capital, and daily resolution
        self.SetStartDate(GetParameter("exec.start_date"))
        self.SetEndDate(GetParameter("exec.end_date"))
        self.SetCash(GetParameter("exec.initial_amount"))
        self.UniverseSettings.Resolution = Resolution.Hour # Hour resolution for intra-day data
        self.UniverseSettings.FillForward = True
        self.UniverseSettings.DataNormalizationMode = DataNormalizationMode.Raw
        
        # 2. Brokerage setup
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage)
        
        # 3. Register Universes
        self.AddUniverse(self.CoarseSelectionFunction)
        self.AddUniverse(EODHDUpcomingEarnings, self.UpcomingEarningsSelectionFunction)
        
        # 4. Schedule final liquidation anchor
        self.RegisterFinalLiquidation(anchor_ticker="SPY", minutes_before_close=120)
        
    def OnData(self, slice_data: Slice):
        # 1. Skip if warming up
        if self.IsWarmingUp:
            return
            
        # 2. Manage and monitor current open positions (exits & stop-losses)
        self.ManageOpenPositions(slice_data)
        
        # 3. Process any pending orders that now have market prices
        self.ProcessPendingOrders(slice_data)
        
        # 4. Purge old calendar cache entries
        self.PurgeExpiredEarnings(purge_days=5)
        
        # 5. Core Signal & Entry Loop
        for underlying in self.earnings_calendar.keys():
            # Skip if we already own this underlying or its options
            if self.IsAlreadyInvested(underlying):
                continue
                
            # Filter and pair options for this underlying
            eligible_pairs = self.GetOptionPairs(underlying, self.earnings_calendar[underlying])
            if not eligible_pairs:
                continue
                
            # Evaluate pairs and calculate metrics
            best_pair = None
            best_metrics = None
            
            for front_contract, back_contract in eligible_pairs:
                metrics = self.CalculateMetrics(underlying, front_contract, back_contract)
                if metrics is None:
                    continue
                    
                # Strict Threshold Filters
                if metrics["slope"] < self.GetParameter("algo.slope_threshold"):
                    continue
                if metrics["vol_ratio"] < 1.0: # Volume must be at least average
                    continue
                if metrics["ivrv_ratio"] < 1.0: # Implied Vol must exceed Realized Vol
                    continue
                    
                # Identify best pair based on highest IV slope
                if best_pair is None or metrics["slope"] > best_metrics["slope"]:
                    best_pair = (front_contract, back_contract)
                    best_metrics = metrics
            
            # If a valid pair passes all filters, size and execute
            if best_pair is not None:
                quantity = self.DeterminePositionSize(underlying, best_metrics)
                if quantity > 0:
                    self.ExecuteCalendarSpread(underlying, best_pair[0], best_pair[1], quantity, best_metrics)

    def IsAlreadyInvested(self, underlying: Symbol) -> bool:
        # Check 1: Check active spread tracker
        if underlying in self.active_spreads:
            return True
            
        # Check 2: Check current portfolio holdings
        # Ensure no active option contract under this underlying is currently invested
        for symbol in self.Portfolio.Keys:
            if symbol.SecurityType == SecurityType.Option and symbol.Underlying == underlying:
                if self.Portfolio[symbol].Invested:
                    return True
                    
        # Check 3: Check pending order queue
        # Ensure we don't have any option orders pending execution for this underlying
        for contract, _, _ in self.pending_option_orders:
            if contract.Underlying == underlying:
                return True
                
        # Check 4: Check working orders in broker queue
        open_orders = self.Transactions.GetOpenOrders()
        for order in open_orders:
            if order.Symbol.SecurityType == SecurityType.Option and order.Symbol.Underlying == underlying:
                return True
                
        return False
```

### 3.2 Helper Calculations

#### Implied Volatility Solver (Newton-Raphson)
```python
def ComputeImpliedVolatility(option_right, S, K, T, r, market_price):
    # Black-Scholes Formula helper
    def BS_Price(sigma):
        d1 = (ln(S/K) + (r + 0.5 * sigma^2)*T) / (sigma * sqrt(T))
        d2 = d1 - sigma * sqrt(T)
        if option_right == Call:
            return S * N(d1) - K * exp(-r*T) * N(d2)
        else:
            return K * exp(-r*T) * N(-d2) - S * N(-d1)
            
    # Vega calculation helper
    def Vega(sigma):
        d1 = (ln(S/K) + (r + 0.5 * sigma^2)*T) / (sigma * sqrt(T))
        return S * n(d1) * sqrt(T)
        
    # Newton-Raphson loop
    sigma = 0.25  # initial guess
    for i in range(100):
        price = BS_Price(sigma)
        vega = Vega(sigma)
        if vega < 1e-8:
            return None
        diff = price - market_price
        if abs(diff) < 1e-5:
            return sigma
        sigma -= diff / vega
        if sigma <= 0 or sigma > 6.0:
            return None
    return None
```

#### Metrics Calculation (Slope, Vol Ratio, IV/RV)
```python
def CalculateMetrics(self, underlying, front_contract, back_contract):
    # 1. Fetch Option closing prices
    front_price = self.GetOptionMidPrice(front_contract)
    back_price = self.GetOptionMidPrice(back_contract)
    underlying_price = self.Securities[underlying].Price
    
    if not front_price or not back_price or not underlying_price:
        return None
        
    # 2. Time to Expiration (Years)
    T_front = (front_contract.Expiry - self.Time) / 365.0
    T_back = (back_contract.Expiry - self.Time) / 365.0
    
    # 3. Calculate IVs
    front_iv = ComputeImpliedVolatility(Call, underlying_price, front_contract.Strike, T_front, 0.0, front_price)
    back_iv = ComputeImpliedVolatility(Call, underlying_price, back_contract.Strike, T_back, 0.0, back_price)
    
    if not front_iv or not back_iv:
        return None
        
    # 4. Calculate IV Slope
    diff_days = (back_contract.Expiry - front_contract.Expiry).days
    slope = (front_iv - back_iv) / diff_days
    
    # 5. Calculate Volume Ratio
    history = self.History(underlying, 35, Resolution.Daily)
    recent_volume = history.Last.Volume
    avg_prev_volume = history.Slice(0, 30).Average(Volume)
    vol_ratio = recent_volume / avg_prev_volume
    
    # 6. Calculate Realized Volatility (RV) and IV/RV Ratio
    returns = history.Slice(0, 30).PercentChanges()
    rv = StandardDeviation(returns) * sqrt(252) # Annualized
    ivrv_ratio = front_iv / rv
    
    return {
        "slope": slope,
        "near_iv": front_iv,
        "far_iv": back_iv,
        "vol_ratio": vol_ratio,
        "ivrv_ratio": ivrv_ratio,
        "strike": front_contract.Strike
    }
```

### 3.3 Position Sizing (Kelly Criterion)
```python
def DeterminePositionSize(self, underlying: Symbol, metrics: Dict[str, Any]) -> int:
    # Load Kelly parameters
    kelly_factor: float = self.GetParameter("risk.kelly.factor")
    kelly_period: int = self.GetParameter("risk.kelly.period")
    
    history: List[Dict[str, Any]] = self.trade_history[underlying]
    
    if len(history) < 5:
        # Default fallback if not enough history: conservative fractional sizing
        kelly_fraction = 0.10
    else:
        wins: int = sum(1 for x in history if x["pnl"] > 0)
        losses: int = sum(1 for x in history if x["pnl"] <= 0)
        total_trades: int = len(history)
        win_rate: float = wins / total_trades
        
        avg_win: float = np.mean([x["pnl"] for x in history if x["pnl"] > 0]) if wins > 0 else 0.0
        avg_loss: float = abs(np.mean([x["pnl"] for x in history if x["pnl"] <= 0])) if losses > 0 else 1.0
        win_loss_ratio: float = avg_win / avg_loss if avg_loss > 0 else 1.0
        
        # Kelly Formula: f* = p - (1-p)/b
        kelly_fraction = win_rate - (1 - win_rate) / win_loss_ratio
        
    # Clamp Kelly fraction
    kelly_fraction = max(0.0, min(kelly_fraction, 1.0)) * kelly_factor
    
    # Capital allocation
    portfolio_value: float = self.Portfolio.TotalPortfolioValue
    allocation_capital: float = portfolio_value * kelly_fraction
    
    # Estimate cost of one spread contract (buy far, sell near)
    spread_cost: float = abs(metrics["back_price"] - metrics["front_price"]) * 100.0
    
    # Safe checks
    if spread_cost <= 0:
        return 0
        
    quantity: int = int(math.floor(allocation_capital / spread_cost))
    return quantity
```

### 3.4 Position Management & Exits
```python
def ManageOpenPositions(self, slice_data: Slice) -> None:
    days_after: int = self.GetParameter("algo.days_after_earnings")
    max_loss_pct: float = self.GetParameter("risk.max_loss_pct")
    liquidated_keys: List[Symbol] = []
    
    for symbol, position in self.active_spreads.items():
        # Check 1: Time-Based Exit (Target Vol Crush realization)
        report_date: datetime = position["report_date"]
        if self.Time.date() >= (report_date + timedelta(days=days_after)).date():
            self.LiquidateSpread(symbol, tag="Target Time-Based Exit (Post-Earnings IV Crush)")
            liquidated_keys.append(symbol)
            continue
            
        # Check 2: Stop Loss (Risk Management)
        front_price: float = self.GetOptionMidPrice(position["front"])
        back_price: float = self.GetOptionMidPrice(position["back"])
        if front_price > 0 and back_price > 0:
            current_cost: float = abs(back_price - front_price)
            unrealized_loss: float = (position["entry_price"] - current_cost) * position["qty"] * 100.0
            unrealized_loss_pct: float = (unrealized_loss / self.Portfolio.TotalPortfolioValue) * 100.0
            
            if unrealized_loss_pct >= max_loss_pct:
                self.LiquidateSpread(symbol, tag=f"Stop Loss Triggered ({unrealized_loss_pct:.2f}% Loss)")
                liquidated_keys.append(symbol)
                continue
            
        # Check 3: Expiry Exits (DTE <= 1 fallback for ITM/ATM)
        for leg_name in ["front", "back"]:
            leg: Symbol = position[leg_name]
            dte: int = (leg.ID.Date.date() - self.Time.date()).days
            if dte <= 1:
                underlying_price: float = self.Securities[symbol].Price
                is_atm_or_itm: bool = underlying_price >= leg.ID.StrikePrice if leg.ID.OptionRight == Call else underlying_price <= leg.ID.StrikePrice
                if is_atm_or_itm:
                    self.LiquidateSpread(symbol, tag=f"Leg DTE={dte} Expiry Exit")
                    liquidated_keys.append(symbol)
                    break
                    
    for k in liquidated_keys:
        self.active_spreads.pop(k, None)

def LiquidateSpread(self, underlying: Symbol, tag: str) -> None:
    position: Dict[str, Any] = self.active_spreads[underlying]
    front: Symbol = position["front"]
    back: Symbol = position["back"]
    qty: int = position["qty"]
    
    # Opposite execution
    legs = [Leg.Create(front, 1), Leg.Create(back, -1)]
    self.ComboMarketOrder(legs, qty, tag=f"CLOSE:{tag}")
    
    # Map realized trade performance directly to opening parameters
    front_price: float = self.GetOptionMidPrice(front)
    back_price: float = self.GetOptionMidPrice(back)
    if front_price > 0 and back_price > 0:
        exit_price: float = abs(back_price - front_price)
        pnl_pct: float = (exit_price - position["entry_price"]) / position["entry_price"]
        self.trade_history[underlying].append({
            "pnl": pnl_pct,
            "entry_slope": position["slope"],
            "entry_vol_ratio": position["vol_ratio"],
            "entry_ivrv_ratio": position["ivrv_ratio"],
            "exit_time": self.Time.isoformat()
        })
```

---

## 4. Implementation Roadmap (Tasks)

The following checklist guides the complete migration and implementation of the strategy into `6_EarningsVolatilityCrunch/main.py`.

- [ ] **Task 1: Project Setup & Config Migration**
  - [ ] Create folder `6_EarningsVolatilityCrunch` in the root workspace.
  - [ ] Create `6_EarningsVolatilityCrunch/config.json` with correct parameter files.
  - [ ] Create boilerplate `main.py` referencing `QuantConnect` libraries.
- [ ] **Task 2: Define Universe Selection**
  - [ ] Implement `CoarseSelectionFunction` filtering by price range and dollar volume.
  - [ ] Implement `UpcomingEarningsSelectionFunction` reading from `EODHDUpcomingEarnings`.
  - [ ] Setup underlying daily/hourly data feeds and enforce raw data mode.
- [ ] **Task 3: Options Retrieval and Pairing**
  - [ ] Create call options filter: Expirations > earnings, ATM to ATM+2 strikes.
  - [ ] Create option pairing function matching consecutive expirations (Front vs. Back leg).
- [ ] **Task 4: Metrics Calculations**
  - [ ] Implement Black-Scholes option pricing model.
  - [ ] Implement Newton-Raphson solver for Implied Volatilities of near and far legs.
  - [ ] Implement volume ratio history provider.
  - [ ] Implement annualized realized volatility calculator.
- [ ] **Task 5: Trade Selection and Sizing**
  - [ ] Implement strict threshold checks for `slope`, `vol_ratio`, and `ivrv_ratio`.
  - [ ] Implement `IsAlreadyInvested` check to query active_spreads, portfolio holdings, pending queues, and working open orders to ensure no duplicate trades or multiple spreads are active for the same ticker.
  - [ ] Implement best-pair selector per underlying.
  - [ ] Implement Kelly Criterion calculation utilizing past wins/losses and average risk rewards.
  - [ ] Implement execution mechanics (ComboMarketOrder) and custom JSON log tagging.
- [ ] **Task 6: Position Tracking & Exits**
  - [ ] Implement time-based post-earnings exit (`algo.days_after_earnings`).
  - [ ] Implement DTE-based options fallback manager (`DTE <= 1`).
  - [ ] Implement stop-loss logic (`risk.max_loss_pct`).
  - [ ] Implement final algorithm liquidation scheduler (120 minutes before final close).
- [ ] **Task 7: Code Validation**
  - [ ] Add explicit type annotations across all classes and helpers.
  - [ ] Compile file syntax locally using `poetry run python compile_agent.py`.

---

## 5. Verification & Testing Plan

To verify that the code functions correctly and avoids regressions, the following testing framework will be implemented.

### 5.1 Unit Tests (Mathematical & Helper Functions)
We will create a test suite (e.g., in a local test script or notebooks) to validate options pricing and solvers.

1.  **Black-Scholes Model Validation**:
    *   *Test*: Pass known parameters (S=100, K=100, T=0.25, r=0.0, sigma=0.20) for a Call option.
    *   *Expected Output*: Price = $3.98.
2.  **Newton-Raphson IV Solver Validation**:
    *   *Test*: Pass S=100, K=100, T=0.25, r=0.0, Price=$3.98.
    *   *Expected Output*: Implied Volatility = 20.0% (0.20).
3.  **Volume Ratio Validation**:
    *   *Test*: Mock a history DataFrame where the last day volume is 1,200,000 and the previous 30-day average is 1,000,000.
    *   *Expected Output*: Volume Ratio = 1.20.
4.  **Realized Volatility Validation**:
    *   *Test*: Mock return series with constant daily standard deviation (e.g., 1%).
    *   *Expected Output*: Annualized RV = 15.87% (0.01 * sqrt(252)).

### 5.2 Integration Tests (Backtest Scenarios)
Once code is written, we will run backtests via the local CLI compiler to verify system flows:

1.  **Upcoming Earnings Trigger Test**:
    *   *Scenario*: Target stock has earnings on day `X`. Verify that the algorithm adds the stock to `earnings_calendar` on day `X - 5` (as per `algo.days_before_earnings`).
2.  **Order Execution and Tagging Test**:
    *   *Scenario*: Trigger a calendar spread trade. Verify that:
        *   A `ComboMarketOrder` is submitted.
        *   Leg 1 (Short) is tagged with JSON containing metrics (`"leg":"SHORT"`).
        *   Leg 2 (Long) is tagged with JSON containing metrics (`"leg":"LONG"`).
3.  **Post-Earnings Exit Test**:
    *   *Scenario*: Stock reports earnings. Verify that the algorithm submits a market order to close both legs exactly on day `EarningsDate + 2` (as per `algo.days_after_earnings`).
4.  **Stop-Loss Exit Test**:
    *   *Scenario*: Mock a large drop in option value exceeding `risk.max_loss_pct`. Verify that the position is closed immediately before expiration.
5.  **Final Day Liquidation Test**:
    *   *Scenario*: Backtest reaches end date. Verify that 120 minutes before market close on the last day, all assets are flattened and no active positions remain.
6.  **Position Duplication & Single-Ticker Control Test**:
    *   *Scenario*: Underlying ticker has an active calendar spread. The algorithm scans upcoming earnings and finds another pair passing all filters.
    *   *Expected Output*: The algorithm skips the entry because `IsAlreadyInvested` returns `True`.
    *   *Scenario*: Underlying ticker has a pending order in the queue or a working order at the brokerage.
    *   *Expected Output*: The algorithm skips new entry processing to avoid duplicate fills.
    *   *Scenario*: Active options exist for a ticker but at a different strike.
    *   *Expected Output*: The algorithm returns `True` for `IsAlreadyInvested` and skips entering different contracts for the same ticker.
