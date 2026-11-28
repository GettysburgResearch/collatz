"""Exact finite interfaces for the local parity-budget counterexample."""
from collections import Counter
from math import comb


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def shortcut(n):
    return (3 * n + 1) // 2 if n & 1 else n // 2


def unit_children(n):
    result = []
    for exponent in range(3, 9):
        numerator = (n << exponent) - 1
        if numerator % 3 == 0:
            child = numerator // 3
            if child % 3:
                require(child > n and child & 1, (n, exponent, child))
                value = child
                for _ in range(exponent):
                    value = shortcut(value)
                require(value == n, (n, exponent, "actual edge"))
                result.append(child)
    require(len(result) == 2, (n, result))
    return result


def check_populations():
    level = {1}
    cohorts = cuts = 0
    for q in range(13):
        require(len(level) == 1 << q, (q, "tree injectivity"))
        log_bound = 8 * q + 5
        bound = 1 << log_bound
        lifted = set()
        for u in sorted(level):
            require(u & 1 and u % 3 and u <= 1 << (8 * q), (q, u))
            value, steps = u, 0
            while value != 1 and steps <= 8 * q:
                value = shortcut(value)
                steps += 1
            require(value == 1 and steps <= 8 * q, (q, u, "first hit"))
            padding = (bound // u).bit_length() - 1
            n = u << padding
            require(bound // 2 < n <= bound and n not in lifted,
                    (q, u, "physical octave"))
            lifted.add(n)
            digits, value = [], n
            for _ in range(2 * log_bound):
                digits.append(value & 1)
                value = shortcut(value)
            for t in sorted({3, max(3, log_bound // 2), log_bound,
                             5 * log_bound // 4, 2 * log_bound}):
                mismatches = sum(digits[i] != digits[i + 2] for i in range(t - 2))
                require(mismatches <= 8 * q + 4, (q, n, t, mismatches))
                cuts += 1
            cohorts += 1
        if q < 12:
            children = [child for n in sorted(level) for child in unit_children(n)]
            require(len(set(children)) == len(children), (q, "merged branches"))
            level = set(children)
    return cohorts, cuts


def check_fair_disagreement():
    words = 0
    for length in range(3, 16):
        histogram = Counter()
        joint = set()
        for bits in range(1 << length):
            disagreement = (bits ^ (bits >> 2)) & ((1 << (length - 2)) - 1)
            histogram[disagreement.bit_count()] += 1
            joint.add((bits & 3, disagreement))
            words += 1
        require(len(joint) == 1 << length, (length, "XOR bijection"))
        require(histogram == {j: 4 * comb(length - 2, j) for j in range(length - 1)},
                (length, "exact binomial law"))
    return words


if __name__ == "__main__":
    cohorts, cuts = check_populations()
    print(cohorts, "distinct terminating-source cohort members;", cuts,
          "actual native cuts;", check_fair_disagreement(), "fair XOR words")
