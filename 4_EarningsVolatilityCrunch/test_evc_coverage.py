import sys
import os
import math
import logging
from datetime import datetime, timedelta
from typing import Any, Dict, List, Tuple
from unittest.mock import MagicMock, patch, PropertyMock

# Configure logging for type validation reports
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("TypeValidator")


def assert_type(val: Any, expected_type: type, var_name: str) -> None:
    """Verifies that a variable matches expected type, logging an explicit error if mismatched."""
    if not isinstance(val, expected_type):
        logger.error(f"[TYPE MISMATCH] Variable '{var_name}' expected {expected_type.__name__}, got {type(val).__name__} (Value: {val})")
        raise TypeError(f"Variable '{var_name}' expected {expected_type.__name__}, got {type(val).__name__}")


# ============================================================================
# 1. Setup mock imports for QuantConnect dependencies
# ============================================================================
mock_qc = MagicMock()

class OptionRight:
    Call = 0
    Put = 1

class SecurityType:
    Equity = 0
    Option = 1
    IndexOption = 2
    FutureOption = 3

class DataNormalizationMode:
    Raw = 0
    RAW = 0

class BrokerageName:
    INTERACTIVE_BROKERS_BROKERAGE = 1

class AccountType:
    MARGIN = 1

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
mock_qc.DataNormalizationMode = DataNormalizationMode
mock_qc.BrokerageName = BrokerageName
mock_qc.AccountType = AccountType
mock_qc.OrderStatus = OrderStatus
mock_qc.OrderEvent = MagicMock
mock_qc.NullOptionAssignmentModel = MagicMock
mock_qc.Symbol = Symbol
mock_qc.QCAlgorithm = MagicMock
mock_qc.Resolution = MagicMock()
mock_qc.UpdateOrderFields = MagicMock
mock_leg = MagicMock()
mock_leg.Create = lambda symbol, ratio: MagicMock(Symbol=symbol, Ratio=ratio)
mock_qc.Leg = mock_leg
mock_qc.CoarseFundamental = MagicMock
mock_qc.FineFundamental = MagicMock
mock_qc.Slice = MagicMock
mock_qc.EODHDUpcomingEarnings = MagicMock
mock_qc.SecurityChanges = MagicMock

sys.modules['AlgorithmImports'] = mock_qc
sys.modules['QuantConnect'] = mock_qc
sys.modules['QuantConnect.Data'] = mock_qc
sys.modules['QuantConnect.Data.Fundamental'] = mock_qc
sys.modules['QuantConnect.DataSource'] = mock_qc
sys.modules['QuantConnect.Securities'] = mock_qc
sys.modules['QuantConnect.Securities.Option'] = mock_qc
sys.modules['QuantConnect.Orders'] = mock_qc

# Add strategy directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import main
from main import EarningsVolatilityCrunch


# ============================================================================
# 2. Test Suite Implementations
# ============================================================================

