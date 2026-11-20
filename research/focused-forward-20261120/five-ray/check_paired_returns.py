#!/usr/bin/env python3
"""Exact certificates and a total partial ordinary five-ray reduction guard."""

import argparse
import json
from fractions import Fraction as F

if not __debug__:
    raise SystemExit("Refusing optimized execution: exact checks require assertions")


def step(n):
    assert n > 0
    return (3 * n + 1) // 2 if n & 1 else n // 2


def path(n, clock):
    values, counts, word = [n], [0], []
    for _ in range(clock):
        odd = n & 1
        word.append(odd)
        n = step(n)
        values.append(n)
        counts.append(counts[-1] + odd)
    return values, counts, tuple(word)


def affine_prefix(a, b, clock):
    """Uniform positive-lift path on a*v+b, when all exposed slopes are even."""
    states, counts, word = [(a, b)], [0], []
    for _ in range(clock):
        assert a % 2 == 0 and b > 0
        odd = b & 1
        word.append(odd)
        a, b = ((3 * a // 2, (3 * b + 1) // 2)
                if odd else (a // 2, b // 2))
        states.append((a, b))
        counts.append(counts[-1] + odd)
    return states, counts, tuple(word)


def meeting(n, clock):
    lower = path(n, clock)[0]
    upper = path(5 * n + 1, clock)[0]
    first_upper = {}
    for j, value in enumerate(upper):
        first_upper.setdefault(value, j)
    for i, value in enumerate(lower):
        if value in first_upper:
            return {"lower_clock": i, "upper_clock": first_upper[value],
                    "endpoint": value}
    return None


def reduce_once(n):
    assert n > 0
    residue = n % 64
    if residue == 11:
        v = (n - 11) // 64
        smaller, rule = 27 * v + 5, "forward_6_odd3"
    elif residue == 35:
        v = (n - 35) // 64
        smaller, rule = 9 * v + 5, "forward_6_odd2"
    elif n % 729 == 410:
        v = (n - 410) // 729
        smaller, rule = 512 * v + 287, "inverse_9_odd6"
    else:
        return None
    assert 0 < smaller < n and v >= 0
    return {"from": n, "to": smaller, "rule": rule, "lift": v}


def guard(n, clock):
    if n <= 0 or clock < 0:
        raise ValueError("positive start and nonnegative clock required")
    original, reductions = n, []
    while True:
        certificate = meeting(n, clock)
        if certificate is not None:
            return {"status": "MERGER_CERTIFIED", "original": original,
                    "terminal": n, "clock_budget": clock,
                    "reductions": reductions, "meeting": certificate}
        reduction = reduce_once(n)
        if reduction is None:
            return {"status": ("REDUCED_UNRESOLVED" if reductions
                               else "UNRESOLVED"),
                    "original": original, "terminal": n,
                    "clock_budget": clock, "reductions": reductions}
        reductions.append(reduction)
        n = reduction["to"]


def check_six_bit_classification():
    cells, hits = 0, []
    for h in range(1, 7):
        # 2**h is the positive representative of the zero binary class.
        for r in range(1, 2**h + 1):
            lower, lp, _ = affine_prefix(2**h, r, h)
            upper, up, _ = affine_prefix(5 * 2**h, 5 * r + 1, h)
            cells += 1
            if lp[-1] == up[-1]:
                a, b = lower[-1]
                c, d = upper[-1]
                assert c == 5 * a
                if d == 5 * b + 1:
                    hits.append((h, r % 2**h, b, lp[-1]))
    assert cells == 126
    assert hits == [(6, 11, 5, 3), (6, 35, 5, 2)]
    expected = ((11, 27, "110100", "000111", 3),
                (35, 9, "110000", "000011", 2))
    for r, slope, lw, uw, odds in expected:
        lo, lp, a = affine_prefix(64, r, 6)
        hi, hp, b = affine_prefix(320, 5 * r + 1, 6)
        assert lo[-1] == (slope, 5)
        assert hi[-1] == (5 * slope, 26)
        assert "".join(map(str, a)) == lw
        assert "".join(map(str, b)) == uw
        assert lp[-1] == hp[-1] == odds
    return cells, hits


def check_expanding_return():
    lo, lp, lw = affine_prefix(512, 287, 9)
    hi, hp, hw = affine_prefix(2560, 1436, 9)
    expected_lo = [(512, 287), (768, 431), (1152, 647), (1728, 971),
                   (2592, 1457), (3888, 2186), (1944, 1093),
                   (2916, 1640), (1458, 820), (729, 410)]
    expected_hi = [(2560, 1436), (1280, 718), (640, 359), (960, 539),
                   (1440, 809), (2160, 1214), (1080, 607),
                   (1620, 911), (2430, 1367), (3645, 2051)]
    assert lo == expected_lo and hi == expected_hi
    assert "".join(map(str, lw)) == "111110100"
    assert "".join(map(str, hw)) == "001110111"
    assert lp[-1] == hp[-1] == 6
    for i in range(1, 9):
        a, b = lo[i]
        c, d = hi[i]
        assert c - 5 * a < 0 and d - 5 * b - 1 < 0
    assert hi[-1] == (5 * lo[-1][0], 5 * lo[-1][1] + 1)
    comparisons = 0
    for a, b in lo:
        for c, d in hi:
            assert (a - c) * (b - d) > 0
            assert F(d - b, a - c) < 0
            comparisons += 1
    ordered = sorted(lo + hi)
    assert all(a < c and b < d for (a, b), (c, d)
               in zip(ordered, ordered[1:]))
    assert comparisons == 100
    assert 729 > 512 and 410 > 287
    assert 512 * 410 - 729 * 287 == 697
    return comparisons


def check_target_gate_regression():
    # Finite replay protects the formulas; the all-time theorem is written.
    replays = hits = 0
    for n in range(1, 2049):
        lo = path(n, 32)[0]
        hi = path(5 * n + 1, 32)[0]
        for h in range(1, 33):
            replays += 1
            if hi[h] == 5 * lo[h] + 1:
                assert lo[h] % 3 == 2
                hits += 1
    # Dropping the equal-clock hypothesis is false on ordinary positive paths.
    assert path(19, 14)[0][-1] == 1
    assert path(96, 4)[0][-1] == 6
    return replays, hits


def check_guard():
    replays = 0
    for v in range(128):
        for n, smaller, physical_source, physical_target, h in (
            (64 * v + 11, 27 * v + 5, 64 * v + 11, 27 * v + 5, 6),
            (64 * v + 35, 9 * v + 5, 64 * v + 35, 9 * v + 5, 6),
            (729 * v + 410, 512 * v + 287,
             512 * v + 287, 729 * v + 410, 9),
        ):
            assert 0 < smaller < n
            lo, lp, _ = path(physical_source, h)
            hi, hp, _ = path(5 * physical_source + 1, h)
            assert lo[-1] == physical_target
            assert hi[-1] == 5 * physical_target + 1
            assert lp[-1] == hp[-1]
            assert reduce_once(n) is not None
            replays += 1
    period = 64 * 729
    covered = sum(reduce_once(n) is not None for n in range(1, period + 1))
    assert period == 46656 and covered == 1520
    assert F(covered, period) == F(95, 2916)
    assert guard(2, 8)["status"] == "UNRESOLVED"
    assert guard(2, 9)["status"] == "MERGER_CERTIFIED"
    result = guard(410, 9)
    assert result["status"] == "REDUCED_UNRESOLVED"
    assert result["terminal"] == 287
    assert len(result["reductions"]) == 1
    assert guard(287, 9)["status"] == "UNRESOLVED"
    return replays, covered, period


def valuation(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def scaling_weight(n):
    return valuation(n, 2) + 2 * valuation(n, 3) + 2 * valuation(n, 5)


def check_conditional_identities():
    # Check only the physical paths used under hypothesis U, not U itself.
    paths = 0
    for x in range(1, 100, 2):
        if x % 3 == 0:
            continue
        for a in range(1, 9):
            assert path(5 * 4**a * x + 1, 2 * a)[0][-1] == 5 * 3**a * x + 1
            z = 5 * 3**(a - 1) * x
            assert z % 2 == 1
            assert step(z) == step(3 * z + 1)
            paths += 1
    for h in range(1, 2049):
        assert path(4 * h + 1, 2)[0][-1] == 3 * h + 1
        if h % 3 != 2:
            assert (4 * h + 1) % 3 != 0
        assert 3 * 5 * (16 * h + 1) + 1 == 16 * (15 * h + 1)
        assert scaling_weight(4 * h) == scaling_weight(3 * h)
        assert scaling_weight(16 * h) == scaling_weight(15 * h)
        assert scaling_weight(10 * h) == scaling_weight(9 * h) - 1
        assert scaling_weight(2 * h) == scaling_weight(h) + 1
    return paths, 2048


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int)
    parser.add_argument("--clock", type=int, default=9)
    args = parser.parse_args()
    if args.start is not None:
        print(json.dumps(guard(args.start, args.clock), indent=2))
        return
    print("SIX-BIT CLASSIFICATION", check_six_bit_classification())
    print("INDEPENDENT-CLOCK AFFINE COMPARISONS", check_expanding_return())
    print("TARGET-GATE REGRESSIONS", check_target_gate_regression())
    print("GUARD REPLAYS / COVERED / PERIOD", check_guard())
    print("CONDITIONAL PATHS / SCALING-MODEL REPLAYS", check_conditional_identities())
    print("PASS: ordinary certificates and partial guard; universal coverage remains open")


if __name__ == "__main__":
    main()
