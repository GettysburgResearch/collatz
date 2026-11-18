"""Exact ternary transfer for C_Q with cap 2Q, including a small-depth word audit."""
import argparse
from fractions import Fraction
from itertools import product


def transfer(depth):
    cap = 2 * depth
    base = 1 << cap
    slopes, moments, maxima = [1], [0], [0]
    previous_scale = 1
    for _ in range(depth):
        old_modulus = len(slopes)
        modulus = 3 * old_modulus
        new_slopes, new_moments, new_maxima = ([0] * modulus for _ in range(3))
        for residue in range(modulus):
            if residue % 3 == 0:
                continue
            # The legal exponents are even for residue 1 and odd for residue 2.
            first = 2 if residue % 3 == 1 else 1
            for exponent in range(first, cap + 1, 2):
                parent = ((residue << exponent) - 1) // 3 % old_modulus
                g = slopes[parent]
                if not g:
                    continue
                weight = base >> exponent
                new_slopes[residue] += 3 * weight * g
                new_moments[residue] += 3 * weight**2 * (previous_scale * g + 3 * moments[parent])
                new_maxima[residue] = max(new_maxima[residue],
                                          weight * (previous_scale + 3 * maxima[parent]))
        slopes, moments, maxima = new_slopes, new_moments, new_maxima
        previous_scale *= base
    assert sum(slopes) == (3 * (base - 1))**depth
    return slopes, moments, maxima


def literal(depth):
    """Form forward affine maps and resolve their odd target by congruence."""
    modulus = 3**depth
    scale = 1 << (2 * depth**2)
    slopes, moments, maxima = ([0] * modulus for _ in range(3))
    scalar = Fraction(0)
    cycle_term = 0
    for word in product(range(1, 2 * depth + 1), repeat=depth):
        offset, denominator = 0, 1
        for exponent in word:
            offset = 3 * offset + denominator
            denominator <<= exponent
        residue = (offset * pow(denominator, -1, modulus)) % modulus
        target = residue if residue % 2 else residue + modulus
        g = modulus * scale // denominator
        f = offset * scale // denominator
        slopes[residue] += g
        moments[residue] += g * f
        maxima[residue] = max(maxima[residue], f)
        if target > 1:
            scalar += Fraction(g * f, depth * (scale * target)**2)
            if (f << 32) >= (2**32 - 1) * target * scale:
                cycle_term = 1
    return (slopes, moments, maxima), scalar + cycle_term


def evaluate(depth):
    arrays = transfer(depth)
    slopes, moments, maxima = arrays
    modulus = len(slopes)
    scale = 1 << (2 * depth**2)
    precision = 10**15
    total = inexact = cycle_term = 0
    for target in range(3, 2 * modulus + 1, 2):
        residue = target % modulus
        if not slopes[residue]:
            continue
        if (maxima[residue] << 32) >= (2**32 - 1) * scale * target:
            cycle_term = 1
        term, remainder = divmod(precision * moments[residue], depth * (scale * target)**2)
        total += term
        inexact += bool(remainder)
    divisor = precision // 10**6
    lower = cycle_term * 10**6 + total // divisor
    upper = cycle_term * 10**6 + (total + inexact + divisor - 1) // divisor
    if depth <= 4:
        expected_arrays, expected = literal(depth)
        assert expected_arrays == arrays
        assert lower <= 10**6 * expected <= upper
    return cycle_term, lower, upper


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("max_depth", nargs="?", type=int, default=10)
    args = parser.parse_args()
    if args.max_depth < 1:
        parser.error("max_depth must be positive")
    print("Q cycle_term C_lower_ppm C_upper_ppm")
    for q in range(1, args.max_depth + 1):
        print(q, *evaluate(q))
