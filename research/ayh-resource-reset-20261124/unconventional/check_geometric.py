"""Exact finite replay for the signed logarithmic terminal and the geometric slices."""

from fractions import Fraction
from math import gcd
from pathlib import Path
import re


PRECISION = 334711


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def positive_trace(x, length):
    count = 0
    for _ in range(length):
        odd = x % 2
        count += odd
        x = (3 * x + 1) // 2 if odd else x // 2
    return x, count


def signed_trace(exponent, length):
    x = Fraction(1, 3 ** -exponent) - 1
    count = 0
    for _ in range(length):
        odd = x.numerator % 2
        count += odd
        x = (3 * x + 1) / 2 if odd else x / 2
    return x, count


def rational_sum(first, stop):
    """Reduced numerator/denominator of sum(4**(i-first)/i)."""
    if stop == first + 1:
        return 1, first
    middle = (first + stop) // 2
    p_left, q_left = rational_sum(first, middle)
    p_right, q_right = rational_sum(middle, stop)
    common = gcd(q_left, q_right)
    left = q_left // common
    right = q_right // common
    num = p_left * right + ((p_right * left) << (2 * (middle - first)))
    den = q_left * right
    common = gcd(num, den)
    return num // common, den // common


def negative_unit(h):
    stop = (h + 80) // 2 + 2
    p, q = rational_sum(1, stop)
    mod = 1 << h
    require(q % 2 == 1, "negative logarithm sum has an unexpected even denominator")
    return 81 * p * pow(3**24 * q, -1, mod) % mod


def check_small_precision():
    h = 2957
    mod = 1 << h
    s = h - 2
    a = 3**162
    b = (pow(a, 1 << s, 1 << (s + 3 + h)) - 1) >> (s + 3)
    require((3**24 * negative_unit(h) + b) % mod == 0, "series disagrees with direct power")


def first_meeting(v, horizon):
    """Use twelve actual shortcut steps per block; refine the first matching block."""
    width = 12
    mask = (1 << width) - 1
    table = [positive_trace(i, width) for i in range(1 << width)]
    slopes = [3**t for t in range(width + 1)]
    x, y = 1 + 3**37 * v, 2 + v
    high_odds = low_odds = 0
    for clock in range(0, horizon, width):
        old = x, y, high_odds, low_odds
        if horizon - clock >= width:
            bx, px = table[x & mask]
            by, py = table[y & mask]
            x = slopes[px] * (x >> width) + bx
            y = slopes[py] * (y >> width) + by
            high_odds += px
            low_odds += py
            if x != y or 37 + high_odds != low_odds:
                continue
        x, y, high_odds, low_odds = old
        for extra in range(1, min(width, horizon - clock) + 1):
            x, px = positive_trace(x, 1)
            y, py = positive_trace(y, 1)
            high_odds += px
            low_odds += py
            if x == y and low_odds == 37 + high_odds:
                return clock + extra, high_odds, low_odds
    raise ArithmeticError("the negative logarithmic seed did not meet by the claimed clock")


def check_kernel_certificate(v):
    """Compare every declared physical block with its independently computed residue profile."""
    src = Path(__file__).with_name("NegativeProfile.lean").read_text()
    unit = re.search(r"^def negativeUnit : Nat := (0x[0-9a-f]+)$", src, re.MULTILINE)
    require(unit and int(unit.group(1), 16) == v, "kernel representative differs from the binary logarithm")
    pattern = re.compile(
        r"private def (upper|lower)([0-9]+) : Checked :=\s*"
        r"⟨⟨([0-9]+),(0x[0-9a-f]+),(0x[0-9a-f]+),([0-9]+)⟩,by decide \+kernel⟩"
    )
    records = {"upper": [], "lower": []}
    for name, index, width, residue, image, grade in pattern.findall(src):
        records[name].append((int(index), int(width), int(residue, 16), int(image, 16), int(grade)))
    final = []
    for name, x in (("upper", 1 + 3**37*v), ("lower", 2+v)):
        clock = count = 0
        by_name = re.search(rf"private def {name} : List Checked :=\s*\[([^\]]+)\]", src)
        require(by_name is not None, "missing kernel block order")
        order = [int(i) for i in re.findall(rf"{name}([0-9]+)", by_name.group(1))]
        require(order == list(range(len(records[name]))), "wrong kernel block order or length")
        for expected_index, (index, width, residue, image, grade) in enumerate(records[name]):
            require(index == expected_index and 0 < width <= 4096, "wrong kernel block")
            require(x % (1 << width) == residue, "kernel residue disagrees with the actual phase")
            require(positive_trace(residue, width) == (image, grade), "kernel local profile disagrees")
            x = 3**grade * (x >> width) + image
            clock += width
            count += grade
        require(clock == PRECISION, "wrong kernel clock sum")
        final.append((x, count))
    require(final[0][0] == final[1][0] and (final[0][1], final[1][1]) == (167282, 167319),
            "kernel blocks disagree about the endpoint or odd counts")
    return len(records["upper"]) + len(records["lower"])


if __name__ == "__main__":
    require(signed_trace(-29, 62) == (1, 34), "negative zero-anchor trace")
    require(signed_trace(-151, 327) == (1, 151), "minus-one upper anchor trace")
    require(signed_trace(-191, 389) == (1, 191), "minus-one lower anchor trace")
    check_small_precision()
    v = negative_unit(PRECISION)
    blocks = check_kernel_certificate(v)
    clock, high, low = first_meeting(v, PRECISION)
    require((clock, high, low) == (334711, 167282, 167319), "wrong first compensated merger")
    print(f"Negative terminal first merges at {clock} with upper/lower odd counts {high}/{low}.")
    print(f"Verified all {blocks} kernel blocks, three signed anchor profiles and the independent 2957-bit unit check.")
