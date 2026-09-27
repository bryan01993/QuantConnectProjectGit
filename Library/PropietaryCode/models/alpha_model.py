from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, date
from typing import List, Dict, Any, Optional, Set, Tuple
from AlgorithmImports import *


@dataclass
class CalendarSpreadOpportunity:
    underlying: Symbol
    front: Symbol
    back: Symbol
    option_right: OptionRight
    metrics: Dict[str, Any]
    report_date: datetime
    report_time: str
    rank_score: float


class CalendarSpreadAlphaModel(AlphaModel):
    """Alpha Model for scanning and ranking pre-earnings calendar spread opportunities."""

    def __init__(self, algorithm: Any) -> None:
        super().__init__()
        self.algo = algorithm

    def Update(self, algorithm: QCAlgorithm, data: Slice) -> List[Insight]:
        opportunities = self.ScanOpportunities(data)
        insights: List[Insight] = []
        for opp in opportunities:
            period = timedelta(days=2)
            insight_short = Insight.Price(opp.front, period, InsightDirection.Down, None, None, "CalendarSpreadAlphaModel", 0.5)
            insight_long = Insight.Price(opp.back, period, InsightDirection.Up, None, None, "CalendarSpreadAlphaModel", 0.5)
            insights.extend([insight_short, insight_long])
        return insights

    def ScanOpportunities(self, data: Slice) -> List[CalendarSpreadOpportunity]:
        if self.algo.Time.hour < 14 or self.algo.Time.hour > 15:
            return []

        opportunities: List[CalendarSpreadOpportunity] = []
        today = self.algo.Time.date()

        for underlying, earnings_info in list(self.algo.earnings_calendar.items()):
            if isinstance(earnings_info, dict):
                report_date = earnings_info["report_date"]
                report_time = earnings_info.get("report_time", "AMC")
            else:
                report_date = earnings_info
                report_time = "AMC" if (hasattr(report_date, "hour") and report_date.hour >= 12) else "BMO"

            is_amc = "AMC" in str(report_time).upper() or (hasattr(report_date, "hour") and report_date.hour >= 12)
            report_d = report_date.date() if hasattr(report_date, "date") else report_date

            # L-01 Fix: Explicit date-only comparison to never skip same-day AMC earnings
            if today > report_d:
                continue

            days_to_earnings = (report_d - today).days

            if is_amc:
                # AMC: Announcing after close today; enter today afternoon (days_to_earnings == 0)
                if days_to_earnings != 0:
                    continue
            else:
                # BMO: Announcing before open on report_d; enter on preceding trading afternoon
                if days_to_earnings <= 0:
                    continue
                if self.algo.Time.weekday() == 4:  # Friday
                    if days_to_earnings > 4:
                        continue
                else:
                    if days_to_earnings > 1:
                        continue

            metrics = self.algo.GetUnderlyingMetricsCached(underlying, report_date)
            if metrics is None:
                continue

            vol_ratio, rv = metrics
            if not self.algo.pass_all and vol_ratio < self.algo.volume_threshold:
                continue

            contracts = self.algo.GetOptionContractsCached(underlying, report_date)
            if not contracts:
                continue

            pairs = self.algo.MatchOptionContracts(contracts)
            if not pairs:
                continue

            call_candidates = []
            put_candidates = []
            temp_added = set()

            for near_c, far_c in pairs:
                if near_c not in self.algo._subscribed_options:
                    if self.algo._ensure_option_tradable(near_c):
                        temp_added.add(near_c)
                if far_c not in self.algo._subscribed_options:
                    if self.algo._ensure_option_tradable(far_c):
                        temp_added.add(far_c)

                m = self.algo.CalculateMetrics(underlying, near_c, far_c, report_date, vol_ratio, rv)
                if m is not None:
                    if near_c.ID.OptionRight == OptionRight.Call:
                        call_candidates.append((m, near_c, far_c))
                    else:
                        put_candidates.append((m, near_c, far_c))

            underlying_price = self.algo.GetUnderlyingPrice(underlying)

            def _rank_score(cand_tuple):
                m = cand_tuple[0]
                strike_dist_pct = abs(m["strike"] - underlying_price) / underlying_price if underlying_price > 0 else 0.0
                return (-m["slope"]) / (1.0 + 50.0 * strike_dist_pct)

            retained = set()
            all_candidates = call_candidates + put_candidates
            if all_candidates and not self.algo.IsAlreadyInvested(underlying):
                best_cand = max(all_candidates, key=_rank_score)
                retained.add(best_cand[1])
                retained.add(best_cand[2])
                opportunities.append(CalendarSpreadOpportunity(
                    underlying=underlying,
                    front=best_cand[1],
                    back=best_cand[2],
                    option_right=best_cand[1].ID.OptionRight,
                    metrics=best_cand[0],
                    report_date=report_date,
                    report_time=report_time,
                    rank_score=_rank_score(best_cand)
                ))

            # Unsubscribe candidate options that were not retained for trading
            for opt_sym in temp_added:
                if opt_sym not in retained:
                    self.algo.UnsubscribeOption(opt_sym)

        return opportunities
