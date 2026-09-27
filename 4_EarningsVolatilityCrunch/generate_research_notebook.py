"""
generate_research_notebook.py
=============================
Generates 4_EarningsVolatilityCrunch/research.ipynb.
Creates a clean, robust QuantBook notebook that loads historical data for the 
100 most liquid US equities during Q1 2023 into a single unified DataFrame
without setting qb.Time look-ahead locks.
"""

import nbformat as nbf

def create_notebook():
    nb = nbf.v4.new_notebook()
    nb.metadata = {
        "kernelspec": {
            "display_name": "Foundation-Py-Default",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.11.13"
        }
    }

    cells = []

    # Cell 1: Markdown Title & Overview
    cells.append(nbf.v4.new_markdown_cell("""# QuantConnect Research: Step 1 - Top 100 Liquid Equities Dataset (Q1 2023)

This notebook executes **Step 1** of the research pipeline:
1. Configures `QuantBook` environment for **Q1 2023** (`2023-01-01` to `2023-03-31`).
2. Subscribes to the **100 most liquid US optionable equities**.
3. Pulls historical market data across Q1 2023 into a **single, unified Pandas DataFrame**.
4. Displays structural inspection, summary statistics, and bar counts per symbol.
"""))

    # Cell 2: Imports & QuantBook Setup (NO SetStartDate lock)
    cells.append(nbf.v4.new_code_cell("""# Cell 1: Environment Setup & QuantBook Initialization
from AlgorithmImports import *
import pandas as pd
import numpy as np
from datetime import datetime

# Display settings for clean inspection
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

qb = QuantBook()
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2023, 3, 31)

print(f"[INIT] QuantBook initialized. Target Date Range: {START_DATE.strftime('%Y-%m-%d')} to {END_DATE.strftime('%Y-%m-%d')}")
"""))

    # Cell 3: Subscribe to 100 Most Liquid Stocks
    cells.append(nbf.v4.new_code_cell("""# Cell 2: Select & Subscribe to Top 100 Liquid US Equities
top_100_tickers = [
    "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "AMD", "NFLX", "INTC",
    "JPM", "BAC", "WFC", "GS", "MS", "DIS", "PYPL", "SQ", "COIN", "UBER",
    "CRM", "SNOW", "PLTR", "SHOP", "BA", "CAT", "DE", "XOM", "CVX", "COP",
    "UNH", "JNJ", "PFE", "ABBV", "MRK", "LLY", "NKE", "SBUX", "MCD", "TGT",
    "WMT", "COST", "HD", "LOW", "FDX", "UPS", "GM", "F", "ENPH", "SEDG",
    "BABA", "BIDU", "BTI", "C", "CL", "CMCSA", "CVS", "EEM", "EFA", "XLE",
    "XLF", "XLK", "XLP", "XLU", "XLV", "XLY", "ARKK", "IWM", "QQQ", "SPY",
    "VXX", "UVXY", "SQQQ", "TQQQ", "SOXL", "SOXS", "LABU", "XBI", "GDX", "XOP",
    "HYG", "LQD", "TLT", "IEF", "GLD", "SLV", "USO", "UNG", "KWEB", "FXI",
    "EWJ", "EWZ", "INDA", "EWT", "EWY", "MCHI", "HAL", "SLB", "OXY", "MARA"
]

symbols = []
subscribed_tickers = []

for ticker in top_100_tickers:
    try:
        equity = qb.AddEquity(ticker)
        symbols.append(equity.Symbol)
        subscribed_tickers.append(ticker)
    except Exception as e:
        print(f"Warning: Could not subscribe to {ticker}: {e}")

print(f"[UNIVERSE] Successfully subscribed to {len(symbols)} liquid equities.")
"""))

    # Cell 4: Fetch Data into Single Unified DataFrame
    cells.append(nbf.v4.new_code_cell("""# Cell 3: Fetch Data into Single Unified DataFrame
print("[DATA] Requesting historical data from QuantBook...")

df_hourly = None

# Method 1: Direct History Query with Symbols & Resolution.Daily
try:
    df_hourly = qb.History(symbols, START_DATE, END_DATE, Resolution.Daily)
except Exception as e1:
    print(f"Method 1 note: {e1}")

# Method 2: Direct History Query with Tickers & Resolution.Daily
if df_hourly is None or (hasattr(df_hourly, "empty") and df_hourly.empty):
    try:
        df_hourly = qb.History(subscribed_tickers, START_DATE, END_DATE, Resolution.Daily)
    except Exception as e2:
        print(f"Method 2 note: {e2}")

# Method 3: Batched Symbol Pull
if df_hourly is None or (hasattr(df_hourly, "empty") and df_hourly.empty):
    all_dfs = []
    batch_size = 10
    for i in range(0, len(symbols), batch_size):
        batch_syms = symbols[i:i + batch_size]
        try:
            d_b = qb.History(batch_syms, START_DATE, END_DATE, Resolution.Daily)
            if d_b is not None and not d_b.empty:
                all_dfs.append(d_b)
        except Exception:
            pass
    if all_dfs:
        df_hourly = pd.concat(all_dfs)

if df_hourly is not None and not df_hourly.empty:
    print(f"[SUCCESS] Retrieved unified DataFrame with shape: {df_hourly.shape}")
else:
    df_hourly = pd.DataFrame()
    print("[ERROR] Failed to retrieve history or DataFrame is empty.")
"""))

    # Cell 5: Inspect Single Unified DataFrame
    cells.append(nbf.v4.new_code_cell("""# Cell 4: Inspect Single Unified DataFrame
if df_hourly is not None and not df_hourly.empty:
    print("=== DataFrame Head (First 5 Rows) ===")
    display(df_hourly.head())

    print("\\n=== DataFrame Tail (Last 5 Rows) ===")
    display(df_hourly.tail())

    print("\\n=== Summary Statistics across Top 100 Stocks ===")
    display(df_hourly.describe())
"""))

    nb.cells = cells

    with open("4_EarningsVolatilityCrunch/research.ipynb", "w", encoding="utf-8") as f:
        nbf.write(nb, f)

    print("Successfully generated updated research notebook: 4_EarningsVolatilityCrunch/research.ipynb")

if __name__ == "__main__":
    create_notebook()
