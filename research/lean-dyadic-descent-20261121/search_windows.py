#!/usr/bin/env python3
"""Discover exact marked-return certificates; this is not a Collatz proof.

All comparisons are integer comparisons.  Each output interval represents
every exponent in that interval through the algebraic window theorem in
MarkedOffsetReturn.lean; the Python search is only a certificate generator.
The selected offsets and exponent windows do not claim universal coverage.
"""

import argparse
import json
from pathlib import Path


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def certificate(r, limit):
    n, odds = r, 0
    for t in range(limit + 1):
        if n == 1:
            return t, odds
        odds += n % 2
        n = step(n)
    return None


def merge(intervals):
    merged = []
    for lo, hi in sorted(intervals):
        if merged and lo <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo, hi])
    return merged


def windows(r, cert, max_q):
    t, p = cert
    source_min = 1
    while r >= 2**source_min or (source_min + 1) * r > 70 * 2**source_min:
        source_min += 1
    rows = []
    for q in range(max(1, p), max_q + 1):
        s = q - p
        clock = t + 2 * s
        three = 3**q
        if three >= 2**clock:
            continue
        a = three.bit_length() - 1
        gap = three - 2**a
        e_max = (70 * 2**a) // (gap + 1) - a - 1
        e_min = max(1, source_min - clock)
        if e_min > e_max:
            continue
        d_min, d_max = clock + e_min, clock + e_max
        # Exact end checks for the theorem's monotone window hypotheses.
        if not (2**a <= three < 2 ** (a + 1)):
            raise ArithmeticError("incorrect binary exponent")
        if not ((a + e_max + 1) * (gap + 1) <= 70 * 2**a):
            raise ArithmeticError("endpoint band certificate failed")
        if not (r < 2**d_min and (d_min + 1) * r <= 70 * 2**d_min):
            raise ArithmeticError("source band certificate failed")
        rows.append({"q": q, "a": a, "s": s, "clock": clock,
                     "e_min": e_min, "e_max": e_max,
                     "d_min": d_min, "d_max": d_max})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offsets", default="1,3,5,7,27,31,127")
    parser.add_argument("--max-q", type=int, default=4096)
    parser.add_argument("--offset-clock-limit", type=int, default=10000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_q < 1 or args.offset_clock_limit < 0:
        parser.error("the search bounds must be nonnegative, with max-q positive")
    offsets = [int(v) for v in args.offsets.split(",")]
    if any(r < 1 or r % 2 != 1 for r in offsets):
        parser.error("offsets must be positive odd integers")
    results = []
    for r in offsets:
        cert = certificate(r, args.offset_clock_limit)
        if cert is None:
            results.append({"offset": r, "status": "UNRESOLVED at selected clock bound"})
            continue
        rows = windows(r, cert, args.max_q)
        results.append({"offset": r, "offset_clock": cert[0], "offset_odds": cert[1],
                        "window_count": len(rows),
                        "covered_exponent_intervals": merge((x["d_min"], x["d_max"]) for x in rows),
                        "windows": rows})
    data = {"scope": "exact arithmetic certificate search on selected offsets and bounded q; not universal Collatz",
            "max_q": args.max_q, "offset_clock_limit": args.offset_clock_limit,
            "source_formula": "n = 2^d + r", "endpoint_formula": "y = 3^q * 2^(d-clock) + 1",
            "results": results}
    rendered = json.dumps(data, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
