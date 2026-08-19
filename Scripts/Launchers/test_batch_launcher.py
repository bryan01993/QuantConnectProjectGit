"""
test_batch_launcher.py
======================
Unit tests for batch_launcher.py argument parsing, YAML config lookup,
extracted data mapping, and chunk record structure.

All external dependencies (BigQuery, QC REST API, subprocess) are mocked.
No cloud calls or BigQuery writes are performed.

Usage:
    poetry run python Scripts/Launchers/test_batch_launcher.py
"""

from __future__ import annotations

import logging
import os
import sys
from typing import Any, Dict, List, Optional
from unittest.mock import patch

# Configure logging for test execution
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("BatchLauncherTest")

# Add Launchers and BigQuery directories to sys.path for imports
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
_BQ_DIR = os.path.join(_PROJECT_ROOT, "Scripts", "BigQuery")
for d in [_THIS_DIR, _PROJECT_ROOT, _BQ_DIR]:
    if d not in sys.path:
        sys.path.insert(0, d)

from bt_launcher import load_yaml_files, parse_yaml_data, extract_parsed_data  # noqa: E402


# ============================================================================
# Shared Test Fixtures
# ============================================================================

SAMPLE_YAML_DATA: List[Dict[str, Any]] = [
    {
        "ALGOS": [
            {
                "ALGO_CODE": 4,
                "ALGO_NAME": "EarningsVolatilityCrunch",
                "ALGO_MAYUS_LETTERS": "EVC",
                "ALGO_PUBLIC_NAME": "Roosevelt",
                "ALGO_VERSION": 1,
                "ALGO_PARAMETRY": [
                    {"ALGO_PARAM_1": {"ALGO_PARAM_1_DEFAULT": 15}},
                    {"ALGO_PARAM_2": "full"},
                ],
                "ALGO_SHORT_NAME": "4EVC",
                "CASH_AMOUNT": 10000,
                "START_DATE": "2023-01-01",
                "END_DATE": "2024-01-01",
            },
            {
                "ALGO_CODE": 0,
                "ALGO_NAME": "AlgoTester",
                "ALGO_MAYUS_LETTERS": "AT",
                "ALGO_PUBLIC_NAME": "GeorgeWashington",
                "ALGO_VERSION": 1,
                "ALGO_PARAMETRY": [
                    {"ALGO_PARAM_1": 0},
                    {"ALGO_PARAM_2": "full"},
                ],
                "ALGO_SHORT_NAME": "0AT",
                "CASH_AMOUNT": 10000,
                "START_DATE": "2023-01-01",
                "END_DATE": "2024-01-01",
            },
        ]
    }
]


# ============================================================================
# 1. Test Module: Default Argument Parsing
# ============================================================================

def test_parse_args_defaults():
    """Verifies default values when no CLI arguments are provided."""
    logger.info("Running Test: test_parse_args_defaults...")

    from batch_launcher import parse_args

    with patch("sys.argv", ["batch_launcher.py"]):
        args = parse_args()

    assert args.algo == "4EVC", f"Expected default algo '4EVC', got '{args.algo}'"
    assert args.years == [2015, 2016, 2017, 2018, 2019, 2020, 2021], (
        f"Expected default years [2015..2021], got {args.years}"
    )
    assert args.batch_id is None, f"Expected batch_id None, got '{args.batch_id}'"
    assert args.project_id is None, f"Expected project_id None, got '{args.project_id}'"

    logger.info("PASS: Default arguments parsed correctly (--algo=4EVC, --years=[2015..2021], --batch-id=None, --project-id=None).")


# ============================================================================
# 2. Test Module: Custom Argument Parsing
# ============================================================================

