#!/usr/bin/env python3
"""Independent exact verifier for X-9605 canonical output."""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Iterator, Sequence

TYPE_VALUES = {
    "1^7": (1,) * 7,
    "1^6,3": (1,) * 6 + (3,),
    "1^6,4": (1,) * 6 + (4,),
    "1^6,5": (1,) * 6 + (5,),
    "1^5,3,3": (1,) * 5 + (3, 3),
}


def bars(total: int, parts: int) -> Iterator[tuple[int, ...]]:
    """Stars-and-bars using separator positions, independent of run.py recursion."""
    for cuts in itertools.combinations(range(total + parts - 1), parts - 1):
        points = (-1,) + cuts + (total + parts - 1,)
        yield tuple(points[i + 1] - points[i] - 1 for i in range(parts))


def arrangements(kind: str) -> Iterator[tuple[int, ...]]:
    if kind == "1^7":
        yield (1,) * 7
    elif kind.startswith("1^6,"):
        high = int(kind.split(",")[1])
        for position in range(7):
            row = [1] * 7
            row[position] = high
            yield tuple(row)
    else:
        for first, second in itertools.combinations(range(7), 2):
            row = [1] * 7
            row[first] = row[second] = 3
            yield tuple(row)


def direct_cd(word: Sequence[int]) -> tuple[int, int]:
    prefix = 0
    c = 0
    k = len(word)
    for index, valuation in enumerate(word):
        c += 3 ** (k - 1 - index) * 2**prefix
        prefix += valuation
    return c, 2**prefix - 3**k


def sparse_e(word: Sequence[int]) -> int:
    prefix = 0
    total = 0
    k = len(word)
    for index, valuation in enumerate(word):
        total += 3 ** (k - 1 - index) * 2**prefix * (4 - 2**valuation)
        prefix += valuation
    return total


def reconstruct_rows(payload: dict[str, object]) -> list[dict[str, object]]:
    expected_rows = payload["finite_rows"]
    assert isinstance(expected_rows, list)
    ranges: dict[str, list[int]] = {}
    for row in expected_rows:
        assert isinstance(row, dict)
        ranges.setdefault(str(row["type"]), []).append(int(row["R"]))

    rows: list[dict[str, object]] = []
    for kind in TYPE_VALUES:
        values = TYPE_VALUES[kind]
        for neutral_count in ranges[kind]:
            d = 2 ** sum(values) * 4**neutral_count - 3**7 * 3**neutral_count
            count = 0
            maximum = None
            height = 0
            rho = None
            for gaps in bars(neutral_count, 7):
                if gaps[-1] != max(gaps):
                    continue
                for exceptional in arrangements(kind):
                    count += 1
                    core: list[int] = []
                    for index, valuation in enumerate(exceptional):
                        core.append(valuation)
                        if index < 6:
                            core.extend([2] * gaps[index])
                    c_core, d_core = direct_cd(core)
                    e_core = c_core - d_core
                    if e_core != sparse_e(core):
                        raise AssertionError("direct/sparse mismatch")
                    maximum = e_core if maximum is None else max(maximum, e_core)
                    if e_core % d == 0:
                        full_word = core + [2] * gaps[-1]
                        c_full, d_full = direct_cd(full_word)
                        if d_full != d or c_full % d != 0:
                            raise AssertionError("neutral-tail divisibility mismatch")
                        start = c_full // d
                        raise AssertionError(f"unexpected cycle hit at {start}")
                    if e_core >= 2 * d:
                        height += 1
                        remainder = e_core % d
                        circular = min(remainder, d - remainder)
                        rho = circular if rho is None else min(rho, circular)
            rows.append(
                {
                    "type": kind,
                    "R": neutral_count,
                    "D": d,
                    "largest_gap_candidates": count,
                    "max_E_core": maximum,
                    "height_survivors": height,
                    "least_nonzero_circular_remainder": rho,
                }
            )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("canonical", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.canonical.read_text(encoding="utf-8"))
    rows = reconstruct_rows(payload)
    if rows != payload["finite_rows"]:
        raise SystemExit("independent finite rows differ from canonical payload")
    totals = payload["totals"]
    assert isinstance(totals, dict)
    if sum(int(row["largest_gap_candidates"]) for row in rows) != int(totals["largest_gap_candidates"]):
        raise SystemExit("candidate total mismatch")
    if sum(int(row["height_survivors"]) for row in rows) != int(totals["height_survivors"]):
        raise SystemExit("height-survivor total mismatch")
    if int(totals["formal_divisor_hits"]) != 0:
        raise SystemExit("canonical payload unexpectedly records a hit")
    print("independent X-9605 verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
