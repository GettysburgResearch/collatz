"""Independent finite controls for the neighboring arbitrary-packet theorem.

These controls reconstruct the binary word, carry, ordinary realization and
full gcd from their definitions. They are evidence for the review, not an
enumeration proof of the all-parameter written theorem.
"""

import hashlib
import json
import math
from functools import reduce
from pathlib import Path


def valuation(n, prime):
    exponent = 0
    while n % prime == 0:
        n //= prime
        exponent += 1
    return exponent


def least_word_period(word):
    failure = [0] * len(word)
    for i in range(1, len(word)):
        j = failure[i - 1]
        while j and word[i] != word[j]:
            j = failure[j - 1]
        if word[i] == word[j]:
            j += 1
        failure[i] = j
    candidate = len(word) - failure[-1]
    return candidate if len(word) % candidate == 0 else len(word)


def check(a, b, r, periods, offsets, polynomial):
    assert b >= 1 and a - b >= 2 and len(periods) >= 2
    assert r >= len(periods) and len(set(offsets)) == len(periods)
    assert all(0 <= s < r for s in offsets)
    assert all(n >= 2 for n in periods)
    assert all(math.gcd(n, m) == 1 for i, n in enumerate(periods)
               for m in periods[i + 1:])
    X, Y, V = 2**a, 3**b, 2**b
    assert X > Y
    L = r * math.prod(periods)
    A, p = a * L, b * L
    S = sum(n - 1 for n in periods)
    profile = [sum(j % (r * n) == s for n, s in zip(periods, offsets))
               for j in range(L)]
    assert set(profile) <= {0, 1}
    positions = [a * j + t + profile[j] for j in range(L) for t in range(b)]
    word = [0] * A
    for position in positions:
        assert 0 <= position < A and word[position] == 0
        word[position] = 1
    assert least_word_period(word) == A

    # Direct full carry, before any cyclotomic or numerical cancellation.
    C = sum(2**d * 3**(p - 1 - h) for h, d in enumerate(positions))
    D = 2**A - 3**p
    K = X**r - Y**r
    R_parts = [(X**(r * n) - Y**(r * n)) // K for n in periods]
    R = math.prod(R_parts)
    B = (K // (X - Y)) * R + sum(
        X**s * Y**(r * n - 1 - s) * (R // Ri)
        for n, s, Ri in zip(periods, offsets, R_parts)
    )
    Dpol, Qpol = K * R, (Y - V) * B
    assert D % Dpol == 0 and C == (D // Dpol) * Qpol
    assert all(math.gcd(Ri, Rj) == 1 for i, Ri in enumerate(R_parts)
               for Rj in R_parts[i + 1:])
    assert math.gcd(B, R) == 1
    g = math.gcd(Dpol, Qpol)
    assert K * (Y - V) % g == 0
    q = D // math.gcd(C, D)
    assert q == Dpol // g
    assert q % (R // math.gcd(R, Y - V)) == 0
    assert q * Y > X**(r * S) and q * q > Dpol
    assert q**(r * S) > Dpol**(r * S - r - 1)

    # An unreduced odd common denominator preserves exact rational parity.
    numerator = C
    minimum = C
    boundaries = []
    for clock, bit in enumerate(word):
        if clock % a == 0:
            boundaries.append(numerator)
        assert numerator > 0 and numerator % 2 == bit
        numerator = (3 * numerator + D) // 2 if bit else numerator // 2
        minimum = min(minimum, numerator)
    assert numerator == C
    assert 2 * minimum * (X - Y) >= D * (Y - V)
    for j in range(L):
        assert X * boundaries[(j + 1) % L] == (
            Y * boundaries[j] + (1 + profile[j]) * (Y - V) * D
        )

    modulus = 2**A
    ordinary = (C * pow(D, -1, modulus)) % modulus
    if ordinary * D <= C:
        ordinary += ((C - ordinary * D) // (modulus * D) + 1) * modulus
    ordinary_start = ordinary
    for bit in word:
        assert ordinary % 2 == bit
        ordinary = (3 * ordinary + 1) // 2 if bit else ordinary // 2
    assert ordinary < ordinary_start

    polynomial_degree = None
    if polynomial:
        import sympy as sp
        z = sp.Symbol("z")
        F = sp.Poly.from_dict({p: 1, 0: -(2**A)}, z, domain=sp.QQ)
        Q = sp.Poly.from_dict({p - 1 - h: 2**d
                              for h, d in enumerate(positions)}, z, domain=sp.QQ)
        G = sp.gcd(F, Q).monic()
        F0, Q0 = F.exquo(G), Q.exquo(G)
        assert F0.degree() == b * r * (1 + S)
        assert F0.eval(3) == -Dpol and Q0.eval(3) == Qpol
        polynomial_degree = G.degree()

    return {
        "parameters": {"a": a, "b": b, "r": r,
                       "periods": periods, "offsets": offsets},
        "word_length": A,
        "odd_count": p,
        "full_binary_primitive_period": A,
        "rational_orbit_and_ordinary_realizer": "PASS",
        "complete_numerical_gcd": str(g),
        "reduced_denominator_bits": q.bit_length(),
        "polynomial_gcd_degree": polynomial_degree,
        "shared_five_prime_power": {
            "K": valuation(K, 5), "R": valuation(R, 5),
            "Y_minus_V": valuation(Y - V, 5),
            "gcd": valuation(g, 5), "reduced_denominator": valuation(q, 5),
        },
    }


if __name__ == "__main__":
    cases = [
        (4, 2, 2, [5, 2], [0, 1], True),
        (3, 1, 4, [2, 3, 5], [3, 0, 2], True),
        (3, 1, 5, [2, 3, 5, 7], [4, 1, 3, 0], False),
        (8, 5, 3, [2, 3, 5], [2, 0, 1], False),
    ]
    results = [check(*case) for case in cases]
    assert results[0]["shared_five_prime_power"] == {
        "K": 2, "R": 1, "Y_minus_V": 1, "gcd": 1,
        "reduced_denominator": 2,
    }
    print(json.dumps({
        "reviewer": "/root/actual_collision",
        "scope": "Independent exact finite controls; not an all-parameter enumeration proof.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "status": "PASS", "cases": results,
    }, indent=2))
