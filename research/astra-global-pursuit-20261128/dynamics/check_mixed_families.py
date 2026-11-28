"""Exact ordinary reruns for the signed sparse labels and mixed-radix intervals."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb
import json

from check_growing_blocks import counted, require


def signed_label(arm, r, depth):
    grade, intercept = arm
    added, endpoint = counted(3**grade * r + intercept, depth)
    return grade + added, endpoint


def audit_signed(family, center, max_depth, counts):
    for depth in range(max_depth + 1):
        size = 2**depth
        grade_laws = [Counter() for _ in family]
        for r in range(size):
            labels = [signed_label(arm, r, depth) for arm in family]
            for law, (q, _), (initial, _) in zip(grade_laws, labels, family):
                law[q - initial] += 1
            for arm, (q, c) in zip(family, labels):
                residual = c - 3**q * (r + center) / size
                for digit in (0, 1):
                    new_r = r + size * digit
                    new_q, new_c = signed_label(arm, new_r, depth + 1)
                    b = new_q - q
                    expected = (3**b * residual + b) / 2
                    actual = new_c - 3**new_q * (new_r + center) / (2 * size)
                    require(actual == expected, "signed centered residual")
                    counts["signed_centered_updates"] += 1
            distinct = sorted(set(labels))
            for (p, a), (q, b) in zip(distinct, distinct[1:]):
                low = a - 3**p * (r + center) / size
                high = b - 3**q * (r + center) / size
                require(Fraction(b, 3**(q-p)) - a == high / 3**(q-p) - low,
                        "signed normalized cancellation")
                counts["signed_normalized_cancellations"] += 1
        for law in grade_laws:
            require(law == Counter({k: comb(depth, k) for k in range(depth + 1)}),
                    "exact marginal binomial law")
            counts["individual_binomial_laws"] += 1


def audit_intervals(h, counts):
    for a, b in product(range(h + 1), repeat=2):
        multiplier = 2**a * 3**b
        for r in range(multiplier):
            k, c = counted(r, a)
            require(c + 1 <= Fraction(3, 2)**a * (r + 1), "intercept bound")
            for anchor in (1, 2, 7, 23, 101, 1024):
                start = multiplier * anchor + r
                grade, actual = counted(start, a)
                require((grade, actual) == (k, 3**(b+k) * anchor + c),
                        "complete mixed-radix interval label")
                counts["ordinary_mixed_interval_lifts"] += 1


def main():
    counts = Counter()
    families = (
        ([(0, -201), (0, 0), (2, 17), (4, -70)], Fraction(-13, 7)),
        ([(5, -2), (0, 400), (1, -90), (1, 20), (3, 7)], Fraction(21, 5)),
    )
    for family, center in families:
        audit_signed(family, center, 7, counts)
    audit_intervals(5, counts)
    print(json.dumps(dict(sorted(counts.items())), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
