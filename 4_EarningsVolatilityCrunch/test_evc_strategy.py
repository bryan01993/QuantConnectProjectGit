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
mock_imports.Resolution = MagicMock()
mock_imports.SecurityType = MagicMock()
mock_imports.DataNormalizationMode = MagicMock()
mock_imports.BrokerageName = MagicMock()
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
    """Verify calendar matching logic pairs near and far contracts by strike."""
    algo = EarningsVolatilityCrunch()
    
    # Create mock symbols/contracts
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
    

    # Test pairing: c1 (near) and c2 (far) have matching strikes (150)
    contracts = [c1, c3, c2]
    pairs = algo.MatchOptionContracts(contracts)
    
    assert len(pairs) == 1
    assert pairs[0] == (c1, c2)

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
    print("All EVC unit tests passed successfully!")
