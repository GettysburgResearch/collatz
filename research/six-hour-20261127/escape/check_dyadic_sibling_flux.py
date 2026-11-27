"""Enumerate the actual visit-to-five coloring on finite positive dyadic levels."""

from collections import Counter
import json


def check(condition, detail):
    if not condition:
        raise ArithmeticError(detail)


def visit_five(limit):
    colors = {1: 0, 5: 1}
    for start in range(1, limit):
        trail = []
        seen = set()
        n = start
        while n not in colors:
            check(n not in seen, ("unresolved cycle", start, n))
            seen.add(n)
            trail.append(n)
            n = (3 * n + 1) // 2 if n % 2 else n // 2
        for value in trail:
            colors[value] = colors[n]
    return colors


def run(depth, initial=3):
    colors = visit_five(1 << (depth + 1))
    opportunity_by_parent_level = []
    for j in range(initial, depth):
        lower = 1 << j
        count = 0
        changes = 0
        for n in range(lower, 2 * lower):
            check(colors[2 * n] == colors[n], ("even", n))
            flux = colors[2 * n + 1] - colors[n]
            count += int(flux != 0)
            changes += flux
        opportunity_by_parent_level.append([j, count, changes])
    sum_c_square = sum_p_square = sum_k = 0
    opportunities_by_count = Counter()
    outcome_counts = Counter()
    start = 1 << depth
    for leaf in range(start, 2 * start):
        p = c = k = 0
        previous_sign = previous_bit = None
        ancestor = leaf >> (depth - initial)
        for j in range(initial, depth):
            n = leaf >> (depth - j)
            bit = (leaf >> (depth - j - 1)) % 2
            e = colors[2 * n + 1] - colors[n]
            p += e
            c += (2 * bit - 1) * e
            if e:
                k += 1
                outcome_counts[k, e, bit] += 1
                if previous_sign is not None:
                    check(e == previous_sign * (1 - 2 * previous_bit),
                          ("next opportunity sign", leaf, j))
                previous_sign, previous_bit = e, bit
        check(p + c == 2 * (colors[leaf] - colors[ancestor]),
              ("telescoping", leaf))
        sum_c_square += c * c
        sum_p_square += p * p
        sum_k += k
        opportunities_by_count[k] += 1
    check(sum_c_square == sum_k, "fair predictable quadratic variation")
    # Every prefix where the hth opportunity is known has equally many
    # full leaves making its immediate left and right choice.
    for k, e, _ in outcome_counts:
        check(outcome_counts[k, e, 0] == outcome_counts[k, e, 1],
              ("balanced outcomes at predictable opportunity", k, e))
    return {"initial_level": initial, "final_level": depth, "uniform_leaves": start,
            "opportunity_by_parent_level": opportunity_by_parent_level,
            "leaf_opportunity_histogram": dict(sorted(opportunities_by_count.items())),
            "sum_centered_square": sum_c_square,
            "sum_predictable_square": sum_p_square, "sum_opportunities": sum_k}


if __name__ == "__main__":
    print(json.dumps([run(12), run(16)], indent=2, sort_keys=True))
