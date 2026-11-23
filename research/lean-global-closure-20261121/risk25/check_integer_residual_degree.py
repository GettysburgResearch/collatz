#!/usr/bin/env python3
"""Exact narrow controls for the residual-degree and recurrence-lattice notes.

This is not a cycle census or a verification of the external Matveev theorem.
No mathematical check relies on Python assertions, including under -O.
"""

from fractions import Fraction
from functools import reduce
from math import gcd
import json

import sympy as sp


X = sp.Symbol("X")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rat(value):
    value = sp.Rational(value)
    return Fraction(int(value.p), int(value.q))


def sym(value):
    return sp.Rational(value.numerator, value.denominator)


def polynomial_word(gaps):
    require(bool(gaps) and all(a >= 1 for a in gaps), "positive gaps required")
    p, A = len(gaps), sum(gaps)
    partials, current = [], 0
    for a in gaps:
        partials.append(current)
        current += a
    F = sp.Poly(X**p - 2**A, X, domain=sp.QQ)
    Q = sp.Poly(sum(2**s * X ** (p - 1 - j) for j, s in enumerate(partials)), X, domain=sp.QQ)
    return p, A, partials, F, Q


def scaled_positions_control(m, n):
    """One explicit PR185 Fourier-cancellation control, not an enumeration."""
    require(m != n and gcd(m, n) == 1, "coprime distinct parameters required")
    length = 2 * m * n
    profile = [int(j % (2*m) == 0 or j % (2*n) == 1) for j in range(length)]
    positions = [5*j + r + profile[j] for j in range(length) for r in range(3)]
    A = 5 * length
    gaps = [positions[j+1] - positions[j] for j in range(len(positions)-1)]
    gaps.append(A + positions[0] - positions[-1])
    return gaps


