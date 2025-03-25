# region imports
from AlgorithmImports import *
from PropietaryCode.decorators import monitor_execution
from datetime import timedelta, datetime


# endregion

class AlgoTester(QCAlgorithm):
    def Initialize(self) -> None:

        self.SetStartDate(*map(int, self.GetParameter("exec.start_date").split('-')))  # Set a fixed start date
        self.SetEndDate(*map(int, self.GetParameter("exec.end_date").split('-')))  # Set a fixed end date
        initial_amount = self.GetParameter("exec.initial_amount")
        if not initial_amount:
            self.Debug("initial amount is not retrieved")
        self.Debug(f"initial_amount = {initial_amount} with type {type(initial_amount)}")
        self.SetCash(initial_amount)  # Set initial cash

        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.option = self.AddOption("SPY", Resolution.Daily)
        self.option.SetFilter(self.OptionFilter)

        parameter_test = self.GetParameter("sector")
        environment_test = self.GetParameter("env")
        universe_coarse_size_test = self.GetParameter("univ.coarse.size")

        self.SetBenchmark("SPY")

        # --- Adding Charts ---
        spy_price_chart = Chart("SPY Price")
        spy_price_chart.AddSeries(Series("Price", SeriesType.Line, 0))
        self.AddChart(spy_price_chart)

        portfolio_chart = Chart("Portfolio Value")
        portfolio_chart.AddSeries(Series("Equity", SeriesType.Line, 0))
        self.AddChart(portfolio_chart)

        option_trades_chart = Chart("Option Trades")
        option_trades_chart.AddSeries(Series("Options Bought", SeriesType.Bar, 0))
        self.AddChart(option_trades_chart)

        self.Log(f"{parameter_test} in sector, and {environment_test} in env")
        self.Log(
            f"{universe_coarse_size_test} in universe_coarse_size_test, and data type {type(universe_coarse_size_test)}.")

        self.next_option_trade = self.Time.replace(day=1)  # Track next option trade day
        self.option_position = None

        self.Schedule.On(self.DateRules.EveryDay(self.spy), self.TimeRules.At(9, 31), self.CheckOptionExpiration)

    def OnData(self, data: Slice):
        if self.spy in data and data[self.spy] is not None and data[self.spy].Close is not None:
            if not self.Portfolio[self.spy].Invested:
                self.MarketOrder(self.spy, int(1000 / data[self.spy].Close))

            # --- Plot SPY Price ---
            self.Plot("SPY Price", "Price", data[self.spy].Close)

        # --- Plot Portfolio Value ---
        self.Plot("Portfolio Value", "Equity", self.Portfolio.TotalPortfolioValue)

        # Buy call option at the beginning of each month
        if self.Time >= self.next_option_trade:
            self.TradeOptions(data)
            self.next_option_trade = self.Time + timedelta(weeks=4)  # Next trade in 1 month

    @monitor_execution
    def OptionFilter(self, universe: OptionFilterUniverse) -> OptionFilterUniverse:
        return universe.Strikes(0, 5).Expiration(0, 31).CallsOnly()

    @monitor_execution
    def TradeOptions(self, data: Slice) -> None:
        if self.option_position and self.Portfolio[self.option_position].Invested:
            return

        chain = self.CurrentSlice.OptionChains.get(self.option.Symbol, None)
        if not chain:
            return

        contracts = sorted(chain, key=lambda x: x.Expiry)
        if not contracts:
            return

        contract = contracts[0]
        self.option_position = contract.Symbol
        self.MarketOrder(contract.Symbol, 1)
        # --- Plot when options are bought ---
        self.Plot("Option Trades", "Options Bought", 1)

    @monitor_execution
    def CheckOptionExpiration(self) -> None:
        if not self.option_position:
            return

        contract = self.option_position
        if contract in self.Portfolio and self.Portfolio[contract].Invested:
            expiry = contract.ID.Date
            expiry_datetime = datetime(expiry.year, expiry.month, expiry.day)
            if (expiry_datetime - self.Time).days <= 3:
                self.Liquidate(contract)
