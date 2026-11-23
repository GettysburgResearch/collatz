#!/usr/bin/env python3
"""Exact finite controls for the all-parameter cyclic-packet theorem.

This is not a universal proof. All checks use explicit exceptions, including
under python -O. SymPy is used only for the selected direct polynomial gcds.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from math import gcd, prod
from pathlib import Path

import sympy as sp


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def least_period(values):
    size = len(values)
    for period in range(1, size + 1):
        if size % period == 0 and all(
            values[i] == values[(i + period) % size] for i in range(size)
        ):
            return period
    raise RuntimeError("period search failed")


def valuation(n, prime):
    result = 0
    while n % prime == 0:
        n //= prime
        result += 1
    return result


def polynomial_check(a, b, r, ns, ss, profile, positions, dpol, numerator):
    z, w = sp.symbols("z w")
    L = len(profile)
    p = b * L
    X = 2**a
    F = sp.Poly(z**p - 2 ** (a * L), z, domain=sp.QQ)
    coefficients = [2**position for position in positions]
    Q = sp.Poly.from_list(coefficients, z, domain=sp.QQ)
    actual_gcd = F.gcd(Q).monic()
    F0, Q0 = F.exquo(actual_gcd), Q.exquo(actual_gcd)
    base = sp.Poly(z ** (b * r) - X**r, z, domain=sp.QQ)
    expected_F0 = base
    for ni in ns:
        factor = sp.Poly(z ** (b * r * ni) - X ** (r * ni), z, domain=sp.QQ)
        expected_F0 *= factor.exquo(base)
    require(F0 == expected_F0, "complete literal F,Q gcd disagrees")
    require(int(F0.eval(3)) == -dpol, "complete denominator sign")
    require(int(Q0.eval(3)) == numerator, "complete residual numerator")

    P = sp.Poly.from_list(list(reversed(profile)), w, domain=sp.QQ)
    total = sp.Poly(w**L - 1, w, domain=sp.QQ)
    base_profile = sp.Poly(w**r - 1, w, domain=sp.QQ)
    H = base_profile
    for ni in ns:
        H *= sp.Poly(w ** (r * ni) - 1, w, domain=sp.QQ).exquo(base_profile)
    require(P.gcd(total).monic() == total.exquo(H), "profile root gcd")
    return {
        "literal_full_gcd_checked": True,
        "profile_gcd_checked": True,
        "gcd_degree": actual_gcd.degree(),
        "residual_degree": F0.degree(),
    }


def check_case(name, a, b, r, ns, ss, check_polynomial=False):
    k = len(ns)
    require(k >= 2 and r >= k and len(ss) == k, "packet cardinality")
    require(all(ni >= 2 for ni in ns), "packet sizes")
    require(all(gcd(u, v) == 1 for u, v in combinations(ns, 2)), "pairwise gcd")
    require(len(set(ss)) == k and all(0 <= s < r for s in ss), "offsets")
    X, Y, V = 2**a, 3**b, 2**b
    require(b >= 1 and a - b >= 2 and X > Y, "embedding parameters")
    L = r * prod(ns)
    A, p = a * L, b * L
    S = sum(ni - 1 for ni in ns)
    profile = [1 + sum(j % (r * ni) == si for ni, si in zip(ns, ss))
               for j in range(L)]
    require(set(profile) == {1, 2}, "profile powers of two")
    positions = [a * j + t + profile[j] - 1 for j in range(L) for t in range(b)]
    require(len(set(positions)) == p and max(positions) < A, "word positions")
    bits = [0] * A
    for position in positions:
        bits[position] = 1
    require(least_period(profile) == L, "primitive coefficient profile")
    require(least_period(bits) == A, "primitive shortcut word")

    # Two independent carry recurrences: ordered one positions and the full
    # affine branch composition through every zero and one of the binary word.
    C = 0
    for position in positions:
        C = 3 * C + 2**position
    affine_carry, odd_count = 0, 0
    for time, bit in enumerate(bits):
        if bit:
            affine_carry = 3 * affine_carry + 2**time
            odd_count += 1
    require(C == affine_carry and odd_count == p, "literal complete carry")
    D = 2**A - 3**p
    K = X**r - Y**r
    factors = [(X ** (r * ni) - Y ** (r * ni)) // K for ni in ns]
    require(all((X ** (r * ni) - Y ** (r * ni)) % K == 0 for ni in ns),
            "integral repunit quotient")
    R = prod(factors)
    B = (K // (X - Y)) * R + sum(
        X**si * Y ** (r * ni - 1 - si) * (R // Ri)
        for ni, si, Ri in zip(ns, ss, factors)
    )
    dpol, numerator = K * R, (Y - V) * B
    x0 = Fraction(C, D)
    require(x0 == Fraction(numerator, dpol), "exact packet rational value")
    require(all(gcd(U, W) == 1 for U, W in combinations(factors, 2)),
            "actual repunits pairwise coprime")
    require(all(gcd(Ri, X * Y) == 1 for Ri in factors), "repunit base units")
    for ni, si, Ri in zip(ns, ss, factors):
        unit = X**si * Y ** (r * ni - 1 - si) * (R // Ri)
        require((B - unit) % Ri == 0 and gcd(unit, Ri) == 1, "packet unit residue")
    require(gcd(B, R) == 1, "full packet product is coprime to B")
    g = gcd(dpol, numerator)
    bound = K * (Y - V)
    q = x0.denominator
    require(bound % g == 0, "full numerical gcd divisibility")
    require(q == dpol // g, "full reduced denominator identity")
    require(q % (R // gcd(R, Y - V)) == 0, "full surviving repunit divisor")
    require(q * Y > X ** (r * S), "complete denominator lower bound")
    require(q ** (r * S) > dpol ** (r * S - r - 1), "logarithmic exponent")
    require(q * q > dpol and q > 1, "square root and integer exclusion")
    require(bound < X ** (r + 1), "uniform gcd upper bound")

    # Exact rational orbit legality uses the numerator parity over odd q.
    x = x0
    states = []
    for bit in bits:
        require(x > 0 and x.denominator % 2 == 1, "positive odd-denominator state")
        require(x.numerator % 2 == bit, "prescribed rational branch is legal")
        require(x.denominator == q, "complete reduced denominator survives rotation")
        states.append(x)
        x = (3 * x + 1) / 2 if bit else x / 2
    require(x == x0, "entire rational orbit closes")
    B0 = Fraction(Y - V, X - Y)
    require(min(states) >= B0 / 2, "all shortcut states satisfy floor bound")
    for j in range(L):
        z0, z1 = states[a * j], states[a * ((j + 1) % L)]
        require(X * z1 == Y * z0 + profile[j] * (Y - V), "actual boundary recurrence")
        require(B0 <= z0 <= 2 * B0, "boundary min/max bound")

    # Choose the ordinary realizer strictly above the rational fixed point.
    modulus = 2**A
    ordinary = (C * pow(D, -1, modulus)) % modulus
    if ordinary <= x0:
        ordinary += ((x0.numerator - ordinary * x0.denominator) //
                     (modulus * x0.denominator) + 1) * modulus
    start = ordinary
    require(Fraction(start) > x0 and start > 0, "ordinary starting value")
    for bit in bits:
        require(ordinary % 2 == bit, "ordinary finite word realization")
        ordinary = (3 * ordinary + 1) // 2 if bit else ordinary // 2
    require(ordinary < start, "chosen ordinary realizer strictly descends")

    item = {
        "name": name,
        "parameters": {"a": a, "b": b, "r": r, "n": ns, "s": ss},
        "A": A, "p": p, "profile_period": L, "shortcut_period": A,
        "full_gcd": str(g), "gcd_bound": str(bound),
        "complete_denominator_bits": dpol.bit_length(),
        "final_denominator_bits": q.bit_length(),
        "rational_states_replayed": A, "ordinary_steps_replayed": A,
        "minimum_state": str(min(states)), "floor_lower_bound": str(B0 / 2),
        "shared_prime_K_R_YminusV": gcd(gcd(K, R), Y - V),
        "polynomial": {"literal_full_gcd_checked": False},
    }
    if name == "shared_prime_powers":
        require(gcd(gcd(K, R), Y - V) == 5, "required shared-prime control")
        item["prime_5_valuations"] = {
            label: valuation(value, 5)
            for label, value in [("K", K), ("R", R), ("Y_minus_V", Y - V),
                                 ("B", B), ("g", g), ("q", q)]
        }
    if check_polynomial:
        item["polynomial"] = polynomial_check(
            a, b, r, ns, ss, profile, positions, dpol, numerator
        )
    return item


def negative_controls():
    a, b, r, ns, ss = 5, 3, 2, [3, 6], [0, 1]
    X, Y, V = 2**a, 3**b, 2**b
    K, L = X**r - Y**r, r * prod(ns)
    factors = [(X ** (r * n) - Y ** (r * n)) // K for n in ns]
    R = prod(factors)
    B = (K // (X - Y)) * R + sum(
        X**s * Y ** (r * n - 1 - s) * (R // Ri)
        for n, s, Ri in zip(ns, ss, factors)
    )
    displayed_gcd = gcd(K * R, (Y - V) * B)
    profile = [1 + sum(j % (r * n) == s for n, s in zip(ns, ss)) for j in range(L)]
    require(gcd(*factors) == 2326513, "noncoprime factor control")
    require(displayed_gcd == 11632565 > K * (Y - V), "noncoprime bound must fail")
    require(least_period(profile) < L, "noncoprime primitive claim must fail")
    overlapping = [1 + (j % 4 == 0) + (j % 6 == 0) for j in range(12)]
    require(3 in overlapping, "overlap leaves powers-of-two domain")
    return {
        "noncoprime_periods": {
            "parameters": {"a": a, "b": b, "r": r, "n": ns, "s": ss},
            "repunit_gcd": str(gcd(*factors)),
            "unreduced_displayed_numerical_gcd": str(displayed_gcd),
            "claimed_bound_outside_domain": str(K * (Y - V)),
            "profile_length": L, "least_profile_period": least_period(profile),
            "complete_polynomial_denominator_claimed": False,
        },
        "overlapping_offsets": {
            "r": 2, "n": [2, 3], "s": [0, 0],
            "coefficient_values": sorted(set(overlapping)),
            "binary_power_embedding_rejected": True,
        },
    }


def main():
    cases = [
        ("original_two_packets", 5, 3, 2, [2, 3], [0, 1], True),
        ("shared_prime_powers", 4, 2, 2, [4, 5], [0, 1], False),
        ("nontrivial_numerical_gcd", 13, 8, 2, [4, 5], [0, 1], False),
        ("large_profile_cancellation", 5, 3, 2, [10, 11], [0, 1], False),
        ("three_packets_polynomial", 3, 1, 3, [2, 3, 5], [0, 1, 2], True),
        ("three_sparse_residues", 5, 3, 5, [2, 3, 5], [0, 2, 4], False),
        ("four_packets", 3, 1, 4, [2, 3, 5, 7], [0, 1, 2, 3], False),
        ("noncoprime_embedding", 6, 3, 3, [2, 3], [1, 2], True),
        ("nearcritical_high_floor", 65, 41, 2, [2, 3], [0, 1], False),
    ]
    results = [check_case(*parameters) for parameters in cases]
    require(Fraction(results[-1]["minimum_state"]) > 40, "high-floor control")
    packet = {
        "status": "PASS",
        "evidence": "exact finite controls; all-parameter theorem is the written proof",
        "arithmetic": "Python integers and Fraction; SymPy QQ polynomial gcd",
        "sympy_version": sp.__version__,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "case_count": len(results),
        "literal_polynomial_gcd_cases": sum(
            item["polynomial"]["literal_full_gcd_checked"] for item in results
        ),
        "total_rational_and_ordinary_steps_each": sum(item["A"] for item in results),
        "cases": results,
        "rejected_hypothesis_controls": negative_controls(),
    }
    print(json.dumps(packet, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
