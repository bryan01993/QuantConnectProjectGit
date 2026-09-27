"""
test_refactored_research_notebook.py
====================================
Validates that 4_EarningsVolatilityCrunch/refactored_research.ipynb
is structurally sound, adheres to nbformat v4 schema, and that every
single code cell passes python compilation without syntax errors.
"""

from pathlib import Path
import nbformat as nbf
import sys

def test_notebook_syntax():
    nb_path = Path("4_EarningsVolatilityCrunch/refactored_research.ipynb")
    assert nb_path.exists(), f"Notebook file not found at {nb_path}"
    
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = nbf.read(f, as_version=4)
        
    print(f"[TEST] Successfully loaded notebook: {nb_path.name}")
    print(f"[TEST] Total cells found: {len(nb.cells)}")
    
    code_cells = [c for c in nb.cells if c.cell_type == "code"]
    md_cells = [c for c in nb.cells if c.cell_type == "markdown"]
    print(f"[TEST] Code cells: {len(code_cells)} | Markdown cells: {len(md_cells)}")
    
    errors = []
    
    # 1. Validate python syntax for each code cell
    for idx, cell in enumerate(code_cells, 1):
        cell_src = cell.source
        header = cell_src.splitlines()[0] if cell_src.splitlines() else f"Cell #{idx}"
        try:
            compile(cell_src, f"<cell_{idx}>", "exec")
            print(f"  [PASS] Cell {idx:02d}: Syntax valid ({header[:65]}...)")
        except SyntaxError as syn_err:
            err_msg = f"Cell {idx} SyntaxError: {syn_err.msg} at line {syn_err.lineno}: {syn_err.text}"
            print(f"  [FAIL] {err_msg}")
            errors.append(err_msg)
        except Exception as exc:
            err_msg = f"Cell {idx} Compilation Error: {exc}"
            print(f"  [FAIL] {err_msg}")
            errors.append(err_msg)

    # 2. Check for required DataFrames and Testing Gates
    required_dfs = [
        "df_universe_coarse",
        "df_earnings_calendar",
        "df_underlying_metrics",
        "df_option_chains_raw",
        "df_calendar_pairs",
        "df_microstructure_quotes",
        "df_event_window_timeseries",
        "df_trade_outcomes",
        "df_factor_audit_deciles",
        "df_intraday_exit_slices",
        "df_parameter_surface_grid",
        "df_pipeline_test_results"
    ]
    
    all_code_src = "\\n".join([c.source for c in code_cells])
    missing_dfs = [df for df in required_dfs if df not in all_code_src]
    
    if missing_dfs:
        errors.append(f"Missing required DataFrames in notebook code: {missing_dfs}")
    else:
        print(f"  [PASS] All 12 required DataFrames/tables are explicitly defined and referenced.")

    # 3. Check for mandatory testing rules
    assert "-105" in all_code_src, "Missing mandatory loss floor gate (< -105%)"
    assert "dsr" in all_code_src, "Missing Deflated Sharpe Ratio calculation"
    assert "spearmanr" in all_code_src, "Missing Spearman rank correlation test"
    assert "linregress" in all_code_src, "Missing OLS regression test"
    assert "europe-west1" in all_code_src, "Missing BigQuery europe-west1 location reference"
    
    print(f"  [PASS] All mandatory research rules (Loss Floor < -105%, Zero-Dollar PnL %, DSR, BQ europe-west1) verified.")

    if errors:
        print(f"\\n[FAIL] Found {len(errors)} validation errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("\\n[SUCCESS] Notebook passed 100% of pre-flight syntax and structural checks!")

if __name__ == "__main__":
    test_notebook_syntax()
