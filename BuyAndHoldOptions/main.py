from AlgorithmImports import *
from datetime import timedelta
from PropietaryCode.decorators import FunctionLogger
from PropietaryCode.BSMModel import BsmModel


# import pydevd_pycharm
# pydevd_pycharm.settrace('localhost', port=6000, stdoutToServer=True, stderrToServer=True)


class BuyAndHoldOptions(QCAlgorithm):

    def Initialize(self):
        self.logger = FunctionLogger(self)
        self.SetStartDate(2015, 1, 1)  # Set Start Date
        self.SetEndDate(2015, 12, 31)  # Set End Date
        self.SetCash(100000)  # Set Strategy Cash

        # Define a list of tickers for the universe
        # For Universe methods do this same procedure in OnSecuritiesChanged
        self.equities = ["AAPL", "GOOG"]
        for ticker in self.equities:
            equity = self.AddEquity(ticker)
            option = self.AddOption(ticker, resolution=Resolution.Daily)

            # Option filter for each equity
            option.SetFilter(self.UniverseFunc)

        # Add a universe of selected tickers
        self.AddUniverse(self.CoarseSelectionFunction)

        self.SetBenchmark("SPY")
        # self.DebugMode = True

        self.max_period_lookback = 21
        self.min_period_lookback = 21

        # self.high = self.MAX(self.equity, self.max_period_lookback, Resolution.Daily, Field.High)
        # self.low = self.MIN(self.equity, self.min_period_lookback, Resolution.Daily, Field.Low)

        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())
        self.risk_free_interest_rate = self.RiskFreeInterestRateModel.GetInterestRate(self.Time)
        self.Settings.MinimumOrderMarginPortfolioPercentage = 10
        self.Debug("BuyAndHoldOptions Initialized")

    @FunctionLogger.log
    def UniverseFunc(self, universe):
        return universe.IncludeWeeklys() \
            .Strikes(-2, 2) \
            .Expiration(timedelta(days=20), timedelta(days=40))

    @FunctionLogger.log
    def CoarseSelectionFunction(self, coarse):
        # Filter the universe for only the tickers we're interested in
        filtered_symbols = [x.Symbol for x in coarse if x.Symbol.Value in self.equities]
        # self.Log(f"filtered_symbols: {filtered_symbols}")
        return filtered_symbols

    # def BuyCall(self, chains):
    #     """Method to execute to open a long position on a call option chain"""
    #     # self.Log(f"Attempting to BuyCall")
    #     # self.Debug(f"Attempting to BuyCall")
    #     expiry = sorted(chains, key=lambda x: x.Expiry, reverse=True)[0].Expiry
    #     calls = [i for i in chains if i.Expiry == expiry and i.Right == OptionRight.Call]
    #     call_contracts = sorted(calls, key=lambda x: abs(x.Strike - x.UnderlyingLastPrice))
    #     if len(call_contracts) == 0:
    #         return
    #     self.call = call_contracts[0]
    #     self.Debug(f"BUY CALL: {self.call} type {type(self.call)}")
    #
    #     quantity = int(
    #         round(((self.equal_weight_allocation * self.Portfolio.TotalPortfolioValue) / (self.call.AskPrice * 100)),
    #               0))
    #     self.Debug(
    #         f"weight: {self.equal_weight_allocation}; Port {self.Portfolio.TotalPortfolioValue}; Ask Price: {self.call.AskPrice}; quantity to purchase: {quantity}")
    #     insight = Insight.Price(self.call.Symbol, timedelta(40), InsightDirection.Up, None, None,
    #                             sourceModel='BuyAndHoldOptions', weight=self.equal_weight_allocation)
    #     self.EmitInsights(insight)
    #     # self.EmitInsights(Insight.Price(self.call.Symbol, timedelta(40), InsightDirection.Up))
    #     self.Buy(self.call.Symbol, quantity).UpdateTag("Open Long Call Position")
    #
    # def SellCall(self, chains):
    #     """Method to execute to open a short position on a call option chain"""
    #     # self.Log(f"Attempting to SellCall")
    #     # self.Debug(f"Attempting to SellCall")
    #     expiry = sorted(chains, key=lambda x: x.Expiry, reverse=False)[0].Expiry
    #     calls = [i for i in chains if i.Expiry == expiry and i.Right == OptionRight.Call]
    #     call_contracts = sorted(calls, key=lambda x: abs(x.Strike - x.UnderlyingLastPrice))
    #     if len(call_contracts) == 0:
    #         return
    #     self.call = call_contracts[0]
    #     self.Debug(f"SELL CALL: {self.call} type {type(self.call)}")
    #
    #     quantity = int(
    #         round(((self.equal_weight_allocation * self.Portfolio.TotalPortfolioValue) / (self.call.BidPrice * 100)),
    #               0))
    #     self.Debug(
    #         f"weight: {self.equal_weight_allocation}; Port {self.Portfolio.TotalPortfolioValue}; Bid Price: {self.call.BidPrice}; quantity to purchase: {quantity}")
    #     insight = Insight.Price(self.call.Symbol, timedelta(40), InsightDirection.Up, None, None,
    #                             sourceModel='BuyAndHoldOptions', weight=self.equal_weight_allocation)
    #     self.EmitInsights(insight)
    #     # self.EmitInsights(Insight.Price(self.call.Symbol, timedelta(40), InsightDirection.Down))
    #     self.Sell(self.call.Symbol, quantity).UpdateTag("Open Short Call Position")

    @FunctionLogger.log
    def CalculateVolatility(self, underlying_symbol):
        """Scheduled event to calculate volatility daily"""
        try:
            self.lookback = 252
            history = self.History(underlying_symbol, self.lookback + 1, Resolution.Daily).close.pct_change().dropna()
            underlying_volatility = round(np.std(history) * np.sqrt(252), 4)  # Annualized Volatility
            return underlying_volatility
        except Exception as e:
            self.Debug(f"Exception: {e}")
            return

    @FunctionLogger.log
    def get_current_underlying_price(self, slice):
        return

    # @timeit
    def OnData(self, slice):
        if not self.Portfolio.Invested:
            for kvp in slice.OptionChains:
                if kvp.Key not in self.Securities:
                    continue
                chain = kvp.Value
                # Buy and hold logic for options goes here
                # This is an example to buy a contract if not yet invested
                # You need to replace it with your own logic
                # get underlying volatility
                for contract in chain:
                    if contract.Right == OptionRight.Call and contract.Expiry.date() > self.Time.date():
                        under_vol = self.CalculateVolatility(underlying_symbol=contract.UnderlyingSymbol)
                        # self.Log(f"Contract Underlying symbol and price: {contract.UnderlyingSymbol}, {self.Securities[contract.UnderlyingSymbol].Price}")
                        # self.Debug(f"under_vol = {under_vol}")
                        # self.Debug(f"k: {contract.Strike}, option_price: {self.Securities[contract.Symbol].Price}")
                        days_to_expiration = (contract.Expiry - self.Time).days
                        self.BSM_price = BsmModel(option_type='c',
                                                  price=self.Securities[contract.UnderlyingSymbol].Price,
                                                  strike=contract.Strike,
                                                  interest_rate=self.risk_free_interest_rate,
                                                  expiry=days_to_expiration,
                                                  volatility=under_vol).bsm_price()
                        self.Log(
                            f"Time {self.Time};{contract.Strike},{contract.Expiry},{self.BSM_price};{contract.AskPrice};{contract.UnderlyingSymbol};{under_vol}")
                        if self.BSM_price > contract.LastPrice:
                            self.Buy(contract.Symbol, 1)
                        elif self.BSM_price < contract.LastPrice:
                            self.Sell(contract.Symbol, 1)
                        else:
                            self.Debug(f"Neither escenario happened")
                        break

    # @timeit
    # def OnData(self, data):
    #     """OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
    #         Arguments:
    #             data: Slice object keyed by symbol containing the stock data
    #     """
    #
    #     # Checks if high value exists
    #     if not self.high.IsReady:
    #         self.Debug(f"High indicator is not ready")
    #         return
    #
    #     # Checks if there is an option position
    #     option_invested = [x.Key for x in self.Portfolio if x.Value.Invested and x.Value.Type == SecurityType.Option]
    #
    #     # If there is an option position liquidate whenever too close to expiration date
    #     if option_invested:
    #         # self.Log(f'Current amount of positions {len(option_invested)}')
    #         if self.Time + timedelta(self.min_days_to_expiration) >= option_invested[0].ID.Date:
    #             self.Liquidate(option_invested[0], "Too close to expiration")
    #             return
    #         else:
    #             # Check if the option position has lost 50% or more of its value
    #             for option_symbol in option_invested:
    #                 # self.Log('Looping through positions')
    #                 option_security = self.Securities[option_symbol]
    #                 # Calculate the loss percentage from the average price and current price
    #                 trade_open_profit_percentage = (
    #                                                            option_security.Price - option_security.Holdings.AveragePrice) / option_security.Holdings.AveragePrice
    #                 # If the loss exceeds 50%, liquidate the position with a market order
    #                 if trade_open_profit_percentage <= self.max_sl_percent:
    #                     self.Liquidate(option_symbol, f"Cutting losses at {trade_open_profit_percentage}")
    #                 if trade_open_profit_percentage > self.max_tp_percent:
    #                     self.Liquidate(option_symbol, f"Taking profit at {trade_open_profit_percentage}")
    #         return
    #
    #     # Strategy Logic Long
    #     if self.Securities[self.equity].Price >= self.high.Current.Value:
    #         for i in data.OptionChains:
    #             chains = i.Value
    #             self.BuyCall(chains)
    #
    #     # Strategy Logic Short
    #     if self.Securities[self.equity].Price <= self.low.Current.Value:
    #         for i in data.OptionChains:
    #             chains = i.Value
    #             self.SellCall(chains)
    #
    #     # Checks if invested
    #     # if not self.Portfolio.Invested:
    #     #     # self.SetHoldings("SPY", 1)
    #     #     self.Debug("Not invested yet")
    #
    # # def UniverseFunc(self, universe):
    # #     return universe.IncludeWeeklys() \
    # #         .Strikes(-1, 1) \
    # #         .Expiration(timedelta(0), timedelta(10))

    @FunctionLogger.log
    def OnOrderEvent(self, orderEvent):
        """ Liquidate stocks in case an option has been exercised"""
        order = self.Transactions.GetOrderById(orderEvent.OrderId)
        self.Log(
            f"OrderEvent FillPrice{orderEvent.FillPrice}; OrderStatus {orderEvent.Status}; Order ID{orderEvent.OrderId}; Quantity {orderEvent.Quantity}")
        if order.Type == OrderType.OptionExercise:
            self.Liquidate(tag="Liquidation")
