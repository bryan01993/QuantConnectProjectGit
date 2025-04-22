from AlgorithmImports import *
from PropietaryCode.decorators import monitor_execution, measure_memory_usage
from PropietaryCode.risk_management import KellyCriterion
from datetime import timedelta
import random
import System
import gc
import sys


class CrossSectionalImpliedVolatilityMeanReversion(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(*map(int, self.GetParameter("exec.start_date").split('-')))
        self.SetEndDate(*map(int, self.GetParameter("exec.end_date").split('-')))
        self.SetCash(self.GetParameter("exec.initial_amount"))
        self.Debug(
            f"initial_amount = {self.GetParameter('exec.initial_amount')} with type {type(self.GetParameter('exec.initial_amount'))}")

        self.UniverseSettings.Resolution = Resolution.HOUR
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage)

        self.spy = self.AddEquity("SPY", Resolution.HOUR).Symbol
        # Scheduling removed. Rebalance will be triggered in OnData if ready

        self.kelly = KellyCriterion(factor=float(self.GetParameter("risk.kelly.factor")),
                                    period=int(self.GetParameter("risk.kelly.period")))

        self.SetWarmUp(timedelta(days=35))  # Only 35 days
        self.highIVSymbols = []
        self.lowIVSymbols = []
        self.latestOptionChains = {}
        self.underlyingSymbols = set()
        self.iv_history = {}  # Store implied volatility history per symbol
        self.lastRebalanceDate = None

    def OnSecuritiesChanged(self, changes):
        # self.Debug(f"OnSecuritiesChanged: {len(changes.AddedSecurities)} added, {len(changes.RemovedSecurities)} removed")
        for sec in changes.AddedSecurities:
            if sec.Symbol.SecurityType == SecurityType.Equity:
                # self.Debug(f"Adding Option for: {sec.Symbol.Value}")
                option = self.AddOption(sec.Symbol.Value, Resolution.Daily)
                option.SetFilter(-2, +2,
                                 timedelta(int(self.GetParameter("algo.option.min_exp_days"))),
                                 timedelta(int(self.GetParameter("algo.option.max_exp_days"))))

        for sec in changes.RemovedSecurities:
            # if sec.Symbol.SecurityType == SecurityType.Equity:
            self.Debug(f"Removing Security: {sec.Symbol.Value}")
                # self.RemoveSecurity(sec.Symbol)

    def OnData(self, slice):
        self.latestOptionChains.clear()
        self.latestOptionChains.update(slice.OptionChains)
        # Only trigger RebalanceDaily when option chains are present and it's around 10:00 AM

        if (self.Time.hour >= 10 and self.Time.date() != self.lastRebalanceDate
                and self.latestOptionChains):
            self.Debug(f"Triggering RebalanceDaily at {self.Time} with {len(self.latestOptionChains)} chains.")
            self.RebalanceDaily()
            self.lastRebalanceDate = self.Time.date()
        elif (self.Time.hour >= 15 and self.latestOptionChains):
            self.Debug(f"Triggering RebalanceDaily at {self.Time} with {len(self.latestOptionChains)} chains.")
            self.RebalanceDaily()
            self.lastRebalanceDate = self.Time.date()

    def CoarseSelectionFunction(self, coarse):
        min_price = int(self.GetParameter("univ.coarse.min_price"))
        max_price = int(self.GetParameter("univ.coarse.max_price"))
        dollar_volume = int(self.GetParameter("univ.coarse.dollar_volume"))
        final_cut = int(self.GetParameter("univ.coarse.final_cut"))

        filtered = (c for c in coarse if
                    min_price < c.Price < max_price and c.DollarVolume > dollar_volume and c.HasFundamentalData)
        top = sorted(filtered, key=lambda c: c.DollarVolume, reverse=True)[:final_cut]
        # self.Debug(f"CoarseSelectionFunction selected {len(top)} symbols.")
        return [x.Symbol for x in top] if top else []

    def FineSelectionFunction(self, fine):
        if not fine:
            return []
        self.underlyingSymbols = {f.Symbol for f in fine}
        return list(set([x.Symbol for x in fine]) - set(self.Securities.Keys))

    def RebalanceDaily(self):
        # Log non-tradable securities with context
        self.non_tradable_details = []
        self.tradable_details = []
        for symbol, sec in self.Securities.items():
            if not sec.IsTradable:
                detail = f"{symbol.Value} | Tradable: {sec.IsTradable}, Delisted: {sec.IsDelisted}, Price: {sec.Price}, Holdings: {sec.Holdings.Quantity}, ExtendedHours: {sec.IsExtendedMarketHours}, FillForward: {sec.IsFillDataForward}, Type: {sec.Type}"
                self.non_tradable_details.append(detail)
        for symbol, sec in self.Securities.items():
            if sec.IsTradable:
                tradable_detail = f"{symbol.Value} | Tradable: {sec.IsTradable}, Delisted: {sec.IsDelisted}, Price: {sec.Price}, Holdings: {sec.Holdings.Quantity}, ExtendedHours: {sec.IsExtendedMarketHours}, FillForward: {sec.IsFillDataForward}, Type: {sec.Type}"
                self.tradable_details.append(tradable_detail)
        # self.Debug("RebalanceDaily triggered.")
        self.LiquidateExpiringOptions()

        candidateOptions = self.SelectLiquidOptions()
        self.Debug(f"SelectLiquidOptions returned {len(candidateOptions)} candidates.")
        if not candidateOptions:
            return

        ivRanks = self.ComputeIVRankings(candidateOptions)
        self.Debug(f"ComputeIVRankings returned {len(ivRanks)} ranks.")
        if not ivRanks:
            return

        topN = 5
        shortVolList = sorted(ivRanks, key=lambda x: x[1], reverse=True)[:topN]
        longVolList = sorted(ivRanks, key=lambda x: x[1])[:topN]

        self.Debug(f"ShortVolList: {[s[0].Value for s in shortVolList]}")
        self.Debug(f"LongVolList: {[s[0].Value for s in longVolList]}")

        self.highIVSymbols = [x[0] for x in shortVolList]
        self.lowIVSymbols = [x[0] for x in longVolList]

        historicalReturns = self.GetRecentDailyReturns()
        self.kelly.Update(historicalReturns)
        kellyFraction = self.kelly.GetFraction()
        self.Debug(f"Kelly Fraction: {kellyFraction:.4f}")

        self.LiquidateRemovedPositions(shortVolList, longVolList)
        self.BuildDeltaNeutralPositions(shortVolList, longVolList, kellyFraction)

    def SelectLiquidOptions(self, optionChains=None):
        results = []
        chains = optionChains or self.latestOptionChains
        if not chains:
            return results

        max_exp_days = int(self.GetParameter("algo.option.max_exp_days"))
        min_open_inter = int(self.GetParameter("algo.option.min_open_inter"))

        for symbol, chain in chains.items():
            underlying_price = chain.Underlying.Price
            if underlying_price == 0:
                continue  # Avoid divide-by-zero error

            contracts = [o for o in chain
                         if (o.Expiry - self.Time).days < max_exp_days
                         and abs(o.Strike - underlying_price) / underlying_price < 0.05
                         and o.OpenInterest > min_open_inter]
            if contracts:
                bestContract = max(contracts, key=lambda x: x.OpenInterest)
                results.append(bestContract)
        return results

    def ComputeIVRankings(self, candidateOptions):
        iv_values = []
        iv_ranks = []

        for contract in candidateOptions:
            option_symbol = contract.Symbol
            current_iv = contract.ImpliedVolatility

            if current_iv is None or current_iv == 0:
                continue

            if option_symbol not in self.iv_history:
                self.iv_history[option_symbol] = []

            self.iv_history[option_symbol].append(current_iv)

            window_size = 30
            history = self.iv_history[option_symbol][-window_size:]

            if len(history) < 25:
                continue

            highest_iv = max(history)
            lowest_iv = min(history)
            rank = sum(1 for v in history if v <= current_iv) / len(history)

            # self.Debug(f"IV Debug: symbol={option_symbol.Value}, high={highest_iv:.3f}, low={lowest_iv:.3f}, current={current_iv:.3f}, percentile={rank:.3f}")

            iv_values.append(current_iv)

            # Only include options meeting directional criteria
            if rank >= 0.8 or rank <= 0.2:
                iv_ranks.append((option_symbol, rank))

                # Plot average IV of the day
        if iv_values:
            avg_iv = np.mean(iv_values)
            self.Plot("IV Summary", "Average IV", avg_iv)

        return iv_ranks

    def LiquidateRemovedPositions(self, shortVolList, longVolList):
        keepSymbols = {x[0] for x in shortVolList} | {x[0] for x in longVolList}
        for holding in list(self.Portfolio.Values):
            if holding.Invested and holding.Symbol not in keepSymbols:
                self.Liquidate(holding.Symbol)

    def LiquidateExpiringOptions(self):
        for holding in list(self.Portfolio.Values):
            if holding.Invested and holding.Symbol.SecurityType == SecurityType.Option:
                expiry = holding.Symbol.ID.Date
                if (expiry.date() - self.Time.date()).days <= 13:
                    self.Liquidate(holding.Symbol)

    def BuildDeltaNeutralPositions(self, shortVolList, longVolList, kellyFraction):
        used_equities = set()
        # self.Debug(f"Entering BuildDeltaNeutralPositions with {len(shortVolList)} shorts and {len(longVolList)} longs.")

        for sym, rank in shortVolList:
            equity = sym.Underlying
            underlying_str = equity.Value
            equity_symbol = equity.Value
            the_securities = self.Securities
            self.Debug(f"Checking if {equity_symbol} exists in Securities: {equity_symbol in self.Securities}")
            if equity_symbol not in self.Securities:
                self.Debug(f"Adding missing equity for short hedge: {underlying_str}")
                equity_symbol = self.AddEquity(underlying_str, Resolution.Daily).Symbol

            if self.Portfolio[sym].Invested:
                self.Debug(f"Already invested in option {sym.Value}, skipping short.")
                continue
            if self.Portfolio[equity_symbol].Invested:
                self.Debug(f"Already invested in equity {equity_symbol}, skipping hedge.")
                continue
            if equity_symbol in used_equities:
                self.Debug(f"Equity {equity_symbol} already used for another hedge.")
                continue
            if not self.Securities[equity_symbol].IsTradable:
                self.Debug(f"Symbol {equity_symbol} is not {self.Securities[equity_symbol].IsTradable}. Skipping.")
                continue

            short_vol_opt_order = self.MarketOrder(sym, -1)
            if sym.ID.OptionRight == OptionRight.Call:
                short_vol_stk_order = self.MarketOrder(equity_symbol, 100)
            else:
                short_vol_stk_order = self.MarketOrder(equity_symbol, -100)
            self.Debug(f"ShortVol {sym.Value} rank={rank:.3f}. Opening short call + long stock.")
            used_equities.add(equity_symbol)

        for sym, rank in longVolList:
            equity = sym.Underlying
            underlying_str = equity.Value
            equity_symbol = equity.Value

            if equity_symbol not in self.Securities:
                self.Debug(f"Adding missing equity for long hedge: {underlying_str}")
                equity_symbol = self.AddEquity(underlying_str, Resolution.Daily).Symbol

            if self.Portfolio[sym].Invested:
                self.Debug(f"Already invested in option {sym.Value}, skipping long.")
                continue
            if self.Portfolio[equity_symbol].Invested:
                self.Debug(f"Already invested in equity {equity_symbol}, skipping hedge.")
                continue
            if equity_symbol in used_equities:
                self.Debug(f"Equity {equity_symbol} already used for another hedge.")
                continue
            if not self.Securities[equity_symbol].IsTradable:
                self.Debug(f"Symbol {equity_symbol} is not {self.Securities[equity_symbol].IsTradable}. Skipping.")
                continue

            long_vol_opt_order = self.MarketOrder(sym, 1)
            if sym.ID.OptionRight == OptionRight.Call:
                long_vol_stk_order = self.MarketOrder(equity_symbol, -100)
            else:
                long_vol_stk_order = self.MarketOrder(equity_symbol, 100)

            self.Debug(f"LongVol {sym.Value} rank={rank:.3f}. Opening long call + short stock.")
            used_equities.add(equity_symbol)


    def GetRecentDailyReturns(self):
        return [random.uniform(-0.01, 0.01) for _ in range(30)]