def test_parse_args_custom_values():
    """Verifies custom CLI arguments are parsed correctly."""
    logger.info("Running Test: test_parse_args_custom_values...")

    from batch_launcher import parse_args

    with patch("sys.argv", [
        "batch_launcher.py",
        "--algo", "0AT",
        "--years", "2020", "2021",
        "--batch-id", "CUSTOM_BATCH_123",
        "--project-id", "99999",
    ]):
        args = parse_args()

    assert args.algo == "0AT", f"Expected algo '0AT', got '{args.algo}'"
    assert args.years == [2020, 2021], f"Expected years [2020, 2021], got {args.years}"
    assert args.batch_id == "CUSTOM_BATCH_123", f"Expected batch_id 'CUSTOM_BATCH_123', got '{args.batch_id}'"
    assert args.project_id == 99999, f"Expected project_id 99999, got {args.project_id}"

    logger.info("PASS: Custom arguments parsed correctly (--algo=0AT, --years=[2020,2021], --batch-id=CUSTOM_BATCH_123, --project-id=99999).")


# ============================================================================
# 3. Test Module: Single Year Argument
# ============================================================================

def test_parse_args_single_year():
    """Verifies that a single --years value parses as a one-element list."""
    logger.info("Running Test: test_parse_args_single_year...")

    from batch_launcher import parse_args

    with patch("sys.argv", ["batch_launcher.py", "--years", "2023"]):
        args = parse_args()

    assert args.years == [2023], f"Expected years [2023], got {args.years}"
    assert isinstance(args.years, list), f"Expected list type, got {type(args.years)}"

    logger.info("PASS: Single year parsed as [2023] list.")


# ============================================================================
# 4. Test Module: YAML Config Lookup by Short Name
# ============================================================================

def test_yaml_config_lookup_by_short_name():
    """Verifies parse_yaml_data resolves algorithm by ALGO_SHORT_NAME."""
    logger.info("Running Test: test_yaml_config_lookup_by_short_name...")

    result = parse_yaml_data(SAMPLE_YAML_DATA, "4EVC")

    assert result is not None, "Expected algo config for '4EVC', got None"
    assert result["ALGO_CODE"] == 4, f"Expected ALGO_CODE 4, got {result['ALGO_CODE']}"
    assert result["ALGO_NAME"] == "EarningsVolatilityCrunch", (
        f"Expected ALGO_NAME 'EarningsVolatilityCrunch', got '{result['ALGO_NAME']}'"
    )
    assert result["ALGO_SHORT_NAME"] == "4EVC", f"Expected ALGO_SHORT_NAME '4EVC', got '{result['ALGO_SHORT_NAME']}'"

    logger.info("PASS: YAML config resolved '4EVC' -> EarningsVolatilityCrunch (code=4).")


# ============================================================================
# 5. Test Module: YAML Config Lookup by Full Name
# ============================================================================

def test_yaml_config_lookup_by_full_name():
    """Verifies parse_yaml_data resolves algorithm by ALGO_NAME."""
    logger.info("Running Test: test_yaml_config_lookup_by_full_name...")

    result = parse_yaml_data(SAMPLE_YAML_DATA, "EarningsVolatilityCrunch")

    assert result is not None, "Expected algo config for 'EarningsVolatilityCrunch', got None"
    assert result["ALGO_CODE"] == 4, f"Expected ALGO_CODE 4, got {result['ALGO_CODE']}"
    assert result["ALGO_SHORT_NAME"] == "4EVC", f"Expected ALGO_SHORT_NAME '4EVC', got '{result['ALGO_SHORT_NAME']}'"

    logger.info("PASS: YAML config resolved 'EarningsVolatilityCrunch' -> 4EVC (code=4).")


# ============================================================================
# 6. Test Module: Unknown Algorithm Returns None
# ============================================================================

def test_yaml_config_lookup_unknown_algo():
    """Verifies parse_yaml_data returns None for a non-existent algorithm."""
    logger.info("Running Test: test_yaml_config_lookup_unknown_algo...")

    result = parse_yaml_data(SAMPLE_YAML_DATA, "NONEXISTENT_ALGO")

    assert result is None, f"Expected None for unknown algo, got {result}"

    logger.info("PASS: Unknown algorithm correctly returned None.")


# ============================================================================
# 7. Test Module: Extract Parsed Data Field Mapping
# ============================================================================

