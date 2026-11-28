#!/usr/bin/env python3
"""Exact bounded controls for the native source-population recursion.

The controls use genuine positive integer trajectories and retain both the
odd-departure count and the physical endpoint. They do not verify an
asymptotic mixing estimate or the Collatz conjecture.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import lru_cache
import json
from math import comb, log


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def literal(n: int, t: int) -> tuple[int, int]:
    odds = 0
    for _ in range(t):
        if n & 1:
            odds += 1
            n = (3*n+1)//2
        else:
            n //= 2
    return odds, n


@lru_cache(maxsize=None)
def affine_label(n: int, t: int) -> tuple[int, int]:
    """Build the complete numerator as an independent arithmetic ledger."""
    initial = n
    numerator = 0
    power3 = 1
    odds = 0
    for tick in range(t):
        bit = n & 1
        if bit:
            numerator = 3*numerator + (1 << tick)
            power3 *= 3
            odds += 1
        n = (3*n+bit)//2 if bit else n//2
    full = power3*initial+numerator
    require(full % (1 << t) == 0, "nonintegral full affine endpoint")
    endpoint = full >> t
    require(endpoint == n, "affine ledger disagrees with actual endpoint")
    return odds, endpoint


@lru_cache(maxsize=None)
def population(N: int, t: int) -> Counter:
    return Counter(affine_label(n, t) for n in range(1, N+1))


def shifted(table: dict) -> dict:
    return {(q+1, y): value for (q, y), value in table.items()}


def scaled_sum(*terms: tuple[int, dict]) -> dict:
    out: dict = {}
    for factor, table in terms:
        for key, value in table.items():
            out[key] = out.get(key, 0)+factor*value
    return {key: value for key, value in out.items() if value}


def signed_trit(N: int, t: int) -> dict:
    result: dict = {}
    for n in range(1, N+1):
        key = affine_label(n, t)
        result[key] = result.get(key, 0)+(3*(n % 3 == 2)-1)
    return {key: value for key, value in result.items() if value}


def binomial_tv(N: int, t: int) -> Fraction:
    counts = Counter()
    for (q, _), frequency in population(N, t).items():
        counts[q] += frequency
    denominator = 2*N*(1 << t)
    numerator = sum(abs(counts[q]*(1 << t)-N*comb(t, q)) for q in range(t+1))
    return Fraction(numerator, denominator)


def main() -> None:
    source_controls = 0
    for n in range(1, 385):
        for t in range(34):
            require(literal(n, t) == affine_label(n, t), "literal/affine mismatch")
            source_controls += 1

    recursion_controls = 0
    nonempty_odd_rows = 0
    for N in range(129):
        for t in range(33):
            cutoff = (3*N+1)//2
            left = population(N, t+1)
            even = population(N//2, t)
            odd = Counter(affine_label(y, t) for y in range(1, cutoff+1) if y % 3 == 2)
            direct_split = scaled_sum((1, even), (1, shifted(odd)))
            require(dict(left) == direct_split, "wrong first-step source cutoff or label")
            trit_split = scaled_sum(
                (3, even), (1, shifted(population(cutoff, t))),
                (1, shifted(signed_trit(cutoff, t))))
            require(scaled_sum((3, left)) == trit_split, "signed native transport identity failed")
            require(sum(left.values()) == N, "source population was lost")
            recursion_controls += 1
            nonempty_odd_rows += bool(odd)

    # The endpoint cannot be adjoined to a time-zero trit mixing claim.
    time_zero = signed_trit(300, 0)
    require(sum(abs(v) for v in time_zero.values()) == 400,
            "time-zero endpoint obstruction changed")
    count_only = Counter()
    for (q, _), v in time_zero.items():
        count_only[q] += v
    require(all(v == 0 for v in count_only.values()), "count-only trit cancellation failed")

    examples = []
    mu = 2/log(4/3)
    for N in (256, 1024, 4096):
        center = mu*log(N)
        for multiplier in (0.5, 1.0, 1.25):
            t = int(multiplier*center)
            tv = binomial_tv(N, t)
            examples.append({"source_cutoff": N, "shortcut_time": t,
                             "critical_multiplier": multiplier,
                             "count_binomial_tv_exact": str(tv),
                             "count_binomial_tv_decimal": round(float(tv), 9)})
    print(json.dumps({"schema": "collatz-native-recursion-controls/v1",
                      "scope": "bounded exact identities; no asymptotic or convergence inference",
                      "literal_affine_source_time_pairs": source_controls,
                      "complete_joint_recursions": recursion_controls,
                      "nonempty_odd_rows": nonempty_odd_rows,
                      "time_zero_joint_trit_norm": "4/3",
                      "time_zero_count_trit_norm": "0",
                      "finite_binomial_comparisons": examples}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
