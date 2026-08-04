#!/usr/bin/env python3
"""X-9402: exact finite checks for the complexity-criticality packet.

The universal statements live in the accompanying proofs. This program checks
finite algebraic interfaces with exact Fraction/integer arithmetic and profiles
finite-state complexity transfer without using an external solver.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Any


def v2(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0) is undefined")
    n = abs(n)
    return (n & -n).bit_length() - 1


def eventual_value(
    prefix: tuple[int, ...], period: tuple[int, ...], M: int, N: int
) -> Fraction:
    if not period:
        raise ValueError("period must be nonempty")
    r = len(prefix)
    s = len(period)
    U = sum(d * M**i * N ** (r - 1 - i) for i, d in enumerate(prefix))
    V = sum(d * M**j * N ** (s - 1 - j) for j, d in enumerate(period))
    numerator = (N - M) * (U * (N**s - M**s) + M**r * V)
    denominator = N**r * (N**s - M**s)
    return Fraction(numerator, denominator)


def eventual_value_direct(
    prefix: tuple[int, ...], period: tuple[int, ...], M: int, N: int
) -> Fraction:
    r = len(prefix)
    s = len(period)
    z = Fraction(M, N)
    prefix_sum = sum((d * z**i for i, d in enumerate(prefix)), Fraction(0))
    period_sum = sum((d * z**j for j, d in enumerate(period)), Fraction(0))
    return Fraction(N - M, N) * (
        prefix_sum + z**r * period_sum / (1 - z**s)
    )


def finite_value(word: tuple[int, ...], M: int, N: int) -> Fraction:
    return sum(
        (
            Fraction((N - M) * d * M**i, N ** (i + 1))
            for i, d in enumerate(word)
        ),
        Fraction(0),
    )


def fibonacci_word(length: int) -> tuple[int, ...]:
    word = "0"
    while len(word) < length:
        word = "".join("01" if c == "0" else "0" for c in word)
    return tuple(int(c) for c in word[:length])


def periodic_height_checks(charts: list[dict[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for chart in charts:
        M, N = chart["M"], chart["N"]
        digits = tuple(chart["digits"])
        count = 0
        max_reduced_denominator_ratio = Fraction(0)
        for r in range(4):
            for s in range(1, 4):
                for prefix in product(digits, repeat=r):
                    for period in product(digits, repeat=s):
                        y = eventual_value(prefix, period, M, N)
                        y_direct = eventual_value_direct(prefix, period, M, N)
                        assert y == y_direct
                        Q = N**r * (N**s - M**s)
                        assert Q % 2 == 1
                        assert y.denominator % 2 == 1
                        assert Q % y.denominator == 0
                        assert y.denominator < N ** (r + s)
                        assert min(digits) <= y <= max(digits)
                        ratio = Fraction(y.denominator, N ** (r + s))
                        max_reduced_denominator_ratio = max(
                            max_reduced_denominator_ratio, ratio
                        )
                        count += 1
        out[chart["name"]] = {
            "cases": count,
            "max_reduced_denominator_ratio": (
                f"{float(max_reduced_denominator_ratio):.12f}"
            ),
        }
    return out


def first_difference_checks(charts: list[dict[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for chart in charts:
        M, N = chart["M"], chart["N"]
        digits = tuple(chart["digits"])
        L = M.bit_length() - 1
        assert M == 1 << L and N % 2 == 1 and N > M
        words = list(product(digits, repeat=4))
        count = 0
        valuation_min = 10**9
        valuation_max = -1
        for left, right in combinations(words, 2):
            m = next(i for i, (a, b) in enumerate(zip(left, right)) if a != b)
            diff = finite_value(left, M, N) - finite_value(right, M, N)
            assert diff.denominator % 2 == 1
            got = v2(diff.numerator)
            want = L * m + v2(left[m] - right[m])
            assert got == want
            valuation_min = min(valuation_min, got)
            valuation_max = max(valuation_max, got)
            count += 1
        out[chart["name"]] = {
            "distinct_pairs": count,
            "valuation_min": valuation_min,
            "valuation_max": valuation_max,
        }
    return out


def random_transducer(
    rng: random.Random, Q: int, B: int
) -> tuple[dict[tuple[int, int], int], dict[tuple[int, int], str]]:
    delta: dict[tuple[int, int], int] = {}
    emit: dict[tuple[int, int], str] = {}
    for q in range(Q):
        for a in (0, 1):
            delta[(q, a)] = rng.randrange(Q)
            length = rng.randrange(1, B + 1)
            emit[(q, a)] = "".join(str(rng.randrange(2)) for _ in range(length))
    return delta, emit


def transducer_bound_checks() -> dict[str, Any]:
    directive = fibonacci_word(700)
    rng = random.Random(9402)
    ell_values = (1, 2, 4, 8, 16, 24, 32)
    machines = 0
    inequalities = 0
    max_factor_to_envelope = 0.0

    for Q in range(1, 5):
        for B in range(1, 5):
            for _ in range(8):
                delta, emit = random_transducer(rng, Q, B)
                states: list[int] = []
                blocks: list[str] = []
                q = 0
                for a in directive:
                    states.append(q)
                    blocks.append(emit[(q, a)])
                    q = delta[(q, a)]
                for ell in ell_values:
                    factors: set[str] = set()
                    keys: set[tuple[int, int, tuple[int, ...]]] = set()
                    input_factors: set[tuple[int, ...]] = set()
                    for i in range(0, len(directive) - ell + 1):
                        u = directive[i : i + ell]
                        input_factors.add(u)
                        material = "".join(blocks[i : i + ell])
                        for offset in range(len(blocks[i])):
                            factor = material[offset : offset + ell]
                            assert len(factor) == ell
                            factors.add(factor)
                            keys.add((states[i], offset, u))
                    envelope = Q * B * len(input_factors)
                    assert len(factors) <= len(keys) <= envelope
                    max_factor_to_envelope = max(
                        max_factor_to_envelope, len(factors) / envelope
                    )
                    inequalities += 1
                machines += 1

    # Exact finite-radius/sliding-block check. Each binary radius-1 local map
    # is one of 2^8 truth tables; an output length-ell factor is determined by
    # an input length-(ell+2) factor.
    x = fibonacci_word(1200)
    sliding_maps = 0
    sliding_inequalities = 0
    for table_bits in product((0, 1), repeat=8):
        table = {
            triple: table_bits[idx]
            for idx, triple in enumerate(product((0, 1), repeat=3))
        }
        y = tuple(table[x[i : i + 3]] for i in range(len(x) - 2))
        for ell in ell_values:
            py = {y[i : i + ell] for i in range(len(y) - ell + 1)}
            px = {x[i : i + ell + 2] for i in range(len(x) - ell - 1)}
            assert len(py) <= len(px)
            sliding_inequalities += 1
        sliding_maps += 1

    return {
        "directive": "Fibonacci fixed point 0->01, 1->0",
        "directive_length": len(directive),
        "machines": machines,
        "sequential_inequalities": inequalities,
        "max_factor_to_QB_envelope": f"{max_factor_to_envelope:.12f}",
        "sliding_radius_1_maps": sliding_maps,
        "sliding_inequalities": sliding_inequalities,
    }


def gap_quadratic_checks() -> dict[str, Any]:
    C = 162
    directive = fibonacci_word(5000)
    gaps = [9]
    for bit in directive:
        gaps.append(gaps[-1] + (153 if bit == 0 else 162))

    results: dict[str, Any] = {}
    for n in (10_000, 20_000, 40_000, 80_000):
        selected = [
            j
            for j in range(1, len(gaps) - 1)
            if n / 2 <= gaps[j] <= 3 * n / 5
        ]
        offsets_per_gap = max(0, math.floor(2 * n / 5) - 1)
        keys: set[tuple[int, int]] = set()
        for j in selected:
            g = gaps[j]
            for a in range(offsets_per_gap):
                assert a <= gaps[j - 1]
                assert a <= n - g - 2
                # Previous and next ones lie outside; the selected factor has
                # exactly two ones, at offsets a and a+g+1.
                assert a - (gaps[j - 1] + 1) < 0
                assert a + g + 1 < n
                assert a + g + 1 + gaps[j + 1] + 1 >= n
                keys.add((g, a))
        theorem_lower = max(
            0,
            (math.floor(n / (10 * C)) - 1)
            * (math.floor(2 * n / 5) - 1),
        )
        assert len(selected) >= max(0, math.floor(n / (10 * C)) - 1)
        assert len(keys) == len(selected) * offsets_per_gap
        assert len(keys) >= theorem_lower
        results[str(n)] = {
            "selected_gaps": len(selected),
            "constructed_distinct_factors": len(keys),
            "proved_uniform_lower_bound": theorem_lower,
            "constructed_ratio_over_n": f"{len(keys) / n:.9f}",
        }
    return {
        "gap_increment_set": [153, 162],
        "C": C,
        "finite_scales": results,
        "interpretation": (
            "finite replay of the two-one factor construction; "
            "the theorem, not these scales, proves Omega(n^2)"
        ),
    }


def constants(charts: list[dict[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for chart in charts:
        M, N = chart["M"], chart["N"]
        beta = math.log(N) / math.log(M)
        delta = beta - 1.0
        out[chart["name"]] = {
            "M": M,
            "N": N,
            "beta_log_M_N": f"{beta:.15f}",
            "delta": f"{delta:.15f}",
            "kappa_reciprocal_delta": f"{1.0 / delta:.12f}",
        }
    return out


def generate() -> dict[str, Any]:
    charts = [
        {"name": "64_to_81", "M": 64, "N": 81, "digits": [0, 1]},
        {"name": "512_to_729", "M": 512, "N": 729, "digits": [0, 1, 2]},
        {
            "name": "2^17_to_3^11",
            "M": 2**17,
            "N": 3**11,
            "digits": [0, 1, 2, 3],
        },
        {
            "name": "2^22_to_3^14",
            "M": 2**22,
            "N": 3**14,
            "digits": [0, 1, 2],
        },
        {
            "name": "2^44_to_3^28",
            "M": 2**44,
            "N": 3**28,
            "digits": [0, 1],
        },
    ]
    return {
        "schema_version": 1,
        "experiment_id": "X-9402",
        "research_question": (
            "How does ordinary-integer repetition rigidity scale across "
            "expanding digit charts, and what finite-state resources are "
            "needed to transfer a low-complexity directive into a survivor code?"
        ),
        "constants": constants(charts),
        "periodic_height": periodic_height_checks(charts),
        "first_difference": first_difference_checks(charts),
        "finite_state_transfer": transducer_bound_checks(),
        "increasing_gap_output": gap_quadratic_checks(),
        "interpretation": {
            "proved_by_finite_computation": [
                "the frozen periodic-rational formula cases",
                "the frozen first-difference valuation cases",
                "the frozen sequential/sliding-block factor-count inequalities",
                "the frozen increasing-gap two-one factor construction",
            ],
            "not_proved_by_finite_computation": [
                "the universal complexity-criticality theorem",
                "existence or nonexistence of an ordinary survivor",
                "closure or impossibility of the active S-adic stack grammar",
                "any theorem about all collision alphabets without the written proof",
            ],
        },
    }


def canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-results", type=Path)
    parser.add_argument("--check-results", type=Path)
    args = parser.parse_args()

    payload = generate()
    data = canonical_bytes(payload)
    digest = hashlib.sha256(data).hexdigest()

    if args.write_results:
        args.write_results.parent.mkdir(parents=True, exist_ok=True)
        args.write_results.write_bytes(data)
    if args.check_results:
        expected = args.check_results.read_bytes()
        if expected != data:
            raise SystemExit("canonical result mismatch")

    print(data.decode("utf-8"), end="")
    print(f"SHA256 {digest}")


if __name__ == "__main__":
    main()
