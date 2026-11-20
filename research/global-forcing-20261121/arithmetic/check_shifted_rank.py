#!/usr/bin/env python3
"""Exact finite controls for SHIFTED_RANK_COMPACTNESS.md; not a Collatz proof."""

from __future__ import annotations

import argparse
from fractions import Fraction
import itertools
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def odd_step(n: int) -> tuple[int, int]:
    require(isinstance(n, int) and not isinstance(n, bool) and n > 0 and n % 2 == 1,
            "source must be a positive odd integer")
    value = 3 * n + 1
    a = (value & -value).bit_length() - 1
    return value >> a, a


def check_edge(n: int, successor: int, a: int, ci: Fraction = Fraction(1),
               cj: Fraction = Fraction(1)) -> None:
    actual, exponent = odd_step(n)
    require(a == exponent and successor == actual, "not the actual odd edge")
    require(a >= 2, "exponent-one edge is degenerate")
    require(ci > 0 and cj > 0, "positive coset representatives required")
    b = a - 1
    m, mp = n + 1, successor + 1
    u, v = Fraction(m, 1) / ci, Fraction(mp, 1) / cj
    tuple_value = (Fraction(2**b), u, 2**b * v)
    terms = (tuple_value[0], Fraction(3, 2) * ci * tuple_value[1],
             -cj * tuple_value[2])
    require(sum(terms) == 1, "shifted unit equation")
    for mask in range(1, 8):
        require(sum(terms[j] for j in range(3) if mask & (1 << j)) != 0,
                "vanishing subsum")
    require(terms[0] + terms[1] > 0, "first pair sign")
    require(terms[0] + terms[2] == 2**b * (1 - mp) < 0, "second pair sign")
    require(terms[1] + terms[2] == 1 - 2**b < 0, "third pair sign")
    require(ci * tuple_value[1] - 1 == n, "source reconstruction")


def block(n: int) -> tuple[list[int], list[int]]:
    odd_step(n)
    m = n + 1
    sigma = (m & -m).bit_length() - 1
    states, exponents = [n], []
    for j in range(sigma):
        nxt, a = odd_step(states[-1])
        require((a == 1) if j < sigma - 1 else (a >= 2), "exact block clock")
        states.append(nxt)
        exponents.append(a)
        if j < sigma - 1:
            require((nxt + 1) * 2 ** (j + 1) == m * 3 ** (j + 1),
                    "shifted run formula")
        require(nxt + 1 < m * m, "integer quadratic block envelope")
    require(states[-1] <= states[-2], "last defect decreases")
    return states, exponents


def factors(value: int) -> dict[int, int]:
    require(value >= 1, "factor domain")
    result: dict[int, int] = {}
    p = 2
    while p * p <= value:
        while value % p == 0:
            value //= p
            result[p] = result.get(p, 0) + 1
        p = 3 if p == 2 else p + 2
    if value > 1:
        result[value] = result.get(value, 0) + 1
    return result


def valuation_vector(value: Fraction) -> dict[int, int]:
    require(value > 0, "positive rational required")
    result = factors(value.numerator)
    for p, exponent in factors(value.denominator).items():
        result[p] = result.get(p, 0) - exponent
    return {p: a for p, a in result.items() if a}


