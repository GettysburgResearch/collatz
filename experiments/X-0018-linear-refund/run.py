#!/usr/bin/env python3
"""X-0018: exact checks for linear-height quotient refund.

Standard-library only. The experiment verifies the phase-34 scaled-tail
cylinders, their overlap quotient map, the arbitrary-width exponent formulas,
and strict ordinary quotient growth above exact certified thresholds.
"""
from __future__ import annotations

import hashlib
import json
from functools import lru_cache
from itertools import product

P = (5, 30, 20, 56)
TOLL = (9, 54, 36, 24)


@lru_cache(maxsize=None)
def odd_multiplier(t: int) -> int:
    return pow(3, 7 * (t + 1))


@lru_cache(maxsize=None)
def binary_radix(t: int) -> int:
    return 1 << (11 * (t + 1))


def exponent_formulas(width: int, base: int) -> tuple[int, int, int, int]:
    if width <= 0 or base < 0:
        raise ValueError("width must be positive and base nonnegative")
    odd = 7 * width * (base + 1) + 56 * width * (width - 1)
    binary = 11 * width * (base + 1) + 88 * width * (width + 1)
    next_binary = 11 * width * (base + 1) + 264 * width * width + 88 * width
    margin = width * (5 * base - 9288 * width - 9363) - 53
    return odd, binary, next_binary, margin


