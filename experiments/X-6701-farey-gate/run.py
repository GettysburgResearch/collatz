#!/usr/bin/env python3
"""Exact certificate for the positive coefficient-stopping gate.

Experiment ID: X-6701
Issue: GettysburgResearch/collatz#75
Agent: gpt56-positive-01

All assertions use fractions.Fraction. Decimal arithmetic is used only to print
human-readable enclosures after the exact comparisons have succeeded.
"""

from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction
from typing import Iterable

Q = Fraction

N_STAR = 4 * 3**44 + 2
LOG_TERMS = 80

CF_PREFIX = [
    0,
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
    2,
]

L_EXPECTED = Q(6_586_818_670, 10_439_860_591)
U_EXPECTED = Q(65_470_613_321, 103_768_467_013)
M_EXPECTED = Q(72_057_431_991, 114_208_327_604)
F_EXPECTED = Q(78_644_250_661, 124_648_188_195)
R_EXPECTED = Q(137_528_045_312, 217_976_794_617)


def require(condition: bool, message: str) -> None:
    """Raise a useful error rather than relying on optimized-away assert."""

    if not condition:
        raise RuntimeError(f"certificate failure: {message}")


def floor_q(x: Q) -> int:
    return x.numerator // x.denominator


def log_integer_interval(x: int, terms: int = LOG_TERMS) -> tuple[Q, Q]:
    """Return an exact rational enclosure for log(x), x > 0.

    We use

        log(x) = 2 * sum_{k>=0} z^(2k+1)/(2k+1),
        z = (x-1)/(x+1).

    For 0 <= z < 1, the omitted positive tail after ``terms`` summands is
    bounded by

        2*z^(2*terms+1) / ((2*terms+1)*(1-z^2)).
    """

    if x <= 0:
        raise ValueError("x must be positive")
    if terms <= 0:
        raise ValueError("terms must be positive")

    z = Q(x - 1, x + 1)
    z2 = z * z
    z_power = z
    partial = Q(0)

    for k in range(terms):
        partial += 2 * z_power / (2 * k + 1)
        z_power *= z2

    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z2))
    return partial, partial + tail


def continued_fraction_certificate(
    lo: Q, hi: Q, coefficients: Iterable[int]
) -> list[Q]:
    """Certify a finite continued-fraction prefix from an exact interval."""

    convergents: list[Q] = []
    p_nm2, p_nm1 = 0, 1
    q_nm2, q_nm1 = 1, 0
    coeffs = list(coefficients)

    for index, expected in enumerate(coeffs):
        require(lo <= hi, f"continued-fraction interval inverted at {index}")
        require(
            floor_q(lo) == expected and floor_q(hi) == expected,
            f"continued-fraction coefficient {index} is not uniquely {expected}",
        )

        p_n = expected * p_nm1 + p_nm2
        q_n = expected * q_nm1 + q_nm2
        convergents.append(Q(p_n, q_n))
        p_nm2, p_nm1 = p_nm1, p_n
        q_nm2, q_nm1 = q_nm1, q_n

        if index + 1 < len(coeffs):
            lo_shift = lo - expected
            hi_shift = hi - expected
            require(lo_shift > 0, f"nonpositive CF tail at coefficient {index}")
            # Reciprocal reverses the interval.
            lo, hi = 1 / hi_shift, 1 / lo_shift

    return convergents


def determinant(left: Q, right: Q) -> int:
    """Return right_num*left_den - left_num*right_den."""

    return (
        right.numerator * left.denominator
        - left.numerator * right.denominator
    )


def decimal_text(x: Q, precision: int = 70) -> str:
    """Human-readable decimal rendering; never used for a proof comparison."""

    with localcontext() as ctx:
        ctx.prec = precision
        return str(Decimal(x.numerator) / Decimal(x.denominator))


