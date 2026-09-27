import sys
import os
import math
from datetime import datetime
from unittest.mock import MagicMock

# 1. Setup mock imports for QuantConnect dependencies
mock_imports = MagicMock()

class OptionRight:
    Call = 0
    Put = 1

mock_imports.OptionRight = OptionRight
mock_imports.QCAlgorithm = MagicMock
mock_imports.AlphaModel = MagicMock
mock_imports.ExecutionModel = MagicMock
mock_imports.Insight = MagicMock()
mock_imports.InsightDirection = MagicMock()
mock_imports.Resolution = MagicMock()
mock_imports.SecurityType = MagicMock()
mock_imports.DataNormalizationMode = MagicMock()
mock_imports.BrokerageName = MagicMock()
mock_imports.OrderEvent = MagicMock
mock_imports.OrderStatus = MagicMock()
mock_imports.NullOptionAssignmentModel = MagicMock
mock_imports.UpdateOrderFields = MagicMock()
mock_imports.Leg = MagicMock()
mock_imports.Symbol = MagicMock
mock_imports.CoarseFundamental = MagicMock
mock_imports.FineFundamental = MagicMock
mock_imports.Slice = MagicMock
mock_imports.EODHDUpcomingEarnings = MagicMock
mock_imports.SecurityChanges = MagicMock

# Inject mock modules into sys.modules before importing main
sys.modules['AlgorithmImports'] = mock_imports
sys.modules['QuantConnect'] = MagicMock()
sys.modules['QuantConnect.Data'] = MagicMock()
sys.modules['QuantConnect.Data.Fundamental'] = MagicMock()
sys.modules['QuantConnect.DataSource'] = MagicMock()
sys.modules['QuantConnect.Securities'] = MagicMock()
sys.modules['QuantConnect.Securities.Option'] = MagicMock()
sys.modules['QuantConnect.Orders'] = MagicMock()

# Add EVC directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import main
from main import EarningsVolatilityCrunch

def test_bs_price():
    """Verify Black-Scholes pricing solver for calls and puts."""
    algo = EarningsVolatilityCrunch()
    
    # S=100, K=100, T=0.1 (years), r=0.01, sigma=0.2
    # Verify call option value is approximately 2.56
    call_price = algo._bs_price(OptionRight.Call, 100.0, 100.0, 0.1, 0.01, 0.2)
    assert math.isclose(call_price, 2.56, abs_tol=0.05)

    # Verify put option value is approximately 2.46
    put_price = algo._bs_price(OptionRight.Put, 100.0, 100.0, 0.1, 0.01, 0.2)
    assert math.isclose(put_price, 2.46, abs_tol=0.05)

def test_vega():
    """Verify Vega calculation (sensitivity to volatility)."""
    algo = EarningsVolatilityCrunch()
    
    # Vega for S=100, K=100, T=0.1, r=0.01, sigma=0.2 should be positive and non-zero
    vega_val = algo._vega(100.0, 100.0, 0.1, 0.01, 0.2)
    assert vega_val > 0.0
    assert math.isclose(vega_val, 12.6, abs_tol=0.2)

def test_implied_volatility_newton():
    """Verify that Newton-Raphson solver converges back to original volatility."""
    algo = EarningsVolatilityCrunch()
    
    # Price a call option under S=100, K=100, T=0.1, r=0.01, sigma=0.25
    market_price = algo._bs_price(OptionRight.Call, 100.0, 100.0, 0.1, 0.01, 0.25)
    
    # Solve for Implied Volatility given the price
    solved_iv = algo._implied_volatility_newton(OptionRight.Call, 100.0, 100.0, 0.1, 0.01, market_price)
    
    assert solved_iv is not None
    assert math.isclose(solved_iv, 0.25, abs_tol=0.01)

