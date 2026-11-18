"""Bound the signed harmonic increment using only integer arithmetic."""

import argparse
from fractions import Fraction

from check_maximum_intervals import SCALE, advance


def drift_interval():
    # log(4/3)/2 = atanh(1/7).
    terms = 16
    lower = sum(Fraction(1, (2 * i + 1) * 7 ** (2 * i + 1)) for i in range(terms))
    tail = Fraction(49, 48 * (2 * terms + 1) * 7 ** (2 * terms + 1))
    return lower, lower + tail


def interval(values, error):
    modulus = len(values)
    blocks = max(1, 300000 // modulus)
    terms = blocks * modulus
    extra_bits = 2**44
    correction = 0
    for x in range(1, 2 * terms, 2):
        correction += extra_bits * values[x % modulus] // (x * (3 * x + 1))
    lower = Fraction(correction, SCALE * extra_bits)
    # Sum of the kernels is at most sum(1/(3n²), n>=1) < 1.
    upper = lower + Fraction(error, SCALE) + Fraction(terms, SCALE * extra_bits)
    upper += Fraction(1 + blocks, 12 * blocks**2 * modulus)
    low_drift, high_drift = drift_interval()
    return low_drift - upper, high_drift - lower


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("depth", type=int, default=10, nargs="?")
    horizon = parser.parse_args().depth
    values, error = [SCALE], 0
    for q in range(horizon + 1):
        low, high = interval(values, error)
        # Round outwards to integral millionths.
        print(q, (10**6 * low).__floor__(), (10**6 * high).__ceil__(), flush=True)
        if q != horizon:
            values, error = advance(values, error, q + 1)


if __name__ == "__main__":
    main()
