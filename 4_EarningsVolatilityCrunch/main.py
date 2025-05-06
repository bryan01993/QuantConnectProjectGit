# region imports
from AlgorithmImports import *
from QuantConnect import Symbol
from QuantConnect.Data.Fundamental import FineFundamental
from QuantConnect.DataSource import EODHDUpcomingEarnings
from QuantConnect.Securities import *
from QuantConnect.Securities.Option import QLOptionPriceModel, IQLRiskFreeRateEstimator,ConstantQLDividendYieldEstimator, IQLUnderlyingVolatilityEstimator
from datetime import timedelta, datetime
import pandas as pd
from PropietaryCode.decorators import monitor_execution
from math import sqrt
# endregion

class EarningsVolatilityCrunch(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(*map(int, self.GetParameter("exec.start_date").split('-')))
        self.SetEndDate(*map(int, self.GetParameter("exec.end_date").split('-')))
        self.SetCash(self.GetParameter("exec.initial_amount"))

        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        self.AddUniverse(EODHDUpcomingEarnings, self.UpcomingEarningsSelectionFunction)
        self.earnings_calendar = {}  # Cache for earnings dates

        # Tracking dictionaries
        self.symbols_total = 0
        self.symbols_optionable = 0
        self.slope_results = {}
        self.volume_results = {}
        self.ivrv_results = {}

    @monitor_execution
    def CoarseSelectionFunction(self, coarse: List[CoarseFundamental]) -> List[Symbol]:
        return [x.Symbol for x in coarse if x.HasFundamentalData]

    def FineSelectionFunction(self, fine: List[FineFundamental]) -> List[Symbol]:
        selected = []
        for f in fine:
            earnings = f.EarningReports.file_date.value
            current_date = self.Time
            if current_date < earnings <= current_date + timedelta(days=30):
                if f.Symbol.HasUnderlying and f.Symbol.SecurityType == SecurityType.Equity:
                    option_symbol = Symbol.CreateOption(f.Symbol.Value, Market.USA, OptionStyle.American,
                                                        OptionRight.Call, 0, self.Time)
                    if self.OptionChainProvider.GetOptionContractList(option_symbol.Underlying, self.Time):
                        selected.append(f.Symbol)
                        self.earnings_calendar[f.Symbol] = earnings
        return selected

    def UpcomingEarningsSelectionFunction(self, earnings: List[EODHDUpcomingEarnings]) -> List[Symbol]:
        selected = []
        for e in earnings:
            if e.ReportDate <= self.Time + timedelta(days=int(self.GetParameter("algo.days_before_earnings"))):
                if self.OptionChainProvider.GetOptionContractList(e.Symbol, self.Time):
                    selected.append(e.Symbol)
                    self.earnings_calendar[e.Symbol] = e.ReportDate
        return selected

    def CheckEarningsAndTrade(self):
        for symbol, earnings_date in self.earnings_calendar.items():
            if symbol in self.Securities and self.Securities[symbol].HasData:
                iv = self.Securities[symbol].VolatilityModel.Volatility
                pass

    def OnData(self, data: Slice):
        earnings_symbols = list(self.earnings_calendar.keys())
        self.symbols_total = len(earnings_symbols)

        optionable_symbols = [s for s in earnings_symbols if self.OptionChainProvider.GetOptionContractList(s, self.Time)]
        self.symbols_optionable = len(optionable_symbols)

        self.slope_results = self.calculate_iv_slope(optionable_symbols)
        self.volume_results = self.filter_pre_earnings_volume()
        self.ivrv_results = self.filter_iv_vs_rv()

    def calculate_iv_slope(self, symbols: List[Symbol]):
        slopes = {}

        for symbol in symbols:
            contracts = self.OptionChainProvider.GetOptionContractList(symbol, self.Time)
            if not contracts:
                continue

            calls = [x for x in contracts if x.ID.OptionRight == OptionRight.Call]
            if len(calls) < 2:
                continue

            # Group contracts by strike
            strikes = {}
            for c in calls:
                strike = c.ID.StrikePrice
                if strike not in strikes:
                    strikes[strike] = []
                strikes[strike].append(c)

            # For each strike, attempt to find two contracts with different expirations
            for strike, grouped in strikes.items():
                if len(grouped) < 2:
                    continue
                grouped = sorted(grouped, key=lambda x: x.ID.Date)
                near_contract_symbol = grouped[0]
                far_contract_symbol = grouped[-1]

                # Add the underlying equity first if not already
                if not self.Securities.ContainsKey(symbol):
                    self.AddEquity(symbol.Value, Resolution.Minute)
                self.Securities[symbol].SetDataNormalizationMode(DataNormalizationMode.Raw)

                # Add option contracts
                near_contract = self.AddOptionContract(near_contract_symbol, Resolution.Minute).Symbol
                far_contract = self.AddOptionContract(far_contract_symbol, Resolution.Minute).Symbol

                if not (self.Securities.ContainsKey(near_contract) and self.Securities.ContainsKey(far_contract)):
                    continue

                near_sec = self.Securities[near_contract]
                far_sec = self.Securities[far_contract]

                if not near_sec.HasData or not far_sec.HasData:
                    continue

                if near_sec.Expiry >= far_sec.Expiry:
                    continue

                try:
                    near_sec.PriceModel = QLOptionPriceModel()
                    far_sec.PriceModel = QLOptionPriceModel()

                    near_iv = near_sec.Greeks.ImpliedVolatility
                    far_iv = far_sec.Greeks.ImpliedVolatility

                except:
                    continue

                diff_days = (far_sec.Expiry.date() - near_sec.Expiry.date()).days
                diff_iv = far_iv - near_iv
                slope = sqrt(diff_days ** 2 + diff_iv ** 2)

                if symbol not in slopes:
                    slopes[symbol] = []
                slopes[symbol].append({
                    "strike": strike,
                    "near_contract": near_contract,
                    "far_contract": far_contract,
                    "slope": slope
                })

        return slopes

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


    def OnEndOfAlgorithm(self):
        self.Debug(f"Total earnings symbols: {self.symbols_total}")
        self.Debug(f"Optionable symbols: {self.symbols_optionable}")

        self.Debug(f"Slope Pass Count: {len(self.slope_results)}")
        self.Debug(f"Volume Pass Count: {len(self.volume_results)}")
        self.Debug(f"IV/RV Pass Count: {len(self.ivrv_results)}")

        self.SetRuntimeStatistic("Earnings Symbols", str(self.symbols_total))
        self.SetRuntimeStatistic("Optionable Symbols", str(self.symbols_optionable))
        self.SetRuntimeStatistic("Slope Filtered", str(len(self.slope_results)))
        self.SetRuntimeStatistic("Volume Filtered", str(len(self.volume_results)))
        self.SetRuntimeStatistic("IV/RV Filtered", str(len(self.ivrv_results)))