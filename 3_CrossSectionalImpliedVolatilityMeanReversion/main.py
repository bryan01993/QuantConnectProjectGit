# The code below modifies the scheduling portion
# to avoid the 'Unable to locate next market open' error.
# We also ensure the date range is aligned with valid SPY data.

from AlgorithmImports import *
from PropietaryCode.decorators import monitor_execution
from PropietaryCode.risk_management import KellyCriterion


class CrossSectionalImpliedVolatilityMeanReversion(QCAlgorithm):

    def Initialize(self):
        # 1) Basic QC Setup
        # Set a date range where SPY definitely trades. For example:
        self.SetStartDate(2021, 1, 1)
        self.SetEndDate(2021, 12, 31)
        self.SetCash(100000)

        # 2) Universe Settings
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)

        # 3) Instead of scheduling on SPY, schedule on the 'market-hours'
        #    of the default US Equities exchange via self.TimeRules.
        #    Or confirm SPY is indeed in the data set.
        #    If we want a daily trigger at 9:35am local time, we can do:
        #    self.TimeRules.AfterMarketOpen(Symbols.SPY, 5) # e.g.

        # But we must ensure SPY is actually added or the system won't find it.
        # Let's add SPY manually to ensure we have that data.
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol

        self.Schedule.On(
            self.DateRules.EveryDay(self.spy),
            self.TimeRules.AfterMarketOpen(self.spy, 30),
            self.RebalanceDaily
        )

        # 4) Instantiate an existing KellyCriterion class
        self.kelly = KellyCriterion(factor=0.5, period=30)

        # 5) Track current short-vol & long-vol sets
        self.highIVSymbols = []
        self.lowIVSymbols = []

    @monitor_execution
    def CoarseSelectionFunction(self, coarse):
        filtered = [c for c in coarse
                    if c.Price > 10
                    and c.DollarVolume > 5e6
                    and c.HasFundamentalData]
        top = sorted(filtered, key=lambda c: c.DollarVolume, reverse=True)[:200]
        return [x.Symbol for x in top]

    @monitor_execution
    def FineSelectionFunction(self, fine):
        return [f.Symbol for f in fine]

    @monitor_execution
    def RebalanceDaily(self):
        candidateOptions = self.SelectLiquidOptions()
        ivRanks = self.ComputeIVRankings(candidateOptions)

        topN = 5
        shortVolList = sorted(ivRanks, key=lambda x: x[1], reverse=True)[:topN]
        longVolList = sorted(ivRanks, key=lambda x: x[1])[:topN]
        self.highIVSymbols = [x[0] for x in shortVolList]
        self.lowIVSymbols = [x[0] for x in longVolList]

        historicalReturns = self.GetRecentDailyReturns()
        self.kelly.Update(historicalReturns)
        kellyFraction = self.kelly.GetFraction()

        self.LiquidateRemovedPositions(shortVolList, longVolList)
        self.BuildDeltaNeutralPositions(shortVolList, longVolList, kellyFraction)

    def SelectLiquidOptions(self):
        pass

    def ComputeIVRankings(self, candidateOptions):
        pass

    def LiquidateRemovedPositions(self, shortVolList, longVolList):
        pass

    def BuildDeltaNeutralPositions(self, shortVolList, longVolList, kellyFraction):
        pass

    def GetRecentDailyReturns(self):
        pass
