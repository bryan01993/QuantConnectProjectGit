# The code below modifies the scheduling portion
# to avoid the 'Unable to locate next market open' error.
# We also ensure the date range is aligned with valid SPY data.
# Additionally, we handle the case where Coarse returns an empty list,
# and set the InteractiveBrokers fee model.

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

        # Use InteractiveBrokers fee model for realistic transaction costs
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin)
        # Alternatively, we can set a security initializer if needed:
        # self.SetSecurityInitializer(lambda security: security.SetFeeModel(InteractiveBrokersFeeModel()))

        # 2) Universe Settings
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)

        # 3) Instead of scheduling on SPY, schedule on the 'market-hours'
        #    of the default US Equities exchange via self.TimeRules.
        #    Or confirm SPY is indeed in the data set.
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
        # Filter out low-priced, illiquid equities
        filtered = [c for c in coarse
                    if c.Price > 10
                    and c.DollarVolume > 5e6
                    and c.HasFundamentalData]
        # Sort by dollar volume descending and pick top 200
        top = sorted(filtered, key=lambda c: c.DollarVolume, reverse=True)[:200]
        # Return the symbol list
        # If top is empty, this function returns [], which can cause issues.
        # We can debug-log or just return.
        if not top:
            self.Debug("CoarseSelectionFunction returned empty list. Possibly no data yet.")
            return []
        return [x.Symbol for x in top]

    @monitor_execution
    def FineSelectionFunction(self, fine):
        # Just pass them all for final selection
        if not fine:
            self.Debug("FineSelectionFunction found no securities.")
            return []
        return [f.Symbol for f in fine]

    @monitor_execution
    def RebalanceDaily(self):
        candidateOptions = self.SelectLiquidOptions()
        if not candidateOptions:
            self.Debug("SelectLiquidOptions returned no candidates; skipping rebalancing.")
            return

        ivRanks = self.ComputeIVRankings(candidateOptions)
        if not ivRanks:
            self.Debug("ComputeIVRankings returned empty; skipping rebalancing.")
            return

        topN = 5
        # Sort by rank desc for shortVol, ascending for longVol
        shortVolList = sorted(ivRanks, key=lambda x: x[1], reverse=True)[:topN]
        longVolList = sorted(ivRanks, key=lambda x: x[1])[:topN]
        if not shortVolList and not longVolList:
            self.Debug("No valid IV rank candidates. Skipping.")
            return

        self.highIVSymbols = [x[0] for x in shortVolList]
        self.lowIVSymbols = [x[0] for x in longVolList]

        historicalReturns = self.GetRecentDailyReturns()
        self.kelly.Update(historicalReturns)
        kellyFraction = self.kelly.GetFraction()

        self.LiquidateRemovedPositions(shortVolList, longVolList)
        self.BuildDeltaNeutralPositions(shortVolList, longVolList, kellyFraction)

    def SelectLiquidOptions(self):
        # TODO: Filter for liquidity, e.g. OI, narrow spreads, near money.
        return []

    def ComputeIVRankings(self, candidateOptions):
        # TODO: Return a list of tuples (symbol, iv_rank)
        return []

    def LiquidateRemovedPositions(self, shortVolList, longVolList):
        # TODO: Liquidate if not in shortVolList or longVolList.
        pass

    def BuildDeltaNeutralPositions(self, shortVolList, longVolList, kellyFraction):
        # TODO: Build delta-neutral positions.
        pass

    def GetRecentDailyReturns(self):
        # TODO: Return daily returns of the strategy or portfolio.
        return []
