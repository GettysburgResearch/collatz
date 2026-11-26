"""Replay the finite numerical data for the changing-center and perfect-power theorems."""

from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import re


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def trace(start, clock):
    x = start
    odd_count = 0
    for _ in range(clock):
        odd_count += x % 2
        x = (3 * x + 1) // 2 if x % 2 else x // 2
    return x, odd_count


def exact_finite_data():
    precision = 2957
    modulus = 1 << precision
    last = precision - 2
    a_power = 3**162
    unit = (pow(a_power, 1 << last, 1 << (precision + last + 3)) - 1) >> (last + 3)
    lifted_unit = (a_power - 1) // 8 % modulus
    for i in range(last):
        lifted_unit = (lifted_unit + (lifted_unit**2 << (i + 2))) % modulus
    require(unit == lifted_unit, "direct modular power and derivative recurrence disagree")
    terminal_unit = unit * pow(3, -58, modulus) % modulus
    anchor = pow(3, -52, 1 << 119)
    intercept = (3**52 * anchor - 1) >> 119
    expected = {"seedB": unit, "seedU": terminal_unit, "a": anchor, "a0": intercept}
    source = Path(__file__).with_name("LogTowerData.lean").read_text()
    for name, value in expected.items():
        match = re.search(rf"^def {name} : Nat := ([0-9]+)$", source, re.MULTILINE)
        require(match and int(match.group(1)) == value, f"Lean datum {name} disagrees")
    require(trace(anchor - 1, 119) == (1 + intercept, 52), "lower signed-anchor lift")
    require(trace(3**63 * anchor - 1, 119) == (1 + 3**71 * intercept, 60), "upper signed-anchor lift")
    y, p = trace(1 + terminal_unit, precision)
    z, q = trace(1 + 3**71 * terminal_unit, precision)
    require(y == z and (p, q) == (1513, 1442), "terminal grade compensation")
    require(trace(3**173 - 1, 1143) == (1, 548), "odd-base upper anchor")
    require(trace(3**131 - 1, 1143) == (1, 590), "odd-base lower anchor")
    require(trace(3233, 107)[0] == 1, "zero-base parent")
    return p, q


def inverse_data():
    x = 2047
    for gap in (2, 1, 2, 2, 1):
        numerator = (x << gap) - 1
        require(numerator % 3 == 0, "fixed odd gap is illegal")
        x = numerator // 3
    require(x == 2155 and 243 * x == 256 * 2047 - 367, "five-step preparation")
    for residue, gap in zip((1, 2, 4, 5, 7, 8), (2, 1, 2, 3, 4, 1)):
        numerator = (residue << gap) - 1
        require(numerator % 3 == 0 and numerator // 3 % 3 != 0, "ternary-unit row")
    for length in range(9):
        identities = set()
        for word in product((0, 1), repeat=length):
            grade = offset = 0
            for odd in word:
                offset = 2 * offset + odd * 3**grade
                grade += odd
            require((grade, offset) not in identities, "nonunique exact numerator")
            identities.add((grade, offset))
            modulus = 3**grade
            y = offset * pow(2**length, -1, modulus) % modulus or modulus
            x = y
            for odd in word:
                require(not odd or x % 3 == 2, "final congruence did not certify prefix")
                x = (2 * x - 1) // 3 if odd else 2 * x
            require(x > 0 and 2**length * y == modulus * x + offset, "word endpoint")
    return 2**9 - 1


def coverage_constants():
    require(Fraction(70711, 50000)**2 > 2, "upper sqrt(2)")
    require(Fraction(4899, 2000)**2 > 6, "upper sqrt(6)")
    require(Fraction(433, 250)**2 < 3, "lower sqrt(3)")
    rho_upper = (Fraction(70711, 50000) + Fraction(4899, 2000)) / 4
    require(rho_upper < Fraction(483, 500), "fractional-moment contraction")
    require(17 * Fraction(433, 250) * (1 - Fraction(483, 500)) > 1, "offset moment bound")
    require(Fraction(5, 4)**5 * Fraction(2, 3)**3 < Fraction(99, 100)**5, "binomial tilt")
    require(3**3 < (2 * Fraction(99, 100))**5, "low-grade shell contraction")
    cutoff = 81 * 2**33
    require(Fraction(486, cutoff**2) == Fraction(1, 27 * 2**65), "parent density constant")
    output = []
    for cost, extra_class in ((Fraction(256, 243), 1), (Fraction(4096, 2187), 27)):
        n = 1
        while cutoff * cost * Fraction(16, 27)**n > 1:
            n += 1
        bound = Fraction(9 * comb(4 * n, 3 * n), 26 * 676 * 3**(3 * n) * extra_class)
        output.append((n, bound))
    return output


if __name__ == "__main__":
    p, q = exact_finite_data()
    print(f"Dyadic terminal at clock 2957 has matching endpoints and grades {p}, {q}.")
    print(f"Verified exact legality and numerator identities for {inverse_data()} finite words.")
    for n, bound in coverage_constants():
        print(f"Positive class bound at n={n} is {float(bound):.10e}.")
