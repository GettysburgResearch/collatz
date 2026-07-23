#!/usr/bin/env python3
"""Exact certificate for the signed-defect charge cylinder (X-8612)."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path
from typing import Sequence


CANONICAL_VERIFIED_EXPONENT = 71
EXPECTED_P_MINUS = 2_733_776_749
EXPECTED_Q_MINUS = 6_586_818_670
EXPECTED_P_PLUS = 27_172_759_629
EXPECTED_Q_PLUS = 65_470_613_321


def atanh_log_bounds(z: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    """Bounds log((1+z)/(1-z)) by its positive atanh series."""
    if not (0 < z < 1):
        raise ValueError("z must lie in (0,1)")
    total = Fraction(0)
    power = z
    z2 = z * z
    for j in range(terms):
        total += 2 * power / (2 * j + 1)
        power *= z2
    tail = 2 * power / ((2 * terms + 1) * (1 - z2))
    return total, total + tail


def ratio_bounds(
    numerator: tuple[Fraction, Fraction],
    denominator: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    n_lo, n_hi = numerator
    d_lo, d_hi = denominator
    if n_lo <= 0 or d_lo <= 0:
        raise ValueError("positive intervals required")
    return n_lo / d_hi, n_hi / d_lo


def logarithm_intervals(x_min: int) -> dict[str, tuple[Fraction, Fraction]]:
    ln2 = atanh_log_bounds(Fraction(1, 3), 150)
    ln43 = atanh_log_bounds(Fraction(1, 7), 80)
    # (1+z)/(1-z) = 1 + 1/(3X) when z=1/(6X+1).
    lne = atanh_log_bounds(Fraction(1, 6 * x_min + 1), 2)
    alpha = ratio_bounds(ln43, ln2)
    beta_num = (ln43[0] - lne[1], ln43[1] - lne[0])
    beta = ratio_bounds(beta_num, ln2)
    return {"ln2": ln2, "ln43": ln43, "lne": lne, "alpha": alpha, "beta": beta}


def stern_brocot_cover(
    beta: tuple[Fraction, Fraction],
    alpha: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction, Fraction, int]:
    """Derive determinant-one neighbors enclosing [beta,alpha)."""
    left = Fraction(0, 1)
    right = Fraction(1, 1)
    for iteration in range(1, 100_001):
        mediant = Fraction(
            left.numerator + right.numerator,
            left.denominator + right.denominator,
        )
        if mediant <= beta[0]:
            left = mediant
        elif mediant >= alpha[1]:
            right = mediant
        elif beta[1] < mediant < alpha[0]:
            return left, right, mediant, iteration
        else:
            raise AssertionError("logarithm intervals are too wide for Stern-Brocot routing")
    raise AssertionError("Stern-Brocot cover did not terminate")


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def frac_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def decimal_text(value: Fraction, digits: int = 48) -> str:
    # Exact long division; no floating point enters the certificate.
    sign = "-" if value < 0 else ""
    value = abs(value)
    n, d = value.numerator, value.denominator
    whole, rem = divmod(n, d)
    out = []
    for _ in range(digits):
        rem *= 10
        digit, rem = divmod(rem, d)
        out.append(str(digit))
    return f"{sign}{whole}." + "".join(out)


def euler_phi(n: int) -> int:
    result = n
    p = 2
    x = n
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            result -= result // p
        p += 1
    if x > 1:
        result -= result // x
    return result


def divisors(n: int) -> list[int]:
    small = []
    large = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
        d += 1
    return small + large[::-1]


def ordered_defect_count(support: int, slack: int) -> int:
    """Coefficient [x^slack](1+x^2+x^3+...)^support."""
    if support < 0 or slack < 0:
        return 0
    dp = [0] * (slack + 1)
    dp[0] = 1
    for _ in range(support):
        nxt = [0] * (slack + 1)
        for used, count in enumerate(dp):
            if not count:
                continue
            nxt[used] += count  # valuation 1, weight 0
            for weight in range(2, slack - used + 1):
                nxt[used + weight] += count
        dp = nxt
    return dp[slack]


def necklace_count(support: int, slack: int) -> int:
    """Weighted Burnside count for cyclic defect necklaces."""
    total = 0
    for repeat in divisors(gcd(support, slack)):
        total += euler_phi(repeat) * ordered_defect_count(
            support // repeat, slack // repeat
        )
    if total % support:
        raise AssertionError("Burnside numerator is not divisible by support")
    return total // support


def rotations(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(word[i:] + word[:i] for i in range(len(word)))


def brute_necklace_count(support: int, slack: int) -> int:
    alphabet = [1] + list(range(3, slack + 2))
    seen: set[tuple[int, ...]] = set()
    count = 0
    for word in product(alphabet, repeat=support):
        if sum(a - 1 for a in word) != slack:
            continue
        canonical = min(rotations(word))
        if canonical not in seen:
            seen.add(canonical)
            count += 1
    return count


def binary_packet_normal_form(
    word: Sequence[int],
) -> tuple[tuple[int, ...], tuple[tuple[int, tuple[int, ...], int], ...]]:
    """
    Convert a positive-charge valuation word to a same-length, same-sum {1,2}
    base. Each high valuation a uses one high position and a-2 one-positions.
    """
    values = list(word)
    ones = [i for i, a in enumerate(values) if a == 1]
    highs = [(i, a) for i, a in enumerate(values) if a >= 3]
    charge = 2 * len(values) - sum(values)
    if charge <= 0:
        raise ValueError("normal form requires positive charge")
    need = sum(a - 2 for _, a in highs)
    if len(ones) < need:
        raise AssertionError("positive charge should supply enough one positions")

    base = values[:]
    cursor = 0
    packets = []
    for high_pos, high_value in highs:
        chosen = tuple(ones[cursor : cursor + high_value - 2])
        cursor += high_value - 2
        base[high_pos] = 2
        for pos in chosen:
            base[pos] = 2
        packets.append((high_pos, chosen, high_value))

    if any(a not in (1, 2) for a in base):
        raise AssertionError("base is not binary")
    if sum(base) != sum(values):
        raise AssertionError("valuation sum changed")
    if base.count(1) != charge:
        raise AssertionError("base charge mismatch")

    rebuilt = base[:]
    for high_pos, chosen, high_value in packets:
        rebuilt[high_pos] = high_value
        for pos in chosen:
            rebuilt[pos] = 1
    if rebuilt != values:
        raise AssertionError("packet reconstruction failed")
    return tuple(base), tuple(packets)


def normal_form_audit(max_length: int = 7, max_letter: int = 6) -> int:
    checked = 0
    alphabet = tuple(a for a in range(1, max_letter + 1))
    for length in range(1, max_length + 1):
        for word in product(alphabet, repeat=length):
            charge = 2 * length - sum(word)
            if charge <= 0:
                continue
            support = sum(a != 2 for a in word)
            slack = support - charge
            sparse_weight = sum(a - 1 for a in word if a != 2)
            if slack != sparse_weight:
                raise AssertionError("slack identity failed")
            base, packets = binary_packet_normal_form(word)
            changed = sum(a != b for a, b in zip(word, base))
            if changed != slack:
                raise AssertionError("Hamming/slack identity failed")
            if len(packets) > slack // 2:
                raise AssertionError("high-count bound failed")
            if packets and max(a for _, _, a in packets) > slack + 1:
                raise AssertionError("high-letter bound failed")
            checked += 1
    return checked


def necklace_audit(max_support: int = 7, max_slack: int = 10) -> int:
    checked = 0
    for support in range(1, max_support + 1):
        for slack in range(max_slack + 1):
            formula = necklace_count(support, slack)
            brute = brute_necklace_count(support, slack)
            if formula != brute:
                raise AssertionError(
                    f"necklace mismatch support={support} slack={slack}: "
                    f"{formula} != {brute}"
                )
            checked += 1
    return checked


def build_payload(verified_exponent: int = CANONICAL_VERIFIED_EXPONENT) -> dict:
    if verified_exponent < 1:
        raise ValueError("verified exponent must be positive")
    x_min = 2**verified_exponent + 1
    intervals = logarithm_intervals(x_min)
    alpha_lo, alpha_hi = intervals["alpha"]
    beta_lo, beta_hi = intervals["beta"]

    lower, upper, mediant, stern_iterations = stern_brocot_cover(
        intervals["beta"], intervals["alpha"]
    )
    charge_floor_lo = ceil_fraction(beta_lo * mediant.denominator)
    charge_floor_hi = ceil_fraction(beta_hi * mediant.denominator)
    if charge_floor_lo != charge_floor_hi:
        raise AssertionError("charge floor is not resolved by the rational interval")
    charge_floor = charge_floor_lo
    length_floor = mediant.denominator

    if upper.numerator * lower.denominator - lower.numerator * upper.denominator != 1:
        raise AssertionError("Farey determinant is not one")
    if not lower < beta_lo:
        raise AssertionError("lower Farey endpoint does not lie below beta")
    if not beta_hi < mediant:
        raise AssertionError("mediant does not lie above beta")
    if not mediant < alpha_lo:
        raise AssertionError("mediant does not lie below alpha")
    if not alpha_hi < upper:
        raise AssertionError("upper Farey endpoint does not lie above alpha")
    if not Fraction(charge_floor - 1, length_floor) < beta_lo:
        raise AssertionError("integer charge floor is not certified")

    if verified_exponent == CANONICAL_VERIFIED_EXPONENT:
        expected = (
            EXPECTED_P_MINUS,
            EXPECTED_Q_MINUS,
            EXPECTED_P_PLUS,
            EXPECTED_Q_PLUS,
        )
        observed = (
            lower.numerator,
            lower.denominator,
            upper.numerator,
            upper.denominator,
        )
        if observed != expected:
            raise AssertionError(f"canonical Farey endpoints changed: {observed}")

    normal_cases = normal_form_audit()
    necklace_cases = necklace_audit()

    margins = {
        "beta_minus_lower": beta_lo - lower,
        "mediant_minus_beta": mediant - beta_hi,
        "alpha_minus_mediant": alpha_lo - mediant,
        "upper_minus_alpha": upper - alpha_hi,
        "beta_minus_previous_charge": (
            beta_lo - Fraction(charge_floor - 1, length_floor)
        ),
    }

    payload = {
        "experiment": "X-8612",
        "status": "exact arithmetic certificate",
        "external_premise": (
            f"every positive integer n < 2^{verified_exponent} reaches {{1,2}}"
        ),
        "verified_exponent": verified_exponent,
        "minimum_cycle_state_under_premise": x_min,
        "alpha_definition": "log_2(4/3)",
        "beta_definition": "log_2(4X/(3X+1))",
        "farey_lower": [lower.numerator, lower.denominator],
        "farey_upper": [upper.numerator, upper.denominator],
        "farey_determinant": 1,
        "stern_brocot_iterations": stern_iterations,
        "mediant_charge_length": [mediant.numerator, mediant.denominator],
        "cycle_odd_state_length_floor": length_floor,
        "cycle_signed_charge_floor": charge_floor,
        "cycle_non2_support_floor": charge_floor,
        "interval_decimal": {
            "beta_lower": decimal_text(beta_lo),
            "beta_upper": decimal_text(beta_hi),
            "alpha_lower": decimal_text(alpha_lo),
            "alpha_upper": decimal_text(alpha_hi),
            "mediant": decimal_text(mediant),
        },
        "exact_margins": {key: frac_text(value) for key, value in margins.items()},
        "normal_form_cases": normal_cases,
        "necklace_formula_cases": necklace_cases,
        "sample_weighted_necklaces": {
            f"s={s},w={w}": necklace_count(s, w)
            for s, w in ((16, 2), (16, 4), (18, 2), (18, 4), (18, 6))
        },
    }
    semantic = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["semantic_sha256"] = hashlib.sha256(semantic).hexdigest()
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/canonical.json"),
    )
    parser.add_argument("--check-results", type=Path)
    parser.add_argument(
        "--verified-exponent",
        type=int,
        default=CANONICAL_VERIFIED_EXPONENT,
    )
    args = parser.parse_args()

    payload = build_payload(args.verified_exponent)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text)

    if args.check_results:
        expected = args.check_results.read_text()
        if text != expected:
            raise SystemExit("canonical result mismatch")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
