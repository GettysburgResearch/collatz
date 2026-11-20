#!/usr/bin/env python3
"""Exact finite checks for simultaneous rational-cycle density.

No floating-point logarithm, source import, factorization, or Collatz
conjecture enters these checks. Arbitrary-input termination is proved in
RATIONAL_CYCLES.md.
"""
from __future__ import annotations

import json
from math import gcd


def odd_step(n: int) -> tuple[int, int]:
    value = 3 * n + 1
    a = (value & -value).bit_length() - 1
    return value >> a, a


def reserved_words(n: int, j: int, q: int) -> tuple[list[int], list[int]]:
    backward = []
    value = n
    for _ in range(q):
        for a in range(1, 5):
            numerator = (value << a) - 1
            if numerator % 3 == 0 and (numerator // 3) % 3:
                value = numerator // 3
                backward.append(a)
                break
        else:
            raise AssertionError("missing legal cap-four inverse action")
    forward = []
    value = n
    total = 0
    while total + 1 < j:
        value, a = odd_step(value)
        forward.append(a)
        total += a
    return backward, forward


def numerator(word: list[int]) -> tuple[int, int]:
    # 3^i * terminal = 2^A * root - C after i inverse edges.
    value = 0
    total = 0
    power3 = 1
    for a in word:
        value = (value << a) + power3
        total += a
        power3 *= 3
    return value, total


def construct(n: int, j: int, q: int, floor: int) -> dict:
    assert n > 0 and n % 2 and n % 3 and j >= 0 and q >= 0 and floor > 0
    back, front = reserved_words(n, j, q)
    size = len(back) + len(front)
    fixed_total = sum(back) + sum(front)
    max_gap = max([2, *back, *front])
    d = size + 2
    power3 = 3**d
    while True:
        total = power3.bit_length()  # 2^(total-1) < 3^d < 2^total.
        power2 = 1 << total
        denominator = power2 - power3
        middle_size = d - size
        twos = total - fixed_total - middle_size
        ones = middle_size - twos
        if (ones >= 1 and twos >= 1 and 5 * total < 8 * d
                and denominator > 1
                and power2 > floor * (1 << max_gap) * denominator):
            break
        d += 1
        power3 *= 3
        if d > 100000:
            raise RuntimeError("finite replay guard exceeded")
    filler = [1, 2] + [1] * (ones - 1) + [2] * (twos - 1)
    word0 = back + filler + list(reversed(front))
    word1 = back + [2, 1] + filler[2:] + list(reversed(front))
    num0, a0 = numerator(word0)
    num1, a1 = numerator(word1)
    assert a0 == a1 == total and len(word0) == len(word1) == d
    difference = num0 - num1
    assert difference == 3**len(back) * 2**(total - sum(back) - 2)
    assert gcd(difference, denominator) == 1
    word, root, swapped = ((word0, num0, False) if num0 % denominator
                           else (word1, num1, True))
    common_gcd = gcd(root, denominator)
    reduced_denominator = denominator // common_gcd
    assert reduced_denominator > 1 and gcd(reduced_denominator, 6) == 1
    assert (root - n * denominator) % (2**j * 3**q) == 0

    current = root
    minimum = root
    for a in word:
        assert current > floor * denominator
        assert current % 2 and current % 3
        assert gcd(current, denominator) == common_gcd
        new_numerator = (current << a) - denominator
        assert new_numerator % 3 == 0
        parent = new_numerator // 3
        # Exact forward gap, not just formal integrality.
        forward_numerator = 3 * parent + denominator
        valuation = (forward_numerator & -forward_numerator).bit_length() - 1
        assert valuation == a
        current = parent
        minimum = min(minimum, current)
    assert current == root

    current = root
    for expected_gap in front:
        value = 3 * current + denominator
        actual_gap = (value & -value).bit_length() - 1
        assert actual_gap == expected_gap
        current = value >> actual_gap
    assert 8 * d - 5 * total > 0
    return {
        "n": n, "binary_digits": j, "ternary_digits": q, "floor": floor,
        "odd_cycle_word_length": d, "total_gap": total,
        "positive_score_per_lap": 8 * d - 5 * total,
        "max_gap": max(word), "swapped_for_nonintegrality": swapped,
        "minimum_exceeds_floor": minimum > floor * denominator,
        "reduced_denominator_bits": reduced_denominator.bit_length(),
        "simultaneous_modulus": 2**j * 3**q,
    }


def immediate_converger(q: int) -> dict:
    forward_gap = 3**(q + 1) + 1
    root = ((1 << forward_gap) - 1) // 3
    assert root % 2 and root % 3
    assert (root + 1) % 3**(q + 1) == 0
    value = root
    for _ in range(q):
        value, rem = divmod(2 * value - 1, 3)
        assert rem == 0 and value > 0 and value % 3
    endpoint, gap = odd_step(root)
    assert endpoint == 1 and gap == forward_gap
    return {"inverse_ones": q, "ordinary_forward_odd_steps": 1,
            "root_bits": root.bit_length(), "score_lower_bound": 3 * q}


def main() -> None:
    fixtures = [
        (1, 0, 0, 1), (1, 8, 8, 25), (5, 7, 5, 20),
        (7, 9, 7, 10), (13, 8, 6, 20), (25, 10, 8, 20),
        (31, 8, 9, 25), (41, 9, 5, 10), (55, 7, 7, 5),
    ]
    rows = [construct(*fixture) for fixture in fixtures]
    control = [immediate_converger(q) for q in range(1, 8)]
    print(json.dumps({
        "status": "PASS", "rational_cycles": rows,
        "inverse_edges_checked": sum(r["odd_cycle_word_length"] for r in rows),
        "immediate_converger_controls": control,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
