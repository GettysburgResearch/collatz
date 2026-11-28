"""Exact source-language entropy certificate for the pinned PR204 return bank."""
from collections import Counter
from fractions import Fraction


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def records(clock_limit, grade_limit):
    stack = [(1, 1, 2, 8, 1, 1)]
    histogram = Counter()
    while stack:
        h, r, left, right, grade, companion_grade = stack.pop()
        if grade == companion_grade and right == 5 * left:
            histogram[h] += 1
            continue
        if h == clock_limit:
            continue
        for bit in range(2):
            x = left + bit * 3**grade
            y = right + bit * 5 * 3**companion_grade
            p, q = grade + x % 2, companion_grade + y % 2
            if max(p, q) <= grade_limit:
                stack.append((h + 1, r + bit * 2**h, step(x), step(y), p, q))
    return histogram


def all_cost(histogram, z):
    return sum(n * z**h for h, n in histogram.items()) / (1 - z)


def main():
    h = records(27, 8)
    expected = {
        6: 1, 8: 2, 9: 1, 10: 3, 11: 4, 12: 12, 13: 16, 14: 41,
        15: 63, 16: 106, 17: 117, 18: 182, 19: 175, 20: 241,
        21: 239, 22: 244, 23: 234, 24: 222, 25: 167, 26: 112, 27: 94,
    }
    require(h == expected and sum(h.values()) == 2276, "PR204 finite return bank")
    require(all_cost(h, Fraction(1, 2)) == Fraction(2923925, 33554432), "conditional cylinder mass")
    majorant = all_cost(h, Fraction(17, 28))
    require(majorant == Fraction(228726486040445967436698285962972757271,
                                 232525991228180563449170925246818025472),
            "rational generating-function bound")
    require(majorant < 1 and 28**25 < 2**18 * 17**25, "pointwise exponent strictly below 18/25")
    print(f"PASS {sum(h.values())} first-return words, conditional mass {all_cost(h, Fraction(1, 2))}")
    print(f"PASS E(17/28)={majorant} < 1, exponent log2(28/17) < 18/25")


if __name__ == "__main__":
    main()
