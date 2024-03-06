from AlgorithmImports import *
from scipy import stats
from datetime import timedelta, datetime

class CrossSectorMRVolatilityOptionTrade(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2018, 1, 1)  # Set Start Date
        self.SetEndDate(2020, 1, 1)  # Set End Date
        self.SetCash(100000)  # Set Strategy Cash
        self.startTime = self.Time  # Store the start time of the algorithm

        equities = ['AAPL', 'MSFT']  # 'GOOG', 'AMZN', 'TSLA'
        for equity in equities:

            self.AddEquity(equity, Resolution.Minute)
            option = self.AddOption(equity, Resolution.Minute)
            option.SetFilter(self.UniverseOptionFilter)

        ### Risk and Expiration Parameters ###
        self.max_days_until_expiration_filter = 65
        self.min_days_until_expiration_filter = 30
        self.max_up_strikes = 2
        self.max_down_strikes = -2
        self.min_days_to_expiration = 14

        self.rolling_window_length = 30  # or another suitable period
        self.equity_rolling_windows = {symbol: RollingWindow[TradeBar](self.rolling_window_length) for symbol in equities}
        self.iv_rolling_windows = {symbol: RollingWindow[float](252) for symbol in equities}  # 252 trading days in a year

        self.equal_weight_allocation = 0.02

        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())

    def OnEndOfAlgorithm(self):
        endTime = self.Time  # Store the end time of the algorithm
        duration = endTime - self.startTime
        self.Log(f"Backtest simulated time duration: {duration}")

    def CalculateHistoricalVolatility(self, window) -> float:
        # Calculate daily log returns
        daily_returns = [np.log(window[i].Close / window[i + 1].Close) for i in range(window.Count - 1)]

        # Calculate the standard deviation of returns
        std_dev = np.std(daily_returns)

        # Annualize the standard deviation
        historical_volatility = std_dev * np.sqrt(252)  # Assuming 252 trading days in a year

        # self.Log(f"Historical Volatility calculated: {historical_volatility}, max std_dev :{std_dev.max()}, min std_dev {std_dev.min()}") # std_dev is only one value, max==min
        return historical_volatility

    def CalculatePercentile(self, iv_window, current_iv):
        if not iv_window.IsReady:
            self.Log("IV rolling window is not ready.")
            return None

        # Convert rolling window of IVs to a list
        iv_list = [iv_window[i] for i in range(iv_window.Count)]

        # Find the percentile of the current IV
        percentile = stats.percentileofscore(iv_list, current_iv) / 100.0

        # self.Log(f"Implied Volatility Percentile calculated: {round(percentile, 4)}; IV List: {iv_list}; Current IV: {round(current_iv, 4)}")
        return percentile

    def UniverseOptionFilter(self, universe: OptionFilterUniverse):
        return universe.IncludeWeeklys()\
                       .Strikes(self.max_down_strikes, self.max_up_strikes)\
                       .Expiration(timedelta(30), timedelta(60))

    def OnData(self, data):
        """OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        """

        insights = []

        for equity, window in self.equity_rolling_windows.items():
            # self.Log(f'OD1 looping {equity},{window} in {len(self.equity_rolling_windows)}')
            if data.Bars.ContainsKey(equity) and data.Bars[equity] is not None:
                # self.Log(f'OD2 conditionals {data.Bars.ContainsKey(equity)} and data.Bars[equity] is Not None')
                window.Add(data.Bars[equity])
                # self.Log(f'OD3 Data Added')
                if window.IsReady:
                    # self.Log(f'OD4 Window is Ready')
                    historical_volatility = self.CalculateHistoricalVolatility(window)
                    # self.Log(f'OD5 Historical Volatility Calculated')
                    self.iv_rolling_windows[equity].Add(historical_volatility)
                    # self.Log(f'OD6 Historical Volatility added to iv_rolling_windows')


                    for option_chain in data.OptionChains.Values:
                        # self.Log(f'OD7 looping {option_chain} in {len(data.OptionChains.Values)}')
                        for contract in option_chain:
                            # self.Log(f'OD8 looping {contract} in option_chain: {option_chain}')
                            equity_symbol = str(contract.Symbol).split(' ')[0]
                            if equity_symbol not in self.iv_rolling_windows:
                                # self.Log(f'OD9 contract Missing in iv_rolling_windows') ### Aqui es donde esta todo el problema
                                # self.Log(f'OD9.1 simple example  equity_symbol {equity_symbol}, contract {contract}, iv_rw {self.iv_rolling_windows}')
                                continue

                            current_iv = contract.ImpliedVolatility
                            # self.Log(f'OD10 ImpliedVolatility is {current_iv}')
                            iv_window = self.iv_rolling_windows[equity_symbol]
                            # self.Log(f'OD11 iv_window obtained for {equity_symbol}')
                            iv_percentile = self.CalculatePercentile(iv_window, current_iv)
                            # self.Log(f'OD12 PercentileCalculated : {iv_percentile}')
                            if iv_percentile is None:
                                # self.Log(f'OD12.1 iv_percentile is None')
                                continue

                            # self.Log(f'OD13 Implied Volatility obtained {current_iv}')
                            self.iv_rolling_windows[equity_symbol].Add(current_iv)
                            # self.Log(f'OD14 Implied Volatility added to iv_rolling_windows')

                            if iv_percentile < 0.15:
                                # self.Log(f'OD15 iv_pecentile {iv_percentile} is less than 0.15')
                                insights.append(Insight.Price(equity, timedelta(days=1), InsightDirection.Up))
                                self.BuyCall(option_chain)
                                # self.Log(f"Bullish Insight on {contract} [OPEN-BUY]")
                            elif iv_percentile > 0.85:
                                # self.Log(f'OD16 iv_pecentile {iv_percentile} is more than 0.85')
                                insights.append(Insight.Price(equity, timedelta(days=1), InsightDirection.Down))
                                self.SellCall(option_chain)
                                # self.Log(f"Bearish Insight on {contract} [OPEN-SELL]")
                            elif 0.15 < iv_percentile < 0.85:
                                pass
                                # self.Log(f'OD17 iv_percentile is in non trade range')

        self.EmitInsights(insights)
        # if not self.Portfolio.Invested:
        #     self.Log('OnData executing not invested') ### Too much LOGGING

    def BuyCall(self, chains):
        """Method to execute to open a long position on a call option chain"""
        expiry = sorted(chains, key=lambda x: x.Expiry, reverse=True)[0].Expiry
        calls = [i for i in chains if i.Expiry == expiry and i.Right == OptionRight.Call]
        call_contracts = sorted(calls, key=lambda x: abs(x.Strike - x.UnderlyingLastPrice))
        if len(call_contracts) == 0:
            return
        self.call = call_contracts[0]
        quantity = int(round(((self.equal_weight_allocation * self.Portfolio.TotalPortfolioValue) / (self.call.AskPrice * 100)),0))
        self.Debug(f"weight: {self.equal_weight_allocation}; Port {self.Portfolio.TotalPortfolioValue}; Ask Price: {self.call.AskPrice}; quantity to purchase: {quantity}")
        insight = Insight.Price(self.call.Symbol, timedelta(40), InsightDirection.Up, None, None, sourceModel='CrossSectorMRVolatilityOptionTrade', weight=self.equal_weight_allocation)
        self.EmitInsights(insight)
        # self.EmitInsights(Insight.Price(self.call.Symbol, timedelta(40), InsightDirection.Up))
        self.Buy(self.call.Symbol, quantity).UpdateTag("Open Long Call Position")

    def SellCall(self, chains):
        """Method to execute to open a short position on a call option chain"""
        expiry = sorted(chains, key=lambda x: x.Expiry, reverse=False)[0].Expiry
        calls = [i for i in chains if i.Expiry == expiry and i.Right == OptionRight.Call]
        call_contracts = sorted(calls, key=lambda x: abs(x.Strike - x.UnderlyingLastPrice))
        if len(call_contracts) == 0:
            return
        self.call = call_contracts[0]


        quantity = int(round(((self.equal_weight_allocation * self.Portfolio.TotalPortfolioValue) / (self.call.BidPrice * 100)),0))
        self.Debug(f"weight: {self.equal_weight_allocation}; Port {self.Portfolio.TotalPortfolioValue}; Bid Price: {self.call.BidPrice}; quantity to purchase: {quantity}")
        insight = Insight.Price(self.call.Symbol, timedelta(40), InsightDirection.Up, None, None, sourceModel='CrossSectorMRVolatilityOptionTrade', weight=self.equal_weight_allocation)
        self.EmitInsights(insight)
        # self.EmitInsights(Insight.Price(self.call.Symbol, timedelta(40), InsightDirection.Down))
        self.Sell(self.call.Symbol, quantity).UpdateTag("Open Short Call Position")

class EqualWeightingPortfolioConstructionModel(PortfolioConstructionModel):
    def __init__(self):
        super().__init__()
        self.targets = []

    def CreateTargets(self, algorithm, insights):
        if len(insights) == 0:
            # Log for debugging
            # algorithm.Log("No insights generated, returning no targets.")  ### Too much LOGGING
            return []

        target_percent = 1.0 / len(insights)
        self.targets = [PortfolioTarget(insight.Symbol, target_percent) for insight in insights]

        # Log for debugging
        algorithm.Log(f"Created targets based on {len(insights)} insights.")

        return self.targets
