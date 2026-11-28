"""Exact signed numerator replay for the ternary stopping-word identity."""

from fractions import Fraction
from itertools import product


def require(condition):
    if not condition:
        raise RuntimeError("denominator ladder identity failed")


def odd_count(value, steps):
    count = 0
    for _ in range(steps):
        if value.numerator % 2:
            count += 1
            value = (3 * value + 1) / 2
        else:
            value /= 2
    return count


def actual_count(cutoff, time, threshold, degree):
    denominator = 3**degree
    return sum(
        odd_count(Fraction(u, denominator), time) >= threshold
        for u in range(1, cutoff * denominator + 1)
    )


def stopping_numerator(cutoff, time, threshold, degree):
    numerator = 0
    for length in range(degree, time + 1):
        modulus = 2**length
        for prefix in product((0, 1), repeat=length - 1):
            if sum(prefix) != degree - 1:
                continue
            offset = 0
            for j, bit in enumerate((*prefix, 1)):
                if bit:
                    offset = 3 * offset + 2**j
            require(offset % 3 == 2 ** (length - 1) % 3)
            first = offset // modulus + 1
            last = (offset + cutoff * 3**degree) // modulus
            for target in range(first, last + 1):
                if odd_count(Fraction(target), time - length) >= threshold - degree:
                    numerator += 3 * (target % 3 == 2) - 1
    return numerator


def main():
    cases = 0
    for cutoff, time in [(4, 7), (11, 8), (16, 9)]:
        for threshold in range(1, 6):
            previous = actual_count(cutoff, time, threshold, 0)
            for degree in range(1, threshold + 1):
                current = actual_count(cutoff, time, threshold, degree)
                require(3 * previous - current == stopping_numerator(cutoff, time, threshold, degree))
                previous = current
                cases += 1
    print(f"Verified all {cases} signed denominator levels with exact rational dynamics.")


if __name__ == "__main__":
    main()
