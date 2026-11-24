"""An exact rational enclosure for the Collatz first-crossing gate at 2^71."""

from fractions import Fraction


def log_bounds(integer, terms=90):
    z = Fraction(integer - 1, integer + 1)
    partial = 2 * sum(z ** (2 * k + 1) / (2 * k + 1) for k in range(terms))
    tail_bound = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return partial, partial + tail_bound


def main():
    log2_lo, log2_hi = log_bounds(2)
    log3_lo, log3_hi = log_bounds(3)
    alpha_lo = log3_lo / log2_hi
    alpha_hi = log3_hi / log2_lo
    lower = Fraction(103768467013, 65470613321)
    upper = Fraction(10439860591, 6586818670)
    epsilon = 1 / (3 * (2 ** 71) * log2_lo)
    if not lower < alpha_lo < alpha_hi < alpha_hi + epsilon < upper:
        raise ArithmeticError('rational interval does not fit between endpoints')
    determinant = upper.numerator * lower.denominator - lower.numerator * upper.denominator
    if determinant != 1:
        raise ArithmeticError('endpoints are not Farey neighbors')
    print(f'Farey endpoints {lower} and {upper}; determinant {determinant}')
    print(f'minimum numerator {lower.numerator + upper.numerator}')
    print(f'minimum denominator {lower.denominator + upper.denominator}')
    print('90-term rational log enclosures passed; minimum source 2^71')


if __name__ == '__main__':
    main()
