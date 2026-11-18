"""Exact finite inverse block capacity used for the conditional floor bound."""

from collections import Counter
from functools import lru_cache

DEPTH = 6
PRECISION = 1 << 24


@lru_cache(None)
def totals(residue, steps):
    if steps == 0:
        return Counter({0: 1})
    result = Counter()
    modulus = 3**steps
    for exponent in range(1, 14):
        numerator = (1 << exponent) * residue - 1
        if numerator % 3 or numerator % 9 == 0:
            continue
        child = numerator // 3 % modulus
        for total, count in totals(child, steps - 1).items():
            result[total + exponent] += count
    return result


def lower_weight(total):
    # floor(PRECISION * (3**DEPTH / 2**total)**(3/5))
    numerator = PRECISION**5 * 3 ** (3 * DEPTH)
    denominator = 1 << (3 * total)
    low, high = 0, PRECISION
    while low + 1 < high:
        middle = (low + high) // 2
        if middle**5 * denominator <= numerator:
            low = middle
        else:
            high = middle
    return low


def main():
    weights = {
        total: lower_weight(total)
        for total in range(DEPTH, 13 * DEPTH + 1)
        if 10 * (1 << total) >= 11 * 3**DEPTH
    }
    minimum = min(
        (sum(count * weights.get(total, 0)
             for total, count in totals(residue, DEPTH).items()), residue)
        for residue in range(3 ** (DEPTH + 1))
        if residue % 3
    )
    assert minimum[0] > PRECISION
    print(f"minimum capacity >= {minimum[0]}/{PRECISION}, residue {minimum[1]}")


if __name__ == "__main__":
    main()
