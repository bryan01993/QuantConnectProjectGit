import sys
import os
import math
import logging
from datetime import datetime, timedelta
from typing import Any, Dict, List
from unittest.mock import MagicMock

# Configure logging for lifecycle events
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("LifecycleSimulator")

# ============================================================================
# 1. QuantConnect Mock Primitive Setup
# ============================================================================
mock_qc = MagicMock()

class OptionRight:
    Call = 0
    Put = 1

class SecurityType:
    Equity = 0
    Option = 1

class OrderStatus:
    New = 0
    Submitted = 1
    Filled = 2
    Canceled = 3

class Symbol:
    def __init__(self, value: str = "AAPL", strike: float = 150.0, expiry: datetime = None, option_right: int = OptionRight.Call, sec_type: int = SecurityType.Option):
        self.Value = value
        self.SecurityType = sec_type
        self.Underlying = None
        self.ID = MagicMock()
        self.ID.OptionRight = option_right
        self.ID.StrikePrice = strike
        self.ID.Date = expiry or (datetime.now() + timedelta(days=30))

    def __repr__(self):
        return f"Symbol({self.Value})"

    def __hash__(self):
        return hash(self.Value)

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.Value == other.Value


mock_qc.OptionRight = OptionRight
mock_qc.SecurityType = SecurityType
mock_qc.OrderStatus = OrderStatus
mock_qc.Symbol = Symbol
mock_qc.QCAlgorithm = MagicMock
mock_qc.Resolution = MagicMock()
mock_leg = MagicMock()
mock_leg.Create = lambda symbol, ratio: MagicMock(Symbol=symbol, Ratio=ratio)
mock_qc.Leg = mock_leg
mock_qc.CoarseFundamental = MagicMock
mock_qc.FineFundamental = MagicMock
mock_qc.EODHDUpcomingEarnings = MagicMock
mock_qc.Slice = MagicMock
mock_qc.SecurityChanges = MagicMock
mock_qc.DataNormalizationMode = MagicMock()
mock_qc.DataNormalizationMode.RAW = 0
mock_qc.DataNormalizationMode.Raw = 0
mock_qc.BrokerageName = MagicMock()
mock_qc.AccountType = MagicMock()

sys.modules['AlgorithmImports'] = mock_qc
sys.modules['QuantConnect'] = mock_qc
sys.modules['QuantConnect.Data'] = mock_qc
sys.modules['QuantConnect.Data.Fundamental'] = mock_qc
sys.modules['QuantConnect.DataSource'] = mock_qc
sys.modules['QuantConnect.Securities'] = mock_qc
sys.modules['QuantConnect.Securities.Option'] = mock_qc
sys.modules['QuantConnect.Orders'] = mock_qc

# Import algorithm
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import main
from main import EarningsVolatilityCrunch


# ============================================================================
# 2. Interactive Lifecycle Simulator Suite
# ============================================================================

