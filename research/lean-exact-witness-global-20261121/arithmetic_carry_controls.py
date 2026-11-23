#!/usr/bin/env python3
"""Exact controls for the M-matrix closing attempt, not a cycle census.

The general carry equivalence and invariant box have written proofs in
HIGH_VARIANCE_ARITHMETIC.md. These calculations check the two displayed
controls and the exact integer margin used by the escape note.
"""
from fractions import Fraction
from itertools import product
from math import prod
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def apply_b(diagonal, vector):
    return [d * vector[i] - 3 * vector[i - 1]
            for i, d in enumerate(diagonal)]


def carry(diagonal):
    require(all(d >= 2 and d % 2 == 0 for d in diagonal),
            "carry requires positive even divisors")
    current = (1,) * len(diagonal)
    history = []
    seen = {}
    while current not in seen and any(current):
        seen[current] = len(history)
        history.append(list(current))
        bits = [c % 2 for c in current]
        numerators = [c + 3 * bits[i] - d * bits[(i + 1) % len(bits)]
                      for i, (c, d) in enumerate(zip(current, diagonal))]
        require(all(n % 2 == 0 for n in numerators), "nonintegral carry")
        current = tuple(n // 2 for n in numerators)
        require(all(1 - d <= c <= 2 for c, d in zip(current, diagonal)),
                "carry left the invariant box")
    history.append(list(current))
    return {"states": history, "reached_zero": not any(current),
            "steps": len(history) - 1, "repeat_at": seen.get(current)}


def main():
    dyadic = [2, 2, 8]
    firing = [5, 8, 3]
    image = apply_b(dyadic, firing)
    reduced = [1 - v for v in image]
    require(image == [1, 1, 0] and reduced == [0, 0, 1],
            "dyadic multi-firing control failed")
    inverse_reduced = [Fraction(6, 5), Fraction(9, 5), Fraction(4, 5)]
    require(apply_b(dyadic, inverse_reduced) == reduced,
            "displayed inverse image failed")
    nonempty_subsets = [v for v in product([0, 1], repeat=3) if any(v)]
    require(all(any(x > 1 for x in apply_b(dyadic, v))
                for v in nonempty_subsets), "chi-superstability control failed")
    rational = [Fraction(n, 5) for n in [19, 31, 49]]
    require(all(dyadic[i] * rational[(i + 1) % 3] == 3 * rational[i] + 1
                for i in range(3)), "rational cycle identities failed")
    dyadic_carry = carry(dyadic)
    require(not dyadic_carry["reached_zero"], "nonintegral control reached zero")

    states = [31, 47, 71, 107, 161, 121, 91, 137, 103]
    divisors = [2, 2, 2, 2, 4, 4, 2, 4, 10]
    require(all(divisors[i] * states[(i + 1) % len(states)] == 3 * states[i] + 1
                for i in range(len(states))), "even-divisor edge failed")
    determinant = prod(divisors) - 3 ** len(states)
    require(determinant == 797, "wrong full determinant")
    even_carry = carry(divisors)
    require(even_carry["reached_zero"] and even_carry["steps"] == 8,
            "even-divisor carry termination failed")
    require(8 * 3125 ** 24 < 3456 ** 24, "orbit-count numerical margin failed")
    print(json.dumps({
        "schema": "collatz-high-variance-arithmetic-controls/v1",
        "scope": "Two exact controls; no all-word or Collatz-cycle exclusion",
        "dyadic": {"gaps": [1, 1, 3], "determinant": 5,
                    "firing": firing, "image": image, "reduced": reduced,
                    "chi_subsets_checked": len(nonempty_subsets),
                    "inverse_reduced": [str(x) for x in inverse_reduced],
                    "rational_cycle": [str(x) for x in rational],
                    "carry": dyadic_carry},
        "even_divisor": {"states": states, "divisors": divisors,
                         "determinant": determinant, "carry": even_carry,
                         "is_collatz_cycle": False,
                         "failed_collatz_divisor": 10,
                         "actual_U_103": 155},
        "orbit_count_exact_integer_margin": True
    }, indent=2))


if __name__ == "__main__":
    main()
