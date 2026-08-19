"""
trade_flow_sankey.py
====================
Generates an interactive Sankey diagram showing the trade lifecycle (Entry -> Outcome -> Exit Reason)
for ANY algorithm (0AT, 4EVC, 1SAOP, 5EVR, etc.) in BTOPTrades.

Data source: `bav-personal-cloud.develop.v_4EVC_trade_flow` (BigQuery view).

Usage:
    # Aggregate across all backtests
    poetry run python Scripts/Visualizations/trade_flow_sankey.py

    # Filter to a specific algorithm or backtest run
    poetry run python Scripts/Visualizations/trade_flow_sankey.py --algo 0AT
    poetry run python Scripts/Visualizations/trade_flow_sankey.py --backtest-id 0AT_20190101_000000_FIRERING

Output:
    An interactive HTML file (default: Scripts/Visualizations/reports/trade_flow.html).
"""

from __future__ import annotations

import argparse
import os
import sys
import webbrowser
from typing import List, Optional, Tuple

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_BQ_DIR = os.path.abspath(os.path.join(_SCRIPT_DIR, "..", "BigQuery"))
if _BQ_DIR not in sys.path:
    sys.path.insert(0, _BQ_DIR)

from db_operator import get_bigquery_client  # noqa: E402

try:
    import plotly.graph_objects as go
except ImportError:
    print("[Error] plotly is required. Install with: pip install plotly")
    sys.exit(1)


PROJECT_ID: str = "bav-personal-cloud"
DATASET_ID: str = "develop"
VIEW_NAME:  str = "v_4EVC_trade_flow"

NODE_COLORS: dict[str, str] = {
    "All Entered Trades": "#4A90D9",  # Blue
    "Winners":            "#2ECC71",  # Green
    "Losers":             "#E74C3C",  # Red
    "Still Open":         "#95A5A6",  # Grey
    "Stop Loss":          "#C0392B",  # Dark red
    "Take Profit":        "#27AE60",  # Dark green
    "Time Exit":          "#F39C12",  # Amber
    "DTE Safety":         "#8E44AD",  # Purple
    "Signal Exit":        "#2980B9",  # Deep blue
    "Risk Exit":          "#D35400",  # Deep orange
    "Option Assignment":  "#E67E22",  # Orange
    "Margin Call":        "#900C3F",  # Crimson
    "Corporate Action":   "#7D3C98",  # Purple
    "Trailing Stop":      "#16A085",  # Teal
    "Rebalance":          "#1ABC9C",  # Light teal
    "Unknown":            "#BDC3C7",  # Light grey
    "Other":              "#BDC3C7",  # Light grey
}
DEFAULT_COLOR: str = "#7F8C8D"


def fetch_edges(
    algo_code: Optional[str] = None,
    backtest_id: Optional[str] = None,
    project_id: str = PROJECT_ID,
    dataset_id: str = DATASET_ID,
) -> Tuple[List[dict], str]:
    full_view_id: str = f"{project_id}.{dataset_id}.{VIEW_NAME}"

    where_conditions = []
    if algo_code:
        where_conditions.append(f"algo_code = '{algo_code}'")
    if backtest_id:
        where_conditions.append(f"backtest_run_id = '{backtest_id}'")

    where_clause = f"WHERE {' AND '.join(where_conditions)}" if where_conditions else ""

    if backtest_id:
        title_suffix = f"Backtest: {backtest_id}"
    elif algo_code:
        title_suffix = f"Algorithm: {algo_code}"
    else:
        title_suffix = "All Algorithms (Aggregated)"

    sql: str = f"""
        SELECT
            source_node,
            target_node,
            SUM(trade_count) AS trade_count,
            ROUND(AVG(avg_pnl), 4) AS avg_pnl
        FROM `{full_view_id}`
        {where_clause}
        GROUP BY source_node, target_node
        ORDER BY source_node, target_node
    """

    client = get_bigquery_client(project_id=project_id)
    job = client.query(sql)
    results = list(job.result())

    if not results:
        raise ValueError(
            f"No data returned from `{full_view_id}` matching criteria (algo={algo_code}, backtest={backtest_id}).\n"
            f"Run: poetry run python Scripts/BigQuery/log_trades_uploader.py"
        )

    return [
        {
            "source_node": row.source_node,
            "target_node": row.target_node,
            "trade_count": row.trade_count,
            "avg_pnl":     row.avg_pnl,
        }
        for row in results
    ], title_suffix


