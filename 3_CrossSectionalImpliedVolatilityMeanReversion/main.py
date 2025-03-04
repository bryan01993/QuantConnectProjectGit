from AlgorithmImports import *
from PropietaryCode.decorators import monitor_execution, measure_memory_usage
from PropietaryCode.risk_management import KellyCriterion
from datetime import timedelta, datetime
import math
import random
import numpy as np

class CrossSectionalImpliedVolatilityMeanReversion(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(*map(int, self.GetParameter("exec.start_date").split('-')))
        self.SetEndDate(*map(int, self.GetParameter("exec.end_date").split('-')))
        initial_amount = float(self.GetParameter("exec.initial_amount"))
        self.SetCash(initial_amount)
        self.Debug(f"initial_amount = {initial_amount} with type {type(initial_amount)}")

        self.UniverseSettings.Resolution = Resolution.Daily

        # Track current universe selection
        self.currentUniverse = []
        # Only refresh once a week (Monday open)
        self.nextUniverseSelectionTime = datetime.min

        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)

        # Instead of daily, do a weekly schedule for Rebalance
        self.Schedule.On(
            self.DateRules.WeekStart("SPY"),
            self.TimeRules.AfterMarketOpen("SPY", 30),
            self.RebalanceWeekly
        )

        self.kelly = KellyCriterion(
            factor=float(self.GetParameter("risk.kelly.factor")),
            period=int(self.GetParameter("risk.kelly.period"))
        )

        self.highIVSymbols = []
        self.lowIVSymbols = []
        self.latestOptionChains = {}
        self.underlyingSymbols = set()
        self.rollingReturns = {}

        # Dictionary to track arrival times for each security
        self.universeArrivalTimes = {}

    def OnSecuritiesChanged(self, changes):
        self.Log("OnSecuritiesChanged event")

        # Process additions
        for sec in changes.AddedSecurities:
            if sec.Symbol.SecurityType == SecurityType.Equity:
                self.Log(f"OnSecuritiesChanged: Adding Option for {sec.Symbol}")
                option = self.AddOption(sec.Symbol.Value, Resolution.Daily)
                option.SetFilter(-2, +2, timedelta(0), timedelta(65))  # up to 65 days expiry
                option.PriceModel = OptionPriceModels.CrankNicolsonFD()

                self.universeArrivalTimes[sec.Symbol] = self.Time  # store arrival time

                if sec.Symbol not in self.rollingReturns:
                    self.rollingReturns[sec.Symbol] = RollingWindow[float](30)

        # Process removals
        for sec in changes.RemovedSecurities:
            arrived = self.universeArrivalTimes.pop(sec.Symbol, self.Time)
            timeInUniverse = (self.Time - arrived).days
            self.Log(f"Removed security: {sec.Symbol} after {timeInUniverse} day(s) in universe.")

            if sec.Symbol in self.rollingReturns:
                del self.rollingReturns[sec.Symbol]

    def OnData(self, slice):
        self.latestOptionChains = dict(slice.OptionChains)
        self.Debug(f"OnData: slice.OptionChains count = {len(self.latestOptionChains)}")

        # Update rolling returns if we have daily Bars
        for symbol in self.rollingReturns.keys():
            if symbol in slice.Bars:
                bar = slice.Bars[symbol]
                if bar.Open != 0:
                    dailyReturn = bar.Close / bar.Open - 1.0
                    self.rollingReturns[symbol].Add(dailyReturn)

    # WEEKLY Universe selection:
    def CoarseSelectionFunction(self, coarse):
        # Only refresh if we are past the nextUniverseSelectionTime
        if self.Time < self.nextUniverseSelectionTime:
            # return the unchanged universe
            return self.currentUniverse

        # Otherwise, we do our standard coarse selection
        self.nextUniverseSelectionTime = self.Time + timedelta(days=7)  # next week
        coarse_list = list(coarse)
        min_price = int(self.GetParameter("univ.coarse.min_price"))
        max_price = int(self.GetParameter("univ.coarse.max_price"))
        min_vol   = int(self.GetParameter("univ.coarse.dollar_volume"))
        final_cut = int(self.GetParameter("univ.coarse.final_cut"))

        self.Log(f"Coarse count = {len(coarse_list)}. min_price={min_price}, max_price={max_price}, "
                 f"min_vol={min_vol}, final_cut={final_cut}")

        filtered = [c for c in coarse_list
                    if c.Price > min_price
                    and c.Price < max_price
                    and c.DollarVolume > min_vol
                    and c.HasFundamentalData]

        self.Log(f"CoarseSelectionFunction: after filter has {len(filtered)} left")

        top = sorted(filtered, key=lambda c: c.DollarVolume, reverse=True)[:final_cut]
        self.Log(f"CoarseSelectionFunction: returning top {len(top)} by dollar volume")

        if not top:
            self.Log("CoarseSelectionFunction returned empty.")
            self.currentUniverse = []
            return []

        # store in self.currentUniverse for subsequent days
        self.currentUniverse = [x.Symbol for x in top]
        return self.currentUniverse

    def FineSelectionFunction(self, fine):
        fine_list = list(fine)
        self.Log(f"FineSelectionFunction: got {len(fine_list)} items in fine filter")
        if not fine_list:
            self.Log("FineSelectionFunction found no securities.")
            return []

        # For demonstration let's just keep them all. Or we can do further filtering.
        self.underlyingSymbols = set([f.Symbol for f in fine_list])
        self.Log(f"FineSelectionFunction returning {len(self.underlyingSymbols)} symbol(s).")
        return list(self.underlyingSymbols)

    # We have renamed this to RebalanceWeekly
    def RebalanceWeekly(self):
        self.Debug("=== RebalanceWeekly triggered ===")
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
        self.Log(f"RebalanceWeekly: kellyFraction = {kellyFraction}")

        self.LiquidateRemovedPositions(shortVolList, longVolList)
        self.BuildDeltaNeutralPositions(shortVolList, longVolList, kellyFraction)

    def SelectLiquidOptions(self):
        self.Log("SelectLiquidOptions: Using slice-based OptionChains.")
        results = []
        if not self.latestOptionChains:
            self.Log("SelectLiquidOptions: self.latestOptionChains is empty.")
            return results

        max_exp = int(self.GetParameter("algo.option.max_exp_days"))
        min_oi  = int(self.GetParameter("algo.option.min_open_inter"))
        self.Log(f"SelectLiquidOptions: checking for expiry < {max_exp} days, open interest > {min_oi}")

        for optSymbol, chain in self.latestOptionChains.items():
            if chain is None:
                continue
            if (chain.Underlying is None) or (chain.Underlying.Price <= 0):
                continue

            contracts_list = list(chain)
            self.Debug(f" - OptionChain {optSymbol.Underlying.Value} has {len(contracts_list)} contracts total.")

            candidate_contracts = []
            for o in chain:
                expiryDays = (o.Expiry - self.Time).days
                strikePerc = abs(o.Strike - chain.Underlying.Price) / chain.Underlying.Price
                if expiryDays < max_exp and strikePerc < 0.10 and o.OpenInterest > min_oi:
                    candidate_contracts.append(o)

            if not candidate_contracts:
                self.Debug(f"   chain for {optSymbol.Underlying.Value} - no contracts pass the filter.")
                continue

            bestContract = sorted(candidate_contracts, key=lambda x: x.OpenInterest, reverse=True)[0]
            results.append(bestContract.Symbol)

        self.Log(f"SelectLiquidOptions: Found {len(results)} option(s).")
        return results

    def ComputeIVRankings(self, candidateOptions):
        self.Log("ComputeIVRankings: Using contract.Greeks.ImpliedVolatility from the chain.")
        ivRankList = []
        for optSymbol in candidateOptions:
            chain = self.latestOptionChains.get(optSymbol, None)
            if chain is None:
                self.Log(f"ComputeIVRankings: No chain found for {optSymbol.Underlying.Value}.")
                continue

            contract = next((c for c in chain if c.Symbol == optSymbol), None)
            if not contract:
                self.Log(f"ComputeIVRankings: No matching contract for {optSymbol}.")
                continue

            if contract.Greeks is None:
                self.Log(f"ComputeIVRankings: contract.Greeks is None for {optSymbol}.")
                continue

            currentIV = contract.Greeks.ImpliedVolatility
            if currentIV is None or currentIV <= 0:
                currentIV = 0.30

            underlyingSymbol = contract.Underlying.Symbol
            histVol = self.ComputeHistoricalVol(underlyingSymbol)
            rank = currentIV - histVol
            ivRankList.append((optSymbol, rank))

        self.Log(f"ComputeIVRankings: Returning {len(ivRankList)} rank entries.")
        return ivRankList

    def ComputeHistoricalVol(self, underlyingSymbol):
        if underlyingSymbol not in self.rollingReturns:
            return 0.25

        window = self.rollingReturns[underlyingSymbol]
        if not window.IsReady:
            return 0.25

        returnsArray = np.array(list(window))
        stdev = np.std(returnsArray, ddof=1)
        hv = stdev * math.sqrt(252)
        if hv <= 0:
            hv = 0.25
        return hv

    def LiquidateRemovedPositions(self, shortVolList, longVolList):
        self.Log("LiquidateRemovedPositions: Checking portfolio...")
        keepSymbols = set([x[0] for x in shortVolList] + [x[0] for x in longVolList])
        for kvp in self.Portfolio:
            holding = kvp.Value
            if holding.Invested and holding.Symbol not in keepSymbols:
                self.Log(f"LiquidateRemovedPositions: Liquidating {holding.Symbol}")
                self.Liquidate(holding.Symbol)

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
        self.Log("BuildDeltaNeutralPositions: (Simple) Delta hedge logic not implemented yet.")

    def GetRecentDailyReturns(self):
        self.Log("GetRecentDailyReturns: Starting placeholder logic.")
        return [random.uniform(-0.01, 0.01) for _ in range(30)]
