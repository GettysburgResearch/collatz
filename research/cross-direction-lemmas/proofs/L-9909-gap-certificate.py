"""Exact certificate for the finite continued-fraction step in L-9909.

This script uses only integer and rational arithmetic.  The logarithm
enclosures come from

    log(x) = 2 * sum_{j >= 0} z^(2j+1)/(2j+1),  z = (x-1)/(x+1),

with the omitted positive tail bounded by a geometric series.
"""

from fractions import Fraction


CF_PREFIX = [
    1,
    1,
    1,
    2,
    2,
    3,
    1,
    5,
    2,
    23,
    2,
    2,
    1,
    1,
    55,
    1,
    4,
    3,
    1,
    1,
    15,
    1,
    9,
]

CUTOFF = 25_000_000_001


def log_bounds(x: int, terms: int = 96) -> tuple[Fraction, Fraction]:
    """Return strict rational lower/upper bounds for log(x), x > 1."""

    z = Fraction(x - 1, x + 1)
    z_squared = z * z
    z_power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += z_power / (2 * j + 1)
        z_power *= z_squared

    lower = 2 * partial
    # In the tail, 1/(2j+1) <= 1/(2*terms+1).
    tail_upper = 2 * z_power / ((2 * terms + 1) * (1 - z_squared))
    return lower, lower + tail_upper


def certify_cf_prefix(
    lower: Fraction, upper: Fraction, expected: list[int]
) -> None:
    """Certify a common continued-fraction prefix for an open interval."""

    assert 0 < lower < upper
    for index, wanted in enumerate(expected):
        lower_floor = lower.numerator // lower.denominator
        upper_floor = upper.numerator // upper.denominator
        assert lower_floor == upper_floor == wanted
        if index + 1 == len(expected):
            return
        lower -= wanted
        upper -= wanted
        assert lower > 0
        lower, upper = 1 / upper, 1 / lower


def convergents(coefficients: list[int]) -> list[tuple[int, int]]:
    """Return (numerator, denominator) pairs."""

    p_before, p_last = 0, 1
    q_before, q_last = 1, 0
    answer = []
    for coefficient in coefficients:
        p = coefficient * p_last + p_before
        q = coefficient * q_last + q_before
        answer.append((p, q))
        p_before, p_last = p_last, p
        q_before, q_last = q_last, q
    return answer


def exponential_partial(x: Fraction, degree: int) -> Fraction:
    """Return sum_{j=0}^degree x^j/j! exactly."""

    term = Fraction(1)
    total = term
    for j in range(1, degree + 1):
        term *= x / j
        total += term
    return total


def main() -> None:
    log2_lower, log2_upper = log_bounds(2)
    log3_lower, log3_upper = log_bounds(3)
    alpha_lower = log3_lower / log2_upper
    alpha_upper = log3_upper / log2_lower
    certify_cf_prefix(alpha_lower, alpha_upper, CF_PREFIX)

    conv = convergents(CF_PREFIX)
    expected_upper = [
        (2, 1),
        (8, 5),
        (65, 41),
        (485, 306),
        (24_727, 15_601),
        (125_743, 79_335),
        (301_994, 190_537),
        (17_087_915, 10_781_274),
        (272_500_658, 171_928_773),
        (630_138_897, 397_573_379),
        (10_439_860_591, 6_586_818_670),
    ]
    upper = [conv[index] for index in range(1, len(conv), 2)]
    assert upper == expected_upper

    # q_22 already exceeds the analytic cutoff, so the list above contains
    # every upper convergent whose denominator is below the cutoff.
    assert conv[22] == (103_768_467_013, 65_470_613_321)
    assert conv[22][1] > CUTOFF

    # For every listed upper convergent from 65/41 onward, q_n+q_(n+1)
    # is below 2^40, while q_n >= 41.  Hence the standard convergent
    # lower bound gives p_n-q_n*alpha > 2^(1-q_n).
    next_denominator_sums = [
        conv[index][1] + conv[index + 1][1]
        for index in range(5, 22, 2)
    ]
    assert max(next_denominator_sums) == 72_057_431_991
    assert max(next_denominator_sums) < 2**40

    # Exact exceptional checks: k=2, k=3, and the primitive 8/5
    # convergent.  The last identity is 1-2^(-delta_5)=13/256>2^-5.
    assert 2**3 < 3**2 < 2**4
    assert 2**4 - 3**2 == 7 > 2 ** (4 - 2) - 1
    assert 2**4 < 3**3 < 2**5
    assert 2**5 - 3**3 == 5 > 2 ** (5 - 3) - 1
    assert Fraction(2**8 - 3**5, 2**8) == Fraction(13, 256) > Fraction(1, 32)

    # Rational checks behind the coarse Matveev cutoff used in the proof.
    matveev_coefficient_upper = (
        Fraction(7, 5) * 30**5 * 24 * Fraction(11, 10)
    )
    assert 16**2 * 2 < 24**2  # 2^4.5 = 16*sqrt(2) < 24.
    assert exponential_partial(Fraction(11, 10), 5) > 3  # log(3) < 11/10.
    assert matveev_coefficient_upper == 898_128_000 < 900_000_000
    assert exponential_partial(Fraction(1), 4) > Fraction(27, 10)
    assert Fraction(27, 10) ** 26 > 2 * CUTOFF
    assert CUTOFF - 1 > 900_000_000 * 27

    print("L-9909 gap certificate: PASS")
    print("certified continued fraction prefix:", CF_PREFIX)
    print("upper convergents below cutoff:", expected_upper)
    print("first following denominator:", conv[22][1])
    print("maximum q_n+q_(n+1):", max(next_denominator_sums))


if __name__ == "__main__":
    main()
