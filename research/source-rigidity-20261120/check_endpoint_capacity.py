#!/usr/bin/env python3
"""Exact finite controls for ENDPOINT_CAPACITY.md; not an infinite proof."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def oddpart(n: int) -> int:
    require(type(n) is int and n > 0, "positive integer required")
    return n // (n & -n)


def b_value(n: int, cutoff: int) -> int:
    return int(oddpart(n) <= cutoff)


def j_value(m: int) -> int:
    require(type(m) is int and m > 0, "positive integer required")
    return max(1, ((m - 1).bit_length() + 1) // 2)


def fixed_value(n: int) -> Fraction:
    return Fraction(1, j_value(oddpart(n)))


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def canonical_digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def floor_at_scale(value: Fraction, scale: int = 1000) -> int:
    return value.numerator * scale // value.denominator


def main() -> None:
    definition_checks = 0
    variation_checks = 0
    edge_failures = []
    zero_constant_rejected = False

    # Quarter-grid representatives capture both integer/half-integer endpoints
    # and their intervening cells over this bounded range of real R.
    for cutoff in range(1, 65):
        a_count = (cutoff + 1) // 2
        b_count = sum(1 for m in range(1, cutoff + 1, 2) if 3 * m > cutoff)
        require(a_count <= 3 * b_count, "odd annulus count failed")
        for n in range(1, 8 * cutoff + 1):
            actual = b_value(3 * n, cutoff) - b_value(n, cutoff)
            expected = -int(cutoff < 3 * oddpart(n) <= 3 * cutoff)
            require(actual == expected, "tripling defect formula failed")
            require(b_value(2 * n, cutoff) == b_value(n, cutoff), "doubling failed")
            definition_checks += 1
        for r4 in range(4, 16 * cutoff + 5):
            left = (r4 + 3) // 4
            right = r4 // 2
            variation = sum(
                abs(b_value(n + 1, cutoff) - b_value(n, cutoff))
                for n in range(left, right + 1)
            )
            defect_count = sum(
                1 for m in range(1, right + 1, 2)
                if cutoff < 3 * m <= 3 * cutoff
            )
            require(variation <= 12 * defect_count, "shell variation failed")
            zero_constant_rejected |= variation > 0
            variation_checks += 1

        power = 4
        while (power - 1) // 3 <= cutoff:
            power *= 4
        n = (power - 1) // 3
        require(n % 2 == 1 and shortcut(n) == power // 2, "ordinary edge failed")
        require(b_value(n, cutoff) == 0 and b_value(shortcut(n), cutoff) == 1,
                "missing odd-branch failure")
        edge_failures.append([cutoff, n, shortcut(n)])

    require(zero_constant_rejected, "negative zero-variation control failed")

    # The exact infinite harmonic norms reduce to these finite odd sums.
    maximum = 4096
    odd_harmonic = [Fraction(0)] * (maximum + 1)
    total = Fraction(0)
    for m in range(1, maximum + 1):
        if m % 2:
            total += Fraction(1, m)
        odd_harmonic[m] = total

    norm_rows = []
    norm_exact_for_hash = []
    false_endpoint_constant_rejected = False
    for cutoff in [1, 2, 3, 4, 7, 16, 64, 256, 1024, 4096]:
        mass = 2 * odd_harmonic[cutoff]
        defect = 2 * (odd_harmonic[cutoff] - odd_harmonic[cutoff // 3])
        require(defect > 0, "nonpositive annulus norm")
        if cutoff in [4, 16, 64, 256, 1024, 4096]:
            require(defect < 3, "finite fixed-function bound failed")
        false_endpoint_constant_rejected |= mass > 3 * defect
        norm_rows.append({
            "cutoff": cutoff,
            "mass_times_1000_floor": floor_at_scale(mass),
            "defect_times_1000_floor": floor_at_scale(defect),
            "ratio_times_1000_floor": floor_at_scale(mass / defect),
        })
        norm_exact_for_hash.append([cutoff, str(mass), str(defect)])
    require(false_endpoint_constant_rejected, "false endpoint constant 3 survived")

    fixed_function_checks = 0
    for m in range(1, 16385):
        j = j_value(m)
        require(m <= 4 ** j and (j == 1 or m > 4 ** (j - 1)), "J formula failed")
        require(j_value(3 * m) - j in [0, 1], "J jump exceeds one")
        # Finite mixture identity, with the exact remaining scalar tail added
        # once its cutoffs all exceed the odd part.
        if m <= 128:
            mixture = sum(
                Fraction(b_value(m, 4 ** k), k * (k + 1))
                for k in range(1, 9)
            ) + Fraction(1, 9)
            require(mixture == fixed_value(m), "fixed function mixture failed")
        fixed_function_checks += 1

    require(fixed_value(5) < fixed_value(shortcut(5)), "real odd-branch control failed")

    ap_checks = 0
    ap_exact_for_hash = []
    for length in [16, 64, 256, 1024, 4096]:
        h = isqrt(length)
        ell = (length - 1).bit_length()
        for start, stride in [(1, 1), (10 ** 12 + 1, 1),
                              (2 ** 127 + 1, 3 ** 13),
                              (2 ** 80 - 1001, 5 ** 17)]:
            terms = [start + stride * i for i in range(length)]
            small = sum(oddpart(n) <= h for n in terms)
            require(small <= h * ell + 1, "small odd-part count failed")
            actual = sum(abs(fixed_value(3 * n) - fixed_value(n)) for n in terms)
            upper = Fraction(h * ell + 1) + Fraction(length, j_value(h + 1) ** 2)
            require(actual <= upper, "uniform arithmetic progression bound failed")
            ap_exact_for_hash.append([length, start, stride, small, str(actual)])
            ap_checks += 1

    report = {
        "status": "PASS: exact finite controls only; infinite proofs are in the note",
        "definition_and_doubling_checks": definition_checks,
        "quarter_grid_shell_variation_checks": variation_checks,
        "explicit_known_convergent_odd_edge_failures": len(edge_failures),
        "edge_failure_digest": canonical_digest(edge_failures),
        "harmonic_norm_rows": norm_rows,
        "exact_harmonic_norm_digest": canonical_digest(norm_exact_for_hash),
        "fixed_function_integer_controls": fixed_function_checks,
        "uniform_odd_progression_controls": ap_checks,
        "exact_progression_digest": canonical_digest(ap_exact_for_hash),
        "negative_controls": [
            "zero shell-variation constant rejected",
            "uniform harmonic coercivity constant 3 rejected",
            "true odd Collatz invariance rejected at explicit ordinary edges",
        ],
        "scope": [
            "No Collatz-invariant nonconstant labeling is constructed.",
            "The examples are ordinary integer functions in a larger analytic cone.",
            "Finite checks do not prove asymptotic limits, uniform infinite bounds, or Collatz.",
        ],
        "proof_sha256": hashlib.sha256(
            Path(__file__).with_name("ENDPOINT_CAPACITY.md").read_bytes()
        ).hexdigest(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