def build_sankey(edges: List[dict], title_suffix: str) -> go.Figure:
    node_labels: List[str] = []
    for edge in edges:
        for label in (edge["source_node"], edge["target_node"]):
            if label not in node_labels:
                node_labels.append(label)

    label_to_idx: dict[str, int] = {lbl: i for i, lbl in enumerate(node_labels)}
    node_colors: List[str] = [NODE_COLORS.get(lbl, DEFAULT_COLOR) for lbl in node_labels]

    sources: List[int] = []
    targets: List[int] = []
    values:  List[int] = []
    hover_labels: List[str] = []

    def _hex_to_rgba(hex_color: str, alpha: float = 0.35) -> str:
        h = hex_color.lstrip("#")
        r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        return f"rgba({r},{g},{b},{alpha})"

    link_colors: List[str] = []

    for edge in edges:
        src_idx = label_to_idx[edge["source_node"]]
        tgt_idx = label_to_idx[edge["target_node"]]
        count   = edge["trade_count"]
        avg_pnl = edge["avg_pnl"]

        sources.append(src_idx)
        targets.append(tgt_idx)
        values.append(count)

        pnl_str = f"{avg_pnl * 100:.2f}%" if avg_pnl is not None else "N/A"
        hover_labels.append(
            f"{edge['source_node']} → {edge['target_node']}<br>"
            f"Trades: {count}<br>"
            f"Avg PnL: {pnl_str}"
        )

        tgt_color = NODE_COLORS.get(edge["target_node"], DEFAULT_COLOR)
        link_colors.append(_hex_to_rgba(tgt_color))

    fig = go.Figure(
        data=[
            go.Sankey(
                arrangement="snap",
                node=dict(
                    pad=20,
                    thickness=25,
                    line=dict(color="white", width=0.5),
                    label=node_labels,
                    color=node_colors,
                    hovertemplate="%{label}<br>Total trades: %{value}<extra></extra>",
                ),
                link=dict(
                    source=sources,
                    target=targets,
                    value=values,
                    color=link_colors,
                    customdata=hover_labels,
                    hovertemplate="%{customdata}<extra></extra>",
                ),
            )
        ]
    )

    fig.update_layout(
        title=dict(
            text=f"QuantConnect Trade Flow — {title_suffix}",
            font=dict(size=18, family="Inter, Arial, sans-serif"),
            x=0.5,
            xanchor="center",
        ),
        font=dict(size=13, family="Inter, Arial, sans-serif"),
        paper_bgcolor="#1a1a2e",
        plot_bgcolor="#1a1a2e",
        font_color="#e0e0e0",
        margin=dict(l=40, r=40, t=80, b=40),
        height=650,
    )

    return fig


def parse_args() -> argparse.Namespace:
    reports_dir = os.path.join(_SCRIPT_DIR, "reports")
    os.makedirs(reports_dir, exist_ok=True)

    parser = argparse.ArgumentParser(
        description="Generate a Trade-Flow Sankey diagram from BigQuery for any algorithm."
    )
    parser.add_argument(
        "--algo",
        type=str,
        default=None,
        help="Filter to a specific algo_code (e.g. 0AT, 4EVC, 1SAOP).",
    )
    parser.add_argument(
        "--backtest-id",
        type=str,
        default=None,
        help="Filter to a specific backtest_run_id.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=os.path.join(reports_dir, "trade_flow.html"),
        help="Output HTML file path (default: Scripts/Visualizations/reports/trade_flow.html).",
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Do not open the browser automatically after generating.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print(f"[Trade Flow Sankey] Fetching trade-flow data from BigQuery...")
    try:
        edges, title_suffix = fetch_edges(algo_code=args.algo, backtest_id=args.backtest_id)
    except ValueError as exc:
        print(f"[Error] {exc}")
        sys.exit(1)

    total_trades = sum(e["trade_count"] for e in edges if e["source_node"] == "All Entered Trades")
    print(f"[Trade Flow Sankey] Loaded {total_trades} entered trades across {len(edges)} edges.")

    print(f"[Trade Flow Sankey] Building Sankey diagram...")
    fig = build_sankey(edges, title_suffix)

    output_path = os.path.abspath(args.output)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.write_html(output_path, include_plotlyjs="cdn")
    print(f"[Trade Flow Sankey] Saved to: {output_path}")

    if not args.no_browser:
        webbrowser.open(f"file://{output_path}")
        print(f"[Trade Flow Sankey] Opened in browser.")


if __name__ == "__main__":
    main()
