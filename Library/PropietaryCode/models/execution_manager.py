from __future__ import annotations

import json
from datetime import datetime, time, timedelta
from typing import Any, Dict, List, Optional, Set
from AlgorithmImports import *

from .alpha_model import CalendarSpreadOpportunity


class CalendarSpreadExecutionManager(ExecutionModel):
    """Execution Manager for spread gating, multi-fill methods, and atomic liquidation."""

    def __init__(self, algorithm: Any) -> None:
        super().__init__()
        self.algo = algorithm

    def ExecuteOpportunity(self, opp: CalendarSpreadOpportunity) -> bool:
        underlying = opp.underlying
        front = opp.front
        back = opp.back
        metrics = opp.metrics
        report_date = opp.report_date
        report_time = opp.report_time

        if not self.algo._ensure_option_tradable(front) or not self.algo._ensure_option_tradable(back):
            self.algo.UnsubscribeOption(front)
            self.algo.UnsubscribeOption(back)
            return False

        front_sec = self.algo.Securities[front] if front in self.algo.Securities else None
        back_sec = self.algo.Securities[back] if back in self.algo.Securities else None

        front_bid = float(front_sec.BidPrice) if front_sec and hasattr(front_sec, "BidPrice") else 0.0
        front_ask = float(front_sec.AskPrice) if front_sec and hasattr(front_sec, "AskPrice") else 0.0
        back_bid = float(back_sec.BidPrice) if back_sec and hasattr(back_sec, "BidPrice") else 0.0
        back_ask = float(back_sec.AskPrice) if back_sec and hasattr(back_sec, "AskPrice") else 0.0

        if front_ask <= 0 or back_ask <= 0:
            front_price = self.algo.GetOptionMidPrice(front)
            back_price = self.algo.GetOptionMidPrice(back)
            if front_price <= 0 or back_price <= 0:
                self.algo.UnsubscribeOption(front)
                self.algo.UnsubscribeOption(back)
                return False
            front_ask = front_price
            back_ask = back_price
            front_bid = front_price * 0.95
            back_bid = back_price * 0.95

        natural_ask = max(0.01, round(back_ask - front_bid, 2)) if front_bid > 0 else round(back_ask, 2)
        comb_spread = (front_ask - front_bid) + (back_ask - back_bid)
        max_spread = getattr(self.algo, "max_spread_threshold", 0.35)
        spread_ratio = (comb_spread / natural_ask) if natural_ask > 0 else 1.0

        # Physical liquidity boundary: enforce reasonable sanity limit even in pass_all (SP-02)
        max_allowed_spread = max_spread * 1.6 if self.algo.pass_all else max_spread
        max_allowed_ratio = 0.40 if self.algo.pass_all else 0.25

        if comb_spread > max_allowed_spread or spread_ratio > max_allowed_ratio:
            self.algo.UnsubscribeOption(front)
            self.algo.UnsubscribeOption(back)
            return False

        qty = self.algo.DeterminePositionSize(underlying, metrics, natural_ask)
        if qty <= 0:
            self.algo.UnsubscribeOption(front)
            self.algo.UnsubscribeOption(back)
            return False

        legs = [Leg.Create(front, -1), Leg.Create(back, 1)]

        front_mid = (front_bid + front_ask) / 2.0 if (front_bid > 0 and front_ask > 0) else front_ask
        back_mid = (back_bid + back_ask) / 2.0 if (back_bid > 0 and back_ask > 0) else back_bid
        mid_debit = max(0.01, round(back_mid - front_mid, 2))

        method = getattr(self.algo, "fill_method", "combo_limit_natural")
        near_tag = self.algo.BuildOrderTag(underlying, front, back, metrics, "SHORT")
        far_tag = self.algo.BuildOrderTag(underlying, front, back, metrics, "LONG")

        tickets = []
        is_adaptive = False
        if method == "combo_limit_mid":
            limit_price = mid_debit
            tickets = self.algo.ComboLimitOrder(legs, qty, limit_price)
        elif method == "combo_market":
            limit_price = natural_ask
            tickets = self.algo.ComboMarketOrder(legs, qty)
        elif method == "individual_market":
            limit_price = natural_ask
            t_front = self.algo.MarketOrder(front, -qty, tag=near_tag)
            t_back = self.algo.MarketOrder(back, qty, tag=far_tag)
            tickets = [t for t in [t_front, t_back] if t is not None]
        elif method == "adaptive_pegged":
            limit_price = mid_debit
            tickets = self.algo.ComboLimitOrder(legs, qty, limit_price)
            is_adaptive = True
        else:  # combo_limit_natural (baseline)
            limit_price = round(natural_ask * (1.0 + self.algo.alpha_spread), 2) if self.algo.pass_all else natural_ask
            limit_price = max(0.01, limit_price)
            tickets = self.algo.ComboLimitOrder(legs, qty, limit_price)

        self.algo.trade_id_counter += 1
        right_str = "C" if front.ID.OptionRight == OptionRight.Call else "P"
        pk = f"{self.algo.backtest_run_id}_{underlying.Value}_{right_str}_{self.algo.trade_id_counter}"

        front_iv = float(metrics.get("front_iv", 0.0))
        back_iv = float(metrics.get("back_iv", 0.0))

        position_info = {
            "pk": pk,
            "underlying": underlying,
            "front": front,
            "back": back,
            "qty": qty,
            "entry_price": limit_price,
            "entry_time": self.algo.Time,
            "report_date": report_date,
            "report_time": report_time,
            "tickets": tickets,
            "slope": metrics["slope"],
            "vol_ratio": metrics["vol_ratio"],
            "ivrv_ratio": metrics["ivrv_ratio"],
            "mae_pct": 0.0,
            "mfe_pct": 0.0,
            "front_iv_open": front_iv,
            "front_iv_max": front_iv,
            "front_iv_min": front_iv,
            "last_front_iv": front_iv,
            "back_iv_open": back_iv,
            "back_iv_max": back_iv,
            "back_iv_min": back_iv,
            "last_back_iv": back_iv,
            "metrics": metrics,
            "entry_fills": {},
            "exit_fills": {},
            "initial_limit": limit_price,
            "natural_ask": natural_ask,
            "mid_debit": mid_debit,
            "comb_spread": comb_spread,
            "fill_method": method,
            "entry_is_adaptive": is_adaptive
        }

        self.algo.active_spreads[pk] = position_info
        if not hasattr(self.algo, "_traded_today"):
            self.algo._traded_today = set()
        self.algo._traded_today.add((underlying, front.ID.OptionRight, self.algo.Time.date()))
        self.algo._traded_today.add((underlying, self.algo.Time.date()))

        if tickets:
            for ticket in tickets:
                self.algo._pending_entry_tickets[ticket.OrderId] = position_info
                try:
                    uf = UpdateOrderFields()
                    uf.Tag = near_tag if ticket.Symbol == front else far_tag
                    ticket.Update(uf)
                except Exception as e:
                    self.algo.Debug(f"[TagUpdate] Failed for {ticket.Symbol.Value}: {e}")

        self.algo.Log(f"[TRADE SIGNAL ENTRY] Time: {self.algo.Time} | Ticker: {underlying.Value} ({right_str}) | Method: {method} | Qty: {qty} | Front: {front.Value} | Back: {back.Value} | NatAsk: {natural_ask} | Mid: {mid_debit} | Spread: {comb_spread} | Slope: {metrics['slope']:.5f} | VolRatio: {metrics['vol_ratio']:.2f}")
        return True

    def LiquidateSpread(self, spread_key: Any, tag: str) -> bool:
        if spread_key not in self.algo.active_spreads:
            return False

        position = self.algo.active_spreads[spread_key]
        if position.get("is_liquidating", False):
            return False

        front = position["front"]
        back = position["back"]
        qty = position["qty"]

        front_qty = abs(self.algo.Portfolio[front].Quantity) if self.algo.Portfolio.ContainsKey(front) else 0
        back_qty = abs(self.algo.Portfolio[back].Quantity) if self.algo.Portfolio.ContainsKey(back) else 0

        for t in position.get("tickets", []):
            if t.Status in [OrderStatus.Submitted, OrderStatus.New]:
                try:
                    t.Cancel("Canceling pending entry ticket prior to liquidation")
                except Exception:
                    pass

        if front_qty == 0 and back_qty == 0:
            self.algo.UnsubscribeOption(front)
            self.algo.UnsubscribeOption(back)
            self.algo.active_spreads.pop(spread_key, None)
            return True

        exit_tickets = []

        if front_qty > 0 and back_qty > 0:
            combo_qty = min(front_qty, back_qty)
            exit_legs = [Leg.Create(front, 1), Leg.Create(back, -1)]
            front_sec, back_sec = self.algo.Securities.get(front), self.algo.Securities.get(back)

            def _safe_float(sec, attr, default=0.0):
                if sec is not None and hasattr(sec, attr):
                    val = getattr(sec, attr)
                    try:
                        f = float(val)
                        return f if f > 0 else default
                    except (ValueError, TypeError):
                        return default
                return default

            front_bid = _safe_float(front_sec, "BidPrice", 0.0)
            front_ask = _safe_float(front_sec, "AskPrice", 0.0)
            back_bid = _safe_float(back_sec, "BidPrice", 0.0)
            back_ask = _safe_float(back_sec, "AskPrice", 0.0)

            if front_bid <= 0 or front_ask <= 0:
                f_p = _safe_float(front_sec, "Price", 0.0)
                if f_p > 0:
                    front_bid = f_p * 0.95
                    front_ask = f_p * 1.05
            if back_bid <= 0 or back_ask <= 0:
                b_p = _safe_float(back_sec, "Price", 0.0)
                if b_p > 0:
                    back_bid = b_p * 0.95
                    back_ask = b_p * 1.05

            natural_credit = back_bid - front_ask
            front_mid = (front_bid + front_ask) / 2.0 if (front_bid > 0 and front_ask > 0) else front_ask
            back_mid = (back_bid + back_ask) / 2.0 if (back_bid > 0 and back_ask > 0) else back_bid
            mid_credit = back_mid - front_mid

            method = getattr(self.algo, "fill_method", "combo_limit_natural")
            is_emergency = any(kw in str(tag).lower() for kw in ("emergency", "expiry", "force", "close:", "stop"))

            # L-03: Inverted exit credit liquidation or emergency close -> ATOMIC MARKET ORDER PAIR
            # Guarantees liquidation even when natural credit < 0, completely resolving the ZERO DEBIT FLOOR deadlock
            if is_emergency or natural_credit < 0.0:
                t_front = self.algo.MarketOrder(front, combo_qty, tag=f"{tag} ATOMIC PAIR CLOSE SHORT")
                t_back = self.algo.MarketOrder(back, -combo_qty, tag=f"{tag} ATOMIC PAIR CLOSE LONG")
                exit_tickets = [t for t in [t_front, t_back] if t is not None]
            elif method == "combo_limit_mid":
                exit_tickets = self.algo.ComboLimitOrder(exit_legs, combo_qty, -round(mid_credit, 2), tag=tag)
            elif method == "combo_market":
                exit_tickets = self.algo.ComboMarketOrder(exit_legs, combo_qty, tag=tag)
            elif method == "individual_market":
                t_front = self.algo.MarketOrder(front, combo_qty, tag=f"{tag} ATOMIC PAIR CLOSE SHORT")
                t_back = self.algo.MarketOrder(back, -combo_qty, tag=f"{tag} ATOMIC PAIR CLOSE LONG")
                exit_tickets = [t for t in [t_front, t_back] if t is not None]
            elif method == "adaptive_pegged":
                exit_tickets = self.algo.ComboLimitOrder(exit_legs, combo_qty, -round(mid_credit, 2), tag=tag)
                position["exit_is_adaptive"] = True
                position["mid_credit"] = mid_credit
                position["natural_credit"] = natural_credit
            else:  # combo_limit_natural baseline
                exit_tickets = self.algo.ComboLimitOrder(exit_legs, combo_qty, -round(natural_credit, 2), tag=tag)

        elif front_qty == 0 and back_qty > 0:
            position["front_expired"] = True
            ticket = self.algo.MarketOrder(back, -back_qty, tag=f"CLOSE: {tag}")
            if ticket:
                exit_tickets = [ticket]

        elif front_qty > 0 and back_qty == 0:
            ticket = self.algo.MarketOrder(front, front_qty, tag=f"CLOSE: EMERGENCY SHORT COVER {tag}")
            if ticket:
                exit_tickets = [ticket]

        if not exit_tickets:
            return False

        position["is_liquidating"] = True
        position["exit_reason"] = tag
        position["liquidation_start_time"] = self.algo.Time

        close_tag = f"CLOSE:{tag}"
        for t in exit_tickets:
            self.algo._pending_exit_tickets[t.OrderId] = position
            try:
                uf = UpdateOrderFields()
                uf.Tag = close_tag
                t.Update(uf)
            except Exception:
                pass

        return True

    def ManagePositions(self, data: Slice) -> None:
        cur_t = self.algo.Time.time()
        if cur_t < time(9, 35) or cur_t >= time(16, 0):
            return

        # Adaptive limit order escalation for pending entries
        for o_id, info in list(self.algo._pending_entry_tickets.items()):
            if info.get("entry_is_adaptive", False):
                entry_submission = info.get("entry_time", self.algo.Time)
                pending_hours = (self.algo.Time - entry_submission).total_seconds() / 3600.0
                if pending_hours >= 1.0 or self.algo.Time.hour >= 15:
                    ticket = self.algo.Transactions.GetOrderTicket(o_id)
                    if ticket and ticket.Status in [OrderStatus.Submitted, OrderStatus.New]:
                        try:
                            uf = UpdateOrderFields()
                            nat_ask = info.get("natural_ask", 0.01)
                            if nat_ask > 0:
                                uf.LimitPrice = nat_ask
                                ticket.Update(uf)
                        except Exception:
                            pass
                    info["entry_is_adaptive"] = False

        for spread_key, position in list(self.algo.active_spreads.items()):
            underlying = position.get("underlying")
            front = position.get("front")
            back = position.get("back")
            entry_debit = float(position.get("entry_price", 0.0))
            underlying_price = float(self.algo.Securities[underlying].Price) if underlying in self.algo.Securities else 0.0

            if front and back and entry_debit > 0:
                front_sec = self.algo.Securities.get(front)
                back_sec = self.algo.Securities.get(back)
                if front_sec and back_sec:
                    f_ask = float(front_sec.AskPrice) if hasattr(front_sec, "AskPrice") else 0.0
                    b_bid = float(back_sec.BidPrice) if hasattr(back_sec, "BidPrice") else 0.0
                    if f_ask > 0 and b_bid > 0:
                        cur_credit = b_bid - f_ask
                        cur_ret_pct = round(((cur_credit - entry_debit) / entry_debit) * 100.0, 2)
                        position["mae_pct"] = min(position.get("mae_pct", 0.0), cur_ret_pct)
                        position["mfe_pct"] = max(position.get("mfe_pct", 0.0), cur_ret_pct)

            if front and front in self.algo.Securities and underlying_price > 0:
                front_price = self.algo.GetOptionMidPrice(front)
                if front_price > 0:
                    T_front = max((front.ID.Date - self.algo.Time).total_seconds(), 0.0) / (365.0 * 24 * 3600)
                    if T_front > 0:
                        cur_front_iv = self.algo._implied_volatility_newton(front.ID.OptionRight, underlying_price, float(front.ID.StrikePrice), T_front, self.algo.risk_free_rate, front_price)
                        if cur_front_iv is not None and cur_front_iv > 0:
                            position["front_iv_max"] = max(position.get("front_iv_max", cur_front_iv), cur_front_iv)
                            position["front_iv_min"] = min(position.get("front_iv_min", cur_front_iv), cur_front_iv)
                            position["last_front_iv"] = cur_front_iv

            if back and back in self.algo.Securities and underlying_price > 0:
                back_price = self.algo.GetOptionMidPrice(back)
                if back_price > 0:
                    T_back = max((back.ID.Date - self.algo.Time).total_seconds(), 0.0) / (365.0 * 24 * 3600)
                    if T_back > 0:
                        cur_back_iv = self.algo._implied_volatility_newton(back.ID.OptionRight, underlying_price, float(back.ID.StrikePrice), T_back, self.algo.risk_free_rate, back_price)
                        if cur_back_iv is not None and cur_back_iv > 0:
                            position["back_iv_max"] = max(position.get("back_iv_max", cur_back_iv), cur_back_iv)
                            position["back_iv_min"] = min(position.get("back_iv_min", cur_back_iv), cur_back_iv)
                            position["last_back_iv"] = cur_back_iv

            front_expiry = front.ID.Date if front else None
            if front_expiry:
                expiry_close = datetime.combine(front_expiry.date(), time(16, 0))
                hours_to_front_expiry = (expiry_close - self.algo.Time).total_seconds() / 3600.0
            else:
                hours_to_front_expiry = 999.0

            entry_time = position.get("entry_time", self.algo.Time)
            days_held = (self.algo.Time.date() - entry_time.date()).days

            # L-02: Enforce mandatory hard close at least 3 hours before front-leg market close on expiration day
            if hours_to_front_expiry <= 3.0 or days_held >= 2:
                self.algo.Log(f"[EXPIRY SAFETY FORCE CLOSE] Closing spread {spread_key} (Hours: {hours_to_front_expiry:.1f}h, Days: {days_held})")
                self.LiquidateSpread(spread_key, "Expiry Safety Force Close")
                continue

            # Adaptive limit escalation for pending exits
            if position.get("is_liquidating", False):
                liq_start = position.get("liquidation_start_time", self.algo.Time)
                pending_liq_hours = (self.algo.Time - liq_start).total_seconds() / 3600.0

                if position.get("exit_is_adaptive", False) and pending_liq_hours >= 1.0:
                    nat_credit = position.get("natural_credit", 0.0)
                    if nat_credit >= 0.01:
                        for ticket_id, pos in list(self.algo._pending_exit_tickets.items()):
                            if pos is position:
                                ticket = self.algo.Transactions.GetOrderTicket(ticket_id)
                                if ticket and ticket.Status in [OrderStatus.Submitted, OrderStatus.New]:
                                    try:
                                        uf = UpdateOrderFields()
                                        uf.LimitPrice = -round(nat_credit, 2)
                                        ticket.Update(uf)
                                    except Exception:
                                        pass
                    position["exit_is_adaptive"] = False

                if pending_liq_hours >= 3.0 or self.algo.Time.hour >= 15:
                    front_qty = abs(self.algo.Portfolio[front].Quantity) if front and self.algo.Portfolio.ContainsKey(front) else 0
                    back_qty = abs(self.algo.Portfolio[back].Quantity) if back and self.algo.Portfolio.ContainsKey(back) else 0
                    if front_qty > 0 and back_qty > 0:
                        combo_qty = min(front_qty, back_qty)
                        exit_legs = [Leg.Create(front, 1), Leg.Create(back, -1)]
                        for ticket_id in list(self.algo._pending_exit_tickets.keys()):
                            if self.algo._pending_exit_tickets.get(ticket_id) is position:
                                try:
                                    t = self.algo.Transactions.GetOrderTicket(ticket_id)
                                    if t and t.Status in [OrderStatus.Submitted, OrderStatus.New]:
                                        t.Cancel("Canceling pending limit before market close")
                                except Exception:
                                    pass
                        self.algo.ComboMarketOrder(exit_legs, combo_qty, tag="CLOSE: Force Market Close Combo")
                    elif back_qty > 0 and front_qty == 0:
                        self.algo.MarketOrder(back, -back_qty, tag="CLOSE: Force Flatten Long Leg")
                    elif front_qty > 0 and back_qty == 0:
                        self.algo.MarketOrder(front, front_qty, tag="CLOSE: Force Cover Short Leg")
                continue

            report_date = position.get("report_date")
            report_time = position.get("report_time", "")
            is_amc = "AMC" in str(report_time).upper() or (report_date and report_date.hour >= 12)
            is_post_earnings = False
            if report_date:
                if is_amc:
                    is_post_earnings = (self.algo.Time.date() > report_date.date())
                else:
                    is_post_earnings = (self.algo.Time.date() >= report_date.date())
            else:
                entry_t = position.get("entry_time", self.algo.Time)
                is_post_earnings = (self.algo.Time.date() > entry_t.date())

            # L-02: Automatic Delta/ITM stop: if short option is >= 8% ITM post-earnings, exit immediately to prevent expiration assignment
            strike = float(front.ID.StrikePrice) if front else 0.0
            if is_post_earnings and strike > 0 and underlying_price > 0:
                itm_pct = abs(underlying_price - strike) / strike
                if itm_pct >= 0.08:
                    self.algo.Log(f"[ITM SAFETY STOP] Underlying gap detected for {spread_key}: {underlying_price:.2f} vs strike {strike:.2f} ({itm_pct*100:.1f}% ITM). Forcing liquidation.")
                    self.LiquidateSpread(spread_key, "ITM Safety Stop Exit")
                    continue

            # Standard scheduled post-earnings exit at exit_hour (10:00 AM EST)
            if is_post_earnings and self.algo.Time.hour >= self.algo.exit_hour:
                self.LiquidateSpread(spread_key, "Post-Earnings 10 AM Exit")
                continue
