#!/usr/bin/env python3
"""Analyze mortgage-rate pass-through extracts using only the Python stdlib."""

from __future__ import annotations

import csv
import datetime as dt
import math
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def fnum(value: str | None) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def parse_date(value: str) -> dt.date:
    return dt.date.fromisoformat(value)


def q_add(q: dt.date, n: int) -> dt.date:
    month_index = q.year * 12 + (q.month - 1) + n * 3
    return dt.date(month_index // 12, month_index % 12 + 1, 1)


def quarter_label(q: dt.date) -> str:
    return f"{q.year}Q{((q.month - 1) // 3) + 1}"


def mean(values: list[float]) -> float | None:
    clean = [v for v in values if v is not None and math.isfinite(v)]
    if not clean:
        return None
    return sum(clean) / len(clean)


def weighted_mean(pairs: list[tuple[float, float]]) -> float | None:
    clean = [(v, w) for v, w in pairs if v is not None and w is not None and w > 0]
    if not clean:
        return None
    total_w = sum(w for _, w in clean)
    return sum(v * w for v, w in clean) / total_w


def stdev(values: list[float]) -> float | None:
    clean = [v for v in values if v is not None and math.isfinite(v)]
    if len(clean) < 2:
        return None
    m = sum(clean) / len(clean)
    return math.sqrt(sum((v - m) ** 2 for v in clean) / (len(clean) - 1))


def median_value(values: list[float]) -> float | None:
    clean = sorted(v for v in values if v is not None and math.isfinite(v))
    if not clean:
        return None
    mid = len(clean) // 2
    if len(clean) % 2:
        return clean[mid]
    return (clean[mid - 1] + clean[mid]) / 2


def zscores(values_by_key: dict[str, float]) -> dict[str, float]:
    vals = list(values_by_key.values())
    m = mean(vals)
    s = stdev(vals)
    if m is None or not s:
        return {}
    return {k: (v - m) / s for k, v in values_by_key.items() if v is not None}


def assign_quartiles(values_by_key: dict[str, float]) -> dict[str, int]:
    ordered = sorted((v, k) for k, v in values_by_key.items() if v is not None)
    n = len(ordered)
    result: dict[str, int] = {}
    for idx, (_, key) in enumerate(ordered):
        result[key] = min(4, int(idx * 4 / n) + 1)
    return result


def two_way_demean(rows: list[dict[str, object]], value_key: str) -> list[float]:
    by_lad: dict[str, list[float]] = defaultdict(list)
    by_q: dict[dt.date, list[float]] = defaultdict(list)
    vals: list[float] = []
    for row in rows:
        value = float(row[value_key])
        vals.append(value)
        by_lad[str(row["lad_code"])].append(value)
        by_q[row["quarter"]].append(value)
    grand = sum(vals) / len(vals)
    lad_mean = {k: sum(v) / len(v) for k, v in by_lad.items()}
    q_mean = {k: sum(v) / len(v) for k, v in by_q.items()}
    return [
        float(row[value_key])
        - lad_mean[str(row["lad_code"])]
        - q_mean[row["quarter"]]
        + grand
        for row in rows
    ]


def cluster_ols_one_x(rows: list[dict[str, object]]) -> dict[str, float | int]:
    if len(rows) < 50:
        return {"n": len(rows), "beta": float("nan"), "se": float("nan"), "t": float("nan"), "p": float("nan")}
    y = two_way_demean(rows, "y")
    x = two_way_demean(rows, "x")
    xx = sum(v * v for v in x)
    if xx == 0:
        return {"n": len(rows), "beta": float("nan"), "se": float("nan"), "t": float("nan"), "p": float("nan")}
    beta = sum(xi * yi for xi, yi in zip(x, y)) / xx
    residuals = [yi - beta * xi for xi, yi in zip(x, y)]
    cluster_scores: dict[str, float] = defaultdict(float)
    for row, xi, ei in zip(rows, x, residuals):
        cluster_scores[str(row["lad_code"])] += xi * ei
    m = len(cluster_scores)
    cluster_sum = sum(score * score for score in cluster_scores.values())
    correction = m / (m - 1) if m > 1 else 1.0
    se = math.sqrt(correction * cluster_sum / (xx * xx))
    t = beta / se if se else float("nan")
    p = math.erfc(abs(t) / math.sqrt(2)) if math.isfinite(t) else float("nan")
    return {"n": len(rows), "clusters": m, "beta": beta, "se": se, "t": t, "p": p}


def invert_matrix(matrix: list[list[float]]) -> list[list[float]] | None:
    n = len(matrix)
    aug = [[float(matrix[i][j]) for j in range(n)] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-12:
            return None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [v / scale for v in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [v - factor * p for v, p in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


def cluster_ols(rows: list[dict[str, object]], x_keys: list[str], interest_key: str = "x") -> dict[str, float | int]:
    clean_rows = [
        row for row in rows
        if row.get("y") is not None and all(row.get(key) is not None for key in x_keys)
    ]
    if len(clean_rows) < max(50, len(x_keys) + 5) or interest_key not in x_keys:
        return {"n": len(clean_rows), "beta": float("nan"), "se": float("nan"), "t": float("nan"), "p": float("nan")}

    y = two_way_demean(clean_rows, "y")
    x_cols = [two_way_demean(clean_rows, key) for key in x_keys]
    k = len(x_keys)
    xtx = [[sum(x_cols[i][r] * x_cols[j][r] for r in range(len(clean_rows))) for j in range(k)] for i in range(k)]
    xty = [sum(x_cols[i][r] * y[r] for r in range(len(clean_rows))) for i in range(k)]
    inv = invert_matrix(xtx)
    if inv is None:
        return {"n": len(clean_rows), "beta": float("nan"), "se": float("nan"), "t": float("nan"), "p": float("nan")}

    betas = [sum(inv[i][j] * xty[j] for j in range(k)) for i in range(k)]
    residuals = [
        y[r] - sum(betas[j] * x_cols[j][r] for j in range(k))
        for r in range(len(clean_rows))
    ]
    cluster_scores: dict[str, list[float]] = defaultdict(lambda: [0.0] * k)
    for row, idx in zip(clean_rows, range(len(clean_rows))):
        scores = cluster_scores[str(row["lad_code"])]
        for j in range(k):
            scores[j] += x_cols[j][idx] * residuals[idx]
    meat = [[0.0 for _ in range(k)] for _ in range(k)]
    for scores in cluster_scores.values():
        for i in range(k):
            for j in range(k):
                meat[i][j] += scores[i] * scores[j]
    middle = [
        [sum(inv[i][a] * meat[a][b] for a in range(k)) for b in range(k)]
        for i in range(k)
    ]
    vcov = [
        [sum(middle[i][b] * inv[j][b] for b in range(k)) for j in range(k)]
        for i in range(k)
    ]
    m = len(cluster_scores)
    correction = m / (m - 1) if m > 1 else 1.0
    interest_idx = x_keys.index(interest_key)
    beta = betas[interest_idx]
    variance = correction * vcov[interest_idx][interest_idx]
    se = math.sqrt(variance) if variance >= 0 else float("nan")
    t = beta / se if se else float("nan")
    p = math.erfc(abs(t) / math.sqrt(2)) if math.isfinite(t) else float("nan")
    return {"n": len(clean_rows), "clusters": m, "beta": beta, "se": se, "t": t, "p": p}


def formatted_result(
    robustness: str,
    outcome: str,
    shock: str,
    constraint: str,
    result: dict[str, float | int],
    note: str,
) -> dict[str, object]:
    beta = result["beta"]
    p = result["p"]
    return {
        "robustness": robustness,
        "outcome": outcome,
        "shock": shock,
        "constraint": constraint,
        "n": result.get("n", ""),
        "clusters": result.get("clusters", ""),
        "beta": f"{beta:.6f}" if isinstance(beta, float) and math.isfinite(beta) else "",
        "cluster_se": f"{result['se']:.6f}" if isinstance(result.get("se"), float) and math.isfinite(result["se"]) else "",
        "t_stat": f"{result['t']:.3f}" if isinstance(result.get("t"), float) and math.isfinite(result["t"]) else "",
        "p_value": f"{p:.4f}" if isinstance(p, float) and math.isfinite(p) else "",
        "note": note,
    }


def svg_line_chart(path: Path, title: str, series: dict[str, list[tuple[dt.date, float]]], y_label: str) -> None:
    width, height = 860, 470
    left, right, top, bottom = 72, 30, 54, 62
    colors = ["#1b4d89", "#b33c2e", "#257a4f", "#7a4f99", "#c27c1a", "#4c6473"]
    all_points = [(q, v) for pts in series.values() for q, v in pts if v is not None and math.isfinite(v)]
    if not all_points:
        return
    dates = sorted({q for q, _ in all_points})
    min_y = min(v for _, v in all_points)
    max_y = max(v for _, v in all_points)
    pad = (max_y - min_y) * 0.08 or 1.0
    min_y -= pad
    max_y += pad
    x_pos = {q: left + (width - left - right) * i / max(1, len(dates) - 1) for i, q in enumerate(dates)}

    def y_pos(v: float) -> float:
        return top + (height - top - bottom) * (max_y - v) / (max_y - min_y)

    lines = []
    for i in range(6):
        y = top + (height - top - bottom) * i / 5
        val = max_y - (max_y - min_y) * i / 5
        lines.append(f'<line x1="{left}" y1="{y:.1f}" x2="{width-right}" y2="{y:.1f}" stroke="#e2e2df" />')
        lines.append(f'<text x="{left-10}" y="{y+4:.1f}" text-anchor="end" font-size="11" fill="#555">{val:.1f}</text>')

    paths = []
    legends = []
    for idx, (name, pts) in enumerate(series.items()):
        color = colors[idx % len(colors)]
        coords = [(x_pos[q], y_pos(v)) for q, v in pts if q in x_pos and v is not None and math.isfinite(v)]
        if not coords:
            continue
        d = " ".join(("M" if i == 0 else "L") + f"{x:.1f},{y:.1f}" for i, (x, y) in enumerate(coords))
        paths.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.4" />')
        lx = left + idx * 165
        ly = height - 20
        legends.append(f'<line x1="{lx}" y1="{ly}" x2="{lx+22}" y2="{ly}" stroke="{color}" stroke-width="2.4" />')
        legends.append(f'<text x="{lx+28}" y="{ly+4}" font-size="12" fill="#333">{name}</text>')

    tick_dates = dates[:: max(1, len(dates) // 8)]
    ticks = []
    for q in tick_dates:
        x = x_pos[q]
        ticks.append(f'<line x1="{x:.1f}" y1="{height-bottom}" x2="{x:.1f}" y2="{height-bottom+5}" stroke="#777" />')
        ticks.append(f'<text x="{x:.1f}" y="{height-bottom+20}" text-anchor="middle" font-size="11" fill="#555">{quarter_label(q)}</text>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<rect width="100%" height="100%" fill="#fbfaf7" />
<text x="{left}" y="28" font-size="19" font-family="Arial, sans-serif" font-weight="700" fill="#222">{title}</text>
<text x="18" y="{top+26}" font-size="12" font-family="Arial, sans-serif" fill="#555" transform="rotate(-90 18,{top+26})">{y_label}</text>
{''.join(lines)}
<line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" stroke="#777" />
<line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" stroke="#777" />
{''.join(ticks)}
{''.join(paths)}
{''.join(legends)}
</svg>
'''
    path.write_text(svg)


def main() -> None:
    join_rows = read_csv(OUT / "postcode-join-quality.csv")
    panel_rows_raw = read_csv(OUT / "lad-quarter-panel.csv")
    mortgage_rows_raw = read_csv(OUT / "mortgage-quarterly.csv")
    constraint_rows_raw = read_csv(OUT / "lad-constraints-year.csv")
    labour_rows_raw = read_csv(OUT / "labour-lad-quarter.csv")

    constraints_by_lad: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    constraints_latest: dict[str, dict[str, float]] = {}
    for row in constraint_rows_raw:
        year = int(row["year"]) if row["year"] else None
        lad = row["lad_code"]
        if not lad or year is None:
            continue
        if 2013 <= year <= 2015:
            for field in ["net_additions_rate", "completions_rate", "vacancy_rate", "long_term_vacancy_rate"]:
                v = fnum(row.get(field))
                if v is not None:
                    constraints_by_lad[lad][field].append(v)
        if year == 2015:
            constraints_latest[lad] = {
                "net_additions_rate": fnum(row.get("net_additions_rate")),
                "vacancy_rate": fnum(row.get("vacancy_rate")),
                "long_term_vacancy_rate": fnum(row.get("long_term_vacancy_rate")),
            }

    static: dict[str, dict[str, float]] = {}
    for lad, fields in constraints_by_lad.items():
        net = mean(fields["net_additions_rate"])
        comp = mean(fields["completions_rate"])
        vac = mean(fields["vacancy_rate"])
        long_vac = mean(fields["long_term_vacancy_rate"])
        if net is not None and vac is not None:
            latest = constraints_latest.get(lad, {})
            static[lad] = {
                "net_additions_rate_pre": net,
                "completions_rate_pre": comp if comp is not None else net,
                "vacancy_rate_pre": vac,
                "long_term_vacancy_rate_pre": long_vac if long_vac is not None else vac,
                "supply_tightness": -net,
                "completions_tightness": -(comp if comp is not None else net),
                "stock_tightness": -vac,
                "long_vacancy_tightness": -(long_vac if long_vac is not None else vac),
                "supply_tightness_2015": -latest["net_additions_rate"] if latest.get("net_additions_rate") is not None else None,
                "stock_tightness_2015": -latest["vacancy_rate"] if latest.get("vacancy_rate") is not None else None,
                "long_vacancy_tightness_2015": -latest["long_term_vacancy_rate"] if latest.get("long_term_vacancy_rate") is not None else None,
            }

    constraint_keys = [
        "supply_tightness",
        "completions_tightness",
        "stock_tightness",
        "long_vacancy_tightness",
        "supply_tightness_2015",
        "stock_tightness_2015",
        "long_vacancy_tightness_2015",
    ]
    for key in constraint_keys:
        values = {lad: vals[key] for lad, vals in static.items() if vals.get(key) is not None}
        zs = zscores(values)
        qs = assign_quartiles(values)
        for lad in static:
            static[lad][f"{key}_z"] = zs.get(lad)
            if key in {"supply_tightness", "stock_tightness", "long_vacancy_tightness"}:
                static[lad][f"{key}_quartile"] = qs.get(lad)

    mortgage: dict[dt.date, dict[str, float]] = {}
    for row in mortgage_rows_raw:
        q = parse_date(row["quarter"])
        mortgage[q] = {k: fnum(v) for k, v in row.items() if k != "quarter"}

    labour: dict[tuple[str, dt.date], dict[str, float]] = {}
    for row in labour_rows_raw:
        q = parse_date(row["quarter"])
        labour[(row["lad_code"], q)] = {
            "claimant_rate": fnum(row.get("claimant_rate")),
            "claimant_count": fnum(row.get("claimant_count")),
        }

    panel: dict[tuple[str, dt.date], dict[str, object]] = {}
    for row in panel_rows_raw:
        q = parse_date(row["quarter"])
        lad = row["lad_code"]
        tx = fnum(row.get("transaction_count"))
        log_price = fnum(row.get("log_real_median_price_cpih"))
        median = fnum(row.get("median_sold_price"))
        mean_log_sold_price = fnum(row.get("mean_log_sold_price"))
        cpih = fnum(row.get("cpih_index"))
        if tx is None or log_price is None or median is None or cpih is None:
            continue
        record = {
            "quarter": q,
            "lad_code": lad,
            "lad_name": row["lad_name"],
            "region_code": row["region_code"],
            "transaction_count": tx,
            "log_transaction_count": math.log(tx),
            "median_sold_price": median,
            "mean_log_sold_price": mean_log_sold_price,
            "real_median_price_cpih": median / cpih,
            "log_real_median_price_cpih": log_price,
            "mean_log_real_price_cpih": mean_log_sold_price - math.log(cpih) if mean_log_sold_price is not None and cpih > 0 else None,
            "log_real_median_price_cpi": fnum(row.get("log_real_median_price_cpi")),
            "detached_share": fnum(row.get("detached_share")),
            "semi_detached_share": fnum(row.get("semi_detached_share")),
            "terraced_share": fnum(row.get("terraced_share")),
            "flat_maisonette_share": fnum(row.get("flat_maisonette_share")),
            "freehold_share": fnum(row.get("freehold_share")),
            "new_build_share": fnum(row.get("new_build_share")),
        }
        panel[(lad, q)] = record

    quarters = sorted({q for _, q in panel})
    lads = sorted({lad for lad, _ in panel})
    sparse_cells = sum(1 for row in panel.values() if float(row["transaction_count"]) < 20)
    post2016_cells = [row for row in panel.values() if row["quarter"] >= dt.date(2016, 1, 1)]

    latest_quarter_rows: list[dict[str, object]] = []
    for q in quarters[-10:]:
        rows_q = [row for row in panel.values() if row["quarter"] == q]
        prior_rows = [row for row in panel.values() if row["quarter"] == q_add(q, -4)]
        total_tx = sum(float(row["transaction_count"]) for row in rows_q)
        prior_total_tx = sum(float(row["transaction_count"]) for row in prior_rows)
        latest_quarter_rows.append({
            "quarter": quarter_label(q),
            "lad_cells": len(rows_q),
            "total_transactions": int(total_tx),
            "median_transactions_per_lad": f"{median_value([float(row['transaction_count']) for row in rows_q]):.1f}",
            "sparse_cells_lt_20_transactions": sum(1 for row in rows_q if float(row["transaction_count"]) < 20),
            "same_quarter_prior_year_transactions": int(prior_total_tx) if prior_total_tx else "",
            "transaction_change_vs_prior_year_pct": f"{(total_tx / prior_total_tx - 1) * 100:.2f}" if prior_total_tx else "",
            "note": "Completed-sale counts by transaction date; the latest quarters may still be revised by later registrations.",
        })

    # Build local-projection model rows.
    model_rows: list[dict[str, object]] = []
    for (lad, q), current in panel.items():
        if q < dt.date(2016, 1, 1):
            continue
        future = panel.get((lad, q_add(q, 4)))
        if future is None or lad not in static or q not in mortgage:
            continue
        if float(current["transaction_count"]) < 20 or float(future["transaction_count"]) < 20:
            continue
        for outcome, y in [
            ("price_h4", float(future["log_real_median_price_cpih"]) - float(current["log_real_median_price_cpih"])),
            ("transactions_h4", float(future["log_transaction_count"]) - float(current["log_transaction_count"])),
        ]:
            for shock in [
                "delta_effective_new_business_headline",
                "delta_quoted_2y_75_ltv",
                "delta_quoted_effective_spread_2y",
            ]:
                shock_value = mortgage[q].get(shock)
                if shock_value is None:
                    continue
                for constraint in ["supply_tightness", "stock_tightness", "long_vacancy_tightness"]:
                    z = static[lad].get(f"{constraint}_z")
                    if z is None:
                        continue
                    model_rows.append({
                        "lad_code": lad,
                        "quarter": q,
                        "outcome": outcome,
                        "shock": shock,
                        "constraint": constraint,
                        "y": y,
                        "x": shock_value * z,
                    })

    model_results: list[dict[str, object]] = []
    for outcome in ["price_h4", "transactions_h4"]:
        for shock in [
            "delta_effective_new_business_headline",
            "delta_quoted_2y_75_ltv",
            "delta_quoted_effective_spread_2y",
        ]:
            for constraint in ["supply_tightness", "stock_tightness", "long_vacancy_tightness"]:
                rows = [r for r in model_rows if r["outcome"] == outcome and r["shock"] == shock and r["constraint"] == constraint]
                res = cluster_ols_one_x(rows)
                beta = res["beta"]
                p = res["p"]
                sign = "negative" if isinstance(beta, float) and beta < 0 else "positive"
                sig = "p<0.05" if isinstance(p, float) and p < 0.05 else ("p<0.10" if isinstance(p, float) and p < 0.10 else "not_significant")
                model_results.append({
                    "outcome": outcome,
                    "shock": shock,
                    "constraint": constraint,
                    "n": res.get("n", ""),
                    "clusters": res.get("clusters", ""),
                    "beta": f"{beta:.6f}" if isinstance(beta, float) and math.isfinite(beta) else "",
                    "cluster_se": f"{res['se']:.6f}" if isinstance(res.get("se"), float) and math.isfinite(res["se"]) else "",
                    "t_stat": f"{res['t']:.3f}" if isinstance(res.get("t"), float) and math.isfinite(res["t"]) else "",
                    "p_value": f"{p:.4f}" if isinstance(p, float) and math.isfinite(p) else "",
                    "sign": sign,
                    "significance": sig,
                })

    def shock_for_timing(q: dt.date, shock: str, timing: str) -> float | None:
        if timing.startswith("lag_"):
            lag = int(timing.split("_")[1].removesuffix("q"))
            return mortgage.get(q_add(q, -lag), {}).get(shock)
        if timing == "current_q":
            return mortgage.get(q, {}).get(shock)
        if timing == "cumulative_2q":
            vals = [mortgage.get(q_add(q, -lag), {}).get(shock) for lag in range(2)]
            return sum(vals) if all(v is not None for v in vals) else None
        if timing == "cumulative_4q":
            vals = [mortgage.get(q_add(q, -lag), {}).get(shock) for lag in range(4)]
            return sum(vals) if all(v is not None for v in vals) else None
        return None

    lagged_rows: list[dict[str, object]] = []
    lagged_timings = [
        ("current_q", "Mortgage-rate change in the same quarter as the completed-sale start point."),
        ("lag_1q", "Mortgage-rate change one quarter before the completed-sale start point."),
        ("lag_2q", "Mortgage-rate change two quarters before the completed-sale start point."),
        ("lag_3q", "Mortgage-rate change three quarters before the completed-sale start point."),
        ("cumulative_2q", "Cumulative mortgage-rate change over the completed-sale start quarter and prior quarter."),
        ("cumulative_4q", "Cumulative mortgage-rate change over the completed-sale start quarter and prior three quarters."),
    ]
    for timing, note in lagged_timings:
        timing_rows: list[dict[str, object]] = []
        for (lad, q), current in panel.items():
            if q < dt.date(2016, 1, 1):
                continue
            future = panel.get((lad, q_add(q, 4)))
            if future is None or lad not in static:
                continue
            if float(current["transaction_count"]) < 20 or float(future["transaction_count"]) < 20:
                continue
            for outcome, y in [
                ("price_h4", float(future["log_real_median_price_cpih"]) - float(current["log_real_median_price_cpih"])),
                ("transactions_h4", float(future["log_transaction_count"]) - float(current["log_transaction_count"])),
            ]:
                for shock in [
                    "delta_effective_new_business_headline",
                    "delta_quoted_2y_75_ltv",
                    "delta_quoted_effective_spread_2y",
                ]:
                    shock_value = shock_for_timing(q, shock, timing)
                    if shock_value is None:
                        continue
                    for constraint in ["supply_tightness", "stock_tightness", "long_vacancy_tightness"]:
                        z = static[lad].get(f"{constraint}_z")
                        if z is None:
                            continue
                        timing_rows.append({
                            "lad_code": lad,
                            "quarter": q,
                            "outcome": outcome,
                            "shock": shock,
                            "constraint": constraint,
                            "y": y,
                            "x": shock_value * z,
                        })
        for outcome in ["price_h4", "transactions_h4"]:
            for shock in [
                "delta_effective_new_business_headline",
                "delta_quoted_2y_75_ltv",
                "delta_quoted_effective_spread_2y",
            ]:
                for constraint in ["supply_tightness", "stock_tightness", "long_vacancy_tightness"]:
                    rows = [r for r in timing_rows if r["outcome"] == outcome and r["shock"] == shock and r["constraint"] == constraint]
                    res = cluster_ols_one_x(rows)
                    beta = res["beta"]
                    p = res["p"]
                    lagged_rows.append({
                        "shock_timing": timing,
                        "outcome": outcome,
                        "shock": shock,
                        "constraint": constraint,
                        "n": res.get("n", ""),
                        "clusters": res.get("clusters", ""),
                        "beta": f"{beta:.6f}" if isinstance(beta, float) and math.isfinite(beta) else "",
                        "cluster_se": f"{res['se']:.6f}" if isinstance(res.get("se"), float) and math.isfinite(res["se"]) else "",
                        "t_stat": f"{res['t']:.3f}" if isinstance(res.get("t"), float) and math.isfinite(res["t"]) else "",
                        "p_value": f"{p:.4f}" if isinstance(p, float) and math.isfinite(p) else "",
                        "note": note,
                    })

    robustness_results: list[dict[str, object]] = []

    def outcome_value(current: dict[str, object], future: dict[str, object], outcome: str, price_field: str) -> float | None:
        if outcome == "price_h4":
            current_y = current.get(price_field)
            future_y = future.get(price_field)
            if current_y is None or future_y is None:
                return None
            return float(future_y) - float(current_y)
        if outcome == "transactions_h4":
            return float(future["log_transaction_count"]) - float(current["log_transaction_count"])
        return None

    def add_robustness_spec(
        robustness: str,
        note: str,
        *,
        outcomes: list[str],
        shocks: list[str],
        constraints: list[str],
        price_field: str = "log_real_median_price_cpih",
        exclude_london: bool = False,
        max_future_quarter: dt.date | None = None,
        min_tx: int = 20,
        composition_controls: bool = False,
        labour_controls: bool = False,
    ) -> None:
        rows_for_spec: list[dict[str, object]] = []
        for (lad, q), current in panel.items():
            if q < dt.date(2016, 1, 1):
                continue
            if exclude_london and current["region_code"] == "E12000007":
                continue
            future = panel.get((lad, q_add(q, 4)))
            if future is None or lad not in static or q not in mortgage:
                continue
            if exclude_london and future["region_code"] == "E12000007":
                continue
            if max_future_quarter and future["quarter"] > max_future_quarter:
                continue
            if float(current["transaction_count"]) < min_tx or float(future["transaction_count"]) < min_tx:
                continue
            controls: dict[str, float] = {}
            if composition_controls:
                for field in ["detached_share", "semi_detached_share", "terraced_share", "freehold_share", "new_build_share"]:
                    current_v = current.get(field)
                    future_v = future.get(field)
                    if current_v is None or future_v is None:
                        controls = {}
                        break
                    controls[f"d_{field}"] = float(future_v) - float(current_v)
                if not controls:
                    continue
            if labour_controls:
                current_labour = labour.get((lad, q))
                future_labour = labour.get((lad, q_add(q, 4)))
                if current_labour is None or future_labour is None:
                    continue
                current_claimant = current_labour.get("claimant_rate")
                future_claimant = future_labour.get("claimant_rate")
                claimant_metric = "claimant_rate"
                if current_claimant is None or future_claimant is None:
                    current_claimant = current_labour.get("claimant_count")
                    future_claimant = future_labour.get("claimant_count")
                    claimant_metric = "claimant_count"
                if current_claimant is None or future_claimant is None:
                    continue
                controls["claimant_metric_start"] = current_claimant
                controls["d_claimant_metric_h4"] = future_claimant - current_claimant
                controls["claimant_metric_is_count"] = 1.0 if claimant_metric == "claimant_count" else 0.0
            for outcome in outcomes:
                y = outcome_value(current, future, outcome, price_field)
                if y is None:
                    continue
                for shock in shocks:
                    shock_value = mortgage[q].get(shock)
                    if shock_value is None:
                        continue
                    for constraint in constraints:
                        z = static[lad].get(f"{constraint}_z")
                        if z is None:
                            continue
                        rows_for_spec.append({
                            "lad_code": lad,
                            "quarter": q,
                            "outcome": outcome,
                            "shock": shock,
                            "constraint": constraint,
                            "y": y,
                            "x": shock_value * z,
                            **controls,
                        })
        control_keys = []
        if composition_controls:
            control_keys.extend(["d_detached_share", "d_semi_detached_share", "d_terraced_share", "d_freehold_share", "d_new_build_share"])
        if labour_controls:
            control_keys.extend(["claimant_metric_start", "d_claimant_metric_h4"])
        x_keys = ["x", *control_keys]
        for outcome in outcomes:
            for shock in shocks:
                for constraint in constraints:
                    rows = [
                        r for r in rows_for_spec
                        if r["outcome"] == outcome and r["shock"] == shock and r["constraint"] == constraint
                    ]
                    res = cluster_ols(rows, x_keys)
                    robustness_results.append(formatted_result(robustness, outcome, shock, constraint, res, note))

    add_robustness_spec(
        "cpi_deflator",
        "Same 4Q price model using CPI instead of CPIH.",
        outcomes=["price_h4"],
        shocks=["delta_effective_new_business_headline", "delta_quoted_2y_75_ltv"],
        constraints=["supply_tightness", "stock_tightness"],
        price_field="log_real_median_price_cpi",
    )
    add_robustness_spec(
        "mean_log_price_measure",
        "Same 4Q price model using mean log sold price deflated by CPIH instead of approximate median sold price.",
        outcomes=["price_h4"],
        shocks=["delta_effective_new_business_headline", "delta_quoted_2y_75_ltv"],
        constraints=["supply_tightness", "stock_tightness"],
        price_field="mean_log_real_price_cpih",
    )
    add_robustness_spec(
        "composition_controls",
        "Price model controlling for 4Q changes in property mix: detached, semi-detached, terraced, freehold, and new-build shares.",
        outcomes=["price_h4"],
        shocks=["delta_effective_new_business_headline", "delta_quoted_2y_75_ltv"],
        constraints=["supply_tightness", "stock_tightness"],
        composition_controls=True,
    )
    add_robustness_spec(
        "labour_controls",
        "Model controlling for starting claimant metric and 4Q claimant-metric change; this extract falls back to claimant count where claimant rate is unavailable.",
        outcomes=["price_h4", "transactions_h4"],
        shocks=["delta_effective_new_business_headline", "delta_quoted_2y_75_ltv"],
        constraints=["supply_tightness", "stock_tightness"],
        labour_controls=True,
    )
    add_robustness_spec(
        "exclude_london",
        "Same model excluding London region_code E12000007.",
        outcomes=["price_h4", "transactions_h4"],
        shocks=["delta_effective_new_business_headline", "delta_quoted_2y_75_ltv"],
        constraints=["supply_tightness", "stock_tightness"],
        exclude_london=True,
    )
    add_robustness_spec(
        "drop_latest_two_completion_quarters",
        "Same model excluding outcomes that end in 2025Q4 or 2026Q1, which are most exposed to late registrations.",
        outcomes=["price_h4", "transactions_h4"],
        shocks=["delta_effective_new_business_headline", "delta_quoted_2y_75_ltv"],
        constraints=["supply_tightness", "stock_tightness"],
        max_future_quarter=dt.date(2025, 7, 1),
    )
    add_robustness_spec(
        "min_50_transactions",
        "Same model requiring at least 50 completed transactions in both start and end LAD-quarter cells.",
        outcomes=["price_h4", "transactions_h4"],
        shocks=["delta_effective_new_business_headline", "delta_quoted_2y_75_ltv"],
        constraints=["supply_tightness", "stock_tightness"],
        min_tx=50,
    )

    for robustness, constraint, note in [
        ("constraint_avg_completions_2013_2015", "completions_tightness", "Uses 2013-2015 average housing completions rate instead of net additions rate."),
        ("constraint_net_additions_2015", "supply_tightness_2015", "Uses 2015-only net additions rate instead of 2013-2015 average net additions rate."),
        ("constraint_vacancy_2015", "stock_tightness_2015", "Uses 2015-only vacancy rate instead of 2013-2015 average vacancy rate."),
        ("constraint_long_vacancy_2015", "long_vacancy_tightness_2015", "Uses 2015-only long-term vacancy rate instead of 2013-2015 average long-term vacancy rate."),
    ]:
        add_robustness_spec(
            robustness,
            note,
            outcomes=["price_h4", "transactions_h4"],
            shocks=["delta_effective_new_business_headline", "delta_quoted_2y_75_ltv"],
            constraints=[constraint],
        )

    # Quartile summaries and indexed series.
    quartile_rows: list[dict[str, object]] = []
    indexed_price: dict[str, list[tuple[dt.date, float]]] = {}
    indexed_tx: dict[str, list[tuple[dt.date, float]]] = {}
    for constraint in ["supply_tightness", "stock_tightness"]:
        for qnum in [1, 2, 3, 4]:
            label = f"{constraint.replace('_', ' ')} Q{qnum}"
            pts_price = []
            pts_tx = []
            for q in quarters:
                rows = [
                    row for (lad, qq), row in panel.items()
                    if qq == q and lad in static and static[lad].get(f"{constraint}_quartile") == qnum
                ]
                rp = weighted_mean([(float(row["real_median_price_cpih"]), float(row["transaction_count"])) for row in rows])
                tx_sum = sum(float(row["transaction_count"]) for row in rows)
                if rp is not None:
                    pts_price.append((q, rp))
                if tx_sum:
                    pts_tx.append((q, tx_sum))
            base_price = next((v for q, v in pts_price if q == dt.date(2016, 1, 1)), None)
            base_tx = next((v for q, v in pts_tx if q == dt.date(2016, 1, 1)), None)
            if base_price:
                indexed_price[label] = [(q, v / base_price * 100) for q, v in pts_price]
            if base_tx:
                indexed_tx[label] = [(q, v / base_tx * 100) for q, v in pts_tx]

            latest_constraints = [
                static[lad] for lad in static
                if static[lad].get(f"{constraint}_quartile") == qnum
            ]
            quartile_rows.append({
                "constraint": constraint,
                "quartile": qnum,
                "lad_count": len(latest_constraints),
                "mean_net_additions_rate_pre": f"{mean([v['net_additions_rate_pre'] for v in latest_constraints]):.6f}",
                "mean_vacancy_rate_pre": f"{mean([v['vacancy_rate_pre'] for v in latest_constraints]):.6f}",
                "mean_long_term_vacancy_rate_pre": f"{mean([v['long_term_vacancy_rate_pre'] for v in latest_constraints]):.6f}",
            })

    # Episode summary around the 2022-24 tightening.
    episode_rows: list[dict[str, object]] = []
    start_q, end_q = dt.date(2021, 10, 1), dt.date(2024, 10, 1)
    for constraint in ["supply_tightness", "stock_tightness"]:
        for qnum in [1, 4]:
            lads_q = [lad for lad, vals in static.items() if vals.get(f"{constraint}_quartile") == qnum]
            start_rows = [panel[(lad, start_q)] for lad in lads_q if (lad, start_q) in panel]
            end_rows = [panel[(lad, end_q)] for lad in lads_q if (lad, end_q) in panel]
            start_price = weighted_mean([(float(r["real_median_price_cpih"]), float(r["transaction_count"])) for r in start_rows])
            end_price = weighted_mean([(float(r["real_median_price_cpih"]), float(r["transaction_count"])) for r in end_rows])
            start_tx = sum(float(r["transaction_count"]) for r in start_rows)
            end_tx = sum(float(r["transaction_count"]) for r in end_rows)
            episode_rows.append({
                "constraint": constraint,
                "quartile": qnum,
                "start_quarter": quarter_label(start_q),
                "end_quarter": quarter_label(end_q),
                "lad_count": len(lads_q),
                "real_price_change_pct": f"{(end_price / start_price - 1) * 100:.2f}" if start_price and end_price else "",
                "transaction_change_pct": f"{(end_tx / start_tx - 1) * 100:.2f}" if start_tx and end_tx else "",
            })

    episode_lagged_rows: list[dict[str, object]] = []
    episode_window_specs = [
        ("original_completion_window", dt.date(2021, 10, 1), dt.date(2024, 10, 1), "Original completed-sale window used in the first draft."),
        ("one_quarter_shifted_forward", dt.date(2022, 1, 1), dt.date(2025, 1, 1), "Completed-sale response window shifted forward one quarter."),
        ("two_quarter_shifted_forward", dt.date(2022, 4, 1), dt.date(2025, 4, 1), "Completed-sale response window shifted forward two quarters."),
    ]
    for window_name, window_start, window_end, note in episode_window_specs:
        for constraint in ["supply_tightness", "stock_tightness"]:
            for qnum in [1, 4]:
                lads_q = [lad for lad, vals in static.items() if vals.get(f"{constraint}_quartile") == qnum]
                start_rows = [panel[(lad, window_start)] for lad in lads_q if (lad, window_start) in panel]
                end_rows = [panel[(lad, window_end)] for lad in lads_q if (lad, window_end) in panel]
                start_price = weighted_mean([(float(r["real_median_price_cpih"]), float(r["transaction_count"])) for r in start_rows])
                end_price = weighted_mean([(float(r["real_median_price_cpih"]), float(r["transaction_count"])) for r in end_rows])
                start_tx = sum(float(r["transaction_count"]) for r in start_rows)
                end_tx = sum(float(r["transaction_count"]) for r in end_rows)
                episode_lagged_rows.append({
                    "window": window_name,
                    "constraint": constraint,
                    "quartile": qnum,
                    "start_quarter": quarter_label(window_start),
                    "end_quarter": quarter_label(window_end),
                    "lad_count": len(lads_q),
                    "real_price_change_pct": f"{(end_price / start_price - 1) * 100:.2f}" if start_price and end_price else "",
                    "transaction_change_pct": f"{(end_tx / start_tx - 1) * 100:.2f}" if start_tx and end_tx else "",
                    "note": note,
                })

    # Hypothesis confidence labels from the screening results.
    def find_result(outcome: str, shock: str, constraint: str) -> dict[str, object]:
        for row in model_results:
            if row["outcome"] == outcome and row["shock"] == shock and row["constraint"] == constraint:
                return row
        return {}

    h1 = find_result("price_h4", "delta_effective_new_business_headline", "supply_tightness")
    h1_q = find_result("price_h4", "delta_quoted_2y_75_ltv", "supply_tightness")
    h2 = find_result("transactions_h4", "delta_effective_new_business_headline", "supply_tightness")
    h3 = find_result("price_h4", "delta_effective_new_business_headline", "stock_tightness")
    h4 = find_result("price_h4", "delta_quoted_effective_spread_2y", "supply_tightness")
    h5_event_supply = [r for r in episode_rows if r["constraint"] == "supply_tightness"]

    hypotheses = [
        {
            "hypothesis": "H1",
            "test": "4Q real price response to effective and quoted mortgage-rate shocks interacted with supply tightness",
            "primary_result": f"effective beta={h1.get('beta', '')}, p={h1.get('p_value', '')}; quoted beta={h1_q.get('beta', '')}, p={h1_q.get('p_value', '')}",
            "confidence": "low" if h1.get("sign") == h1_q.get("sign") else "inconclusive",
            "interpretation": "Screening evidence is directional if both mortgage shock definitions agree; not publication-grade causal evidence.",
        },
        {
            "hypothesis": "H2",
            "test": "4Q transaction-count response to effective mortgage-rate shocks interacted with supply tightness",
            "primary_result": f"transaction beta={h2.get('beta', '')}, p={h2.get('p_value', '')}",
            "confidence": "low" if h2.get("significance") != "not_significant" else "inconclusive",
            "interpretation": "Transaction evidence is useful for liquidity stress, but registration lag makes timing cautious.",
        },
        {
            "hypothesis": "H3",
            "test": "4Q real price response to effective mortgage-rate shocks interacted with vacancy tightness",
            "primary_result": f"stock-tightness beta={h3.get('beta', '')}, p={h3.get('p_value', '')}",
            "confidence": "low" if h3.get("significance") != "not_significant" else "inconclusive",
            "interpretation": "Vacancy is a stock-buffer proxy; evidence should be read alongside supply-flow results.",
        },
        {
            "hypothesis": "H4",
            "test": "4Q real price response to quoted-effective spread shock interacted with supply tightness",
            "primary_result": f"spread beta={h4.get('beta', '')}, p={h4.get('p_value', '')}",
            "confidence": "low" if h4.get("significance") != "not_significant" else "inconclusive",
            "interpretation": "Spread results indicate whether friction/selection adds signal beyond rate levels.",
        },
        {
            "hypothesis": "H5",
            "test": "2021Q4-2024Q4 high-versus-low tightness episode comparison",
            "primary_result": "; ".join(
                f"{r['constraint']} Q{r['quartile']} price={r['real_price_change_pct']}%, tx={r['transaction_change_pct']}%"
                for r in h5_event_supply
            ),
            "confidence": "low",
            "interpretation": "Episode evidence is informative for the recent fixed-rate reset but not enough to establish stable long-run timing.",
        },
    ]

    quality_rows = []
    for row in join_rows:
        if int(row["transaction_year"]) >= 2015:
            quality_rows.append({
                "metric": f"postcode_match_rate_{row['transaction_year']}",
                "value": row["postcode_match_rate"],
                "note": "Current NSPL snapshot matched to PPD transaction postcodes.",
            })
    quality_rows.extend([
        {"metric": "lad_quarter_rows", "value": len(panel), "note": "England LAD-quarter cells from 2015Q1 onward."},
        {"metric": "lad_count", "value": len(lads), "note": "Distinct LADs in main panel."},
        {"metric": "quarter_count", "value": len(quarters), "note": f"{quarter_label(min(quarters))} to {quarter_label(max(quarters))}."},
        {"metric": "sparse_cells_lt_20_transactions", "value": sparse_cells, "note": "Cells below model inclusion threshold."},
        {"metric": "post2016_model_candidate_cells", "value": len(post2016_cells), "note": "Cells before horizon and sparse filtering."},
        {"metric": "static_constraint_lad_count", "value": len(static), "note": "LADs with 2013-2015 supply and vacancy proxies."},
        {"metric": "latest_quarter_in_extract", "value": quarter_label(max(quarters)), "note": "Most recent completed-sale quarter present in the local extract; treat as provisional until registration lag checks pass."},
    ])

    data_issue_rows = [
        {
            "data_issue": "Completed-sale timing and late registration",
            "mitigation": "Latest-quarter completeness audit, exclusion of outcomes ending in 2025Q4/2026Q1, lagged and cumulative mortgage-rate timings, and shifted episode windows.",
            "residual_risk": "Completion date can still lag price negotiation and mortgage arrangement; exact decision date is unobserved.",
            "confidence_effect": "Downgrades timing claims and recent-episode interpretation.",
        },
        {
            "data_issue": "Approximate median price and changing transaction composition",
            "mitigation": "Mean-log price robustness and property-mix controls using property type, tenure, and new-build shares.",
            "residual_risk": "No repeat-sales or hedonic adjustment; unobserved quality mix can remain.",
            "confidence_effect": "Keeps price findings low-confidence unless direction survives both checks.",
        },
        {
            "data_issue": "Current postcode geography applied to historical sales",
            "mitigation": "Postcode match-rate audit by transaction year and explicit NSPL-snapshot caveat.",
            "residual_risk": "Point-in-time geography reconstruction is not available in the current extract.",
            "confidence_effect": "Supports LAD-level screening but not fine-grained historical boundary claims.",
        },
        {
            "data_issue": "Annual supply/vacancy timing and definitions",
            "mitigation": "Predetermined 2013-2015 averages plus alternative 2015-only and completions-based constraint checks.",
            "residual_risk": "Supply and vacancy are annual, realized, and may be endogenous to local demand conditions.",
            "confidence_effect": "Constraint-sensitive results stay low-confidence.",
        },
        {
            "data_issue": "Local labour-market confounding",
            "mitigation": "Claimant metric level and 4Q change controls from the existing labour extract; the current extract falls back to claimant count where claimant rate is unavailable.",
            "residual_risk": "Claimant count is not population-normalized and is not a complete local-demand control.",
            "confidence_effect": "Findings that depend on labour-control inclusion are not treated as robust.",
        },
        {
            "data_issue": "Sparse LAD-quarter cells",
            "mitigation": "Baseline excludes cells below 20 transactions; robustness requires at least 50 transactions at both start and horizon.",
            "residual_risk": "Small or volatile local markets can still have noisy median prices.",
            "confidence_effect": "Sparse-sensitive results are treated cautiously.",
        },
        {
            "data_issue": "Observed mortgage rates are not exogenous shocks",
            "mitigation": "Multiple mortgage-rate definitions and timing conventions; conclusions framed as screening associations.",
            "residual_risk": "No MPC/OIS surprise instrument is included.",
            "confidence_effect": "Prevents causal monetary-policy claims.",
        },
    ]

    write_csv(OUT / "data-quality-summary.csv", quality_rows, ["metric", "value", "note"])
    write_csv(OUT / "latest-quarter-completeness.csv", latest_quarter_rows, ["quarter", "lad_cells", "total_transactions", "median_transactions_per_lad", "sparse_cells_lt_20_transactions", "same_quarter_prior_year_transactions", "transaction_change_vs_prior_year_pct", "note"])
    write_csv(OUT / "model-results.csv", model_results, ["outcome", "shock", "constraint", "n", "clusters", "beta", "cluster_se", "t_stat", "p_value", "sign", "significance"])
    write_csv(OUT / "lagged-shock-results.csv", lagged_rows, ["shock_timing", "outcome", "shock", "constraint", "n", "clusters", "beta", "cluster_se", "t_stat", "p_value", "note"])
    write_csv(OUT / "robustness-results.csv", robustness_results, ["robustness", "outcome", "shock", "constraint", "n", "clusters", "beta", "cluster_se", "t_stat", "p_value", "note"])
    write_csv(OUT / "data-issues-mitigation-summary.csv", data_issue_rows, ["data_issue", "mitigation", "residual_risk", "confidence_effect"])
    write_csv(OUT / "hypothesis-summary.csv", hypotheses, ["hypothesis", "test", "primary_result", "confidence", "interpretation"])
    write_csv(OUT / "constraint-quartile-summary.csv", quartile_rows, ["constraint", "quartile", "lad_count", "mean_net_additions_rate_pre", "mean_vacancy_rate_pre", "mean_long_term_vacancy_rate_pre"])
    write_csv(OUT / "episode-2022-2024-summary.csv", episode_rows, ["constraint", "quartile", "start_quarter", "end_quarter", "lad_count", "real_price_change_pct", "transaction_change_pct"])
    write_csv(OUT / "episode-lagged-window-summary.csv", episode_lagged_rows, ["window", "constraint", "quartile", "start_quarter", "end_quarter", "lad_count", "real_price_change_pct", "transaction_change_pct", "note"])

    mortgage_series = {
        "Effective new business": [(q, vals["effective_new_business_headline"]) for q, vals in sorted(mortgage.items()) if vals.get("effective_new_business_headline") is not None],
        "Quoted 2y 75 LTV": [(q, vals["quoted_2y_75_ltv_bv34"]) for q, vals in sorted(mortgage.items()) if vals.get("quoted_2y_75_ltv_bv34") is not None],
        "Quoted 5y 75 LTV": [(q, vals["quoted_5y_75_ltv_bv42"]) for q, vals in sorted(mortgage.items()) if vals.get("quoted_5y_75_ltv_bv42") is not None],
    }
    svg_line_chart(OUT / "figure-1-mortgage-rates.svg", "Mortgage rates used as national shocks", mortgage_series, "Percent")

    svg_line_chart(
        OUT / "figure-2-real-price-index-by-supply-tightness.svg",
        "Real completed-sale price index by supply-tightness quartile",
        {
            "Q1 loosest": indexed_price.get("supply tightness Q1", []),
            "Q4 tightest": indexed_price.get("supply tightness Q4", []),
        },
        "Index, 2016Q1 = 100",
    )
    svg_line_chart(
        OUT / "figure-3-transaction-index-by-supply-tightness.svg",
        "Transaction count index by supply-tightness quartile",
        {
            "Q1 loosest": indexed_tx.get("supply tightness Q1", []),
            "Q4 tightest": indexed_tx.get("supply tightness Q4", []),
        },
        "Index, 2016Q1 = 100",
    )
    svg_line_chart(
        OUT / "figure-4-real-price-index-by-stock-tightness.svg",
        "Real completed-sale price index by vacancy-tightness quartile",
        {
            "Q1 loosest": indexed_price.get("stock tightness Q1", []),
            "Q4 tightest": indexed_price.get("stock tightness Q4", []),
        },
        "Index, 2016Q1 = 100",
    )

    summary_md = [
        "# Analysis Results Summary",
        "",
        f"- Main LAD-quarter panel rows: `{len(panel):,}`.",
        f"- LADs in panel: `{len(lads):,}`.",
        f"- Quarters in panel: `{quarter_label(min(quarters))}` to `{quarter_label(max(quarters))}`.",
        f"- Sparse cells with fewer than 20 transactions: `{sparse_cells:,}`.",
        f"- LADs with static 2013-2015 supply and vacancy constraints: `{len(static):,}`.",
        "",
        "## Hypothesis Summary",
        "",
    ]
    for row in hypotheses:
        summary_md.append(f"- `{row['hypothesis']}` `{row['confidence']}`: {row['primary_result']}")
    summary_md.extend([
        "",
        "## Data Issue Mitigations",
        "",
    ])
    for row in data_issue_rows:
        summary_md.append(f"- `{row['data_issue']}`: {row['mitigation']} Residual risk: {row['residual_risk']}")
    summary_md.extend([
        "",
        "## Completed-Sale Timing Checks",
        "",
        "| Quarter | LAD cells | Transactions | Median transactions per LAD | Sparse cells | Change vs prior year |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ])
    for row in latest_quarter_rows:
        summary_md.append(
            f"| {row['quarter']} | {row['lad_cells']} | {row['total_transactions']} | {row['median_transactions_per_lad']} | {row['sparse_cells_lt_20_transactions']} | {row['transaction_change_vs_prior_year_pct']}% |"
        )
    summary_md.extend([
        "",
        "## Lagged Mortgage-Rate Results",
        "",
        "| Timing | Outcome | Shock | Constraint | Beta | SE | p-value | N |",
        "| --- | --- | --- | --- | ---: | ---: | ---: | ---: |",
    ])
    for row in lagged_rows:
        if row["outcome"] in {"price_h4", "transactions_h4"} and row["constraint"] in {"supply_tightness", "stock_tightness"} and row["shock"] in {"delta_effective_new_business_headline", "delta_quoted_2y_75_ltv"}:
            summary_md.append(
                f"| {row['shock_timing']} | {row['outcome']} | {row['shock']} | {row['constraint']} | {row['beta']} | {row['cluster_se']} | {row['p_value']} | {row['n']} |"
            )
    summary_md.extend([
        "",
        "## Robustness Results",
        "",
        "| Robustness | Outcome | Shock | Constraint | Beta | SE | p-value | N |",
        "| --- | --- | --- | --- | ---: | ---: | ---: | ---: |",
    ])
    for row in robustness_results:
        summary_md.append(
            f"| {row['robustness']} | {row['outcome']} | {row['shock']} | {row['constraint']} | {row['beta']} | {row['cluster_se']} | {row['p_value']} | {row['n']} |"
        )
    summary_md.extend([
        "",
        "## Primary Model Results",
        "",
        "| Outcome | Shock | Constraint | Beta | SE | p-value | N |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: |",
    ])
    for row in model_results:
        if row["outcome"] == "price_h4" and row["constraint"] in {"supply_tightness", "stock_tightness"}:
            summary_md.append(
                f"| {row['outcome']} | {row['shock']} | {row['constraint']} | {row['beta']} | {row['cluster_se']} | {row['p_value']} | {row['n']} |"
            )
    (OUT / "analysis-results-summary.md").write_text("\n".join(summary_md) + "\n")


if __name__ == "__main__":
    main()
