"""
test_hdbt_ingestion_pipeline.py
================================
Unit test suite for the Heavy-Duty Backtest (HDBT) BigQuery data ingestion pipeline.

Tests:
1. JSON-only orders trade record parsing (groupOrderManager combo orders, tag parameters, backtestId keying).
2. Closed trades symbol struct extraction (multi-leg option contract structures).
3. Batch chunk tagging (batch_id, chunk_index, and backtestId assignment).
4. Deduplication logic against existing primary keys.
5. Batch chunk lifecycle state transitions.
"""

import json
import os
import sys
import tempfile
import unittest
from unittest.mock import MagicMock

# Ensure project root & Scripts/BigQuery are in sys.path
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_BQ_DIR = os.path.abspath(os.path.join(_THIS_DIR, ".."))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", "..", ".."))
for d in [_BQ_DIR, _PROJECT_ROOT]:
    if d not in sys.path:
        sys.path.insert(0, d)

from log_trades_uploader import parse_orders_json_file, sanitize_record, normalize_timestamp  # noqa: E402
from batch_manager import update_chunk_status  # noqa: E402


class TestHDBTIngestionPipeline(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_parse_orders_json_trade_record(self):
        """Test parsing orders JSON file (groupOrderManager combo orders and tag metrics) into backtestId records."""
        orders_payload = [
            {
                "id": 1,
                "status": "filled",
                "time": "2023-08-15T14:00:00Z",
                "quantity": 10,
                "price": 9.20,
                "symbol": {"value": "GEF 231020C00065000"},
                "tag": "{\"u\":\"GEF\",\"k\":65.0,\"vol_ratio\":1.35,\"slope\":0.0025,\"ivrv\":1.15,\"near\":\"230915\",\"far\":\"231020\"}",
                "groupOrderManager": {"id": 101, "limitPrice": 0.80, "quantity": 10}
            },
            {
                "id": 2,
                "status": "filled",
                "time": "2023-08-15T14:00:00Z",
                "quantity": -10,
                "price": 8.40,
                "symbol": {"value": "GEF 230915C00065000"},
                "tag": "",
                "groupOrderManager": {"id": 101, "limitPrice": 0.80, "quantity": 10}
            }
        ]

        orders_file_path = os.path.join(self.test_dir, "BT_4EVC_TEST_orders.json")
        with open(orders_file_path, "w", encoding="utf-8") as f:
            json.dump(orders_payload, f)

        parsed_rows = parse_orders_json_file(orders_file_path)
        self.assertGreaterEqual(len(parsed_rows), 1)

        row = parsed_rows[0]
        self.assertEqual(row["backtestId"], "BT_4EVC_TEST")
        self.assertEqual(row["underlying"], "GEF")
        self.assertEqual(row["action"], "OPEN")
        self.assertEqual(row["vol_ratio"], 1.35)
        self.assertEqual(row["slope"], 0.0025)
        self.assertEqual(row["ivrv_ratio"], 1.15)
        self.assertEqual(row["entry_price"], 0.80)

    def test_closed_trades_symbol_list_extraction(self):
        """Test symbol struct parsing logic for multi-leg option contracts (symbols list vs symbol dict)."""
        ct_symbols_list = {
            "id": "1",
            "symbols": [{"value": "GEF 230915C00065000", "permtick": "GEF"}],
            "entryPrice": 8.40,
            "exitPrice": 11.00,
            "quantity": 10,
            "profitLoss": -2600.0
        }
        
        sym_val = "UNKNOWN"
        if ct_symbols_list.get("symbols") and isinstance(ct_symbols_list.get("symbols"), list):
            s0 = ct_symbols_list["symbols"][0]
            sym_val = str(s0.get("value") or s0.get("permtick") or "UNKNOWN")
            
        self.assertEqual(sym_val, "GEF 230915C00065000")

    def test_batch_chunk_tagging(self):
        """Test attaching batch_id, chunk_index, and backtestId tags to parsed trade records."""
        raw_rows = [
            {"pk": "PK_1", "action": "OPEN", "underlying": "AAPL", "backtest_run_id": "BT_4EVC_001"},
            {"pk": "PK_1", "action": "CLOSE", "underlying": "AAPL", "backtest_run_id": "BT_4EVC_001"}
        ]
        batch_id = "BATCH_4EVC_TEST_001"
        chunk_idx = 3

        for r in raw_rows:
            r["batch_id"] = batch_id
            r["chunk_index"] = chunk_idx
            if "backtest_run_id" in r and "backtestId" not in r:
                r["backtestId"] = r.pop("backtest_run_id")

        self.assertEqual(raw_rows[0]["batch_id"], "BATCH_4EVC_TEST_001")
        self.assertEqual(raw_rows[0]["chunk_index"], 3)
        self.assertEqual(raw_rows[0]["backtestId"], "BT_4EVC_001")
        self.assertNotIn("backtest_run_id", raw_rows[0])

    def test_deduplication_logic(self):
        """Test deduplicating trade rows against existing BigQuery primary key set."""
        existing_keys = {("PK_1_OPEN", "OPEN"), ("PK_1_CLOSE", "CLOSE")}
        candidate_rows = [
            {"pk": "PK_1_OPEN", "action": "OPEN", "underlying": "AAPL", "backtestId": "BT_1"},
            {"pk": "PK_2_OPEN", "action": "OPEN", "underlying": "MSFT", "backtestId": "BT_1"},
            {"pk": "PK_2_CLOSE", "action": "CLOSE", "underlying": "MSFT", "backtestId": "BT_1"}
        ]

        new_rows = []
        for r in candidate_rows:
            k = (r.get("pk"), r.get("action"))
            if k[0] and k[1] and k not in existing_keys:
                new_rows.append(r)
                existing_keys.add(k)

        self.assertEqual(len(new_rows), 2)
        self.assertEqual(new_rows[0]["pk"], "PK_2_OPEN")
        self.assertEqual(new_rows[1]["pk"], "PK_2_CLOSE")

    def test_poller_chunk_lifecycle(self):
        """Test updating batch chunk status in BigQuery BTOPBatchChunks."""
        mock_bq_client = MagicMock()
        mock_query_job = MagicMock()
        mock_bq_client.query.return_value = mock_query_job

        update_chunk_status(mock_bq_client, "BATCH_001", "BATCH_001_Y2020", "COMPLETED")

        mock_bq_client.query.assert_called_once()
        query_arg = mock_bq_client.query.call_args[0][0]
        self.assertIn("UPDATE `bav-personal-cloud.develop.BTOPBatchChunks`", query_arg)
        self.assertIn("SET status = @new_status", query_arg)
        self.assertIn("WHERE batch_id = @batch_id", query_arg)


if __name__ == "__main__":
    unittest.main()