def main() -> None:
    log2_lo, log2_hi = log_integer_interval(2)
    log3_lo, log3_hi = log_integer_interval(3)

    require(log2_lo < log2_hi, "log(2) enclosure is not strict")
    require(log3_lo < log3_hi, "log(3) enclosure is not strict")

    alpha_lo = log2_lo / log3_hi
    alpha_hi = log2_hi / log3_lo
    eps_lo = log2_lo / (3 * N_STAR * log3_hi * log3_hi)
    eps_hi = log2_hi / (3 * N_STAR * log3_lo * log3_lo)

    convergents = continued_fraction_certificate(alpha_lo, alpha_hi, CF_PREFIX)
    L = convergents[22]
    U = convergents[23]
    R = convergents[24]

    require(L == L_EXPECTED, "left convergent mismatch")
    require(U == U_EXPECTED, "upper convergent mismatch")
    require(R == R_EXPECTED, "next convergent mismatch")
    require(determinant(L, U) == 1, "L and U are not Farey neighbors")

    M = Q(L.numerator + U.numerator, L.denominator + U.denominator)
    F = Q(2 * L.numerator + U.numerator, 2 * L.denominator + U.denominator)

    require(M == M_EXPECTED, "first mediant mismatch")
    require(F == F_EXPECTED, "left adjacent mediant mismatch")
    require(
        R == Q(L.numerator + 2 * U.numerator, L.denominator + 2 * U.denominator),
        "right adjacent mediant mismatch",
    )
    require(determinant(F, M) == 1, "F and M are not Farey neighbors")
    require(determinant(M, U) == 1, "M and U are not Farey neighbors")

    # Rigorous ordering of the microscopic admissible window.
    window_lower_lo = alpha_lo - eps_hi
    window_lower_hi = alpha_hi - eps_lo
    require(L < window_lower_lo, "L is not below the whole window")
    require(F < window_lower_lo, "F is not below the whole window")
    require(window_lower_hi < M, "M is not above the whole lower endpoint")
    require(M < alpha_lo, "M is not rigorously below alpha")
    require(alpha_hi < U, "U is not rigorously above alpha")

    j = M.denominator
    q = M.numerator

    # This gives ceil((j-1)*alpha) = q for the mechanical extremizer.
    require((j - 1) * alpha_lo > q - 1, "lower mechanical endpoint failed")
    require((j - 1) * alpha_hi < q, "upper mechanical endpoint failed")

    # lambda = j*log(2)-q*log(3) > 0 and C = exp(-lambda).
    lambda_lo = j * log2_lo - q * log3_hi
    lambda_hi = j * log2_hi - q * log3_lo
    require(lambda_lo > 0, "candidate coefficient is not rigorously subcritical")
    require(lambda_hi < 1, "lambda is outside the elementary exponential bound")

    # For lambda >= 0, 1-exp(-lambda) >= lambda-lambda^2/2.
    # The following is deliberately conservative: use the lower linear term
    # and the upper quadratic term.
    coefficient_drop_lo = lambda_lo - lambda_hi * lambda_hi / 2
    require(coefficient_drop_lo > 0, "coefficient-drop lower bound is nonpositive")

    # Denjoy--Koksma gives E < j/(6 log(3)) + 4/3.  A lower
    # enclosure for log(3) gives an upper enclosure for this expression.
    remainder_upper = Q(j, 6) / log3_lo + Q(4, 3)
    floor_drop_lower = N_STAR * coefficient_drop_lo
    margin_lower = floor_drop_lower - remainder_upper
    require(margin_lower > 0, "the first Farey candidate was not excluded")

    first_gate = M.denominator
    right_gate = M.denominator + U.denominator
    left_gate = F.denominator + M.denominator
    repeated_m_gate = 2 * M.denominator
    sharpened_gate = min(right_gate, left_gate, repeated_m_gate)

    require(first_gate == 114_208_327_604, "first gate changed")
    require(right_gate == 217_976_794_617, "right Farey gate changed")
    require(left_gate == 238_856_515_799, "left Farey gate changed")
    require(repeated_m_gate == 228_416_655_208, "repeated-mediant gate changed")
    require(sharpened_gate == 217_976_794_617, "sharpened gate changed")

    print("X-6701 EXACT CERTIFICATE: PASS")
    print(f"log series terms             : {LOG_TERMS}")
    print(f"N_*                          : {N_STAR}")
    print(f"N_*/2^71                     : {decimal_text(Q(N_STAR, 2**71), 40)}")
    print(f"alpha lower                  : {decimal_text(alpha_lo)}")
    print(f"alpha upper                  : {decimal_text(alpha_hi)}")
    print(f"epsilon lower                : {decimal_text(eps_lo)}")
    print(f"epsilon upper                : {decimal_text(eps_hi)}")
    print(f"continued-fraction prefix    : {CF_PREFIX}")
    print(f"L                            : {L}")
    print(f"U                            : {U}")
    print(f"M                            : {M}")
    print(f"F                            : {F}")
    print(f"next convergent              : {R}")
    print(f"alpha-M lower                : {decimal_text(alpha_lo - M)}")
    print(f"alpha-M upper                : {decimal_text(alpha_hi - M)}")
    print(f"lambda lower                 : {decimal_text(lambda_lo)}")
    print(f"lambda upper                 : {decimal_text(lambda_hi)}")
    print(f"remainder upper              : {decimal_text(remainder_upper)}")
    print(f"N_* coefficient-drop lower  : {decimal_text(floor_drop_lower)}")
    print(f"exclusion margin lower       : {decimal_text(margin_lower)}")
    print(f"first denominator gate       : {first_gate}")
    print(f"left-cell next denominator   : {left_gate}")
    print(f"same-rational next multiple  : {repeated_m_gate}")
    print(f"right-cell next denominator  : {right_gate}")
    print(f"SHARPENED GATE               : {sharpened_gate}")


if __name__ == "__main__":
    main()
