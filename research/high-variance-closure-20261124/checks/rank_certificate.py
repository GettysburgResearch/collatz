"""Exact independent finite checks for the restricted negative-center valley envelope."""

from fractions import Fraction
from math import gcd


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(x):
    """Shortcut on a Fraction in Z_2."""
    return (3 * x + 1) / 2 if x.numerator % 2 else x / 2


def tangent_cut(source, threshold):
    x = Fraction(source)
    scale = Fraction(1)
    for clock in range(200):
        bound = scale * (x + 1) - source
        if 1 + source / bound < threshold:
            return clock, x, scale, bound
        scale *= Fraction(2, 3) if x.numerator % 2 else 2
        x = shortcut(x)
    raise ValueError("No cutoff in finite check")


def candidates(source, threshold, cutoff):
    """Exhaust every center whose score reaches threshold before cutoff."""
    require(threshold > 1, "threshold must exceed one")
    for clock in range(cutoff):
        power = 2**clock
        q = 1
        while threshold * q < power:
            # If h <= power / threshold < power, this interval for d
            # has length below one; its only possible integer is this one.
            d = source * q // power + 1
            h = power * d - source * q
            if d % 2 and q < h and threshold * h <= power and gcd(h, q) == 1:
                yield h, q, Fraction(power, h)
            q *= 3


def membership(h, q):
    """A concrete finite proof for this one candidate, never a general oracle."""
    x = Fraction(-h, q)
    seen = set()
    for _ in range(2000):
        if x == -5:
            return True
        if x >= -1 or x in seen:
            return False
        seen.add(x)
        x = shortcut(x)
    raise ValueError("Negative center not classified within certificate budget")


def exact_value(source, threshold):
    cutoff, _, _, _ = tangent_cut(source, threshold)
    eligible = list(candidates(source, threshold, cutoff))
    hits = [(score, h, q) for h, q, score in eligible if membership(h, q)]
    if not hits:
        raise ValueError("No lower witness at threshold")
    return max(hits), cutoff, len(eligible), len(hits)


def main():
    cutoff, x, scale, bound = tangent_cut(31, Fraction(18))
    require((cutoff, x, scale, bound) == (
        30, 319, Fraction(2**30, 3**21), Fraction(19326434387, 10460353203)
    ), "source tail cutoff changed")
    require(not list(candidates(31, Fraction(18), cutoff)), "finite box is not empty")
    require(3**5 * 1 - 1 == 2 * 121 and 31 + 1 == 2**5, "ordinary valley mismatch")
    require(Fraction(128, 7) > 18, "target lower bound failed")
    for source, threshold, expected in (
        (1, Fraction(8, 7), Fraction(8, 7)),
        (31, Fraction(14), Fraction(4294967296, 291622243)),
        (121, Fraction(18), Fraction(67108864, 2804503)),
    ):
        (score, h, q), cutoff, possible, hits = exact_value(source, threshold)
        require(score == expected, "unexpected exact envelope value")
        print(f"n={source} E={score} witness=-{h}/{q} cutoff={cutoff}"
              f" admissible={possible} tree_hits={hits}")
    print("strict restricted-envelope increase: 31 -> 121")


if __name__ == "__main__":
    main()