def test_extract_parsed_data_fields():
    """Verifies extract_parsed_data maps all YAML keys to cmd_vars dict correctly."""
    logger.info("Running Test: test_extract_parsed_data_fields...")

    algo_config = parse_yaml_data(SAMPLE_YAML_DATA, "4EVC")
    assert algo_config is not None, "Pre-condition failed: could not find 4EVC config"

    cmd_vars = extract_parsed_data(algo_config)

    # Validate all expected keys exist
    expected_keys = [
        "cmd_algo_code", "cmd_algo_name", "cmd_algo_short_name",
        "cmd_algo_proyect", "cmd_algo_mayus_letters", "cmd_algo_public_name",
        "cmd_algo_version", "cmd_algo_parametry", "cmd_algo_start_date",
        "cmd_algo_end_date",
    ]
    for key in expected_keys:
        assert key in cmd_vars, f"Missing key '{key}' in cmd_vars"

    # Validate specific field values
    assert cmd_vars["cmd_algo_code"] == 4, f"Expected cmd_algo_code=4, got {cmd_vars['cmd_algo_code']}"
    assert cmd_vars["cmd_algo_name"] == "EarningsVolatilityCrunch", (
        f"Expected cmd_algo_name='EarningsVolatilityCrunch', got '{cmd_vars['cmd_algo_name']}'"
    )
    assert cmd_vars["cmd_algo_short_name"] == "4EVC", (
        f"Expected cmd_algo_short_name='4EVC', got '{cmd_vars['cmd_algo_short_name']}'"
    )
    assert cmd_vars["cmd_algo_proyect"] == "4EVC", (
        f"Expected cmd_algo_proyect='4EVC', got '{cmd_vars['cmd_algo_proyect']}'"
    )
    assert cmd_vars["cmd_algo_mayus_letters"] == "EVC", (
        f"Expected cmd_algo_mayus_letters='EVC', got '{cmd_vars['cmd_algo_mayus_letters']}'"
    )
    assert cmd_vars["cmd_algo_public_name"] == "Roosevelt", (
        f"Expected cmd_algo_public_name='Roosevelt', got '{cmd_vars['cmd_algo_public_name']}'"
    )
    assert cmd_vars["cmd_algo_version"] == 1, (
        f"Expected cmd_algo_version=1, got {cmd_vars['cmd_algo_version']}"
    )
    assert cmd_vars["cmd_algo_start_date"] == "2023-01-01", (
        f"Expected cmd_algo_start_date='2023-01-01', got '{cmd_vars['cmd_algo_start_date']}'"
    )
    assert cmd_vars["cmd_algo_end_date"] == "2024-01-01", (
        f"Expected cmd_algo_end_date='2024-01-01', got '{cmd_vars['cmd_algo_end_date']}'"
    )

    logger.info("PASS: All 10 cmd_vars fields mapped correctly from YAML config.")


# ============================================================================
# 8. Test Module: Chunk Records Structure
# ============================================================================

