"""Exact calibrations for the moving width margin, disjoint moments and grade trap."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import prod


def require(value, message):
    if not value:
        raise ValueError(message)


def native(x):
    raw = 3 * x + 1
    numerator = raw & -raw
    return raw // numerator, numerator.bit_length() - 1


def width_margin():
    lo = Fraction(158496250, 10**8)
    hi = Fraction(158496251, 10**8)
    # Atanh series proves the bracket for log_2(3).
    def log_interval(x):
        t = Fraction(x - 1, x + 1)
        partial = 2 * sum(t ** (2 * i + 1) / (2 * i + 1) for i in range(55))
        error = 2 * t**111 / (111 * (1 - t*t))
        return partial, partial + error

    ln2, ln3 = log_interval(2), log_interval(3)
    require(lo < ln3[0] / ln2[1] <= ln3[1] / ln2[0] < hi, "gamma bracket")
    d_lo = Fraction(3, 8) * ((2-hi) * 5*lo/3 + (2*lo-3)*Fraction(3, 2))
    d_hi = Fraction(3, 8) * ((2-lo) * 5*hi/3 + (2*hi-3)*Fraction(3, 2))
    require(Fraction(50671, 100000) < d_lo <= d_hi < Fraction(50673, 100000),
            "entropy rate")
    require(1 - 3*d_hi/lo > Fraction(4088, 100000) > Fraction(1, 25),
            "shrinking margin")
    print("Certified .50671 < d_* < .50673 and 1 - 3d_*/gamma > .04088 > 1/25.")


def power_paths():
    starts = (65, 79, 107, 191, 247, 289, 359, 443, 625, 905, 961, 1073, 1087, 1129)
    ends, exponents = zip(*(native(x) for x in starts))
    require(len(set(starts + ends)) == 2 * len(starts), "disjoint vertices")
    require(min(starts + ends) >= 31 and all(x % 3 for x in starts + ends), "units")
    require(Counter(exponents) == {1: 7, 2: 7}, "word law")
    require(Counter(x % 6 for x in starts) == Counter(x % 6 for x in ends), "residues")
    require(all(sum(x**k for x in starts) == sum(x**k for x in ends)
                for k in range(3)), "ordinary power sums")
    separate = (19, 25, 29, 43, 143)
    endpoints = tuple(native(x)[0] for x in separate)
    require(prod(separate) == prod(endpoints) == 84702475 and set(separate) != set(endpoints),
            "separate product control")
    print("Fourteen disjoint degree-two native edges, modulus 6 and equal type frequencies.")
    print("Separate five-source multiplicative mass 84702475 is exact.")


def prouhet():
    cases = 0
    for width, degree in product(range(2, 8), range(1, 5)):
        tally = [[0] * (degree + 1) for _ in range(width)]
        for n in range(width ** (degree + 1)):
            digits, x = 0, n
            while x:
                x, digit = divmod(x, width)
                digits += digit
            row = tally[digits % width]
            for k in range(degree + 1):
                row[k] += n**k
        require(all(v == tally[0] for v in tally), "Prouhet class mismatch")
        cases += 1
    print(f"{cases} generalized Prouhet partitions passed.")


def grade_trap():
    labels = (4097, 4100, 4124, 4130)
    heights = []
    for i in range(3):
        heights.append(labels[0] - labels[1] - labels[2] + labels[3])
        tags = tuple(x & -x for x in labels)
        physical = tuple(x // c for x, c in zip(labels, tags))
        require(max(tags) <= 4 and all(x % 3 for x in physical), "grade trap sources")
        if i < 2:
            raw = tuple(3*x+c for x,c in zip(labels,tags))
            require(all(r % 4 == 0 for r in raw), "common winding two")
            labels = tuple(r // 4 for r in raw)
            require(tuple(native(x)[0] for x in physical) ==
                    tuple(z // (z & -z) for z in labels), "actual Syracuse edges")
    require(heights == [3, 1, 0], "height drop")
    print("Three-grade four-column register with common windings 2,2 has heights 3,1,0.")


if __name__ == "__main__":
    width_margin()
    power_paths()
    prouhet()
    grade_trap()
