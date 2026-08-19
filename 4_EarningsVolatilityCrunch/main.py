import math
import json
import uuid
from datetime import timedelta, datetime, date, time
from collections import defaultdict
from typing import List, Dict, Tuple, Optional, Set, Any
import numpy as np

import os
import sys

_WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_LIBRARY_DIR = os.path.join(_WORKSPACE_DIR, "Library")
for path_dir in [_WORKSPACE_DIR, _LIBRARY_DIR]:
    if path_dir not in sys.path:
        sys.path.insert(0, path_dir)

from AlgorithmImports import *
from PropietaryCode import monitor_execution
# endregion

# Pure math standard normal distribution helpers (100x faster than scipy.stats.norm)
def _norm_cdf(x: float) -> float:
    """Standard normal cumulative distribution function using math.erf."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def _norm_pdf(x: float) -> float:
    """Standard normal probability density function."""
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


class EarningsVolatilityCrunch(QCAlgorithm):
    # State tracking variables
    earnings_calendar: Dict[Symbol, datetime] = {}
    pending_option_orders: List[Tuple[Symbol, int, str]] = []  # Queue of (contract, qty, tag)
    active_spreads: Dict[Symbol, Dict[str, Any]] = {}          # {underlying: {front, back, qty, entry_price, report_date}}
    trade_history: Dict[Symbol, List[Dict[str, Any]]] = defaultdict(list) # {underlying: [{"pnl", ...}]}
    
    # High-Performance Caches (Eliminates repeated OptionChainProvider & History calls)
    _metrics_cache: Dict[Tuple[Symbol, date], Tuple[float, float]] = {}      # {(symbol, date): (vol_ratio, rv)}
    _option_chain_cache: Dict[Tuple[Symbol, date], List[Symbol]] = {}        # {(symbol, date): option_contracts}
    _subscribed_options: Set[Symbol] = set()                                 # Set of currently subscribed option contracts
    
    # Thresholds and params
    initial_amount: float = 0.0
    max_symbols: int = 4000
    alpha_spread: float = 0.20
    days_before_earnings: int = 0
    days_after_earnings: int = 0
    slope_threshold: float = 0.0
    max_spread_threshold: float = 2.00
    max_loss_pct: float = 0.0
    kelly_factor: float = 0.0
    kelly_period: int = 0
    option_upper_filter: int = 0
    option_lower_filter: int = 0
    option_max_exp_days: int = 0
    option_min_exp_days: int = 0
    
    # Pass-all toggle for profit-to-factor trade analysis
    pass_all: bool = False
    volume_threshold: float = 1.0
    ivrv_threshold: float = 1.0
    
    # State flags
    _final_liquidated: bool = False
    _algo_end_date: Optional[date] = None

    def Initialize(self) -> None:
        """Initial settings, universes, parameter loading, and schedule events."""
        # Reset all class-level dictionary caches to prevent memory leaks across runs
        EarningsVolatilityCrunch._metrics_cache.clear()
        EarningsVolatilityCrunch._option_chain_cache.clear()
        EarningsVolatilityCrunch._subscribed_options.clear()
        self.earnings_calendar.clear()
        self.active_spreads.clear()
        self.pending_option_orders.clear()

        # Unique identifier for this backtest execution run and trade counter
        self.backtest_run_id = f"EVC_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{str(uuid.uuid4())[:8]}"
        self.trade_id_counter = 0
        self._pending_entry_tickets = {}
        self._pending_exit_tickets = {}
        self._traded_today = set()

        # 1. Setup Resolution and parameters (Strict Hourly Resolution)
        self.universe_settings.resolution = Resolution.HOUR
        self.universe_settings.fill_forward = True
        self.universe_settings.data_normalization_mode = DataNormalizationMode.RAW
        self.universe_settings.dispose_on_universe_removal = True

        # 2. Brokerage setup
        self.set_brokerage_model(BrokerageName.INTERACTIVE_BROKERS_BROKERAGE, AccountType.MARGIN)

        # 3. Load configuration parameters
        self.initial_amount = float(self.GetParameter("exec.initial_amount", "100000000.0"))
        self.max_symbols = int(self.GetParameter("univ.coarse.max_symbols", "4000"))
        self.alpha_spread = float(self.GetParameter("exec.alpha_spread", "0.20"))
        self.risk_free_rate = float(self.GetParameter("exec.risk_free_rate", "0.045")) # Current 4.5% benchmark interest rate
        self.SetStartDate(*map(int, self.GetParameter("exec.start_date", "2020-01-01").split('-')))
        self.SetEndDate(*map(int, self.GetParameter("exec.end_date", "2025-12-31").split('-')))
        self.SetCash(self.initial_amount)
        self.SetWarmUp(10, Resolution.Daily)

        self.min_days_before_earnings = int(self.GetParameter("algo.min_days_before_earnings", "1"))
        self.days_before_earnings = int(self.GetParameter("algo.days_before_earnings", "3"))
        self.days_after_earnings = int(self.GetParameter("algo.days_after_earnings", "0"))
        self.entry_hour = int(self.GetParameter("algo.entry_hour", "15"))
        self.exit_hour = int(self.GetParameter("algo.exit_hour", "10"))
        self.slope_threshold = float(self.GetParameter("algo.slope_threshold", "0.0"))
        self.max_spread_threshold = float(self.GetParameter("algo.max_spread_threshold", "0.25"))

        # Data collection mode enforcement (pass_all = True for data collection across 3000 symbols)
        pass_all_param = str(self.GetParameter("algo.pass_all", "true")).lower() == "true"
        is_hdbt = str(self.GetParameter("algo.is_hdbt", "false")).lower() == "true"
        if pass_all_param or is_hdbt:
            self.pass_all = True
            self.max_symbols = max(3000, self.max_symbols)
            self.Log(f"[Data Collection Initialize] Running un-filtered mode: pass_all=True, max_symbols={self.max_symbols}")
        else:
            self.pass_all = False
            self.Log(f"[Initialize] Filtered run mode: pass_all=False, max_symbols={self.max_symbols}")

        self.volume_threshold = float(self.GetParameter("algo.volume_threshold", "1.0"))
        self.ivrv_threshold = float(self.GetParameter("algo.ivrv_threshold", "1.0"))
        
        self.max_loss_pct = float(self.GetParameter("risk.max_loss_pct", "70.0"))
        self.kelly_factor = float(self.GetParameter("risk.kelly.factor", "0.35"))
        self.kelly_period = int(self.GetParameter("risk.kelly.period", "30"))
        
        self.option_upper_filter = int(self.GetParameter("algo.option.upper_filter", "2"))
        self.option_lower_filter = int(self.GetParameter("algo.option.lower_filter", "-2"))
        self.option_max_exp_days = int(self.GetParameter("algo.option.max_exp_days", "150"))
        self.option_min_exp_days = int(self.GetParameter("algo.option.min_exp_days", "5"))
        self.min_days_between_contracts = int(self.GetParameter("algo.min_days_between", "60"))

        # Fix 3, 4 Parameters: Minimum IV Ratio and ITM Safety Guard
        self.min_iv_ratio = float(self.GetParameter("algo.min_iv_ratio", "1.15"))
        self.itm_safety_pct = float(self.GetParameter("risk.itm_safety_pct", "1.5"))

        # 4. Universes Setup (Coarse + EODHD Upcoming Earnings)
        self.AddUniverse(self.CoarseSelectionFunction)
        self.AddUniverse(EODHDUpcomingEarnings, self.UpcomingEarningsSelectionFunction)

        # 5. Scheduled final liquidation anchor
        self.RegisterFinalLiquidation(anchor_ticker="SPY", minutes_before_close=120)

    def CoarseSelectionFunction(self, coarse: List[CoarseFundamental]) -> List[Symbol]:
        """Filters initial universe by price (min_price and above) and daily volume (> 1.5M shares per day)."""
        min_price = float(self.GetParameter("univ.coarse.min_price", "15"))
        min_share_volume = float(self.GetParameter("univ.coarse.min_share_volume", "1500000"))

        filtered = [
            x for x in coarse 
            if x.HasFundamentalData
            and x.Price >= min_price
            and x.Volume is not None
            and x.Volume >= min_share_volume
        ]
        sorted_filtered = sorted(filtered, key=lambda x: x.DollarVolume, reverse=True)
        selected_symbols = [x.Symbol for x in sorted_filtered[:self.max_symbols]]
        self._active_coarse_tickers = {x.Value for x in selected_symbols}
        return selected_symbols

    def UpcomingEarningsSelectionFunction(self, earnings: List[EODHDUpcomingEarnings]) -> List[Symbol]:
        """Identifies stocks with upcoming earnings strictly between min_days_before_earnings and days_before_earnings."""
        selected = []
        min_cutoff = (self.Time + timedelta(days=self.min_days_before_earnings)).date()
        target_cutoff = (self.Time + timedelta(days=self.days_before_earnings)).date()
        active_tickers = getattr(self, "_active_coarse_tickers", set())

        for e in earnings:
            if e.ReportDate is not None:
                # Ensure the ticker string is present in valid liquid coarse universe to prevent missing factor file memory crashes
                if active_tickers and e.Symbol.Value not in active_tickers:
                    continue
                report_d = e.ReportDate.date()
                if min_cutoff <= report_d <= target_cutoff:
                    selected.append(e.Symbol)
                    self.earnings_calendar[e.Symbol] = e.ReportDate

                    if len(selected) >= self.max_symbols:
                        break
        return selected

    def OnSecuritiesChanged(self, changes: SecurityChanges) -> None:
        """Sets raw price data normalization for all added equities."""
        for security in changes.AddedSecurities:
            if security.Type == SecurityType.Equity:
                security.SetDataNormalizationMode(DataNormalizationMode.Raw)

    def OnData(self, data: Slice) -> None:
        """Core slice event handler performing position management and calendar spread entry scanning."""
        if self.IsWarmingUp:
            return

        # 0. Equity Assignment Emergency Liquidator: Immediately flatten short stock & cut paired long option leg via Market orders
        for holding in list(self.Portfolio.Values):
            if holding.Invested and holding.Symbol.SecurityType == SecurityType.Equity:
                open_orders = self.Transactions.GetOpenOrders(holding.Symbol)
                if not open_orders:
                    self.Log(f"[ASSIGNMENT EMERGENCY] Short option assigned! Flattening equity stock holding {holding.Symbol.Value} Qty: {holding.Quantity}")
                    self.MarketOrder(holding.Symbol, -holding.Quantity, tag="FLATTEN: Assignment Stock Emergency")
                    
                    # Immediately cut remaining paired long option leg for this underlying as fast as possible
                    underlying = holding.Symbol
                    if underlying in self.active_spreads:
                        pos = self.active_spreads[underlying]
                        back = pos.get("back")
                        if back and self.Portfolio.ContainsKey(back) and self.Portfolio[back].Invested:
                            back_qty = self.Portfolio[back].Quantity
                            self.Log(f"[ASSIGNMENT EMERGENCY] Immediately cutting paired long option leg {back.Value} Qty: {back_qty}")
                            self.MarketOrder(back, -back_qty, tag="FLATTEN: Emergency Long Leg Cut Post-Assignment")
                        self.UnsubscribeOption(pos.get("front"))
                        self.UnsubscribeOption(back)
                        self.active_spreads.pop(underlying, None)
                    else:
                        # Scan portfolio for any remaining option contracts on this underlying
                        for sec in list(self.Portfolio.Values):
                            if sec.Invested and sec.Symbol.SecurityType in [SecurityType.Option, SecurityType.IndexOption]:
                                sec_und = sec.Symbol.Underlying if hasattr(sec.Symbol, "Underlying") and sec.Symbol.Underlying else None
                                if sec.Symbol.Underlying == underlying or (sec_und and sec_und.Value == underlying.Value):
                                    self.Log(f"[ASSIGNMENT EMERGENCY] Cutting unhedged long option contract {sec.Symbol.Value} Qty: {sec.Quantity}")
                                    self.MarketOrder(sec.Symbol, -sec.Quantity, tag="FLATTEN: Emergency Option Cut Post-Assignment")

        # 0b. Orphaned Option Leg Sweeper: Flatten any single unhedged long or short option leg not active in active_spreads
        self.SweepOrphanedOptionLegs()

        # 1. Manage open positions (Time exit, DTE Safety)
        self.ManageOpenPositions(data)

        # 2. Process pending queued option orders
        self.ProcessPendingOrders(data)

        # 3. Clean up expired earnings cache
        self.PurgeExpiredEarnings()

        # 4. Scan upcoming earnings calendar candidates for spread entries
        # Video Timing Rule: Enter during afternoon pre-close hours (2:00 PM to 4:00 PM EST / hours 14 or 15)
        if self.Time.hour < 14 or self.Time.hour > 15:
            return

        for underlying, report_date in list(self.earnings_calendar.items()):
            # Guard 1: Skip if already invested
            if self.IsAlreadyInvested(underlying):
                continue

            # Guard 2: BMO vs AMC Timing Differentiation
            # AMC (After Market Close): Earnings released post-close on report_date. Entry window is afternoon of report_date itself (days_to_earnings == 0).
            # BMO (Before Market Open) / Default: Earnings released pre-open on report_date. Entry window is afternoon of day prior (days_to_earnings == 1).
            is_amc = report_date.hour >= 12 or getattr(report_date, "ReportTime", "") == "AMC"
            days_to_earnings = (report_date.date() - self.Time.date()).days

            if is_amc:
                if days_to_earnings != 0:
                    continue
            else:
                if days_to_earnings < self.min_days_before_earnings or days_to_earnings > self.days_before_earnings:
                    continue

            # Step A: Pre-calculate Stock-Level Metrics (vol_ratio, RV)
            metrics = self.GetUnderlyingMetricsCached(underlying, report_date)
            if metrics is None:
                continue

            vol_ratio, rv = metrics

            # Tier 1 Gate (Stock Level): Volume Ratio Gate (bypassed if pass_all=True)
            if not self.pass_all and vol_ratio < self.volume_threshold:
                continue

            # Step B: Get active Call option contracts
            contracts = self.GetCallOptionContractsCached(underlying, report_date)
            if not contracts:
                continue

            # Step C: Pair Call contracts by strike price
            pairs = self.MatchOptionContracts(contracts)
            if not pairs:
                continue

            # Step D: Evaluate candidates with 3-tier short-circuit cascade
            candidates = []
            for near_c, far_c in pairs:
                if not self._ensure_option_tradable(near_c) or not self._ensure_option_tradable(far_c):
                    continue

                m = self.CalculateMetrics(underlying, near_c, far_c, report_date, vol_ratio, rv)
                if m is not None:
                    candidates.append((m, near_c, far_c))

            if not candidates:
                continue

            # Select best candidate pair by ranking high IV slope penalized by distance from slightly OTM (+3%) target strike
            underlying_price = float(self.Securities[underlying].Price) if underlying in self.Securities else 1.0
            target_otm_price = underlying_price * 1.03
            def _rank_score(cand_tuple):
                m = cand_tuple[0]
                strike_dist_pct = abs(m["strike"] - target_otm_price) / underlying_price if underlying_price > 0 else 0.0
                # A negative slope is a GOOD slope (Front IV > Back IV). We rank by magnitude of negative slope penalized by distance from OTM target.
                return (-m["slope"]) / (1.0 + 10.0 * strike_dist_pct)

            best_candidate, best_front, best_back = max(candidates, key=_rank_score)

            # Determine Kelly position sizing
            qty = self.DeterminePositionSize(underlying, best_candidate)
            if qty <= 0:
                continue

            # Submit combo market order for calendar spread
            self.ExecuteCalendarSpread(underlying, best_front, best_back, qty, best_candidate, report_date)

    def IsAlreadyInvested(self, underlying: Symbol) -> bool:
        """Enforces single-ticker exclusivity and prevents duplicate positions on the same calendar day."""
        # 1. Daily Lockout: Lock out ticker if an entry was already submitted today for this underlying
        if (underlying, self.Time.date()) in getattr(self, "_traded_today", set()):
            return True

        if underlying in self.active_spreads:
            return True

        und_val = underlying.Value if hasattr(underlying, "Value") else str(underlying)

        for symbol in self.Portfolio.Keys:
            s_und = symbol.Underlying if hasattr(symbol, "Underlying") and symbol.Underlying else None
            s_und_val = s_und.Value if s_und and hasattr(s_und, "Value") else (str(s_und) if s_und else "")
            if symbol.SecurityType in [SecurityType.Option, SecurityType.IndexOption, SecurityType.FutureOption] and (symbol.Underlying == underlying or s_und_val == und_val):
                if self.Portfolio[symbol].Invested:
                    return True

        for contract, _, _ in self.pending_option_orders:
            c_und = contract.Underlying if hasattr(contract, "Underlying") and contract.Underlying else None
            c_und_val = c_und.Value if c_und and hasattr(c_und, "Value") else (str(c_und) if c_und else "")
            if contract.Underlying == underlying or c_und_val == und_val:
                return True

        open_orders = self.Transactions.GetOpenOrders()
        for order in open_orders:
            o_und = order.Symbol.Underlying if hasattr(order.Symbol, "Underlying") and order.Symbol.Underlying else None
            o_und_val = o_und.Value if o_und and hasattr(o_und, "Value") else (str(o_und) if o_und else "")
            if order.Symbol.SecurityType in [SecurityType.Option, SecurityType.IndexOption, SecurityType.FutureOption] and (order.Symbol.Underlying == underlying or o_und_val == und_val):
                return True

        return False

    @monitor_execution
    def GetCallOptionContractsCached(self, symbol: Symbol, earnings_time: datetime) -> List[Symbol]:
        """Gets Call option contracts expiring after earnings with daily OptionChainProvider caching."""
        cache_key = (symbol, self.Time.date())
        if cache_key in self._option_chain_cache:
            contracts = self._option_chain_cache[cache_key]
        else:
            try:
                contracts = self.OptionChainProvider.GetOptionContractList(symbol, self.Time)
                self._option_chain_cache[cache_key] = contracts if contracts else []
            except Exception as e:
                self.Debug(f"[GetCallOptionContractsCached] Option chain lookup exception for {symbol.Value}: {e}")
                self._option_chain_cache[cache_key] = []
                contracts = []

        if not contracts:
            return []

        price = 0.0
        if symbol in self.Securities and self.Securities[symbol].Price > 0:
            price = float(self.Securities[symbol].Price)

        if price <= 0.0:
            return []

        min_date = earnings_time.date()
        max_date = (earnings_time + timedelta(days=self.option_max_exp_days)).date()

        valid = [
            c for c in contracts
            if c.ID.OptionRight == OptionRight.Call
            and min_date < c.ID.Date.date() <= max_date
        ]

        if not valid:
            return []

        strikes = sorted(list({float(c.ID.StrikePrice) for c in valid}))
        if not strikes:
            return []

        # Target slightly OTM call strike (~0.40 Delta / +2% to +4% OTM strike above underlying price)
        otm_strikes = [s for s in strikes if s >= price]
        target_strike = otm_strikes[0] if otm_strikes else min(strikes, key=lambda s: abs(s - price))
        strike_idx = strikes.index(target_strike)
        
        start_idx = max(0, strike_idx + self.option_lower_filter)
        end_idx = min(len(strikes) - 1, strike_idx + self.option_upper_filter)
        allowed_strikes = set(strikes[start_idx:end_idx + 1])

        return [c for c in valid if float(c.ID.StrikePrice) in allowed_strikes]

    @monitor_execution
    def MatchOptionContracts(self, contracts: List[Symbol]) -> List[Tuple[Symbol, Symbol]]:
        """Pairs Call contracts for each strike:
        - Near leg (front): Strictly the NEAREST expiration date after earnings.
        - Far leg (back): The first expiration date that is >= min_days_between_contracts (e.g. 45 days) AFTER the near leg's expiration.
        """
        buckets = defaultdict(list)
        for c in contracts:
            key = (c.ID.OptionRight, float(c.ID.StrikePrice))
            buckets[key].append(c)

        matches: List[Tuple[Symbol, Symbol]] = []
        for key, lst in buckets.items():
            lst.sort(key=lambda x: x.ID.Date)
            if not lst:
                continue

            # Front leg is strictly the nearest expiration date after earnings
            near = lst[0]

            # Far leg is the first expiration at least min_days_between_contracts (45 days) after near leg's expiration
            for far in lst[1:]:
                days_gap = (far.ID.Date.date() - near.ID.Date.date()).days
                if days_gap >= self.min_days_between_contracts:
                    matches.append((near, far))
                    break

        return matches

    @monitor_execution
    def GetUnderlyingMetricsCached(self, underlying: Symbol, earnings_date: datetime) -> Optional[Tuple[float, float]]:
        """Calculates volume ratio and realized volatility with daily targeted caching."""
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
        if vol_col is None or close_col is None:
            return None

        vol_series = df[vol_col]
        if len(vol_series) < 31:
            return None

        recent_volume = float(vol_series.iloc[-1])
        avg_volume = float(vol_series.iloc[-31:-1].mean())
        if not avg_volume or math.isnan(recent_volume) or math.isnan(avg_volume) or avg_volume <= 0:
            return None

        vol_ratio = recent_volume / avg_volume

        close_series = df[close_col]
        if len(close_series) < 31:
            return None

        closes = close_series.iloc[-31:].astype(float).values
        if len(closes) < 31 or np.any(np.isnan(closes)) or np.any(closes <= 0):
            return None

        logrets = np.log(closes[1:] / closes[:-1])
        rv = float(logrets.std(ddof=1)) * math.sqrt(252.0)

        if math.isnan(rv) or rv <= 0:
            return None

        res = (vol_ratio, rv)
        self._metrics_cache[cache_key] = res
        return res

    @monitor_execution
    def CalculateMetrics(self, underlying: Symbol, front: Symbol, back: Symbol, earnings_date: datetime, vol_ratio: float, rv: float) -> Optional[Dict[str, Any]]:
        """Calculates slope, volume ratio, and IV/RV ratio using a 3-tier short-circuit early filtering cascade."""
        # Tier 1 Gate (Stock Level): Volume Ratio Gate (0 BSM Solves)
        if not self.pass_all and vol_ratio < self.volume_threshold:
            return None

        front_exp = front.ID.Date
        back_exp = back.ID.Date
        if not (front_exp < back_exp):
            return None
        if front_exp.date() <= max(earnings_date.date(), self.Time.date()):
            return None

        front_price = self.GetOptionMidPrice(front)
        underlying_price = float(self.Securities[underlying].Price) if underlying in self.Securities else 0.0

        if front_price <= 0.0 or underlying_price <= 0.0:
            return None

        T_front = max((front_exp - self.Time).total_seconds(), 0.0) / (365.0 * 24 * 3600)
        if T_front <= 0.0:
            return None

        # Tier 2 Gate (Near Option Level): Solve Near Option IV & Check IV/RV Ratio (Saved far option BSM solve!)
        near_iv = self._implied_volatility_newton(front.ID.OptionRight, underlying_price, float(front.ID.StrikePrice), T_front, self.risk_free_rate, front_price)
        if near_iv is None or near_iv <= 0.0:
            return None

        ivrv_ratio = near_iv / rv
        if not self.pass_all and ivrv_ratio < self.ivrv_threshold:
            return None

        # Tier 3 Gate (Far Option Level): Solve Far Option IV & Check IV Term Structure Slope
        back_price = self.GetOptionMidPrice(back)
        if back_price <= 0.0:
            return None

        T_back = max((back_exp - self.Time).total_seconds(), 0.0) / (365.0 * 24 * 3600)
        if T_back <= 0.0:
            return None

        far_iv = self._implied_volatility_newton(back.ID.OptionRight, underlying_price, float(back.ID.StrikePrice), T_back, self.risk_free_rate, back_price)
        if far_iv is None or far_iv <= 0.0:
            return None

        front_dte = int((front_exp.date() - self.Time.date()).days)
        back_dte = int((back_exp.date() - self.Time.date()).days)
        diff_dte = front_dte - back_dte

        if diff_dte >= 0:
            return None

        # Formula: (FRONT_IV - BACK_IV) / (front_dte - back_dte)
        # Note: diff_dte is negative (e.g. 7 - 52 = -45). A negative slope represents high front IV crunch potential (GOOD SLOPE).
        slope = (near_iv - far_iv) / float(diff_dte)
        if not self.pass_all and slope > self.slope_threshold:
            return None

        option_iv_ratio = near_iv / far_iv if far_iv > 0 else 1.0
        if not self.pass_all and option_iv_ratio < self.min_iv_ratio:
            return None

        front_sec = self.Securities[front] if front in self.Securities else None
        back_sec = self.Securities[back] if back in self.Securities else None
        
        front_bid = float(front_sec.BidPrice) if front_sec and hasattr(front_sec, "BidPrice") else 0.0
        front_ask = float(front_sec.AskPrice) if front_sec and hasattr(front_sec, "AskPrice") else 0.0
        back_bid = float(back_sec.BidPrice) if back_sec and hasattr(back_sec, "BidPrice") else 0.0
        back_ask = float(back_sec.AskPrice) if back_sec and hasattr(back_sec, "AskPrice") else 0.0

        front_spread = round(abs(front_ask - front_bid), 4)
        back_spread = round(abs(back_ask - back_bid), 4)
        comb_spread = round(front_spread + back_spread, 4)

        if not self.pass_all and self.max_spread_threshold > 0:
            if front_spread > self.max_spread_threshold or back_spread > self.max_spread_threshold or comb_spread > self.max_spread_threshold:
                return None

        return {
            "slope": round(float(slope), 5),
            "front_iv": round(float(near_iv), 5),
            "back_iv": round(float(far_iv), 5),
            "iv_ratio": round(float(option_iv_ratio), 5),
            "front_dte": front_dte,
            "back_dte": back_dte,
            "vol_ratio": round(float(vol_ratio), 5),
            "ivrv_ratio": round(float(ivrv_ratio), 5),
            "strike": float(front.ID.StrikePrice),
            "front_price": front_price,
            "back_price": back_price,
            "front_spread": front_spread,
            "back_spread": back_spread,
            "comb_spread": comb_spread,
            "edate": earnings_date.strftime("%Y-%m-%d")
        }

    def DeterminePositionSize(self, underlying: Symbol, metrics: Dict[str, Any]) -> int:
        """Determines options quantity utilizing Kelly Criterion sizing."""
        history = self.trade_history[underlying]
        
        if len(history) < 5:
            kelly_fraction = 0.10
        else:
            wins = sum(1 for x in history if x["pnl"] > 0)
            losses = sum(1 for x in history if x["pnl"] <= 0)
            win_rate = wins / len(history)
            
            avg_win = np.mean([x["pnl"] for x in history if x["pnl"] > 0]) if wins > 0 else 0.0
            avg_loss = abs(np.mean([x["pnl"] for x in history if x["pnl"] <= 0])) if losses > 0 else 1.0
            win_loss_ratio = avg_win / avg_loss if avg_loss > 0 else 1.0
            
            kelly_fraction = win_rate - (1 - win_rate) / win_loss_ratio

        kelly_fraction = max(0.0, min(kelly_fraction, 1.0)) * self.kelly_factor
        
        # Scale dollar allocation to target ~$1,000 per trade
        max_trade_dollar_cap = float(self.GetParameter("risk.max_trade_allocation", "1000.0"))
        allocation = min(self.Portfolio.TotalPortfolioValue * kelly_fraction, max_trade_dollar_cap)

        spread_cost = abs(metrics["back_price"] - metrics["front_price"]) * 100.0
        if spread_cost <= 0.0:
            return 0

        raw_qty = int(math.floor(allocation / spread_cost))
        
        # Cap combo contracts at 10 (10 short + 10 long = 20 contracts total per trade)
        max_combo_contracts = int(self.GetParameter("risk.max_combo_contracts", "10"))
        qty = max(0, min(raw_qty, max_combo_contracts))
        return qty

    def LogTradeRecord(self, action: str, underlying: Symbol, front: Symbol, back: Symbol, qty: int, entry_price: float, metrics: Dict[str, Any], pk: str, exit_price: float = 0.0, pnl: float = 0.0, exit_reason: str = "") -> None:
        """Logs structured JSON record of trade metadata for BigQuery ingestion."""
        param_dict = {
            "front_iv": round(float(metrics.get("front_iv", 0.0)), 5),
            "back_iv": round(float(metrics.get("back_iv", 0.0)), 5),
            "iv_ratio": round(float(metrics.get("iv_ratio", 0.0)), 5),
            "front_dte": int(metrics.get("front_dte", 0)),
            "back_dte": int(metrics.get("back_dte", 0)),
            "vol_ratio": round(float(metrics.get("vol_ratio", 0.0)), 5),
            "slope": round(float(metrics.get("slope", 0.0)), 5),
            "ivrv_ratio": round(float(metrics.get("ivrv_ratio", 0.0)), 5),
            "comb_spread": round(float(metrics.get("comb_spread", 0.0)), 4),
            "mae_pct": round(float(metrics.get("mae_pct", 0.0)), 2),
            "mfe_pct": round(float(metrics.get("mfe_pct", 0.0)), 2),
            "holding_hours": round(float(metrics.get("holding_hours", 0.0)), 2),
            "exit_reason": exit_reason
        }
        
        record = {
            "pk": pk,
            "backtestId": self.backtest_run_id,
            "backtest_run_id": self.backtest_run_id,
            "algo_code": "4EVC",
            "timestamp": self.Time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "underlying": underlying.Value,
            "action": action,
            "qty": qty,
            "strike": float(front.ID.StrikePrice),
            "near_expiry": str(front.ID.Date.date()),
            "far_expiry": str(back.ID.Date.date()),
            "earnings_date": str(metrics.get("edate", "")),
            "vol_ratio": round(float(metrics.get("vol_ratio", 0.0)), 5),
            "slope": round(float(metrics.get("slope", 0.0)), 5),
            "ivrv_ratio": round(float(metrics.get("ivrv_ratio", 0.0)), 5),
            "entry_price": round(entry_price, 5),
            "exit_price": round(exit_price, 5),
            "pnl": round(pnl, 5),
            "exit_reason": exit_reason,
            "parameters": json.dumps(param_dict, separators=(',', ':'))
        }
        self.Log(f"[BIGQUERY_TRADE_RECORD] {json.dumps(record, separators=(',', ':'))}")

    def OnOrderEvent(self, orderEvent: OrderEvent) -> None:
        """Handles order execution events, confirming entry and exit fills to calculate exact 100% executed fill prices."""
        order_id = orderEvent.OrderId
        if orderEvent.Status == OrderStatus.Filled:
            # 1. Entry Order Fill Handling
            if order_id in self._pending_entry_tickets:
                info = self._pending_entry_tickets[order_id]
                underlying = info["underlying"]
                symbol = orderEvent.Symbol
                fill_price = float(orderEvent.FillPrice)
                
                info.setdefault("entry_fills", {})[symbol] = fill_price

                # When both entry legs fill, calculate actual net debit paid and log OPEN record
                if info["front"] in info["entry_fills"] and info["back"] in info["entry_fills"]:
                    if not info.get("logged_open", False):
                        info["logged_open"] = True
                        front_fill = info["entry_fills"][info["front"]]
                        back_fill = info["entry_fills"][info["back"]]
                        actual_debit = round(abs(back_fill - front_fill), 5)
                        if actual_debit > 0:
                            info["entry_price"] = actual_debit

                        self.active_spreads[underlying] = info
                        self.LogTradeRecord("OPEN", underlying, info["front"], info["back"], info["qty"], info["entry_price"], info["metrics"], pk=info["pk"])
                        self.Log(f"[ORDER EVENT FILL] Confirmed entry fill for {underlying.Value} at actual debit ${info['entry_price']:.2f}. Added to active spreads.")
                        
                        # Clean up pending entry tickets
                        tickets = info.get("tickets", [])
                        for t in tickets:
                            self._pending_entry_tickets.pop(t.OrderId, None)

            # 2. Exit Order Fill Handling (Calculates actual 100% executed fill prices)
            elif order_id in self._pending_exit_tickets:
                info = self._pending_exit_tickets[order_id]
                underlying = info["underlying"]
                symbol = orderEvent.Symbol
                fill_price = float(orderEvent.FillPrice)

                info.setdefault("exit_fills", {})[symbol] = fill_price

                # Check if both exit legs have completed fill
                if info["front"] in info["exit_fills"] and info["back"] in info["exit_fills"]:
                    if not info.get("logged_close", False):
                        info["logged_close"] = True
                        front_exit_fill = info["exit_fills"][info["front"]]
                        back_exit_fill = info["exit_fills"][info["back"]]
                        
                        # Actual net exit credit received from 100% real execution fills
                        actual_exit_credit = round(back_exit_fill - front_exit_fill, 5)
                        # Clamped non-negative exit credit for long debit spread
                        exit_price = max(0.0, actual_exit_credit)
                        
                        entry_debit = info["entry_price"]
                        realized_pnl = round((exit_price - entry_debit) / entry_debit, 5) if entry_debit > 0 else 0.0
                        
                        # Enforce max loss floor of -100% (-1.0) for long calendar debit spread
                        pnl = max(-1.0, realized_pnl)
                        
                        exit_reason = info.get("exit_reason", "Liquidation")
                        pk = info.get("pk", "unknown")
                        qty = info["qty"]

                        entry_time = info.get("entry_time", self.Time)
                        holding_hours = round((self.Time - entry_time).total_seconds() / 3600.0, 2)

                        metrics = {
                            "vol_ratio": info["vol_ratio"],
                            "slope": info["slope"],
                            "ivrv_ratio": info["ivrv_ratio"],
                            "mae_pct": info.get("mae_pct", 0.0),
                            "mfe_pct": info.get("mfe_pct", 0.0),
                            "holding_hours": holding_hours
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
                        self.Log(f"[ORDER EVENT EXIT FILL] Confirmed exit fill for {underlying.Value} at credit ${exit_price:.2f} (Realized PnL: {pnl*100:.2f}% | MAE: {info.get('mae_pct', 0.0):.2f}% | MFE: {info.get('mfe_pct', 0.0):.2f}% | Duration: {holding_hours}h).")

                        self.UnsubscribeOption(info["front"])
                        self.UnsubscribeOption(info["back"])
                        self.active_spreads.pop(underlying, None)
                        
                        # Clean up pending exit tickets
                        for o_id in list(self._pending_exit_tickets.keys()):
                            if self._pending_exit_tickets[o_id] is info:
                                self._pending_exit_tickets.pop(o_id, None)

        elif orderEvent.Status in [OrderStatus.Canceled, OrderStatus.Invalid]:
            if order_id in self._pending_entry_tickets:
                self._pending_entry_tickets.pop(order_id, None)
            if order_id in self._pending_exit_tickets:
                self._pending_exit_tickets.pop(order_id, None)

    def ExecuteCalendarSpread(self, underlying: Symbol, front: Symbol, back: Symbol, qty: int, metrics: Dict[str, Any], report_date: datetime) -> None:
        """Executes a native QuantConnect CallCalendar strategy order for the calendar spread."""
        if not self._ensure_option_tradable(front) or not self._ensure_option_tradable(back):
            return

        # Prepare legs for atomic combo limit order
        legs = [
            Leg.Create(front, -1),  # Sell near-term option
            Leg.Create(back, 1)     # Buy far-term option
        ]

        natural_ask = metrics["back_price"] - metrics["front_price"]
        
        # In pass_all / data collection mode, execute as market order if natural ask is <= 0
        if self.pass_all and natural_ask <= 0:
            tickets = self.ComboMarketOrder(legs, qty)
        else:
            if self.pass_all:
                limit_price = round(natural_ask * (1.0 + self.alpha_spread), 2)
            else:
                limit_price = round(natural_ask, 2)
            limit_price = max(0.01, limit_price)
            tickets = self.ComboLimitOrder(legs, qty, limit_price)

        self.trade_id_counter += 1
        pk = f"{self.backtest_run_id}_{underlying.Value}_{self.trade_id_counter}"

        # Target exit time: 10:00 AM EST on the morning after earnings announcement
        exit_date = (report_date + timedelta(days=self.days_after_earnings + 1)).date()
        target_exit_time = datetime.combine(exit_date, time(self.exit_hour, 0))

        position_info = {
            "pk": pk,
            "underlying": underlying,
            "front": front,
            "back": back,
            "qty": qty,
            "entry_price": abs(metrics["back_price"] - metrics["front_price"]),
            "entry_time": self.Time,
            "report_date": report_date,
            "exit_time": target_exit_time,
            "tickets": tickets,
            "slope": metrics["slope"],
            "vol_ratio": metrics["vol_ratio"],
            "ivrv_ratio": metrics["ivrv_ratio"],
            "mae_pct": 0.0,
            "mfe_pct": 0.0,
            "metrics": metrics,
            "entry_fills": {},
            "exit_fills": {}
        }

        # Track position info for active spread and register pending entry tickets
        self.active_spreads[underlying] = position_info

        # Enforce single-entry per calendar day for this ticker and remove from earnings calendar
        self._traded_today.add((underlying, self.Time.date()))
        self.earnings_calendar.pop(underlying, None)

        near_tag = self.BuildOrderTag(underlying, front, back, metrics, "SHORT")
        far_tag = self.BuildOrderTag(underlying, front, back, metrics, "LONG")

        if tickets:
            for ticket in tickets:
                self._pending_entry_tickets[ticket.OrderId] = position_info
                try:
                    uf = UpdateOrderFields()
                    uf.Tag = near_tag if ticket.Symbol == front else far_tag
                    ticket.Update(uf)
                except Exception as e:
                    self.Debug(f"[TagUpdate] Failed for {ticket.Symbol.Value}: {e}")

        self.Log(f"[TRADE SIGNAL ENTRY] Time: {self.Time} | Ticker: {underlying.Value} | Qty: {qty} | Front: {front.Value} | Back: {back.Value} | Slope: {metrics['slope']:.5f} | VolRatio: {metrics['vol_ratio']:.2f} | IV/RV: {metrics['ivrv_ratio']:.2f} | PassAll: {self.pass_all}")

    def ManageOpenPositions(self, data: Slice) -> None:
        """Monitors positions for time-based targets, stop losses, and expiration risks."""
        liquidated_underlyings = []

        for underlying, position in list(self.active_spreads.items()):
            # Update MAE and MFE on every bar tick
            entry_debit = float(position.get("entry_price", 0.0))
            front = position.get("front")
            back = position.get("back")
            if front and back and entry_debit > 0:
                front_sec = self.Securities.get(front)
                back_sec = self.Securities.get(back)
                if front_sec and back_sec:
                    f_ask = float(front_sec.AskPrice) if hasattr(front_sec, "AskPrice") else 0.0
                    b_bid = float(back_sec.BidPrice) if hasattr(back_sec, "BidPrice") else 0.0
                    if f_ask > 0 and b_bid > 0:
                        cur_credit = b_bid - f_ask
                        cur_ret_pct = round(((cur_credit - entry_debit) / entry_debit) * 100.0, 2)
                        position["mae_pct"] = min(position.get("mae_pct", 0.0), cur_ret_pct)
                        position["mfe_pct"] = max(position.get("mfe_pct", 0.0), cur_ret_pct)

            entry_time = position.get("entry_time", self.Time)
            
            # Guard: Require position to have been entered on a prior calendar date before time-based exit can trigger
            is_different_day = self.Time.date() > entry_time.date()

            if position.get("is_liquidating", False):
                continue

            # Exit logic: Exit 1 hour post-market-open after earnings
            if self.Time >= position.get("exit_time", datetime.max):
                placed = self.LiquidateSpread(underlying, "Time-Based Exit (1-Hour Post-Market-Open Crush)")
                if placed:
                    liquidated_underlyings.append(underlying)
                continue

        for u in liquidated_underlyings:
            self.active_spreads.pop(u, None)

    def SweepOrphanedOptionLegs(self) -> None:
        """Scans portfolio for any option contracts held without an active paired calendar spread entry."""
        active_contracts = set()
        active_underlyings = set(self.active_spreads.keys())

        for pos in self.active_spreads.values():
            if "front" in pos:
                active_contracts.add(pos["front"])
            if "back" in pos:
                active_contracts.add(pos["back"])

        for pos in getattr(self, "_pending_exit_tickets", {}).values():
            if isinstance(pos, dict):
                if "front" in pos:
                    active_contracts.add(pos["front"])
                if "back" in pos:
                    active_contracts.add(pos["back"])

        for sec in list(self.Portfolio.Values):
            if sec.Invested and sec.Symbol.SecurityType in [SecurityType.Option, SecurityType.IndexOption]:
                if sec.Symbol in active_contracts:
                    continue
                
                und = sec.Symbol.Underlying if hasattr(sec.Symbol, "Underlying") and sec.Symbol.Underlying else None
                if und and und in active_underlyings:
                    continue

                open_orders = self.Transactions.GetOpenOrders(sec.Symbol)
                if not open_orders:
                    self.Log(f"[ORPHAN SWEEPER] Liquidating unhedged orphaned option leg: {sec.Symbol.Value} Qty: {sec.Quantity}")
                    self.MarketOrder(sec.Symbol, -sec.Quantity, tag="FLATTEN: Orphaned Long Leg Sweep")

    def LiquidateSpread(self, underlying: Symbol, tag: str) -> bool:
        """Offsetting combo strategy order to flatten active calendar spread legs together."""
        if underlying not in self.active_spreads:
            return False

        position = self.active_spreads[underlying]
        if position.get("is_liquidating", False):
            return False

        front = position["front"]
        back = position["back"]
        qty = position["qty"]
        pk = position.get("pk", "unknown")

        front_qty = abs(self.Portfolio[front].Quantity) if self.Portfolio.ContainsKey(front) else 0
        back_qty = abs(self.Portfolio[back].Quantity) if self.Portfolio.ContainsKey(back) else 0

        # Absolute Guard: Do NOT send liquidation orders if portfolio holds 0 contracts for both legs
        if front_qty == 0 and back_qty == 0:
            self.Debug(f"[LiquidateSpread] Purging active_spreads for {underlying.Value}: legs not held in portfolio.")
            self.UnsubscribeOption(front)
            self.UnsubscribeOption(back)
            self.active_spreads.pop(underlying, None)
            return True

        # Close legs together using atomic combo limit order (floor limit price at $0.00 so exit credit is never negative)
        combo_qty = min(front_qty, back_qty)
        exit_tickets = []
        if combo_qty > 0:
            exit_legs = [
                Leg.Create(front, 1),   # Buy back short near call
                Leg.Create(back, -1)   # Sell long far call
            ]
            front_sec = self.Securities[front] if front in self.Securities else None
            back_sec = self.Securities[back] if back in self.Securities else None
            front_ask = float(front_sec.AskPrice) if front_sec and hasattr(front_sec, "AskPrice") else 0.0
            back_bid = float(back_sec.BidPrice) if back_sec and hasattr(back_sec, "BidPrice") else 0.0

            net_entry_debit = float(position.get("net_debit_paid", 0.0))
            max_allowed_exit_debit = max(net_entry_debit * 0.05, 0.05) if net_entry_debit > 0 else 0.05

            if front_ask > 0 and back_bid > 0:
                natural_credit = back_bid - front_ask
                if natural_credit >= -max_allowed_exit_debit:
                    limit_credit = round(natural_credit, 2)
                    if limit_credit >= 0.01:
                        exit_tickets = self.ComboLimitOrder(exit_legs, combo_qty, limit_credit, tag=tag)
                    else:
                        exit_tickets = self.ComboMarketOrder(exit_legs, combo_qty, tag=tag)
                else:
                    # If natural credit is more negative than -max_allowed_exit_debit, closing early costs excessive debit (> -105% loss).
                    # Skip market liquidation; let short near call be assigned/expire naturally so long far call hedges it, capping loss at -100%.
                    self.Log(f"LiquidateSpread: Skipped early exit for {underlying} (exit credit {natural_credit:.2f} exceeds -105% loss floor relative to entry debit {net_entry_debit:.2f})")
                    return False
            else:
                # If quotes are unavailable or zero, do not force market exit if it might cost debit
                self.Log(f"LiquidateSpread: Insufficient quote data to close {underlying} (front_ask={front_ask}, back_bid={back_bid})")
                return False

        if not exit_tickets:
            return False

        # Mark position as liquidating only if exit tickets were submitted
        position["is_liquidating"] = True
        position["exit_reason"] = tag

        # Cancel any pending entry tickets if unfilled
        tickets = position.get("tickets", [])
        for t in tickets:
            if t.Status in [OrderStatus.Submitted, OrderStatus.New]:
                try:
                    t.Cancel("Canceling pending entry ticket prior to liquidation")
                except Exception:
                    pass

        # Register exit tickets for tracking 100% real fill prices in OnOrderEvent
        close_tag = f"CLOSE:{tag}"
        for t in exit_tickets:
            self._pending_exit_tickets[t.OrderId] = position
            try:
                uf = UpdateOrderFields()
                uf.Tag = close_tag
                t.Update(uf)
            except Exception:
                pass

        return True

    def ProcessPendingOrders(self, data: Slice) -> None:
        """Drains pending orders waiting for market feed availability."""
        still_pending = []
        for contract, qty, tag in self.pending_option_orders:
            if data.ContainsKey(contract) and self.Securities[contract].HasData and self.Securities[contract].Price > 0:
                self.MarketOrder(contract, qty, tag=f"fulfilled {tag}")
            else:
                still_pending.append((contract, qty, tag))
        self.pending_option_orders = still_pending

    def PurgeExpiredEarnings(self, purge_days: int = 5) -> None:
        """Cleans calendar cache of old announcements, daily caches, and uninvested option securities."""
        cutoff = self.Time - timedelta(days=purge_days)
        self.earnings_calendar = {
            sym: dt for sym, dt in self.earnings_calendar.items() if dt >= cutoff
        }

        # Purge daily metrics and option chain caches older than 5 days
        cutoff_date = cutoff.date()
        self._metrics_cache = {
            k: v for k, v in self._metrics_cache.items() if k[1] >= cutoff_date
        }
        self._option_chain_cache = {
            k: v for k, v in self._option_chain_cache.items() if k[1] >= cutoff_date
        }

        # Explicitly remove uninvested option securities to prevent LEAN memory growth
        active_contracts = self._get_active_spread_contracts()
        for sec in list(self.Securities.Values):
            if sec.Symbol.SecurityType in [SecurityType.Option, SecurityType.IndexOption] and not sec.Invested:
                if sec.Symbol not in active_contracts:
                    try:
                        self.RemoveOptionContract(sec.Symbol)
                    except Exception:
                        try:
                            self.RemoveSecurity(sec.Symbol)
                        except Exception:
                            pass
                    if sec.Symbol in self._subscribed_options:
                        self._subscribed_options.remove(sec.Symbol)

        # Force explicit Python Garbage Collection every 5 days to unhook PyObject wrappers
        try:
            import gc
            gc.collect()
        except Exception:
            pass

    def RegisterFinalLiquidation(self, anchor_ticker: str = "SPY", minutes_before_close: int = 120) -> None:
        """Schedules market-close final liquidation rule near EndDate."""
        self._final_liquidated = False
        self._algo_end_date = self.EndDate.date()
        anchor = self.AddEquity(anchor_ticker, Resolution.Hour).Symbol

        def _maybe_final_liquidation():
            if self._final_liquidated:
                return
            if (self.Time.date() + timedelta(days=1)) >= self._algo_end_date:
                self.Transactions.CancelOpenOrders()
                for underlying in list(self.active_spreads.keys()):
                    self.LiquidateSpread(underlying, "End-of-Backtest Liquidation")
                self.Liquidate()
                self._final_liquidated = True

        def _cancel_unfilled_entry_orders():
            open_orders = self.Transactions.GetOpenOrders()
            for order in open_orders:
                if order.Status in [OrderStatus.Submitted, OrderStatus.New]:
                    try:
                        self.Transactions.CancelOrder(order.Id, "EOD: Canceling unfilled entry limit order")
                    except Exception as e:
                        self.Debug(f"[EOD Cancel] Failed for order #{order.Id}: {e}")

            # Clean up active_spreads ONLY for positions where NO tickets filled AND NO option legs are held
            to_purge = []
            for underlying, pos in list(self.active_spreads.items()):
                front = pos.get("front")
                back = pos.get("back")
                entry_fills = pos.get("entry_fills", {})
                
                fq = abs(self.Portfolio[front].Quantity) if front and self.Portfolio.ContainsKey(front) else 0
                bq = abs(self.Portfolio[back].Quantity) if back and self.Portfolio.ContainsKey(back) else 0
                
                # If neither leg is invested AND entry_fills has no fills, then purge
                if fq == 0 and bq == 0 and not entry_fills:
                    to_purge.append(underlying)
            for u in to_purge:
                self.active_spreads.pop(u, None)

        self.Schedule.On(
            self.DateRules.EveryDay(anchor),
            self.TimeRules.BeforeMarketClose(anchor, 5),
            _cancel_unfilled_entry_orders
        )

        self.Schedule.On(
            self.DateRules.EveryDay(anchor),
            self.TimeRules.BeforeMarketClose(anchor, minutes_before_close),
            _maybe_final_liquidation
        )

    def OnEndOfAlgorithm(self) -> None:
        """Native LEAN lifecycle hook: Closes 100% of open positions on final backtest bar with structured exit tag."""
        self.Log(f"[OnEndOfAlgorithm] Backtest ending. Liquidating {len(self.active_spreads)} active spreads...")
        
        # 1. Liquidate all active calendar spreads with exit_reason tag for BigQuery grouping
        for underlying in list(self.active_spreads.keys()):
            self.LiquidateSpread(underlying, "End-of-Backtest Liquidation")

        # 2. Cancel any remaining open orders
        try:
            self.Transactions.CancelOpenOrders()
        except Exception:
            pass

        # 3. Liquidate any leftover portfolio securities
        try:
            self.Liquidate()
        except Exception:
            pass

    def _ensure_option_tradable(self, contract: Symbol, res: Resolution = Resolution.Hour) -> bool:
        """Subscribes to option contract safely handling delisted underlying assets."""
        if not self.Securities.ContainsKey(contract):
            try:
                o = self.AddOptionContract(contract, res)
                o.SetOptionAssignmentModel(NullOptionAssignmentModel())
            except Exception as e:
                self.Debug(f"[_ensure_option_tradable] Cannot subscribe to {contract.Value} (delisted or invalid): {e}")
                return False
        self._subscribed_options.add(contract)

        u = contract.Underlying
        if self.Securities.ContainsKey(u):
            self.Securities[u].SetDataNormalizationMode(DataNormalizationMode.Raw)
        return True

    def UnsubscribeOption(self, contract: Symbol) -> None:
        """Purges contract from active algorithm tracking and explicitly removes security from LEAN engine RAM."""
        try:
            if contract in self._subscribed_options:
                self._subscribed_options.remove(contract)
            if self.Securities.ContainsKey(contract):
                try:
                    self.RemoveOptionContract(contract)
                except Exception:
                    try:
                        self.RemoveSecurity(contract)
                    except Exception:
                        pass
        except Exception as e:
            self.Debug(f"[UnsubscribeOption] Failed to remove tracking for {contract.Value}: {e}")

    def _get_active_spread_contracts(self) -> Set[Symbol]:
        """Helper returning all option symbols currently held in active spreads."""
        res = set()
        for pos in self.active_spreads.values():
            if "front" in pos:
                res.add(pos["front"])
            if "back" in pos:
                res.add(pos["back"])
        return res

    def GetOptionMidPrice(self, sym: Symbol) -> float:
        """Retrieves bid/ask mid-price directly from Securities (NO History calls)."""
        if sym in self.Securities:
            sec = self.Securities[sym]
            bid = float(sec.BidPrice)
            ask = float(sec.AskPrice)
            if bid > 0 and ask > 0:
                return (bid + ask) / 2.0
            if float(sec.Price) > 0:
                return float(sec.Price)
        return 0.0

    def BuildOrderTag(self, symbol: Symbol, front: Symbol, back: Symbol, metrics: Dict[str, Any], side: str, trade_id: Optional[str] = None) -> str:
        """Generates compact JSON order tag."""
        t_id = trade_id or metrics.get("trade_id") or f"T_{symbol.Value}_{self.Time.strftime('%Y%m%d_%H%M%S')}"
        payload = {
            "u": symbol.Value,
            "trade_id": t_id,
            "leg": side,
            "k": metrics.get("strike", float(front.ID.StrikePrice)),
            "near": str(front.ID.Date.date()),
            "far": str(back.ID.Date.date()),
            "edate": str(metrics.get("edate", "")),
            "front_iv": round(float(metrics.get("front_iv", 0.0)), 5),
            "back_iv": round(float(metrics.get("back_iv", 0.0)), 5),
            "iv_ratio": round(float(metrics.get("iv_ratio", 0.0)), 5),
            "front_dte": int(metrics.get("front_dte", 0)),
            "back_dte": int(metrics.get("back_dte", 0)),
            "slope": round(float(metrics.get("slope", 0.0)), 5),
            "ivrv": round(float(metrics.get("ivrv_ratio", 0.0)), 5),
            "vol_ratio": round(float(metrics.get("vol_ratio", 0.0)), 5),
            "spread": round(float(metrics.get("comb_spread", 0.0)), 4),
            "ts": self.Time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        s = json.dumps(payload, separators=(",", ":"))
        return s[:1024]

    # --- High-Performance Black-Scholes and Newton-Raphson Solver ---
    def _bs_price(self, right: OptionRight, S: float, K: float, T: float, r: float, sigma: float) -> float:
        if sigma <= 0.0 or T <= 0.0 or S <= 0.0 or K <= 0.0:
            return 0.0
        d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)
        if right == OptionRight.Call:
            return S * _norm_cdf(d1) - K * math.exp(-r * T) * _norm_cdf(d2)
        else:
            return K * math.exp(-r * T) * _norm_cdf(-d2) - S * _norm_cdf(-d1)

    def _vega(self, S: float, K: float, T: float, r: float, sigma: float) -> float:
        if sigma <= 0.0 or T <= 0.0 or S <= 0.0 or K <= 0.0:
            return 0.0
        d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
        return S * _norm_pdf(d1) * math.sqrt(T)

    @monitor_execution
    def _implied_volatility_newton(self, right: OptionRight, S: float, K: float, T: float, r: float, market_price: float) -> Optional[float]:
        """Fast Newton-Raphson IV solver using pure math.erf standard normal CDF."""
        if right == OptionRight.Call:
            intrinsic = max(S - K * math.exp(-r * T), 0.0)
        else:
            intrinsic = max(K * math.exp(-r * T) - S, 0.0)
        if market_price <= intrinsic:
            return None

        sigma = 0.25
        for _ in range(20):
            price = self._bs_price(right, S, K, T, r, sigma)
            v = self._vega(S, K, T, r, sigma)
            if v < 1e-8:
                return None
            diff = price - market_price
            if abs(diff) < 1e-4:
                return sigma
            sigma -= diff / v
            if sigma <= 0.0 or sigma > 6.0:
                return None
        return None
