#!/usr/bin/env python3
"""Exact controls for a failed all-word cycle attack, not a cycle proof.

Only Python's standard library is used. The search used to discover the
five-edge witness is deliberately not a dependency of its verification.
"""

from collections import Counter
from fractions import Fraction
from math import gcd, prod
import json


def shortcut(n):
    assert isinstance(n, int) and n > 0
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def odd_edge(x):
    assert x > 0 and x % 2
    y = 3 * x + 1
    a = 0
    while y % 2 == 0:
        y //= 2
        a += 1
    return y, a


def residual(sources, images):
    out = Counter(images)
    out.subtract(sources)
    return {str(n): c for n, c in sorted(out.items()) if c}


def residue_counts(values, q):
    return Counter(n % q for n in values)


def rational_shortcut(x):
    assert x.denominator % 2
    parity = x.numerator % 2
    return (3 * x + 1) / 2 if parity else x / 2


def main():
    edges = [(25, 19, 2), (19, 29, 1), (29, 11, 3),
             (55, 83, 1), (83, 125, 1)]
    assert all(odd_edge(x) == (y, a) for x, y, a in edges)
    odd_sources = [x for x, y, a in edges]
    odd_images = [y for x, y, a in edges]
    assert len(set(odd_sources)) == len(edges)
    assert len(set(odd_images)) == len(edges)
    assert all(x > 1 and gcd(x, 6) == 1 for x in odd_sources + odd_images)
    assert prod(odd_sources) == prod(odd_images) == 62882875
    assert Counter(odd_sources) != Counter(odd_images)

    # Expand both paths into genuine shortcut edges. The path boundary is not
    # silently identified: 22 maps to 11, and the second path starts at 55.
    shortcut_sources = [25, 38, 19, 29, 44, 22, 55, 83]
    shortcut_images = [shortcut(n) for n in shortcut_sources]
    assert shortcut_images == [38, 19, 29, 44, 22, 11, 83, 125]
    assert len(set(shortcut_sources)) == len(shortcut_sources)
    assert len(set(shortcut_images)) == len(shortcut_images)
    assert residual(shortcut_sources, shortcut_images) == {
        "11": 1, "25": -1, "55": -1, "125": 1}
    assert residue_counts(shortcut_sources, 4) == residue_counts(shortcut_images, 4)
    assert residue_counts(shortcut_sources, 14) == residue_counts(shortcut_images, 14)

    A = sum(a for _, _, a in edges)
    p = len(edges)
    D = 2 ** A - 3 ** p
    m = min(odd_sources)
    M = (p * 2 ** A - D) // (3 * D)
    assert (A, p, D, m, M) == (8, 5, 13, 19, 32)
    assert D * (3 * m + 1) <= p * 2 ** A
    word = [n % 2 for n in shortcut_sources]
    positions = [i for i, e in enumerate(word) if e]
    C = sum(3 ** (p - 1 - j) * 2 ** d for j, d in enumerate(positions))
    assert word == [1, 0, 1, 1, 0, 0, 1, 1]
    assert gcd(A, p) == 1  # Any repetition count would divide A and p.
    assert (C, C % D, gcd(C, D)) == (581, 9, 1)

    # A primitive positive rational cycle yields a different integer set that
    # satisfies all Fourier tests with orders dividing 24, while failing the
    # exact polynomial identity. The full denominator remains 13.
    rational = [Fraction(C, D)]
    for _ in range(A - 1):
        rational.append(rational_shortcut(rational[-1]))
    assert rational_shortcut(rational[-1]) == rational[0]
    assert len(set(rational)) == A
    assert [x.numerator % 2 for x in rational] == word
    q = 8
    modulus = 6 * q
    lifts = [(x.numerator * pow(x.denominator, -1, modulus)) % modulus
             for x in rational]
    assert lifts == [41, 38, 19, 29, 44, 46, 23, 11]
    assert len(set(lifts)) == A and all(n > 1 and n % 3 for n in lifts)
    images = [shortcut(n) for n in lifts]
    assert len(set(images)) == A
    assert residue_counts(lifts, 3 * q) == residue_counts(images, 3 * q)
    assert Counter(lifts) != Counter(images)
    assert min(lifts) <= M

    result = {
        "status": "exact_obstructions_only_no_Collatz_closure",
        "distinct_odd_edges": edges,
        "source_and_image_product": prod(odd_sources),
        "shortcut_sources": shortcut_sources,
        "shortcut_images": shortcut_images,
        "shortcut_polynomial_residual": residual(shortcut_sources, shortcut_images),
        "finite_Fourier_orders_passed_by_product_witness": [4, 14],
        "full_word": word,
        "A": A, "p": p, "D": D, "C": C, "C_mod_D": C % D,
        "cycle_minimum_inequality_passes": True,
        "candidate_minimum": m, "minimum_upper_bound": M,
        "rational_cycle": [str(x) for x in rational],
        "root_of_unity_lifts": lifts,
        "lift_images": images,
        "lift_residue_modulus": 3 * q,
        "lift_polynomial_residual": residual(lifts, images),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
