#!/usr/bin/env python3
"""Check the new Fourier-interface formulas, not any unproved basin estimate.

All modular and rational checks use integer/Fraction arithmetic. Complex and
trigonometric numbers below are explicitly numerical sanity checks.
"""

from __future__ import annotations

import cmath
from fractions import Fraction
import json
import math
from pathlib import Path


def shortcut(n: int) -> int:
    assert n > 0
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def odd_part(n: int) -> int:
    assert n > 0
    return n // (n & -n)


def odd_step(n: int) -> int:
    assert n > 0 and n % 2 == 1
    return odd_part(3 * n + 1)


def initial(n: int) -> int:
    return 1 if n == 0 else int(n % 5 != 0)


def accelerated_output(n: int) -> int:
    return 1 if n == 0 else initial(odd_step(odd_part(n)))


def radial_sum(r: float, zeta: complex) -> complex:
    """Numerical value of (1-r) E(r*zeta), using exact exponent residues."""
    log_r = math.log(r)
    out = 0j
    p = 1
    while 3 * p * log_r > -750:
        numerator = math.exp(3 * p * log_r)
        denominator = -math.expm1(10 * p * log_r)
        out += (1 - r) * numerator / denominator * zeta ** ((3 * p) % 5)
        p *= 2
    return out


def main() -> None:
    limit = 10_000
    for n in range(1, limit + 1):
        assert int(shortcut(n) % 5 == 0) == int(n % 10 in (0, 3))
        assert initial(2 * n) == initial(n)
        assert accelerated_output(n) == int(odd_part(n) % 5 != 3)
        assert accelerated_output(2 * n) == accelerated_output(n)
        assert (odd_part(n) % 10 == 3) == (odd_part(n) % 5 == 3)

    assert initial(1) == initial(2) == 1
    assert accelerated_output(1) == accelerated_output(2) == 1
    assert accelerated_output(3) == 0
    assert accelerated_output(shortcut(3)) == accelerated_output(5) == 1

    residues = [(3 * pow(2, j, 5)) % 5 for j in range(4)]
    assert residues == [3, 1, 2, 4]
    assert (3 * pow(2, 4, 5)) % 5 == residues[0]
    weights = [Fraction(1, 10) * Fraction(1, 2**j) / (1 - Fraction(1, 16)) for j in range(4)]
    assert weights == [Fraction(8, 75), Fraction(4, 75), Fraction(2, 75), Fraction(1, 75)]
    assert sum(weights) == Fraction(1, 5)

    zeta = cmath.exp(2j * math.pi / 5)
    residue = sum(float(w) * zeta**j for w, j in zip(weights, residues))
    imaginary_formula = (math.sin(2 * math.pi / 5) - 2 * math.sin(math.pi / 5)) / 25
    assert abs(residue.imag - imaginary_formula) < 1e-15
    assert residue.imag < 0

    numeric_radial = []
    for k in (2, 4, 6, 8):
        r = 1 - 10.0 ** (-k)
        value = radial_sum(r, zeta)
        numeric_radial.append({
            "r": r,
            "real": value.real,
            "imaginary": value.imag,
            "distance_from_exact_formula_evaluated_numerically": abs(value - residue),
        })
    assert numeric_radial[-1]["distance_from_exact_formula_evaluated_numerically"] < 1e-7

    result = {
        "status": "new formulas checked; no Collatz proof or uniform basin norm bound claimed",
        "exact_checks": {
            "positive_integer_range": [1, limit],
            "shortcut_preimage_residues_mod_10": [0, 3],
            "initial_dyadic_invariance": True,
            "accelerated_modular_formula": True,
            "accelerated_dyadic_invariance": True,
            "anchor_values_at_1_and_2": [1, 1],
            "failure_of_full_fixed_point_at_3": {"d_3": 0, "d_T3": 1},
            "exponent_residue_cycle_mod_5": residues,
            "rational_boundary_weights": {str(j): str(w) for j, w in zip(residues, weights)},
        },
        "numerical_sanity_checks_not_proofs": {
            "boundary_residue_real": residue.real,
            "boundary_residue_imaginary": residue.imag,
            "raw_shortcut_L1_logarithm_coefficient": 2 / (5 * math.pi) / math.tan(math.pi / 10),
            "radial_values": numeric_radial,
        },
        "infinite_conclusions": "See the written proofs in FOURIER_IDEMPOTENT_CLOSURE_ATTEMPT.md",
    }
    path = Path(__file__).with_name("fourier-interface-checks.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
