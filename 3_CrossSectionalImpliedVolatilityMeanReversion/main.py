from AlgorithmImports import *
from PropietaryCode.decorators import monitor_execution, measure_memory_usage
from PropietaryCode.risk_management import KellyCriterion
from datetime import timedelta
import math
import random
import numpy as np

class CrossSectionalImpliedVolatilityMeanReversion(QCAlgorithm):

    def Initialize(self):
        # 1) Basic QC Setup
        self.SetStartDate(*map(int, self.GetParameter("exec.start_date").split('-')))  # Set a fixed start date
        self.SetEndDate(*map(int, self.GetParameter("exec.end_date").split('-')))   # Set a fixed end date
        # Note: self.GetParameter always returns a string, so we convert to float
        initial_amount = float(self.GetParameter("exec.initial_amount"))
        self.SetCash(initial_amount)
        self.Debug(f"initial_amount = {initial_amount} with type {type(initial_amount)}")

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
        self.kelly = KellyCriterion(
            factor=float(self.GetParameter("risk.kelly.factor")),
            period=int(self.GetParameter("risk.kelly.period"))
        )

        # 6) short-vol & long-vol lists
        self.highIVSymbols = []
        self.lowIVSymbols  = []

        # We'll store the slice-based OptionChains in OnData, keyed by the OPTION symbol
        # Instead of using underlying symbols as the dictionary key.
        self.latestOptionChains = {}

        # We'll track the underlying equity symbols that pass Universe selection
        # so we can do AddOption(...) for them.
        self.underlyingSymbols = set()
        # Create a dictionary for rolling windows of daily returns
        self.rollingReturns = {}

    def OnSecuritiesChanged(self, changes):
        self.Log("OnSecuritiesChanged event")
        for sec in changes.AddedSecurities:
            if sec.Symbol.SecurityType == SecurityType.Equity:
                self.Log(f"OnSecuritiesChanged: Adding Option for {sec.Symbol}")
                option = self.AddOption(sec.Symbol.Value, Resolution.Daily)
                option.SetFilter(-2, +2, timedelta(0), timedelta(60))
                option.PriceModel = OptionPriceModels.CrankNicolsonFD()

                # Create a rolling window of size 30 for each newly added equity
                if sec.Symbol not in self.rollingReturns:
                    self.rollingReturns[sec.Symbol] = RollingWindow[float](30)

        for sec in changes.RemovedSecurities:
            self.Log(f"Removed security: {sec.Symbol}")
            if sec.Symbol in self.rollingReturns:
                del self.rollingReturns[sec.Symbol]

    def OnData(self, slice):
        # Keep reference to slice-based OptionChains dictionary, but these chains are keyed by the option Symbol
        # i.e. slice.OptionChains[optionSymbol]
        self.latestOptionChains = dict(slice.OptionChains)

        # Update rolling returns for each equity
        for symbol in self.rollingReturns.keys():
            if symbol in slice.Bars:
                bar = slice.Bars[symbol]
                if bar.Open != 0:
                    dailyReturn = bar.Close / bar.Open - 1.0
                    self.rollingReturns[symbol].Add(dailyReturn)

    def CoarseSelectionFunction(self, coarse):
        filtered = [c for c in coarse
                    if c.Price > int(self.GetParameter("univ.coarse.min_price"))
                    and c.Price < int(self.GetParameter("univ.coarse.max_price"))
                    and c.DollarVolume > int(self.GetParameter("univ.coarse.dollar_volume"))
                    and c.HasFundamentalData]
        top = sorted(filtered, key=lambda c: c.DollarVolume, reverse=True)[:int(self.GetParameter("univ.coarse.final_cut"))]
        if not top:
            self.Log("CoarseSelectionFunction returned empty.")
            return []
        return [x.Symbol for x in top]

    def FineSelectionFunction(self, fine):
        if not fine:
            self.Log("FineSelectionFunction found no securities.")
            return []
        # We'll store these equity symbols so we can AddOption for them
        self.underlyingSymbols = set([f.Symbol for f in fine])
        return list(self.underlyingSymbols)

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

    def SelectLiquidOptions(self):
        self.Log("SelectLiquidOptions: Using slice-based OptionChains.")
        results = []
        if not self.latestOptionChains:
            self.Log("SelectLiquidOptions: self.latestOptionChains is empty.")
            return results

        # self.latestOptionChains is keyed by option Symbol, e.g. Symbol("SPY 240119C00475000")
        # We iterate over them:
        for optSymbol, chain in self.latestOptionChains.items():
            # optSymbol is an Option Symbol
            # chain is the OptionChain object
            if chain is None:
                continue
            if (chain.Underlying is None) or (chain.Underlying.Price <= 0):
                continue

            contracts = [o for o in chain
                         if (o.Expiry - self.Time).days < int(self.GetParameter("algo.option.max_exp_days"))
                            and abs(o.Strike - chain.Underlying.Price)/chain.Underlying.Price < 0.10
                            and o.OpenInterest > int(self.GetParameter("algo.option.min_open_inter"))]
            if not contracts:
                continue
            bestContract = sorted(contracts, key=lambda x: x.OpenInterest, reverse=True)[0]
            results.append(bestContract.Symbol)

        self.Log(f"SelectLiquidOptions: Found {len(results)} option(s).")
        return results

    def ComputeIVRankings(self, candidateOptions):
        self.Log("ComputeIVRankings: Using contract.Greeks.ImpliedVolatility from the chain.")
        ivRankList = []

        # candidateOptions is a list of contract symbols
        for optSymbol in candidateOptions:
            # We'll retrieve the chain from self.latestOptionChains by the *option* Symbol
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

            # We'll compute historical vol from the underlying's RollingWindow
            underlyingSymbol = contract.Underlying.Symbol
            histVol = self.ComputeHistoricalVol(underlyingSymbol)
            rank = currentIV - histVol
            ivRankList.append((optSymbol, rank))

        self.Log(f"ComputeIVRankings: Returning {len(ivRankList)} rank entries.")
        return ivRankList

    def ComputeHistoricalVol(self, underlyingSymbol):
        """
        Compute the annualized historical volatility from the rolling
        daily returns window: std(returns) * sqrt(252).
        Fallback if insufficient data or no rolling window.
        """
        if underlyingSymbol not in self.rollingReturns:
            return 0.25  # fallback

        window = self.rollingReturns[underlyingSymbol]
        if not window.IsReady:
            # Not enough data in the rolling window
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
        self.Log("BuildDeltaNeutralPositions: Delta hedge logic not yet implemented.")

    def GetRecentDailyReturns(self):
        self.Log("GetRecentDailyReturns: Starting placeholder logic.")
        return [random.uniform(-0.01, 0.01) for _ in range(30)]