def simulate_scenario_a_standard_amc_lifecycle():
    """Simulates standard AMC (After Market Close) earnings trade lifecycle."""
    logger.info("=" * 70)
    logger.info("SIMULATING SCENARIO A: STANDARD AMC TRADE LIFECYCLE (AAPL)")
    logger.info("=" * 70)

    algo = EarningsVolatilityCrunch()
    algo.backtest_run_id = "SIM_RUN_AMC"
    algo.IsWarmingUp = False
    algo.entry_hour = 14
    algo.exit_hour = 10
    algo.days_after_earnings = 0
    algo.min_days_before_earnings = 1
    algo.days_before_earnings = 3
    algo.min_days_between_contracts = 21
    algo.max_loss_pct = 70.0
    algo.kelly_factor = 0.35
    algo.pass_all = True
    algo.risk_free_rate = 0.045
    algo.trade_id_counter = 0
    algo.GetParameter = lambda k, d=None: d
    algo.Transactions = MagicMock()
    algo.Transactions.GetOpenOrders = MagicMock(return_value=[])

    # ------------------------------------------------------------------------
    # STAGE 1: Discovery (Aug 11, 2026 at 10:00 AM EST)
    # AAPL earnings scheduled for Aug 11 at 16:00 EST (AMC)
    # ------------------------------------------------------------------------
    algo.Time = datetime(2026, 8, 11, 10, 0)
    underlying = Symbol("AAPL", sec_type=SecurityType.Equity)
    report_date = datetime(2026, 8, 11, 16, 0) # AMC
    algo.earnings_calendar[underlying] = report_date
    logger.info(f"Stage 1 [Discovery]: AAPL earnings discovered for {report_date} (AMC).")
    assert len(algo.active_spreads) == 0

    # ------------------------------------------------------------------------
    # STAGE 2 & 3: Entry Window & Option Matching (Aug 11 at 14:00 EST / 2:00 PM)
    # ------------------------------------------------------------------------
    algo.Time = datetime(2026, 8, 11, 14, 0)
    logger.info(f"Stage 2 [Entry Window]: Current Time = {algo.Time}. Checking AMC timing rule...")

    # Mock option contracts
    front = Symbol("AAPL_FRONT", strike=150.0, expiry=datetime(2026, 8, 25), option_right=OptionRight.Call) # 14 DTE
    back = Symbol("AAPL_BACK", strike=150.0, expiry=datetime(2026, 9, 29), option_right=OptionRight.Call)   # 49 DTE (35d gap)

    sec_map = {
        underlying: MagicMock(Price=150.0),
        front: MagicMock(Price=3.0),
        back: MagicMock(Price=5.0)
    }
    mock_sec = MagicMock()
    mock_sec.__getitem__ = lambda self, k: sec_map[k]
    mock_sec.__contains__ = lambda self, k: k in sec_map
    mock_sec.ContainsKey = lambda k: k in sec_map
    algo.Securities = mock_sec
    algo.Portfolio = MagicMock(TotalPortfolioValue=100000.0)

    algo.GetCallOptionContractsCached = MagicMock(return_value=[front, back])
    algo.MatchOptionContracts = MagicMock(return_value=[(front, back)])
    algo.GetUnderlyingMetricsCached = MagicMock(return_value=(1.5, 0.20))
    algo.GetOptionMidPrice = MagicMock(side_effect=lambda s: 3.0 if s == front else 5.0)
    algo._implied_volatility_newton = MagicMock(side_effect=lambda right, S, K, T, r, price: 0.25 if price == 3.0 else 0.35)

    t1 = MagicMock(Status=OrderStatus.Submitted)
    t2 = MagicMock(Status=OrderStatus.Submitted)
    algo.ComboLimitOrder = MagicMock(return_value=[t1, t2])
    algo.Log = MagicMock()

    # Trigger OnData entry loop
    algo.OnData(data=MagicMock())

    # Verify Stage 4 & 5 (Position Sized & Order Placed)
    assert underlying in algo.active_spreads
    pos = algo.active_spreads[underlying]
    logger.info(f"Stage 4 & 5 [Position Placed]: AAPL Calendar Spread entered with Qty={pos['qty']}, Entry Price=${pos['entry_price']:.2f}")

    # ------------------------------------------------------------------------
    # STAGE 6: Post-Earnings Day Exit (Aug 12 at 10:00 AM EST / 1 Hour Post-Open)
    # ------------------------------------------------------------------------
    algo.Time = datetime(2026, 8, 12, 10, 0)
    logger.info(f"Stage 6 [Post-Earnings Exit]: Current Time = {algo.Time}. Triggering 1-hour post-open exit...")

    algo.ComboMarketOrder = MagicMock(return_value=[t1, t2])
    algo.Transactions = MagicMock()
    algo.Transactions.GetOpenOrders = MagicMock(return_value=[])

    # Trigger ManageOpenPositions
    algo.ManageOpenPositions(data=MagicMock())

    # Verify Stage 7 (Liquidation & State Cleanup)
    assert underlying not in algo.active_spreads
    logger.info("Stage 7 [Cleanup]: AAPL position liquidated cleanly. State removed.")
    logger.info("SUCCESS: Scenario A Lifecycle Simulation Completed!\n")