def test_match_option_contracts():
    """Verify calendar matching logic pairs near and far contracts by strike for both Calls and Puts."""
    algo = EarningsVolatilityCrunch()
    
    # Create mock symbols/contracts for Calls
    c1 = MagicMock()
    c1.ID.OptionRight = OptionRight.Call
    c1.ID.StrikePrice = 150.0
    c1.ID.Date = datetime(2026, 7, 10)
    
    c2 = MagicMock()
    c2.ID.OptionRight = OptionRight.Call
    c2.ID.StrikePrice = 150.0
    c2.ID.Date = datetime(2026, 7, 17)
    
    c3 = MagicMock()
    c3.ID.OptionRight = OptionRight.Call
    c3.ID.StrikePrice = 160.0
    c3.ID.Date = datetime(2026, 7, 10)
    
    # Create mock symbols/contracts for Puts
    p1 = MagicMock()
    p1.ID.OptionRight = OptionRight.Put
    p1.ID.StrikePrice = 150.0
    p1.ID.Date = datetime(2026, 7, 10)
    
    p2 = MagicMock()
    p2.ID.OptionRight = OptionRight.Put
    p2.ID.StrikePrice = 150.0
    p2.ID.Date = datetime(2026, 7, 17)

    # Test pairing: (c1, c2) for Calls, (p1, p2) for Puts
    algo.min_days_between_contracts = 5
    algo.max_days_between_contracts = 31
    contracts = [c1, c3, c2, p1, p2]
    pairs = algo.MatchOptionContracts(contracts)
    
    assert len(pairs) == 2
    assert (c1, c2) in pairs
    assert (p1, p2) in pairs

def test_atomic_liquidation():
    """Verify Task 1.1: Atomic combo liquidation closes BOTH legs simultaneously."""
    class MockPortfolio(dict):
        def ContainsKey(self, key):
            return key in self

    algo = EarningsVolatilityCrunch()
    algo.active_spreads = {}
    algo.Portfolio = MockPortfolio()
    algo.Securities = {}
    algo.UnsubscribeOption = MagicMock()
    algo.ComboLimitOrder = MagicMock(return_value=[MagicMock()])
    algo.MarketOrder = MagicMock(return_value=MagicMock())
    algo._pending_exit_tickets = {}

    front = MagicMock()
    back = MagicMock()

    front_holding = MagicMock()
    front_holding.Quantity = -5
    back_holding = MagicMock()
    back_holding.Quantity = 5

    algo.Portfolio[front] = front_holding
    algo.Portfolio[back] = back_holding

    # Scenario: Natural credit < 0.01 (salvage / negative credit scenario)
    front_sec = MagicMock()
    front_sec.AskPrice = 2.0
    back_sec = MagicMock()
    back_sec.BidPrice = 1.0
    algo.Securities[front] = front_sec
    algo.Securities[back] = back_sec

    pos = {
        "front": front,
        "back": back,
        "qty": 5,
        "tickets": []
    }
    algo.active_spreads["test_pk"] = pos

    from main import CalendarSpreadExecutionManager
    exec_mgr = CalendarSpreadExecutionManager(algo)
    res = exec_mgr.LiquidateSpread("test_pk", "Test Atomic Close")

    assert res is True
    # Verify BOTH market orders were submitted (short cover + long close)
    assert algo.MarketOrder.call_count == 2
    calls = [c[0] for c in algo.MarketOrder.call_args_list]
    assert (front, 5) in [(c[0], c[1]) for c in calls]
    assert (back, -5) in [(c[0], c[1]) for c in calls]

def test_margin_position_sizing():
    """Verify Task 1.3: Dynamic margin pre-check prevents buying power exhaustion."""
    algo = EarningsVolatilityCrunch()
    algo.Portfolio = MagicMock()
    algo.Portfolio.TotalPortfolioValue = 100000.0
    algo.Portfolio.MarginRemaining = 500.0  # Only $500 margin remaining

    metrics = {"underlying_price": 100.0}
    # When natural_ask is $3.00 ($300/contract), $500 margin should only allow max 1 contract
    qty = algo.DeterminePositionSize(MagicMock(), metrics, natural_ask=3.0)
    assert qty <= 1

    # When margin is $0, qty MUST be 0
    algo.Portfolio.MarginRemaining = 0.0
    qty_zero = algo.DeterminePositionSize(MagicMock(), metrics, natural_ask=3.0)
    assert qty_zero == 0

