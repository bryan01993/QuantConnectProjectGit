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
        self.AddUniverse(self.Universe.Index.QC500)  # Use a built-in universe like QC500
        self.UniverseSettings.Resolution = Resolution.Hour

        # Option-specific settings
        self.min_days_to_expiration = 4
        self.equal_weight_allocation = 0.05
        self.max_sl_percent = -0.5
        self.max_tp_percent = 1.0
        self.max_period_lookback = 21
        self.min_period_lookback = 21
        self.Settings.MinimumOrderMarginPortfolioPercentage = 10

        # Dynamic storage for symbols and indicators
        self.symbols = {}
        self.indicators = {}

        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())
        print("BuyAndHoldOptions Initialized")

    def UniverseSelection(self, coarse):
        # Filter the universe for only the tickers we're interested in
        selected = [symbol for symbol in coarse if symbol.Symbol.Value in self.tickers]
        for symbol in selected:
            if symbol.Symbol not in self.symbols:
                self.symbols[symbol.Symbol] = symbol

                # Add options for the selected symbol
                option = self.AddOption(symbol.Symbol.Value, resolution=Resolution.Hour)
                option.SetFilter(-3, 3, timedelta(20), timedelta(40))

                # Add indicators for the symbol
                self.indicators[symbol.Symbol] = {
                    'high': self.MAX(symbol.Symbol, self.max_period_lookback, Resolution.Daily, Field.High),
                    'low': self.MIN(symbol.Symbol, self.min_period_lookback, Resolution.Daily, Field.Low)
                }
        return [symbol.Symbol for symbol in selected]

    # ... rest of your code ...
# ... existing OnData logic, updated to handle dynamic symbols and indicators ...

# Note: You'll need to integrate your existing BuyCall and SellCall logic
# and make them work with the dynamically selected symbols and their corresponding indicators.