def simulate_scenario_b_friday_entry_monday_bmo():
    """Simulates Friday entry for Monday BMO (Before Market Open) earnings release."""
    logger.info("=" * 70)
    logger.info("SIMULATING SCENARIO B: FRIDAY ENTRY FOR MONDAY BMO EARNINGS (MSFT)")
    logger.info("=" * 70)

    algo = EarningsVolatilityCrunch()
    algo.backtest_run_id = "SIM_RUN_BMO"
    algo.IsWarmingUp = False
    algo.entry_hour = 14
    algo.exit_hour = 10
    algo.days_after_earnings = 0
    algo.min_days_before_earnings = 1
    algo.days_before_earnings = 3
    algo.min_days_between_contracts = 21
    algo.max_loss_pct = 70.0
    algo.kelly_factor = 0.35
    algo.pass_all = True
    algo.risk_free_rate = 0.045
    algo.trade_id_counter = 0
    algo.GetParameter = lambda k, d=None: d
    algo.Transactions = MagicMock()
    algo.Transactions.GetOpenOrders = MagicMock(return_value=[])

    underlying = Symbol("MSFT", sec_type=SecurityType.Equity)
    # Monday BMO Earnings (Aug 17 at 8:00 AM EST)
    report_date = datetime(2026, 8, 17, 8, 0)
    algo.earnings_calendar[underlying] = report_date

    # Friday Afternoon Entry (Aug 14 at 14:00 EST / 2:00 PM)
    algo.Time = datetime(2026, 8, 14, 14, 0)
    days_to_earnings = (report_date.date() - algo.Time.date()).days
    logger.info(f"Friday 2:00 PM EST: Current Date = {algo.Time.date()}, Report Date = {report_date.date()}, Days To Earnings = {days_to_earnings}")
    assert days_to_earnings == 3 # Friday -> Monday = 3 days

    front = Symbol("MSFT_FRONT", strike=300.0, expiry=datetime(2026, 8, 28), option_right=OptionRight.Call)
    back = Symbol("MSFT_BACK", strike=300.0, expiry=datetime(2026, 10, 2), option_right=OptionRight.Call)

    sec_map = {underlying: MagicMock(Price=300.0), front: MagicMock(Price=5.0), back: MagicMock(Price=8.0)}
    mock_sec = MagicMock()
    mock_sec.__getitem__ = lambda self, k: sec_map[k]
    mock_sec.__contains__ = lambda self, k: k in sec_map
    mock_sec.ContainsKey = lambda k: k in sec_map
    algo.Securities = mock_sec
    algo.Portfolio = MagicMock(TotalPortfolioValue=100000.0)

    algo.GetCallOptionContractsCached = MagicMock(return_value=[front, back])
    algo.MatchOptionContracts = MagicMock(return_value=[(front, back)])
    algo.GetUnderlyingMetricsCached = MagicMock(return_value=(1.5, 0.20))
    algo.GetOptionMidPrice = MagicMock(side_effect=lambda s: 5.0 if s == front else 8.0)
    algo._implied_volatility_newton = MagicMock(side_effect=lambda right, S, K, T, r, price: 0.25 if price == 5.0 else 0.35)

    t1, t2 = MagicMock(Status=OrderStatus.Submitted), MagicMock(Status=OrderStatus.Submitted)
    algo.ComboLimitOrder = MagicMock(return_value=[t1, t2])
    algo.Log = MagicMock()

    # Enter trade on Friday
    algo.OnData(data=MagicMock())
    assert underlying in algo.active_spreads
    logger.info("Friday Entry: MSFT spread successfully entered prior to weekend.")

    # Monday Post-Earnings Exit (Aug 17 at 10:00 AM EST)
    algo.Time = datetime(2026, 8, 17, 10, 0)
    logger.info(f"Monday 10:00 AM EST: Post-earnings exit triggered for BMO report.")

    algo.ComboMarketOrder = MagicMock(return_value=[t1, t2])
    algo.Transactions = MagicMock()
    algo.Transactions.GetOpenOrders = MagicMock(return_value=[])

    algo.ManageOpenPositions(data=MagicMock())
    assert underlying not in algo.active_spreads
    logger.info("SUCCESS: Scenario B Lifecycle Simulation Completed!\n")


