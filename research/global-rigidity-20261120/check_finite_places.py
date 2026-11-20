#!/usr/bin/env python3
"""Exact finite replay for FP1; imports only its sibling arithmetic checker."""

from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import json
from math import gcd, lcm
from pathlib import Path

from check_adic_real_density import (
    check_cycle,
    floor_log2_ratio,
    prefix,
    require,
    ternary_exponent,
)


def modular_order(value: int, modulus: int) -> int:
    require(modulus > 1 and gcd(value, modulus) == 1, "modular order domain")
    current = value % modulus
    order = 1
    while current != 1:
        current = current * value % modulus
        order += 1
        require(order <= modulus, "finite unit group order")
    return order


def affine_word(word: list[int]) -> tuple[int, int]:
    q = c = 0
    for k, bit in enumerate(word):
        if bit:
            c = 3 * c + (1 << k)
            q += 1
    return q, c


def modular_gadget(word: list[int], modulus: int, residue: int, a0: int) -> tuple[list[int], int]:
    k = len(word)
    q, c = affine_word(word)
    inverse_two = pow(2, -1, modulus)
    slope = 3**q * pow(inverse_two, k, modulus) % modulus
    shift = c * pow(inverse_two, k, modulus) % modulus
    inverse_slope = pow(slope, -1, modulus)
    scale = pow(2, a0, modulus)
    target = (
        (2 * scale * inverse_slope) % modulus,
        (scale * (-2 * shift * inverse_slope - residue)) % modulus,
    )
    identity = (1, 0)
    queue = deque([identity])
    predecessors: dict[tuple[int, int], tuple[tuple[int, int], int] | None] = {identity: None}
    while queue:
        state = queue.popleft()
        if state == target:
            result: list[int] = []
            cursor = state
            while predecessors[cursor] is not None:
                previous, bit = predecessors[cursor]
                result.append(bit)
                cursor = previous
            result.reverse()
            return result, len(predecessors)
        s, t = state
        for bit in (0, 1):
            if bit:
                nxt = (3 * s * inverse_two % modulus, (3 * t + 1) * inverse_two % modulus)
            else:
                nxt = (s * inverse_two % modulus, t * inverse_two % modulus)
            if nxt not in predecessors:
                predecessors[nxt] = (state, bit)
                queue.append(nxt)
        require(len(predecessors) <= modulus * modulus, "finite affine group size")
    raise RuntimeError("required modular affine gadget was not generated")


