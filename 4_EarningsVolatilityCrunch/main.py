import math
import json
import uuid
from datetime import timedelta, datetime, date, time
from collections import defaultdict
from typing import List, Dict, Tuple, Optional, Set, Any
from dataclasses import dataclass
import numpy as np
import os
import sys

_WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_LIBRARY_DIR = os.path.join(_WORKSPACE_DIR, "Library")
for path_dir in [_WORKSPACE_DIR, _LIBRARY_DIR]:
    if path_dir not in sys.path:
        sys.path.insert(0, path_dir)

from AlgorithmImports import *
from PropietaryCode import (
    monitor_execution,
    fast_norm_cdf,
    fast_norm_pdf,
    fast_bs_price,
    fast_vega,
    fast_implied_volatility_newton,
    CalendarSpreadOpportunity,
    CalendarSpreadAlphaModel,
    CalendarSpreadExecutionManager,
)

_norm_cdf = fast_norm_cdf
_norm_pdf = fast_norm_pdf


class EarningsVolatilityCrunch(QCAlgorithm):
    earnings_calendar: Dict[Symbol, Dict[str, Any]] = {}
    pending_option_orders: List[Tuple[Symbol, int, str]] = []
    active_spreads: Dict[str, Dict[str, Any]] = {}
    trade_history: Dict[Symbol, List[Dict[str, Any]]] = defaultdict(list)
    
    _metrics_cache: Dict[Tuple[Symbol, date], Tuple[float, float]] = {}
    _option_chain_cache: Dict[Tuple[Symbol, date], List[Symbol]] = {}
    _subscribed_options: Set[Symbol] = set()
    _final_liquidated: bool = False
    _algo_end_date: Optional[date] = None

    def Initialize(self) -> None:
        EarningsVolatilityCrunch._metrics_cache.clear()
        EarningsVolatilityCrunch._option_chain_cache.clear()
        EarningsVolatilityCrunch._subscribed_options.clear()
        self.earnings_calendar.clear()
        self.active_spreads.clear()
        self.pending_option_orders.clear()

        self.backtest_run_id = f"EVC_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{str(uuid.uuid4())[:8]}"
        self.trade_id_counter = 0
        self._pending_entry_tickets = {}
        self._pending_exit_tickets = {}
        self._traded_today = set()
        self._underlying_prices = {}

        self.universe_settings.resolution = Resolution.HOUR
        self.universe_settings.fill_forward = True
        self.universe_settings.data_normalization_mode = DataNormalizationMode.RAW
        self.universe_settings.dispose_on_universe_removal = True
        self.Settings.SeedInitialPrices = True

        self.set_brokerage_model(BrokerageName.INTERACTIVE_BROKERS_BROKERAGE, AccountType.MARGIN)

        self.initial_amount = float(self.GetParameter("exec.initial_amount", "100000000.0"))
        self.max_symbols = int(self.GetParameter("univ.coarse.max_symbols", "2000"))
        self.alpha_spread = float(self.GetParameter("exec.alpha_spread", "0.20"))
        self.risk_free_rate = float(self.GetParameter("exec.risk_free_rate", "0.045"))
        self.SetStartDate(*map(int, self.GetParameter("exec.start_date", "2020-01-01").split('-')))
        self.SetEndDate(*map(int, self.GetParameter("exec.end_date", "2025-12-31").split('-')))
        self.SetCash(self.initial_amount)
        self.SetWarmUp(10, Resolution.Daily)

        self.min_days_before_earnings = 0
        self.days_before_earnings = 1
        self.days_after_earnings = 0
        self.entry_hour = int(self.GetParameter("algo.entry_hour", "15"))
        self.exit_hour = int(self.GetParameter("algo.exit_hour", "10"))
        self.slope_threshold = float(self.GetParameter("algo.slope_threshold", "0.0"))
        self.max_spread_threshold = float(self.GetParameter("algo.max_spread_threshold", "0.25"))
        self.fill_method = str(self.GetParameter("exec.fill_method", "combo_limit_natural")).lower()
        self.Log(f"[Initialize] Execution fill method configured: {self.fill_method}")

        pass_all_param = str(self.GetParameter("algo.pass_all", "true")).lower() == "true"
        is_hdbt = str(self.GetParameter("algo.is_hdbt", "false")).lower() == "true"
        if pass_all_param or is_hdbt:
            self.pass_all = True
            self.max_symbols = max(2000, self.max_symbols)
            self.Log(f"[Initialize] Running pass_all=True, max_symbols={self.max_symbols}")
        else:
            self.pass_all = False
            self.Log(f"[Initialize] Filtered run mode: pass_all=False, max_symbols={self.max_symbols}")

        self.volume_threshold = float(self.GetParameter("algo.volume_threshold", "1.0"))
        self.ivrv_threshold = float(self.GetParameter("algo.ivrv_threshold", "1.0"))
        self.max_loss_pct = float(self.GetParameter("risk.max_loss_pct", "70.0"))
        self.kelly_factor = float(self.GetParameter("risk.kelly.factor", "0.35"))
        self.kelly_period = int(self.GetParameter("risk.kelly.period", "30"))
        
        self.option_upper_filter = int(self.GetParameter("algo.option.upper_filter", "0"))
        self.option_lower_filter = int(self.GetParameter("algo.option.lower_filter", "0"))
        self.option_max_exp_days = int(self.GetParameter("algo.option.max_exp_days", "150"))
        self.option_min_exp_days = int(self.GetParameter("algo.option.min_exp_days", "5"))
        self.min_days_between_contracts = int(self.GetParameter("algo.min_days_between", "21"))
        self.max_days_between_contracts = int(self.GetParameter("algo.max_days_between", "31"))

        self.min_iv_ratio = float(self.GetParameter("algo.min_iv_ratio", "1.15"))
        self.itm_safety_pct = float(self.GetParameter("risk.itm_safety_pct", "1.5"))

        self.alpha_model = CalendarSpreadAlphaModel(self)
        self.execution_manager = CalendarSpreadExecutionManager(self)

        self.AddUniverse(self.CoarseSelectionFunction)
        self.AddUniverse(EODHDUpcomingEarnings, self.UpcomingEarningsSelectionFunction)
        self.RegisterFinalLiquidation(anchor_ticker="SPY", minutes_before_close=120)

    def CoarseSelectionFunction(self, coarse: List[CoarseFundamental]) -> List[Symbol]:
        min_price = float(self.GetParameter("univ.coarse.min_price", "5"))
        min_share_volume = float(self.GetParameter("univ.coarse.min_share_volume", "0"))

        filtered = [
            x for x in coarse 
            if x.HasFundamentalData and x.Price >= min_price and (
                (min_share_volume > 0 and x.Volume is not None and x.Volume >= min_share_volume) or
                (min_share_volume <= 0 and x.Volume is not None and x.Volume > 0 and x.DollarVolume is not None and x.DollarVolume > 0)
            )
        ]
        sorted_filtered = sorted(filtered, key=lambda x: x.DollarVolume, reverse=True)
        selected_symbols = [x.Symbol for x in sorted_filtered[:self.max_symbols]]
        self._active_coarse_tickers = {x.Value for x in selected_symbols}
        return []

    def UpcomingEarningsSelectionFunction(self, earnings: List[EODHDUpcomingEarnings]) -> List[Symbol]:
        selected = []
        min_cutoff = self.Time.date()
        target_cutoff = (self.Time + timedelta(days=3)).date()
        active_tickers = getattr(self, "_active_coarse_tickers", set())

        for e in earnings:
            if e.ReportDate is not None:
                if active_tickers and e.Symbol.Value not in active_tickers:
                    continue
                report_d = e.ReportDate.date()
                if min_cutoff <= report_d <= target_cutoff:
                    selected.append(e.Symbol)
                    r_time = str(e.ReportTime) if hasattr(e, "ReportTime") else ("AMC" if e.ReportDate.hour >= 12 else "BMO")
                    self.earnings_calendar[e.Symbol] = {
                        "report_date": e.ReportDate,
                        "report_time": r_time
                    }
        return selected

    def OnSecuritiesChanged(self, changes: SecurityChanges) -> None:
        for security in changes.AddedSecurities:
            if security.Type == SecurityType.Equity:
                security.SetDataNormalizationMode(DataNormalizationMode.Raw)

    def OnData(self, data: Slice) -> None:
        if self.IsWarmingUp:
            return

        for holding in list(self.Portfolio.Values):
            if holding.Invested and holding.Symbol.SecurityType == SecurityType.Equity:
                open_orders = self.Transactions.GetOpenOrders(holding.Symbol)
                if not open_orders:
                    self.Log(f"[ASSIGNMENT EMERGENCY] Flattening assigned equity {holding.Symbol.Value} Qty: {holding.Quantity}")
                    self.MarketOrder(holding.Symbol, -holding.Quantity, tag="FLATTEN: Assignment Stock Emergency")
                    
                    underlying = holding.Symbol
                    for s_key, pos in list(self.active_spreads.items()):
                        if pos.get("underlying") == underlying:
                            back = pos.get("back")
                            if back and self.Portfolio.ContainsKey(back) and self.Portfolio[back].Invested:
                                back_qty = self.Portfolio[back].Quantity
                                self.MarketOrder(back, -back_qty, tag="FLATTEN: Emergency Long Leg Cut Post-Assignment")
                            self.UnsubscribeOption(pos.get("front"))
                            self.UnsubscribeOption(back)
                            self.active_spreads.pop(s_key, None)

        self.SweepOrphanedOptionLegs()
        self.execution_manager.ManagePositions(data)
        self.ProcessPendingOrders(data)
        self.PurgeExpiredEarnings()

        opportunities = self.alpha_model.ScanOpportunities(data)
        for opp in opportunities:
            self.execution_manager.ExecuteOpportunity(opp)

    def IsAlreadyInvested(self, underlying: Symbol, option_right: Optional[OptionRight] = None) -> bool:
        if option_right is not None:
            if (underlying, option_right, self.Time.date()) in getattr(self, "_traded_today", set()):
                return True
        else:
            if (underlying, self.Time.date()) in getattr(self, "_traded_today", set()):
                return True

        for pos in self.active_spreads.values():
            if pos.get("underlying") == underlying:
                if option_right is None:
                    return True
                f = pos.get("front")
                if f and f.ID.OptionRight == option_right:
                    return True

        und_val = underlying.Value if hasattr(underlying, "Value") else str(underlying)
        def _match(s: Any) -> bool:
            su = getattr(s, "Underlying", None)
            return su == underlying or (getattr(su, "Value", str(su)) == und_val if su else False)

        opt_types = (SecurityType.Option, SecurityType.IndexOption, SecurityType.FutureOption)
        for s in self.Portfolio.Keys:
            if s.SecurityType in opt_types and _match(s) and self.Portfolio[s].Invested:
                if option_right is None or s.ID.OptionRight == option_right:
                    return True

        for c, _, _ in self.pending_option_orders:
            if _match(c) and (option_right is None or c.ID.OptionRight == option_right):
                return True

        for o in self.Transactions.GetOpenOrders():
            if o.Symbol.SecurityType in opt_types and _match(o.Symbol):
                if option_right is None or o.Symbol.ID.OptionRight == option_right:
                    return True

        return False

    def GetUnderlyingPrice(self, symbol: Symbol) -> float:
        if symbol in self.Securities and self.Securities[symbol].Price > 0:
            return float(self.Securities[symbol].Price)
        return float(self._underlying_prices.get(symbol, 0.0))

    @monitor_execution
    def GetOptionContractsCached(self, symbol: Symbol, earnings_time: datetime) -> List[Symbol]:
        cache_key = (symbol, self.Time.date())
        if cache_key in self._option_chain_cache:
            contracts = self._option_chain_cache[cache_key]
        else:
            try:
                contracts = self.OptionChainProvider.GetOptionContractList(symbol, self.Time)
                self._option_chain_cache[cache_key] = contracts if contracts else []
            except Exception as e:
                self.Debug(f"[GetOptionContractsCached] Lookup exception for {symbol.Value}: {e}")
                self._option_chain_cache[cache_key] = []
                contracts = []

        if not contracts:
            return []

        price = self.GetUnderlyingPrice(symbol)
        if price <= 0.0:
            return []

        min_date = max(self.Time.date(), earnings_time.date())
        max_date = (earnings_time + timedelta(days=self.option_max_exp_days)).date()

        valid = [
            c for c in contracts
            if c.ID.Date.date() > min_date and c.ID.Date.date() <= max_date
        ]
        if not valid:
            return []

        selected = []

        for right in (OptionRight.Call, OptionRight.Put):
            right_contracts = [c for c in valid if c.ID.OptionRight == right]
            if right_contracts:
                strikes = sorted(list({float(c.ID.StrikePrice) for c in right_contracts}))
                target = min(strikes, key=lambda s: abs(s - price))
                idx = strikes.index(target)
                start = max(0, idx + self.option_lower_filter)
                end = min(len(strikes) - 1, idx + self.option_upper_filter)
                allowed = set(strikes[start:end + 1])
                selected.extend([c for c in right_contracts if float(c.ID.StrikePrice) in allowed])

        return selected

    @monitor_execution
    def MatchOptionContracts(self, contracts: List[Symbol]) -> List[Tuple[Symbol, Symbol]]:
        buckets = defaultdict(list)
        for c in contracts:
            key = (c.ID.OptionRight, float(c.ID.StrikePrice))
            buckets[key].append(c)

        matches: List[Tuple[Symbol, Symbol]] = []
        for key, lst in buckets.items():
            lst.sort(key=lambda x: x.ID.Date)
            if not lst:
                continue

            near = lst[0]
            for far in lst[1:]:
                days_gap = (far.ID.Date.date() - near.ID.Date.date()).days
                if self.min_days_between_contracts <= days_gap <= self.max_days_between_contracts:
                    matches.append((near, far))
                    break

        return matches

    @monitor_execution
    def GetUnderlyingMetricsCached(self, underlying: Symbol, earnings_date: datetime) -> Optional[Tuple[float, float]]:
        cache_key = (underlying, self.Time.date())
        if cache_key in self._metrics_cache:
            return self._metrics_cache[cache_key]

        earnings_date_naive = earnings_date.replace(tzinfo=None)

        try:
            history = self.History(underlying, 35, Resolution.Daily)
        except Exception:
            return None
        if history is None or getattr(history, "empty", True):
            return None

        df = history.loc[underlying] if hasattr(history.index, "levels") and underlying in history.index else history
        if hasattr(df.index, "tz") and df.index.tz is not None:
            df = df.tz_localize(None)

        df = df[df.index < earnings_date_naive]
        if len(df) < 31:
            return None

        vol_col = 'volume' if 'volume' in df.columns else ('Volume' if 'Volume' in df.columns else None)
        close_col = 'close' if 'close' in df.columns else ('Close' if 'Close' in df.columns else None)
        if not vol_col or not close_col or len(df[vol_col]) < 31 or len(df[close_col]) < 31:
            return None

        vol_series, close_series = df[vol_col], df[close_col]
        recent_volume, avg_volume = float(vol_series.iloc[-1]), float(vol_series.iloc[-31:-1].mean())
        if not avg_volume or math.isnan(recent_volume) or math.isnan(avg_volume) or avg_volume <= 0:
            return None

        vol_ratio = recent_volume / avg_volume
        self._underlying_prices[underlying] = float(close_series.iloc[-1])
        returns = close_series.pct_change().dropna()
        if len(returns) < 30:
            return None
        realized_volatility = float(returns.iloc[-30:].std() * math.sqrt(252))

        result = (vol_ratio, realized_volatility)
        self._metrics_cache[cache_key] = result
        return result

    @monitor_execution
    def CalculateMetrics(self, underlying: Symbol, near_contract: Symbol, far_contract: Symbol, 
                         earnings_date: datetime, vol_ratio: float, rv: float) -> Optional[Dict[str, Any]]:
        underlying_price = self.GetUnderlyingPrice(underlying)
        if underlying_price <= 0:
            return None

        near_price = self.GetOptionMidPrice(near_contract)
        far_price = self.GetOptionMidPrice(far_contract)
        if near_price <= 0 or far_price <= 0:
            return None

        T_near = max((near_contract.ID.Date - self.Time).total_seconds(), 0.0) / (365.0 * 24 * 3600)
        T_far = max((far_contract.ID.Date - self.Time).total_seconds(), 0.0) / (365.0 * 24 * 3600)
        if T_near <= 0 or T_far <= 0 or T_far <= T_near:
            return None

        strike = float(near_contract.ID.StrikePrice)
        right = near_contract.ID.OptionRight

        iv_near = self._implied_volatility_newton(right, underlying_price, strike, T_near, self.risk_free_rate, near_price)
        iv_far = self._implied_volatility_newton(right, underlying_price, strike, T_far, self.risk_free_rate, far_price)
        if iv_near is None or iv_far is None or iv_near <= 0 or iv_far <= 0:
            return None

        delta_T_days = (far_contract.ID.Date.date() - near_contract.ID.Date.date()).days
        if delta_T_days <= 0:
            return None

        slope = (iv_far - iv_near) / delta_T_days
        ivrv_ratio = iv_near / rv if rv > 0 else 0.0

        if not self.pass_all:
            if self.slope_threshold != 0.0 and slope > self.slope_threshold:
                return None
            if ivrv_ratio < self.ivrv_threshold:
                return None

        return {
            "vol_ratio": vol_ratio,
            "slope": slope,
            "ivrv_ratio": ivrv_ratio,
            "front_iv": iv_near,
            "back_iv": iv_far,
            "strike": strike,
            "underlying_price": underlying_price,
            "rv": rv
        }

    def _bs_price(self, right: Any, S: float, K: float, T: float, r: float, sigma: float) -> float:
        return fast_bs_price(right, S, K, T, r, sigma)

    def _vega(self, S: float, K: float, T: float, r: float, sigma: float) -> float:
        return fast_vega(S, K, T, r, sigma)

    def _implied_volatility_newton(self, right: Any, S: float, K: float, T: float, r: float, market_price: float) -> Optional[float]:
        return fast_implied_volatility_newton(right, S, K, T, r, market_price)

    def GetOptionMidPrice(self, symbol: Symbol) -> float:
        if symbol in self.Securities:
            sec = self.Securities[symbol]
            bid = float(sec.BidPrice) if hasattr(sec, "BidPrice") else 0.0
            ask = float(sec.AskPrice) if hasattr(sec, "AskPrice") else 0.0
            if bid > 0 and ask > 0:
                return (bid + ask) / 2.0
            price = float(sec.Price) if hasattr(sec, "Price") else 0.0
            if price > 0:
                return price
        try:
            hist = self.History(symbol, 1, Resolution.Hour)
            if hist is not None and not getattr(hist, "empty", True):
                col = 'close' if 'close' in hist.columns else ('Close' if 'Close' in hist.columns else None)
                if col:
                    return float(hist[col].iloc[-1])
        except Exception:
            pass
        return 0.0

    def DeterminePositionSize(self, underlying: Symbol, metrics: Dict[str, Any], natural_ask: float = 0.0) -> int:
        total_equity = float(self.Portfolio.TotalPortfolioValue)
        margin_remaining = float(self.Portfolio.MarginRemaining)
        if total_equity <= 0 or margin_remaining <= 0:
            return 0

        target_allocation = 0.01
        capital_to_risk = min(total_equity * target_allocation, margin_remaining * 0.02)
        if natural_ask > 0.01:
            contract_cost = max(natural_ask * 100.0, 25.0)
        else:
            debit_est = metrics.get("underlying_price", 100.0) * 0.03
            contract_cost = max(debit_est * 100.0, 25.0)
        qty = int(capital_to_risk / contract_cost)
        max_margin_qty = int((margin_remaining * 0.05) / contract_cost)
        qty = min(qty, max_margin_qty)
        
        return max(1, min(qty, 25)) if (qty >= 1 and margin_remaining >= contract_cost) else 0

    def BuildOrderTag(self, underlying: Symbol, front: Symbol, back: Symbol, metrics: Dict[str, Any], leg_type: str) -> str:
        right_str = "C" if front.ID.OptionRight == OptionRight.Call else "P"
        payload = {
            "u": underlying.Value,
            "right": right_str,
            "k": float(front.ID.StrikePrice),
            "near": front.ID.Date.strftime("%Y-%m-%d"),
            "far": back.ID.Date.strftime("%Y-%m-%d"),
            "slope": round(float(metrics.get("slope", 0.0)), 6),
            "vol_ratio": round(float(metrics.get("vol_ratio", 0.0)), 4),
            "ivrv_ratio": round(float(metrics.get("ivrv_ratio", 0.0)), 4),
            "front_iv": round(float(metrics.get("front_iv", 0.0)), 4),
            "back_iv": round(float(metrics.get("back_iv", 0.0)), 4),
            "leg": leg_type
        }
        return json.dumps(payload, separators=(',', ':'))

    def OnOrderEvent(self, orderEvent: OrderEvent) -> None:
        order_id = orderEvent.OrderId
        if orderEvent.Status == OrderStatus.Filled:
            if order_id in self._pending_entry_tickets:
                info = self._pending_entry_tickets[order_id]
                underlying = info["underlying"]
                symbol = orderEvent.Symbol
                fill_price = float(orderEvent.FillPrice)
                info.setdefault("entry_fills", {})[symbol] = fill_price

                if info["front"] in info["entry_fills"] and info["back"] in info["entry_fills"]:
                    if not info.get("logged_open", False):
                        info["logged_open"] = True
                        front_fill = info["entry_fills"][info["front"]]
                        back_fill = info["entry_fills"][info["back"]]
                        actual_entry_debit = round(back_fill - front_fill, 5)
                        if actual_entry_debit > 0:
                            info["entry_price"] = actual_entry_debit

                        self.active_spreads[info["pk"]] = info
                        self.LogTradeRecord("OPEN", underlying, info["front"], info["back"], info["qty"], info["entry_price"], info["metrics"], pk=info["pk"])
                        right_name = "Call" if info["front"].ID.OptionRight == OptionRight.Call else "Put"
                        self.Log(f"[ORDER EVENT FILL] Confirmed entry fill for {underlying.Value} ({right_name}) at debit ${info['entry_price']:.2f}.")
                        
                        for t in info.get("tickets", []):
                            self._pending_entry_tickets.pop(t.OrderId, None)

            elif order_id in self._pending_exit_tickets:
                info = self._pending_exit_tickets[order_id]
                underlying = info["underlying"]
                symbol = orderEvent.Symbol
                fill_price = float(orderEvent.FillPrice)
                info.setdefault("exit_fills", {})[symbol] = fill_price

                is_combo_filled = (info["front"] in info["exit_fills"] and info["back"] in info["exit_fills"])
                is_single_back_filled = (info.get("front_expired", False) and info["back"] in info["exit_fills"])

                if is_combo_filled or is_single_back_filled:
                    if not info.get("logged_close", False):
                        info["logged_close"] = True
                        front_exit_fill = info["exit_fills"].get(info["front"], 0.0)
                        back_exit_fill = info["exit_fills"].get(info["back"], 0.0)
                        
                        actual_exit_credit = round(back_exit_fill - front_exit_fill, 5)
                        exit_price = max(0.0, actual_exit_credit)
                        
                        entry_debit = info["entry_price"]
                        realized_pnl = round((exit_price - entry_debit) / entry_debit, 5) if entry_debit > 0 else 0.0
                        pnl = realized_pnl
                        
                        exit_reason = info.get("exit_reason", "Post-Earnings 10 AM Exit")
                        pk = info.get("pk", "unknown")
                        qty = info["qty"]

                        entry_time = info.get("entry_time", self.Time)
                        holding_hours = round((self.Time - entry_time).total_seconds() / 3600.0, 2)

                        front_iv_open = float(info.get("front_iv_open", info.get("metrics", {}).get("front_iv", 0.0)))
                        front_iv_max = float(info.get("front_iv_max", front_iv_open))
                        front_iv_min = float(info.get("front_iv_min", front_iv_open))
                        front_iv_close = float(info.get("last_front_iv", front_iv_open))

                        back_iv_open = float(info.get("back_iv_open", info.get("metrics", {}).get("back_iv", 0.0)))
                        back_iv_max = float(info.get("back_iv_max", back_iv_open))
                        back_iv_min = float(info.get("back_iv_min", back_iv_open))
                        back_iv_close = float(info.get("last_back_iv", back_iv_open))

                        front_iv_crush_pct = round(((front_iv_open - front_iv_close) / front_iv_open) * 100.0, 2) if front_iv_open > 0 else 0.0
                        back_iv_crush_pct = round(((back_iv_open - back_iv_close) / back_iv_open) * 100.0, 2) if back_iv_open > 0 else 0.0
                        front_iv_crush_diff = round(front_iv_open - front_iv_close, 5)
                        back_iv_crush_diff = round(back_iv_open - back_iv_close, 5)

                        metrics = {
                            "vol_ratio": info["vol_ratio"],
                            "slope": info["slope"],
                            "ivrv_ratio": info["ivrv_ratio"],
                            "mae_pct": info.get("mae_pct", 0.0),
                            "mfe_pct": info.get("mfe_pct", 0.0),
                            "holding_hours": holding_hours,
                            "front_iv_open": front_iv_open,
                            "front_iv_max": front_iv_max,
                            "front_iv_min": front_iv_min,
                            "front_iv_close": front_iv_close,
                            "front_iv_crush_pct": front_iv_crush_pct,
                            "front_iv_crush_diff": front_iv_crush_diff,
                            "back_iv_open": back_iv_open,
                            "back_iv_max": back_iv_max,
                            "back_iv_min": back_iv_min,
                            "back_iv_close": back_iv_close,
                            "back_iv_crush_pct": back_iv_crush_pct,
                            "back_iv_crush_diff": back_iv_crush_diff,
                            "comb_spread_entry": float(info.get("comb_spread", 0.0)),
                            "natural_ask_entry": float(info.get("natural_ask", 0.0)),
                            "mid_debit_entry": float(info.get("mid_debit", 0.0)),
                            "fill_method": info.get("fill_method", getattr(self, "fill_method", "combo_limit_natural")),
                            "exit_reason": exit_reason
                        }
                        
                        self.trade_history[underlying].append({
                            "pnl": pnl,
                            "entry_slope": info["slope"],
                            "entry_vol_ratio": info["vol_ratio"],
                            "entry_ivrv_ratio": info["ivrv_ratio"],
                            "exit_time": self.Time.isoformat()
                        })
                        self.trade_history[underlying] = self.trade_history[underlying][-20:]

                        self.LogTradeRecord("CLOSE", underlying, info["front"], info["back"], qty, entry_debit, metrics, pk=pk, exit_price=exit_price, pnl=pnl, exit_reason=exit_reason)
                        right_name = "Call" if info["front"].ID.OptionRight == OptionRight.Call else "Put"
                        self.Log(f"[ORDER EVENT EXIT FILL] Confirmed exit fill for {underlying.Value} ({right_name}) at credit ${exit_price:.2f} (Realized PnL: {pnl*100:.2f}% | Front IV Open/Close: {front_iv_open:.4f}/{front_iv_close:.4f} [Crush: {front_iv_crush_pct:.1f}%] | Back IV Open/Close: {back_iv_open:.4f}/{back_iv_close:.4f} [Crush: {back_iv_crush_pct:.1f}%] | Duration: {holding_hours}h).")

                        self.UnsubscribeOption(info["front"])
                        self.UnsubscribeOption(info["back"])
                        self.active_spreads.pop(info["pk"], None)
                        
                        for o_id in list(self._pending_exit_tickets.keys()):
                            if self._pending_exit_tickets[o_id] is info:
                                self._pending_exit_tickets.pop(o_id, None)

        elif orderEvent.Status in [OrderStatus.Canceled, OrderStatus.Invalid]:
            if order_id in self._pending_entry_tickets:
                self._pending_entry_tickets.pop(order_id, None)
            if order_id in self._pending_exit_tickets:
                self._pending_exit_tickets.pop(order_id, None)

    def ExecuteCalendarSpread(self, underlying: Symbol, front: Symbol, back: Symbol, qty: int, metrics: Dict[str, Any], report_date: datetime, report_time: str) -> None:
        opp = CalendarSpreadOpportunity(
            underlying=underlying,
            front=front,
            back=back,
            option_right=front.ID.OptionRight,
            metrics=metrics,
            report_date=report_date,
            report_time=report_time,
            rank_score=0.0
        )
        self.execution_manager.ExecuteOpportunity(opp)

    def ManageOpenPositions(self, data: Slice) -> None:
        self.execution_manager.ManagePositions(data)

    def SweepOrphanedOptionLegs(self) -> None:
        all_positions = list(self.active_spreads.values()) + [p for p in getattr(self, "_pending_exit_tickets", {}).values() if isinstance(p, dict)]
        active_contracts = {p[k] for p in all_positions for k in ("front", "back") if k in p}
        active_underlyings = {p["underlying"] for p in all_positions if "underlying" in p}

        for sec in list(self.Portfolio.Values):
            if sec.Invested and sec.Symbol.SecurityType in [SecurityType.Option, SecurityType.IndexOption]:
                if sec.Symbol in active_contracts:
                    continue
                und = sec.Symbol.Underlying if hasattr(sec.Symbol, "Underlying") and sec.Symbol.Underlying else None
                if und and und in active_underlyings:
                    continue

                open_orders = self.Transactions.GetOpenOrders(sec.Symbol)
                if not open_orders:
                    if sec.Quantity > 0:
                        self.Log(f"[ORPHAN SWEEPER] Liquidating unhedged long leg: {sec.Symbol.Value} Qty: {sec.Quantity}")
                        self.MarketOrder(sec.Symbol, -sec.Quantity, tag="FLATTEN: Orphaned Long Leg Sweep")

    def LiquidateSpread(self, spread_key: Any, tag: str) -> bool:
        return self.execution_manager.LiquidateSpread(spread_key, tag)

    def _ensure_option_tradable(self, symbol: Symbol) -> bool:
        if not symbol:
            return False
        if symbol not in self.Securities:
            try:
                opt = self.AddOptionContract(symbol, Resolution.Hour)
                opt.SetDataNormalizationMode(DataNormalizationMode.Raw)
                opt.SetOptionAssignmentModel(NullOptionAssignmentModel())
                self._subscribed_options.add(symbol)
            except Exception as e:
                self.Debug(f"Failed to add option contract {symbol.Value}: {e}")
                return False
        return True

    def UnsubscribeOption(self, symbol: Optional[Symbol]) -> None:
        if symbol and symbol in self._subscribed_options:
            try:
                self.RemoveSecurity(symbol)
                self._subscribed_options.discard(symbol)
            except Exception:
                pass

    def ProcessPendingOrders(self, data: Slice) -> None:
        still_pending = []
        for contract, qty, tag in self.pending_option_orders:
            if data.ContainsKey(contract) and self.Securities[contract].HasData and self.Securities[contract].Price > 0:
                self.MarketOrder(contract, qty, tag=f"fulfilled {tag}")
            else:
                still_pending.append((contract, qty, tag))
        self.pending_option_orders = still_pending

    def PurgeExpiredEarnings(self) -> None:
        today = self.Time.date()
        expired_keys = [
            sym for sym, info in self.earnings_calendar.items()
            if (isinstance(info, dict) and info["report_date"].date() < today) or
               (isinstance(info, datetime) and info.date() < today)
        ]
        for k in expired_keys:
            self.earnings_calendar.pop(k, None)

        # Evict cache entries older than 5 days to prevent monotonic memory leaks
        cutoff = today - timedelta(days=5)
        stale_metrics = [k for k in list(self._metrics_cache.keys()) if k[1] < cutoff]
        for k in stale_metrics:
            self._metrics_cache.pop(k, None)

        stale_chains = [k for k in list(self._option_chain_cache.keys()) if k[1] < cutoff]
        for k in stale_chains:
            self._option_chain_cache.pop(k, None)

    def RegisterFinalLiquidation(self, anchor_ticker: str = "SPY", minutes_before_close: int = 120) -> None:
        try:
            self.Schedule.On(
                self.DateRules.EveryDay(anchor_ticker),
                self.TimeRules.BeforeMarketClose(anchor_ticker, minutes_before_close),
                self._ExecuteFinalLiquidationCheck
            )
        except Exception as e:
            self.Debug(f"[RegisterFinalLiquidation] Could not register scheduled liquidation: {e}")

    def _ExecuteFinalLiquidationCheck(self) -> None:
        if self._algo_end_date is None:
            self._algo_end_date = self.EndDate.date() if hasattr(self, "EndDate") and self.EndDate else None

        if self._algo_end_date is not None and self.Time.date() >= self._algo_end_date:
            if not self._final_liquidated:
                self.LiquidateAllPositions(tag="FINAL_ALGO_END_FLATTEN")
                self._final_liquidated = True

    def LiquidateAllPositions(self, tag: str = "FORCE_FLATTEN") -> None:
        self.Log(f"[LiquidateAllPositions] Executing portfolio liquidation under tag: {tag}")
        for spread_key in list(self.active_spreads.keys()):
            self.execution_manager.LiquidateSpread(spread_key, tag)

    def LogTradeRecord(self, action: str, underlying: Symbol, front: Symbol, back: Symbol, qty: int, price: float,
                       metrics: Dict[str, Any], pk: Optional[str] = None, exit_price: float = 0.0, pnl: float = 0.0,
                       exit_reason: str = "") -> None:
        trade_data = {
            "pk": pk or f"{self.backtest_run_id}_{underlying.Value}_{self.Time.strftime('%Y%m%d%H%M%S')}",
            "algo_code": "4EVC",
            "timestamp": self.Time.isoformat(),
            "underlying": underlying.Value,
            "action": action,
            "qty": qty,
            "strike": float(front.ID.StrikePrice),
            "near_expiry": front.ID.Date.strftime("%Y-%m-%d"),
            "far_expiry": back.ID.Date.strftime("%Y-%m-%d"),
            "vol_ratio": float(metrics.get("vol_ratio", 0.0)),
            "slope": float(metrics.get("slope", 0.0)),
            "ivrv_ratio": float(metrics.get("ivrv_ratio", 0.0)),
            "entry_price": float(price),
            "exit_price": float(exit_price),
            "pnl": float(pnl),
            "exit_reason": exit_reason,
            "parameters": json.dumps({
                "pass_all": self.pass_all,
                "fill_method": metrics.get("fill_method", getattr(self, "fill_method", "combo_limit_natural")),
                "comb_spread_entry": metrics.get("comb_spread_entry", 0.0),
                "natural_ask_entry": metrics.get("natural_ask_entry", 0.0),
                "mid_debit_entry": metrics.get("mid_debit_entry", 0.0),
                "front_iv": metrics.get("front_iv", 0.0),
                "back_iv": metrics.get("back_iv", 0.0),
                "holding_hours": metrics.get("holding_hours", 0.0),
                "mae_pct": metrics.get("mae_pct", 0.0),
                "mfe_pct": metrics.get("mfe_pct", 0.0),
                "front_iv_crush_pct": metrics.get("front_iv_crush_pct", 0.0),
                "back_iv_crush_pct": metrics.get("back_iv_crush_pct", 0.0)
            })
        }
        self.Log(f"[BIGQUERY_TRADE_RECORD] {json.dumps(trade_data)}")

