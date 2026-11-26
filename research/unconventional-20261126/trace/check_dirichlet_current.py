"""Certify a positive Dirichlet increment from an upper bound on its damping term.

All comparisons and transfer arrays are integers. Infinite letter tails use the
mean-one density bound by the number of cells. Infinite spatial tails use a
whole-period mass bound. NumPy supplies integer arrays only.
"""
from fractions import Fraction
import json
import numpy as np


def upper_damping():
    depth, bits, letters = 13, 40, 50
    scale = 1 << bits
    mass = np.array([scale], dtype=np.int64)
    cap = np.iinfo(np.int64).max
    for level in range(1, depth + 1):
        modulus = 3 ** level
        # A density with mean one is bounded by the number of cells.
        tail = (scale * modulus + (1 << letters) - 1) // (1 << letters)
        if 3 * int(mass.max()) + (1 << letters) > cap:
            raise OverflowError("Transfer quotient would exceed the array range")
        result = np.full(modulus, tail, dtype=np.int64)
        residue = np.arange(modulus, dtype=np.int64)
        for exponent in range(1, letters + 1):
            residue = 2 * residue % modulus
            use = residue % 3 == 1
            terms = (3 * mass[(residue[use] - 1) // 3]
                     + (1 << exponent) - 1) // (1 << exponent)
            if int(result.max()) + int(terms.max()) > cap:
                raise OverflowError("Transfer accumulation would exceed the array range")
            result[use] += terms
        mass = result
    odd = np.arange(1, modulus + 1, 2, dtype=np.int64)
    if modulus * (3 * modulus + 1) > cap:
        raise OverflowError("Spatial denominator would exceed the array range")
    denominator = odd * (3 * odd + 1)
    if int(mass.max()) + int(denominator.max()) > cap:
        raise OverflowError("Spatial quotient would exceed the array range")
    rounded = (mass[odd % modulus] + denominator - 1) // denominator
    # Python's accumulating integer avoids an overflowing NumPy total.
    head = Fraction(sum(map(int, rounded)), scale)
    tail = Fraction(2, 3 * modulus)
    bound = head + tail
    c_lower = Fraction(1, 7) + Fraction(1, 3 * 7 ** 3)
    if bound >= c_lower:
        raise ArithmeticError("The rounded damping bound does not certify a positive increment")
    return {
        "depth": depth,
        "ternary_modulus": modulus,
        "fixed_point_bits": bits,
        "retained_exponents": letters,
        "head_upper": str(head),
        "tail_upper": str(tail),
        "damping_upper": str(bound),
        "c_star_lower": str(c_lower),
        "dirichlet_increment_lower": str(c_lower - bound),
        "verdict": "B14 > B13"
    }


if __name__ == "__main__":
    print(json.dumps(upper_damping(), indent=2))
