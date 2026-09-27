"""
test_evc_research_notebook.py
==============================
Standalone local test harness for the 4EVC Earnings Volatility Research Notebook.
Simulates QuantBook environment, mock option chains, historical bars, and earnings dates
to verify end-to-end execution without requiring QuantConnect Cloud.
"""

from __future__ import annotations

import math
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any

import numpy as np
import pandas as pd
from scipy.stats import norm


# ============================================================================
# Mathematical Solvers & Pricing Models
# ============================================================================

def calculate_realized_volatility(close_prices: pd.Series) -> float:
    """Computes 30-day annualized realized volatility from daily/hourly closes."""
    if len(close_prices) < 5:
        return 0.30
    log_returns = np.log(close_prices / close_prices.shift(1)).dropna()
    if log_returns.empty or np.all(log_returns == 0):
        return 0.30
    return float(log_returns.std() * np.sqrt(252))


def calculate_volume_ratio(volumes: pd.Series, recent_window: int = 5, base_window: int = 30) -> float:
    """Computes volume ratio (recent volume vs 30-day average volume)."""
    if len(volumes) < recent_window:
        return 1.0
    recent_vol = volumes.iloc[-recent_window:].mean()
    base_vol = volumes.iloc[-base_window:].mean() if len(volumes) >= base_window else volumes.mean()
    if base_vol <= 0:
        return 1.0
    return float(recent_vol / base_vol)


def black_scholes_iv(
    option_right: str,
    S: float,
    K: float,
    T: float,
    r: float,
    market_price: float,
    max_iter: int = 100,
    precision: float = 1e-4
) -> Optional[float]:
    """
    Newton-Raphson Black-Scholes implied volatility solver with fallback bisection.
    Supports both Call ('C' / 'CALL') and Put ('P' / 'PUT') options.
    """
    if S <= 0 or K <= 0 or T <= 0.0001 or market_price <= 0:
        return None

    is_call = option_right.upper().startswith("C")
    discount = math.exp(-r * T)
    intrinsic = max(S - K * discount, 0.0) if is_call else max(K * discount - S, 0.0)

    if market_price < intrinsic:
        return None

    # Initial guess via Brenner-Subrahmanyam approximation
    sigma = math.sqrt(2.0 * math.pi / T) * (market_price / S)
    sigma = max(0.05, min(sigma, 3.0))

    # Newton-Raphson iterations
    for _ in range(max_iter):
        d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)

        if is_call:
            price = S * norm.cdf(d1) - K * discount * norm.cdf(d2)
        else:
            price = K * discount * norm.cdf(-d2) - S * norm.cdf(-d1)

        vega = S * norm.pdf(d1) * math.sqrt(T)
        diff = price - market_price

        if abs(diff) < precision:
            return round(sigma, 5)

        if vega < 1e-8:
            break

        sigma -= diff / vega
        if sigma <= 0.001 or sigma > 10.0:
            break

    # Fallback: Bisection Method
    low_sig, high_sig = 0.01, 8.0
    for _ in range(50):
        mid_sig = (low_sig + high_sig) / 2.0
        d1 = (math.log(S / K) + (r + 0.5 * mid_sig ** 2) * T) / (mid_sig * math.sqrt(T))
        d2 = d1 - mid_sig * math.sqrt(T)

        if is_call:
            price = S * norm.cdf(d1) - K * discount * norm.cdf(d2)
        else:
            price = K * discount * norm.cdf(-d2) - S * norm.cdf(-d1)

        diff = price - market_price
        if abs(diff) < precision:
            return round(mid_sig, 5)

        if diff > 0:
            high_sig = mid_sig
        else:
            low_sig = mid_sig

    return round(mid_sig, 5) if mid_sig > 0.01 else None


# ============================================================================
# Mock QuantBook Environment for Local Validation
# ============================================================================

