#!/usr/bin/env python3
"""Independent exact verifier for the bounded-power length certificates.

Does not import the producer. Recomputes affine maps by rational evaluation
at 0 and 1, checks each physical fixed cycle, and checks the integer tail
threshold. It checks certificate arithmetic, not the published analytic
theorem or an unexecuted cycle enumeration. Checks remain active under -O.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def rational_word(word: str, x: int) -> Fraction:
    y = Fraction(x)
    for bit in word:
        y = (3 * y + 1) / 2 if bit == "1" else y / 2
    return y


def check_min_binary_ceiling(value: Fraction | int, b: int, label: str) -> None:
    require(isinstance(b, int) and b >= 0, label + ": invalid exponent")
    require(value <= 2**b, label + ": insufficient bound")
    require(b == 0 or value > 2 ** (b - 1), label + ": not the claimed minimum")


def check_threshold(row: dict) -> None:
    r, b, d, q = (row[key] for key in ("r", "b", "d", "q"))
    require(all(isinstance(x, int) for x in (r, b, d, q)), "threshold types")
    require(r > 0 and min(b, d, q) >= 0, "threshold signs")
    a = 2**r - 1
    c = b + 3 * 8589934592 + 1 + d
    j = a * c
    require(row["A"] == a and row["C_budget"] == c and row["J"] == j, "budget arithmetic")
    require(row["threshold_rhs"] == j * (q + 2), "threshold right side")
    require(row["strict_length_upper_bound"] == 2**q, "length upper bound")
    require(j * (q + 2) <= 2**q, "tail threshold failed")
    require(q == 0 or j * (q + 1) > 2 ** (q - 1), "threshold was not minimal")


def physical_fixed_cycle(word: str, x: int) -> list[int]:
    n, states = x, []
    for bit in word:
        require(n > 0 and n % 2 == int(bit), "fixed-cycle parity or positivity")
        states.append(n)
        n = n // 2 if n % 2 == 0 else (3 * n + 1) // 2
    require(n == x, "fixed-cycle closing edge")
    if x in states[1:]:
        states = states[: states.index(x, 1)]
    minimum = min(states)
    pivot = states.index(minimum)
    return states[pivot:] + states[:pivot]


def check_schema(row: dict) -> None:
    data = row["affine_blocks"]
    require(len(data) == row["r"] and len(data) > 0, "block count")
    b_value = Fraction(0)
    coeff = 0
    expected_fixed = []
    for index, block in enumerate(data):
        word = block["word"]
        require(isinstance(word, str) and len(word) > 0 and set(word) <= {"0", "1"}, "invalid word")
        length, odd_count = len(word), word.count("1")
        zero, one = rational_word(word, 0), rational_word(word, 1)
        a_value = (one - zero) * 2**length
        c_value = zero * 2**length
        require(a_value.denominator == 1 and c_value.denominator == 1, "affine integrality")
        a, c = a_value.numerator, c_value.numerator
        d = 2**length - a
        require(block["length"] == length and block["odd_count"] == odd_count, "block combinatorics")
        require(a == 3**odd_count and block["a"] == a and block["C"] == c and block["D"] == d, "affine coefficients")
        require(d != 0 and d % 2 == 1 and c >= 0, "affine sign or denominator")
        b_value += 2 * abs(Fraction(c, d))
        coeff = max(coeff, abs(d) + c)
        if d > 0 and c > 0 and c % d == 0:
            x = c // d
            expected_fixed.append({"block_index": index, "entry": x, "primitive_cycle": physical_fixed_cycle(word, x)})
    require(row["B"] == [b_value.numerator, b_value.denominator], "rotation translation bound")
    require(row["max_divisibility_coefficient"] == coeff, "divisibility coefficient")
    require(row["fixed_block_cycles"] == expected_fixed, "fixed-block exception set")
    check_min_binary_ceiling(b_value + 1, row["b"], "translation binary ceiling")
    check_min_binary_ceiling(coeff, row["d"], "divisibility binary ceiling")
    check_threshold(row)


def check_uniform(row: dict) -> None:
    r, h = row["r"], row["maximum_base_length"]
    require(isinstance(r, int) and isinstance(h, int) and min(r, h) > 0, "uniform parameters")
    require(row["B"] == 2 * r * 3**h and row["d"] == 2 * h + 1, "uniform constants")
    check_min_binary_ceiling(row["B"] + 1, row["b"], "uniform translation binary ceiling")
    check_threshold(row)


def verify(cert: dict) -> dict:
    require(cert["format"] == "collatz-bounded-power-bound-v1", "certificate format")
    require(cert["matveev_K"] == 8589934592, "external theorem specialization")
    require(cert["scope"] == {
        "independent_nonnegative_exponents": True,
        "positive_integer_cycles_only": True,
        "full_cycle_enumeration_executed": False,
        "external_logarithm_theorem": "Matveev 2000 II, Corollary 2.3",
    }, "claim scope")
    require(len(cert["schemas"]) > 0 and len(cert["uniform_bounds"]) > 0, "empty certificate")
    for row in cert["schemas"]:
        check_schema(row)
    for row in cert["uniform_bounds"]:
        check_uniform(row)
    return {"schemas": len(cert["schemas"]), "uniform_bounds": len(cert["uniform_bounds"])}


def rejection_controls(cert: dict) -> int:
    cases = []
    bad = copy.deepcopy(cert)
    bad["matveev_K"] = 1
    cases.append(bad)
    bad = copy.deepcopy(cert)
    bad["schemas"][0]["affine_blocks"][0]["C"] += 1
    cases.append(bad)
    bad = copy.deepcopy(cert)
    bad["schemas"][0]["q"] -= 1
    cases.append(bad)
    bad = copy.deepcopy(cert)
    bad["schemas"][2]["fixed_block_cycles"] = []
    cases.append(bad)
    for index, bad in enumerate(cases):
        try:
            verify(bad)
        except (ValueError, KeyError, TypeError):
            continue
        raise ValueError(f"damaged certificate {index} was incorrectly accepted")
    return len(cases)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?", type=Path, default=Path(__file__).with_name("bounded_power_certificates.json"))
    parser.add_argument("--rejection-controls", action="store_true")
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    cert = json.loads(raw)
    result = {"status": "PASS", "sha256": hashlib.sha256(raw).hexdigest(), **verify(cert)}
    if args.rejection_controls:
        result["damaged_certificates_rejected"] = rejection_controls(cert)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