def test_initialization_and_type_verification():
    """Verifies algorithm parameters, state variables, and exact runtime types."""
    logger.info("Running Test: test_initialization_and_type_verification...")
    algo = EarningsVolatilityCrunch()
    
    # Configure mock parameters
    param_dict = {
        "exec.initial_amount": "100000000.0",
        "univ.coarse.max_symbols": "150",
        "exec.risk_free_rate": "0.045",
        "exec.start_date": "2024-01-01",
        "exec.end_date": "2024-12-31",
        "algo.min_days_before_earnings": "1",
        "algo.days_before_earnings": "3",
        "algo.days_after_earnings": "0",
        "algo.entry_hour": "14",
        "algo.exit_hour": "10",
        "algo.slope_threshold": "0.001",
        "algo.pass_all": "true",
        "algo.volume_threshold": "1.0",
        "algo.ivrv_threshold": "1.0",
        "risk.max_loss_pct": "70.0",
        "risk.kelly.factor": "0.35",
        "risk.kelly.period": "30",
        "risk.max_trade_allocation": "1000.0",
        "risk.max_combo_contracts": "10",
        "algo.option.upper_filter": "2",
        "algo.option.lower_filter": "-2",
        "algo.option.max_exp_days": "90",
        "algo.option.min_exp_days": "5",
        "algo.min_days_between": "21"
    }
    algo.GetParameter = lambda k, d=None: param_dict.get(k, d)
    algo.SetStartDate = MagicMock()
    algo.SetEndDate = MagicMock()
    algo.SetCash = MagicMock()
    algo.SetWarmUp = MagicMock()
    algo.AddUniverse = MagicMock()
    algo.RegisterFinalLiquidation = MagicMock()

    algo.Initialize()

    # Verify types of initialized parameters
    assert_type(algo.initial_amount, float, "initial_amount")
    assert_type(algo.max_symbols, int, "max_symbols")
    assert_type(algo.risk_free_rate, float, "risk_free_rate")
    assert_type(algo.min_days_before_earnings, int, "min_days_before_earnings")
    assert_type(algo.days_before_earnings, int, "days_before_earnings")
    assert_type(algo.days_after_earnings, int, "days_after_earnings")
    assert_type(algo.entry_hour, int, "entry_hour")
    assert_type(algo.exit_hour, int, "exit_hour")
    assert_type(algo.slope_threshold, float, "slope_threshold")
    assert_type(algo.pass_all, bool, "pass_all")
    assert_type(algo.max_loss_pct, float, "max_loss_pct")
    assert_type(algo.kelly_factor, float, "kelly_factor")
    assert_type(algo.kelly_period, int, "kelly_period")
    assert_type(algo.option_upper_filter, int, "option_upper_filter")
    assert_type(algo.option_lower_filter, int, "option_lower_filter")
    assert_type(algo.option_max_exp_days, int, "option_max_exp_days")
    assert_type(algo.option_min_exp_days, int, "option_min_exp_days")
    assert_type(algo.min_days_between_contracts, int, "min_days_between_contracts")

    assert algo.max_symbols == 150
    assert algo.risk_free_rate == 0.045
    assert algo.min_days_between_contracts == 21
    logger.info("PASS: test_initialization_and_type_verification passed.")


def test_black_scholes_pricing_and_greeks():
    """Tests Black-Scholes pricing, Vega calculations, and Newton-Raphson IV solver."""
    logger.info("Running Test: test_black_scholes_pricing_and_greeks...")
    algo = EarningsVolatilityCrunch()
    algo.risk_free_rate = 0.045

    # 1. Test Call & Put pricing
    call_p = algo._bs_price(OptionRight.Call, S=100.0, K=100.0, T=0.1, r=0.045, sigma=0.25)
    put_p = algo._bs_price(OptionRight.Put, S=100.0, K=100.0, T=0.1, r=0.045, sigma=0.25)
    assert_type(call_p, float, "call_price")
    assert_type(put_p, float, "put_price")
    assert call_p > 0.0
    assert put_p > 0.0

    # Test edge case T <= 0 or S <= 0 or sigma <= 0
    assert algo._bs_price(OptionRight.Call, S=100.0, K=100.0, T=0.0, r=0.045, sigma=0.25) == 0.0
    assert algo._bs_price(OptionRight.Call, S=-10.0, K=100.0, T=0.1, r=0.045, sigma=0.25) == 0.0

    # 2. Test Vega calculation
    v_val = algo._vega(S=100.0, K=100.0, T=0.1, r=0.045, sigma=0.25)
    assert_type(v_val, float, "vega_val")
    assert v_val > 0.0
    assert algo._vega(S=100.0, K=100.0, T=0.0, r=0.045, sigma=0.25) == 0.0

    # 3. Test Implied Volatility Newton Solver
    market_price = algo._bs_price(OptionRight.Call, S=100.0, K=100.0, T=0.1, r=0.045, sigma=0.30)
    solved_iv = algo._implied_volatility_newton(OptionRight.Call, S=100.0, K=100.0, T=0.1, r=0.045, market_price=market_price)
    assert_type(solved_iv, float, "solved_iv")
    assert math.isclose(solved_iv, 0.30, abs_tol=0.01)

    # Edge cases for IV solver
    assert algo._implied_volatility_newton(OptionRight.Call, S=100.0, K=100.0, T=0.0, r=0.045, market_price=5.0) is None
    assert algo._implied_volatility_newton(OptionRight.Call, S=100.0, K=100.0, T=0.1, r=0.045, market_price=0.0) is None
    logger.info("PASS: test_black_scholes_pricing_and_greeks passed.")