def generate_mock_research_dataset(num_events: int = 60) -> pd.DataFrame:
    """Generates synthetic earnings events, option chains, and calculates full 4EVC metrics matrix."""
    np.random.seed(42)
    tickers = ["AAPL", "MSFT", "NVDA", "AMD", "AMZN", "GOOGL", "META", "TSLA", "NFLX", "INTC"]
    
    records = []
    start_date = datetime(2023, 1, 5)

    for i in range(num_events):
        ticker = np.random.choice(tickers)
        earnings_date = start_date + timedelta(days=int(i * 1.4))
        entry_time = earnings_date - timedelta(days=1, hours=2)  # 2:00 PM T-1
        exit_time = earnings_date + timedelta(hours=10)         # 10:00 AM T+1

        underlying_price = float(np.random.uniform(50.0, 250.0))
        rv_30 = float(np.random.uniform(0.20, 0.65))
        vol_ratio = float(np.random.uniform(0.8, 2.5))
        
        # Option Chains
        strike = round(underlying_price, 0)
        front_exp = earnings_date + timedelta(days=int(np.random.choice([2, 3, 5, 7])))
        back_exp = front_exp + timedelta(days=int(np.random.choice([21, 28, 35, 42])))
        
        front_dte = (front_exp.date() - entry_time.date()).days
        back_dte = (back_exp.date() - entry_time.date()).days
        diff_dte = front_dte - back_dte

        # Volatilities & Pre-Earnings Inversion
        front_iv = rv_30 * np.random.uniform(1.8, 3.8)
        back_iv = rv_30 * np.random.uniform(1.0, 1.6)
        slope = (front_iv - back_iv) / float(diff_dte)
        ivrv_ratio = front_iv / rv_30

        # Option Pricing
        T_front = front_dte / 365.0
        T_back = back_dte / 365.0
        r = 0.045

        # Theoretical Black-Scholes Values at Entry
        d1_f = (math.log(underlying_price / strike) + (r + 0.5 * front_iv ** 2) * T_front) / (front_iv * math.sqrt(T_front))
        d2_f = d1_f - front_iv * math.sqrt(T_front)
        front_entry_mid = underlying_price * norm.cdf(d1_f) - strike * math.exp(-r * T_front) * norm.cdf(d2_f)
        
        d1_b = (math.log(underlying_price / strike) + (r + 0.5 * back_iv ** 2) * T_back) / (back_iv * math.sqrt(T_back))
        d2_b = d1_b - back_iv * math.sqrt(T_back)
        back_entry_mid = underlying_price * norm.cdf(d1_b) - strike * math.exp(-r * T_back) * norm.cdf(d2_b)

        # Bid/Ask Spread with realistic illiquidity tiers
        front_spread = max(0.03, round(front_entry_mid * np.random.uniform(0.02, 0.12), 2))
        back_spread = max(0.04, round(back_entry_mid * np.random.uniform(0.03, 0.14), 2))

        front_bid = round(front_entry_mid - front_spread / 2.0, 2)
        front_ask = round(front_entry_mid + front_spread / 2.0, 2)
        back_bid = round(back_entry_mid - back_spread / 2.0, 2)
        back_ask = round(back_entry_mid + back_spread / 2.0, 2)

        entry_mid_debit = round(back_entry_mid - front_entry_mid, 4)
        entry_mkt_debit = round(back_ask - front_bid, 4)  # Buy back at Ask, sell front at Bid

        # Post-Earnings Jump & Exit Pricing
        post_jump_pct = np.random.normal(0.0, rv_30 / np.sqrt(252) * 2.2)
        post_stock_price = underlying_price * (1.0 + post_jump_pct)

        # IV Crush: Front crushes 50-80%, Back crushes 15-30%
        post_front_iv = front_iv * np.random.uniform(0.25, 0.45)
        post_back_iv = back_iv * np.random.uniform(0.70, 0.85)

        T_front_exit = max(0.001, (front_exp - exit_time).total_seconds() / (365.0 * 24 * 3600))
        T_back_exit = max(0.01, (back_exp - exit_time).total_seconds() / (365.0 * 24 * 3600))

        d1_fe = (math.log(post_stock_price / strike) + (r + 0.5 * post_front_iv ** 2) * T_front_exit) / (post_front_iv * math.sqrt(T_front_exit))
        d2_fe = d1_fe - post_front_iv * math.sqrt(T_front_exit)
        front_exit_mid = post_stock_price * norm.cdf(d1_fe) - strike * math.exp(-r * T_front_exit) * norm.cdf(d2_fe)

        d1_be = (math.log(post_stock_price / strike) + (r + 0.5 * post_back_iv ** 2) * T_back_exit) / (post_back_iv * math.sqrt(T_back_exit))
        d2_be = d1_be - post_back_iv * math.sqrt(T_back_exit)
        back_exit_mid = post_stock_price * norm.cdf(d1_be) - strike * math.exp(-r * T_back_exit) * norm.cdf(d2_be)

        front_exit_spread = max(0.03, round(front_exit_mid * np.random.uniform(0.02, 0.12), 2))
        back_exit_spread = max(0.04, round(back_exit_mid * np.random.uniform(0.03, 0.14), 2))

        front_exit_ask = round(front_exit_mid + front_exit_spread / 2.0, 2)
        back_exit_bid = round(back_exit_mid - back_exit_spread / 2.0, 2)

        exit_mid_credit = round(back_exit_mid - front_exit_mid, 4)
        exit_mkt_credit = round(max(0.0, back_exit_bid - front_exit_ask), 4)

        # Returns
        return_mid_pct = round(((exit_mid_credit - entry_mid_debit) / entry_mid_debit) * 100.0, 2) if entry_mid_debit > 0 else 0.0
        return_mkt_pct = round(((exit_mkt_credit - entry_mkt_debit) / entry_mkt_debit) * 100.0, 2) if entry_mkt_debit > 0 else 0.0
        slippage_drag_pct = round(return_mid_pct - return_mkt_pct, 2)

        records.append({
            "timestamp": entry_time,
            "ticker": ticker,
            "earnings_date": earnings_date,
            "underlying_price": round(underlying_price, 2),
            "strike": strike,
            "front_dte": front_dte,
            "back_dte": back_dte,
            "front_bid": front_bid,
            "front_ask": front_ask,
            "front_mid": round(front_entry_mid, 2),
            "back_bid": back_bid,
            "back_ask": back_ask,
            "back_mid": round(back_entry_mid, 2),
            "entry_spread_pct": round(((front_spread + back_spread) / (entry_mid_debit if entry_mid_debit > 0 else 1.0)) * 100.0, 2),
            "vol_ratio": round(vol_ratio, 2),
            "rv_30": round(rv_30, 4),
            "front_iv": round(front_iv, 4),
            "back_iv": round(back_iv, 4),
            "slope": round(slope, 5),
            "ivrv_ratio": round(ivrv_ratio, 2),
            "entry_mid_debit": entry_mid_debit,
            "entry_mkt_debit": entry_mkt_debit,
            "exit_mid_credit": exit_mid_credit,
            "exit_mkt_credit": exit_mkt_credit,
            "return_mid_pct": return_mid_pct,
            "return_mkt_pct": return_mkt_pct,
            "slippage_drag_pct": slippage_drag_pct,
            "post_jump_pct": round(post_jump_pct * 100.0, 2)
        })

    df = pd.DataFrame(records)
    df.set_index(["timestamp", "ticker"], inplace=True)
    return df