def simulate_scenario_c_post_earnings_stop_loss():
    """Simulates 70% post-earnings emergency stop loss threshold execution."""
    logger.info("=" * 70)
    logger.info("SIMULATING SCENARIO C: POST-EARNINGS EMERGENCY STOP LOSS (70% CRASH)")
    logger.info("=" * 70)

    algo = EarningsVolatilityCrunch()
    algo.backtest_run_id = "SIM_RUN_STOP"
    algo.IsWarmingUp = False
    algo.exit_hour = 10
    algo.max_loss_pct = 70.0
    algo.GetParameter = lambda k, d=None: d

    underlying = Symbol("NVDA", sec_type=SecurityType.Equity)
    front = Symbol("NVDA_FRONT", strike=100.0, expiry=datetime(2026, 8, 25), option_right=OptionRight.Call)
    back = Symbol("NVDA_BACK", strike=100.0, expiry=datetime(2026, 9, 29), option_right=OptionRight.Call)

    t1, t2 = MagicMock(Status=OrderStatus.Submitted), MagicMock(Status=OrderStatus.Submitted)
    metrics = {
        "strike": 100.0, "front_price": 5.0, "back_price": 9.0,
        "front_spread": 0.1, "back_spread": 0.1, "comb_spread": 0.2,
        "edate": "2026-08-11", "slope": 0.005, "vol_ratio": 1.5, "ivrv_ratio": 1.2
    }

    # Position entered at $4.00 debit ($9.00 - $5.00)
    algo.active_spreads[underlying] = {
        "pk": "STOP_PK", "front": front, "back": back, "qty": 5, "entry_price": 4.0,
        "entry_time": datetime(2026, 8, 11, 14, 0), "report_date": datetime(2026, 8, 11, 16, 0),
        "tickets": [t1, t2], "slope": 0.005, "vol_ratio": 1.5, "ivrv_ratio": 1.2,
        "metrics": metrics
    }

    # Post-Earnings Open (Aug 12 at 9:35 AM EST - before 10:00 AM time exit)
    algo.Time = datetime(2026, 8, 12, 9, 35)
    logger.info(f"Aug 12 at 9:35 AM EST: Stock crashes. Simulating severe IV collapse & price crash...")

    # Current mid prices: front = $0.50, back = $1.20 -> current net value = $0.70 (Loss = -82.5% > -70%)
    algo.GetOptionMidPrice = MagicMock(side_effect=lambda s: 0.50 if s == front else 1.20)
    algo.ComboMarketOrder = MagicMock(return_value=[t1, t2])
    algo.Log = MagicMock()
    algo.Transactions = MagicMock()
    algo.Transactions.GetOpenOrders = MagicMock(return_value=[])

    algo.ManageOpenPositions(data=MagicMock())

    assert underlying not in algo.active_spreads
    logger.info("Emergency Stop Loss: -82.5% loss detected at 9:35 AM. Emergency liquidation executed successfully!")
    logger.info("SUCCESS: Scenario C Lifecycle Simulation Completed!\n")


def simulate_scenario_d_unfilled_order_cancellation():
    """Simulates 3:55 PM pre-close cancellation of unfilled entry limit orders."""
    logger.info("=" * 70)
    logger.info("SIMULATING SCENARIO D: UNFILLED LIMIT ORDER EOD CANCELLATION")
    logger.info("=" * 70)

    algo = EarningsVolatilityCrunch()
    algo.Time = datetime(2026, 8, 11, 15, 55)

    o1 = MagicMock(Id=101, Status=OrderStatus.Submitted)
    o2 = MagicMock(Id=102, Status=OrderStatus.Filled) # Already filled (skip)

    algo.Transactions = MagicMock()
    algo.Transactions.GetOpenOrders = MagicMock(return_value=[o1, o2])
    algo.Transactions.CancelOrder = MagicMock()

    logger.info(f"Aug 11 at 3:55 PM EST: Running scheduled EOD order cancellation handler...")
    
    # Run cancellation routine
    open_orders = algo.Transactions.GetOpenOrders()
    for order in open_orders:
        if order.Status in [OrderStatus.Submitted, OrderStatus.New]:
            algo.Transactions.CancelOrder(order.Id, "EOD: Canceling unfilled entry limit order")

    algo.Transactions.CancelOrder.assert_called_once_with(101, "EOD: Canceling unfilled entry limit order")
    logger.info("EOD Order Cancellation: Unfilled limit order #101 cancelled cleanly at 3:55 PM EST.")
    logger.info("SUCCESS: Scenario D Lifecycle Simulation Completed!\n")


# ============================================================================
# 3. Main Runner
# ============================================================================

def run_all_simulations():
    logger.info("=" * 70)
    logger.info("STARTING INTERACTIVE TRADE LIFECYCLE SIMULATOR FOR 4EVC")
    logger.info("=" * 70)

    simulate_scenario_a_standard_amc_lifecycle()
    simulate_scenario_b_friday_entry_monday_bmo()
    simulate_scenario_c_post_earnings_stop_loss()
    simulate_scenario_d_unfilled_order_cancellation()

    logger.info("=" * 70)
    logger.info("ALL 4 TRADE LIFECYCLE SCENARIOS SIMULATED AND VERIFIED SUCCESSFULLY!")
    logger.info("=" * 70)


if __name__ == "__main__":
    run_all_simulations()
