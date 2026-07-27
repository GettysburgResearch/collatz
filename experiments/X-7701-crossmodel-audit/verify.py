#!/usr/bin/env python3
"""Separate exact verifier for X-7701; does not import check.py."""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

LOW = Fraction(176251, 111202)
HIGH = Fraction(301994, 190537)


def ceil_q(q: Fraction) -> int:
    return (q.numerator + q.denominator - 1) // q.denominator


def first_admissible(F: int, stop: int) -> tuple[int, int]:
    eps = Fraction(1000, 2079 * F)
    for m in range(1, stop + 1):
        kl = ceil_q(m * LOW)
        ku = ceil_q(m * HIGH)
        assert kl == ku
        r = Fraction(kl, m) - eps
        if LOW >= r:
            return m, kl
        assert HIGH <= r
    raise AssertionError


def floor_sweep(limit: int = 10**6) -> tuple[int, int]:
    lengths: dict[int, int] = {1: 0}
    best = 0
    first = 1
    for start in range(1, limit + 1):
        x = start
        trail: list[int] = []
        while x not in lengths:
            trail.append(x)
            if x & 1:
                x = 3 * x + 1
            else:
                x >>= 1
        value = lengths[x]
        while trail:
            y = trail.pop()
            value += 1
            lengths[y] = value
        if lengths[start] > best:
            best = lengths[start]
            first = start
    return best, first


def windows(m: int) -> list[int]:
    lo = (3**m).bit_length()
    result = []
    k = lo
    while (1 << k) * (7**m) <= 22**m:
        result.append(k)
        k += 1
    return result


def recurse_compositions(m: int, K: int) -> tuple[int, int]:
    """Independent DFS over parts rather than combinations of partial sums."""
    mod = (1 << K) - 3**m
    three = [3**j for j in range(m)]
    total = hits = 0

    def dfs(pos: int, remaining: int, partial_A: int, residue: int) -> None:
        nonlocal total, hits
        if pos == m - 1:
            if remaining < 1:
                return
            total += 1
            if residue % mod == 0:
                hits += 1
            return
        max_part = remaining - (m - pos - 1)
        for part in range(1, max_part + 1):
            new_A = partial_A + part
            coeff_exp = m - 2 - pos
            new_residue = (residue + three[coeff_exp] * pow(2, new_A, mod)) % mod
            dfs(pos + 1, remaining - part, new_A, new_residue)

    dfs(0, K, 0, three[m - 1] % mod)
    return total, hits


def l9927() -> tuple[int, int, int]:
    num = den = p3 = 1
    count = maximum = threshold = 0
    for m in range(1, 1100):
        idx = m - 1
        u = 3 * idx + 7 + idx % 2
        num *= 3 * u + 1
        den *= u
        p3 *= 3
        kappa = p3.bit_length()
        if (1 << kappa) * den > num:
            count += 1
            maximum = m
        if threshold == 0 and num >= 2 * p3 * den:
            threshold = m
    return count, maximum, threshold


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py results/canonical.json")
    payload = json.loads(Path(sys.argv[1]).read_text())
    assert payload["experiment"] == "X-7701"
    assert first_admissible(10**6, 2966) == (2966, 4701)
    assert first_admissible(10**9, 47468) == (47468, 75235)
    assert floor_sweep() == (524, 837799)
    assert payload["l9913_floor_replay"] == {
        "verified_through": 10**6,
        "maximum_total_stopping_time": 524,
        "first_argmax": 837799,
    }
    assert l9927() == (166, 1024, 1039)

    expected_rows = []
    total = 0
    for m in range(7, 15):
        for K in windows(m):
            n, h = recurse_compositions(m, K)
            expected_rows.append({"m": m, "K": K, "compositions": n, "divisibility_hits": h})
            total += n
    assert expected_rows == payload["l9915_crossmodel_partial_replay"]["rows"]
    assert total == 648635
    assert all(row["divisibility_hits"] == 0 for row in expected_rows)

    c = payload["claude_reciprocity_repair"]
    assert Fraction(c["replacement_constant"]) == Fraction(7, 10)
    assert Fraction(c["error_upper"]) < Fraction(c["gap_lower"])

    p = payload["l9918_parseval_counterexample"]
    q = int(p["modulus"])
    assert int(p["digit_count"]) == q
    assert Fraction(p["mean_square"]) == q
    assert Fraction(p["density_with_abs_g_at_most_1"]) == Fraction(q - 1, q)
    assert Fraction(p["violating_density"]) == Fraction(1, q)
    print("X-7701 independent verification passed")


if __name__ == "__main__":
    main()
