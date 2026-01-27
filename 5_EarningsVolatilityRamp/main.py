# region imports
from AlgorithmImports import *
from QuantConnect.DataSource import EODHDUpcomingEarnings
from typing import List, Set, Optional
import math
import numpy as np
# endregion

class EarningsVolatilityRamp(QCAlgorithm):

    def initialize(self):
        # Locally Lean installs free sample data, to download more data please visit https://www.quantconnect.com/docs/v2/lean-cli/datasets/downloading-data
        self.set_start_date(2010, 1, 1) 
        self.set_end_date(2026, 1, 1)
        self.set_cash(1000000000000) 
        
        # Ensure resolution is DAILY as requested
        self.universe_settings.resolution = Resolution.DAILY
        
        # Parameters for Earnings Window
        self.earnings_window_min = 14
        self.earnings_window_max = 22
        
        # Parameters for Ambient Volatility Calculation
        self.ambient_min_days_before = 1
        self.ambient_max_days_before = 5
        
        # State to store liquid symbols for intersection
        self.liquid_symbols: Set[Symbol] = set()
        
        # Dictionary to store earnings dates
        self.earnings_calendar = {}
        
        # Unique Trade ID counter
        self.trade_count = 0

        # 2. Create a universe of liquid stocks (Coarse Selection)
        self.add_universe(self.coarse_universe_selection)

        # 1. Obtain all the stocks that are going to have earnings in the next 14-22 days
        self.add_universe(EODHDUpcomingEarnings, self.earnings_universe_selection)
        
        self.add_equity("SPY", Resolution.DAILY)

    # region Universe Selection

    def coarse_universe_selection(self, coarse: List[CoarseFundamental]) -> List[Symbol]:
        """
        Selects liquid stocks with:
        - Price > $10
        - Dollar Volume > $10,000,000 (Proxy for liquidity/healthy)
        - Has Fundamental Data
        """
        # Define thresholds
        min_price = 10
        min_dollar_volume = 10_000_000
        
        # Filter coarse universe
        selected = [
            x.Symbol for x in coarse 
            if x.has_fundamental_data 
            and x.price > min_price 
            and x.dollar_volume > min_dollar_volume
        ]
        
        # Update the liquid symbols set for use in earnings selection
        self.liquid_symbols = set(selected)
        
        # Return selected symbols to keep them in the universe/feed
        return selected

    def earnings_universe_selection(self, data: List[EODHDUpcomingEarnings]) -> List[Symbol]:
        """
        Selects stocks with earnings reports scheduled within the target window (next 14-22 days).
        Inner-joins with the 'liquid_symbols' set identified by Coarse Selection.
        Checks for Option capability.
        """
        selected_symbols = []
        
        # Calculate target date range
        target_start = self.time.date() + timedelta(days=self.earnings_window_min)
        target_end = self.time.date() + timedelta(days=self.earnings_window_max)
        
        for earnings in data:
            symbol = earnings.symbol
            
            # Intersection Check: Must be in the liquid symbols list
            if not self.liquid_symbols or symbol not in self.liquid_symbols:
                continue

            if earnings.report_date:
                report_date = earnings.report_date.date()
                if target_start <= report_date <= target_end:
                    
                    # Ensure the stock has options
                    if self.option_chain_provider.get_option_contract_list(symbol, self.time):
                        selected_symbols.append(symbol)
                        self.earnings_calendar[symbol] = report_date
                        
                        # Note: The requirement "20k average daily option volume" is hard to filter 
                        # directly here without premium total option volume data or history on options.
                        # We rely on High Dollar Volume + Has Options as a strong proxy for now.
                    
        return selected_symbols

    def on_data(self, data: Slice):
        """
        Primary entry point for the algorithm. Executes the strategy:
        1. Identifies tickers 14 days from earnings.
        2. Calculates Ambient Vol, Event Vol, and Implied Move.
        3. Enters an ATM Straddle with a unique ID and tags metrics.
        4. Exits positions 1 day before earnings.
        """
        current_date = self.time.date()
        
        # Process symbols in the earnings calendar
        for symbol, earnings_date in list(self.earnings_calendar.items()):
            # Days to earnings
            days_to_earnings = (earnings_date - current_date).days
            
            # --- EXIT LOGIC: 1 day before earnings ---
            if days_to_earnings == 1:
                self.liquidate_ticker_and_options(symbol, "Exiting day before earnings")
                continue

            # --- ENTRY LOGIC: 14 days before earnings ---
            if days_to_earnings == 14:
                # 1. Skip if already invested in this ticker's complex (Equity or Options)
                if self.is_invested_in_ticker(symbol):
                    continue
                
                # 2. Get Option Chain for calculations and entry
                chain = data.OptionChains.get(symbol)
                if chain is None or not any(chain):
                    # Option data might be missing in this slice; request it for next time if possible
                    # In Daily resolution, we rely on the subscription from on_securities_changed
                    continue
                
                # 3. Calculate Strategy Metrics
                v_ambient = self.calculate_ambient_volatility(symbol, earnings_date, chain)
                if v_ambient is None:
                    continue
                    
                v_event = self.calculate_event_volatility(symbol, earnings_date, chain, v_ambient)
                if v_event is None:
                    continue
                
                # Note: calculate_implied_move currently returns % move as per latest user edit
                v_move_pct = self.calculate_implied_move(v_event, chain.underlying.price)
                
                # 4. Find Target Expiry (First expiry after earnings)
                expiries = sorted(list(set(c.expiry.date() for c in chain if c.expiry.date() > earnings_date)))
                if not expiries:
                    continue
                target_expiry = expiries[0]
                
                # 5. Select ATM Straddle Contracts
                underlying_price = chain.underlying.price
                contracts_at_expiry = [c for c in chain if c.expiry.date() == target_expiry]
                
                # Find closest strike
                atm_strike = min(contracts_at_expiry, key=lambda x: abs(x.strike - underlying_price)).strike
                
                call = [c for c in contracts_at_expiry if c.right == OptionRight.CALL and c.strike == atm_strike]
                put = [c for c in contracts_at_expiry if c.right == OptionRight.PUT and c.strike == atm_strike]
                
                if call and put:
                    self.trade_count += 1
                    trade_id = f"TRADE_{self.trade_count}_{symbol.value}"
                    
                    # Create tag with all metrics for the order ticket record
                    tag = f"ID:{trade_id} | AmbVol:{v_ambient:.4f} | EvVol:{v_event:.4f} | ImpMove:{v_move_pct:.4f}"
                    
                    # Entry: 1 unit of straddle (Equal quantity for Call and Put)
                    # We can use set_holdings or order by quantity. 
                    self.market_order(call[0].symbol, 1, tag=tag)
                    self.market_order(put[0].symbol, 1, tag=tag)
                    
                    self.debug(f"[{current_date}] Entered Straddle for {symbol.value}: {tag}")

        # Basic portfolio allocation (e.g. SPY) if desired, but prioritize option liquidity
        if not self.portfolio.invested and "SPY" in data:
            self.set_holdings("SPY", 0.01) # Reduced focus on SPY to keep room for straddles

    def on_securities_changed(self, changes: SecurityChanges):
        """
        Handles subscriptions for options when an equity enters the earnings universe.
        """
        for security in changes.added_securities:
            symbol = security.symbol
            # Automatically add options for universe equities to ensure we get chains in on_data
            if symbol.security_type == SecurityType.EQUITY and symbol.value != "SPY":
                option = self.add_option(symbol)
                # Filter for ATM and near-term expirations covering the 14-22 day window
                option.set_filter(-3, 3, timedelta(days=0), timedelta(days=60))

    def is_invested_in_ticker(self, symbol: Symbol) -> bool:
        """Helper to check if we have any position in the underlying or its options."""
        if self.portfolio[symbol].invested:
            return True
        return any(p.invested and p.symbol.security_type == SecurityType.OPTION and p.symbol.underlying == symbol 
                   for p in self.portfolio.values())

    def liquidate_ticker_and_options(self, symbol: Symbol, message: str = ""):
        """Helper to liquidate all positions related to an underlying."""
        if self.portfolio[symbol].invested:
            self.liquidate(symbol, message)
        
        for p in self.portfolio.values():
            if p.invested and p.symbol.security_type == SecurityType.OPTION and p.symbol.underlying == symbol:
                self.liquidate(p.symbol, message)


            
    # region Value Calculation Helper Functions
    
    def calculate_days_to_earnings_on_open(self, symbol: Symbol, earnings_date: date) -> int:
        """
        Calculates the number of days from current time to the earnings release.
        Maps to: v_days_to_earnings_on_open
        """
        v_days_to_earnings_on_open = (earnings_date - self.time.date()).days
        return v_days_to_earnings_on_open

    def calculate_ambient_volatility(self, symbol: Symbol, earnings_date: date, chain: OptionChain) -> Optional[float]:
        """
        Calculates the background/ambient volatility (excluding earnings event volatility).
        Method 1: Implied volatility of an ATM contract expiring 3-5 days BEFORE earnings.
        Method 2: Forward volatility of the first two expirations AFTER earnings (to cancel out the event).
        
        :param symbol: The underlying Symbol
        :param earnings_date: The expected date of the earnings report
        :param chain: The option chain for the symbol
        :return: Annualized ambient volatility or None
        """
        if chain is None or not any(chain):
            self.log(f"No option chain data for {symbol} to calculate ambient volatility")
            return None
            
        # Extract unique expiries and sort them
        expiries = sorted(list(set(contract.expiry.date() for contract in chain)))
        
        # Method 1: Preferred - Expiry prior to earnings
        # Look for an expiry that is at least X days before and at most Y days before
        target_expiries_before = [
            d for d in expiries 
            if self.ambient_min_days_before <= (earnings_date - d).days <= self.ambient_max_days_before
        ]
        
        if target_expiries_before:
            target_expiry = target_expiries_before[-1] # Take the one closest to earnings in the range
            iv = self._get_atm_iv(chain, target_expiry)
            if iv is not None:
                return iv
            
        # Method 2: Proxy - Forward volatility of two expiries AFTER earnings
        # This extracts the non-event volatility by differencing two expiries that both contain the event.
        # Formula: sigma_ambient = sqrt( (sigma2^2 * T2 - sigma1^2 * T1) / (T2 - T1) )
        after_expiries = [d for d in expiries if d > earnings_date]
        if len(after_expiries) >= 2:
            t1_date = after_expiries[0]
            t2_date = after_expiries[1]
            
            iv1 = self._get_atm_iv(chain, t1_date)
            iv2 = self._get_atm_iv(chain, t2_date)
            
            if iv1 is not None and iv2 is not None:
                # Use total days from today to expiry for T calculation (annualized)
                days1 = (t1_date - self.time.date()).days
                days2 = (t2_date - self.time.date()).days
                
                # Ensure we have a valid time difference
                if days2 > days1 > 0:
                    t1 = days1 / 365.0
                    t2 = days2 / 365.0
                    
                    # Calculate forward variance
                    fwd_var = (iv2**2 * t2 - iv1**2 * t1) / (t2 - t1)
                    if fwd_var > 0:
                        return math.sqrt(fwd_var)
        
        self.debug(f"Could not calculate ambient volatility for {symbol} using preferred or proxy methods.")
        return None

    def _get_atm_iv(self, chain: OptionChain, expiry: date) -> Optional[float]:
        """
        Helper to get the Implied Volatility of the ATM contract for a given expiry.
        ATM is defined as the contract with the strike closest to the underlying price.
        """
        contracts = [c for c in chain if c.expiry.date() == expiry]
        if not contracts:
            return None
            
        underlying_price = chain.underlying.price
        if underlying_price <= 0:
            return None
            
        # Find ATM contract (closest strike to underlying price)
        # We look at both calls and puts; typically they should have similar IV for ATM
        atm_contract = min(contracts, key=lambda x: abs(x.strike - underlying_price))
        
        # QuantConnect usually populates implied_volatility if initialized correctly
        iv = atm_contract.implied_volatility
        return float(iv) if iv is not None and iv > 0 else None

    def calculate_event_volatility(self, symbol: Symbol, earnings_date: date, chain: OptionChain, v_ambient_volatility: float) -> Optional[float]:
        """
        Calculates the implied volatility specifically for the earnings event.
        Formula: Sev = sqrt(S_total**2 * T - S_ambient**2 * (T-1))
        Where S_total is the IV of the first expiry after earnings, and T is days to expiry.
        
        :param symbol: The underlying Symbol
        :param earnings_date: The expected date of the earnings report
        :param chain: The option chain for the symbol
        :param v_ambient_volatility: The background volatility (annualized)
        :return: Annualized-equivalent event volatility or None
        """
        if chain is None or not any(chain) or v_ambient_volatility is None:
            return None
            
        # Find the first expiry AFTER the earnings date (the one containing the event premium)
        expiries = sorted(list(set(contract.expiry.date() for contract in chain)))
        after_expiries = [d for d in expiries if d > earnings_date]
        
        if not after_expiries:
            self.debug(f"No expiries after earnings date {earnings_date} found for {symbol}")
            return None
            
        target_expiry = after_expiries[0]
        v_total_volatility = self._get_atm_iv(chain, target_expiry)
        
        if v_total_volatility is None:
            return None
            
        # Days to expiry (T)
        t_days = (target_expiry - self.time.date()).days
        if t_days <= 0:
            return None
            
        # Solve for Sigma event: Sev = sqrt(Stotal**2 * T - Sambient**2 * (T-1))
        # This isolatest the variance contribution of the event day.
        try:
            event_variance_scaled = (v_total_volatility**2 * t_days) - (v_ambient_volatility**2 * (t_days - 1))
            # Handle potential negative results due to data noise or if ambient > total
            v_event_volatility = math.sqrt(max(0, event_variance_scaled))
            return v_event_volatility
        except Exception as e:
            self.error(f"Error calculating event volatility for {symbol}: {str(e)}")
            return None

    def calculate_implied_move(self, event_volatility: float, price: float) -> float:
        """
        Calculates the expected absolute move implied by the event volatility.
        Formula: Implied_absolute_move = Sevent * Root(1/365) * Root(2/pi) * Price
        Maps to: v_implied_move
        """
        if not event_volatility or not price:
            return 0.0
            
        # Sev * sqrt(1/365) converts annualized event vol to single-day event vol
        # sqrt(2/pi) converts standard deviation to expected absolute move (approx 0.8)
        v_implied_move = event_volatility * math.sqrt(1.0 / 365.0) * math.sqrt(2.0 / math.pi)
        return v_implied_move

    def calculate_previous_implied_move(self, symbol: Symbol) -> Optional[float]:
        """
        Retrieves the implied move calculated for the PREVIOUS earnings event.
        Requires storage/history of past analysis.
        Maps to: v_previous_implied_move
        """
        # Placeholder: Retrieve from self.ObjectStore or internal history cache
        v_previous_implied_move = None
        return v_previous_implied_move

    def calculate_last_realized_move(self, symbol: Symbol) -> Optional[float]:
        """
        Calculates the actual realized % move of the stock during the last earnings event.
        Maps to: v_last_realized_move
        """
        # Logic: Find last earnings date -> Get close before and open/close after -> Calc % diff
        v_last_realized_move = None
        return v_last_realized_move

    def calculate_avg_implied_move(self, symbol: Symbol) -> Optional[float]:
        """
        Calculates the average of implied moves over the last N earnings cycles.
        Maps to: v_avg_implied_move
        """
        # Logic: Average of historical v_implied_move values
        v_avg_implied_move = None
        return v_avg_implied_move

    # endregion

#TO-DO:
#1. Obtain all the stocks that are going to have earnings in the next 14-22 days
#2. Create a universe of liquid stocks with at least 20k average daily option volume at entry, inner-join with the previous list
#3. Calculate the following metrics for each stock/option?:
    #3.1  v_ambient_volatility -> taken TESTING
    #3.2  v_event_volatility -> taken   TESTING
    #3.3  v_implied_move -> calculated from 3.2 TESTING
    #3.4  v_previous_implied_move (if none then null) -> taken from 3.2 TODO
    #3.5  r_implied_last_implied_move -> 3.3 / 3.4 TODO
    #3.6  v_last_realized_move -> unknown??? TODO
    #3.7  gap_implied_last_realized_move -> unknown??? TODO
    #3.8  v_avg_implied_move -> average of 3.3 TODO
    #3.9  r_implied_last_implied_move -> 3.8 / 3.3 TODO
    #3.10 gap_implied_avg_realized -> 3.3 / avg(3.6) TODO
    #3.11 v_days_to_earnings_on_open -> taken TODO
    
#4. Open a straddle on each of the stocks that exist in point 2. but attaching in the ticket a single ID and all the attributes from point 3.
#5. Monitor to close the position the day before the earnings announcement.
#6. 
