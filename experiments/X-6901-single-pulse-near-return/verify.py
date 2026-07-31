#!/usr/bin/env python3
"""Exact verifier for T-6907.

The sole external theorem dependency is the same explicit two-logarithm
Matveev lower bound used by PR #53 T-8202. Everything after that quoted lower
bound is reconstructed with Python integers and fractions.Fraction.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)

TERMS = 180
MATVEEV_C2 = 2**32


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if not self.lo < self.hi:
            raise ValueError("invalid interval")


def atanh_interval(z: Fraction) -> Interval:
    if not Fraction(0) <= z < 1:
        raise ValueError("atanh domain")
    total = Fraction(0)
    power = z
    square = z * z
    for index in range(TERMS):
        total += 2 * power / (2 * index + 1)
        power *= square
    tail = 2 * power / ((2 * TERMS + 1) * (1 - square))
    return Interval(total, total + tail)


LOG2 = atanh_interval(Fraction(1, 3))


def log_integer(n: int) -> Interval:
    if n <= 0:
        raise ValueError("log domain")
    if n == 2:
        return LOG2
    shift = n.bit_length() - 1
    mantissa = Fraction(n, 2**shift)
    z = (mantissa - 1) / (mantissa + 1)
    core = atanh_interval(z)
    return Interval(
        shift * LOG2.lo + core.lo,
        shift * LOG2.hi + core.hi,
    )


LOG3 = log_integer(3)


def alpha_interval(A: int, k: int) -> Interval:
    return Interval(
        (k * LOG3.lo - A * LOG2.hi) / LOG2.hi,
        (k * LOG3.hi - A * LOG2.lo) / LOG2.lo,
    )


def continued_fraction(interval: Interval, cutoff: int) -> list[dict[str, int | str]]:
    lo, hi = interval.lo, interval.hi
    original_lo, original_hi = lo, hi
    p_prev2, p_prev1 = 0, 1
    q_prev2, q_prev1 = 1, 0
    rows: list[dict[str, int | str]] = []

    for index in range(256):
        partial = lo.numerator // lo.denominator
        if partial != hi.numerator // hi.denominator:
            raise AssertionError(f"continued-fraction interval unresolved at {index}")
        p = partial * p_prev1 + p_prev2
        q = partial * q_prev1 + q_prev2
        value = Fraction(p, q)
        if value < original_lo:
            side = "below"
        elif value > original_hi:
            side = "above"
        else:
            raise AssertionError("convergent lies inside unresolved interval")
        rows.append(
            {
                "index": index,
                "partial_quotient": partial,
                "p": p,
                "q": q,
                "side": side,
            }
        )
        if q > cutoff:
            return rows
        lo, hi = 1 / (hi - partial), 1 / (lo - partial)
        p_prev2, p_prev1 = p_prev1, p
        q_prev2, q_prev1 = q_prev1, q

    raise AssertionError("continued fraction did not pass cutoff")


def certify_matveev_cutoff(A: int, k: int, gmax: int, cutoff: int) -> None:
    constant_hi = MATVEEV_C2 * LOG2.hi * LOG3.hi
    left = cutoff * A * LOG2.lo
    right = log_integer(2 * gmax).hi + constant_hi * (
        1 + log_integer(k * cutoff + 1).hi
    )
    derivative = A * LOG2.lo - constant_hi * Fraction(k, k * cutoff + 1)
    if not left > right:
        raise AssertionError("Matveev cutoff margin is not positive")
    if not derivative > 0:
        raise AssertionError("Matveev cutoff function is not increasing")


def certify_legendre_threshold(A: int, gmax: int, first_r: int) -> None:
    U = 2**A
    if not U**first_r * LOG2.lo > 4 * gmax * first_r:
        raise AssertionError("Legendre threshold fails")
    if not Fraction(U * first_r, first_r + 1) > 1:
        raise AssertionError("U^r/r is not certified increasing")


def reject_upper_convergents(
    A: int,
    gmax: int,
    rows: list[dict[str, int | str]],
    cutoff: int,
    minimum_r: int,
) -> list[dict[str, int]]:
    rejected: list[dict[str, int]] = []
    for index, row in enumerate(rows[:-1]):
        q = int(row["q"])
        if row["side"] != "above" or q >= cutoff or q < minimum_r:
            continue
        p = int(row["p"])
        q_next = int(rows[index + 1]["q"])
        if not 2 ** (A * q) > 4 * gmax * (q + q_next):
            raise AssertionError(f"upper convergent {p}/{q} was not rejected")
        rejected.append({"p": p, "q": q, "q_next": q_next})
    return rejected


def prefix_sums(word: tuple[int, ...]) -> list[int]:
    out = [0]
    for value in word:
        out.append(out[-1] + value)
    return out


def affine_numerator(word: tuple[int, ...]) -> int:
    pref = prefix_sums(word)
    length = len(word)
    return sum(
        3 ** (length - 1 - index) * 2 ** pref[index]
        for index in range(length)
    )


def valuation_two(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0)")
    n = abs(n)
    return (n & -n).bit_length() - 1


def rotate(word: tuple[int, ...], shift: int) -> tuple[int, ...]:
    shift %= len(word)
    return word[shift:] + word[:shift]


def negative_fixed_point(word: tuple[int, ...]) -> int:
    denominator = 2 ** sum(word) - 3 ** len(word)
    numerator = affine_numerator(word)
    if numerator % denominator:
        raise AssertionError("base word is not an integral cycle")
    start = numerator // denominator
    if start >= 0 or start % 2 == 0:
        raise AssertionError("base cycle is not negative odd")
    current = start
    for value in word:
        raw = 3 * current + 1
        if valuation_two(raw) != value:
            raise AssertionError("base valuation mismatch")
        current = raw // 2**value
    if current != start:
        raise AssertionError("base cycle does not close")
    return start


def small_exact_scan(
    base: tuple[int, ...],
    maximum_repetition: int,
) -> dict[str, object]:
    packets = 0
    candidates = 0
    hits: list[dict[str, object]] = []

    for repetition in range(1, maximum_repetition + 1):
        odd_length = len(base) * repetition
        for rotation in range(len(base)):
            primitive = rotate(base, rotation)
            word = primitive * repetition
            z = negative_fixed_point(word)
            U = 2 ** sum(word)
            Q = 3**odd_length
            g = -(3 * z + 1)

            minimum_multiple = (-z) // (3 ** (odd_length - 1)) + 1
            if not minimum_multiple * U > g:
                raise AssertionError("small-case pulse cap has nonpositive slope")

            numerator = minimum_multiple * Q - g
            denominator = minimum_multiple * U - g
            maximum_delta = -1
            while denominator * 2 ** (maximum_delta + 1) <= numerator:
                maximum_delta += 1

            packets += 1
            for delta in range(1, maximum_delta + 1):
                D = U * 2**delta - Q
                if D <= 0:
                    continue
                maximum_reduced_numerator = g * (2**delta - 1)
                maximum_multiple = maximum_reduced_numerator // D

                for multiple in range(minimum_multiple, maximum_multiple + 1):
                    residual = maximum_reduced_numerator - multiple * D
                    if residual % 3:
                        continue
                    displacement = residual // 3
                    start = z + multiple * 3 ** (odd_length - 1)
                    if start <= 0:
                        raise AssertionError("candidate positivity failed")

                    pulsed = list(word)
                    pulsed[0] += delta
                    current = start
                    for value in pulsed:
                        raw = 3 * current + 1
                        if raw <= 0 or valuation_two(raw) != value:
                            raise AssertionError("candidate physical replay failed")
                        current = raw // 2**value
                    if current != start + displacement:
                        raise AssertionError("candidate endpoint mismatch")

                    candidates += 1
                    hits.append(
                        {
                            "repetition": repetition,
                            "rotation": rotation,
                            "delta": delta,
                            "multiple": multiple,
                            "displacement": displacement,
                            "start": start,
                            "word": pulsed,
                        }
                    )

    return {
        "packets": packets,
        "candidates": candidates,
        "hits": hits,
    }


CASES = (
    {
        "name": "negative-three-cycle",
        "base": (1, 2),
        "A": 3,
        "k": 2,
        "gmax": 20,
        "cutoff": 50_000_000_000,
        "legendre_r": 3,
        "small_r": 2,
    },
    {
        "name": "negative-eleven-cycle",
        "base": (1, 1, 1, 2, 1, 1, 4),
        "A": 11,
        "k": 7,
        "gmax": 272,
        "cutoff": 12_000_000_000,
        "legendre_r": 1,
        "small_r": 1,
    },
)


def build_payload() -> dict[str, object]:
    cases: list[dict[str, object]] = []
    for spec in CASES:
        interval = alpha_interval(int(spec["A"]), int(spec["k"]))
        rows = continued_fraction(interval, int(spec["cutoff"]))
        certify_matveev_cutoff(
            int(spec["A"]),
            int(spec["k"]),
            int(spec["gmax"]),
            int(spec["cutoff"]),
        )
        certify_legendre_threshold(
            int(spec["A"]),
            int(spec["gmax"]),
            int(spec["legendre_r"]),
        )
        rejected = reject_upper_convergents(
            int(spec["A"]),
            int(spec["gmax"]),
            rows,
            int(spec["cutoff"]),
            int(spec["legendre_r"]),
        )
        small = small_exact_scan(
            tuple(spec["base"]),
            int(spec["small_r"]),
        )
        cases.append(
            {
                "name": spec["name"],
                "continued_fraction_rows": len(rows),
                "upper_convergents_rejected": rejected,
                "small_exact_scan": small,
            }
        )

    hits = [
        hit
        for case in cases
        for hit in case["small_exact_scan"]["hits"]
    ]
    if len(hits) != 1:
        raise AssertionError("expected exactly one trivial hit")
    hit = hits[0]
    if not (
        hit["start"] == 1
        and hit["displacement"] == 0
        and hit["word"] == [2, 2]
    ):
        raise AssertionError("the sole hit is not the trivial cycle")

    semantic = json.dumps(cases, sort_keys=True, separators=(",", ":"))
    return {
        "experiment_id": "X-6901",
        "status": "EXACT FINITE CERTIFICATE / SOURCE-DEPENDENT ANALYTIC REDUCTION",
        "cases": cases,
        "nontrivial_hits": 0,
        "trivial_hits": 1,
        "semantic_sha256": hashlib.sha256(semantic.encode()).hexdigest(),
    }


def main() -> None:
    payload = build_payload()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
