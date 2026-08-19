"""
trade_logger.py
===============
Universal QuantConnect Trade Logging Decorators for BigQuery Ingestion.

This module provides reusable python decorators (@log_trade_entry and @log_trade_exit)
that standardize trade execution and liquidation logging across any algorithm in this repository.

Log Format:
    Each decorator automatically formats a JSON payload prefixed with '[BIGQUERY_TRADE_RECORD]'
    and passes it to QuantConnect's self.Log(...) method.

Usage Example:
    from PropietaryCode.decorators import log_trade_entry, log_trade_exit

    class MyOptionStrategy(QCAlgorithm):
        algo_code = "4EVC"

        @log_trade_entry
        def ExecuteCalendarSpread(self, underlying, front, back, qty, metrics, report_date):
            # ... execution logic ...
            pass

        @log_trade_exit
        def LiquidateSpread(self, underlying, tag: str):
            # ... liquidation logic ...
            pass
"""

from __future__ import annotations

import json
import functools
import datetime as dt
from typing import Any, Callable, Dict, Optional, Union, Tuple


def normalize_exit_reason(tag: str) -> str:
    """
    Parses a raw order tag string and maps it to a standardized exit category.

    Args:
        tag: Raw order tag string (e.g. 'Stop Loss Triggered (-12.50% loss)').

    Returns:
        One of: 'Stop Loss', 'Take Profit', 'Time Exit', 'DTE Safety', 'Signal Exit',
                'Risk Exit', 'Trailing Stop', 'Rebalance', 'Option Assignment',
                'Margin Call', 'Corporate Action', 'Other'.
    """
    if not tag:
        return "Other"

    tag_upper = tag.upper()
    if "ASSIGNMENT" in tag_upper or "ASSIGNED" in tag_upper or "EXERCISE" in tag_upper or "DELIVERED" in tag_upper:
        return "Option Assignment"
    elif "MARGIN CALL" in tag_upper or "FORCE LIQUIDAT" in tag_upper or "OVER-MARGIN" in tag_upper:
        return "Margin Call"
    elif "DELIST" in tag_upper or "SPLIT" in tag_upper or "MERGER" in tag_upper or "CORPORATE" in tag_upper:
        return "Corporate Action"
    elif "TRAILING" in tag_upper:
        return "Trailing Stop"
    elif "STOP" in tag_upper or "LOSS" in tag_upper:
        return "Stop Loss"
    elif "TAKE PROFIT" in tag_upper or "TAKEPROFIT" in tag_upper or "PROFIT" in tag_upper or "TARGET" in tag_upper:
        return "Take Profit"
    elif "TIME" in tag_upper or "EXPIRE" in tag_upper or "CRUSH" in tag_upper or "POST-EARNINGS" in tag_upper or "HOLDING" in tag_upper:
        return "Time Exit"
    elif "DTE" in tag_upper or "SAFETY" in tag_upper:
        return "DTE Safety"
    elif "SIGNAL" in tag_upper or "REVERSION" in tag_upper or "THRESHOLD" in tag_upper or "INDICATOR" in tag_upper:
        return "Signal Exit"
    elif "RISK" in tag_upper or "MARGIN" in tag_upper or "CAPITAL" in tag_upper:
        return "Risk Exit"
    elif "REBALANCE" in tag_upper or "ALLOCATION" in tag_upper:
        return "Rebalance"
    else:
        return "Other"


def _extract_symbol_str(val: Any) -> str:
    """Helper to convert a QC Symbol or string to ticker string."""
    if hasattr(val, "Value"):
        return str(val.Value)
    return str(val)


def _get_algo_meta(algorithm_instance: Any) -> Tuple[str, str]:
    """
    Extracts algo_code and backtest_run_id from a QCAlgorithm instance.
    Falls back to safe default strings if not explicitly defined.
    """
    algo_code = getattr(algorithm_instance, "algo_code", algorithm_instance.__class__.__name__)
    
    run_id = getattr(algorithm_instance, "backtest_run_id", None)
    if not run_id:
        current_time_str = algorithm_instance.Time.strftime("%Y%m%d_%H%M%S") if hasattr(algorithm_instance, "Time") else "00000000"
        run_id = f"{algo_code}_{current_time_str}"
        setattr(algorithm_instance, "backtest_run_id", run_id)
        
    return algo_code, run_id


def _extract_strike_price(symbol_obj: Any) -> Optional[float]:
    """Safely extracts StrikePrice only for Option/FutureOption/IndexOption SecurityTypes."""
    if not symbol_obj or not hasattr(symbol_obj, "ID"):
        return None
    try:
        sec_type_str = str(getattr(symbol_obj.ID, "SecurityType", "")).upper()
        if "OPTION" in sec_type_str:
            return float(symbol_obj.ID.StrikePrice)
    except Exception:
        pass
    return None


