#!/usr/bin/env python3
"""Replay the dyadic division coefficients and actual folded rational cycle windows."""
from fractions import Fraction
from itertools import product
from math import gcd
import json


def coefficients(clock):
    prefix = [0]
    for letter in clock:
        prefix.append(prefix[-1] + letter)
    size = 2 ** prefix[-1]
    weights = [
        Fraction(pow(3 ** (j + 1), -1, size >> b), size >> b)
        for j, b in enumerate(prefix[:-1])
    ]
    incoming = [Fraction(1, size)]
    incoming.extend((2 ** b) * u for b, u in zip(clock, weights))
    digits = [v - 3 * u for v, u in zip(incoming, weights)] + [incoming[-1]]
    assert all(e.denominator == 1 and -2 <= e <= 3 for e in digits)
    homogeneous = sum(e * Fraction(3 ** j, 2 ** b)
                      for j, (e, b) in enumerate(zip(digits, prefix)))
    assert homogeneous == Fraction(1, size)
    return size, weights, [int(e) for e in digits]


def lifted(values, r):
    wrap, phase = divmod(r, len(values))
    return values[phase] << wrap


def check_cycle(p, d, minimum):
    numerators, marks, gaps = [], [], []
    x = minimum
    for _ in range(p):
        band = (x // minimum).bit_length() - 1
        assert 0 <= band <= 2
        mark = 1 << (2 - band)
        numerators.append(mark * x)
        marks.append(mark)
        raw = 3 * x + d
        gap = (raw & -raw).bit_length() - 1
        assert gap in (1, 2)
        gaps.append(gap)
        x = raw >> gap
    assert x == minimum and len(set(numerators)) == p
    h = sum(gaps)
    order = sorted(range(p), key=numerators.__getitem__)
    assert all(order[j * h % p] == j for j in range(p))
    nums = [numerators[j] for j in order]
    marks = [marks[j] for j in order]
    n = 1
    while (d << (n * h // p)) < 8 * minimum:
        n += 1
    prefix = [j * h // p for j in range(n + 1)]
    clock = [b - a for a, b in zip(prefix, prefix[1:])]
    offsets = [(j * h) % p for j in range(n + 1)]
    size, weights, digits = coefficients(clock)
    images = []
    for r in range(p):
        new_num = sum(e * lifted(nums, r + k) for e, k in zip(digits, offsets))
        rhs = Fraction(nums[r], size) + d * sum(
            u * lifted(marks, r + k) for u, k in zip(weights, offsets)
        )
        assert new_num == rhs and gcd(d, new_num) == 1
        assert 0 < new_num <= (1 + 8 * n) * d
        images.append(new_num)
    defects = [lifted(images, r + h) - 3 * images[r] for r in range(p)]
    for r, value in enumerate(defects):
        assert value == d * sum(e * lifted(marks, r + k)
                                for e, k in zip(digits, offsets))
    return {
        "period": p, "denominator": d, "minimum_numerator": minimum,
        "window": n, "coefficients": digits,
        "different_images": len(set(images)),
        "minimum_image": str(Fraction(min(images), d)),
        "maximum_image": str(Fraction(max(images), d)),
        "minimum_signed_defect": min(defects) // d,
        "maximum_signed_defect": max(defects) // d,
    }


def main():
    checked = 0
    for n in range(1, 13):
        for clock in product((1, 2), repeat=n):
            coefficients(clock)
            checked += 1
    controls = [(5, 13, 283), (8, 1631, 10865),
                (41, 44835377399, 29340952507853)]
    print(json.dumps({"binary_calendars_through_length_12": checked,
                      "ordered_rational_controls": [check_cycle(*row) for row in controls]},
                     indent=2))


if __name__ == "__main__":
    main()