def test_unclamped_exit_pnl():
    """Verify Task L-04: Negative exit credit is not clamped to 0.0 or -1.0."""
    algo = EarningsVolatilityCrunch()
    algo.LogTradeRecord = MagicMock()
    algo.Log = MagicMock()
    
    front = MagicMock()
    back = MagicMock()
    
    order_event = MagicMock()
    order_event.OrderId = 999
    order_event.Status = mock_imports.OrderStatus.Filled
    order_event.Symbol = back
    order_event.FillPrice = 1.0  # Far leg exit fill: $1.00
    
    info = {
        "underlying": MagicMock(),
        "front": front,
        "back": back,
        "qty": 1,
        "entry_price": 2.0,  # Entry debit was $2.00
        "exit_fills": {front: 2.5},  # Near leg exit cover fill: $2.50
        "metrics": {}
    }
    algo._pending_exit_tickets = {999: info}
    
    # Process exit fill: net credit is $1.00 - $2.50 = -$1.50 (negative exit credit)
    algo.OnOrderEvent(order_event)
    
    # True realized PnL should be (-1.50 - 2.00) / 2.00 = -1.75 (-175%), NOT clamped to -1.0 (-100%)
    calls = algo.LogTradeRecord.call_args_list
    assert len(calls) == 1
    call_kwargs = calls[0][1]
    assert math.isclose(call_kwargs["exit_price"], -1.5, abs_tol=1e-4)
    assert math.isclose(call_kwargs["pnl"], -1.75, abs_tol=1e-4)

def test_orphan_sweeper_short_and_long():
    """Verify Task L-05: Orphan sweeper closes both unhedged long and short option legs."""
    algo = EarningsVolatilityCrunch()
    algo.active_spreads = {}
    algo._pending_exit_tickets = {}
    algo._pending_entry_tickets = {}
    algo.Transactions = MagicMock()
    algo.Transactions.GetOpenOrders.return_value = []
    algo.MarketOrder = MagicMock()
    algo.Log = MagicMock()

    long_sec = MagicMock()
    long_sec.Invested = True
    long_sec.Symbol.SecurityType = mock_imports.SecurityType.Option
    long_sec.Quantity = 3

    short_sec = MagicMock()
    short_sec.Invested = True
    short_sec.Symbol.SecurityType = mock_imports.SecurityType.Option
    short_sec.Quantity = -2

    algo.Portfolio = MagicMock()
    algo.Portfolio.Values = [long_sec, short_sec]

    algo.SweepOrphanedOptionLegs()

    assert algo.MarketOrder.call_count == 2
    calls = [c[0] for c in algo.MarketOrder.call_args_list]
    # Long leg flattened with -3, short leg covered with +2
    assert (long_sec.Symbol, -3) in [(c[0], c[1]) for c in calls]
    assert (short_sec.Symbol, 2) in [(c[0], c[1]) for c in calls]

if __name__ == "__main__":
    print("Running EVC unit tests...")
    test_bs_price()
    print("test_bs_price passed.")
    test_vega()
    print("test_vega passed.")
    test_implied_volatility_newton()
    print("test_implied_volatility_newton passed.")
    test_match_option_contracts()
    print("test_match_option_contracts passed.")
    test_atomic_liquidation()
    print("test_atomic_liquidation passed.")
    test_margin_position_sizing()
    print("test_margin_position_sizing passed.")
    test_unclamped_exit_pnl()
    print("test_unclamped_exit_pnl passed.")
    test_orphan_sweeper_short_and_long()
    print("test_orphan_sweeper_short_and_long passed.")
    print("All EVC unit tests passed successfully!")

