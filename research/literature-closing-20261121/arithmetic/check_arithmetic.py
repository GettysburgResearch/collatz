#!/usr/bin/env python3
"""Exact finite regression for the arithmetic identities in this packet.

This checks the implementation and examples.  It is not an exhaustive Collatz
test, a proof of convergence, or a substitute for the written/Lean proofs.
"""
from __future__ import annotations

from fractions import Fraction
import json
import math
from itertools import combinations


def step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def valuation(n: int, prime: int) -> int:
    if n == 0:
        raise ValueError("zero has no finite valuation")
    n = abs(n)
    result = 0
    while n % prime == 0:
        n //= prime
        result += 1
    return result


def local_norm(n: int, prime: int) -> Fraction:
    return Fraction(0) if n == 0 else Fraction(1, prime ** valuation(n, prime))


def marked(n: int) -> bool:
    if n <= 0 or n % 2 == 0:
        return False
    d = n.bit_length() - 1
    return (d + 1) * (n - 2**d) <= 70 * 2**d


def parity(n: int, length: int) -> tuple[int, ...]:
    result = []
    for _ in range(length):
        result.append(n % 2)
        n = step(n)
    return tuple(result)


def word_affine(word: tuple[int, ...]) -> tuple[int, int, int]:
    """Return q, s, C with F_word(x)=(3**s*x+C)/2**q."""
    C = s = 0
    for index, bit in enumerate(word):
        if bit:
            C = 3 * C + 2**index
            s += 1
    return len(word), s, C