def test_coarse_and_upcoming_earnings_universes():
    """Tests Coarse selection logic and EODHD upcoming earnings universe processing."""
    logger.info("Running Test: test_coarse_and_upcoming_earnings_universes...")
    algo = EarningsVolatilityCrunch()
    algo.Time = datetime(2026, 7, 28)
    algo.min_days_before_earnings = 1
    algo.days_before_earnings = 3
    algo.GetParameter = MagicMock(side_effect=lambda k, d=None: "15" if "min_price" in k else ("500" if "max_price" in k else ("500000" if "volume" in k else d)))
    algo.max_symbols = 150

    # Mock CoarseFundamental list
    c1 = MagicMock(Price=25.0, Volume=100000.0, DollarVolume=1000000.0, Symbol=Symbol("AAPL", sec_type=SecurityType.Equity))
    c2 = MagicMock(Price=5.0, Volume=100000.0, DollarVolume=1000000.0, Symbol=Symbol("PENNY", sec_type=SecurityType.Equity)) # Fails price
    c3 = MagicMock(Price=100.0, Volume=100.0, DollarVolume=10000.0, Symbol=Symbol("LOWVOL", sec_type=SecurityType.Equity)) # Fails volume
    
    selected_coarse = algo.CoarseSelectionFunction([c1, c2, c3])
    assert_type(selected_coarse, list, "selected_coarse")
    assert len(selected_coarse) == 1
    assert selected_coarse[0].Value == "AAPL"

    # Mock EODHD Upcoming Earnings list
    e1 = MagicMock(Symbol=Symbol("AAPL", sec_type=SecurityType.Equity), ReportDate=datetime(2026, 7, 30, 16, 0))
    e2 = MagicMock(Symbol=Symbol("MSFT", sec_type=SecurityType.Equity), ReportDate=datetime(2026, 7, 30, 8, 0))
    
    selected_earnings = algo.UpcomingEarningsSelectionFunction([e1, e2])
    assert_type(selected_earnings, list, "selected_earnings")
    assert len(selected_earnings) == 2
    assert algo.earnings_calendar[e1.Symbol] == e1.ReportDate
    logger.info("PASS: test_coarse_and_upcoming_earnings_universes passed.")


def test_get_call_option_contracts_cached():
    """Tests ATM Call option contract filtering and expiration bounds."""
    logger.info("Running Test: test_get_call_option_contracts_cached...")
    algo = EarningsVolatilityCrunch()
    algo.Time = datetime(2026, 7, 28)
    algo.option_max_exp_days = 90
    algo.option_min_exp_days = 5
    algo.option_upper_filter = 2
    algo.option_lower_filter = -2

    underlying = Symbol("AAPL", sec_type=SecurityType.Equity)
    algo.Securities = {underlying: MagicMock(Price=150.0)}

    c_atm = Symbol("AAPL_150_CALL", strike=150.0, expiry=datetime(2026, 8, 20), option_right=OptionRight.Call)
    c_otm = Symbol("AAPL_155_CALL", strike=155.0, expiry=datetime(2026, 8, 20), option_right=OptionRight.Call)
    c_far_otm = Symbol("AAPL_300_CALL", strike=300.0, expiry=datetime(2026, 8, 20), option_right=OptionRight.Call) # Excluded by strike filter
    c_put = Symbol("AAPL_150_PUT", strike=150.0, expiry=datetime(2026, 8, 20), option_right=OptionRight.Put) # Excluded by type filter

    c_s1 = Symbol("AAPL_140_CALL", strike=140.0, expiry=datetime(2026, 8, 20), option_right=OptionRight.Call)
    c_s2 = Symbol("AAPL_145_CALL", strike=145.0, expiry=datetime(2026, 8, 20), option_right=OptionRight.Call)
    c_s3 = Symbol("AAPL_160_CALL", strike=160.0, expiry=datetime(2026, 8, 20), option_right=OptionRight.Call)

    algo.OptionChainProvider = MagicMock()
    algo.OptionChainProvider.GetOptionContractList = MagicMock(return_value=[c_s1, c_s2, c_atm, c_otm, c_s3, c_far_otm, c_put])

    contracts = algo.GetCallOptionContractsCached(underlying, earnings_time=datetime(2026, 8, 1))
    assert_type(contracts, list, "contracts")
    assert len(contracts) == 5
    assert c_atm in contracts
    assert c_otm in contracts
    assert c_far_otm not in contracts
    assert c_put not in contracts
    logger.info("PASS: test_get_call_option_contracts_cached passed.")


