"""Finite exact controls for translated period strips and cyclic charges."""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_strip(points, numerator, denominator, radius, counts):
    if len(points) < 2:
        return
    width = points[-1][0] - points[0][0]
    lines = Counter()
    for (x, y), (z, w) in combinations(points, 2):
        q, a = z - x, w - y
        divisor = gcd(q, a)
        q, a = q // divisor, a // divisor
        lines[q, a, q * y - a * x] += 1
    (q, a, _), _ = lines.most_common(1)[0]
    levels = Counter(q * y - a * x for x, y in points)
    largest = max(levels.values())
    level_span = max(levels) - min(levels)
    direction_error = abs(numerator * q - denominator * a)
    require((largest - 1) * q <= width, "horizontal primitive spacing")
    require((largest - 1) * direction_error <= 2 * radius, "signed primitive spacing")
    require(denominator * level_span <= 2 * radius * q + width * direction_error,
            "determinant range")
    require(denominator * level_span * (largest - 1) <= 4 * width * radius,
            "scaled determinant span")
    if len(levels) > 1:
        require(denominator * (len(points) - 1) <= 12 * width * radius,
                "noncollinear packing")
        counts["noncollinear"] += 1
    else:
        counts["affine_line"] += 1
        errors = sorted(abs(numerator * x - denominator * y) for x, y in points)
        for i, error in enumerate(errors):
            require(2 * error >= i * direction_error, "two-sided error packing")
        if (q, a) != (1, 0) and min(errors) * 2 < (len(points) - 1) * direction_error:
            counts["line_where_one_sided_minimum_bound_fails"] += 1


def translated_strips():
    counts = Counter()
    for a, b in [(8, 13), (12, 19), (41, 65), (53, 84), (67, 106)]:
        for start in [0, 19, 193, 1039, 10**12 + 315]:
            for width in [11, 27, 64, 113]:
                for radius in [1, 3, 7, 11, 17]:
                    points = []
                    for n in range(start, start + width):
                        u = (2 * a * n + b) // (2 * b)
                        if abs(a * n - b * u) <= radius:
                            points.append((n, u))
                    for picked in [points, points[::2], points[1::3],
                                   [t for t in points if t[0] % 3 != 1]]:
                        check_strip(picked, a, b, radius, counts)
    require(counts["affine_line"] > 0 and counts["noncollinear"] > 0,
            "both strip geometries must occur")
    require(counts["line_where_one_sided_minimum_bound_fails"] > 0,
            "the mixed-sign line control must be exercised")
    return counts


def cycle_word(n, mask):
    word = tuple((mask >> j) & 1 for j in range(n))
    if word != min(word[j:] + word[:j] for j in range(n)):
        return None
    if any(word == word[j:] + word[:j] for j in range(1, n)):
        return None
    k = sum(word)
    if k == 0:
        return None
    carry = 0
    for j, symbol in enumerate(word):
        if symbol:
            carry = 3 * carry + (1 << j)
    root = Fraction(carry, (1 << n) - 3**k)
    x = root
    phases = []
    for symbol in word:
        require((x.numerator & 1) == symbol, "native odd denominator parity")
        phases.append(abs(x))
        x = (3*x+1)/2 if symbol else x/2
    require(x == root and len(set(phases)) == n, "primitive physical trace")
    return root, phases


def rational_cycles():
    counts = Counter()
    for n in range(1, 12):
        for mask in range(1, 1 << n):
            cycle = cycle_word(n, mask)
            if cycle is None:
                continue
            root, phases = cycle
            counts["positive_cycles" if root > 0 else "negative_cycles"] += 1
            for B in [2, 9]:
                # The future-minimum and Gronwall identities work for every
                # positive potential, so this control uses two rational ones.
                for power in [1, 2]:
                    f = [1/y**power for y in phases]
                    increments = [v + B*(v-f[(i+1) % n]) for i, v in enumerate(f)]
                    partial = [Fraction(0)]
                    for increment in 2*increments:
                        partial.append(partial[-1] + increment)
                    minima = [min(partial[i:i+n]) for i in range(n+1)]
                    charges = [minima[i+1]-minima[i] for i in range(n)]
                    require(all(v >= 0 for v in charges) and sum(charges) == sum(f),
                            "positive future-minimum budget")
                    for i, charge in enumerate(charges):
                        require(charge <= (B+1)*f[i], "single charge height")
                        if charge == 0:
                            continue
                        counts["positive_charged_cuts"] += 1
                        running_sum = Fraction(0)
                        for j in range(1, n+1):
                            running_sum += f[(i+j-1) % n]
                            value = f[(i+j) % n]
                            require(value <= f[i]+running_sum/B, "prefix charge")
                            require(value <= f[i]*Fraction(B+1,B)**j,
                                    "exact geometric upper bound")
                            counts["charged_prefixes"] += 1
    return counts


def main():
    s = Fraction(19,20)
    def formula(M):
        return (M-1)*s/(1+M*s)

    require(formula(3) == Fraction(38,77), "exponent-three specialization")
    require(formula(Fraction(143,10)) == Fraction(2527,2917),
            "explicit separation specialization")
    require(formula(Fraction("5.116201")) == Fraction(26069273,39069273),
            "three-logarithm specialization")
    require(s/(1+s) == Fraction(19,39), "area specialization")
    print(json.dumps({
        "translated_strips": translated_strips(),
        "native_cycles": rational_cycles(),
        "three_logarithm_period_exponent": str(formula(Fraction("5.116201"))),
        "explicit_separation_period_exponent": str(formula(Fraction(143,10))),
        "exponent_three_limit": str(formula(3)),
        "scope": "Exact finite arithmetic and native trace controls, not an asymptotic proof."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
