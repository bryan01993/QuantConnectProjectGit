# Statistical Arbitrage Options Pair Trading Script
from AlgorithmImports import *
from datetime import timedelta
import pandas as pd

class StatisticalArbitrageOptionsPair(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        a_dataframe = pd.DataFrame({"Column1": [1, 2, 3], "Column2": [4, 5, 6]})
        a_dataframe.to_csv('output.csv', index=False)
        self.SetEndDate(2023, 1, 1)
        self.SetCash(100000)

        self.Log("Initializing the strategy...")

        self.symbols = self.SelectSectorSymbols(self.GetParameter("sector"))
        for symbol in self.symbols:
            equity = self.AddEquity(symbol, Resolution.Daily)
            option = self.AddOption(symbol, Resolution.Daily)
            option.SetFilter(self.UniverseFilter)

        self.SetBenchmark("SPY")

        self.SetUniverseSelection(ManualUniverseSelectionModel(self.symbols))
        self.SetAlpha(VolatilityDifferenceAlphaModel())
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())
        self.SetExecution(ImmediateExecutionModel())
        self.SetRiskManagement(MaximumDrawdownPercentPerSecurity(0.05))

        self.Debug(f"Selected symbols: {self.symbols}")

    def SelectSectorSymbols(self, sector):
        sector_map = {
            "Technology": ["AAPL", "MSFT", "GOOG"],
            "Finance": ["JPM", "BAC", "GS"],
            "Healthcare": ["JNJ", "PFE", "MRK"]
        }
        return sector_map.get(sector, [])

    def UniverseFilter(self, universe):
        return universe.Strikes(-5, 5).Expiration(10, 45)

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

            algorithm.Log(f"Symbol: {symbol}, Realized Vol: {realized_vol}, Implied Vol: {implied_vol}")

            if implied_vol > 0 and realized_vol > 0 and (implied_vol - realized_vol > self.threshold):
                insights.append(Insight.Price(symbol, timedelta(days=30), InsightDirection.Flat))
                algorithm.Log(f"Generated insight for symbol {symbol}")

        return insights

    def OnSecuritiesChanged(self, algorithm, changes):
        for security in changes.AddedSecurities:
            self.volatility_data[security.Symbol] = RollingWindow[float](self.lookback)
            algorithm.Log(f"Added security: {security.Symbol}")
        for security in changes.RemovedSecurities:
            self.volatility_data.pop(security.Symbol, None)
            algorithm.Log(f"Removed security: {security.Symbol}")

    def CalculateRealizedVolatility(self, symbol, algorithm):
        history = algorithm.History(symbol, self.lookback, Resolution.Daily)
        if history.empty or len(history) < self.lookback:
            algorithm.Log(f"Insufficient history for symbol {symbol}")
            return 0
        returns = history["close"].pct_change().dropna()
        return returns.std() * (252 ** 0.5)

    def GetImpliedVolatility(self, symbol, algorithm):
        option_chains = getattr(algorithm, 'OptionChains', None)
        if not option_chains or symbol not in option_chains:
            algorithm.Log(f"No option chain available for symbol {symbol}")
            return 0
        option_chain = option_chains[symbol]
        if not option_chain:
            algorithm.Log(f"Empty option chain for symbol {symbol}")
            return 0
        at_the_money = sorted(option_chain, key=lambda x: abs(x.Strike - x.UnderlyingLastPrice))[:1]
        implied_vol = sum(o.ImpliedVolatility for o in at_the_money) / len(at_the_money) if at_the_money else 0
        algorithm.Log(f"Symbol: {symbol}, At-the-money Implied Volatility: {implied_vol}")
        return implied_vol

class EqualWeightingPortfolioConstructionModel(PortfolioConstructionModel):
    def CreateTargets(self, algorithm, insights):
        targets = []
        for insight in insights:
            if insight.Direction == InsightDirection.Flat:
                targets.append(PortfolioTarget.Percent(algorithm.Portfolio[insight.Symbol].Symbol, 0.02))
                algorithm.Log(f"Creating target for symbol {insight.Symbol}")
        return targets

class ImmediateExecutionModel(ExecutionModel):
    def Execute(self, algorithm, targets):
        for target in targets:
            symbol = target.Symbol
            if symbol.SecurityType == SecurityType.Option:
                algorithm.Log(f"Executing market order for symbol {symbol} with quantity {target.Quantity}")
                algorithm.MarketOrder(symbol, target.Quantity)