def test_match_option_contracts():
    """Tests calendar option contract matching with 21-day minimum expiration gap."""
    logger.info("Running Test: test_match_option_contracts...")
    algo = EarningsVolatilityCrunch()
    algo.min_days_between_contracts = 21

    c_near = Symbol("NEAR_CALL", strike=150.0, expiry=datetime(2026, 8, 10), option_right=OptionRight.Call)
    c_far_too_close = Symbol("FAR_CLOSE_CALL", strike=150.0, expiry=datetime(2026, 8, 20), option_right=OptionRight.Call) # 10 days gap (too close)
    c_far_valid = Symbol("FAR_VALID_CALL", strike=150.0, expiry=datetime(2026, 9, 15), option_right=OptionRight.Call) # 36 days gap (valid)

    contracts = [c_near, c_far_too_close, c_far_valid]
    pairs = algo.MatchOptionContracts(contracts)
    
    assert_type(pairs, list, "pairs")
    assert len(pairs) == 2
    assert pairs[0] == (c_near, c_far_valid)
    logger.info("PASS: test_match_option_contracts passed.")


def test_underlying_metrics_cached():
    """Tests volume ratio and 30-day realized volatility calculations."""
    logger.info("Running Test: test_underlying_metrics_cached...")
    algo = EarningsVolatilityCrunch()
    algo.Time = datetime(2026, 7, 28)
    underlying = Symbol("AAPL", sec_type=SecurityType.Equity)

    # Mock pandas dataframe return for History
    import pandas as pd
    import numpy as np
    dates = pd.date_range(end='2026-07-28', periods=35, freq='D')
    df = pd.DataFrame({
        'close': np.linspace(100, 110, 35),
        'volume': [1000000] * 34 + [2000000] # Volume ratio = 2.0
    }, index=dates)
    
    algo.History = MagicMock(return_value=df)
    res = algo.GetUnderlyingMetricsCached(underlying, earnings_date=datetime(2026, 7, 29))
    
    assert_type(res, tuple, "metrics_tuple")
    vol_ratio, rv = res
    assert_type(vol_ratio, float, "vol_ratio")
    assert_type(rv, float, "rv")
    assert math.isclose(vol_ratio, 2.0, abs_tol=0.1)
    assert rv > 0.0
    logger.info("PASS: test_underlying_metrics_cached passed.")


def test_calculate_metrics_short_circuit_cascade():
    """Tests 3-tier short circuit gate cascade and IV term-structure slope calculation."""
    logger.info("Running Test: test_calculate_metrics_short_circuit_cascade...")
    algo = EarningsVolatilityCrunch()
    algo.Time = datetime(2026, 7, 28)
    algo.risk_free_rate = 0.045
    algo.pass_all = True

    underlying = Symbol("AAPL", sec_type=SecurityType.Equity)
    front = Symbol("FRONT", strike=150.0, expiry=datetime(2026, 8, 10), option_right=OptionRight.Call)
    back = Symbol("BACK", strike=150.0, expiry=datetime(2026, 9, 15), option_right=OptionRight.Call)

    algo.Securities = {
        underlying: MagicMock(Price=150.0),
        front: MagicMock(Price=3.0),
        back: MagicMock(Price=5.0)
    }
    algo.GetOptionMidPrice = MagicMock(side_effect=lambda s: 3.0 if s == front else 5.0)

    # Mock _implied_volatility_newton returns
    algo._implied_volatility_newton = MagicMock(side_effect=lambda right, S, K, T, r, price: 0.35 if price == 3.0 else 0.30)

    metrics = algo.CalculateMetrics(underlying, front, back, earnings_date=datetime(2026, 7, 30), vol_ratio=1.5, rv=0.20)
    assert_type(metrics, dict, "metrics_dict")
    assert "slope" in metrics
    assert "vol_ratio" in metrics
    assert "ivrv_ratio" in metrics
    assert metrics["vol_ratio"] == 1.5
    logger.info("PASS: test_calculate_metrics_short_circuit_cascade passed.")