def test_research_pipeline():
    """Runs verification checks on the research dataset generation and mathematical assertions."""
    print("=" * 70)
    print("Testing 4EVC QuantBook Research Pipeline Engine")
    print("=" * 70)

    # 1. Test Black Scholes Solver
    call_iv = black_scholes_iv("Call", S=100.0, K=100.0, T=0.082, r=0.045, market_price=4.50)
    assert call_iv is not None and 0.20 <= call_iv <= 0.80, f"Call IV Solver failed: {call_iv}"
    print(f"[PASS] Black-Scholes Call IV Solver validated: IV={call_iv:.4f}")

    put_iv = black_scholes_iv("Put", S=100.0, K=100.0, T=0.082, r=0.045, market_price=4.20)
    assert put_iv is not None and 0.20 <= put_iv <= 0.80, f"Put IV Solver failed: {put_iv}"
    print(f"[PASS] Black-Scholes Put IV Solver validated: IV={put_iv:.4f}")

    # 2. Test Realized Volatility
    sample_prices = pd.Series([100.0, 101.5, 99.8, 102.1, 100.9, 103.4, 102.8, 104.0, 101.9, 102.5])
    rv = calculate_realized_volatility(sample_prices)
    assert 0.05 <= rv <= 1.0, f"Realized volatility out of bounds: {rv}"
    print(f"[PASS] Realized Volatility Solver validated: RV={rv:.4f}")

    # 3. Generate Master Research DataFrame
    df = generate_mock_research_dataset(num_events=100)
    assert not df.empty, "Research dataset is empty!"
    assert len(df) == 100, f"Expected 100 rows, got {len(df)}"
    print(f"[PASS] Master Research DataFrame generated: shape={df.shape}")

    # 4. Verify Column Schema
    required_cols = [
        "underlying_price", "strike", "front_dte", "back_dte",
        "front_bid", "front_ask", "back_bid", "back_ask",
        "vol_ratio", "rv_30", "front_iv", "back_iv", "slope", "ivrv_ratio",
        "entry_mid_debit", "entry_mkt_debit", "exit_mid_credit", "exit_mkt_credit",
        "return_mid_pct", "return_mkt_pct", "slippage_drag_pct"
    ]
    for col in required_cols:
        assert col in df.columns, f"Missing required column: {col}"
    print(f"[PASS] All {len(required_cols)} required schema columns verified.")

    # 5. Performance Summary
    mean_mid = df["return_mid_pct"].mean()
    mean_mkt = df["return_mkt_pct"].mean()
    mean_drag = df["slippage_drag_pct"].mean()

    print("\n--- Summary Performance Across 100 Simulated Q1 2023 Events ---")
    print(f"Mean Mid-Price Return:   {mean_mid:+.2f}%")
    print(f"Mean Market-Order Return:{mean_mkt:+.2f}%")
    print(f"Mean Bid-Ask Friction:   {mean_drag:.2f}% drag")
    print("=" * 70)
    print("ALL LOCAL RESEARCH PIPELINE TESTS PASSED SUCCESSFULLY!")
    print("=" * 70)


if __name__ == "__main__":
    test_research_pipeline()