def check_control(name, gaps, expected_degree, expected_denominator=None, expected_states=None):
    p, A, partials, F, Q = polynomial_word(gaps)
    D, C = 2**A - 3**p, int(Q.eval(3))
    require(D > 0, f"{name}: positive cycle cone")
    x0 = Fraction(C, D)
    states, value = [], x0
    for a in gaps:
        states.append(value)
        require(value > 0 and value.numerator % 2 == 1 and value.denominator % 2 == 1,
                f"{name}: positive odd rational state")
        value = (3*value+1)/2**a
    require(value == x0, f"{name}: exact closure")
    if expected_states is not None:
        require(states == expected_states, f"{name}: supplied exact state list")

    G = sp.gcd(F, Q).monic()
    F0, Q0 = F.exquo(G), Q.exquo(G)
    d = F0.degree()
    require(d == expected_degree, f"{name}: residual degree")
    require(A*d % p == 0, f"{name}: integral residual constant exponent")
    residual_radius_product = Fraction(2 ** (A*d // p))
    Dpol = abs(int(F0.eval(3)))
    fiber_gcd = gcd(Dpol, int(Q0.eval(3)))
    q = Dpol // fiber_gcd
    require(q == x0.denominator, f"{name}: exact residual numerical denominator")
    require(all(x.denominator == q for x in states), f"{name}: common odd denominator")
    if expected_denominator is not None:
        require(q == expected_denominator, f"{name}: expected odd denominator")

    m, M = min(states), max(states)
    lower_radius, upper_radius = 3 + 1/M, 3 + 1/m
    # Check every rotation, keeping the same complete F and monic gcd.
    for rotation in range(p):
        aa = gaps[rotation:] + gaps[:rotation]
        xx = states[rotation:] + states[:rotation]
        _, _, ss, Fr, Qr = polynomial_word(aa)
        require(Fr == F and sp.gcd(Fr, Qr).monic() == G,
                f"{name}: cyclic polynomial gcd invariance")
        vv = [2**s*x for s, x in zip(ss, xx)]
        H = sp.Poly(sum(sym(v)*X**(p-1-j) for j, v in enumerate(vv)), X, domain=sp.QQ)
        J = H.exquo(G)
        require(sp.Poly(X-3, X, domain=sp.QQ)*H == Qr + Fr.mul_ground(sym(xx[0])),
                f"{name}: actual numerator polynomial identity")
        require(J.degree() == d-1 and rat(J.LC()) == xx[0],
                f"{name}: residual numerator degree and leading coefficient")
        actual_product = abs(rat(J.eval(0))) / xx[0]
        require(actual_product == residual_radius_product/(3+1/xx[-1]),
                f"{name}: residual constant-term root product")
        require(lower_radius**(d-1) <= actual_product <= upper_radius**(d-1),
                f"{name}: exact Enestrom-Kakeya product inequalities")
        if d > 1:
            require(actual_product > 3**(d-1), f"{name}: strict outer radius")
        else:
            require(actual_product == 1, f"{name}: empty root product")
        require((1+1/(3*xx[-1]))**p <= Fraction(2**A,3**p)**d,
                f"{name}: exact powered concentration inequality")
        next_gaps = aa[1:] + aa[:1]
        _, _, _, _, next_Q = polynomial_word(next_gaps)
        require(next_Q.mul_ground(2**aa[0]) == sp.Poly(X, X, domain=sp.QQ)*Qr-Fr,
                f"{name}: rotation sign and full polynomial identity")
        qJ = J.mul_ground(q)
        require(all(c.q == 1 for c in qJ.all_coeffs()), f"{name}: qJ integral")
        require(reduce(gcd, [abs(int(c)) for c in qJ.all_coeffs()], 0) == 1,
                f"{name}: primitive scaled residual numerator")

    # Rotate to the genuine minimum before applying the height statements.
    start = states.index(m)
    min_gaps = gaps[start:] + gaps[:start]
    _, _, ss, _, _ = polynomial_word(min_gaps)
    deficits = [p*s-A*j for j, s in enumerate(ss)]
    minimum_deficit = min(deficits)
    for start in range(p):
        require(min(deficits[(start+j) % p] for j in range(d)) == minimum_deficit,
                f"{name}: every degree-sized window sees the global two-adic deficit")
    require(-minimum_deficit <= (A-p)*(d-1), f"{name}: residual-degree deficit bound")
    kappa2 = (-minimum_deficit+p-1)//p
    multiplier = Fraction(2**A, 3**p)
    require((M/m)**p <= multiplier**p * 2**((A-p)*(d-1)),
            f"{name}: exact powered whole-cycle amplitude bound")
    require(M <= multiplier*(Fraction(3,2)**(d-1)*(m+1)-1),
            f"{name}: fixed-base whole-cycle amplitude bound")
    require(M/multiplier <= m*2**kappa2 < 2*M*multiplier,
            f"{name}: maximum versus two-adic normalization comparison")

    return {
        "name": name, "p": p, "A": A, "d": d, "degree_G": G.degree(),
        "minimum": str(m), "maximum": str(M), "odd_denominator": q,
        "residual_denominator": Dpol, "same_fiber_gcd": fiber_gcd,
        "two_adic_deficit_ceiling": kappa2,
        "integer_cycle_control": q == 1,
        "all_rotations_checked": p,
    }


def main():
    controls = [
        check_control("trivial_odd_cycle", [2], 1, 1),
        check_control("repeated_trivial_cycle", [2]*6, 1, 1),
        check_control("wrong_conjugate_rational", [1,1,1,1,2,2,1,4], 8, 233),
        check_control("sharp_two_adic_deficit", [1]*7+[6], 8, 1631),
        check_control("nontrivial_polynomial_cancellation", scaled_positions_control(2,3), 24),
    ]
    y = [187,283,427,643,967,1453,1091,1639,2461,1847,2773,2081,781,587,883,1327,1993]
    gaps = [1,1,1,1,1,2,1,1,2,1,2,3,2,1,1,1,5]
    large_gcd = check_control("small_odd_denominator_large_gcd", gaps, 17, 5,
                              [Fraction(v,5) for v in y])
    require(large_gcd["residual_denominator"] == 5077565,
            "large-gcd control complete residual denominator")
    require(large_gcd["same_fiber_gcd"] == 1015513 > max(y),
            "large-gcd control exceeds every reduced numerator")
    controls.append(large_gcd)
    print(json.dumps({"status": "PASS", "scope": "six exact controls; no cycle census",
                      "controls": controls}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
