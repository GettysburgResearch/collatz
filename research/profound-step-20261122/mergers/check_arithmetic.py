#!/usr/bin/env python3
"""Exact finite regression for the arbitrary-debt theorem's ordinary inputs.

No finite count is used as evidence of global Collatz convergence. Explicit
exception checks are preserved under optimized Python.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path


def require(test: bool, message: str) -> None:
    if not test:
        raise ValueError(message)


def step(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def orbit(n: int, clocks: int) -> int:
    for _ in range(clocks):
        n = step(n)
    return n


def odd_gap(n: int) -> tuple[int, int]:
    require(n > 0 and n & 1 == 1, "odd source required")
    m, a = 3 * n + 1, 0
    while m & 1 == 0:
        m //= 2
        a += 1
    return a, m


def complement(b: int, clocks: int) -> tuple[int, int]:
    count = 0
    for _ in range(clocks):
        if b & 1:
            b = (3 * b - 1) // 2
            count += 1
        else:
            b //= 2
        require(b > 0, "complement positivity")
    return count, b


def ordinary_source(word: tuple[int, ...]) -> tuple[int, int]:
    """Solve the full parity cylinder, with an odd final endpoint."""
    carry, total = 0, 0
    for a in word:
        carry = 3 * carry + 2**total
        total += a
    modulus = 2 ** (total + 1)
    n = ((2**total - carry) * pow(3 ** len(word), -1, modulus)) % modulus
    require(n > 0 and n & 1 == 1, "positive ordinary source")
    current = n
    for a in word:
        got, current = odd_gap(current)
        require(got == a, "incorrect source valuation")
    return n, current


def run_checks() -> dict[str, object]:
    one_gap_count = 0
    for r in range(1, 2048, 2):
        a, u = odd_gap(r)
        for p in range(1, 9):
            for d in sorted({0, 1, 2, 3 ** (p - 1), 3**p * r // 2}):
                n = 3**p * r - d
                if n <= 0:
                    continue
                odd, new_debt = complement(3 ** (p - 1) + d, a)
                q = p - 1 + odd
                require(orbit(n, a) + new_debt == 3**q * u, "one-gap balance")
                one_gap_count += 1

    composed_steps, zero_exponent_captures = 0, 0
    for r in range(1, 1024, 2):
        a, u = odd_gap(r)
        x = orbit(9 * r + 2, a)
        p, d = a + 1, 1
        require(x + d == 3**p * u, "initial carry")
        for _ in range(24):
            if p == 0:
                require(0 < x <= 2 * u + 1, "zero-exponent interval")
                zero_exponent_captures += 1
                break
            a, next_source = odd_gap(u)
            odd, d = complement(3 ** (p - 1) + d, a)
            p = p - 1 + odd
            x = orbit(x, a)
            u = next_source
            require(x + d == 3**p * u, "composed carry balance")
            composed_steps += 1

    language_count, language_max_bits = 0, 0
    for length in range(9):
        for body in itertools.product((2, 3), repeat=length):
            word = (1,) + body + (2,)
            r, u = ordinary_source(word)
            target = orbit(9 * r + 2, sum(word))
            require(target == 3 * u - 1, "shorter-language transport")
            require(0 < target <= 4 * u + 1, "padded-source interval")
            language_count += 1
            language_max_bits = max(language_max_bits, r.bit_length())

    ghost_rows = []
    for k in range(1, 33):
        r_num = 2 ** (16 * k + 2) + 1
        u_num = 3 ** (5 * k) * 2 ** (k + 2) + 1
        z_num = 3 ** (9 * k + 2) * 2 ** (k + 2) + 19
        require(r_num % 5 == u_num % 5 == z_num % 5 == 0, "ghost integrality")
        r, u, z = r_num // 5, u_num // 5, z_num // 5
        current = r
        for j in range(5 * k):
            expected = (3**j * 2 ** (16 * k + 2 - 3 * j) + 1) // 5
            require(current == expected, "intermediate ordinary source")
            a, current = odd_gap(current)
            require(a == 3, "exact gap-three realization")
        require(current == u == orbit(r, 15 * k), "source endpoint")
        require(orbit(9 * r + 2, 15 * k) == z, "target endpoint")
        debt = (3 ** (4 * k + 2) - 19) // 5
        require(z + debt == 3 ** (4 * k + 2) * u, "ghost debt")
        require(z > 8 * u + 1, "unfunded endpoint capture")
        ghost_rows.append({"k": k, "source_bits": r.bit_length(),
                           "ternary_exponent": 4 * k + 2,
                           "ordinary_clocks": 15 * k})

    return {
        "status": "PASSED",
        "scope": "finite exact ordinary regressions; no universal convergence claim",
        "global_collatz_proved": False,
        "one_gap_instances": one_gap_count,
        "composed_actual_gap_steps": composed_steps,
        "zero_exponent_captures_in_bounded_sample": zero_exponent_captures,
        "shorter_language_words": language_count,
        "shorter_language_max_source_bits": language_max_bits,
        "ordinary_ghost_families": ghost_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run_checks()
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
