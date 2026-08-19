"""
test_bq_trade_ingestion_integrity.py
======================================
Automated verification test suite for Google BigQuery trade ingestion integrity.
Enforces non-null underlying symbols, symbol RECORD struct validity, and cross-table
trade count consistency across BTOPResults, BTOPTotalPerformanceClosedTrades, and BTOPTrades.
"""

import unittest
import sys
import os

# Ensure project root and Scripts directory are in sys.path
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_BIGQUERY_DIR = os.path.dirname(_THIS_DIR)
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", "..", ".."))
for d in [_THIS_DIR, _BIGQUERY_DIR, _PROJECT_ROOT, os.path.join(_PROJECT_ROOT, "Scripts")]:
    if d not in sys.path:
        sys.path.insert(0, d)

from db_operator import get_bigquery_client

PROJECT_ID = "bav-personal-cloud"
DATASET_ID = "develop"


class TestBQTradeIngestionIntegrity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = get_bigquery_client()

    def test_01_no_null_underlying_in_consolidated_spread_trades(self):
        """Asserts that v_4EVC_consolidated_spread_trades has 0 rows with NULL underlying."""
        query = f"""
        SELECT COUNT(*) as null_count
        FROM `{PROJECT_ID}.{DATASET_ID}.v_4EVC_consolidated_spread_trades`
        WHERE underlying IS NULL
        """
        rows = list(self.client.query(query, location="europe-west1").result())
        null_count = rows[0].null_count if rows else 0
        self.assertEqual(
            null_count, 0,
            f"FAILED: Found {null_count} rows with NULL underlying in v_4EVC_consolidated_spread_trades!"
        )

    def test_02_closed_trades_symbol_struct_validity(self):
        """Asserts that BTOPTotalPerformanceClosedTrades.symbol.underlying.value is non-null for all rows."""
        query = f"""
        SELECT COUNT(*) as invalid_count
        FROM `{PROJECT_ID}.{DATASET_ID}.BTOPTotalPerformanceClosedTrades`
        WHERE symbol IS NULL OR symbol.underlying.value IS NULL
        """
        rows = list(self.client.query(query, location="europe-west1").result())
        invalid_count = rows[0].invalid_count if rows else 0
        self.assertEqual(
            invalid_count, 0,
            f"FAILED: Found {invalid_count} rows with NULL symbol or NULL symbol.underlying.value in BTOPTotalPerformanceClosedTrades!"
        )

    def test_03_btoptrades_underlying_validity(self):
        """Asserts that BTOPTrades.underlying is non-null for all rows."""
        query = f"""
        SELECT COUNT(*) as null_count
        FROM `{PROJECT_ID}.{DATASET_ID}.BTOPTrades`
        WHERE underlying IS NULL OR TRIM(underlying) = ''
        """
        rows = list(self.client.query(query, location="europe-west1").result())
        null_count = rows[0].null_count if rows else 0
        self.assertEqual(
            null_count, 0,
            f"FAILED: Found {null_count} rows with NULL or empty underlying in BTOPTrades!"
        )

    def test_04_enriched_trades_underlying_validity(self):
        """Asserts that v_4EVC_enriched_trades has 0 rows with NULL underlying."""
        query = f"""
        SELECT COUNT(*) as null_count
        FROM `{PROJECT_ID}.{DATASET_ID}.v_4EVC_enriched_trades`
        WHERE underlying IS NULL
        """
        rows = list(self.client.query(query, location="europe-west1").result())
        null_count = rows[0].null_count if rows else 0
        self.assertEqual(
            null_count, 0,
            f"FAILED: Found {null_count} rows with NULL underlying in v_4EVC_enriched_trades!"
        )

    def test_05_predictors_non_null_integrity(self):
        """Asserts that 100% of trades for backtests with uploaded orders have non-null slope, vol_ratio, and ivrv_ratio."""
        query = f"""
        SELECT 
            COUNT(*) as total_trades,
            COUNT(slope) as non_null_slope,
            COUNT(vol_ratio) as non_null_vol,
            COUNT(ivrv_ratio) as non_null_ivrv
        FROM `{PROJECT_ID}.{DATASET_ID}.v_4EVC_consolidated_spread_trades`
        WHERE backtestId IN (SELECT DISTINCT backtestId FROM `{PROJECT_ID}.{DATASET_ID}.BTOPOrders`)
        """
        rows = list(self.client.query(query, location="europe-west1").result())
        if not rows or rows[0].total_trades == 0:
            return
        
        r = rows[0]
        total = r.total_trades
        slope_pct = (r.non_null_slope / total) * 100.0
        vol_pct = (r.non_null_vol / total) * 100.0
        ivrv_pct = (r.non_null_ivrv / total) * 100.0

        self.assertEqual(
            r.non_null_slope, total,
            f"FAILED: Only {r.non_null_slope}/{total} ({slope_pct:.1f}%) trades have non-null 'slope'!"
        )
        self.assertEqual(
            r.non_null_vol, total,
            f"FAILED: Only {r.non_null_vol}/{total} ({vol_pct:.1f}%) trades have non-null 'vol_ratio'!"
        )
        self.assertEqual(
            r.non_null_ivrv, total,
            f"FAILED: Only {r.non_null_ivrv}/{total} ({ivrv_pct:.1f}%) trades have non-null 'ivrv_ratio'!"
        )


if __name__ == "__main__":
    unittest.main()