def matrix_rank(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    matrix = [list(map(Fraction, row)) for row in rows]
    width, pivot = len(matrix[0]), 0
    require(all(len(row) == width for row in matrix), "rectangular matrix")
    for col in range(width):
        selected = next((j for j in range(pivot, len(matrix)) if matrix[j][col]), None)
        if selected is None:
            continue
        matrix[pivot], matrix[selected] = matrix[selected], matrix[pivot]
        divisor = matrix[pivot][col]
        matrix[pivot] = [x / divisor for x in matrix[pivot]]
        for j in range(len(matrix)):
            if j != pivot and matrix[j][col]:
                scale = matrix[j][col]
                matrix[j] = [x - scale * y for x, y in zip(matrix[j], matrix[pivot])]
        pivot += 1
        if pivot == len(matrix):
            break
    return pivot


def multiplicative_rank(values: list[Fraction]) -> int:
    columns = [valuation_vector(Fraction(value)) for value in values]
    primes = sorted({p for column in columns for p in column})
    return matrix_rank([[Fraction(column.get(p, 0)) for column in columns] for p in primes])


def cover_rank(values: list[Fraction], k: int) -> int:
    require(k >= 1 and values, "nonempty finite cover")
    best = len(values)
    for labels in itertools.product(range(k), repeat=len(values)):
        representatives: dict[int, Fraction] = {}
        ratios = []
        for value, label in zip(values, labels):
            representatives.setdefault(label, value)
            ratios.append(value / representatives[label])
        best = min(best, multiplicative_rank(ratios))
    return best


def inverse_tower(length: int) -> tuple[list[int], list[int]]:
    require(length >= 0, "tower length")
    states, exponents = [1], []
    for _ in range(length):
        q = states[-1]
        choices = (2, 4, 6) if q % 3 == 1 else (3, 5, 7)
        divisibility_flags = []
        candidates = []
        for a in choices:
            require((2**a * q - 1) % 3 == 0, "integral inverse choices")
            x = (2**a * q - 1) // 3
            divisibility_flags.append(x % 3 == 0)
            if x > q and x % 3:
                candidates.append((a, x))
        require(sum(divisibility_flags) == 1, "exactly one ternary obstruction")
        require(candidates, "inverse tower has an admissible extension")
        a, x = candidates[0]
        require(odd_step(x) == (q, a), "inverse ordinary replay")
        states.append(x)
        exponents.append(a)
    return states, exponents


def run() -> dict:
    edge_checks = 0
    for n in list(range(1, 4096, 2)) + [(2 ** (2*j) - 1) // 3 for j in range(1, 81)]:
        successor, a = odd_step(n)
        if a >= 2:
            for ci, cj in ((Fraction(1), Fraction(1)), (Fraction(6, 35), Fraction(22, 13))):
                check_edge(n, successor, a, ci, cj)
                edge_checks += 1

    block_checks, block_edges = 0, 0
    for n in list(range(1, 1024, 2)) + [2**h * q - 1 for h in range(2, 81) for q in (1, 5, 7, 11)]:
        states, exponents = block(n)
        block_checks += 1
        block_edges += len(exponents)
        check_edge(states[-2], states[-1], exponents[-1])

    clock_checks = 0
    for start in range(1, 256, 2):
        n, seen, d = start, {start}, 0
        ell = (start + 1 - 1).bit_length()
        for N in range(1, 97):
            n, a = odd_step(n)
            d += a >= 2
            if n in seen:
                break
            seen.add(n)
            require(N < ell * (2**(d + 1) - 1), "integer fixed-source deadline")
            clock_checks += 1

    for generators in ((2,), (6,), (6, 35), (Fraction(6, 35), 10), (2, 3, 5)):
        r = multiplicative_rank(list(map(Fraction, generators)))
        tuple_generators = [(Fraction(2), Fraction(1), Fraction(2))]
        tuple_generators += [(Fraction(1), Fraction(g), Fraction(1)) for g in generators]
        tuple_generators += [(Fraction(1), Fraction(1), Fraction(g)) for g in generators]
        coords = [[valuation_vector(value) for value in triple] for triple in tuple_generators]
        primes = sorted({p for triple in coords for coordinate in triple for p in coordinate})
        rows = [[Fraction(triple[coordinate].get(p, 0)) for triple in coords]
                for coordinate in range(3) for p in primes]
        require(matrix_rank(rows) == 2*r + 1, "three-coordinate group rank")

    samples = [
        ([6, 24, 96], 1, 1, 2),
        ([6, 24, 10, 40], 2, 1, 3),
        ([2, 3, 5], 3, 0, 3),
        ([2, 3, 5], 1, 2, 3),
    ]
    for values, k, expected_cover, expected_absolute in samples:
        rationals = list(map(Fraction, values))
        require(cover_rank(rationals, k) == expected_cover, "finite coset-cover decision")
        require(multiplicative_rank(rationals) == expected_absolute, "absolute rank distinction")

    states, exponents = inverse_tower(128)
    n = states[-1]
    for a in reversed(exponents):
        require(n > 1, "tower first-hit certificate")
        n, actual = odd_step(n)
        require(actual == a >= 2, "tower exact defect certificate")
    require(n == 1, "tower endpoint")
    tower_ranks = [multiplicative_rank([Fraction(n + 1) for n in states[:j + 1]])
                   for j in range(12)]
    require(tower_ranks[0] == 1 and tower_ranks[-1] > 1, "finite rank variation control")

    require(400 * 2**14 + 1 < 2**23, "cycle minimum constant")
    for d in range(1, 129):
        require(d <= 2**(d - 1), "integer log d comparison")
        require(241*d - 105 > 23 + 15*d, "cycle ceiling separation")
        require(256*d*2**d < 256*(d + 1)*2**(d + 1), "cycle ceiling monotonicity")

    negative = [
        lambda: odd_step(0), lambda: odd_step(-1), lambda: odd_step(2),
        lambda: check_edge(3, 5, 1), lambda: check_edge(5, 1, 3),
        lambda: check_edge(5, 3, 4), lambda: check_edge(5, 1, 4, Fraction(0)),
        lambda: multiplicative_rank([Fraction(0)]), lambda: inverse_tower(-1),
    ]
    rejected = 0
    for action in negative:
        try:
            action()
        except ValueError:
            rejected += 1
        else:
            raise ValueError("malformed or out-of-domain control was accepted")

    for h in range(2, 81):
        n = 2**h - 1
        successor, a = odd_step(n)
        require(a == 1 and successor + 1 == 3 * 2**(h - 1), "degenerate family")

    return {
        "schema": "collatz-shifted-rank-finite-controls/v1",
        "status": "PASS",
        "scope": "Exact finite algebra, domain, rank and certificate controls; no all-cycle census or Collatz proof",
        "external_inputs_not_proved_by_execution": [
            "Evertse-Schlickewei-Schmidt Theorem 1.1",
            "Lagarias Lemma 2.2(1) logarithmic-form estimate",
        ],
        "edge_and_coset_reconstructions": edge_checks,
        "run_defect_blocks": block_checks,
        "actual_block_edges": block_edges,
        "simple_prefix_clock_checks": clock_checks,
        "group_rank_reconstructions": 5,
        "finite_coset_cover_cases": len(samples),
        "cycle_integer_constant_controls": 385,
        "degenerate_family_instances": 79,
        "negative_controls_rejected": rejected,
        "inverse_tower": {
            "odd_depth": len(exponents), "all_edges_defects": True,
            "largest_source_bits": states[-1].bit_length(),
            "first_twelve_values": states[:12],
            "first_twelve_shifted_absolute_ranks": tower_ranks,
        },
        "symbolic_constants": {
            "ess_coefficient": 18**9,
            "B_r_binary_exponent_coefficient": 4*18**9,
            "cycle_height_log_bound": "256*d*2**d",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="compare the complete deterministic report")
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.check is not None:
        require(args.check.read_text(encoding="utf-8") == rendered, "frozen report differs")
    print(rendered, end="")


if __name__ == "__main__":
    main()
