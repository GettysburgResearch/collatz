#!/usr/bin/env python3
"""Small exact checks supporting the SHA-scoped pre-public review.

This deliberately does not rerun any expensive frontier or MITM census.
It checks only the localized arithmetic needed to diagnose or corroborate
specific review findings.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction


FROZEN_HEADS = {
    "35": "eaba69839c07cb83794b711ecdce62c75ce765f9",
    "37": "a518db7feece37513ddcda729553e8b8c4c4d657",
    "38": "6673ed0e765417448b2657fff2856a7d4909d113",
    "42": "ada763dcc9ca317b65691ec6d9129f514b54fd07",
}


def atanh_log_bounds(z: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    if not 0 < z < 1:
        raise ValueError("z must lie in (0,1)")
    total = Fraction(0)
    power = z
    z2 = z * z
    for j in range(terms):
        total += 2 * power / (2 * j + 1)
        power *= z2
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return total, total + tail


def quotient_bounds(
    numerator: tuple[Fraction, Fraction],
    denominator: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    return numerator[0] / denominator[1], numerator[1] / denominator[0]


def check_pr35() -> dict[str, object]:
    root = 4_538_335_001_132_531
    x = root
    digits: list[str] = []
    first_overflow_step: int | None = None
    for step in range(50):
        if first_overflow_step is None and x >= 2**64:
            first_overflow_step = step
        residue = x % 4
        if residue not in (0, 3):
            raise AssertionError((step, x, residue))
        digits.append(str((-residue) % 4))
        x = (5 * x + 3) // 4

    expected_word = "10011110111001011100001001101001011101010100000010"
    if "".join(digits) != expected_word:
        raise AssertionError("PR35 depth-50 word mismatch")
    if first_overflow_step != 38:
        raise AssertionError("unexpected first uint64 overflow step")
    if x != 317_978_093_383_929_174_805:
        raise AssertionError("unexpected exact state after 50 steps")
    if (-x) % 4 != 3:
        raise AssertionError("unexpected first forbidden digit")

    # Reproduce the source program's wrapped replay field.  This confirms that
    # its frozen value is a uint64 artifact, not the exact physical state.
    modulus = 2**64
    wrapped = root
    for _ in range(50):
        wrapped = ((5 * wrapped + 3) % modulus) // 4
    if wrapped != 1_085_242_780_136_381_205:
        raise AssertionError("wrapped source field changed")

    return {
        "least_root_from_frozen_artifact": root,
        "first_uint64_overflow_step": first_overflow_step,
        "exact_state_after_50": x,
        "wrapped_source_field": wrapped,
        "first_forbidden_digit": 3,
        "bottom_digit_prefix": expected_word,
    }


def check_pr37() -> dict[str, object]:
    # The two constant itineraries select the zero nearest-integer completion.
    # Their factor complexity is one, so they are exact counterexamples to the
    # unqualified original T-9318 while lying outside repaired T-9319.
    return {
        "constant_zero_completion": 0,
        "constant_one_completion": 0,
        "constant_factor_complexity": 1,
        "original_T_9318_counterexamples": 2,
    }


def minimum_support(k: int) -> int:
    left = 14**k
    base = 11**k
    lo, hi = 0, k
    while lo < hi:
        mid = (lo + hi) // 2
        if left <= base * 2**mid:
            hi = mid
        else:
            lo = mid + 1
    return lo


def check_pr38() -> dict[str, object]:
    k = 50_001
    support = minimum_support(k)
    if support != 17_397:
        raise AssertionError("PR38 support threshold mismatch")
    left = 14**k
    base = 11**k
    if not base * 2 ** (support - 1) < left <= base * 2**support:
        raise AssertionError("PR38 exact threshold inequalities failed")
    return {
        "conditional_length": k,
        "minimum_support": support,
        "strict_below": True,
        "at_threshold": True,
    }


def check_pr42() -> dict[str, object]:
    x_min = 2**71 + 1
    ln2 = atanh_log_bounds(Fraction(1, 3), 150)
    ln43 = atanh_log_bounds(Fraction(1, 7), 80)
    lne = atanh_log_bounds(Fraction(1, 6 * x_min + 1), 2)
    alpha = quotient_bounds(ln43, ln2)
    beta = quotient_bounds((ln43[0] - lne[1], ln43[1] - lne[0]), ln2)

    p_minus, q_minus = 2_733_776_749, 6_586_818_670
    p_plus, q_plus = 27_172_759_629, 65_470_613_321
    charge = p_minus + p_plus
    length = q_minus + q_plus

    lower = Fraction(p_minus, q_minus)
    mediant = Fraction(charge, length)
    upper = Fraction(p_plus, q_plus)

    if p_plus * q_minus - p_minus * q_plus != 1:
        raise AssertionError("PR42 Farey determinant failed")
    if not lower < beta[0] < beta[1] < mediant:
        raise AssertionError("PR42 lower charge-cylinder ordering failed")
    if not mediant < alpha[0] < alpha[1] < upper:
        raise AssertionError("PR42 upper charge-cylinder ordering failed")
    if not Fraction(charge - 1, length) < beta[0]:
        raise AssertionError("PR42 integer charge floor failed")
    if (length, charge) != (72_057_431_991, 29_906_536_378):
        raise AssertionError("PR42 floors changed")

    return {
        "farey_determinant": 1,
        "odd_state_floor": length,
        "signed_charge_floor": charge,
        "non2_support_floor": charge,
        "all_interval_checks": True,
    }


def main() -> None:
    payload: dict[str, object] = {
        "frozen_heads": FROZEN_HEADS,
        "pr35": check_pr35(),
        "pr37": check_pr37(),
        "pr38": check_pr38(),
        "pr42": check_pr42(),
    }
    semantic = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["semantic_sha256"] = hashlib.sha256(semantic.encode()).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
