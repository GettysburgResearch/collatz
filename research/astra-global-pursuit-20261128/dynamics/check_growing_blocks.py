"""Finite exact controls for the common-cylinder residual compression."""

from collections import Counter, defaultdict
from math import isqrt
import json


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def shortcut(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def counted(x, steps):
    grade = 0
    for _ in range(steps):
        grade += x % 2
        x = shortcut(x)
    return grade, x


def ceil_sqrt_fraction(numerator, denominator):
    root = isqrt(numerator // denominator)
    return root if root * root * denominator == numerator else root + 1


def rounded_weight(labels, scale, residue):
    return sum(
        1 + ceil_sqrt_fraction(scale * c - 3**q * residue, scale)
        for q, c in labels
    )


def audit_width(width, levels, counts):
    # Index labels are computed independently on the canonical positive
    # or zero starts, then checked against the two-refinement construction.
    for j in range(levels):
        scale = 1 << j
        for r in range(scale):
            labels = sorted({counted(r + d, j) for d in range(width)})
            expected = [
                {counted(r + digit * scale + d, j + 1) for d in range(width)}
                for digit in (0, 1)
            ]
            children = [set(), set()]
            by_grade = defaultdict(list)
            for q, c in labels:
                slope = 3**q
                residual = scale * c - slope * r
                require(residual >= 0, "nonnegative residual")
                by_grade[q].append(residual)
                for digit in (0, 1):
                    real_input = slope * digit + c
                    b = real_input % 2
                    q_new, c_new = q + b, shortcut(real_input)
                    updated = 2 * scale * c_new - 3**q_new * (r + digit * scale)
                    require(updated == 3**b * residual + scale * b, "residual update")
                    children[digit].add((q_new, c_new))
                    counts["arm_digit_residual_updates"] += 1
            require(children == expected, "complete child label sets")
            counts["complete_child_label_sets"] += 2
            for group in by_grade.values():
                require(all(b - a >= scale for a, b in zip(group, group[1:])), "spacing")
                counts["grade_lists"] += 1
            # Test several exact cutoffs in the packing bound before powers.
            for cutoff in (1, 4, 8, 16):
                small = sum(
                    n < cutoff * scale for group in by_grade.values() for n in group
                )
                require(small <= cutoff * (j + 1), "low residual packing")
                counts["integer_packing_bounds"] += 1
            gaps = 0
            for (p, a), (q, b) in zip(labels, labels[1:]):
                k = q - p
                gaps += k
                left = scale * a - 3**p * r
                right = scale * b - 3**q * r
                require(
                    scale * (b - 3**k * a) == right - 3**k * left,
                    "normalized bridge cancellation",
                )
                counts["sorted_offset_identities"] += 1
            require(gaps <= j, "telescoping grade gap")
            counts["grade_telescopes"] += 1
            # sqrt concavity with upward rounding gives E W' <=
            # (49/50) W + 2 N: sufficient slack for an integer-only control.
            parent_w = rounded_weight(labels, scale, r)
            twice_child_w = sum(
                rounded_weight(children[d], 2 * scale, r + d * scale) for d in (0, 1)
            )
            require(25 * twice_child_w <= 49 * parent_w + 100 * len(labels),
                    "rounded fractional drift")
            counts["two_child_rounded_drifts"] += 1
            for tail in (1, 7, 37):
                actual = {counted(r + scale * tail + d, j) for d in range(width)}
                predicted = {(q, 3**q * tail + c) for q, c in labels}
                require(actual == predicted, "ordinary source cylinder lifts")
                counts["ordinary_whole_block_lifts"] += 1


def main():
    counts = Counter()
    for width in (2, 3, 5, 8, 17, 64):
        audit_width(width, 9, counts)
    print(json.dumps(dict(sorted(counts.items())), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