def _extract_expiry_date(symbol_obj: Any) -> Optional[str]:
    """Safely extracts expiration Date only for expiring SecurityTypes (Options/Futures)."""
    if not symbol_obj or not hasattr(symbol_obj, "ID"):
        return None
    try:
        sec_type_str = str(getattr(symbol_obj.ID, "SecurityType", "")).upper()
        if "OPTION" in sec_type_str or "FUTURE" in sec_type_str:
            return str(symbol_obj.ID.Date.date())
    except Exception:
        pass
    return None


def _buffer_trade_record(self_obj: Any, record: Dict[str, Any]) -> None:
    """Buffers trade record in memory for ObjectStore persistence."""
    if not hasattr(self_obj, "_universal_trade_buffer"):
        setattr(self_obj, "_universal_trade_buffer", [])
    buffer = getattr(self_obj, "_universal_trade_buffer")
    buffer.append(record)


def save_trade_buffer_to_object_store(self_obj: Any) -> None:
    """
    Saves accumulated trade records buffer into QuantConnect ObjectStore at algorithm completion (OnFrameworkEnd).
    Uses a deterministic key (BTOPTrades_{algo_code}_latest.json) to overwrite previous runs and prevent cloud storage accumulation.
    """
    if not hasattr(self_obj, "ObjectStore") or not hasattr(self_obj, "_universal_trade_buffer"):
        return
    buffer = getattr(self_obj, "_universal_trade_buffer", [])
    if not buffer:
        return
    try:
        algo_code, backtest_run_id = _get_algo_meta(self_obj)
        key = f"BTOPTrades_{algo_code}_latest.json"
        payload_str = json.dumps(buffer, indent=2)
        self_obj.ObjectStore.Save(key, payload_str)
        if hasattr(self_obj, "Log"):
            self_obj.Log(f"[OBJECTSTORE_SAVED] Saved {len(buffer)} trade records to key '{key}'.")
    except Exception as err:
        if hasattr(self_obj, "Error"):
            self_obj.Error(f"[universal_trade_logger] Failed to save trade buffer to ObjectStore: {err}")


def log_trade_entry(func: Callable) -> Callable:
    """
    Decorator for strategy entry methods (e.g. ExecuteCalendarSpread, OpenPosition).
    
    Executes the underlying entry method, then formats and logs a standardized
    OPEN record for BigQuery ingestion via self.Log('[BIGQUERY_TRADE_RECORD] ...')
    and buffers in memory for ObjectStore persistence.
    """
    @functools.wraps(func)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        # 1. Run original execution logic
        result = func(self, *args, **kwargs)

        try:
            algo_code, backtest_run_id = _get_algo_meta(self)
            
            underlying = args[0] if len(args) > 0 else kwargs.get("underlying", "UNKNOWN")
            underlying_str = _extract_symbol_str(underlying)
            
            front = args[1] if len(args) > 1 else kwargs.get("front")
            back = args[2] if len(args) > 2 else kwargs.get("back")
            qty = args[3] if len(args) > 3 else kwargs.get("qty", 1)
            metrics = args[4] if len(args) > 4 else kwargs.get("metrics", {})

            strike = _extract_strike_price(front)
            near_expiry = _extract_expiry_date(front)
            far_expiry = _extract_expiry_date(back)

            pk_counter = getattr(self, "_trade_record_counter", 0) + 1
            setattr(self, "_trade_record_counter", pk_counter)
            pk = f"{backtest_run_id}_{underlying_str}_{pk_counter}"

            if not hasattr(self, "_universal_active_positions"):
                self._universal_active_positions = {}
            
            entry_price = getattr(self, "last_entry_price", 0.0)
            self._universal_active_positions[underlying_str] = {
                "pk": pk,
                "entry_price": entry_price,
                "metrics": metrics if isinstance(metrics, dict) else {},
                "qty": qty,
                "strike": strike,
                "near_expiry": near_expiry,
                "far_expiry": far_expiry
            }

            timestamp_str = self.Time.strftime("%Y-%m-%dT%H:%M:%SZ") if hasattr(self, "Time") else dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            
            param_dict = {
                k: round(float(v), 5) if isinstance(v, (int, float)) else str(v)
                for k, v in (metrics if isinstance(metrics, dict) else {}).items()
            }

            record: Dict[str, Any] = {
                "pk": pk,
                "backtest_run_id": backtest_run_id,
                "algo_code": algo_code,
                "timestamp": timestamp_str,
                "underlying": underlying_str,
                "action": "OPEN",
                "qty": int(qty) if isinstance(qty, (int, float)) else 1,
                "strike": strike,
                "near_expiry": near_expiry,
                "far_expiry": far_expiry,
                "vol_ratio": round(float(metrics.get("vol_ratio", 0.0)), 5) if isinstance(metrics, dict) and "vol_ratio" in metrics else None,
                "slope": round(float(metrics.get("slope", 0.0)), 5) if isinstance(metrics, dict) and "slope" in metrics else None,
                "ivrv_ratio": round(float(metrics.get("ivrv_ratio", 0.0)), 5) if isinstance(metrics, dict) and "ivrv_ratio" in metrics else None,
                "entry_price": round(float(entry_price), 5),
                "exit_price": 0.0,
                "pnl": 0.0,
                "exit_reason": "",
                "parameters": json.dumps(param_dict, separators=(',', ':'))
            }

            # 1. Real-time stdout logging
            if hasattr(self, "Log"):
                self.Log(f"[BIGQUERY_TRADE_RECORD] {json.dumps(record, separators=(',', ':'))}")

            # 2. In-memory buffer for ObjectStore persistence
            _buffer_trade_record(self, record)

        except Exception as err:
            if hasattr(self, "Error"):
                self.Error(f"[universal_trade_logger] Error in @log_trade_entry: {err}")

        return result

    return wrapper


