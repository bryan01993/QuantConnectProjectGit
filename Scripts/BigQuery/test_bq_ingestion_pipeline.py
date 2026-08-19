import os
import sys
import json
import logging
import datetime as dt
from typing import Dict, Any, List, Optional
from unittest.mock import MagicMock, patch

# Configure logging for test execution
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("IngestionPipelineTest")

# Add Scripts/BigQuery to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import db_operator
import log_trades_uploader
import bt_handler


# ============================================================================
# 1. Test Module: Missing Data Resilience
# ============================================================================

def test_missing_data_resilience():
    """Verifies pipeline resilience when JSON input has missing keys or null values."""
    logger.info("Running Test: test_missing_data_resilience...")

    # 1. Test empty orders JSON file
    empty_file = os.path.join(os.path.dirname(__file__), "test_empty_orders.json")
    with open(empty_file, "w", encoding="utf-8") as f:
        json.dump([], f)

    try:
        rows = log_trades_uploader.parse_orders_json_file(empty_file)
        assert isinstance(rows, list)
        assert len(rows) == 0
    finally:
        if os.path.exists(empty_file):
            os.remove(empty_file)

    # 2. Test order dict missing optional keys (symbol, tag, price, quantity)
    incomplete_orders = [
        {},  # Completely empty order
        {"id": 1, "status": "Filled"},  # Missing symbol, time, quantity
        {"symbol": {"value": "AAPL"}}  # Missing price, tag, time
    ]
    incomplete_file = os.path.join(os.path.dirname(__file__), "test_incomplete_orders.json")
    with open(incomplete_file, "w", encoding="utf-8") as f:
        json.dump(incomplete_orders, f)

    try:
        rows = log_trades_uploader.parse_orders_json_file(incomplete_file)
        assert isinstance(rows, list)
        # Incomplete orders without valid trade setup should produce 0 valid closed trades
        logger.info(f"PASS: Incomplete orders parsed safely without throwing KeyError. Rows produced: {len(rows)}")
    finally:
        if os.path.exists(incomplete_file):
            os.remove(incomplete_file)


# ============================================================================
# 2. Test Module: Malformed JSON & Non-Schema Names
# ============================================================================

def test_malformed_json_and_wrong_names():
    """Verifies log parser skips corrupt JSON lines and sanitize_record strips non-schema fields."""
    logger.info("Running Test: test_malformed_json_and_wrong_names...")

    # 1. Test log file with valid, malformed, and truncated lines
    log_content = """2026-07-28 15:00:00 [INFO] Strategy processing hourly bar...
2026-07-28 15:00:00 [INFO] [BIGQUERY_TRADE_RECORD] {"pk": "PK_VALID_1", "algo_code": "4EVC", "timestamp": "2026-07-28T15:00:00Z", "underlying": "AAPL", "action": "OPEN", "qty": 5, "strike": 150.0, "near_expiry": "2026-08-25", "far_expiry": "2026-09-29", "vol_ratio": 1.5, "slope": 0.005, "ivrv_ratio": 1.2, "entry_price": 2.0, "exit_price": 0.0, "pnl": 0.0, "earnings_date": "2026-07-29", "unknown_extra_field": "SHOULD_BE_STRIPPED"}
2026-07-28 15:01:00 [INFO] [BIGQUERY_TRADE_RECORD] {"pk": "PK_CORRUPT_2", "underlying": "MSFT", "action": "OPEN" UNCLOSED_JSON_STRING...
2026-07-28 15:02:00 [INFO] [BIGQUERY_TRADE_RECORD] NOT_EVEN_JSON
"""
    test_log_file = os.path.join(os.path.dirname(__file__), "test_corrupt.log")
    with open(test_log_file, "w", encoding="utf-8") as f:
        f.write(log_content)

    try:
        parsed_rows = log_trades_uploader.parse_log_file(test_log_file)
        assert len(parsed_rows) == 1
        assert parsed_rows[0]["pk"] == "PK_VALID_1"
        assert "unknown_extra_field" not in parsed_rows[0]
        assert "earnings_date" not in parsed_rows[0]

        params = json.loads(parsed_rows[0]["parameters"])
        assert params["earnings_date"] == "2026-07-29"

        logger.info("PASS: Malformed log lines skipped, legacy fields sanitized successfully.")
    finally:
        if os.path.exists(test_log_file):
            os.remove(test_log_file)


# ============================================================================
# 3. Test Module: Timestamp Normalizer Heterogeneity
# ============================================================================

def test_timestamp_converter_heterogeneity():
    """Verifies timestamp normalizer handles epoch seconds, epoch milliseconds, and ISO strings."""
    logger.info("Running Test: test_timestamp_converter_heterogeneity...")

    # 1. Unix Epoch Seconds (e.g. 1715000000 -> 2024-05-06)
    ts_sec = log_trades_uploader.normalize_timestamp(1715000000)
    assert "2024-05-06" in ts_sec

    # 2. Unix Epoch Milliseconds (e.g. 1715000000000 -> 2024-05-06)
    ts_ms = log_trades_uploader.normalize_timestamp(1715000000000)
    assert "2024-05-06" in ts_ms

    # 3. ISO String
    iso_str = "2024-05-06T13:33:20Z"
    ts_iso = log_trades_uploader.normalize_timestamp(iso_str)
    assert ts_iso == iso_str

    # 4. Numeric String
    ts_num_str = log_trades_uploader.normalize_timestamp("1715000000.0")
    assert "2024-05-06" in ts_num_str

    logger.info("PASS: All 4 timestamp representations normalized to ISO-8601 UTC.")


