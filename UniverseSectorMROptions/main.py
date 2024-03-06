### START CODE ###

# region imports
from typing import Optional, Any

from AlgorithmImports import *
from QuantConnect.Data.Fundamental import MorningstarSectorCode
from datetime import timedelta
from ..PropietaryCode.decorators import timeit
from QuantConnect.Algorithm import QCAlgorithm
import statsmodels.tsa.stattools as ts
import statsmodels.api as sm
import numpy as np

# endregion

class UniverseSectorMROptions(QCAlgorithm):

    def __init__(self):
        super().__init__()
        self.OptionChains = None

    def Initialize(self):
        self.SetStartDate(2018, 1, 1)  # Set Start Date
        self.SetEndDate(2019, 6, 1)  # Set End Date
        self.SetCash(100000)  # Set Strategy Cash
        self.UniverseSettings.Resolution = Resolution.Daily
        # self.AddUniverse(self.FundamentalSelectionFunction)
        self.AddUniverse(self.CoarseSelectionFunction,
                         self.FineSelectionFunction)  # Universe based on a Financial Services ETF
        self.UniverseSettings.Leverage = 1.0
        # self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())
        self.startTime = self.Time  # Store the start time of the algorithm
        self.chain_of_options = self.OptionChainProvider
        self.selected_sector_list = [MorningstarSectorCode.FinancialServices,
                                     MorningstarSectorCode.RealEstate,
                                     MorningstarSectorCode.BasicMaterials,
                                     MorningstarSectorCode.Energy,
                                     MorningstarSectorCode.Healthcare,
                                     MorningstarSectorCode.Industrials,
                                     MorningstarSectorCode.ConsumerCyclical,
                                     MorningstarSectorCode.Utilities]
        self.minimum_dollar_amount_volume = 10000000
        self.min_stock_price = 10
        self.max_stock_price = 200
        self.historical_data_days_backward = 250
        self.max_coarse_stocks = 400
        self.max_fine_stocks = 100
        self.target_dtexp_multiplier = 1.5
        self.min_opt_days_to_exp = 15
        self.max_opt_days_to_exp = 90
        self.SetPortfolioConstruction(CustomEqualWeightingPCM(max_weight_per_insight=0.01))

    @timeit
    def OnSecuritiesChanged(self, changes):
        pass
        # for security in changes.AddedSecurities:
        # self.AddEquity(security.Symbol, Resolution.Daily)
        # self.Log(f'OSC0 added {security}')

        # for security in changes.RemovedSecurities:
        # self.AddEquity(security.Symbol, Resolution.Daily)
        # self.Log(f'OSC1 removed {security}')

    @timeit
    def CoarseSelectionFunction(self, coarse) -> list:
        # Filter for stocks that are liquid enough and if they have enough fundamental data.
        self.filtered_by_price = sorted(
            [(x.Symbol, x.DollarVolume) for x in coarse if self.min_stock_price < x.Price < self.max_stock_price
             and x.DollarVolume > self.minimum_dollar_amount_volume and x.HasFundamentalData], key=lambda x: x[1],
            reverse=True)[
                                 :self.max_coarse_stocks]
        return [symbol for symbol, _ in self.filtered_by_price]

    @timeit
    def FineSelectionFunction(self, fine) -> list:
        # Filter for stocks that belong to one specific sector
        self.financial_services_stocks = [sec.Symbol for sec in fine
                                          if
                                          sec.AssetClassification.MorningstarSectorCode in self.selected_sector_list][
                                         :self.max_fine_stocks]

        # Filter for stocks that are optionable
        self.optionable_stocks = []
        for symbol in self.financial_services_stocks:
            # self.Log(f'U1 {symbol}') # STEP XHWS2641G291
            # if self.Securities.ContainsKey(symbol):
            option_contracts = self.OptionChainProvider.GetOptionContractList(symbol, self.Time)
            if len(option_contracts) > 0:
                self.optionable_stocks.append(symbol)
            else:
                pass

        # Log the list of optionable stocks
        # stocks_printed = [str(symbol) for symbol in self.optionable_stocks]
        # self.Log(f'U4 finserv & optionable  stocks {stocks_printed}, len: {len(self.optionable_stocks)}') # ['ABCB R735QTJ8XC9X', 'ACL R735QTJ8XC9X']

        return self.optionable_stocks

    def GetOptionsByInsight(self, insight_direction: str, reversion_time: timedelta) -> Optional[Any]:
        target_expiration = self.Time + timedelta(days=reversion_time.days * self.target_dtexp_multiplier)
        option_chain = self.OptionChainProvider.GetOptionContractList(self.security.Symbol, self.Time)  # To abandon
        self.option.SetFilter(-3, 3, timedelta(self.min_opt_days_to_exp),
                              timedelta(reversion_time.days * self.target_dtexp_multiplier))
        max_expiration_date = self.Time + timedelta(days=self.max_opt_days_to_exp)  # To abandon
        valid_options = [option for option in option_chain if
                         option.ID.Date >= target_expiration and option.ID.Date < max_expiration_date]  # To abandon
        # self.Debug(f"{valid_options}, has a len of {len(valid_options)}")
        # self.Debug(f"{option_chain}")
        if insight_direction:
            if insight_direction == 'Bullish':
                expiry = sorted(self.security_chains, key=lambda x: x.Expiry, reverse=True)[0].Expiry
                calls = [i for i in self.security_chains if i.Expiry == expiry and i.Right == OptionRight.Call]
                call_contracts = sorted(calls, key=lambda x: abs(x.Strike - x.UnderlyingLastPrice))
                if len(call_contracts) == 0:
                    return None
                self.call = call_contracts[0]
                self.Debug(f"CALL: {self.call} type {type(self.call)}")
                return self.call

            elif insight_direction == 'Bearish':
                expiry = sorted(self.security_chains, key=lambda x: x.Expiry, reverse=False)[0].Expiry
                puts = [i for i in self.security_chains if i.Expiry == expiry and i.Right == OptionRight.Put]
                put_contracts = sorted(puts, key=lambda x: abs(x.Strike - x.UnderlyingLastPrice))
                if len(put_contracts) == 0:
                    return None
                self.put = put_contracts[0]
                self.Debug(f"PUT: {self.put} type {type(self.put)}")
                return self.put

            elif insight_direction == 'Neutral':
                return None
        else:
            return None

    def SelectSingleDirectionalOptions(self, list_of_options):
        # # Select near-the-money call option
        current_price = self.security.Price
        if list_of_options:
            # selected_option = min(list_of_options,key=lambda x: abs(x.ID.StrikePrice - current_price))
            # self.Debug(f"selected_option {selected_option}")
            return list_of_options
        else:
            return None

    def ExecutionOptionOrder(self, max_amount: float, option_price: float, option_selected: list):
        if option_selected:
            options_quantity = self.CalculateOptionQuantity(self, max_amount, option_price)
            self.Buy(option_selected.Symbol, options_quantity)
            return None

    def CalculateOptionQuantity(self, max_amount: float, option_price: float) -> int:
        quantity = int(round(((max_amount) / (self.option_price.BidPrice * 100)), 0))
        self.Debug(
            f"max_amount =1000; option_price= {option_price}; quantity to purchase: {quantity}")
        return quantity

    # @timeit
    def OnData(self, data):
        #  Loop on securities inside the Universe
        for security in self.ActiveSecurities.Values:
            self.security = security
            if self.security.HasData:
                #  Gets history for ADF and OU processes
                price_history = self.History(self.security.Symbol, self.historical_data_days_backward, Resolution.Daily)
                # Apply the ADF test to the closing prices
                if price_history.empty:
                    self.Log(f"No price history available for {self.security.Symbol}")
                else:
                    # Test ADF to see if the stock is mean-reverting
                    if self.ApplyADFTest(price_history['close']):
                        # Calculate Z-Score to see if we are above/below the mean
                        self.z_score = round(self.CalculateZScore(price_history['close']), 4)
                        # Calculate OU Process to obtain time to reversion and Mean price (target)
                        self.reversion_time, mean_level = self.FitOUProcess(price_history['close'])

                        if self.EnsureAllVariables(self.z_score, self.reversion_time, mean_level):
                            insight_direction = self.EvaluateZScore(self.z_score)
                            try:
                                self.option = self.AddOption(self.security.Symbol, resolution=Resolution.Hour)
                                self.option.SetFilter(-3,3,timedelta(self.min_opt_days_to_exp), timedelta(self.max_opt_days_to_exp))
                            except:
                                self.Log(f" security {self.security.Symbol} has no options")
                                pass
                            for symbol, chains in data.OptionChains.items():
                                symbol_looped = symbol
                                chain_looped = chains
                                self.Log(f"looping through {data.OptionChains.items()} with {symbol_looped} and {chain_looped}")
                            #     self.security_chains = chains
                            #     list_of_directional_options = self.GetOptionsByInsight(insight_direction,
                            #                                                            self.reversion_time)
                            #     # for symbol, chains in data.OptionChains.items():
                            #     # self.security_chains = chains
                            #     option_selected = self.SelectSingleDirectionalOptions(list_of_directional_options)
                            #     insight_created = self.CreateOptionDirectionalInsight(insight_direction,
                            #                                                           self.reversion_time, mean_level,
                            #                                                           list_of_directional_options)
                            #     self.Debug(f"Option_selected = {option_selected} of type {type(option_selected)}")
                            # if option_selected:
                            #     option_order_execution = self.ExecutionOptionOrder(max_amount=1000, option_price=option_selected.BidPrice, option_selected=option_selected)

    # @timeit
    def ApplyADFTest(self, price_series) -> bool:
        if len(price_series) > self.historical_data_days_backward * 0.5:
            adf_result = ts.adfuller(price_series)
            # Check if the test statistic is less than the 5% critical value
            is_mean_reverting = adf_result[0] < adf_result[4]['5%']
            if is_mean_reverting:
                self.Log(
                    f"ADF test result for {price_series.name}: Statistic: {adf_result[0]}, 5% Critical Value: {adf_result[4]['5%']}, Mean Reverting: {is_mean_reverting}")
            return is_mean_reverting
        else:
            return False

    def ApplyHurstTest(self, price_series):
        # Implement Hurst exponent calculation
        # it's another method to replace ADF to test for mean reversion time series
        pass

    def FitOUProcess(self, price_series) -> (timedelta, float):
        """
        Fit an Ornstein-Uhlenbeck process to the given price series and
        calculate the expected time to reversion.
        """
        # function_time_start = self.Time
        try:
            # Calculate changes in the price series
            delta_prices = np.diff(price_series)

            # Prepare the lagged price series (X_t-1)
            lagged_prices = price_series[:-1]

            # Perform linear regression to estimate theta and mu
            X = sm.add_constant(lagged_prices)
            model = sm.OLS(delta_prices, X).fit()

            theta = -model.params[1]
            mu = model.params[0] / theta

            # Calculate expected time to reversion
            if theta > 0:
                self.int_days_to_reversion = theta
                expected_time_to_reversion = timedelta(days=1 / theta)
                self.Log(f"FOUP0 {self.security} Expected time to reversion: {expected_time_to_reversion} days")
                # function_time_emd = self.Time
                # total_time = function_time_emd-function_time_start
                # self.Debug(f'FitOUProcess took {total_time} seconds') # Debug
                return expected_time_to_reversion, mu
            else:
                self.Log("FOUP1 Theta is not positive. The series might not be mean-reverting.")
                return None, None

        except Exception as e:
            self.Log(f"FOUPE Error in fitting OU process: {str(e)}")
            return None, None

    @timeit
    def CalculateZScore(self, price_series) -> Optional[float]:
        try:
            # Linear regression with time as the independent variable
            X = np.arange(len(price_series)).reshape(-1, 1)
            y = price_series.values
            model = sm.OLS(y, sm.add_constant(X)).fit()
            residuals = model.resid

            # Calculate Z-score
            mean = np.mean(residuals)
            std_dev = np.std(residuals)
            if std_dev > 0:
                z_score = (residuals[-1] - mean) / std_dev
                return z_score
            else:
                return None
        except Exception as e:
            self.Log(f"Error in calculating Z-score: {str(e)}")
            return None

    @timeit
    def EvaluateZScore(self, z_score: float) -> str:
        # self.Debug(f'z_score received {z_score}')
        if z_score <= -2:
            return 'Bullish'
        if -2 < z_score < 2:
            return 'Neutral'
        if z_score >= 2:
            return 'Bearish'
        else:
            # self.Debug(f'Unexpected value {z_score}') # Unexpected value 1.2865 ## WHY? you dumbfuck
            return f'Unexpected value {z_score} with type {type(z_score)}'

    # @timeit
    def CreateOptionDirectionalInsight(self, insight_direction: str, insight_duration: timedelta, mean_level: float,
                                       option_selected):
        if option_selected:
            self.Debug(f"option_selected {option_selected} of type {type(option_selected)}")
            insight_direction_object = ''
            if insight_direction == 'Bullish':
                insight_direction_object = InsightDirection.Up
            elif insight_direction == 'Bearish':
                insight_direction_object = InsightDirection.Down
            elif insight_direction == 'Neutral':
                insight_direction_object = InsightDirection.Flat
                return None
            elif 'Unexpected' in insight_direction:
                # self.Debug(f'{insight_direction} is not determined.') # Unexpected value 1.2865 ## WHY?
                return None
            try:
                insight = Insight.Price(symbol=option_selected.Symbol,
                                        barCount=40,
                                        direction=insight_direction_object,
                                        magnitude=0.69,
                                        confidence=0.70,
                                        sourceModel='UniverseSectorMROptions',
                                        weight=0.5,
                                        tag='UniverseSectorMROptionsTAG')

                self.Debug(f"Option insight emitted for {option_selected}")
                self.EmitInsights(insight)
                return insight

            except Exception as e:
                self.Debug(f"Found the following exception when emitting insight. {e}")
                self.Log(f"Found the following exception when emitting insight. {e}")
                return None

    @timeit
    def EnsureAllVariables(self, z_score: float, reversion_time: timedelta, mean_level: float) -> bool:
        if z_score is not None and reversion_time is not None and mean_level is not None:
            return True
        else:
            self.Debug(f'Unexpected values encountered')
            return False

    def OnEndOfAlgorithm(self):
        endTime = self.Time  # Store the end time of the algorithm
        duration = endTime - self.startTime
        self.Log(f"Backtest simulated time duration: {duration}")


# Add additional methods and logic as needed


class CustomEqualWeightingPCM(EqualWeightingPortfolioConstructionModel):
    def __init__(self, max_weight_per_insight=0.01):
        self.max_weight_per_insight = max_weight_per_insight
        super().__init__()

    def CreateTargets(self, algorithm, insights):
        targets = super().CreateTargets(algorithm, insights)
        current_balance = algorithm.Portfolio.TotalPortfolioValue
        max_weight_value = current_balance * self.max_weight_per_insight

        # Adjust targets based on max weight per insight
        adjusted_targets = []
        for target in targets:
            # Calculate target quantity based on max weight
            target_value = min(abs(target.Quantity * algorithm.Securities[target.Symbol].Price), max_weight_value)
            quantity = target_value / algorithm.Securities[target.Symbol].Price
            adjusted_quantity = quantity if target.Quantity >= 0 else -quantity
            adjusted_targets.append(PortfolioTarget(target.Symbol, adjusted_quantity))
            # algorithm.Debug(f"Target for {target.Symbol}: {adjusted_quantity} shares, equal to {algorithm.Securities[target.Symbol].Price * quantity}")

        return adjusted_targets
### END CODE ###