def minimum_certified_base(width: int) -> int:
    numerator = 9288 * width + 9363 + 53 // width
    base = ((numerator // 5 + 1 + 15) // 16) * 16
    while exponent_formulas(width, base)[3] <= 0:
        base += 16
    while base > 16 and exponent_formulas(width, base - 16)[3] > 0:
        base -= 16
    return base


@lru_cache(maxsize=None)
def edge_units(t: int) -> tuple[int, int, int, int]:
    n = odd_multiplier(t)
    q = binary_radix(t + 16)
    modulus = 64 * q
    return n, q, modulus, pow(n, -1, modulus)


@lru_cache(maxsize=None)
def overlap_inverse(t: int) -> int:
    return pow(odd_multiplier(t), -1, binary_radix(t + 32))


@lru_cache(maxsize=None)
def edge_cylinder(t: int, source_type: int, target_type: int) -> tuple[int, int]:
    n, q, modulus, inverse = edge_units(t)
    residue = ((q * P[target_type] - TOLL[source_type]) * inverse) % modulus
    output = (n * residue + TOLL[source_type]) // q
    assert residue % 64 == P[source_type]
    assert output % 64 == P[target_type]
    assert 0 <= residue < modulus
    assert n * residue + TOLL[source_type] == q * output
    return residue, output


@lru_cache(maxsize=None)
def overlap_transition(t: int, i: int, j: int, k: int) -> tuple[int, int, int]:
    _, first_output = edge_cylinder(t, i, j)
    next_input, _ = edge_cylinder(t + 16, j, k)
    assert (first_output - next_input) % 64 == 0
    offset = (first_output - next_input) // 64
    n = odd_multiplier(t)
    q = binary_radix(t + 32)
    residue = (-offset * overlap_inverse(t)) % q
    carry = (n * residue + offset) // q
    assert 0 <= residue < q
    assert carry >= 0
    assert n * residue + offset == q * carry
    return residue, carry, q


def replay_overlap(t: int, i: int, j: int, k: int, high: int) -> tuple[int, int]:
    first_input, first_output = edge_cylinder(t, i, j)
    second_input, _ = edge_cylinder(t + 16, j, k)
    residue, carry, q = overlap_transition(t, i, j, k)
    n = odd_multiplier(t)
    entering = residue + q * high
    leaving = carry + n * high
    w0 = first_input + 64 * binary_radix(t + 16) * entering
    w1_from_first = first_output + 64 * n * entering
    w1_for_second = second_input + 64 * q * leaving
    assert w1_from_first == w1_for_second
    assert binary_radix(t + 16) * w1_from_first == n * w0 + TOLL[i]
    return entering, leaving


@lru_cache(maxsize=None)
def block_units(base: int, width: int) -> tuple[int, int, int]:
    odd = 1
    radix = 1
    for step in range(width):
        odd *= odd_multiplier(base + 16 * step)
        radix *= binary_radix(base + 16 * (step + 1))
    return odd, radix, pow(odd, -1, 64 * radix)


@lru_cache(maxsize=None)
def compose_block(base: int, types: tuple[int, ...]) -> tuple[int, int, int, int]:
    width = len(types) - 1
    if width < 1:
        raise ValueError("a block needs at least one transition")
    odd, radix, inverse = block_units(base, width)
    toll = 0
    partial_radix = 1
    for step, source_type in enumerate(types[:-1]):
        n = odd_multiplier(base + 16 * step)
        toll = n * toll + TOLL[source_type] * partial_radix
        partial_radix *= binary_radix(base + 16 * (step + 1))
    assert partial_radix == radix
    modulus = 64 * radix
    residue = ((radix * P[types[-1]] - toll) * inverse) % modulus
    output = (odd * residue + toll) // radix
    assert residue % 64 == P[types[0]]
    assert output % 64 == P[types[-1]]
    assert odd * residue + toll == radix * output
    return residue, output, odd, radix


@lru_cache(maxsize=None)
def block_overlap_inverse(base: int, width: int) -> int:
    odd, _, _ = block_units(base, width)
    _, next_radix, _ = block_units(base + 16 * width, width)
    return pow(odd, -1, next_radix)


def replay_block_pair(base: int, left: tuple[int, ...], right: tuple[int, ...], high: int) -> tuple[int, int]:
    if left[-1] != right[0]:
        raise ValueError("block pair must overlap in its tower type")
    width = len(left) - 1
    if len(right) != width + 1:
        raise ValueError("block widths differ")
    r1, s1, n1, q1 = compose_block(base, left)
    r2, _, _, q2 = compose_block(base + 16 * width, right)
    assert (s1 - r2) % 64 == 0
    offset = (s1 - r2) // 64
    residue = (-offset * block_overlap_inverse(base, width)) % q2
    carry = (n1 * residue + offset) // q2
    assert carry >= 0
    entering = residue + q2 * high
    leaving = carry + n1 * high
    assert s1 + 64 * n1 * entering == r2 + 64 * q2 * leaving
    assert r1 + 64 * q1 * entering >= 0
    return entering, leaving


def main() -> None:
    assert pow(3, 53) > (1 << 84)
    thresholds = {width: minimum_certified_base(width) for width in (1, 2, 16, 256)}
    assert thresholds == {1: 3744, 2: 5600, 16: 31600, 256: 477424}
    for width, base in thresholds.items():
        odd, _, next_binary, margin = exponent_formulas(width, base)
        assert margin > 0
        assert 84 * odd > 53 * (next_binary + 1)
        if width <= 2:
            assert pow(3, odd) > 2 * (1 << next_binary)
        if base > 16:
            assert exponent_formulas(width, base - 16)[3] <= 0

    t = thresholds[1]
    for i, j in product(range(4), repeat=2):
        edge_cylinder(t, i, j)
    one_step_records = []
    for i, j, k in product(range(4), repeat=3):
        residue, carry, q = overlap_transition(t, i, j, k)
        for high in (1, 2, 17):
            entering, leaving = replay_overlap(t, i, j, k, high)
            assert leaving > entering
        one_step_records.append((i, j, k, residue & ((1 << 64) - 1), carry & ((1 << 64) - 1), q.bit_length()))

    base2 = thresholds[2]
    words2 = list(product(range(4), repeat=3))
    for word in words2:
        compose_block(base2, word)

    pair_count = 0
    for left in words2:
        for tail_a in range(4):
            tail_b = (left[0] + left[1] + left[2] + tail_a) % 4
            right = (left[-1], tail_a, tail_b)
            entering, leaving = replay_block_pair(base2, left, right, 1)
            assert leaving > entering
            pair_count += 1
    assert pair_count == 256

    payload = {
        "thresholds": thresholds,
        "one_step_triples": len(one_step_records),
        "width_two_words": len(words2),
        "width_two_pairs": pair_count,
        "first_triple_low64": one_step_records[0][3:5],
        "last_triple_low64": one_step_records[-1][3:5],
    }
    digest = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    print("linear-height quotient-refund checks passed")
    print(f"thresholds={thresholds}")
    print(f"one_step_triples={len(one_step_records)}")
    print(f"width_two_words={len(words2)} width_two_pairs={pair_count}")
    print(f"semantic_sha256={digest}")


if __name__ == "__main__":
    main()
