# 4EVC_report_overview — Looker Studio Setup Guide

This document walks through building the **`4EVC_report_overview`** report in Looker Studio (formerly Google Data Studio).
The report shows **decile plots** that correlate the 4EVC trade entry signals against realized PnL — one plot per signal — with a backtest selector dropdown.

---

## Prerequisites

| Item | Detail |
|---|---|
| BigQuery view deployed | Run `poetry run python Scripts/BigQuery/create_4evc_decile_view.py` first |
| BigQuery view name | `bav-personal-cloud.develop.v_4EVC_decile_signals` |
| Google account | Must have read access to the `bav-personal-cloud` GCP project |
| Looker Studio URL | [lookerstudio.google.com](https://lookerstudio.google.com) |

---

## Step 1 — Create a New Report

1. Go to [lookerstudio.google.com](https://lookerstudio.google.com) and click **Create → Report**.
2. In the **Add data to report** panel, select **BigQuery**.
3. Choose **Custom Query** (not table selector — this allows us to point directly at the view).
4. Set:
   - **Billing Project:** `bav-personal-cloud`
   - **Custom Query:**
     ```sql
     SELECT * FROM `bav-personal-cloud.develop.v_4EVC_decile_signals`
     ```
5. Click **Add → Add to Report**.
6. Rename the report to **`4EVC_report_overview`** (top-left title bar).

---

## Step 2 — Verify the Data Source Schema

After connecting, confirm the following fields are available:

| Field Name | Type | Role |
|---|---|---|
| `backtest_run_id` | Text | Dimension (used for filtering) |
| `signal_name` | Text | Dimension (used for chart filter) |
| `decile` | Number | X-axis dimension |
| `mean_pnl` | Number | Metric (Y-axis — set aggregation to **None / AVG**) |
| `trade_count` | Number | Secondary metric |

> [!IMPORTANT]
> Change `decile` type to **Number** (not Text) so Looker Studio sorts it 1–10 correctly on the X-axis. Click the field → pencil icon → set Type = **Number**.

---

## Step 3 — Add the Backtest Selector (Filter Control)

This dropdown lets you choose which backtest to inspect.

1. In the top menu: **Insert → Filter Control**.
2. Place it at the top of the report canvas.
3. In the right-side **Filter Control** properties:
   - **Control Field:** `backtest_run_id`
   - **Metric:** *(leave empty)*
   - **Default selection:** *(optional: your most recent run ID)*
4. Label it **"Select Backtest Run"**.

> [!NOTE]
> When a backtest is selected, **all charts on the page** will automatically filter to only that backtest's data because they share the same data source.

---

## Step 4 — Add the Three Decile Charts

Repeat the following steps **3 times**, once per signal (`vol_ratio`, `slope`, `ivrv_ratio`).

### 4a — Insert a Line Chart

1. **Insert → Line Chart**.
2. Place it on the canvas. Aim for a 3-column row layout.

### 4b — Configure Dimensions and Metrics

In the **Chart → Data** panel (right side):

| Property | Value |
|---|---|
| **Dimension** | `decile` |
| **Metric** | `mean_pnl` (aggregation: **AVG** or **Sum** if already pre-aggregated) |
| **Sort** | `decile` Ascending |

> [!TIP]
> Since `mean_pnl` is already aggregated in the view, set the metric aggregation to **Sum** (which equals the value since each decile appears once per backtest) — or use **AVG** to be safe.

### 4c — Add a Signal Filter (Chart-Level)

Each chart must only show one signal. Add a **filter** inside the chart:

1. In Chart → **Data** tab → scroll to **Filter** section → click **Add a Filter**.
2. Click **Create a Filter**:
   - **Name:** e.g. `filter_vol_ratio`
   - **Include:** `signal_name` → **Equal to (=)** → `vol_ratio`
3. Click **Save**.

Repeat for the other two charts with `slope` and `ivrv_ratio`.

### 4d — Chart Titles and Styling

For each chart:

| Signal | Chart Title |
|---|---|
| `vol_ratio` | `Mean Return Pct by vol_ratio Decile` |
| `slope` | `Mean Return Pct by slope Decile` |
| `ivrv_ratio` | `Mean Return Pct by ivrv_ratio Decile` |

**Style settings (in Chart → Style tab):**
- **Series color:** `#1A73E8` (blue line — matches the reference image)
- **Show data labels:** ✅ On
- **Chart background:** White
- **Y-axis title:** `Mean Return Pct`
- **X-axis title:** `Decile Range` (or `Decile`)
- **Reference Line:** Add a horizontal reference line at Y = 0 (zero line) to visually separate positive/negative deciles

---

## Step 5 — Add a Zero Reference Line

For each chart, in the **Style** tab:
1. Scroll to **Reference lines**.
2. Click **Add reference line**.
3. Set **Value = 0**, **Line color = red dashed**, **Label = "Zero"**.

This matches the reference-image styling and makes the monotonic trend easy to read.

---

## Step 6 — Final Layout

Suggested layout on a single report page:

```
┌────────────────────────────────────────────────────┐
│  4EVC_report_overview              [Select Backtest]│
├──────────────┬──────────────┬──────────────────────┤
│  vol_ratio   │    slope     │     ivrv_ratio        │
│  Decile Plot │  Decile Plot │     Decile Plot       │
│              │              │                       │
└──────────────┴──────────────┴───────────────────────┘
```

---

## Step 7 — Share / Bookmark

1. Click **Share** (top right) → choose viewer access settings.
2. Copy the report URL and save it — the URL encodes the report ID.
3. Optionally use **File → Embed Report** to embed it in a dashboard later.

---

## Signal Interpretation Guide

| Signal | Decile Direction | Healthy Pattern |
|---|---|---|
| `vol_ratio` | 10 = highest volume surge | Higher decile → higher mean return (monotonic ↑) |
| `slope` | 10 = steepest IV term slope | Higher decile → higher mean return (monotonic ↑) |
| `ivrv_ratio` | 10 = most elevated IV vs RV | Higher decile → higher mean return (monotonic ↑) |

> [!NOTE]
> A **monotonically increasing** trend (left to right, decile 1 → 10) means the signal positively predicts trade profitability. The reference image shows a **decreasing** trend because the signal was sorted in reverse — both are valid depending on convention. In this implementation, **decile 10 = strongest entry condition**.

---

## Maintenance

- Every time new 4EVC backtests are uploaded via `log_trades_uploader.py`, the view automatically includes them — no manual refresh needed.
- The backtest selector will automatically populate with new `backtest_run_id` values.
- If the `BTOPTrades` schema changes, re-run `create_4evc_decile_view.py` to recreate the view.
