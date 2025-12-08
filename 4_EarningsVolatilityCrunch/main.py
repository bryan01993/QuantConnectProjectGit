# region imports
import math

from AlgorithmImports import *
from QuantConnect import Symbol
from QuantConnect.Data.Fundamental import FineFundamental
from QuantConnect.DataSource import EODHDUpcomingEarnings
from QuantConnect.Securities import *
from collections import defaultdict
from math import log, sqrt, exp
from scipy.stats import norm
from QuantConnect.Securities.Option import QLOptionPriceModel
from QuantConnect.Orders import UpdateOrderFields
from datetime import timedelta, datetime, date
import pandas as pd
from PropietaryCode.decorators import monitor_execution
from math import sqrt
import json

# Global storage dictionary
OBJECT_LOG = {}
# endregion

import io
import csv
from datetime import datetime


def describe_object(obj, obj_name="unknown"):
    description = {
        "name": obj_name,
        "type": str(type(obj)),
        "attributes": {},
        "methods": []
    }

    for attr in dir(obj):
        if attr.startswith("__"):
            continue
        try:
            value = getattr(obj, attr)
            if callable(value):
                description["methods"].append(attr)
            else:
                description["attributes"][attr] = value
        except Exception as e:
            description["attributes"][attr] = f"<Error reading: {e}>"

    # Append to global OBJECT_LOG
    OBJECT_LOG[obj_name] = description