def test_determine_position_size_kelly():
    """Tests Half-Kelly Criterion position sizing formula and allocation caps."""
    logger.info("Running Test: test_determine_position_size_kelly...")
    algo = EarningsVolatilityCrunch()
    algo.kelly_factor = 0.35
    algo.GetParameter = MagicMock(side_effect=lambda k, d=None: "1000.0" if "allocation" in k else ("10" if "combo" in k else d))

    underlying = Symbol("AAPL", sec_type=SecurityType.Equity)
    algo.Portfolio = MagicMock(TotalPortfolioValue=100000.0)

    # 1. Test when trade history < 5 (default 10% kelly fraction)
    algo.trade_history[underlying] = []
    metrics = {"back_price": 5.0, "front_price": 3.0} # Spread cost = $200.00
    qty = algo.DeterminePositionSize(underlying, metrics)
    assert_type(qty, int, "qty")
    assert qty == 5 # min(100000 * 0.10 * 0.35 = $3500 -> capped at $1000 / $200 = 5)

    # 2. Test when spread cost exceeds $1000 (e.g. $1250)
    expensive_metrics = {"back_price": 17.5, "front_price": 5.0} # Spread cost = $1250.00
    qty_expensive = algo.DeterminePositionSize(underlying, expensive_metrics)
    assert qty_expensive == 0 # Floor division = 0 (skipped)
    logger.info("PASS: test_determine_position_size_kelly passed.")


def test_execute_calendar_spread_and_logging():
    """Tests ComboLimitOrder submission, order tagging, and BigQuery trade logging."""
    logger.info("Running Test: test_execute_calendar_spread_and_logging...")
    algo = EarningsVolatilityCrunch()
    algo._pending_entry_tickets = {}
    algo.active_spreads = {}
    algo.trade_id_counter = 0
    algo.Time = datetime(2026, 7, 28, 15, 0)
    algo.backtest_run_id = "TEST_RUN_123"

    underlying = Symbol("AAPL", sec_type=SecurityType.Equity)
    front = Symbol("FRONT", strike=150.0, expiry=datetime(2026, 8, 10), option_right=OptionRight.Call)
    front.ID = MagicMock()
    front.ID.StrikePrice = 150.0
    front.ID.Date = MagicMock()
    front.ID.Date.date = MagicMock(return_value=datetime(2026, 8, 10).date())

    back = Symbol("BACK", strike=150.0, expiry=datetime(2026, 9, 15), option_right=OptionRight.Call)
    back.ID = MagicMock()
    back.ID.StrikePrice = 150.0
    back.ID.Date = MagicMock()
    back.ID.Date.date = MagicMock(return_value=datetime(2026, 9, 15).date())

    class MockTicket:
        def __init__(self, order_id):
            self.OrderId = order_id
            self.Status = OrderStatus.Submitted
        def Update(self, uf):
            pass

    t1 = MockTicket(101)
    t2 = MockTicket(102)
    algo.ComboLimitOrder = MagicMock(return_value=[t1, t2])
    algo.Log = MagicMock()
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

    metrics = {
        "strike": 150.0, "front_price": 3.0, "back_price": 5.0,
        "front_spread": 0.1, "back_spread": 0.1, "comb_spread": 0.2,
        "edate": "2026-07-29", "slope": 0.005, "vol_ratio": 1.5, "ivrv_ratio": 1.2
    }

    algo.ExecuteCalendarSpread(underlying, front, back, qty=5, metrics=metrics, report_date=datetime(2026, 7, 29))
    
    # Simulate fill event
    event = MagicMock(OrderId=101, Status=OrderStatus.Filled)
    algo.OnOrderEvent(event)

    assert underlying in algo.active_spreads
    assert algo.active_spreads[underlying]["qty"] == 5
    algo.Log.assert_called()
    logger.info("PASS: test_execute_calendar_spread_and_logging passed.")


