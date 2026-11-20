#!/usr/bin/env python3
"""Exact finite checks for MAHLER_AND_INTEGRALITY_AUDIT.md.

This is not a Collatz proof or a boundary-regularity certificate.
No assertion is disabled by Python optimization.
"""

from collections import defaultdict
from fractions import Fraction
import json
from math import gcd


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def clean(poly):
    return {e: c for e, c in poly.items() if c}


def mixed_residual(coefficients):
    """Exact roots-of-unity projection, minus w(F(w^3)-F(w^6))."""
    result = defaultdict(int)
    for n, coefficient in coefficients.items():
        if n % 3 == 2:
            result[2 * n] += coefficient
        result[3 * n + 1] -= coefficient
        result[6 * n + 1] += coefficient
    return clean(result)


def coefficient_signature(coefficients):
    result = defaultdict(int)
    limit = max(coefficients, default=0)
    f = lambda n: coefficients.get(n, 0)
    for m in range(1, limit + 1):
        result[6 * m + 1] = f(m) - f(2 * m)
    for k in range(limit + 1):
        result[6 * k + 4] = f(3 * k + 2) - f(2 * k + 1)
    return clean(result)


def check_coefficient_equivalence():
    for n in range(1, 129):
        coeffs = {n: 1}
        require(mixed_residual(coeffs) == coefficient_signature(coeffs),
                f"Coefficient signature failed on basis index {n}")
    coeffs = {n: (n * n + 3 * n + 1) % 11 - 5 for n in range(1, 129)}
    require(mixed_residual(coeffs) == coefficient_signature(coeffs),
            "Coefficient signature failed on signed integer combination")
    return 129


def oddpart(n):
    while n % 2 == 0:
        n //= 2
    return n