class EarningsVolatilityCrunch(QCAlgorithm):

    @monitor_execution
    def Initialize(self):
        # --- Run OnData on a daily cadence ---
        # Use daily resolution across the board so OnData fires once per trading day
        self.UniverseSettings.Resolution = Resolution.DAILY
        self.UniverseSettings.FillForward = False

        # Brokerage & fee model (Interactive Brokers)
        self.SetBrokerageModel(BrokerageName.INTERACTIVE_BROKERS_BROKERAGE)

        # Dates, cash, warmup
        self.SetStartDate(*map(int, self.GetParameter("exec.start_date").split('-')))
        self.SetEndDate(*map(int, self.GetParameter("exec.end_date").split('-')))
        self.SetCash(self.GetParameter("exec.initial_amount"))
        self.SetWarmUp(5, Resolution.Daily)

        # Universes
        self.AddUniverse(self.CoarseSelectionFunction)
        self.AddUniverse(EODHDUpcomingEarnings, self.UpcomingEarningsSelectionFunction)

        # Ensure all equities added (by you or by option legs) are RAW
        self.UniverseSettings.DataNormalizationMode = DataNormalizationMode.Raw

        # State
        self.earnings_calendar = {}  # Cache for earnings dates
        self.symbols_total = 0
        self.symbols_optionable = 0
        self.slope_results = {}
        self.volume_results = {}
        self.ivrv_results = {}
        self.added_equities = set()
        self.latest_iv_data = {}
        self.pending_option_orders = []  # list[tuple[Symbol, int, str]]
        self._last_earnings_scan = None
        self._processed_earnings = {}  # {Symbol: last_processed_time}
        self.symbol_states = {}  # by underlying/strategy key
        self.bar_size = Resolution.Hour  # whatever you use
        self.trade_all = True  # bool for Debugging trades of all sorts vs only filtered trades
        self.register_final_liquidation(self, anchor_ticker="SPY", minutes_before_close=120)
        # Stores the most recent snapshot of calendar candidates (by underlying)
        self.calendar_candidates = {}
        # Same-bar de-dup guard (calendar_id set)
        self._calendars_seen_this_bar = set()
        self.near_candidates = {}
        self.far_candidates = {}
        self._candidates_built_at = None

    @monitor_execution
    def OnEndOfDay(self):
        tpv = self.Portfolio.TotalPortfolioValue or 0
        if tpv == 0:
            return

        holdings = [
            (symbol, holding.HoldingsValue / tpv)
            for symbol, holding in self.Portfolio.items()
            if holding.Invested
        ]
        if not holdings:
            return

        for sym, pct in sorted(holdings, key=lambda x: x[1], reverse=True)[:5]:
            sec_type = sym.ID.SecurityType
            self.Debug(f"{sym.Value} | {sec_type} | {pct:.2%}")

    # @monitor_execution
    def CoarseSelectionFunction(self, coarse: List[CoarseFundamental]) -> List[Symbol]:
        lower_price = int(self.GetParameter("univ.coarse.min_price"))  # Define lower price bound
        upper_price = int(self.GetParameter("univ.coarse.max_price"))  # Define upper price bound
        min_volume = int(self.GetParameter("univ.coarse.dollar_volume"))

        return [x.Symbol for x in coarse if x.HasFundamentalData
                and lower_price <= x.Price <= upper_price
                and x.Volume is not None
                and x.Volume >= min_volume][
               :int(self.GetParameter("univ.coarse.max_symbols"))]

    # @monitor_execution
    def UpcomingEarningsSelectionFunction(self, earnings: List[EODHDUpcomingEarnings]) -> List[Symbol]:
        selected = []
        max_items = 100

        for e in earnings:
            if e.ReportDate <= self.Time + timedelta(days=int(self.GetParameter("algo.days_before_earnings"))):
                if self.OptionChainProvider.GetOptionContractList(e.Symbol, self.Time):
                    selected.append(e.Symbol)
                    self.earnings_calendar[e.Symbol] = e.ReportDate
                    self.AddEquity(e.Symbol, Resolution.DAILY)

                    # stop once we have 20
                    if len(selected) >= max_items:
                        break

        total = len(earnings)
        optionable = len(selected)
        # self.Log(f"[{self.Time}] Earnings Announcements: {total}, Optionable: {optionable}")
        return selected

    # @monitor_execution
    def OnData(self, data: Slice):
        if self.IsWarmingUp:  # Ensure Algo has warmed
            return

        for kvp in self.Portfolio:  # Loop through Portfolio
            symbol = kvp.Key
            holding = kvp.Value

            if holding.Invested and symbol.ID.SecurityType == SecurityType.Equity:  # Eliminate Equities from Portfolio
                self.Liquidate(symbol, tag=f"[{self.Time}] OnData flatten equities")

        if self.pending_option_orders:  # drain pending orders that now have prices
            still_pending = []
            for contract, qty, tag in self.pending_option_orders:
                if data.ContainsKey(contract) and self.Securities[contract].HasData and self.Securities[
                    contract].Price > 0:
                    self.MarketOnOpenOrder(contract, qty, tag=f"non-fullfiled {tag}")
                else:
                    still_pending.append((contract, qty, tag))
            self.pending_option_orders = still_pending

        self.purge_old_earnings_data(purge_days=5)  # Purge old passed earnings data

        self.contract_results = {}  # new dictionary to collect results

        # before the symbol loop (once per OnData)
        if not hasattr(self, "contract_results"):
            self.contract_results = {}  # {(front, back): {"slope":..., "volume_ok":..., "ivrv":..., "ts": datetime}}

        for symbol, earnings_date in self.earnings_calendar.items():  # Main Loop
            # self.Debug(f"Looping through {symbol.Value} with earnings {earnings_date}")
            if self.Portfolio[symbol].Invested:
                # self.Debug(f"symbol {symbol} already invested, skipping. Should Monitor Pos")
                ## TODO handle already invested positions
                continue

            # Extra safeguard: skip if any option positions exist for this underlying
            already_invested_options = any(
                sec.Invested and sec.Symbol.HasUnderlying and sec.Symbol.Underlying == symbol
                for sec in self.Portfolio.Values
            )
            if already_invested_options:
                # self.Debug(f"Options on {symbol} already invested, skipping new trade.")
                ## Skip analysis since you already got a trade
                continue

            strike_chains = self.get_calls_up_to_two_strikes(symbol, earnings_date)
            contract_tuples = self.match_option_contracts_by_strike_and_type_2(contracts=strike_chains)

            for front_contract, back_contract in contract_tuples:
                key = (front_contract, back_contract)
                cached = self.contract_results.get(key)
                use_cache = cached and (self.Time - cached["ts"] < timedelta(hours=24))

                if use_cache:
                    results = cached

                else:
                    slopes = self.calculate_iv_slope_pair(front_contract, back_contract, earnings_date, self.Time)
                    vol_ratio = self.filter_pre_earnings_volume(symbol, earnings_date)
                    ivrv_ratio = self.iv_over_rv_ratio(symbol, earnings_date,
                                                       iv_annualized=slopes['near_iv']) if slopes else None

                    self.contract_results[(front_contract, back_contract)] = {
                        "slope": slopes['slope'] if slopes else None,
                        "front_iv": slopes['near_iv'] if slopes else None,
                        "back_iv": slopes['far_iv'] if slopes else None,
                        "vol_ratio": vol_ratio,
                        "strike": slopes['strike'] if slopes else None,
                        "ivrv": ivrv_ratio,
                        "ts": self.Time
                    }

            # ### Debugging results DELETE After dev
            # the_results = self.contract_results
            # if the_results:
            #     for (front, back), metrics in the_results.items():
            #         self.Log(f"{front.Value} | {back.Value} -> slope={metrics['slope']}, "
            #                 f"vol_ratio={metrics['vol_ratio']}, ivrv={metrics['ivrv']}, fiv={metrics['front_iv']}, biv={metrics['back_iv']}")
            #         self.Log('Jump to next OnData')
            # else:
            #     self.Debug("No option pairs stored in results.")
        # --- modify OnData(), inside/near your `if self.trade_all:` branch ---
        if self.trade_all and self.contract_results:
            # self.Debug(f"initial conditions passed: {len(self.contract_results)} pairs")
            if getattr(self, "_candidates_built_at", None) != self.Time:
                self._candidates_built_at = self.Time

            # 1) reset same-bar seen set
            if getattr(self, "_last_bar_time", None) != self.Time:
                self._calendars_seen_this_bar = set()
                self._last_bar_time = self.Time

            from collections import defaultdict
            candidates_by_underlying = defaultdict(list)

            # 2) iterate over your universe / chains as you already do
            for (front_contract, back_contract), metrics in self.contract_results.items():
                symbol = front_contract.Underlying

                # (A) obtain your precomputed analytics for this underlying
                slope = metrics['slope']
                ivrv_ratio = metrics['ivrv']
                vol_ratio = metrics['vol_ratio']

                if slope is None or ivrv_ratio is None or vol_ratio is None:
                    continue

                # (B) Construct candidate rows (NO orders here)
                # We already have the matched pair (front_contract, back_contract) from the loop key
                
                calendar_id, row = self._row_from_pair(symbol, front_contract, back_contract, slope, ivrv_ratio, vol_ratio)

                # de-dup within this bar
                if calendar_id in self._calendars_seen_this_bar:
                    continue

                self._calendars_seen_this_bar.add(calendar_id)
                candidates_by_underlying[str(symbol)].append(row)

            # 3) publish snapshot for later ranking/placement stage
            self.calendar_candidates = dict(candidates_by_underlying)
            # Optional tiny debug:
            self.Debug(f"[{self.Time}] candidates: {sum(len(v) for v in self.calendar_candidates.values())}")
            pass
        if self.trade_all:
            for (front_contract, back_contract), m in self.contract_results.items():
                slope_ok = m["slope"]
                volume_ok = m["vol_ratio"]
                ivrv_ok = m["ivrv"]
                if slope_ok and volume_ok and ivrv_ok:
                    # ensure strike in metrics for tagging
                    m["strike"] = float(front_contract.ID.StrikePrice)
                    self.place_tagged_calendar(symbol=front_contract.Underlying,
                                               front_contract=front_contract,
                                               back_contract=back_contract,
                                               qty=1,
                                               metrics=m,
                                               long_calendar=True)

        #     ### TO IMPLEMENT LATER ###
        #     option_symbol = self.AddOption(symbol, Resolution.HOUR)
        #     strat = OptionStrategies.call_calendar_spread(option_symbol,
        #                                                     symbol_slopes['strike'],
        #                                                     symbol_slopes['near_contract_expiry'],
        #                                                     symbol_slopes['far_contract_expiry'])
        #     self.buy(strat, 1)  # self.sell(...) for short calendar

    def OnEndOfAlgorithm(self):
        # Safety log so you can spot anything that failed to close
        still = [p.Symbol.Value for p in self.Portfolio.Values if p.Invested]
        if still:
            self.Debug(f"[FINAL][WARN] Still invested in: {still}")
        else:
            self.Debug("[FINAL] All positions closed before backtest end.")

    ### Functions Start ###
    def _ensure_option_tradable(self, contract: Symbol, res=Resolution.Hour):
        if not self.Securities.ContainsKey(contract):
            self.AddOptionContract(contract, res)  # adds underlying too
        u = contract.Underlying
        if self.Securities.ContainsKey(u):
            self.Securities[u].SetDataNormalizationMode(DataNormalizationMode.Raw)

    def build_order_tag(self, symbol, front_contract, back_contract, metrics, side):
        """Return a compact, JSON-safe tag string."""

        def sym_str(x):
            # QuantConnect Symbol → value; everything else → str
            return getattr(x, "Value", str(x))

        def to_float(x):
            # Accept None, int/float, numpy numbers, and strings with comma decimals
            if x is None:
                return None
            if isinstance(x, (int, float)):
                return float(x)
            try:
                s = str(x).strip().replace(",", ".")
                return float(s)
            except Exception:
                return None

        # Strike: prefer metrics['strike'] if numeric; else fall back to contract
        k = to_float(metrics.get("strike"))
        if k is None:
            k = to_float(getattr(getattr(front_contract, "ID", None), "StrikePrice", None))

        payload = {
            "u": sym_str(symbol),
            "leg": str(side),  # e.g., "LONG" / "SHORT"
            "k": k,
            "near": str(getattr(getattr(front_contract, "ID", None), "Date").date()),
            "far": str(getattr(getattr(back_contract, "ID", None), "Date").date()),
            "slope": round(to_float(metrics.get("slope")), 5),
            "ivrv": round(to_float(metrics.get("ivrv")), 5),
            "vol_ratio": round(to_float(metrics.get("vol_ratio")), 5),  # handles 1,86 → 1.86, dicts → None
            "ts": (metrics.get("ts") or datetime.utcnow()).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

        # Drop Nones to keep the tag short and avoid junk
        payload = {k: v for k, v in payload.items() if v is not None}

        s = json.dumps(payload, separators=(",", ":"))  # compact

        # Optional: enforce ~1KB tag guard (QC tags are small)
        if len(s) > 1024:
            for key in ("vol_ratio", "ivrv", "slope"):
                if key in payload:
                    payload.pop(key)
                    s = json.dumps(payload, separators=(",", ":"))
                    if len(s) <= 1024:
                        break
            if len(s) > 1024:
                s = s[:1024]

        return s

    def place_tagged_calendar(self, symbol, front_contract, back_contract, qty, metrics, long_calendar=True):
        """
        Submits a calendar spread and tags each leg with JSON including slope/ivrv/vol flags.
        long_calendar=True -> SHORT near, LONG far
        """
        # Ensure contracts tradable
        self._ensure_option_tradable(front_contract)
        self._ensure_option_tradable(back_contract)

        # Legs: calendar is same strike/right; typical long calendar: short near, long far
        sign_near = -1 if long_calendar else +1
        sign_far = +1 if long_calendar else -1

        legs = [
            Leg.Create(front_contract, sign_near),
            Leg.Create(back_contract, sign_far),
        ]

        base_tag = f"calendar:{symbol.Value}:{front_contract.ID.StrikePrice}@{front_contract.ID.OptionRight}"
        tickets = self.ComboMarketOrder(legs, 1 if qty is None else int(qty), tag=base_tag)

        # Tag each leg with detailed JSON
        near_tag = self.build_order_tag(symbol, front_contract, back_contract, metrics,
                                        side=("SHORT" if long_calendar else "LONG"))
        far_tag = self.build_order_tag(symbol, front_contract, back_contract, metrics,
                                       side=("LONG" if long_calendar else "SHORT"))

        if self.IsWarmingUp:
            return  # or queue tags to apply later

        # tickets come back in the same order as legs; map them directly
        for ticket, leg in zip(tickets, legs):
            try:
                uf = UpdateOrderFields()
                # if this leg corresponds to the front_contract (near), use near_tag; otherwise far_tag
                uf.Tag = near_tag if leg.Symbol == front_contract else far_tag
                ticket.Update(uf)
            except Exception as e:
                # small defensive log so we don't silently lose tag updates in live/backtest
                self.Debug(f"[TagUpdate] Failed to update tag for {getattr(leg, 'Symbol', leg)}: {e}")

    # @monitor_execution
    def calculate_iv_slope_pair(self,
                                front_contract: Symbol,
                                back_contract: Symbol,
                                earnings_time: datetime,
                                now: datetime) -> Optional[dict]:
        """
        Compute the IV slope between two *specific* option contracts.

        Args:
            front_contract: earlier-expiring option Symbol
            back_contract: later-expiring option Symbol
            earnings_time: earnings datetime to validate against
            now: current algorithm time (self.Time)

        Returns:
            dict with keys {"strike", "near_contract", "far_contract", "slope", "diff_days", "near_iv", "far_iv"}
            or None if invalid / cannot compute.
        """
        front_exp = front_contract.ID.Date
        back_exp = back_contract.ID.Date

        # Must be ordered and both after earnings & now
        if not (front_exp < back_exp):
            return None
        if not (front_exp.date() > max(earnings_time.date(), now.date())):
            return None
        if back_exp.date() <= now.date():
            return None

        diff_days = (back_exp.date() - front_exp.date()).days
        if diff_days <= 0:
            return None

        # Compute IVs (uses your existing get_implied_volatilities)
        near_iv, far_iv = self.get_implied_volatilities(front_contract, back_contract, now=self.Time,
                                                        earnings_time=earnings_time)
        if near_iv is None or far_iv is None:
            return None

        slope = (near_iv - far_iv) / diff_days
        return {
            "strike": front_contract.ID.StrikePrice,
            "near_contract": front_contract,
            "near_contract_expiry": front_contract.ID.Date,
            "far_contract_expiry": back_contract.ID.Date,
            "far_contract": back_contract,
            "near_iv": round(near_iv, 4),
            "far_iv": round(far_iv, 4),
            "slope": round(slope, 4),
            "diff_days": diff_days
        }

    # Optional convenience wrapper if you still want to process all pairs for a symbol
    def calculate_iv_slopes_for_symbol(self, symbol: Symbol, earnings_time: datetime) -> list:
        front_chain, back_chain = self.get_two_closest_option_chains(symbol, earnings_time)
        if not front_chain or not back_chain:
            return []
        results = []
        for front, back in self.match_option_contracts_by_strike_and_type(front_chain, back_chain):
            item = self.calculate_iv_slope_pair(front, back, earnings_time, self.Time)
            if item is not None:
                results.append(item)
        return results

    #
    # # @monitor_execution
    def filter_pre_earnings_volume(self, symbol, earnings_date: datetime, threshold: float = 1.20) -> Optional[float]:
        """
        Returns the ratio (recent_volume / avg_prev_30) if >= threshold, else None.
        """
        history = self.History(symbol, 35, Resolution.Daily)
        if history is None or getattr(history, "empty", False):
            return None

        grouped = history.loc[symbol] if isinstance(history.index, pd.MultiIndex) else history
        grouped = grouped[grouped.index < earnings_date]
        if grouped is None or len(grouped) < 31:
            return None

        recent_volume = grouped.iloc[-1].volume
        avg_volume = grouped.iloc[-31:-1].volume.mean()
        if not avg_volume:
            return None

        ratio = float(recent_volume) / float(avg_volume)
        return ratio

    def iv_over_rv_ratio(self, symbol: Symbol, earnings_date, iv_annualized: float, window: int = 30) -> float:
        # Get enough daily history, then trim to strictly pre-earnings
        hist = self.History(symbol, window + 1 + 10, Resolution.Daily)
        if hist is None or hist.empty:
            return float('nan')
        df = hist.loc[symbol] if isinstance(hist.index, pd.MultiIndex) else hist
        df = df[df.index < earnings_date]
        if len(df) < window + 1:
            return float('nan')

        closes = df['close'].iloc[-(window + 1):].astype(float).values
        logrets = np.log(closes[1:] / closes[:-1])
        rv = float(logrets.std(ddof=1)) * math.sqrt(252.0)  # annualized

        return float('nan') if rv <= 0 else float(iv_annualized / rv)

    def purge_old_earnings_data(self, purge_days: int = 15) -> None:
        cutoff = self.Time - timedelta(days=purge_days)
        before_count = len(self.earnings_calendar)

        # Filter earnings_calendar and log dropped keys
        new_calendar = {}
        for symbol, date in self.earnings_calendar.items():
            if date >= cutoff:
                new_calendar[symbol] = date
            else:
                # self.Debug(f"[Purge] Dropping {symbol} with earnings date {date} older than cutoff {cutoff}")
                pass
        self.earnings_calendar = new_calendar

        after_count = len(self.earnings_calendar)
        if before_count != after_count:
            pass
            # self.Debug(f"[Purge] Earnings calendar reduced from {before_count} to {after_count}")

        # Clean slopes dictionary
        cleaned_slopes = {}
        if self.slope_results:
            for symbol, slopes in self.slope_results.items():
                if symbol not in self.earnings_calendar:
                    # self.Debug(f"[Purge] Removing slopes for {symbol} as it is no longer in earnings_calendar")
                    continue
                valid = [s for s in slopes if s['near_contract'].ID.Date > self.Time]
                if len(valid) != len(slopes):
                    pass
                    # self.Debug(f"[Purge] {symbol}: removed {len(slopes) - len(valid)} expired slope entries")
                if valid:
                    cleaned_slopes[symbol] = valid
            self.slope_results = cleaned_slopes

    def _make_calendar_id(self, underlying: str, right: str, strike: float, near_expiry, far_expiry) -> str:
        """Deterministic ID for de-dup/risk controls."""
        ne = str(getattr(near_expiry, "date", lambda: near_expiry)())
        fe = str(getattr(far_expiry, "date", lambda: far_expiry)())
        return f"{underlying}|{right}|{int(round(strike))}|{ne}→{fe}"

    def _row_from_pair(self, underlying, near_contract, far_contract, slope: float, ivrv_ratio: float,
                       vol_ratio: float):
        """Shape a single candidate row (no orders here)."""
        right = str(near_contract.ID.OptionRight)[0]  # 'C' or 'P'
        strike = float(near_contract.ID.StrikePrice)
        near_exp = near_contract.ID.Date
        far_exp = far_contract.ID.Date

        calendar_id = self._make_calendar_id(underlying, right, strike, near_exp, far_exp)

        return calendar_id, {
            "calendar_id": calendar_id,
            "underlying": str(underlying),
            "calendar_pair": {
                "near": {
                    "expiry": str(near_exp.date()),
                    "right": right,
                    "strike": strike,
                    "symbol_str": str(near_contract)
                },
                "far": {
                    "expiry": str(far_exp.date()),
                    "right": right,
                    "strike": strike,
                    "symbol_str": str(far_contract)
                }
            },
            "metrics": {
                "slope": float(slope),
                "ivrv_ratio": float(ivrv_ratio),
                "vol_ratio": float(vol_ratio)
            },
            "ranking": {
                "liquidity_score": None,
                "edge_score": None,
                "composite": None
            },
            "ts": self.Time.isoformat()
        }

    def _should_final_liquidate(self, today: date, end_date: date) -> bool:
        # Trigger on the last trading day whose "tomorrow" is >= algorithm EndDate.
        return (today + timedelta(days=1)) >= end_date

    def register_final_liquidation(self, anchor_ticker: str = "SPY", minutes_before_close: int = 10):
        """
        Schedules a one-time 'final liquidation' near the last close.
        - anchor_ticker is only used to anchor the market calendar (no impact on holdings).
        - Works across weekends/holidays by firing on the last trading day before EndDate.
        """
        # Ensure we have an anchor security for exchange hours
        anchor = self.Securities[anchor_ticker].Symbol if anchor_ticker in self.Securities \
            else self.AddEquity(anchor_ticker, Resolution.Minute).Symbol
        self._final_liquidated = False
        self._algo_end_date = self.EndDate.date()

        def _maybe_final_liquidation():
            if self._final_liquidated:
                return
            if self._should_final_liquidate(self.Time.date(), self._algo_end_date):
                self.Debug(f"[FINAL] Cancelling open orders + liquidating at {self.Time}")
                # 1) cancel ALL open orders first (stops/limits/GTCs)
                self.Transactions.CancelOpenOrders()
                # 2) liquidate every invested security (equities, options, etc.)
                for sec in self.Portfolio.Values:
                    if sec.Invested:
                        # For options/futures, Liquidate(symbol) sends the correct offsetting order
                        self.Liquidate(sec.Symbol)
                self._final_liquidated = True

        # Run daily near close; the predicate limits execution to the last trading day.
        self.Schedule.On(
            self.DateRules.EveryDay(anchor),
            self.TimeRules.BeforeMarketClose(anchor, minutes_before_close),
            _maybe_final_liquidation
        )

    def _queue_or_trade_now(self, contract: Symbol, quantity: int, tag: str, data: Slice | None):
        # must be subscribed
        self._ensure_option_tradable(contract)

        # if we have a Slice (OnData path), only trade when the bar is present
        if data is not None:
            if data.ContainsKey(contract) and self.Securities[contract].HasData and self.Securities[contract].Price > 0:
                self.MarketOrder(contract, quantity, tag=tag)
                return True
            return False

        # scheduled path (no Slice): try a 1-bar history probe; if not available, queue for next OnData
        hist = self.History(contract, 1, Resolution.Hour)
        if hasattr(hist, "empty") and not hist.empty:
            self.MarketOrder(contract, quantity, tag=tag)
            return True

        # queue and let OnData place it once we get a bar
        self.pending_option_orders.append((contract, quantity, tag))
        self.Debug(f"[Queue] Waiting for first bar: {contract}")
        return False

    def get_two_closest_option_chains(self, symbol: Symbol, earnings_time: datetime) -> Tuple[
        List[Symbol], List[Symbol]]:
        """
        Two earliest expiries strictly after earnings and now, with 25 <= DTE <= 60.
        For each expiry, keep ONLY the 2 ATM contracts (CALL + PUT at the ATM strike).
        """
        contracts = self.OptionChainProvider.GetOptionContractList(symbol, self.Time)
        if not contracts:
            return [], []

        # Group by expiry
        contracts_by_exp: Dict[datetime, List[Symbol]] = {}
        for c in contracts:
            contracts_by_exp.setdefault(c.ID.Date, []).append(c)

        # Underlying price (once)
        price = None
        if symbol in self.Securities and self.Securities[symbol].Price > 0:
            price = float(self.Securities[symbol].Price)
        if not price or price <= 0:
            hist = self.History(symbol, 1, Resolution.Minute)
            if not hist.empty:
                try:
                    price = float(hist["close"].iloc[-1])
                except Exception:
                    price = None
        if not price or price <= 0:
            return [], []  # can’t find ATM without a price

        min_after = max(earnings_time.date(), self.Time.date())

        # DTE window: 25–60 inclusive, strictly after min_after
        def dte(exp: datetime) -> int:
            return (exp.date() - self.Time.date()).days

        valid_expiries = sorted(
            exp for exp in contracts_by_exp
            if exp.date() > min_after and 25 <= dte(exp) <= 60
        )
        if not valid_expiries:
            return [], []

        front_exp = valid_expiries[0]
        back_exp = valid_expiries[1] if len(valid_expiries) > 1 else None

        def _atm_pair(chain_contracts: List[Symbol]) -> List[Symbol]:
            if not chain_contracts:
                return []
            # find ATM strike
            strikes = sorted({float(c.ID.StrikePrice) for c in chain_contracts})
            if not strikes:
                return []
            atm_strike = min(strikes, key=lambda s: abs(s - price))
            # keep only CALL + PUT at ATM strike (2 contracts max)
            out = [c for c in chain_contracts if float(c.ID.StrikePrice) == atm_strike]
            # Prefer returning at most one CALL and one PUT
            call = next((c for c in out if getattr(c.ID, "Right", None) == OptionRight.Call), None)
            put = next((c for c in out if getattr(c.ID, "Right", None) == OptionRight.Put), None)
            return [x for x in (call, put) if x is not None]

        front_list = _atm_pair(contracts_by_exp.get(front_exp, []))
        if back_exp is None:
            return front_list, []
        back_list = _atm_pair(contracts_by_exp.get(back_exp, []))
        return front_list, back_list

    def get_calls_up_to_two_strikes(self, symbol: Symbol, earnings_time: datetime) -> List[Symbol]:
        """
        Return all CALL option contracts for `symbol` that:
        - Expire strictly after earnings_time,
        - Expire no more than 45 days afterward,
        - Are at-the-money (ATM) or up to 2 strikes above ATM.
        """
        contracts = self.OptionChainProvider.GetOptionContractList(symbol, self.Time)
        if not contracts:
            return []

        # Get current underlying price
        price = None
        if symbol in self.Securities and self.Securities[symbol].Price > 0:
            price = float(self.Securities[symbol].Price)
        if not price or price <= 0:
            hist = self.History(symbol, 1, Resolution.Minute)
            if not hist.empty:
                price = float(hist["close"].iloc[-1])

        if not price or price <= 0:
            return []

        # Expiry window: > earnings_time and within 45 days
        min_date = earnings_time.date()
        max_date = (earnings_time + timedelta(days=45)).date()

        valid = [c for c in contracts
                 if c.ID.OptionRight == OptionRight.Call
                 and min_date < c.ID.Date.date() <= max_date]

        if not valid:
            return []

        # Determine ATM strike
        strikes = sorted({float(c.ID.StrikePrice) for c in valid})
        if not strikes:
            return []

        atm = min(strikes, key=lambda s: abs(s - price))
        strikes_keep = {s for s in strikes if s >= atm and s <= atm + 2 * (strikes[1] - strikes[0])}

        return [c for c in valid if float(c.ID.StrikePrice) in strikes_keep]

    def match_option_contracts_by_strike_and_type_2(self, contracts: List[Symbol]) -> List[Tuple[Symbol, Symbol]]:
        """
        From a list of option Symbols, return all pairs (near, next) such that:
        - Same strike and option right (call/put).
        - Different expiration dates.
        Produces all expiry combinations (E1,E2), (E1,E3), … not just consecutive.
        """
        from collections import defaultdict
        from typing import List, Tuple
        import itertools
        if not contracts:
            return []

        # Bucket by (Right, Strike)
        buckets = defaultdict(list)
        for c in contracts:
            key = (c.ID.OptionRight, float(c.ID.StrikePrice))
            buckets[key].append(c)

        matches: List[Tuple[Symbol, Symbol]] = []
        for key, lst in buckets.items():
            # Sort contracts by expiry
            lst.sort(key=lambda x: x.ID.Date)
            # All combinations of 2 different expiries
            for near, far in itertools.combinations(lst, 2):
                matches.append((near, far))

        return matches[:20]  # keep top 20 if needed

    def match_option_contracts_by_strike_and_type(self, near_chain: List[Symbol], next_chain: List[Symbol]) -> List[
        Tuple[Symbol, Symbol]]:
        """
        Match option contracts from two expiration chains by strike and option type (call/put).

        Parameters:
            near_chain (List[Symbol]): List of option Symbols with earlier expiration
            next_chain (List[Symbol]): List of option Symbols with later expiration

        Returns:
            List[Tuple[Symbol, Symbol]]: List of matched option contracts as (near, next)
        """
        matches = []
        next_lookup = {(c.ID.OptionRight, c.ID.StrikePrice): c for c in next_chain}

        for near_contract in near_chain:
            key = (near_contract.ID.OptionRight, near_contract.ID.StrikePrice)
            if key in next_lookup:
                matches.append((near_contract, next_lookup[key]))
        return matches[:20]

    def get_implied_volatilities(self,
                                 near_symbol: Symbol,
                                 far_symbol: Symbol,
                                 now: datetime = None,
                                 earnings_time: datetime = None) -> Tuple[Optional[float], Optional[float]]:
        """
        Robust & efficient IV fetch for a near/far option pair.
        - Mirrors the validations used in calculate_iv_slope_pair (legs must be after max(earnings_time, now)).
        - Avoids brittle MultiIndex key lookup (no hist.loc[sym]); always grabs the last row safely.
        - Uses bid/ask mid if present, else trade close.
        - Gets 1 bar of underlying history (fallback to Security.Price).
        """
        import math
        now = now or self.Time
        earnings_time = earnings_time or datetime(1970, 1, 1)

        def _last_row_safely(hist_df: pd.DataFrame) -> Optional[pd.Series]:
            if not hasattr(hist_df, 'empty') or hist_df.empty:
                return None
            # Whether flat index or MultiIndex, the last row corresponds to the (only) symbol we requested
            try:
                return hist_df.iloc[-1]
            except Exception:
                return None

        def _latest_underlying_close(under_sym: Symbol) -> Optional[float]:
            # Prefer 1 daily bar; fallback to Security.Price
            try:
                hist = self.History(under_sym, 1, Resolution.Daily)
            except Exception:
                hist = None
            if hist is not None and hasattr(hist, 'empty') and not hist.empty:
                row = _last_row_safely(hist)
                if row is not None and 'close' in row:
                    try:
                        c = float(row['close'])
                        if c > 0:
                            return c
                    except Exception:
                        pass
            # Fallback
            sec = self.Securities.get(under_sym, None)
            if sec is not None and sec.HasData and sec.Price > 0:
                return float(sec.Price)
            return None

        def _option_mid_close(sym: Symbol) -> Optional[float]:
            # Count-based history is faster and avoids tz windows
            try:
                hist = self.History(sym, 15, Resolution.Daily)
            except Exception:
                return None
            row = _last_row_safely(hist)
            if row is None:
                return None
            # Try bid/ask mid first
            bid = row['bidclose'] if 'bidclose' in row else None
            ask = row['askclose'] if 'askclose' in row else None
            if bid is not None and ask is not None:
                try:
                    mid = (float(ask) + float(bid)) / 2.0
                    if mid > 0:
                        return mid
                except Exception:
                    pass
            # Fallback to trade close
            if 'close' in row:
                try:
                    c = float(row['close'])
                    if c > 0:
                        return c
                except Exception:
                    pass
            return None

        def _compute_iv(sym: Symbol) -> Optional[float]:
            exp = sym.ID.Date
            # Validate vs earnings and now, must be strictly in the future
            min_cut = max(earnings_time.date(), now.date())
            if exp.date() <= min_cut:
                return None

            opt_px = _option_mid_close(sym)
            if opt_px is None or opt_px <= 0:
                return None

            under_sym = sym.Underlying
            S = _latest_underlying_close(under_sym)
            if S is None or S <= 0:
                return None

            T = max((exp - now).total_seconds(), 0.0) / (365.0 * 24 * 3600)
            if T <= 0:
                return None

            K = float(sym.ID.StrikePrice)
            r = 0.0

            # Use option-right aware pricer/vega
            return self._implied_volatility_newton(sym.ID.OptionRight, S, K, T, r, opt_px)

        near_iv = _compute_iv(near_symbol)
        far_iv = _compute_iv(far_symbol)
        return near_iv, far_iv

    # --- Helpers for IV -----------------------------------------------------------
    def _bs_price(self, right: OptionRight, S: float, K: float, T: float, r: float, sigma: float) -> float:
        if sigma <= 0 or T <= 0 or S <= 0 or K <= 0:
            return 0.0
        d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)
        if right == OptionRight.Call:
            return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
        else:
            # Put
            return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    def _vega(self, S: float, K: float, T: float, r: float, sigma: float) -> float:
        if sigma <= 0 or T <= 0 or S <= 0 or K <= 0:
            return 0.0
        d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
        return S * norm.pdf(d1) * math.sqrt(T)

    def _implied_volatility_newton(self, right: OptionRight, S: float, K: float, T: float, r: float,
                                   market_price: float) -> Optional[float]:
        # Guard: intrinsic bound
        if right == OptionRight.Call:
            intrinsic = max(S - K * math.exp(-r * T), 0.0)
        else:
            intrinsic = max(K * math.exp(-r * T) - S, 0.0)
        if market_price <= intrinsic:
            return None

        sigma = 0.25
        for _ in range(100):
            price = self._bs_price(right, S, K, T, r, sigma)
            v = self._vega(S, K, T, r, sigma)
            if v < 1e-8:
                return None
            diff = price - market_price
            if abs(diff) < 1e-5:
                return sigma
            sigma -= diff / v
            if sigma <= 0 or sigma > 6:  # basic clamps
                return None
        return None
