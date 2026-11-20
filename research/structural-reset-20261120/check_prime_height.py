#!/usr/bin/env python3
"""Small exact checks for the elementary prime-height proof.

This is a regression of finite identities and inequalities, not a proof of
their universal statements and not a convergence search. No floating-point
logarithms, external packages, or optimization-sensitive assertions are used.
"""

from __future__ import annotations

import json
from math import gcd, lcm, prod


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(label)


def odd_step(n: int) -> tuple[int, int]:
    require(n > 0 and n % 2 == 1, "positive odd input")
    value = 3 * n + 1
    exponent = (value & -value).bit_length() - 1
    return value >> exponent, exponent


def prefix(n: int, transitions: int) -> tuple[list[int], list[int]]:
    states, exponents = [n], []
    for _ in range(transitions):
        n, exponent = odd_step(n)
        states.append(n)
        exponents.append(exponent)
    return states, exponents


def p_part(n: int, p: int) -> int:
    value = 1
    while n % p == 0:
        n //= p
        value *= p
    return value


def s_part(n: int, primes: tuple[int, ...]) -> int:
    return prod(p_part(n, p) for p in primes)


def main() -> None:
    seeds = sorted(set(
        [1, 3, 5, 7, 9, 27, 31, 41, 97, 121, 255, 3**20]
        + [(1 << k) - 1 for k in (8, 32, 128, 512)]
        + [((1 << k) - 1) // 3 for k in (6, 20, 128, 512, 2048)]
    ))
    pool = (3, 5, 7, 11, 13, 17, 19, 31, 127)
    counts = {"affine_pairs": 0, "local_budgets": 0,
              "finite_history_budgets": 0, "predecessor_controls": 0}
    largest_exponent = 0
    for seed in seeds:
        states, exponents = prefix(seed, 32)
        largest_exponent = max(largest_exponent, *exponents)
        for i in range(32):
            total, correction = 0, 0
            for j in range(i + 1, min(33, i + 9)):
                correction = 3 * correction + (1 << total)
                total += exponents[j - 1]
                gap = j - i
                left, right = states[i], states[j]
                common = gcd(left, right)
                require((1 << total) * right == 3**gap * left + correction,
                        "exact affine relation")
                require(correction > 0 and correction % common == 0,
                        "gcd divides the positive correction")
                require(correction * (1 << gap)
                        <= (1 << total) * (3**gap - (1 << gap)),
                        "unrestricted correction bound")
                require((1 << total) * right <= 4**gap * left,
                        "logarithmic division balance")
                require(common * right < 6**gap * left,
                        "stronger exact pair bound")
                require(common * right < 8**gap * left,
                        "ADEL-001 after exponentiating")
                counts["affine_pairs"] += 1

        for length in (1, 2, 7, 16, 31, 32):
            visited = states[:length]
            height_product = prod(visited)
            # These are the heaviest primes within this explicitly finite
            # candidate pool, chosen anew after inspecting each whole prefix.
            ordered = sorted(pool,
                             key=lambda p: prod(p_part(n, p) for n in visited),
                             reverse=True)
            for size in (1, 2, 3):
                selected = tuple(ordered[:size])
                selected_product = prod(s_part(n, selected) for n in visited)
                for width in (2, 3, 5, 8):
                    whole = length // width * width
                    tail_product = prod(visited[whole:])
                    # r*Y <= s*W + s*r^2*x0 + 5*s*r^2*N + r*tail.
                    rhs = (height_product**size
                           * seed**(size * width**2)
                           * (1 << (5 * size * width**2 * length))
                           * tail_product**width)
                    require(selected_product**width <= rhs,
                            "ADEL-003 exact finite-history inequality")
                    counts["finite_history_budgets"] += 1
                    for start in range(0, whole, width):
                        block = visited[start:start + width]
                        block_parts = prod(s_part(n, selected) for n in block)
                        # Clear the block-range logarithm using min and max.
                        lhs = block_parts**width * min(block)**(size * width**2)
                        rhs = (prod(block)**size
                               * max(block)**(size * width**2)
                               * (1 << (3 * size * width**3)))
                        require(lhs <= rhs, "ADEL-002 exact local inequality")
                        counts["local_budgets"] += 1

    for selected in ((2, 3, 5, 7, 13), (2, 3, 5, 7, 11, 13),
                     (5, 17, 257)):
        # Fermat's p-1 suffices in place of the exact multiplicative order.
        period = lcm(6, *(p - 1 for p in selected if p not in (2, 3)))
        for k in (0, 1, 2):
            exponent = 2 + period * k
            n = ((1 << exponent) - 1) // 3
            endpoint, actual_exponent = odd_step(n)
            require(endpoint == 1 and actual_exponent == exponent,
                    "one-step ordinary predecessor control")
            require(s_part(n, selected) == 1,
                    "no height on the prescribed finite prime set")
            counts["predecessor_controls"] += 1

    print(json.dumps({
        "status": "PASS", "seed_count": len(seeds),
        "transitions_per_seed": 32, "pair_gap_at_most": 8,
        "largest_actual_division_exponent": largest_exponent,
        "adaptive_prime_pool": list(pool), "counts": counts,
        "scope": "finite exact arithmetic regressions; universal proofs are written separately",
        "not_claimed": ["Collatz proof", "all prime sets tested", "formal verification",
                        "any escaping orbit observed", "any nontrivial positive cycle excluded"]
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
