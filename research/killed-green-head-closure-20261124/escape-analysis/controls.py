"""Exact finite controls for the ordinary two-gap construction and row counts."""
import json
from fractions import Fraction
from functools import lru_cache


def require(condition):
    if not condition:
        raise AssertionError("finite arithmetic check failed")


def unit(x):
    return x > 0 and x % 2 == 1 and x % 3 != 0


def step(x):
    numerator = 3 * x + 1
    gap = (numerator & -numerator).bit_length() - 1
    return numerator >> gap, gap


def inverse(z, gap):
    numerator = (z << gap) - 1
    candidate, remainder = divmod(numerator, 3)
    return candidate if remainder == 0 and unit(candidate) else None


@lru_cache(None)
def powers(k):
    modulus = 3 ** (k + 2)
    order = 2 * 3 ** (k + 1)
    lookup = {pow(2, f, modulus): f for f in range(1, order + 1)}
    require(len(lookup) == order)
    return modulus, order, lookup


def pad(z, total, k, residue):
    modulus, order, lookup = powers(k)
    first = lookup[(pow(2, total, modulus) * z - 3 - 9 * residue) % modulus]
    last = total - first
    require(1 <= first <= order and last >= 1)
    y = inverse(z, last)
    require(y is not None)
    x = inverse(y, first)
    require(x is not None and x % 3 ** k == residue)
    require(step(x) == (y, first) and step(y) == (z, last))
    require(9 * x == (z << total) - (1 << first) - 3)
    return x


def menu(z):
    children = [(child, e) for e in range(1, 7) if (child := inverse(z, e)) is not None]
    require(len(children) == 2)
    return children


def tree(q0, m):
    level = [(q0, 0)]
    for _ in range(m):
        level = [(child, used + e) for z, used in level for child, e in menu(z)]
    require(len(set(z for z, _ in level)) == len(level) == 2 ** m)
    return level


def read(x, length):
    total = 0
    for _ in range(length):
        x, e = step(x)
        total += e
    return x, total


def finite_row(q, b, eps):
    # Inverse tree: enumerate feasible gaps under the residual exact total.
    def visit(z, remaining, clock):
        if remaining == 0:
            if clock == 0:
                yield z
            return
        for e in range(1, clock - remaining + 2):
            y = inverse(z, e)
            if y is not None:
                yield from visit(y, remaining - 1, clock - e)

    threshold = int((1 - eps) * 4 ** b * q / 3 ** b)
    inverse_sources = [z for z in visit(q, b, 2 * b) if z <= threshold]
    require(len(inverse_sources) == len(set(inverse_sources)))
    # Independent forward enumeration, with no inverse congruences.
    direct = {x for x in range(1, threshold + 1, 2)
              if unit(x) and read(x, b) == (q, 2 * b)}
    require(set(inverse_sources) == direct)
    return len(direct)


def main():
    counts = {"two_gap_cases": 0, "sharp_cutoff_failures_expected": 0,
              "small_row_comparisons": 0, "small_row_sources": 0,
              "literal_padded_sources": 0, "large_literal_rows": []}
    for k in range(1, 4):
        modulus, order, _ = powers(k)
        for z in range(1, 60, 2):
            if not unit(z):
                continue
            for total in range(order + 1, order + 14):
                for residue in range(1, 3 ** k):
                    if residue % 3:
                        pad(z, total, k, residue)
                        counts["two_gap_cases"] += 1
        for first in range(1, order):
            require((9 + pow(2, first, modulus) + 3 - pow(2, order, modulus) * 13) % modulus)
        counts["sharp_cutoff_failures_expected"] += 1

    for q in range(1, 60, 2):
        if unit(q):
            for b in range(1, 9):
                for eps in [Fraction(1, 3), Fraction(1, 13), Fraction(1, 31)]:
                    counts["small_row_sources"] += finite_row(q, b, eps)
                    counts["small_row_comparisons"] += 1

    # An ordinary start with exactly prescribed initial odd gaps. No all-time
    # conclusion about this integer is needed for the finite checks.
    q0 = (1 << 511) - 1
    for b, m, k in [(52, 3, 1), (105, 6, 2), (147, 9, 2), (224, 11, 3)]:
        i = b - m - 2
        q, suffix_clock = read(q0, i)
        require(q == 3 ** i * (1 << (511 - i)) - 1 and suffix_clock == i)
        leaves = tree(q0, m)
        all_sources = set()
        for r in range(1, 3 ** k):
            if not r % 3:
                continue
            per_class = set()
            for z, clock in leaves:
                t = 2 * b - suffix_clock - clock
                x = pad(z, t, k, r)
                require(read(x, m + 2) == (q0, t + clock))
                require(read(x, b) == (q, 2 * b))
                require(((4 ** b * q - 3 ** b * x) * (3 * q0 + 1)
                        >= 4 ** b * q))
                per_class.add(x)
            require(len(per_class) == 2 ** m and not (all_sources & per_class))
            all_sources.update(per_class)
        counts["literal_padded_sources"] += len(all_sources)
        counts["large_literal_rows"].append({"odd_depth": b, "clock": 2 * b,
                                              "tree_depth": m, "ternary_digits": k,
                                              "distinct_sources": len(all_sources)})
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
