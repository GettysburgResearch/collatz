#!/usr/bin/env python3
"""Exact full-denominator zero count by ordinary cycle minima.

Default controls compare all periods 1..18 with exhaustive word counts.
--large-fiber-control also counts the complete (27,17) residue law.
No external mathematics package or logarithmic-form estimate is used.
"""

from __future__ import annotations

import argparse
from array import array
from collections import Counter
import hashlib
from itertools import combinations
import json
from math import comb, gcd
from pathlib import Path
import time


def step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def numerator(positions: tuple[int, ...]) -> int:
    p = len(positions)
    return sum(3 ** (p - 1 - i) * 2 ** d for i, d in enumerate(positions))


def minimum_bound(A: int, p: int) -> int:
    if not 1 <= p <= A:
        raise ValueError("Expected 1 <= p <= A")
    D = 2 ** A - 3 ** p
    if D <= 0:
        raise ValueError("Expected the positive full denominator 2^A-3^p")
    return (p * 2 ** A - D) // (3 * D)


def zero_count_by_minima(A: int, p: int) -> tuple[int, list[dict]]:
    bound = minimum_bound(A, p)
    count = 0
    certificates = []
    for m in range(1, bound + 1):
        if gcd(m, 6) != 1:
            continue
        x = m
        odds = 0
        path = []
        for ell in range(1, A + 1):
            path.append(x)
            odds += x % 2
            x = step(x)
            if x < m:
                break
            if x == m:
                if A % ell == 0 and odds * (A // ell) == p:
                    count += ell
                    certificates.append({"minimum": m, "period": ell,
                                         "odd_count": odds, "cycle": path})
                break
    return count, certificates


def direct_word_count(A: int, p: int) -> int:
    D = 2 ** A - 3 ** p
    return sum(numerator(pos) % D == 0 for pos in combinations(range(A), p))


def residue_control(A: int = 27, p: int = 17) -> dict:
    """Complete meet-in-the-middle enumeration, with no random sampling."""
    D = 2 ** A - 3 ** p
    h = A // 2
    counts = array("I", [0]) * D
    for lo_p in range(max(0, p - (A - h)), min(h, p) + 1):
        hi_p = p - lo_p
        lo = [3 ** hi_p * numerator(pos)
              for pos in combinations(range(h), lo_p)]
        hi = [2 ** h * numerator(pos)
              for pos in combinations(range(A - h), hi_p)]
        for left in lo:
            for right in hi:
                counts[(left + right) % D] += 1
    W = comb(A, p)
    assert sum(counts) == W
    maximum = max(counts)
    maximizing = [r for r, v in enumerate(counts) if v == maximum]
    direct_minimum_count, certs = zero_count_by_minima(A, p)
    assert counts[0] == direct_minimum_count
    return {"A": A, "p": p, "D": D, "word_count": W,
            "zero_count": counts[0], "maximum_fiber": maximum,
            "maximizing_residues": maximizing,
            "minimum_bound": minimum_bound(A, p),
            "cycle_certificates": certs}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-period", type=int, default=18)
    parser.add_argument("--large-fiber-control", action="store_true")
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    start = time.monotonic()
    rows = []
    total_words = 0
    for A in range(1, args.max_period + 1):
        for p in range(1, A + 1):
            D = 2 ** A - 3 ** p
            if D <= 0:
                continue
            actual, certificates = zero_count_by_minima(A, p)
            direct = direct_word_count(A, p)
            assert actual == direct, (A, p, actual, direct)
            bound = minimum_bound(A, p)
            candidates = sum(gcd(m, 6) == 1 for m in range(1, bound + 1))
            assert direct <= A * candidates
            for cert in certificates:
                assert D * (3 * cert["minimum"] + 1) <= p * 2 ** A
            W = comb(A, p)
            total_words += W
            rows.append({"A": A, "p": p, "D": D,
                         "word_count": W, "zero_count": direct,
                         "minimum_bound": bound,
                         "cycle_certificates": certificates})
    result = {"status": "PASSED", "max_period": args.max_period,
              "parameter_pairs": len(rows), "words_enumerated": total_words,
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "scope": "Finite algorithm controls only; no unrestricted cycle exclusion.",
              "parameters": rows}
    if args.large_fiber_control:
        result["large_fiber_control"] = residue_control()
    result["elapsed_seconds"] = round(time.monotonic() - start, 3)
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "parameters"}, indent=2))


if __name__ == "__main__":
    main()
