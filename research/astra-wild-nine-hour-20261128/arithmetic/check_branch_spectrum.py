"""Finite exact controls for the affine-branch spectrum. No asymptotic test."""

import json
from itertools import product
from math import comb


def require(condition, context):
    if not condition:
        raise ValueError(context)


def iterate(value, length, sign=1):
    grade = 0
    for _ in range(length):
        if value % 2:
            value = (3 * value + sign) // 2
            grade += 1
        else:
            value //= 2
    return grade, value


def word_row(length, mask):
    """Return exact grade and numerator of the offset over 2^length."""
    grade, numerator = 0, 0
    for index in range(length):
        if (mask >> index) & 1:
            numerator = 3 * numerator + (1 << index)
            grade += 1
    return grade, numerator


def canonical(length, mask):
    grade, numerator = word_row(length, mask)
    modulus = 3**grade
    value = (numerator * pow(2**length, -1, modulus)) % modulus
    return grade, value


def check_rows(max_depth):
    receipts = []
    for k in range(max_depth + 1):
        positive = [set() for _ in range(k + 1)]
        negative = [set() for _ in range(k + 1)]
        formal = [set() for _ in range(k + 1)]
        ordinary = set()
        for r in range(2**k):
            p, value = iterate(r, k)
            positive[p].add(value)
            require(0 <= value < 3**p, (k, p, r))
            q, omitted = iterate((-r) % (2**k), k, sign=-1)
            require(q == p and omitted == (3**p - value if r else 0), (k, r))
            negative[q].add(omitted)
            q, offset = canonical(k, r)
            formal[q].add(offset)
            grade, endpoint = iterate(3 * 2**k + r, k)
            require((grade, endpoint) == (p, 3**p * 3 + value), (k, r, "lift"))
            ordinary.add(endpoint)
        counts = [len(values) for values in positive]
        require(positive == formal, (k, "formal set mismatch"))
        require(counts == [len(values) for values in negative], (k, "reflection"))
        require(sum(counts) == len(ordinary), (k, "unmarked interval"))
        require(all(n <= min(comb(k, p), 3**p) for p, n in enumerate(counts)),
                (k, "capacity"))
        receipts.append({"depth": k, "by_grade": counts, "total": sum(counts)})
    return receipts


def check_gap_orientation():
    cases = 0
    for n in range(1, 6):
        modulus = 3**n
        for gaps in product(range(1, 5), repeat=n):
            total = 0
            row = 0
            for i, gap in enumerate(gaps):
                total += gap
                row += 3**i * pow(2**total, -1, modulus)
            clock = 0
            mask = 0
            for gap in reversed(gaps):
                mask |= 1 << clock
                clock += gap
            require(canonical(clock, mask) == (n, row % modulus), gaps)
            cases += 1
    return cases


def check_padding():
    cases = 0
    for k in range(8):
        for length in range(5):
            for tail in range(2**length):
                seen = {}
                for prefix in range(2**k):
                    old = canonical(k, prefix)
                    new = canonical(k + length, prefix | (tail << k))
                    require(seen.setdefault(new, old) == old, (k, length, tail))
                    cases += 1
    return cases


if __name__ == "__main__":
    rows = check_rows(16)
    require(rows[12]["total"] == 1535, "paper 212, depth 12 comparison")
    print(json.dumps({"rows": rows, "gap_words": check_gap_orientation(),
                      "padding_words": check_padding()}, indent=2))