def check_parseval_redundancy():
    # These infinite Boolean functions obey doubling invariance. They are not
    # claimed to obey the odd Collatz relation. Comparing residuals checks that
    # taking the proposed norm has introduced no additional equation.
    functions = [
        lambda n: 1,
        lambda n: int(oddpart(n) == 3),
        lambda n: int(oddpart(n) % 5 in (1, 3)),
    ]
    cutoff = 1600
    for index, f in enumerate(functions):
        norm_residual = defaultdict(int)
        radial_residual = defaultdict(int)
        for n in range(1, cutoff // 4 + 1):
            if n % 3 == 2:
                norm_residual[4 * n] += f(n) ** 2
                radial_residual[4 * n] += f(n)
        for n in range(1, (cutoff - 2) // 6 + 1):
            coefficient = f(n) - (f(n // 2) if n % 2 == 0 else 0)
            norm_residual[6 * n + 2] -= coefficient ** 2
            radial_residual[6 * n + 2] -= f(n)
            if 12 * n + 2 <= cutoff:
                radial_residual[12 * n + 2] += f(n)
        require(clean(norm_residual) == clean(radial_residual),
                f"Norm/radial identity mismatch for fixture {index}")

    # Sparse analytic control: doubling + Boolean does not give odd invariance.
    sparse = {n: int(oddpart(n) == 3) for n in range(1, 129)}
    require(mixed_residual(sparse).get(10) == -1,
            "Sparse control must fail the odd relation at n=3")
    return {"exact_residual_comparisons": len(functions),
            "coefficient_cutoff": cutoff, "sparse_control_w10": -1}


def component_count(period):
    parent = list(range(period))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        parent[find(x)] = find(y)

    for x in range(period):
        union(x, (2 * x) % period)
        union(x, (3 * x + 1) % period)
    return len({find(x) for x in range(period)})


def check_moduli():
    moduli = sorted(set(range(1, 256, 2)) |
                    {3 ** j for j in range(1, 9)} |
                    {5 * 3 ** 7, 5 * 7 * 11})
    for period in moduli:
        require(component_count(period) == 1,
                f"More than one residue component modulo {period}")
    return {"number_of_moduli": len(moduli), "largest_modulus": max(moduli)}


def forward_gap_cycle(gaps):
    a = c = 0
    for gap in gaps:
        c = 3 * c + 2 ** a
        a += gap
    d = 2 ** a - 3 ** len(gaps)
    require(d > 0, "Expected a positive cycle denominator")
    root = Fraction(c, d)
    states = []
    x = root
    for gap in gaps:
        states.append(x)
        require(x > 0 and x.denominator % 2 == 1 and x.numerator % 2 == 1,
                "Gap-cycle state is not a positive odd rational")
        require(x.numerator % 3 != 0 and x.denominator % 3 != 0,
                "Gap-cycle state is not a ternary unit")
        y = 3 * x + 1
        require(y.numerator % 2 ** gap == 0,
                "Advertised gap is too large")
        require(y.numerator % 2 ** (gap + 1) != 0,
                "Advertised gap is too small")
        x = y / 2 ** gap
    require(x == root, "Exact gap-cycle replay did not close")
    return root, c, d, a, states


def remove_two_three(n):
    for p in (2, 3):
        while n % p == 0:
            n //= p
    return n


def outside_norm_product(r):
    return Fraction(remove_two_three(r.denominator),
                    remove_two_three(abs(r.numerator)))


def denominator_height_exp2(r):
    return remove_two_three(r.denominator)


def wrong_signed_height_exp2(r):
    return remove_two_three(abs(r.numerator))


def check_height_and_cycles():
    require(denominator_height_exp2(Fraction(5)) == 1,
            "Integer denominator height should vanish")
    require(wrong_signed_height_exp2(Fraction(5)) == 5,
            "Wrong height must count the numerator factor 5")
    require(denominator_height_exp2(Fraction(1, 5)) == 5,
            "The denominator factor 5 must be detected")
    require(wrong_signed_height_exp2(Fraction(1, 5)) == 1,
            "Wrong sign must miss denominator factor 5")

    simple, c0, d0, a0, _ = forward_gap_cycle([1, 1, 1, 1, 4])
    require(simple == Fraction(211, 13), "Unexpected simple root")
    shortcut_states = []
    x = simple
    for bit in [1, 1, 1, 1, 1, 0, 0, 0]:
        shortcut_states.append(x)
        require(x.numerator % 2 == bit, "Shortcut parity mismatch")
        x = (3 * x + 1) / 2 if bit else x / 2
    require(x == simple, "Shortcut replay did not close")
    require([x.numerator for x in shortcut_states] ==
            [211, 323, 491, 743, 1121, 1688, 844, 422],
            "Unexpected shortcut-state numerators")
    require(outside_norm_product(simple) == Fraction(13, 211),
            "Incorrect product for simple root")

    gaps = [2] * 10 + [1] * 7
    root, c, d, a, states = forward_gap_cycle(gaps)
    require(root == Fraction(60888923, 71515), "Unexpected positive-score root")
    require(8 * len(gaps) - 5 * a == 1, "Loop score should equal one")
    require(outside_norm_product(root) == Fraction(71515, 60888923),
            "Incorrect product for positive-score root")
    require(root.denominator > 1 and outside_norm_product(root) < 1,
            "Positive-score product counterexample failed")
    require(gcd(root.denominator, 6) == 1, "Denominator has a forbidden factor")

    repetitions = 0
    for count in range(2, 9):
        repeated, ct, dt, _, _ = forward_gap_cycle(gaps * count)
        factor = sum((2 ** a) ** (count - 1 - j) *
                     (3 ** len(gaps)) ** j for j in range(count))
        require(ct == c * factor and dt == d * factor,
                "Repeated-word common factor mismatch")
        require(repeated == root, "Reduced root changed on word repetition")
        repetitions += 1
    return {
        "simple_root": str(simple),
        "simple_product": str(outside_norm_product(simple)),
        "positive_score_root": str(root),
        "positive_score_product": str(outside_norm_product(root)),
        "positive_loop_score": 1,
        "repetitions_checked": repetitions,
        "height_sign_counterexamples": ["5", "1/5"],
    }


def check_positive_inverse_letters():
    roots = [1, 5, 7, 11, 13]
    count = 0
    for root in roots:
        frontier = [root]
        for _ in range(5):
            following = []
            for x in frontier:
                for gap in range(1, 9):
                    numerator = 2 ** gap * x - 1
                    if numerator % 3:
                        continue
                    y = numerator // 3
                    if y % 3 == 0:
                        continue
                    require(y > 0 and y % 2 == 1,
                            "Legal inverse letter lost positive odd integrality")
                    require((3 * y + 1) // 2 ** gap == x and
                            (3 * y + 1) % 2 ** gap == 0,
                            "Inverse letter replay failed")
                    following.append(y)
                    count += 1
            frontier = following
    return {"roots": roots, "depth": 5, "gap_cap": 8,
            "legal_letters_replayed": count}


def main():
    receipt = {
        "status": "PASS",
        "scope": "Exact finite checks and counterexamples; no global Collatz closure",
        "coefficient_equivalence_cases": check_coefficient_equivalence(),
        "parseval_redundancy": check_parseval_redundancy(),
        "periodic_residue_checks": check_moduli(),
        "height_and_cycles": check_height_and_cycles(),
        "positive_inverse_replays": check_positive_inverse_letters(),
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
