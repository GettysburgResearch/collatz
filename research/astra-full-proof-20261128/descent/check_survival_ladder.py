"""Compare rational-source enumeration with independent affine-word endpoints."""

from fractions import Fraction
from itertools import product


def trace(source, count, freeze=False):
    value = source
    weight = Fraction(1)
    minimum = value
    seen = {value}
    frozen = False
    for _ in range(count):
        while value.numerator % 2 == 0:
            value /= 2
            minimum = min(minimum, value)
            frozen = frozen or (freeze and value in seen)
            seen.add(value)
        if not frozen:
            weight *= 3 * value / (3 * value + 1)
        value = (3 * value + 1) / 2
        minimum = min(minimum, value)
        frozen = frozen or (freeze and value in seen)
        seen.add(value)
    return value, weight, minimum


def source_average(size, degree, horizon, barrier, freeze):
    denominator = 3**degree
    total = Fraction(0)
    for numerator in range(1, size * denominator + 1):
        source = Fraction(numerator, denominator)
        _, survival, _ = trace(source, horizon, freeze)
        _, _, minimum = trace(source, horizon + 2)
        if minimum >= barrier:
            total += survival
    return total / (size * denominator)


def word_rung(size, degree, horizon, barrier, freeze):
    # Before the next odd departure the formal numerator cannot exceed
    # max(original numerator, initial odd denominator), even if unreduced.
    max_even_run = (size * 3**degree).bit_length() - 1
    total = Fraction(0)
    used_words = 0
    for runs in product(range(max_even_run + 1), repeat=degree):
        slope = Fraction(1)
        intercept = Fraction(0)
        clock = 0
        source_floor = barrier
        for run in runs:
            # Positive even states decrease to the odd input.
            source_floor = max(source_floor, (2**run * barrier - intercept) / slope)
            clock += run + 1
            multiplier = Fraction(3, 2 ** (run + 1))
            slope *= multiplier
            intercept = multiplier * intercept + Fraction(1, 2)
        source_floor = max(source_floor, (barrier - intercept) / slope)
        endpoint_floor = slope * source_floor + intercept
        width = size * slope
        endpoints = range(int(intercept) + 1, int(intercept + width) + 1)
        if endpoints:
            used_words += 1
        for endpoint in endpoints:
            source = (endpoint - intercept) / slope
            _, _, prefix_minimum = trace(source, degree)
            if (endpoint >= endpoint_floor) != (prefix_minimum >= barrier):
                raise ArithmeticError('affine endpoint floor disagreed with path')
            _, _, minimum = trace(source, horizon + 2)
            if minimum < barrier:
                continue
            ordinary_depth = 0
            native_inverse = Fraction(endpoint)
            for run in reversed(runs):
                native_inverse = 2**run * (2 * native_inverse - 1) / 3
                if native_inverse.denominator != 1:
                    break
                ordinary_depth += 1
            numerator = int(source * 3**degree)
            ternary_depth = 0
            while ternary_depth < degree and numerator % 3 == 0:
                ternary_depth += 1
                numerator //= 3
            if ordinary_depth != ternary_depth:
                raise ArithmeticError('inverse integrality depth mismatch')
            prefix_survival = (endpoint - intercept) / endpoint
            if freeze:
                _, marked_survival, _ = trace(source, horizon, True)
                toll_bound = 1 + 1 / (3 * max(Fraction(1), barrier))
                if marked_survival > prefix_survival * toll_bound**ordinary_depth:
                    raise ArithmeticError('repeat correction exceeded depth bound')
                remaining = marked_survival / prefix_survival
            else:
                _, remaining, _ = trace(Fraction(endpoint), horizon - degree)
            trit = 3 * (endpoint % 3 == 2) - 1
            total += (
                trit * (endpoint - intercept) * remaining
                / (width * endpoint * 2**clock)
            )
    return total, used_words


def main():
    comparisons = 0
    occupied = 0
    for size, horizon in [(1, 3), (4, 4), (11, 3), (16, 3)]:
        for barrier in [Fraction(0), Fraction(1), Fraction(3, 2), Fraction(3)]:
            for freeze in [False, True]:
                previous = source_average(size, 0, horizon, barrier, freeze)
                for degree in range(1, horizon + 1):
                    current = source_average(size, degree, horizon, barrier, freeze)
                    rung, words = word_rung(size, degree, horizon, barrier, freeze)
                    if previous - current != rung:
                        raise ArithmeticError((size, horizon, degree, barrier, rung))
                    previous = current
                    comparisons += 1
                    occupied += words
    print(f'{comparisons} exact rational rung comparisons passed '
          f'across {occupied} occupied word instances')


if __name__ == '__main__':
    main()
