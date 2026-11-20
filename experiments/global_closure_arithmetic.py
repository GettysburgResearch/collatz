#!/usr/bin/env python3
"""Bounded exact replay of GA-001--GA-005 in global-closure-20261120.

The uniform claims are proved in research/global-closure-20261120/arithmetic.md.
This executable neither proves Collatz nor constructs an infinite orbit.
It uses Python's standard library only. Saved reports have no timestamps.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256, shake_256
import json
from math import comb, gcd, isqrt, prod
from pathlib import Path


SCHEMA = "collatz-global-arithmetic-v1"
EDGE_COUNTS = (1, 2, 3, 4, 8, 16, 32, 64)


def valuation_two(n: int) -> int:
    if n <= 0:
        raise ValueError("valuation requires a positive integer")
    return (n & -n).bit_length() - 1


def runs(n: int) -> int:
    if n < 0:
        raise ValueError("run count requires a nonnegative integer")
    return (n & ~(n << 1)).bit_count()


def runs_from_string(n: int) -> int:
    if n == 0:
        return 0
    return 1 + bin(n)[2:].count("01")


def odd_step(n: int) -> tuple[int, int]:
    if n <= 0 or n % 2 == 0:
        raise ValueError("source must be positive odd")
    affine = 3 * n + 1
    a = valuation_two(affine)
    return affine >> a, a


def clock(n: int) -> int:
    if n <= 0 or n % 2 == 0:
        raise ValueError("clock requires a positive odd source")
    return valuation_two(n + 1) - 1


def integer_hash(n: int) -> str:
    return sha256(n.to_bytes(max(1, (n.bit_length() + 7) // 8), "big")).hexdigest()


def rational_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def check_complete_small_residue_counts() -> dict:
    words = 0
    permutation_points = 0
    for length in range(1, 13):
        observed = Counter(runs(n) for n in range(0, 1 << length, 2))
        for count in range(length + 1):
            expected = comb(length, 2 * count) if 2 * count <= length else 0
            assert observed[count] == expected
        for n in range(0, 1 << length, 2):
            assert runs(n) == runs_from_string(n)
            words += 1
        if length <= 10:
            modulus = 1 << length
            expected_even = list(range(0, modulus, 2))
            for multiplier in (1, 3, 5, 9, 15):
                actual = sorted((multiplier * v - 1) % modulus
                                for v in range(1, modulus, 2))
                assert actual == expected_even
                permutation_points += modulus // 2
    return {
        "complete_even_word_lengths": [1, 12],
        "even_words_checked": words,
        "odd_multiplier_permutation_lengths": [1, 10],
        "odd_multipliers": [1, 3, 5, 9, 15],
        "permutation_points_checked": permutation_points,
    }


def find_parameter(m: int, length: int, multiplier: int, mode: str) -> tuple[int, int]:
    """A finite exhaustive order, starting at a deterministic dispersed point.

    Cycling by two through the lower length-1 bits enumerates every odd
    length-bit candidate. GA-002 proves that at least one candidate works.
    The hash only chooses the starting point; termination does not assume
    that a hash sequence eventually hits a good source.
    """
    if m < 2 or length % 16 or multiplier <= 0 or multiplier % 2 == 0:
        raise ValueError("GA-002 domain violation")
    quarter = length // 4
    assert 4 * m * pow(16, quarter) < pow(27, quarter)
    lower_mask = (1 << (length - 1)) - 1
    modulus_mask = (1 << length) - 1
    seed = f"{SCHEMA}|{mode}|m={m}|L={length}".encode("ascii")
    raw = int.from_bytes(shake_256(seed).digest((length + 7) // 8), "big")
    first_lower = (raw & lower_mask) | 1
    attempts = 0
    number_of_candidates = 1 << (length - 2)
    while attempts < number_of_candidates:
        lower = (first_lower + 2 * attempts) & lower_mask
        v = (1 << (length - 1)) | lower
        attempts += 1
        residue = (multiplier * v) & modulus_mask
        good = True
        for _ in range(m):
            assert residue & 1
            if runs(residue - 1) < length // 8:
                good = False
                break
            residue = (3 * residue) & modulus_mask
        if good:
            assert v.bit_length() == length and v & 1
            return v, attempts
    raise AssertionError("GA-002 counting bound contradicted")


def replay_block(edges: int, mode: str) -> dict:
    m = edges + 1
    if mode == "linear_height":
        length = 16 * m
        multiplier = 1
        bitlength_bound = 18 * m - 1
    elif mode == "pairwise_coprime":
        length = 16 * m * m
        multiplier = prod(pow(3, d) - pow(2, d) for d in range(1, m))
        multiplier *= prod(2 * k - 1 for k in range(1, m + 1))
        bitlength_bound = 18 * m * m + m - 1
        assert multiplier < 1 << (2 * m * m - m)
    else:
        raise ValueError("unknown regime")
    v, attempts = find_parameter(m, length, multiplier, mode)
    scaled = multiplier * v
    nodes = []
    suffix_counts = []
    full_counts = []
    mask = (1 << length) - 1
    for i in range(m):
        n = (scaled << (m - i)) - 1
        suffix = (scaled - 1) & mask
        assert n > 1 and n & 1
        assert runs(suffix) >= length // 8
        assert runs(suffix) == runs_from_string(suffix)
        assert runs(n) == runs_from_string(n)
        assert runs(n) == runs(scaled - 1) + 1
        assert runs(n) >= length // 8 + 1
        assert 10 * runs(n) > n.bit_length()
        assert n.bit_length() <= bitlength_bound
        assert n.bit_count() >= runs(n)
        nodes.append(n)
        suffix_counts.append(runs(suffix))
        full_counts.append(runs(n))
        scaled *= 3
    assert clock(nodes[0]) == edges
    if mode == "linear_height":
        assert nodes[0].bit_length() == 17 * m
    for i in range(edges):
        actual, a = odd_step(nodes[i])
        assert a == 1 and actual == nodes[i + 1]
        assert 2 * actual > 3 * nodes[i]
        assert actual < 2 * nodes[i]
        assert clock(actual) == clock(nodes[i]) - 1
    _, endpoint_valuation = odd_step(nodes[-1])
    assert endpoint_valuation >= 2 and clock(nodes[-1]) == 0

    pair_checks = 0
    nontrivial_gcds = 0
    roughness_checks = 0
    for i in range(m):
        for j in range(i + 1, m):
            distance = j - i
            correction = pow(3, distance) - pow(2, distance)
            assert (nodes[j] << distance) == pow(3, distance) * nodes[i] + correction
            common = gcd(nodes[i], nodes[j])
            assert correction % common == 0
            nontrivial_gcds += int(common > 1)
            if mode == "pairwise_coprime":
                assert common == 1
            # Exact consequence for the extremal interval containing these nodes.
            width = nodes[j] - nodes[i]
            assert pow(3, distance) < pow(2, distance) * (width + 1)
            pair_checks += 1
    if mode == "pairwise_coprime":
        small_odd_multiple = prod(2 * k - 1 for k in range(1, m + 1))
        for n in nodes:
            assert n % multiplier == multiplier - 1
            assert gcd(n, small_odd_multiple) == 1
            roughness_checks += 1
        h_lower = length + m - 2
        coefficient = Fraction(h_lower + edges, m * h_lower)
        claimed = Fraction(1, m) * (1 + Fraction(1, 16 * m))
        assert coefficient < claimed
        prime_certificate = {
            "method": "all distinct-state gcds equal one; no full factorization",
            "height_share_upper_coefficient_per_prime": rational_text(coefficient),
            "normalized_count_share_upper_coefficient_per_prime": f"1/{m}",
            "excluded_prime_upper_bound": 2 * m - 1,
        }
    else:
        r = isqrt(m)
        if r * r < m:
            r += 1
        blocks = (m + r - 1) // r
        h_lower = 17 * m - 2
        height_upper = 18 * m - 1
        assert Fraction(height_upper, h_lower) <= Fraction(9, 8)
        assert h_lower >= 16 * m
        coefficient = Fraction(blocks * height_upper + r * m, m * h_lower)
        simple = Fraction(9, 8) * (Fraction(1, r) + Fraction(1, m))
        simple += Fraction(r, 16 * m)
        assert coefficient <= simple
        prime_certificate = {
            "method": "exact affine gcd constants and blocks; no full factorization",
            "block_length": r,
            "number_of_blocks": blocks,
            "height_and_normalized_count_share_upper_coefficient_per_prime": rational_text(coefficient),
        }
    result = {
        "mode": mode,
        "odd_edges": edges,
        "states": m,
        "parameter_bitlength": length,
        "multiplier_bitlength": multiplier.bit_length(),
        "source_bitlength": nodes[0].bit_length(),
        "largest_state_bitlength": max(n.bit_length() for n in nodes),
        "proved_state_bitlength_bound": bitlength_bound,
        "minimum_one_runs": min(full_counts),
        "minimum_suffix_one_runs": min(suffix_counts),
        "proved_one_run_lower_bound": length // 8 + 1,
        "candidates_checked": attempts,
        "parameter_sha256": integer_hash(v),
        "source_sha256": integer_hash(nodes[0]),
        "endpoint_sha256": integer_hash(nodes[-1]),
        "all_state_pair_checks": pair_checks,
        "nontrivial_gcds": nontrivial_gcds,
        "small_prime_exclusion_checks": roughness_checks,
        "valuation_after_displayed_block": endpoint_valuation,
        "prime_height_certificate": prime_certificate,
    }
    if edges <= 4:
        result["source_hex"] = hex(nodes[0])
    return result


def check_recharge_family() -> dict:
    parameters = tuple(range(1, 129)) + (256, 1024, 4096)
    literal_edges = 0
    for m in parameters:
        z = (1 << (m + 3)) - 3
        x = 3 * (1 << m) - 1
        image, a = odd_step(z)
        assert image == x and a == 3
        assert clock(z) == 0 and clock(x) == m - 1
        assert x < z < 4 * x
        assert runs(z) == runs(x) == 2
        assert z.bit_count() == m + 2 and x.bit_count() == m + 1
        current = x
        for j in range(m - 1):
            following, a = odd_step(current)
            assert a == 1 and following > current
            assert clock(current) == m - 1 - j
            current = following
        assert current == 2 * pow(3, m) - 1
        assert clock(current) == 0
        assert odd_step(current)[1] >= 2
        literal_edges += m
    coefficient_examples = [
        (Fraction(1), Fraction(7), Fraction(100), Fraction(100)),
        (Fraction(1, 2), Fraction(-1000), Fraction(-8), Fraction(9)),
        (Fraction(3), Fraction(0), Fraction(0), Fraction(-100)),
    ]
    potential_examples = []
    for lam, mu, nu, kappa in coefficient_examples:
        threshold = (abs(nu) + 2 * abs(kappa)) / lam
        m = threshold.numerator // threshold.denominator + 3
        lower = lam * (m - 1) - abs(nu) - 2 * abs(kappa)
        assert lower > 0
        z = (1 << (m + 3)) - 3
        x = 3 * (1 << m) - 1
        assert odd_step(z) == (x, 3)
        assert runs(z) == runs(x) == 2
        assert z.bit_count() - x.bit_count() == 1
        assert x < z < 4 * x
        potential_examples.append({
            "coefficients_lambda_mu_nu_kappa": list(map(rational_text, (lam, mu, nu, kappa))),
            "m": m,
            "certified_potential_increase_lower_bound": rational_text(lower),
        })
    return {
        "parameters_m": list(parameters),
        "families_checked": len(parameters),
        "literal_odd_edges_checked": literal_edges,
        "largest_recharge": max(parameters) - 1,
        "fixed_reset_valuation": 3,
        "potential_counterexamples": potential_examples,
    }


def check_failed_strengthenings() -> dict:
    off_by_one = []
    for requested_edges in (1, 2, 8, 32):
        # The tempting source 2^N*u-1 has N-1, not N, valuation-one edges.
        source = (3 << requested_edges) - 1
        assert clock(source) == requested_edges - 1
        current = source
        for _ in range(requested_edges - 1):
            current, a = odd_step(current)
            assert a == 1
        assert odd_step(current)[1] >= 2
        off_by_one.append(requested_edges)
    sample = [15, 23, 35, 53]
    assert all(odd_step(a) == (b, 1) for a, b in zip(sample, sample[1:]))
    assert gcd(sample[0], sample[2]) == 5
    even_multiplier_rejected = False
    try:
        find_parameter(2, 32, 2, "invalid")
    except ValueError:
        even_multiplier_rejected = True
    assert even_multiplier_rejected
    return {
        "missing_extra_power_of_two_rejected_for_N": off_by_one,
        "pairwise_coprime_without_multiplier_counterexample": {
            "actual_orbit_segment": sample,
            "gcd_of_first_and_third": 5,
        },
        "even_multiplier_domain_violation_rejected": even_multiplier_rejected,
    }


def build_report() -> dict:
    small = check_complete_small_residue_counts()
    cases = [replay_block(n, mode)
             for mode in ("linear_height", "pairwise_coprime")
             for n in EDGE_COUNTS]
    recharge = check_recharge_family()
    negative = check_failed_strengthenings()
    return {
        "schema": SCHEMA,
        "status": "PASS",
        "scope": "bounded exact-integer replay; no formal verification or global Collatz resolution",
        "claims": ["GA-001", "GA-002", "GA-003", "GA-004", "GA-005"],
        "complete_small_residue_checks": small,
        "block_cases": cases,
        "block_totals": {
            "cases": len(cases),
            "literal_odd_edges": sum(c["odd_edges"] for c in cases),
            "states": sum(c["states"] for c in cases),
            "all_state_pair_checks": sum(c["all_state_pair_checks"] for c in cases),
            "small_prime_exclusion_checks": sum(c["small_prime_exclusion_checks"] for c in cases),
            "largest_state_bitlength": max(c["largest_state_bitlength"] for c in cases),
            "maximum_candidates_needed": max(c["candidates_checked"] for c in cases),
        },
        "recharge_checks": recharge,
        "failed_strengthenings": negative,
        "limitations": [
            "Different requested block lengths use different ordinary sources.",
            "Each displayed block ends before an actual valuation of at least two.",
            "Large states are not factored; uniform prime-set bounds rest on the written gcd arguments.",
            "No assertion about the subsequent convergence or divergence of these sources is made.",
            "Finite replay does not replace the universal written proofs or independent mathematical review.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path, help="write a new report; refuse to replace an existing path")
    group.add_argument("--compare", type=Path, help="regenerate and compare with an existing report")
    args = parser.parse_args()
    if args.output is not None and args.output.exists():
        parser.error(f"output already exists: {args.output}")
    report = build_report()
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.compare is not None:
        expected = args.compare.read_text(encoding="utf-8")
        if encoded != expected:
            raise SystemExit("FAIL: regenerated report differs")
        print("PASS: exact regeneration matches saved report")
    elif args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(encoded)
        print(f"PASS: wrote {args.output}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("verification requires assertions; optimized Python is not supported")
    main()
