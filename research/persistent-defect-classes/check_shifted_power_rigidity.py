#!/usr/bin/env python3
"""Exact finite interface checks; no extrapolation to universal mergers."""
from collections import defaultdict
import json


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def record(k, c, horizon):
    source = 3**k + c
    n, odds = source, 0
    out = []
    for p in range(horizon + 1):
        offset = 2**p * n - 3**odds * source
        assert 0 <= offset <= 3**p - 2**p
        shifted = 3**odds * c + offset
        out.append((k, c, p, odds, shifted, n))
        odds += n % 2
        n = step(n)
    return out


def at(k, c, p):
    return record(k, c, p)[-1]


def main():
    endpoints = defaultdict(list)
    for k in range(1, 19):
        for c in range(3):
            for rec in record(k, c, 40):
                endpoints[rec[-1]].append(rec)
    pairs = homogeneous = asynchronous = propagated = 0
    for bucket in endpoints.values():
        for i, left in enumerate(bucket):
            for right in bucket[i + 1:]:
                k, c, p, a, d1, _ = left
                l, d, q, b, d2, _ = right
                if (k, c) == (l, d):
                    continue
                L, N = max(p, q), min(k + a, l + b)
                identity = p == q and k + a == l + b and d1 == d2
                assert identity or L >= N, (left, right)
                if p != q:
                    assert L >= min(k, l)
                    asynchronous += 1
                if L < k and k == l:
                    assert p == q and a == b
                pairs += 1
                homogeneous += identity
                # Avoid exponential-sized replay integers for large L.
                # This is a bounded replay of the proved progression rule.
                if identity and L <= 6:
                    period = 1 if L <= 1 else 2 if L == 2 else 2 ** (L - 2)
                    new_left = at(k + period, c, p)
                    new_right = at(l + period, d, q)
                    assert new_left[3] == a and new_right[3] == b
                    assert new_left[-1] == new_right[-1]
                    propagated += 1
    assert pairs and homogeneous and asynchronous and propagated
    print(json.dumps({
        "status": "PASS", "exponent_range": [1, 18],
        "shifts": [0, 1, 2], "clock_max": 40,
        "actual_merger_pairs_checked": pairs,
        "homogeneous_pairs": homogeneous,
        "unequal_clock_pairs": asynchronous,
        "exponent_progression_replays_clock_at_most_6": propagated,
        "scope": "Finite arithmetic interfaces only; the written divisibility proof "
                 "establishes the all-parameter dichotomy, not universal merging.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
