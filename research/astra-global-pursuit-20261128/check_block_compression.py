#!/usr/bin/env python3
"""Independent finite replay of the integer interfaces in GROWING_BLOCKS.md.

This does not test the imported probability estimate or certify an asymptotic.
All comparisons below are exact integer/rational comparisons and remain active
under Python optimization. Native paths are recomputed independently for every
prefix refinement; the proposed residual recurrence is only the comparison.
"""
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def require(condition, context):
    if not condition:
        raise ValueError(context)


def native(n, steps):
    odd = 0
    for _ in range(steps):
        bit = n % 2
        odd += bit
        n = (3 * n + 1) // 2 if bit else n // 2
    return odd, n


def check():
    counts = {"source_prefixes": 0, "ordinary_lifts": 0,
              "residual_refinements": 0, "within_grade_pairs": 0,
              "sorted_pair_offsets": 0, "packing_controls": 0}
    digest = hashlib.sha256()
    for j in range(10):
        den = 2 ** j
        for r in range(den):
            for size in (1, 2, 3, 5, 8, 13, 32, 65):
                arm = [native(r + d, j) for d in range(size)]
                labels = sorted(set(arm))
                residual = {(q, c): Fraction(den * c - 3 ** q * r, den)
                            for q, c in labels}
                counts["source_prefixes"] += 1
                for q, c in labels:
                    require(0 <= q <= j, ("grade", j, r, q, c))
                    require(residual[q, c] >= 0,
                            ("negative residual", j, r, q, c))
                for d, (q, c) in enumerate(arm):
                    for z in (1, 3, 7):
                        require(native(r + den * z + d, j) ==
                                (q, 3 ** q * z + c),
                                ("physical lift", j, r, d, z))
                        counts["ordinary_lifts"] += 1
                    for digit in (0, 1):
                        rp = r + den * digit
                        qp, cp = native(rp + d, j + 1)
                        bit = (3 ** q * digit + c) % 2
                        require(qp == q + bit,
                                ("grade refinement", j, r, d, digit))
                        require(2 * cp == 3 ** bit * (3 ** q * digit + c) + bit,
                                ("intercept refinement", j, r, d, digit))
                        actual = Fraction(2 * den * cp - 3 ** qp * rp, 2 * den)
                        predicted = (3 ** bit * residual[q, c] + bit) / 2
                        require(actual == predicted,
                                ("residual recurrence", j, r, d, digit))
                        counts["residual_refinements"] += 1
                for q in range(j + 1):
                    values = sorted(residual[label] for label in labels if label[0] == q)
                    for left, right in zip(values, values[1:]):
                        require(right - left >= 1 and (right - left).denominator == 1,
                                ("unit spacing", j, r, size, q))
                        counts["within_grade_pairs"] += 1
                    for cutoff in (1, 4, 16):
                        require(sum(v < cutoff for v in values) <= cutoff,
                                ("low residual packing", j, r, size, q, cutoff))
                        counts["packing_controls"] += 1
                total_grade_gap = 0
                for low, high in zip(labels, labels[1:]):
                    q, c = low
                    qp, cp = high
                    gap = qp - q
                    total_grade_gap += gap
                    scale = 3 ** gap
                    direct = abs(Fraction(cp, scale) - c)
                    via_residual = abs(residual[high] / scale - residual[low])
                    require(direct == via_residual and
                            direct <= residual[low] + residual[high],
                            ("normalized pair offset", j, r, size, low, high))
                    counts["sorted_pair_offsets"] += 1
                require(total_grade_gap <= j, ("telescoping grade gaps", j, r, size))
                digest.update(json.dumps([j, r, size, labels], separators=(",", ":")).encode())
    return {"status": "PASS", "scope": "finite exact integer interfaces only",
            "coverage": {"prefix_depths": [0, 9], "block_sizes": [1, 2, 3, 5, 8, 13, 32, 65],
                         "positive_high_lifts": [1, 3, 7]},
            "counts": counts, "semantic_sha256": digest.hexdigest(),
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == "__main__":
    print(json.dumps(check(), sort_keys=True, indent=2))