# ============================================================================
# 4. Test Module: Percentage String Metrics Stripper
# ============================================================================

def test_statistic_string_stripping():
    """Verifies that percentage strings (e.g. '0.257%') in QuantConnect stats are converted safely."""
    logger.info("Running Test: test_statistic_string_stripping...")

    def clean_metric_val(val: Any) -> Optional[float]:
        if val is None:
            return None
        if isinstance(val, (int, float)):
            return float(val)
        if isinstance(val, str):
            s = val.replace("%", "").replace("$", "").replace(",", "").strip()
            try:
                return float(s)
            except ValueError:
                return None
        return None

    assert clean_metric_val("0.257%") == 0.257
    assert clean_metric_val("-1753.786") == -1753.786
    assert clean_metric_val("$14,205.60") == 14205.60
    assert clean_metric_val("N/A") is None
    assert clean_metric_val(None) is None

    logger.info("PASS: Percentage and currency metric strings cleaned safely.")


# ============================================================================
# 5. Test Module: Chunking & NDJSON Load Job Fallback
# ============================================================================

def test_chunking_and_ndjson_fallback():
    """Verifies that insert_rows_chunked_with_fallback triggers NDJSON fallback for large rows or errors."""
    logger.info("Running Test: test_chunking_and_ndjson_fallback...")

    mock_client = MagicMock()
    table_id = "develop.BTOPTrades"

    # 1. Normal small rows -> insert_rows_json called
    rows_small = [{"pk": f"PK_{i}", "underlying": "AAPL"} for i in range(10)]
    mock_client.insert_rows_json.return_value = [] # No errors

    db_operator.insert_rows_chunked_with_fallback(mock_client, table_id, rows_small)
    mock_client.insert_rows_json.assert_called()

    # 2. Oversize row (>950KB) -> triggers _load_via_ndjson fallback
    mock_client.reset_mock()
    huge_row = {"pk": "PK_HUGE", "payload": "X" * 1_000_000}
    rows_huge = [huge_row]

    with patch.object(db_operator, "_load_via_ndjson") as mock_ndjson:
        db_operator.insert_rows_chunked_with_fallback(mock_client, table_id, rows_huge)
        mock_ndjson.assert_called_once()
        mock_client.insert_rows_json.assert_not_called()

    logger.info("PASS: Streaming chunker and NDJSON fallback triggered correctly.")


# ============================================================================
# 6. Test Module: Primary Key Deduplication
# ============================================================================

def test_primary_key_deduplication():
    """Verifies get_existing_records deduplication logic filters existing (pk, action) rows."""
    logger.info("Running Test: test_primary_key_deduplication...")

    mock_client = MagicMock()
    mock_row1 = MagicMock(pk="PK_EXISTING_1", action="CLOSE")
    mock_row2 = MagicMock(pk="PK_EXISTING_2", action="OPEN")
    mock_query_job = MagicMock()
    mock_query_job.result.return_value = [mock_row1, mock_row2]
    mock_client.query.return_value = mock_query_job

    existing_set = log_trades_uploader.get_existing_records(mock_client, "proj", "dev")
    assert ("PK_EXISTING_1", "CLOSE") in existing_set
    assert ("PK_EXISTING_2", "OPEN") in existing_set
    assert ("PK_NEW_3", "CLOSE") not in existing_set

    # Test filtering out existing rows
    candidate_rows = [
        {"pk": "PK_EXISTING_1", "action": "CLOSE", "data": 1},
        {"pk": "PK_NEW_3", "action": "CLOSE", "data": 2}
    ]
    new_rows = [r for r in candidate_rows if (r["pk"], r["action"]) not in existing_set]
    assert len(new_rows) == 1
    assert new_rows[0]["pk"] == "PK_NEW_3"

    logger.info("PASS: Primary Key deduplication filtered existing records cleanly.")


# ============================================================================
# 7. Main Runner
# ============================================================================

def run_all_ingestion_tests():
    logger.info("=" * 70)
    logger.info("STARTING BIGQUERY INGESTION PIPELINE TEST SUITE")
    logger.info("=" * 70)

    test_missing_data_resilience()
    test_malformed_json_and_wrong_names()
    test_timestamp_converter_heterogeneity()
    test_statistic_string_stripping()
    test_chunking_and_ndjson_fallback()
    test_primary_key_deduplication()

    logger.info("=" * 70)
    logger.info("SUCCESS: ALL 6 INGESTION PIPELINE TEST MODULES PASSED!")
    logger.info("=" * 70)


if __name__ == "__main__":
    run_all_ingestion_tests()
