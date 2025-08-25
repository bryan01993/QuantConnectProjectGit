# region imports
from AlgorithmImports import *
from QuantConnect import Symbol
from QuantConnect.Data.Fundamental import FineFundamental
from QuantConnect.DataSource import EODHDUpcomingEarnings
from QuantConnect.Securities import *
from math import log, sqrt, exp
from scipy.stats import norm
from QuantConnect.Securities.Option import QLOptionPriceModel
from datetime import timedelta, datetime
import pandas as pd
from PropietaryCode.decorators import monitor_execution
from math import sqrt

# Global storage dictionary
OBJECT_LOG = {}
# endregion

import io
import csv
from datetime import datetime


def describe_object(obj, obj_name="unknown"):
    description = {
        "name": obj_name,
        "type": str(type(obj)),
        "attributes": {},
        "methods": []
    }

    for attr in dir(obj):
        if attr.startswith("__"):
            continue
        try:
            value = getattr(obj, attr)
            if callable(value):
                description["methods"].append(attr)
            else:
                description["attributes"][attr] = value
        except Exception as e:
            description["attributes"][attr] = f"<Error reading: {e}>"

    # Append to global OBJECT_LOG
    OBJECT_LOG[obj_name] = description


class EarningsVolatilityCrunch(QCAlgorithm):

    @monitor_execution
    def Initialize(self):
        # --- Run OnData on a daily cadence ---
        # Use daily resolution across the board so OnData fires once per trading day
        self.UniverseSettings.Resolution = Resolution.Daily
        self.UniverseSettings.FillForward = False

        # Brokerage & fee model (Interactive Brokers)
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage)

        # # Schedule OnData explicitly at market open and close
        # self.Schedule.On(self.DateRules.EveryDay(), self.TimeRules.AfterMarketOpen("SPY", 0), lambda: self.OnData(Slice()))
        # self.Schedule.On(self.DateRules.EveryDay(), self.TimeRules.BeforeMarketClose("SPY", 0), lambda: self.OnData(Slice()))

        # Dates, cash, warmup
        self.SetStartDate(*map(int, self.GetParameter("exec.start_date").split('-')))
        self.SetEndDate(*map(int, self.GetParameter("exec.end_date").split('-')))
        self.SetCash(self.GetParameter("exec.initial_amount"))
        self.SetWarmUp(10, Resolution.Daily)

        # Universes
        self.AddUniverse(self.CoarseSelectionFunction)
        self.AddUniverse(EODHDUpcomingEarnings, self.UpcomingEarningsSelectionFunction)

        # State
        self.earnings_calendar = {}  # Cache for earnings dates
        self.symbols_total = 0
        self.symbols_optionable = 0
        self.slope_results = {}
        self.volume_results = {}
        self.ivrv_results = {}
        self.added_equities = set()
        self.latest_iv_data = {}

    def PurgeOldEarningsData(self, purge_days:int = 15) -> None:
        cutoff = self.Time - timedelta(days=purge_days)
        before_count = len(self.earnings_calendar)

        # Filter earnings_calendar and log dropped keys
        new_calendar = {}
        for symbol, date in self.earnings_calendar.items():
            if date >= cutoff:
                new_calendar[symbol] = date
            else:
                # self.Debug(f"[Purge] Dropping {symbol} with earnings date {date} older than cutoff {cutoff}")
                pass
        self.earnings_calendar = new_calendar

        after_count = len(self.earnings_calendar)
        if before_count != after_count:
            self.Debug(f"[Purge] Earnings calendar reduced from {before_count} to {after_count}")

        # Clean slopes dictionary
        cleaned_slopes = {}
        if self.slope_results:
            for symbol, slopes in self.slope_results.items():
                if symbol not in self.earnings_calendar:
                    self.Debug(f"[Purge] Removing slopes for {symbol} as it is no longer in earnings_calendar")
                    continue
                valid = [s for s in slopes if s['near_contract'].ID.Date > self.Time]
                if len(valid) != len(slopes):
                    self.Debug(f"[Purge] {symbol}: removed {len(slopes) - len(valid)} expired slope entries")
                if valid:
                    cleaned_slopes[symbol] = valid
            self.slope_results = cleaned_slopes

    # @monitor_execution
    def CoarseSelectionFunction(self, coarse: List[CoarseFundamental]) -> List[Symbol]:
        lower_price = int(self.GetParameter("univ.coarse.min_price"))  # Define lower price bound
        upper_price = int(self.GetParameter("univ.coarse.max_price"))  # Define upper price bound
        return [x.Symbol for x in coarse if x.HasFundamentalData and lower_price <= x.Price <= upper_price][
               :int(self.GetParameter("univ.coarse.max_symbols"))]

    # @monitor_execution
    def UpcomingEarningsSelectionFunction(self, earnings: List[EODHDUpcomingEarnings]) -> List[Symbol]:
        selected = []
        for e in earnings:
            if e.ReportDate <= self.Time + timedelta(days=int(self.GetParameter("algo.days_before_earnings"))):
                if self.OptionChainProvider.GetOptionContractList(e.Symbol, self.Time):
                    selected.append(e.Symbol)
                    self.earnings_calendar[e.Symbol] = e.ReportDate

        total = len(earnings)
        optionable = len(selected)
        # self.Log(f"[{self.Time}] Earnings Announcements: {total}, Optionable: {optionable}")

        return selected

    # @monitor_execution
    def CheckEarningsAndTrade(self):
        for symbol, earnings_date in self.earnings_calendar.items():
            if symbol in self.Securities and self.Securities[symbol].HasData:
                iv = self.Securities[symbol].VolatilityModel.Volatility
                pass

    # @monitor_execution
    def get_two_closest_option_chains(self, symbol: Symbol, earnings_time: datetime) -> Tuple[
        List[Symbol], List[Symbol]]:
        """
        Return the *two earliest* option-expiration chains such that:
          - front_expiry  > earnings_time (strictly after earnings), and
          - back_expiry   > front_expiry (the next available after front)
        Also guarantees neither expiry is already past self.Time (no expired chains).
        """
        # Use current time for the contract list to avoid resurrecting already-expired chains
        contracts = self.OptionChainProvider.GetOptionContractList(symbol, self.Time)
        if not contracts:
            self.Debug(f"[Chains] No option contracts for {symbol} at {self.Time}")
            return [], []

        # Group contracts by expiry
        contracts_by_exp: Dict[datetime, List[Symbol]] = {}
        for c in contracts:
            contracts_by_exp.setdefault(c.ID.Date, []).append(c)

        # Minimum acceptable expiry: strictly after earnings AND not in the past vs algorithm clock
        min_expiry_date = max(earnings_time.date(), self.Time.date())

        # Collect all expiries that are strictly > min_expiry_date
        valid_expiries = sorted([exp for exp in contracts_by_exp.keys() if exp.date() > min_expiry_date])

        if not valid_expiries:
            self.Debug(
                f"[Chains] No expiries after earnings for {symbol}: earnings={earnings_time.date()}, now={self.Time.date()}")
            return [], []

        front_exp = valid_expiries[0]
        back_exp = valid_expiries[1] if len(valid_expiries) > 1 else None

        if back_exp is None:
            self.Debug(f"[Chains] Only one valid expiry for {symbol}: front={front_exp.date()} (no back expiry)")
            return contracts_by_exp.get(front_exp, []), []

        # Optional debug breadcrumb
        self.Debug(
            f"[Chains] {symbol}: earnings={earnings_time.date()} -> front={front_exp.date()}, back={back_exp.date()}")
        return contracts_by_exp.get(front_exp, []), contracts_by_exp.get(back_exp, [])

    # @monitor_execution
    def match_option_contracts_by_strike_and_type(self, near_chain: List[Symbol], next_chain: List[Symbol]) -> List[
        Tuple[Symbol, Symbol]]:
        """
        Match option contracts from two expiration chains by strike and option type (call/put).

        Parameters:
            near_chain (List[Symbol]): List of option Symbols with earlier expiration
            next_chain (List[Symbol]): List of option Symbols with later expiration

        Returns:
            List[Tuple[Symbol, Symbol]]: List of matched option contracts as (near, next)
        """
        matches = []
        next_lookup = {(c.ID.OptionRight, c.ID.StrikePrice): c for c in next_chain}

        for near_contract in near_chain:
            key = (near_contract.ID.OptionRight, near_contract.ID.StrikePrice)
            if key in next_lookup:
                matches.append((near_contract, next_lookup[key]))
        return matches

    # @monitor_execution
    def get_implied_volatilities(self, near_symbol, far_symbol):

        def compute_iv(symbol):

            if symbol.ID.Date <= self.Time:
                # self.Debug(f"[IV] Skipping {symbol.Value}, already expired")
                return None

            # contract = self.AddOptionContract(symbol, Resolution.Daily)
            history = self.History(symbol, symbol.ID.Date - timedelta(15), self.Time,
                                   Resolution.Daily)
            if history.empty:
                # self.Log(f"No history for {symbol}")
                return None

            last_row = history.iloc[-1]
            try:
                underlying_symbol = symbol.Underlying
                underlying_history = self.History([underlying_symbol], self.Time - timedelta(15), symbol.ID.Date,
                                                  Resolution.Daily)
                if underlying_history.empty:
                    # self.Log(f"No underlying history for {underlying_symbol}")
                    return None

                S = underlying_history.iloc[-1].close
                K = symbol.ID.StrikePrice
                expiry = symbol.ID.Date
                T = (expiry - last_row.name[-1]).days / 365.0
                if T <= 0:
                    # self.Log(f"Non-positive T for {symbol}")
                    return None

                price = (last_row.askclose + last_row.bidclose) / 2.0
                if price <= 0:
                    # self.Log(f"Non-positive price for {symbol}")
                    return None

                iv = self.black_scholes_call_iv(S, K, T, 0.0, price)
                # self.Log(f"Computed IV for {symbol}: {iv}")
                return iv
            except Exception as e:
                # self.Log(f"Error computing IV for {symbol}: {e}")
                return None

        near_iv = compute_iv(near_symbol)
        far_iv = compute_iv(far_symbol)

        return (near_iv, far_iv)

    @monitor_execution
    def black_scholes_call_iv(self, S, K, T, r, option_price):
        if T <= 0:
            # self.Log(f"[IV] Skipping: T <= 0 (T={T:.6f})")
            return None

        intrinsic_value = max(S - K * exp(-r * T), 0)
        if option_price <= intrinsic_value:
            # self.Log(f"[IV] Skipping: option_price <= intrinsic_value ({option_price:.4f} <= {intrinsic_value:.4f})")
            return None

        MAX_ITER = 100
        PRECISION = 1.0e-5
        sigma = 0.2

        for i in range(MAX_ITER):
            try:
                d1 = (log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * sqrt(T))
                d2 = d1 - sigma * sqrt(T)
                price = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
                vega = S * norm.pdf(d1) * sqrt(T)

                if vega < 1e-8:
                    # self.Log(f"[IV] Skipping: vega too small (vega={vega:.8f}) at iter {i}")
                    return None

                diff = price - option_price
                # self.Log(
                #     f"[IV] iter {i}: sigma={sigma:.6f}, price={price:.4f}, target={option_price:.4f}, diff={diff:.6f}")

                if abs(diff) < PRECISION:
                    # self.Log(f"[IV] Converged at iter {i} with sigma={sigma:.6f}")
                    return sigma

                sigma -= diff / vega
            except Exception as e:
                # self.Log(f"[IV] Error at iter {i}: {e}")
                return None

        # self.Log(f"[IV] Failed to converge after {MAX_ITER} iterations")
        return None

    # @monitor_execution
    def OnData(self, data: Slice):

        self.PurgeOldEarningsData(purge_days=5)

        for symbol, earnings_date in self.earnings_calendar.items():
            self.Debug(f"Looping through {symbol.Value} with earnings {earnings_date}")
            if self.Portfolio[symbol].Invested:
                self.Debug(f"symbol {symbol} already invested, skipping. Should Monitor Pos")
                continue

            front_chain, back_chain = self.get_two_closest_option_chains(symbol, earnings_time=earnings_date)
            if len(front_chain) > 1 and len(back_chain) > 1:
                self.Debug(f"here it obtained front:{front_chain[0].Value} and back:{back_chain[0].Value}")



            # symbol_slopes = self.calculate_iv_slope(self.earnings_calendar)
    #
    #         if symbol_slopes:
    #             self.Log(f"{symbol} has found a slope")
    #
    #         slope_info = max(symbol_slopes, key=lambda x: x['slope'])
    #         if slope_info['slope'] < 0.7:
    #             self.Debug(f"here it would purchase the spread for {symbol}-{self.Time}")
    #             continue
    #
    #         if symbol not in self.volume_results:
    #             continue
    #
    #         if symbol not in self.ivrv_results:
    #             continue
    #
    #         try:
    #             self.Debug(f"Placing Call Calendar for {symbol} with slope {slope_info['slope']:.2f}")
    #             # self.PlaceCallCalendar(symbol, slope_info['near_contract'], slope_info['far_contract'])
    #         except Exception as e:
    #             self.Debug(f"Failed to place order for {symbol}: {e}")
    #
    # @monitor_execution
    # def calculate_iv_slope(self, earnings_calendar: Dict[Symbol, datetime]):
    #     if not hasattr(self, "slope_cache"):
    #         self.slope_cache = {}
    #     self.Debug(f"[{self.Time}] Starting calculate_iv_slope for {len(earnings_calendar)} symbols")
    #
    #     slopes = {}
    #     max_total_contracts = 50
    #     contract_count = 0
    #
    #     for symbol, earnings_date in earnings_calendar.items():
    #         if symbol in self.slope_cache:
    #             slopes[symbol] = self.slope_cache[symbol]
    #             self.Debug(f"[Cache Hit] Skipping slope computation for {symbol}")
    #             continue
    #         # self.Debug(f"Processing symbol: {symbol.Value}")
    #         if contract_count >= max_total_contracts:
    #             break
    #         # Ensure raw data normalization to avoid exceptions
    #         if symbol in self.Securities:
    #             self.Securities[symbol].SetDataNormalizationMode(DataNormalizationMode.Raw)
    #
    #         front_chain, back_chain = self.get_two_closest_option_chains(symbol, earnings_time=earnings_date)
    #         contracts_tuples = self.match_option_contracts_by_strike_and_type(near_chain=front_chain, next_chain=back_chain)
    #
    #         if not contracts_tuples:
    #             continue
    #
    #         slopes[symbol] = []
    #         for front, back in contracts_tuples:
    #             # near_sec = self.AddOptionContract(front, Resolution.Daily)
    #             # far_sec = self.AddOptionContract(back, Resolution.Daily)
    #
    #             near_iv, far_iv = self.get_implied_volatilities(front, back)
    #
    #             diff_days = (back.ID.Date.date() - front.ID.Date.date()).days
    #             if diff_days <= 0 or near_iv is None or far_iv is None:
    #                 continue
    #
    #             slope = (near_iv - far_iv) / diff_days
    #             slopes[symbol].append({
    #                 "strike": front.ID.StrikePrice,
    #                 "near_contract": front,
    #                 "far_contract": back,
    #                 "slope": slope,
    #                 "diff_days": diff_days
    #             })
    #
    #     for symbol, entries in slopes.items():
    #         # First line: symbol and symbol.Value
    #         self.Log(f" Slopes Symbol: {symbol} | Value: {symbol.Value}")
    #
    #         # Second line(s): details for each slope entry
    #         for entry in entries:
    #             self.Log(
    #                 f"  strike {entry['strike']}; "
    #                 f"near_contract {entry['near_contract']}; "
    #                 f"far_contract {entry['far_contract']}; "
    #                 f"slope {entry['slope']}; "
    #                 f"diff_days {entry['diff_days']}"
    #             )
    #     return slopes
    #
    # # @monitor_execution
    # def filter_pre_earnings_volume(self, threshold: float = 1.20):
    #     volume_ratios = {}
    #     for symbol, earnings_date in self.earnings_calendar.items():
    #         history = self.History(symbol, 31, Resolution.Daily)
    #         if history.empty or len(history.index.get_level_values(0).unique()) < 31:
    #             continue
    #
    #         grouped = history.loc[symbol] if isinstance(history.index, pd.MultiIndex) else history
    #         recent_volume = grouped.iloc[-1].volume
    #         avg_volume = grouped.iloc[:-1].volume.mean()
    #
    #         if avg_volume > 0:
    #             ratio = recent_volume / avg_volume
    #             if ratio >= threshold:
    #                 volume_ratios[symbol] = ratio
    #
    #     return volume_ratios
    #
    # # @monitor_execution
    # def filter_iv_vs_rv(self, threshold: float = 0.8):
    #     iv_rv_ratios = {}
    #     for symbol, earnings_date in self.earnings_calendar.items():
    #         if symbol not in self.Securities or not self.Securities[symbol].HasData:
    #             continue
    #
    #         iv = self.Securities[symbol].VolatilityModel.Volatility
    #         history = self.History(symbol, 30, Resolution.Daily)
    #         if history.empty or len(history.index.get_level_values(0).unique()) < 30:
    #             continue
    #
    #         grouped = history.loc[symbol] if isinstance(history.index, pd.MultiIndex) else history
    #         returns = grouped['close'].pct_change().dropna()
    #         if returns.empty:
    #             continue
    #
    #         rv = returns.std() * sqrt(252)
    #
    #         if rv > 0:
    #             ratio = iv / rv
    #             if ratio >= threshold:
    #                 iv_rv_ratios[symbol] = ratio
    #
    #     return iv_rv_ratios
    #
    # def ComputeSlopes(self):
    #     # self.Debug(f"[{self.Time}] Starting slope calculation for {len(self.earnings_calendar)} symbols")
    #     self.slope_results = self.calculate_iv_slope(self.earnings_calendar)
    #     # self.Debug(f"[{self.Time}] Slope calculation complete. {len(self.slope_results) if self.slope_results else 0} symbols with slope data")
    #
    # def OnEndOfAlgorithm(self):
    #     # describe_object(self.Portfolio, "Portfolio")
    #     # describe_object(self.Transactions, "Transactions")
    #     describe_object(self.earnings_calendar, "earnings_calendar")
    #
    #     self.Debug(f"Total earnings symbols: {self.symbols_total}")
    #     self.Debug(f"Optionable symbols: {self.symbols_optionable}")
    #
    #     self.Debug(f"Slope Pass Count: {len(self.slope_results) if self.slope_results else 0}")
    #     self.Debug(f"Volume Pass Count: {len(self.volume_results) if self.volume_results else 0}")
    #     self.Debug(f"IV/RV Pass Count: {len(self.ivrv_results) if self.ivrv_results else 0}")
    #
    #     # Still not available for testing
    #     # self.SetRuntimeStatistic("Earnings Symbols", str(self.symbols_total))
    #     # self.SetRuntimeStatistic("Optionable Symbols", str(self.symbols_optionable))
    #     # self.SetRuntimeStatistic("Slope Filtered", str(len(self.slope_results) if self.slope_results else 0))
    #     # self.SetRuntimeStatistic("Volume Filtered", str(len(self.volume_results) if self.volume_results else 0))
    #     # self.SetRuntimeStatistic("IV/RV Filtered", str(len(self.ivrv_results) if self.ivrv_results else 0))
    #     import json
    #
    #     if OBJECT_LOG:
    #         for name, info in OBJECT_LOG.items():
    #             object_summary = {
    #                 "type": info["type"],
    #                 "attributes": list(info["attributes"].keys()),
    #                 "methods": info["methods"]
    #             }
    #             # Store each object in its own runtime key
    #             key = f"Object {name}"
    #             value = json.dumps(object_summary)[:5000]  # Truncate just in case
    #             self.SetRuntimeStatistic(key, value)
