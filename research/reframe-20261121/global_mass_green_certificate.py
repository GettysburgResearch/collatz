#!/usr/bin/env python3
"""Exact finite-source certificate for the Green-power attempt in GLOBAL_MASS.md.

This does not test Collatz over an unbounded source range.  For the 21 odd
ternary units at most 63, it records actual first hits of 11 or actual hits
of 1 before 11.  The mathematical reciprocal-square tail bound supplies
the unbounded-source upper bound; finite replay alone does not supply it.
All comparisons use integers and Fraction, never floating-point numbers.
"""

from fractions import Fraction
import json


def trace_to_one_or_target(source: int, target: int) -> tuple[int, int, int]:
    value, clock, valuation_sum = source, 0, 0
    seen: set[int] = set()
    while value not in (1, target):
        if value in seen:
            raise RuntimeError(f"unresolved cycle from source {source}")
        if clock >= 10000:
            raise RuntimeError(f"unresolved source {source} at replay limit")
        seen.add(value)
        even = 3 * value + 1
        valuation = (even & -even).bit_length() - 1
        value = even >> valuation
        clock += 1
        valuation_sum += valuation
    return value, clock, valuation_sum


def certificate() -> dict:
    target, cutoff = 11, 63
    # The target itself is nonperiodic: 11 -> 17 -> 13 -> 5 -> 1.
    target_tail = []
    value = target
    while value != 1:
        target_tail.append(value)
        even = 3 * value + 1
        valuation = (even & -even).bit_length() - 1
        value = even >> valuation
    target_tail.append(1)
    if target_tail != [11, 17, 13, 5, 1]:
        raise AssertionError("target-tail certificate changed")

    hits, misses = [], []
    partial = Fraction(0)
    for source in range(1, cutoff + 1, 2):
        if source % 3 == 0:
            continue
        endpoint, clock, valuation_sum = trace_to_one_or_target(source, target)
        if endpoint == target:
            hits.append([source, clock, valuation_sum])
            partial += Fraction(3 ** (2 * clock), 2 ** (2 * valuation_sum))
        else:
            misses.append(source)

    # Every omitted odd source n contributes at most target^2/n^2.
    # Convexity on [n-1,n+1] gives
    # sum_(odd n>cutoff) n^-2 <= 1/[2(cutoff+1)].
    tail = Fraction(target * target, 2 * (cutoff + 1))
    upper = partial + tail
    if partial != Fraction(68729473, 16777216):
        raise AssertionError("finite-source pressure changed")
    if upper != Fraction(84589185, 16777216):
        raise AssertionError("certified pressure upper bound changed")
    if not upper < Fraction(81, 16):
        raise AssertionError("Green compression obstruction failed")
    return {
        "map": "accelerated odd 3x+1 on positive odd ternary units",
        "target": target,
        "target_tail": target_tail,
        "cutoff": cutoff,
        "hits_source_clock_total_valuation": hits,
        "sources_reaching_one_before_target": misses,
        "finite_pressure": str(partial),
        "all_omitted_sources_upper_bound": str(tail),
        "full_G2_target_upper_bound": str(upper),
        "comparison": "84589185/16777216 < 81/16",
        "scope": "G2(11) upper bound; not an unbounded convergence test",
    }


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2))
