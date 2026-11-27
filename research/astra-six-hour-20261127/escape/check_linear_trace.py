"""Rigorous finite enclosures for the unclipped modulus-eight trace.

Use --depth 16 for the retained run. Fixed-point transfer uses the exact
geometric recursion on the single doubling orbit of the ternary units.
A separate full-period enumeration validates the first five levels.
"""

from argparse import ArgumentParser
from array import array
from fractions import Fraction

PRECISION = 42
SCALE = 1 << PRECISION
EXTRA = 20
SIGNED_COEFFICIENTS = (0, -1, 0, 3, 0, -5, 0, 3)


def fixed_level(previous, depth):
    modulus = 3 ** depth
    smaller = modulus // 3
    period = 2 * smaller
    numerator = array("Q", [0]) * modulus
    residue = 1
    current = 0
    # The last full orbit then has at least this many prior substitutions.
    # The exact density is at most 2**depth by the two admissible parities.
    warm_steps = PRECISION + depth + 2
    for _ in range(period + warm_steps):
        residue = (residue + (modulus if residue % 2 else 0)) // 2
        if residue % 3 == 2:
            source = ((2 * residue - 1) // 3) % smaller
            current += 3 * previous[source]
        current //= 2
        numerator[residue] = current
    return numerator


def interval(numerator, depth):
    modulus = len(numerator)
    total = 0
    # Each integer division is rounded down, including for negative terms.
    for residue, value in enumerate(numerator):
        if value:
            odd = residue if residue % 2 else residue + modulus
            coefficient = SIGNED_COEFFICIENTS[odd % 8]
            total += ((coefficient * value) << EXTRA) // odd
    # If the previous supremum error is eps fixed-point units, one row
    # costs at most 2*eps + 2 for floors + 1/4 for the tail.
    density_error = 3 * ((1 << depth) - 1)
    # sum_{odd<2q} 1/odd <= 1 + log(2q) <= 2 + 2*depth.
    allowance = (5 * density_error * (2 + 2 * depth)) << EXTRA
    denominator = 4 * (SCALE << EXTRA)
    return Fraction(total - allowance, denominator), Fraction(
        total + modulus + allowance, denominator
    )


def enumerated_level(previous_numerators, previous_denominator):
    smaller = len(previous_numerators)
    modulus = 3 * smaller
    period = 2 * smaller
    denominator = previous_denominator * ((1 << period) - 1)
    numerators = [0] * modulus
    for source, weight in enumerate(previous_numerators):
        endpoint = (3 * source + 1) % modulus
        for exponent in range(1, period + 1):
            endpoint = (endpoint + (modulus if endpoint % 2 else 0)) // 2
            numerators[endpoint] += weight << (period - exponent)
    assert sum(numerators) == denominator
    return numerators, denominator


def exact_trace(numerators, denominator):
    modulus = len(numerators)
    return sum(
        Fraction(
            SIGNED_COEFFICIENTS[odd % 8] * modulus * numerators[odd % modulus],
            4 * denominator * odd,
        )
        for odd in range(1, 2 * modulus, 2)
    )


def format_outward(value, upper):
    denominator = 10 ** 7
    scaled = value * denominator
    bound = -((-scaled.numerator) // scaled.denominator) if upper else (
        scaled.numerator // scaled.denominator
    )
    sign = "-" if bound < 0 else ""
    digits, fractional = divmod(abs(bound), denominator)
    return f"{sign}{digits}.{fractional:07d}"


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--depth", type=int, default=16)
    args = parser.parse_args()
    if not 1 <= args.depth <= 18:
        parser.error("depth must lie between 1 and 18")
    previous = array("Q", [SCALE])
    exact_numerators, exact_denominator = [1], 1
    print("depth\tlower_signed_sum\tupper_signed_sum\texact_enumeration")
    for depth in range(1, args.depth + 1):
        previous = fixed_level(previous, depth)
        lower, upper = interval(previous, depth)
        verified = "not_run"
        if depth <= 5:
            exact_numerators, exact_denominator = enumerated_level(
                exact_numerators, exact_denominator
            )
            exact = exact_trace(exact_numerators, exact_denominator)
            assert lower <= exact <= upper
            for residue, approx in enumerate(previous):
                actual = Fraction(
                    SCALE * len(previous) * exact_numerators[residue], exact_denominator
                )
                assert 0 <= actual - approx <= 3 * ((1 << depth) - 1)
            verified = "yes"
        print(
            depth,
            format_outward(lower, False),
            format_outward(upper, True),
            verified,
            sep="\t",
            flush=True,
        )


if __name__ == "__main__":
    main()
