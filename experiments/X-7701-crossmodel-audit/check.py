#!/usr/bin/env python3
"""Independent exact checks for the Claude/Fable cross-model audit.

Standard library only. This checker deliberately covers only the finite
arithmetic interfaces named in the audit report; it is not a Collatz search.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


L0 = Fraction(176251, 111202)
U0 = Fraction(301994, 190537)


def ceil_fraction(x: Fraction) -> int:
    return -((-x.numerator) // x.denominator)


def admissible_mstar(floor: int, limit: int) -> tuple[int, int]:
    eps = Fraction(1000, 2079 * floor)
    for m in range(1, limit + 1):
        k_lo = ceil_fraction(m * L0)
        k_hi = ceil_fraction(m * U0)
        if k_lo != k_hi:
            raise AssertionError(f"enclosure does not determine ceil at m={m}")
        k = k_lo
        r = Fraction(k, m) - eps
        if L0 >= r:
            return m, k
        if not U0 <= r:
            raise AssertionError(f"enclosure does not decide admissibility at m={m}")
    raise AssertionError(f"no admissible m through {limit}")


def l9927_eliminations() -> tuple[list[int], int]:
    eliminated: list[int] = []
    numerator = 1
    denominator = 1
    power3 = 1
    threshold = 0
    for m in range(1, 1100):
        k = m - 1
        u = 3 * k + 7 + (k & 1)
        numerator *= 3 * u + 1
        denominator *= u
        power3 *= 3
        kappa = power3.bit_length()
        if (1 << kappa) * denominator > numerator:
            eliminated.append(m)
        if threshold == 0 and numerator >= 2 * power3 * denominator:
            threshold = m
    return eliminated, threshold


def cycle_window(m: int) -> list[int]:
    p3 = 3**m
    k = p3.bit_length()
    out: list[int] = []
    while (1 << k) * 7**m <= 22**m:
        out.append(k)
        k += 1
    return out


def divisibility_count(m: int, k: int) -> tuple[int, int]:
    d = (1 << k) - 3**m
    powers3 = [3**j for j in range(m)]
    powers2 = [pow(2, a, d) for a in range(k)]
    base = powers3[m - 1] % d
    total = 0
    hits = 0
    for partials in combinations(range(1, k), m - 1):
        c = base
        for j, a in enumerate(partials, start=1):
            c = (c + powers3[m - 1 - j] * powers2[a]) % d
        total += 1
        hits += c == 0
    return total, hits


def l9915_small_replay() -> tuple[list[dict[str, int]], int]:
    rows: list[dict[str, int]] = []
    total = 0
    for m in range(7, 15):
        for k in cycle_window(m):
            count, hits = divisibility_count(m, k)
            rows.append({"m": m, "K": k, "compositions": count, "divisibility_hits": hits})
            total += count
    return rows, total


def collatz_floor_sweep(limit: int = 10**6) -> dict[str, int]:
    steps: dict[int, int] = {1: 0}
    maximum = 0
    argmax = 1
    for n in range(1, limit + 1):
        x = n
        path: list[int] = []
        while x not in steps:
            path.append(x)
            x = x // 2 if x % 2 == 0 else 3 * x + 1
        length = steps[x]
        for y in reversed(path):
            length += 1
            steps[y] = length
        if steps[n] > maximum:
            maximum = steps[n]
            argmax = n
    return {
        "verified_through": limit,
        "maximum_total_stopping_time": maximum,
        "first_argmax": argmax,
    }


def parseval_counterexample(k: int = 8) -> dict[str, object]:
    modulus = 2**k
    d = modulus
    # D is the complete residue group. Its Fourier sum is d at v=0 and 0 elsewhere.
    mean_square = Fraction(d * d, modulus)
    small_density = Fraction(modulus - 1, modulus)
    assert mean_square == d
    return {
        "modulus": modulus,
        "digit_count": d,
        "mean_square": str(mean_square),
        "density_with_abs_g_at_most_1": str(small_density),
        "violating_density": str(Fraction(1, modulus)),
    }


def claude_error_absorption() -> dict[str, object]:
    # From 3 < pi < 4:
    #   1/2 < a=2/pi+1/81 < 55/81 < 7/10.
    # The submitted reciprocity error is <4/32^K.
    # For K>=7, the gap (7/10)^r-a^r is bounded below by
    # (17/810)*2^(-(r-1)) >= (17/810)*2^(-(K-1)).
    k = 7
    error_upper = Fraction(4, 32**k)
    gap_lower = Fraction(17, 810) * Fraction(1, 2 ** (k - 1))
    assert Fraction(55, 81) < Fraction(7, 10)
    assert error_upper < gap_lower
    return {
        "replacement_constant": "7/10",
        "first_feasible_K_checked": k,
        "error_upper": str(error_upper),
        "gap_lower": str(gap_lower),
    }


def build_payload() -> dict[str, object]:
    m1 = admissible_mstar(10**6, 2966)
    m2 = admissible_mstar(10**9, 47468)
    eliminated, threshold = l9927_eliminations()
    rows, small_total = l9915_small_replay()
    assert m1 == (2966, 4701)
    assert m2 == (47468, 75235)
    assert len(eliminated) == 166
    assert max(eliminated) == 1024
    assert threshold == 1039
    assert small_total == 648635
    assert all(row["divisibility_hits"] == 0 for row in rows)
    elimination_digest = hashlib.sha256(",".join(map(str, eliminated)).encode()).hexdigest()
    payload: dict[str, object] = {
        "experiment": "X-7701",
        "frozen_sources": {
            "claude_symbolic": "407a788972a72da2fde59c19e9446e02647cc4f4",
            "fable_foundry_cone": "0888a211f2703f5d3082e60fcbd0e8002b4b4650",
            "fable_foundations": "2cb80b4629ebfde5c8aaa3433c38e1382ea956b7",
        },
        "claude_reciprocity_repair": claude_error_absorption(),
        "l9913_floor_replay": collatz_floor_sweep(),
        "l9913": {
            "F_1e6": {"m_star": m1[0], "K": m1[1]},
            "F_1e9": {"m_star": m2[0], "K": m2[1]},
        },
        "l9915_crossmodel_partial_replay": {
            "scope": "m=7..14 only",
            "rows": rows,
            "total_compositions": small_total,
            "total_divisibility_hits": 0,
        },
        "l9927": {
            "eliminated_count": len(eliminated),
            "maximum_eliminated_m": max(eliminated),
            "first_permanent_nonempty_threshold": threshold,
            "elimination_list_sha256": elimination_digest,
        },
        "l9918_parseval_counterexample": parseval_counterexample(),
        "limitations": [
            "does not replay L-9915 for m=15..21",
            "does not replay T-9925 memory-bound phase-floor certificates",
            "does not prove any Collatz orbit statement",
        ],
    }
    semantic = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    payload["semantic_digest"] = semantic
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    parser.add_argument("--check-results")
    args = parser.parse_args()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(text)
    if args.check_results:
        expected = json.loads(Path(args.check_results).read_text())
        if payload != expected:
            raise SystemExit("result mismatch")
    print(text, end="")


if __name__ == "__main__":
    main()
