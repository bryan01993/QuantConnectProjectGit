from AlgorithmImports import *
from PropietaryCode.decorators import monitor_execution
from PropietaryCode.memory_decorator import  measure_memory_usage
from PropietaryCode.risk_management import KellyCriterion
from datetime import timedelta
import random

class CrossSectionalImpliedVolatilityMeanReversion(QCAlgorithm):

    def Initialize(self):
        # 1) Basic QC Setup
        self.SetStartDate(2021, 1, 1)
        self.SetEndDate(2024, 12, 31)
        self.SetCash(100000)

        # 2) Universe Settings
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)

        # 3) Possibly set your brokerage model
        # self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin)

        # 4) Add SPY to anchor the schedule
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.Schedule.On(
            self.DateRules.EveryDay(self.spy),
            self.TimeRules.AfterMarketOpen(self.spy, 30),
            self.RebalanceDaily
        )

        # 5) KellyCriterion for sizing
        self.kelly = KellyCriterion(factor=0.5, period=30)

        # 6) short-vol & long-vol lists
        self.highIVSymbols = []
        self.lowIVSymbols  = []

        # We'll store the slice-based OptionChains in OnData
        self.latestOptionChains = {}

        # We'll track the underlying equity symbols that pass Universe selection
        # so we can do AddOption(...) for them.
        self.underlyingSymbols = set()

    # @measure_memory_usage
    #@monitor_execution
    def OnSecuritiesChanged(self, changes):
        self.Log("OnSecuritiesChanged event")
        # For each equity security added, also add Option data
        for sec in changes.AddedSecurities:
            if sec.Symbol.SecurityType == SecurityType.Equity:
                self.Log(f"OnSecuritiesChanged: Adding Option for {sec.Symbol}")
                option = self.AddOption(sec.Symbol.Value, Resolution.Daily)
                # Option filter, e.g. near money, expiry < 60 days
                optional: option.SetFilter(-2, +2, timedelta(0), timedelta(60))
        # For removed securities, optionally remove or do something
        for sec in changes.RemovedSecurities:
            self.Log(f"Removed security: {sec.Symbol}")
            # Possibly remove or liquidate positions

    def OnData(self, slice):
        # Keep reference to slice-based OptionChains dictionary
        self.latestOptionChains = slice.OptionChains

    # @measure_memory_usage
    #@monitor_execution
    def CoarseSelectionFunction(self, coarse):
        filtered = [c for c in coarse
                    if c.Price > 10
                    and c.DollarVolume > 5e6
                    and c.HasFundamentalData]
        top = sorted(filtered, key=lambda c: c.DollarVolume, reverse=True)[:10]
        if not top:
            self.Log("CoarseSelectionFunction returned empty.")
            return []
        return [x.Symbol for x in top]

    #@monitor_execution
    def FineSelectionFunction(self, fine):
        if not fine:
            self.Log("FineSelectionFunction found no securities.")
            return []
        # We'll store these equity symbols so we can AddOption for them
        self.underlyingSymbols = set([f.Symbol for f in fine])
        return list(self.underlyingSymbols)

    #@monitor_execution
    def RebalanceDaily(self):
        candidateOptions = self.SelectLiquidOptions()
        if not candidateOptions:
            self.Debug("SelectLiquidOptions returned no candidates; skipping.")
            return

        ivRanks = self.ComputeIVRankings(candidateOptions)
        if not ivRanks:
            self.Debug("ComputeIVRankings returned empty; skipping.")
            return

        topN = 5
        shortVolList = sorted(ivRanks, key=lambda x: x[1], reverse=True)[:topN]
        longVolList  = sorted(ivRanks, key=lambda x: x[1])[:topN]
        if not shortVolList and not longVolList:
            self.Debug("No valid IV rank candidates. Skipping.")
            return

        self.highIVSymbols = [x[0] for x in shortVolList]
        self.lowIVSymbols  = [x[0] for x in longVolList]

        historicalReturns = self.GetRecentDailyReturns()
        self.kelly.Update(historicalReturns)
        kellyFraction = self.kelly.GetFraction()
        self.Log(f"RebalanceDaily: kellyFraction = {kellyFraction}")

        self.LiquidateRemovedPositions(shortVolList, longVolList)
        self.BuildDeltaNeutralPositions(shortVolList, longVolList, kellyFraction)

    #@monitor_execution
    def SelectLiquidOptions(self):
        self.Log("SelectLiquidOptions: Using slice-based OptionChains.")
        results = []
        if not self.latestOptionChains:
            self.Log("SelectLiquidOptions: self.latestOptionChains is empty.")
            return results

        for symbol, chain in self.latestOptionChains.items():
            # Filter for near expiry (< 45 days), near the money (±5%), decent OI
            contracts = [o for o in chain
                         if (o.Expiry - self.Time).days < 45
                            and abs(o.Strike - chain.Underlying.Price)/chain.Underlying.Price < 0.05
                            and o.OpenInterest > 100]
            if not contracts:
                continue
            bestContract = sorted(contracts, key=lambda x: x.OpenInterest, reverse=True)[0]
            results.append(bestContract.Symbol)

        self.Log(f"SelectLiquidOptions: Found {len(results)} option(s).")
        return results

    #@monitor_execution
    def ComputeIVRankings(self, candidateOptions):
        self.Log("ComputeIVRankings: Starting placeholder logic.")
        random.seed(42)
        ivRankList = []
        for sym in candidateOptions:
            currentIV = random.uniform(0.2, 0.6)
            historicalMeanIV = 0.3
            rank = currentIV - historicalMeanIV
            ivRankList.append((sym, rank))
        self.Log(f"ComputeIVRankings: Returning {len(ivRankList)} rank entries.")
        return ivRankList

    #@monitor_execution
    def LiquidateRemovedPositions(self, shortVolList, longVolList):
        self.Log("LiquidateRemovedPositions: Checking portfolio...")
        keepSymbols = set([x[0] for x in shortVolList] + [x[0] for x in longVolList])
        for kvp in self.Portfolio:
            holding = kvp.Value
            if holding.Invested and holding.Symbol not in keepSymbols:
                self.Log(f"LiquidateRemovedPositions: Liquidating {holding.Symbol}")
                self.Liquidate(holding.Symbol)

    # #@monitor_execution
    def BuildDeltaNeutralPositions(self, shortVolList, longVolList, kellyFraction):
        self.Log("BuildDeltaNeutralPositions: Adjusting positions for delta neutrality.")
        for sym, rank in shortVolList:
            if not self.Portfolio[sym].Invested:
                self.Log(f"ShortVol {sym.Value} rank={rank:.3f}. Opening short call position.")
                self.MarketOrder(sym, -1)
        for sym, rank in longVolList:
            if not self.Portfolio[sym].Invested:
                self.Log(f"LongVol {sym.Value} rank={rank:.3f}. Opening long call position.")
                self.MarketOrder(sym, 1)
        self.Log("BuildDeltaNeutralPositions: Delta hedge logic not yet implemented.")

    #@monitor_execution
    def GetRecentDailyReturns(self):
        self.Log("GetRecentDailyReturns: Starting placeholder logic.")
        return [random.uniform(-0.01, 0.01) for _ in range(30)]