def main() -> None:
    counts = {
        "actual_odd_prefixes": 0,
        "nontrivial_marked_prefixes": 0,
        "independent_return_batches": 0,
        "periodic_shadow_depths": 0,
        "exact_periodic_shadows": 0,
        "preperiodic_shadow_identities": 0,
        "binary_cylinder_sources": 0,
        "marked_parity_lifts": 0,
        "near_marked_returns_with_immediate_parity_disagreement": 0,
        "coupled_marked_triples_with_coprime_remainders": 0,
    }
    for n in range(1, 1024, 2):
        x = n
        A = B = 0
        batch: list[Fraction] = []
        for j in range(1, 33):
            a = valuation(3 * x + 1, 2)
            B = 3 * B + 2**A
            A += a
            x = (3 * x + 1) // 2**a
            d = x.bit_length() - 1
            u = x - 2**d
            X, Y, Z = 3**j, 2 ** (A + d), B
            assert 2**A * x == X * n + Z
            assert Z > 0 and Z % 3 != 0
            assert math.gcd(X, Y) == 1
            arch = X * Y * abs(n * X + Z - Y)
            at_two = local_norm(X, 2) * local_norm(Y, 2) * local_norm(n * X + Z, 2)
            at_three = local_norm(X, 3) * local_norm(Y, 3) * local_norm(Z, 3)
            product = arch * at_two * at_three
            assert product == u
            counts["actual_odd_prefixes"] += 1
            if marked(x) and x > 1:
                assert product >= 1
                counts["nontrivial_marked_prefixes"] += 1
                batch.append(product)
                if len(batch) == 3:
                    assert math.prod(batch) >= 1
                    batch.clear()
                    counts["independent_return_batches"] += 1

    for x in range(1, 512):
        for q in range(1, 10):
            word = parity(x, q)
            _, s, C = word_affine(word)
            D = 2**q - 3**s
            assert D != 0 and D % 2 != 0
            N = D * x - C
            endpoint = x
            for _ in range(q):
                endpoint = step(endpoint)
            assert N == 2**q * (x - endpoint)
            if N == 0:
                assert x == endpoint
                counts["exact_periodic_shadows"] += 1
            else:
                depth = valuation(N, 2)
                assert depth >= q and 2**depth <= abs(N)
                actual = parity(x, depth + 1)
                assert all(actual[i] == word[i % q] for i in range(depth))
                assert actual[depth] != word[depth % q]
                counts["periodic_shadow_depths"] += 1

            for p in range(4):
                initial = x
                prefix = parity(initial, p)
                _, a, C_U = word_affine(prefix)
                tail = initial
                for _ in range(p):
                    tail = step(tail)
                period = parity(tail, q)
                _, b, C_V = word_affine(period)
                denominator = 2**q - 3**b
                numerator = 3**a * denominator * initial + denominator * C_U - 2**p * C_V
                assert numerator == 2**p * (denominator * tail - C_V)
                counts["preperiodic_shadow_identities"] += 1

    for length in range(1, 11):
        codes = {parity(n, length) for n in range(2**length)}
        assert len(codes) == 2**length
        counts["binary_cylinder_sources"] += 2**length
        d = max(16, 2 * length + 8)
        for residue in range(1, 2**length, 2):
            source = 2**d + residue
            assert marked(source)
            assert parity(source, length) == parity(residue, length)
            counts["marked_parity_lifts"] += 1

    near_return_examples = []
    triple_examples = []
    for q in (12, 53, 665):
        power_three = 3**q
        A = power_three.bit_length() - 1
        assert q <= A < 2 * q
        assert 0 < q * (power_three - 2**A) <= 4 * 2**A
        number_of_twos = A - q
        if q == 12:
            choices = list(combinations(range(1, q), number_of_twos))
        else:
            choices = [tuple(1 + (i + offset) % (q - 1) for i in range(number_of_twos))
                       for offset in range(10)]
        seen = set()
        for positions in choices:
            positions = set(positions)
            valuations = [2 if i in positions else 1 for i in range(q)]
            assert valuations[0] == 1 and sum(valuations) == A
            C = exponent = 0
            for a in valuations:
                C = 3 * C + 2**exponent
                exponent += a
            modulus = 2 ** (A + 2)
            residue = ((2**A - C) * pow(power_three, -1, modulus)) % modulus
            d = A + q + 8
            x = 2**d + residue
            y = (power_three * x + C) // 2**A
            assert x % 4 == 3 and y % 4 == 1
            assert x > 0 and x < y
            assert x.bit_length() == y.bit_length() == d + 1
            assert marked(x) and marked(y)
            assert q * (y - 2**d) < 5 * 2**d
            assert q * (y - x) < 5 * x
            actual = x
            for a in valuations:
                assert valuation(3 * actual + 1, 2) == a
                actual = (3 * actual + 1) // 2**a
            assert actual == y
            assert parity(x, 2) == (1, 1) and parity(y, 2) == (1, 0)
            assert x not in seen
            seen.add(x)
            counts["near_marked_returns_with_immediate_parity_disagreement"] += 1
        near_return_examples.append({
            "q": q, "A": A, "d": d, "distinct_valuation_words_checked": len(choices),
            "first_source_decimal_if_short": str(min(seen)) if d < 128 else None,
            "source_bits": d + 1,
            "parity_at_source": [1, 1], "parity_at_return": [1, 0],
        })

        assert 0 < q * (power_three - 2**A) <= 2 * 2**A
        prefix_twos = A - q - 1
        if q == 12:
            prefix_choices = list(combinations(range(q - 2), prefix_twos))
        else:
            prefix_choices = [tuple((i + offset) % (q - 2) for i in range(prefix_twos))
                              for offset in range(10)]
        for positions in prefix_choices:
            positions = set(positions)
            prefix = [2 if i in positions else 1 for i in range(q - 2)]
            assert sum(prefix) == A - 3
            first, second = prefix + [1, 2], prefix + [2, 1]
            carries = []
            for block in (first, second):
                c = exponent = 0
                for a in block:
                    c = 3 * c + 2**exponent
                    exponent += a
                assert exponent == A
                carries.append(c)
            c1, c2 = carries
            assert c2 - c1 == 2 ** (A - 2)
            total_carry = power_three * c1 + 2**A * c2
            residue = ((2 ** (2 * A) - total_carry) *
                       pow(power_three**2, -1, 2 ** (2 * A + 2))) % 2 ** (2 * A + 2)
            d = 2 * A + 2 * q + 8
            states = [2**d + residue]
            actual = states[0]
            for block in (first, second):
                for a in block:
                    assert valuation(3 * actual + 1, 2) == a
                    actual = (3 * actual + 1) // 2**a
                states.append(actual)
            assert states[0] < states[1] < states[2]
            assert states[2] % 4 == 1
            assert all(marked(x) and x.bit_length() == d + 1 for x in states)
            offsets = [x - 2**d for x in states]
            assert all(0 < q * u < 5 * 2**d for u in offsets)
            R01 = 2**A * offsets[1] - power_three * offsets[0]
            R12 = 2**A * offsets[2] - power_three * offsets[1]
            R02 = 2 ** (2 * A) * offsets[2] - power_three**2 * offsets[0]
            assert R01 == c1 + (power_three - 2**A) * 2**d
            assert R12 == c2 + (power_three - 2**A) * 2**d
            assert R01 % 2 == R12 % 2 == 1
            assert R12 - R01 == 2 ** (A - 2)
            assert math.gcd(R01, R12) == math.gcd(R01, R02) == 1
            assert R02 == 2**A * R12 + power_three * R01
            assert valuation(states[1] - states[0], 2) == A - 2
            counts["coupled_marked_triples_with_coprime_remainders"] += 1
        triple_examples.append({
            "q": q, "A": A, "d": 2 * A + 2 * q + 8,
            "distinct_prefix_words_checked": len(prefix_choices),
            "source_bits": 2 * A + 2 * q + 9,
            "adjacent_remainder_gcd": 1,
            "first_pair_parity_agreement_depth": A - 2,
        })

    print(json.dumps({
        "status": "PASS",
        "arithmetic": "exact Python integers and fractions",
        "scope": "finite identity, local-factor, shadow-depth and parity-lift regressions only",
        "counts": counts,
        "near_return_examples": near_return_examples,
        "coupled_triple_examples": triple_examples,
        "universal_convergence_claim": False,
    }, indent=2))


if __name__ == "__main__":
    main()
