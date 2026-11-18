"""Finite replay for the unsafe-return weight theorem, using positive physical sources."""
from fractions import Fraction
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
source = runpy.run_path(str(ROOT / "experiments/X-ASTRA3-005-spectrum-switch/run.py"))
rank, module, jump = (source[name] for name in ("rank", "module", "jump"))


def require(value, context):
    if not value:
        raise ValueError(context)


def valuation(value, p):
    numerator = abs(value.numerator)
    require(numerator > 0 and value.denominator % p, "invalid local valuation")
    count = 0
    while numerator % p == 0:
        count += 1
        numerator //= p
    return count


def coefficients(value):
    h = valuation(2 * value + 1, 3)
    modes = [0, 1, 2] + ([h] if h >= 3 else [])
    leading = []
    for a in modes:
        slope = 3**a - 2**(a + 1)
        offset = 3**a - 2**a
        exponent = valuation(slope * value + offset, 3)
        require(exponent < 7, "insufficient ternary precision")
        leading.append(Fraction(slope**2, 3**exponent))
    return h, leading


def check_periods(periods):
    modulus = 2**(11 * (periods + 2))
    power = 3**(11 * periods + 7)
    x = power * (modulus + (-17 * pow(power, -1, modulus)) % modulus)
    start = x
    for _ in range(periods):
        y, z = (81 * x + 65) // 32, (2187 * x + 2363) // 512
        successor = z // 4
        require(module(x) == (y, 4, 1, 5), "wrong first maximal module")
        require(module(y) == (z, 3, 1, 4), "wrong second maximal module")
        require(module(z) == (successor, 0, 2, 2), "wrong third maximal module")
        require(jump(x) == y and jump(y) == successor, "wrong unsafe guards")
        require(rank(y) >= start**2 // 10, "first induced rank too small")
        require(rank(successor) >= start**2 // 10, "second induced rank too small")
        x = successor


def main():
    expected = [
        (-17, 1, [1, Fraction(1, 9), Fraction(1, 3)]),
        (Fraction(65, 32), 4, [1, Fraction(1, 3), Fraction(1, 9), Fraction(2401, 81)]),
        (-41, 4, [1, Fraction(1, 3), Fraction(1, 9), Fraction(2401, 243)]),
        (-68, 3, [1, Fraction(1, 3), Fraction(1, 9), Fraction(121, 729)]),
    ]
    for representative, h, row in expected:
        require(coefficients(Fraction(representative)) == (h, row), "wrong ternary row")

    for periods in (1, 2, 5, 12, 32):
        check_periods(periods)

    # Eleven bits suffice for one sample return: the second mode ends at
    # an even state, which certifies its maximality without a second period.
    modulus = 2**11
    target = -17 * pow(7, -1, modulus) % modulus
    least = next(t for t in range(2**8) if pow(9, t, modulus) == target)
    for j in (1, 2, 3):
        x = 7 * 3**(2 * (least + j * 2**8))
        y = (81 * x + 65) // 32
        require(rank(x) == 7 * x and jump(x) == y, "geometric source failed")
        require(rank(y) >= x**2 // 10, "geometric source inflation failed")

    print("4 exact ternary rows; 104 induced returns on 5 CRT sources; "
          "3 geometric sources at the first return.")


if __name__ == "__main__":
    main()
