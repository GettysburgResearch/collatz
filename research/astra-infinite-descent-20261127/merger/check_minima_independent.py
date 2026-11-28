"""Literal independent replay of both minimum dates and tie choices on 16 supplied rows.

Each gap gets its own modular power and both trajectories advance one step at a
time through the entire supplied paid horizon. The report selection is by
smallest absolute paid horizon, with input order breaking equal horizons.
"""
import csv
import json
import re
from pathlib import Path


def pinned_prices(price_file):
    text = price_file.read_text()
    rows = text.split("private def rows : Array Row := #[", 1)[1].split("]", 1)[0]
    pattern = r"⟨(\d+), (\d+), (\d+), (\d+), (\d+), (\d+)⟩"
    values = [int(row[2]) + int(row[3]) for row in re.findall(pattern, rows)]
    if len(values) != 81:
        raise ValueError("expected the pinned 81 prices")
    return values


def first_meeting(upper, lower, gap, horizon):
    upper_grade = lower_grade = 0
    first = None
    for clock in range(1, horizon + 1):
        upper_odd = upper % 2
        lower_odd = lower % 2
        upper_grade += upper_odd
        lower_grade += lower_odd
        upper = (3 * upper + 1) // 2 if upper_odd else upper // 2
        lower = (3 * lower + 1) // 2 if lower_odd else lower // 2
        if first is None and upper == lower and lower_grade == gap + upper_grade:
            first = clock
    return first


def check_row(row, costs):
    k, any_extra, any_gap, any_saving, paid_extra, paid_gap, paid_saving = row
    j = 18 * k + 4
    horizon = j + paid_extra
    modulus = 1 << horizon
    m = (12 << (18 * k)) - 1
    if m < 4 * horizon + 4:
        raise ValueError(("height guard", k))
    hits = []
    for d in range(1, horizon):
        exponent = m - d
        residue = pow(3, exponent, modulus)
        first = first_meeting(3 ** d * residue - 1, residue - 1, d, horizon)
        if first is not None:
            price = costs[((exponent - 1) // 2) % 81]
            hits.append((first, price - d, d))

    paid_hits = [hit for hit in hits if hit[1] <= 0]
    if not hits or min(hits) != (j + any_extra, -any_saving, any_gap):
        raise ValueError(("unrestricted first date or tie choice", k))
    if not paid_hits or min(paid_hits) != (j + paid_extra, -paid_saving, paid_gap):
        raise ValueError(("paid first date or tie choice", k))
    possible_gaps = horizon - 1
    all_ties = sum(clock == horizon for clock, _, _ in hits) > 1
    paid_ties = sum(clock == horizon for clock, _, _ in paid_hits) > 1
    return possible_gaps, horizon * possible_gaps, all_ties, paid_ties


def main():
    source = Path(__file__).resolve().parents[1]
    report = source.parents[1] / "reports" / source.name / "merger" / "SUPPLIED_MINIMA.csv"
    with report.open(newline="") as stream:
        reader = csv.reader(stream)
        expected = "k any_extra any_gap any_saving paid_extra paid_gap paid_saving".split()
        if next(reader) != expected:
            raise ValueError("unexpected table header")
        rows = [list(map(int, row)) for row in reader]
    if len(rows) != 192 or any(len(row) != 7 or row[0] != k for k, row in enumerate(rows, 1)):
        raise ValueError("incomplete or unordered supplied rows")
    chosen = sorted(rows, key=lambda row: 18 * row[0] + 4 + row[4])[:16]
    costs = pinned_prices(source / "imports" / "pr206" / "ReturnDescentRows.lean")
    results = [check_row(row, costs) for row in chosen]
    print(json.dumps({
        "supplied_k": [row[0] for row in chosen],
        "examined_gaps": sum(entry[0] for entry in results),
        "complete_scalar_clock_pairs": sum(entry[1] for entry in results),
        "rows_with_multiple_gaps_at_first_paid_clock": sum(entry[2] for entry in results),
        "rows_with_multiple_paid_gaps_at_first_paid_clock": sum(entry[3] for entry in results),
    }, indent=2))


if __name__ == "__main__":
    main()