def construct(case: dict, max_b: int) -> dict:
    original_k = case["binary_precision"]
    original_z = case["binary_residue"] % (1 << original_k)
    original_word, _, _, _ = prefix(original_z, original_k)
    m, t = case["ternary_precision"], case["ternary_residue"]
    modulus, residue = case["extra_modulus"], case["extra_residue"]
    require(modulus > 1 and gcd(modulus, 6) == 1, "extra modulus domain")
    a0, ternary_period = ternary_exponent(t, m)
    gadget, searched_states = modular_gadget(original_word, modulus, residue, a0)
    word = original_word + gadget
    k = len(word)
    q, c = affine_word(word)
    # The full arbitrary word has exactly this binary source cylinder.
    z = (-c * pow(3**q, -1, 1 << k)) % (1 << k) if k else 0
    require(prefix(z, k)[0] == word, "control word parity cylinder")
    require(z % (1 << original_k) == original_z, "original binary cylinder retained")
    inverse_two = pow(2, -1, modulus)
    a_period = lcm(ternary_period, modular_order(2, modulus))
    b_period = modular_order(3 * inverse_two % modulus, modulus)
    target = Fraction(*case["real_target"])
    error = Fraction(*case["real_error"])
    two_k, three_q = 1 << k, 3**q
    upper_after_prefix = Fraction(three_q, two_k) * (target + error) + Fraction(c, two_k) + 1
    three_b = 1
    for b in range(1, max_b + 1):
        three_b *= 3
        if b < m or b % b_period or (1 << b) <= upper_after_prefix:
            continue
        numerator = three_b * (c + two_k) - (two_k << b)
        slope_numerator = three_q * three_b
        threshold = slope_numerator * target.numerator + numerator * target.denominator
        ideal_a = floor_log2_ratio(threshold, target.numerator) - k - b
        lower = a0 + ((ideal_a - a0) // a_period) * a_period
        for a in (lower, lower + a_period):
            if a < 1:
                continue
            denominator = (1 << (k + a + b)) - slope_numerator
            if denominator <= 0:
                continue
            score = 8 * (q + b) - 5 * (k + a + b)
            if score <= 0:
                continue
            error_numerator = abs(numerator * target.denominator - denominator * target.numerator)
            if error_numerator * error.denominator >= denominator * target.denominator * error.numerator:
                continue
            root = Fraction(numerator, denominator)
            require(root.denominator > 1, "noninteger cycle")
            require(gcd(denominator, modulus) == 1, "full denominator avoids extra primes")
            require(gcd(root.denominator, modulus) == 1, "reduced denominator avoids extra primes")
            require((root.numerator - residue * root.denominator) % modulus == 0, "extra modular agreement")
            n_total = k + a + b
            require(denominator % modulus == -(1 << n_total) % modulus, "full modular denominator identity")
            require(numerator % modulus == -residue * (1 << n_total) % modulus, "full modular numerator identity")
            record = check_cycle({
                "target": target, "error": error,
                "k": k, "z": z, "m": m, "t": t,
                "word": word, "q": q, "c": c,
                "a": a, "b": b, "root": root, "score": score,
                "period": a_period, "a0": a0,
            })
            record.update({
                "original_binary_precision": original_k,
                "original_binary_residue": original_z,
                "extra_modulus": modulus,
                "extra_residue": residue % modulus,
                "control_word": "".join(map(str, gadget)),
                "control_group_states_searched": searched_states,
                "a_progression_modulus": a_period,
                "b_progression_modulus": b_period,
            })
            if target.denominator == 1:
                difference = root.numerator - target.numerator * root.denominator
                controlled_modulus = (1 << original_k) * 3**m * modulus
                if difference % controlled_modulus == 0:
                    require(abs(difference) >= controlled_modulus, "all controlled places denominator cost")
                    require(root.denominator * error > controlled_modulus, "strict all-place cost")
            return record
    raise RuntimeError(f"bounded finite-places witness search exhausted: {case!r}")


CASES = [
    {"real_target": (5, 1), "real_error": (1, 4), "binary_precision": 5, "binary_residue": 5, "ternary_precision": 2, "ternary_residue": 5, "extra_modulus": 5, "extra_residue": 0},
    {"real_target": (7, 1), "real_error": (1, 4), "binary_precision": 7, "binary_residue": 7, "ternary_precision": 2, "ternary_residue": 7, "extra_modulus": 91, "extra_residue": 7},
    {"real_target": (4, 3), "real_error": (1, 20), "binary_precision": 4, "binary_residue": 13, "ternary_precision": 3, "ternary_residue": 2, "extra_modulus": 35, "extra_residue": 28},
    {"real_target": (13, 7), "real_error": (1, 20), "binary_precision": 5, "binary_residue": 18, "ternary_precision": 2, "ternary_residue": 11, "extra_modulus": 25, "extra_residue": 14},
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-b", type=int, default=80000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    require(args.max_b >= 1, "positive max-b")
    cases = [construct(case, args.max_b) for case in CASES]
    report = {
        "status": "PASS",
        "scope": "finite rational-cycle witnesses; no fixed ordinary continuation or full Collatz proof",
        "arithmetic": "integers and exact fractions; checks active under -OO",
        "case_count": len(cases),
        "cases": cases,
        "total_shortcut_edges": sum(case["shortcut_lap_length"] for case in cases),
        "total_accelerated_edges": sum(case["odd_lap_count"] for case in cases),
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
