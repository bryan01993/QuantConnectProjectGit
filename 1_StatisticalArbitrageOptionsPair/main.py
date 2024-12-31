from AlgorithmImports import *
from datetime import timedelta

class StatisticalArbitrageOptionsPair(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2023, 1, 1)
        self.SetCash(100000)

        ## self.sector = "Technology"  # Example: Selectable sector
        self.symbols = self.SelectSectorSymbols(self.GetParameter("sector"))
        for symbol in self.symbols:
            equity = self.AddEquity(symbol, Resolution.Daily)
            option = self.AddOption(symbol, Resolution.Daily)
            option.SetFilter(self.UniverseFilter)

        self.SetBenchmark("SPY")

        # Framework models
        self.SetUniverseSelection(CustomUniverseSelectionModel(self.symbols))
        self.SetAlpha(VolatilityDifferenceAlphaModel())
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())
        self.SetExecution(ImmediateExecutionModel())
        self.SetRiskManagement(MaximumDrawdownPercentPerSecurity(0.05))

    def SelectSectorSymbols(self, sector):
        # Example implementation: Select symbols based on sector
        sector_map = {
            "Technology": ["AAPL", "MSFT", "GOOG"],
            "Finance": ["JPM", "BAC", "GS"],
            "Healthcare": ["JNJ", "PFE", "MRK"]
        }
        return sector_map.get(sector, [])

    def UniverseFilter(self, universe):
        return universe.Strikes(-5, 5).Expiration(10, 45)

class CustomUniverseSelectionModel(UniverseSelectionModel):
    def __init__(self, symbols):
        self.symbols = symbols

    def CreateUniverses(self, algorithm):
        return [ManualUniverse(algorithm, self.symbols)]

class VolatilityDifferenceAlphaModel(AlphaModel):
    def __init__(self, lookback=30, threshold=0.05):
        self.lookback = lookback
        self.threshold = threshold
        self.volatility_data = {}

    def Update(self, algorithm, data):
        insights = []
        for symbol in self.volatility_data.keys():
            realized_vol = self.CalculateRealizedVolatility(symbol, algorithm)
            implied_vol = self.GetImpliedVolatility(symbol, algorithm)

            if implied_vol - realized_vol > self.threshold:
                insights.append(Insight.Price(symbol, timedelta(days=30), InsightDirection.Flat))

        return insights

    def OnSecuritiesChanged(self, algorithm, changes):
        for security in changes.AddedSecurities:
            self.volatility_data[security.Symbol] = RollingWindow[float](self.lookback)
        for security in changes.RemovedSecurities:
            self.volatility_data.pop(security.Symbol, None)

    def CalculateRealizedVolatility(self, symbol, algorithm):
        history = algorithm.History(symbol, self.lookback, Resolution.Daily)
        if len(history) < self.lookback:
            return 0
        returns = history["close"].pct_change().dropna()
        return returns.std() * (252 ** 0.5)

    def GetImpliedVolatility(self, symbol, algorithm):
        option_chain = algorithm.OptionChains.get(symbol, None)
        if not option_chain:
            return 0
        at_the_money = sorted(option_chain, key=lambda x: abs(x.Strike - x.UnderlyingLastPrice))[:1]
        return sum(o.ImpliedVolatility for o in at_the_money) / len(at_the_money) if at_the_money else 0

class EqualWeightingPortfolioConstructionModel(PortfolioConstructionModel):
    def CreateTargets(self, algorithm, insights):
        targets = []
        for insight in insights:
            if insight.Direction == InsightDirection.Flat:
                targets.append(PortfolioTarget.Percent(algorithm.Portfolio[insight.Symbol].Symbol, 0.02))
        return targets

class ImmediateExecutionModel(ExecutionModel):
    def Execute(self, algorithm, targets):
        for target in targets:
            symbol = target.Symbol
            if symbol.SecurityType == SecurityType.Option:
                algorithm.MarketOrder(symbol, target.Quantity)
