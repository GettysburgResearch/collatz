"""A small diagnostic for the all-residue conjecture; not a cycle proof."""

from collections import Counter
from itertools import combinations

A, p = 8, 5
D = 2**A - 3**p
histogram = Counter()
for positions in combinations(range(A), p):
    numerator = sum(2**d * 3 ** (p - 1 - i) for i, d in enumerate(positions))
    histogram[numerator % D] += 1

expected = [0, 3, 4, 7, 4, 3, 7, 5, 3, 4, 4, 6, 6]
actual = [histogram[r] for r in range(D)]
assert actual == expected
assert sum(actual) == 56
assert max(actual) == A - 1
print({"A": A, "p": p, "D": D, "histogram": actual, "maximum": max(actual)})