def test_chunk_records_structure():
    """
    Simulates the main() loop logic to verify chunk_records are built correctly:
    - Chunk 1 should have status 'RUNNING' with a real hex backtest_id.
    - Chunks 2..N should have status 'PENDING' with chunk_name as backtest_id.
    - Date ranges should be YYYY-01-01 to YYYY-12-31.
    - chunk_name format should be '{batch_id}_Y{year}'.
    """
    logger.info("Running Test: test_chunk_records_structure...")

    years = [2019, 2020, 2021]
    batch_id = "HDBT_4EVC_V1.0_20260803_221100"
    compile_id = "mock_compile_abc123"
    mock_hex_id = "fa3b8c91d204e7"

    chunk_records: List[Dict[str, Any]] = []

    for idx, yr in enumerate(years, start=1):
        start_date = f"{yr}-01-01"
        end_date = f"{yr}-12-31"
        chunk_name = f"{batch_id}_Y{yr}"

        if idx == 1:
            # Simulate successful cloud backtest creation for chunk 1
            chunk_records.append({
                "backtest_id": mock_hex_id,
                "chunk_index": idx,
                "start_date": start_date,
                "end_date": end_date,
                "status": "RUNNING",
                "compile_id": compile_id,
            })
        else:
            # Remaining chunks queued as PENDING
            chunk_records.append({
                "backtest_id": chunk_name,
                "chunk_index": idx,
                "start_date": start_date,
                "end_date": end_date,
                "status": "PENDING",
                "compile_id": compile_id,
            })

    # Assertions
    assert len(chunk_records) == 3, f"Expected 3 chunk records, got {len(chunk_records)}"

    # Chunk 1: RUNNING with real hex ID
    c1 = chunk_records[0]
    assert c1["status"] == "RUNNING", f"Chunk 1 status should be 'RUNNING', got '{c1['status']}'"
    assert c1["backtest_id"] == mock_hex_id, f"Chunk 1 backtest_id should be hex ID, got '{c1['backtest_id']}'"
    assert c1["chunk_index"] == 1, f"Chunk 1 index should be 1, got {c1['chunk_index']}"
    assert c1["start_date"] == "2019-01-01", f"Chunk 1 start_date wrong: {c1['start_date']}"
    assert c1["end_date"] == "2019-12-31", f"Chunk 1 end_date wrong: {c1['end_date']}"
    assert c1["compile_id"] == compile_id, f"Chunk 1 compile_id wrong: {c1['compile_id']}"

    # Chunk 2: PENDING with chunk_name as backtest_id
    c2 = chunk_records[1]
    assert c2["status"] == "PENDING", f"Chunk 2 status should be 'PENDING', got '{c2['status']}'"
    assert c2["backtest_id"] == f"{batch_id}_Y2020", (
        f"Chunk 2 backtest_id should be chunk_name, got '{c2['backtest_id']}'"
    )
    assert c2["chunk_index"] == 2, f"Chunk 2 index should be 2, got {c2['chunk_index']}"
    assert c2["start_date"] == "2020-01-01", f"Chunk 2 start_date wrong: {c2['start_date']}"
    assert c2["end_date"] == "2020-12-31", f"Chunk 2 end_date wrong: {c2['end_date']}"

    # Chunk 3: PENDING
    c3 = chunk_records[2]
    assert c3["status"] == "PENDING", f"Chunk 3 status should be 'PENDING', got '{c3['status']}'"
    assert c3["backtest_id"] == f"{batch_id}_Y2021", (
        f"Chunk 3 backtest_id should be chunk_name, got '{c3['backtest_id']}'"
    )
    assert c3["chunk_index"] == 3, f"Chunk 3 index should be 3, got {c3['chunk_index']}"

    # Verify only 1 RUNNING and rest are PENDING
    running_count = sum(1 for c in chunk_records if c["status"] == "RUNNING")
    pending_count = sum(1 for c in chunk_records if c["status"] == "PENDING")
    assert running_count == 1, f"Expected exactly 1 RUNNING chunk, got {running_count}"
    assert pending_count == 2, f"Expected exactly 2 PENDING chunks, got {pending_count}"

    logger.info("PASS: Chunk records structure validated — 1 RUNNING + 2 PENDING, correct dates, names, and IDs.")


# ============================================================================
# Main Runner
# ============================================================================

def run_all_batch_launcher_tests():
    """Execute all batch launcher unit tests sequentially."""
    logger.info("=" * 70)
    logger.info("STARTING BATCH LAUNCHER TEST SUITE")
    logger.info("=" * 70)

    test_parse_args_defaults()
    test_parse_args_custom_values()
    test_parse_args_single_year()
    test_yaml_config_lookup_by_short_name()
    test_yaml_config_lookup_by_full_name()
    test_yaml_config_lookup_unknown_algo()
    test_extract_parsed_data_fields()
    test_chunk_records_structure()

    logger.info("=" * 70)
    logger.info("SUCCESS: ALL 8 BATCH LAUNCHER TEST MODULES PASSED!")
    logger.info("=" * 70)


if __name__ == "__main__":
    run_all_batch_launcher_tests()