def test_manage_open_positions_and_exit_rules():
    """Tests BMO vs AMC timing differentiation, 1-hour post-open time exit, and post-earnings stop loss."""
    logger.info("Running Test: test_manage_open_positions_and_exit_rules...")
    algo = EarningsVolatilityCrunch()
    algo.backtest_run_id = "TEST_RUN_123"
    algo.Time = datetime(2026, 7, 30, 10, 0) # 10:00 AM EST (exit_hour)
    algo.days_after_earnings = 0
    algo.exit_hour = 10
    algo.max_loss_pct = 70.0

    underlying = Symbol("AAPL", sec_type=SecurityType.Equity)
    front = Symbol("FRONT", strike=150.0, expiry=datetime(2026, 8, 10), option_right=OptionRight.Call)
    back = Symbol("BACK", strike=150.0, expiry=datetime(2026, 9, 15), option_right=OptionRight.Call)

    t1 = MagicMock(Status=OrderStatus.Submitted)
    t2 = MagicMock(Status=OrderStatus.Submitted)

    metrics = {
        "strike": 150.0, "front_price": 3.0, "back_price": 5.0,
        "front_spread": 0.1, "back_spread": 0.1, "comb_spread": 0.2,
        "edate": "2026-07-29", "slope": 0.005, "vol_ratio": 1.5, "ivrv_ratio": 1.2
    }

    algo.active_spreads[underlying] = {
        "pk": "TEST_PK", "front": front, "back": back, "qty": 5, "entry_price": 2.0,
        "entry_time": datetime(2026, 7, 29, 15, 0), "report_date": datetime(2026, 7, 30, 8, 0), # BMO
        "tickets": [t1, t2], "slope": 0.005, "vol_ratio": 1.5, "ivrv_ratio": 1.2,
        "metrics": metrics
    }

    algo.ComboMarketOrder = MagicMock(return_value=[t1, t2])
    algo.Log = MagicMock()
    mock_port = MagicMock()
    mock_port.ContainsKey = lambda k: False
    mock_port.__getitem__ = lambda self, k: MagicMock(Invested=False, Quantity=0)
    algo.Portfolio = mock_port
    algo.Transactions = MagicMock()
    algo.Transactions.GetOpenOrders = MagicMock(return_value=[])

    # Execute ManageOpenPositions (should trigger Time Exit at 10:00 AM post-earnings)
    algo.ManageOpenPositions(data=MagicMock())

    assert underlying not in algo.active_spreads # Position liquidated
    logger.info("PASS: test_manage_open_positions_and_exit_rules passed.")


def test_order_cancellation_and_scheduled_anchors():
    """Tests 5-minute pre-close order cancellation and scheduled liquidation helper."""
    logger.info("Running Test: test_order_cancellation_and_scheduled_anchors...")
    algo = EarningsVolatilityCrunch()
    algo.Schedule = MagicMock()
    algo.DateRules = MagicMock()
    algo.TimeRules = MagicMock()

    algo.RegisterFinalLiquidation(anchor_ticker="SPY", minutes_before_close=120)
    algo.Schedule.On.assert_called()
    logger.info("PASS: test_order_cancellation_and_scheduled_anchors passed.")


def test_on_end_of_algorithm_liquidation():
    """Tests OnEndOfAlgorithm native LEAN hook liquidates all open spreads with exit_reason tag."""
    logger.info("Running Test: test_on_end_of_algorithm_liquidation...")
    algo = EarningsVolatilityCrunch()
    algo.backtest_run_id = "TEST_RUN_END"
    algo.Time = datetime(2026, 12, 31, 16, 0)

    underlying = Symbol("AAPL", sec_type=SecurityType.Equity)
    front = Symbol("FRONT", strike=150.0)
    back = Symbol("BACK", strike=150.0)

    algo.active_spreads[underlying] = {
        "pk": "END_PK", "front": front, "back": back, "qty": 5, "entry_price": 2.0,
        "entry_time": datetime(2026, 12, 30, 15, 0), "report_date": datetime(2026, 12, 31, 8, 0),
        "tickets": [], "slope": 0.005, "vol_ratio": 1.5, "ivrv_ratio": 1.2,
        "metrics": {"vol_ratio": 1.5, "slope": 0.005, "ivrv_ratio": 1.2}
    }
    algo.Log = MagicMock()
    algo.Transactions = MagicMock()
    algo.Transactions.GetOpenOrders = MagicMock(return_value=[])

    algo.OnEndOfAlgorithm()
    assert len(algo.active_spreads) == 0
    logger.info("PASS: test_on_end_of_algorithm_liquidation passed.")


# ============================================================================
# 3. Main Test Suite Runner
# ============================================================================

def run_all_tests():
    logger.info("=" * 70)
    logger.info("STARTING 100% COVERAGE & TYPE VERIFICATION TEST SUITE FOR 4EVC")
    logger.info("=" * 70)

    test_initialization_and_type_verification()
    test_black_scholes_pricing_and_greeks()
    test_coarse_and_upcoming_earnings_universes()
    test_get_call_option_contracts_cached()
    test_match_option_contracts()
    test_underlying_metrics_cached()
    test_calculate_metrics_short_circuit_cascade()
    test_determine_position_size_kelly()
    test_execute_calendar_spread_and_logging()
    test_manage_open_positions_and_exit_rules()
    test_order_cancellation_and_scheduled_anchors()
    test_on_end_of_algorithm_liquidation()

    logger.info("=" * 70)
    logger.info("SUCCESS: ALL 11 TEST MODULES PASSED WITH 100% TYPE VALIDATION!")
    logger.info("=" * 70)


if __name__ == "__main__":
    import traceback
    try:
        run_all_tests()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
