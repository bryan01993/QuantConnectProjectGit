# region imports
from AlgorithmImports import *
from PropietaryCode.decorators import monitor_execution
from datetime import timedelta, datetime


# endregion

class AlgoTester(QCAlgorithm):
    def Initialize(self):

        self.SetStartDate(*map(int, self.GetParameter("exec.start_date").split('-')))  # Set a fixed start date
        self.SetEndDate(*map(int, self.GetParameter("exec.end_date").split('-')))   # Set a fixed end date
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
        self.Log(f"{parameter_test} in sector, and {environment_test} in env")
        self.Log(f"{universe_coarse_size_test} in universe_coarse_size_test, and data type {type(universe_coarse_size_test)}.")

        self.next_option_trade = self.Time.replace(day=1)  # Track next option trade day
        self.option_position = None

        self.Schedule.On(self.DateRules.EveryDay(self.spy), self.TimeRules.At(9, 31), self.CheckOptionExpiration)

    def OnData(self, data):
        if not self.Portfolio[self.spy].Invested:
            self.MarketOrder(self.spy, int(1000 / data[self.spy].Close))

        # Buy call option at the beginning of each month
        if self.Time >= self.next_option_trade:
            self.TradeOptions(data)
            self.next_option_trade = self.Time + timedelta(weeks=4)  # Next trade in 1 month

    @monitor_execution
    def OptionFilter(self, universe):
        return universe.Strikes(0, 5).Expiration(0, 31).CallsOnly()

    @monitor_execution
    def TradeOptions(self, data):
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

    @monitor_execution
    def CheckOptionExpiration(self):
        if not self.option_position:
            return

        contract = self.option_position
        if contract in self.Portfolio and self.Portfolio[contract].Invested:
            expiry = contract.ID.Date
            expiry_datetime = datetime(expiry.year, expiry.month, expiry.day)
            if (expiry_datetime - self.Time).days <= 3:
                self.Liquidate(contract)
