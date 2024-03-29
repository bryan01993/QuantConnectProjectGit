from AlgorithmImports import *
from datetime import timedelta

class BuyAndHoldOptions(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2010, 10, 7)  # Set Start Date
        self.SetEndDate(2020, 10, 11)  # Set End Date
        self.SetCash(100000)  # Set Strategy Cash

        # Define a list of tickers for the universe
        self.tickers = ["MSFT", "AAPL"]

        # Add a universe of selected tickers
        self.AddUniverse(self.CoarseSelectionFunction)

        equity = self.AddEquity("MSFT", Resolution.Hour)
        equity.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.equity = equity.Symbol
        self.SetBenchmark(self.equity)
        self.min_days_to_expiration = 4
        self.option = self.AddOption("MSFT", resolution=Resolution.Hour)
        self.option.SetFilter(-3, 3, timedelta(20), timedelta(40))

        self.equal_weight_allocation = 0.05
        self.max_sl_percent = -0.5
        self.max_tp_percent = 1.0

        self.max_period_lookback = 21
        self.min_period_lookback = 21

        self.high = self.MAX(self.equity, self.max_period_lookback, Resolution.Daily, Field.High)
        self.low = self.MIN(self.equity, self.min_period_lookback, Resolution.Daily, Field.Low)

        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())

        self.Settings.MinimumOrderMarginPortfolioPercentage = 10
        print("BuyAndHoldOptions Initialized")

    def CoarseSelectionFunction(self, coarse):
        # Filter the universe for only the tickers we're interested in
        filtered_symbols = [x.Symbol for x in coarse if x.Symbol.Value in self.tickers]
        return filtered_symbols

    def BuyCall(self, chains):
        """Method to execute to open a long position on a call option chain"""
        # self.Log(f"Attempting to BuyCall")
        # self.Debug(f"Attempting to BuyCall")
        expiry = sorted(chains, key=lambda x: x.Expiry, reverse=True)[0].Expiry
        calls = [i for i in chains if i.Expiry == expiry and i.Right == OptionRight.Call]
        call_contracts = sorted(calls, key=lambda x: abs(x.Strike - x.UnderlyingLastPrice))
        if len(call_contracts) == 0:
            return
        self.call = call_contracts[0]
        self.Debug(f"BUY CALL: {self.call} type {type(self.call)}")

        quantity = int(round(((self.equal_weight_allocation * self.Portfolio.TotalPortfolioValue) / (self.call.AskPrice * 100)),0))
        self.Debug(f"weight: {self.equal_weight_allocation}; Port {self.Portfolio.TotalPortfolioValue}; Ask Price: {self.call.AskPrice}; quantity to purchase: {quantity}")
        insight = Insight.Price(self.call.Symbol, timedelta(40), InsightDirection.Up, None, None, sourceModel='BuyAndHoldOptions', weight=self.equal_weight_allocation)
        self.EmitInsights(insight)
        # self.EmitInsights(Insight.Price(self.call.Symbol, timedelta(40), InsightDirection.Up))
        self.Buy(self.call.Symbol, quantity).UpdateTag("Open Long Call Position")


    def SellCall(self, chains):
        """Method to execute to open a short position on a call option chain"""
        # self.Log(f"Attempting to SellCall")
        # self.Debug(f"Attempting to SellCall")
        expiry = sorted(chains, key=lambda x: x.Expiry, reverse=False)[0].Expiry
        calls = [i for i in chains if i.Expiry == expiry and i.Right == OptionRight.Call]
        call_contracts = sorted(calls, key=lambda x: abs(x.Strike - x.UnderlyingLastPrice))
        if len(call_contracts) == 0:
            return
        self.call = call_contracts[0]
        self.Debug(f"SELL CALL: {self.call} type {type(self.call)}")


        quantity = int(round(((self.equal_weight_allocation * self.Portfolio.TotalPortfolioValue) / (self.call.BidPrice * 100)),0))
        self.Debug(f"weight: {self.equal_weight_allocation}; Port {self.Portfolio.TotalPortfolioValue}; Bid Price: {self.call.BidPrice}; quantity to purchase: {quantity}")
        insight = Insight.Price(self.call.Symbol, timedelta(40), InsightDirection.Up, None, None, sourceModel='BuyAndHoldOptions', weight=self.equal_weight_allocation)
        self.EmitInsights(insight)
        # self.EmitInsights(Insight.Price(self.call.Symbol, timedelta(40), InsightDirection.Down))
        self.Sell(self.call.Symbol, quantity).UpdateTag("Open Short Call Position")

    def OnData(self, data):
        """OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        """

        # Checks if high value exists
        if not self.high.IsReady:
            self.Debug(f"High indicator is not ready")
            return

        # Checks if there is an option position
        option_invested = [x.Key for x in self.Portfolio if x.Value.Invested and x.Value.Type == SecurityType.Option]

        # If there is an option position liquidate whenever too close to expiration date
        if option_invested:
            # self.Log(f'Current amount of positions {len(option_invested)}')
            if self.Time + timedelta(self.min_days_to_expiration) >= option_invested[0].ID.Date:
                self.Liquidate(option_invested[0], "Too close to expiration")
                return
            else:
                # Check if the option position has lost 50% or more of its value
                for option_symbol in option_invested:
                    # self.Log('Looping through positions')
                    option_security = self.Securities[option_symbol]
                    # Calculate the loss percentage from the average price and current price
                    trade_open_profit_percentage = (option_security.Price - option_security.Holdings.AveragePrice) / option_security.Holdings.AveragePrice
                    # If the loss exceeds 50%, liquidate the position with a market order
                    if trade_open_profit_percentage <= self.max_sl_percent:
                        self.Liquidate(option_symbol, f"Cutting losses at {trade_open_profit_percentage}")
                    if trade_open_profit_percentage > self.max_tp_percent:
                        self.Liquidate(option_symbol, f"Taking profit at {trade_open_profit_percentage}")
            return

        # Strategy Logic Long
        if self.Securities[self.equity].Price >= self.high.Current.Value:
            for i in data.OptionChains:
                chains = i.Value
                self.BuyCall(chains)

        # Strategy Logic Short
        if self.Securities[self.equity].Price <= self.low.Current.Value:
            for i in data.OptionChains:
                chains = i.Value
                self.SellCall(chains)

        # Checks if invested
        # if not self.Portfolio.Invested:
        #     # self.SetHoldings("SPY", 1)
        #     self.Debug("Not invested yet")

    # def UniverseFunc(self, universe):
    #     return universe.IncludeWeeklys() \
    #         .Strikes(-1, 1) \
    #         .Expiration(timedelta(0), timedelta(10))

    def OnOrderEvent(self, orderEvent):
        """ Liquidate stocks in case an option has been exercised"""
        order = self.Transactions.GetOrderById(orderEvent.OrderId)
        self.Log(f"OrderEvent FillPrice{orderEvent.FillPrice}; OrderStatus {orderEvent.Status}; Order ID{orderEvent.OrderId}; Quantity {orderEvent.Quantity}")
        if order.Type == OrderType.OptionExercise:
            self.Liquidate(tag="Liquidation of exercised stocks")
