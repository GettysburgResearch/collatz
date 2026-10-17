#!/usr/bin/env python3
"""Exact checks for the 2-adic repetition-rigidity packet.

This experiment is deliberately dependency-free.  It validates finite
algebraic and combinatorial interfaces used by L-9401, L-9402, T-9401, and
T-9402.  The mathematical claims are proved in the claim files; finite
checks are adversarial tests, not proof of an infinite statement.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Sequence

EXPERIMENT_ID = "X-9401"
PREFIX_MAX = 6
PERIOD_MAX = 6
COMBINATORIAL_WORD_LENGTH = 11
PROFILE_LENGTH = 16_384
PROFILE_ELL = (1, 2, 4, 8, 16, 32, 64)


def word_from_mask(mask: int, length: int) -> tuple[int, ...]:
    """Return a length-``length`` binary word in position order."""

    return tuple((mask >> i) & 1 for i in range(length))


def weighted_word(word: Sequence[int]) -> int:
    """Return sum word[i] * 64^i * 81^(len(word)-1-i)."""

    length = len(word)
    return sum(bit * 64**i * 81 ** (length - 1 - i) for i, bit in enumerate(word))


def periodic_formula(prefix: Sequence[int], period: Sequence[int]) -> tuple[int, int]:
    """Return the unreduced numerator/denominator from L-9401."""

    if not period:
        raise ValueError("period must be nonempty")
    r = len(prefix)
    s = len(period)
    u = weighted_word(prefix) if r else 0
    v = weighted_word(period)
    denominator = 81**r * (81**s - 64**s)
    numerator = 17 * (u * (81**s - 64**s) + 64**r * v)
    return numerator, denominator


def periodic_value(prefix: Sequence[int], period: Sequence[int]) -> Fraction:
    """Evaluate an eventually periodic code by an independent geometric sum."""

    if not period:
        raise ValueError("period must be nonempty")
    r = len(prefix)
    s = len(period)
    prefix_sum = sum(
        (Fraction(17 * bit * 64**i, 81 ** (i + 1)) for i, bit in enumerate(prefix)),
        Fraction(0),
    )
    one_period = sum(
        (
            Fraction(17 * bit * 64 ** (r + j), 81 ** (r + j + 1))
            for j, bit in enumerate(period)
        ),
        Fraction(0),
    )
    ratio = Fraction(64**s, 81**s)
    return prefix_sum + one_period / (1 - ratio)


def code_digit(prefix: Sequence[int], period: Sequence[int], index: int) -> int:
    if index < 0:
        raise ValueError("index must be nonnegative")
    if not period:
        raise ValueError("period must be nonempty")
    if index < len(prefix):
        return prefix[index]
    return period[(index - len(prefix)) % len(period)]


def first_difference(
    left_prefix: Sequence[int],
    left_period: Sequence[int],
    right_prefix: Sequence[int],
    right_period: Sequence[int],
) -> int | None:
    """Find the first difference, or None if the eventual codes are identical."""

    transient = max(len(left_prefix), len(right_prefix))
    cycle = math.lcm(len(left_period), len(right_period))
    # One full joint period after both transients decides equality forever.
    for index in range(transient + cycle):
        if code_digit(left_prefix, left_period, index) != code_digit(
            right_prefix, right_period, index
        ):
            return index
    return None


def v2_integer(value: int) -> int:
    if value == 0:
        raise ValueError("v2(0) is infinite")
    value = abs(value)
    return (value & -value).bit_length() - 1


def check_periodic_height() -> dict[str, int]:
    cases = 0
    boundary_zero = 0
    boundary_one = 0
    for r in range(PREFIX_MAX + 1):
        for s in range(1, PERIOD_MAX + 1):
            for prefix_mask in range(1 << r):
                prefix = word_from_mask(prefix_mask, r)
                for period_mask in range(1 << s):
                    period = word_from_mask(period_mask, s)
                    numerator, denominator = periodic_formula(prefix, period)
                    formula_value = Fraction(numerator, denominator)
                    direct_value = periodic_value(prefix, period)
                    assert formula_value == direct_value
                    assert denominator % 2 == 1
                    assert direct_value.denominator % 2 == 1
                    assert denominator < 81 ** (r + s)
                    assert 0 <= direct_value <= 1
                    assert denominator % direct_value.denominator == 0
                    if direct_value == 0:
                        boundary_zero += 1
                    if direct_value == 1:
                        boundary_one += 1
                    cases += 1
    return {
        "cases": cases,
        "zero_value_representations": boundary_zero,
        "one_value_representations": boundary_one,
    }


def small_eventual_codes() -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    codes: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for r in range(3):
        for s in range(1, 4):
            for prefix_mask in range(1 << r):
                prefix = word_from_mask(prefix_mask, r)
                for period_mask in range(1 << s):
                    period = word_from_mask(period_mask, s)
                    codes.append((prefix, period))
    return codes


def check_first_difference_valuation() -> dict[str, int]:
    codes = small_eventual_codes()
    distinct_pairs = 0
    duplicate_presentations = 0
    max_first_difference = 0
    for (lp, lv), (rp, rv) in combinations(codes, 2):
        m = first_difference(lp, lv, rp, rv)
        left = periodic_value(lp, lv)
        right = periodic_value(rp, rv)
        if m is None:
            assert left == right
            duplicate_presentations += 1
            continue
        assert left != right
        difference = left - right
        assert difference.denominator % 2 == 1
        assert v2_integer(difference.numerator) == 6 * m
        distinct_pairs += 1
        max_first_difference = max(max_first_difference, m)
    return {
        "eventual_code_presentations": len(codes),
        "distinct_pairs_checked": distinct_pairs,
        "duplicate_presentations": duplicate_presentations,
        "max_first_difference": max_first_difference,
    }


def periodic_continuation_digit(word: Sequence[int], r: int, t: int, index: int) -> int:
    if index < r:
        return word[index]
    return word[r + ((index - r) % (t - r))]


def check_repetition_prefix_combinatorics() -> dict[str, int]:
    length = COMBINATORIAL_WORD_LENGTH
    repeated_factor_instances = 0
    overlapping_instances = 0
    maximum_shared_prefix = 0
    for mask in range(1 << length):
        word = word_from_mask(mask, length)
        for r in range(length):
            for t in range(r + 1, length):
                max_ell = length - t
                for ell in range(1, max_ell + 1):
                    if word[r : r + ell] != word[t : t + ell]:
                        continue
                    target = t + ell
                    for index in range(target):
                        assert periodic_continuation_digit(word, r, t, index) == word[index]
                    repeated_factor_instances += 1
                    if ell > t - r:
                        overlapping_instances += 1
                    maximum_shared_prefix = max(maximum_shared_prefix, target)
    return {
        "word_length": length,
        "words_exhausted": 1 << length,
        "repeated_factor_instances": repeated_factor_instances,
        "overlapping_instances": overlapping_instances,
        "maximum_shared_prefix": maximum_shared_prefix,
    }


def fibonacci_word(length: int) -> bytes:
    word = "0"
    while len(word) < length:
        word = "".join("01" if symbol == "0" else "0" for symbol in word)
    return word[:length].encode("ascii")


def thue_morse_word(length: int) -> bytes:
    return bytes(48 + (index.bit_count() & 1) for index in range(length))


def period_doubling_word(length: int) -> bytes:
    # Fixed point of 0 -> 01, 1 -> 00; equivalently v2(n+1) mod 2.
    return bytes(48 + (v2_integer(index + 1) & 1) for index in range(length))


def pseudorandom_word(length: int) -> bytes:
    rng = random.Random(9401)
    return bytes(48 + rng.getrandbits(1) for _ in range(length))


def finite_factor_complexity(word: bytes, ell: int) -> int:
    if ell <= 0 or ell > len(word):
        raise ValueError("invalid factor length")
    return len({word[start : start + ell] for start in range(len(word) - ell + 1)})


def profile_complexities() -> dict[str, object]:
    generators = {
        "fibonacci": fibonacci_word,
        "thue_morse": thue_morse_word,
        "period_doubling": period_doubling_word,
        "pseudorandom_seed_9401": pseudorandom_word,
    }
    profiles: dict[str, object] = {}
    for name, generator in generators.items():
        word = generator(PROFILE_LENGTH)
        values = {str(ell): finite_factor_complexity(word, ell) for ell in PROFILE_ELL}
        profiles[name] = {
            "prefix_length": PROFILE_LENGTH,
            "complexity": values,
            "max_profile_ratio": max(values[str(ell)] / ell for ell in PROFILE_ELL),
            "prefix_sha256": hashlib.sha256(word).hexdigest(),
        }
    # A sufficiently long Fibonacci prefix contains all factors through 64.
    for ell in PROFILE_ELL:
        assert profiles["fibonacci"]["complexity"][str(ell)] == ell + 1  # type: ignore[index]
    return profiles


def run_all() -> dict[str, object]:
    delta = math.log(81, 64) - 1.0
    kappa = 1.0 / delta
    assert periodic_value((), (0,)) == 0
    assert periodic_value((), (1,)) == 1
    return {
        "experiment_id": EXPERIMENT_ID,
        "schema_version": 1,
        "parameters": {
            "prefix_max": PREFIX_MAX,
            "period_max": PERIOD_MAX,
            "combinatorial_word_length": COMBINATORIAL_WORD_LENGTH,
            "profile_length": PROFILE_LENGTH,
            "profile_ell": list(PROFILE_ELL),
        },
        "constants": {
            "delta_log64_81_minus_1": format(delta, ".16g"),
            "kappa_reciprocal": format(kappa, ".16g"),
        },
        "periodic_height": check_periodic_height(),
        "first_difference_valuation": check_first_difference_valuation(),
        "repetition_prefix_combinatorics": check_repetition_prefix_combinatorics(),
        "illustrative_factor_complexity": profile_complexities(),
        "interpretation": {
            "proved_by_finite_computation": [
                "the frozen finite formula test range",
                "the frozen finite first-difference sample",
                "the frozen finite repetition-prefix census",
            ],
            "not_proved_by_finite_computation": [
                "existence or nonexistence of a nontrivial ordinary survivor",
                "T-9401 for arbitrary infinite codes",
                "T-9402 for arbitrary infinite codes",
                "a directive-to-output complexity transfer theorem",
            ],
        },
    }


def canonical_bytes(results: dict[str, object]) -> bytes:
    return (json.dumps(results, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-results", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    results = run_all()
    payload = canonical_bytes(results)

    if args.write_results is not None:
        args.write_results.parent.mkdir(parents=True, exist_ok=True)
        args.write_results.write_bytes(payload)

    if args.check_results is not None:
        committed = args.check_results.read_bytes()
        if committed != payload:
            raise SystemExit(
                f"result mismatch: generated sha256={hashlib.sha256(payload).hexdigest()} "
                f"committed sha256={hashlib.sha256(committed).hexdigest()}"
            )

    print(payload.decode("utf-8"), end="")
    print(f"canonical_sha256={hashlib.sha256(payload).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