def log_trade_exit(func: Callable) -> Callable:
    """
    Decorator for strategy exit methods (e.g. LiquidateSpread, ExitPosition).
    
    Executes the underlying exit method, then formats and logs a standardized
    CLOSE record containing exit_reason and realized pnl for BigQuery ingestion,
    and buffers in memory for ObjectStore persistence.
    """
    @functools.wraps(func)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        underlying = args[0] if len(args) > 0 else kwargs.get("underlying", "UNKNOWN")
        underlying_str = _extract_symbol_str(underlying)
        raw_tag = args[1] if len(args) > 1 else kwargs.get("tag", "Exit")

        active_positions = getattr(self, "_universal_active_positions", {})
        pos_info = active_positions.get(underlying_str, {})
        
        pk = pos_info.get("pk", f"CLOSE_{underlying_str}_{getattr(self, '_trade_record_counter', 1)}")
        metrics = pos_info.get("metrics", {})

        # 1. Execute liquidation function
        result = func(self, *args, **kwargs)

        try:
            algo_code, backtest_run_id = _get_algo_meta(self)
            exit_reason = normalize_exit_reason(str(raw_tag))

            entry_price = float(pos_info.get("entry_price", getattr(self, "last_entry_price", 0.0)))
            exit_price = float(getattr(self, "last_exit_price", 0.0))
            pnl = float(getattr(self, "last_pnl", 0.0))

            timestamp_str = self.Time.strftime("%Y-%m-%dT%H:%M:%SZ") if hasattr(self, "Time") else dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

            param_dict = {
                k: round(float(v), 5) if isinstance(v, (int, float)) else str(v)
                for k, v in metrics.items()
            }

            record: Dict[str, Any] = {
                "pk": pk,
                "backtest_run_id": backtest_run_id,
                "algo_code": algo_code,
                "timestamp": timestamp_str,
                "underlying": underlying_str,
                "action": "CLOSE",
                "qty": int(pos_info.get("qty", 1)),
                "strike": pos_info.get("strike"),
                "near_expiry": pos_info.get("near_expiry"),
                "far_expiry": pos_info.get("far_expiry"),
                "vol_ratio": round(float(metrics.get("vol_ratio", 0.0)), 5) if "vol_ratio" in metrics else None,
                "slope": round(float(metrics.get("slope", 0.0)), 5) if "slope" in metrics else None,
                "ivrv_ratio": round(float(metrics.get("ivrv_ratio", 0.0)), 5) if "ivrv_ratio" in metrics else None,
                "entry_price": round(entry_price, 5),
                "exit_price": round(exit_price, 5),
                "pnl": round(pnl, 5),
                "exit_reason": exit_reason,
                "parameters": json.dumps(param_dict, separators=(',', ':'))
            }

            # 1. Real-time stdout logging
            if hasattr(self, "Log"):
                self.Log(f"[BIGQUERY_TRADE_RECORD] {json.dumps(record, separators=(',', ':'))}")

            # 2. In-memory buffer for ObjectStore persistence
            _buffer_trade_record(self, record)

            # Clean up active position tracking
            if underlying_str in active_positions:
                del active_positions[underlying_str]

        except Exception as err:
            if hasattr(self, "Error"):
                self.Error(f"[universal_trade_logger] Error in @log_trade_exit: {err}")

        return result

    return wrapper
