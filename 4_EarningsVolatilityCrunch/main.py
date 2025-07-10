# region imports
from AlgorithmImports import *
from QuantConnect import Symbol
from QuantConnect.Data.Fundamental import FineFundamental
from QuantConnect.DataSource import EODHDUpcomingEarnings
from QuantConnect.Securities import *

from QuantConnect.Securities.Option import QLOptionPriceModel
from datetime import timedelta, datetime
import pandas as pd
from PropietaryCode.decorators import monitor_execution
from math import sqrt

# Global storage dictionary
OBJECT_LOG = {}
# endregion

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
        self.Schedule.On(self.DateRules.EveryDay(), self.TimeRules.Every(timedelta(hours=1)), self.ComputeSlopes)
        self.SetStartDate(*map(int, self.GetParameter("exec.start_date").split('-')))
        self.SetEndDate(*map(int, self.GetParameter("exec.end_date").split('-')))
        self.SetCash(self.GetParameter("exec.initial_amount"))
        self.SetWarmUp(10, Resolution.Daily)

        self.UniverseSettings.Resolution = Resolution.Hour
        self.AddUniverse(self.CoarseSelectionFunction)
        self.AddUniverse(EODHDUpcomingEarnings, self.UpcomingEarningsSelectionFunction)
        self.earnings_calendar = {}  # Cache for earnings dates

        self.symbols_total = 0
        self.symbols_optionable = 0
        self.slope_results = {}
        self.volume_results = {}
        self.ivrv_results = {}
        self.added_equities = set()

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
        self.Log(f"[{self.Time}] Earnings Announcements: {total}, Optionable: {optionable}")

        return selected

    # @monitor_execution
    def CheckEarningsAndTrade(self):
        for symbol, earnings_date in self.earnings_calendar.items():
            if symbol in self.Securities and self.Securities[symbol].HasData:
                iv = self.Securities[symbol].VolatilityModel.Volatility
                pass

    @monitor_execution
    def get_two_closest_option_chains(self, symbol: Symbol, earnings_time: datetime) -> Tuple[
        List[Symbol], List[Symbol]]:
        """
        Get the option chains for the closest expiration before `earnings_time`, and the closest on or after it.

        Parameters:
            qc (QCAlgorithm or QuantBook): Algorithm instance with OptionChainProvider
            symbol (Symbol): The underlying asset symbol (equity)
            earnings_time (datetime): The earnings date to compare against

        Returns:
            Tuple[List[Symbol], List[Symbol]]: (near_exp_chain_before_earnings, far_exp_chain_on_or_after_earnings)
        """
        lookback_time = earnings_time - timedelta(days=30)
        frontlook_time = earnings_time + timedelta(days=30)
        contracts = self.OptionChainProvider.GetOptionContractList(symbol, lookback_time)
        if not contracts:
            return [], []

        # Group by expiration date
        contracts_by_exp = {}
        for c in contracts:
            exp = c.ID.Date
            contracts_by_exp.setdefault(exp, []).append(c)

        # Filter and sort
        before = [exp for exp in contracts_by_exp if earnings_time > exp >= lookback_time]
        after_or_equal = [exp for exp in contracts_by_exp if earnings_time <= exp < frontlook_time]

        near = sorted(before)[-1] if before else None
        far = sorted(after_or_equal)[0] if after_or_equal else None

        return contracts_by_exp.get(near, []), contracts_by_exp.get(far, [])

    @monitor_execution
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


    @monitor_execution
    def get_implied_volatilities(self, near_symbol: Symbol, far_symbol: Symbol) -> Tuple[float, float]:
        """
        Safely extract the implied volatilities from two option contracts with error handling.

        Parameters:
            qc (QCAlgorithm): The algorithm context
            near_symbol (Symbol): Near-term option contract symbol
            far_symbol (Symbol): Far-term option contract symbol

        Returns:
            Tuple[float, float]: (near_iv, far_iv) or (None, None) if any error occurs
        """
        self.Securities[near_symbol.Symbol].PriceModel = OptionPriceModels.CrankNicolsonFD()
        self.Securities[far_symbol.Symbol].PriceModel = OptionPriceModels.CrankNicolsonFD()

        try:
            front_iv = self.Securities[near_symbol.Symbol].PriceModel.Volatility
        except Exception as e:
            self.Debug(f"[Error] Fetching IV for near contract {near_symbol.Value}: {e}")
            front_iv = None

        try:
            back_iv = self.Securities[far_symbol.Symbol].VolatilityModel.Volatility
        except Exception as e:
            self.Debug(f"[Error] Fetching IV for far contract {far_symbol.Value}: {e}")
            back_iv = None

        return front_iv, back_iv

    @monitor_execution
    def OnData(self, data: Slice):
        for symbol in self.earnings_calendar:
            if self.Portfolio[symbol].Invested:
                continue

            symbol_slopes = self.slope_results.get(symbol, [])
            if not symbol_slopes:
                self.Debug(f"No slopes found for {symbol}")
                continue

            slope_info = max(symbol_slopes, key=lambda x: x['slope'])
            if slope_info['slope'] < 0.7:
                continue

            if symbol not in self.volume_results:
                continue

            if symbol not in self.ivrv_results:
                continue

            try:
                self.Log(f"Placing Call Calendar for {symbol} with slope {slope_info['slope']:.2f}")
                # self.PlaceCallCalendar(symbol, slope_info['near_contract'], slope_info['far_contract'])
            except Exception as e:
                self.Log(f"Failed to place order for {symbol}: {e}")

    @monitor_execution
    def calculate_iv_slope(self, earnings_calendar: Dict[Symbol, datetime]):
        if not hasattr(self, "slope_cache"):
            self.slope_cache = {}
        self.Debug(f"[{self.Time}] Starting calculate_iv_slope for {len(earnings_calendar)} symbols")

        slopes = {}
        max_total_contracts = 50
        contract_count = 0

        for symbol, earnings_date in earnings_calendar.items():
            if symbol in self.slope_cache:
                slopes[symbol] = self.slope_cache[symbol]
                self.Debug(f"[Cache Hit] Skipping slope computation for {symbol}")
                continue
            self.Debug(f"Processing symbol: {symbol.Value}")
            if contract_count >= max_total_contracts:
                break
            # Ensure raw data normalization to avoid exceptions
            if symbol in self.Securities:
                self.Securities[symbol].SetDataNormalizationMode(DataNormalizationMode.Raw)

            front_chain, back_chain = self.get_two_closest_option_chains(symbol, earnings_time=earnings_date)
            contracts_tuples = self.match_option_contracts_by_strike_and_type(near_chain=front_chain, next_chain=back_chain)

            if not contracts_tuples:
                continue

            slopes[symbol] = []
            for front, back in contracts_tuples:
                near_sec = self.AddOptionContract(front, Resolution.Daily)
                far_sec = self.AddOptionContract(back, Resolution.Daily)

                near_iv, far_iv = self.get_implied_volatilities(near_sec, far_sec)

                diff_days = (back.ID.Date.date() - front.ID.Date.date()).days
                if diff_days <= 0 or near_iv is None or far_iv is None:
                    continue

                slope = (far_iv - near_iv) / diff_days
                slopes[symbol].append({
                    "strike": front.ID.StrikePrice,
                    "near_contract": front,
                    "far_contract": back,
                    "slope": slope
                })

        return slopes

    @monitor_execution
    def filter_pre_earnings_volume(self, threshold: float = 1.20):
        volume_ratios = {}
        for symbol, earnings_date in self.earnings_calendar.items():
            history = self.History(symbol, 31, Resolution.Daily)
            if history.empty or len(history.index.get_level_values(0).unique()) < 31:
                continue

            grouped = history.loc[symbol] if isinstance(history.index, pd.MultiIndex) else history
            recent_volume = grouped.iloc[-1].volume
            avg_volume = grouped.iloc[:-1].volume.mean()

            if avg_volume > 0:
                ratio = recent_volume / avg_volume
                if ratio >= threshold:
                    volume_ratios[symbol] = ratio

        return volume_ratios

    @monitor_execution
    def filter_iv_vs_rv(self, threshold: float = 0.8):
        iv_rv_ratios = {}
        for symbol, earnings_date in self.earnings_calendar.items():
            if symbol not in self.Securities or not self.Securities[symbol].HasData:
                continue

            iv = self.Securities[symbol].VolatilityModel.Volatility
            history = self.History(symbol, 30, Resolution.Daily)
            if history.empty or len(history.index.get_level_values(0).unique()) < 30:
                continue

            grouped = history.loc[symbol] if isinstance(history.index, pd.MultiIndex) else history
            returns = grouped['close'].pct_change().dropna()
            if returns.empty:
                continue

            rv = returns.std() * sqrt(252)

            if rv > 0:
                ratio = iv / rv
                if ratio >= threshold:
                    iv_rv_ratios[symbol] = ratio

        return iv_rv_ratios

    def ComputeSlopes(self):
        self.Debug(f"[{self.Time}] Starting slope calculation for {len(self.earnings_calendar)} symbols")
        self.slope_results = self.calculate_iv_slope(self.earnings_calendar)
        self.Debug(f"[{self.Time}] Slope calculation complete. {len(self.slope_results) if self.slope_results else 0} symbols with slope data")


    def OnEndOfAlgorithm(self):
        describe_object(self.Portfolio, "Portfolio")
        describe_object(self.Transactions, "Transactions")

        self.Debug(f"Total earnings symbols: {self.symbols_total}")
        self.Debug(f"Optionable symbols: {self.symbols_optionable}")

        self.Debug(f"Slope Pass Count: {len(self.slope_results) if self.slope_results else 0}")
        self.Debug(f"Volume Pass Count: {len(self.volume_results) if self.volume_results else 0}")
        self.Debug(f"IV/RV Pass Count: {len(self.ivrv_results) if self.ivrv_results else 0}")

        self.SetRuntimeStatistic("Earnings Symbols", str(self.symbols_total))
        self.SetRuntimeStatistic("Optionable Symbols", str(self.symbols_optionable))
        self.SetRuntimeStatistic("Slope Filtered", str(len(self.slope_results) if self.slope_results else 0))
        self.SetRuntimeStatistic("Volume Filtered", str(len(self.volume_results) if self.volume_results else 0))
        self.SetRuntimeStatistic("IV/RV Filtered", str(len(self.ivrv_results) if self.ivrv_results else 0))
        import json

        if OBJECT_LOG:
            for name, info in OBJECT_LOG.items():
                object_summary = {
                    "type": info["type"],
                    "attributes": list(info["attributes"].keys()),
                    "methods": info["methods"]
                }
                # Store each object in its own runtime key
                key = f"Object {name}"
                value = json.dumps(object_summary)[:5000]  # Truncate just in case
                self.SetRuntimeStatistic(key, value)

