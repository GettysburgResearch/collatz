"""Exact inverse calendars versus physical first hits, plus the leading simplex count."""

from collections import Counter
from fractions import Fraction
from math import factorial
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(x):
    return (3 * x + 1) // 2 if x % 2 else x // 2


def direct_grade(x, target, budget):
    # 2^t * target <= 4^budget * x for every qualifying visit.
    duration = ((x << (2 * budget)) // target).bit_length() - 1
    grade = 0
    for _ in range(duration + 1):
        if x == target:
            return grade
        grade += x % 2
        if grade > budget:
            break
        x = step(x)
    return budget + 1


def inverse_grades(target, source_limit, budget):
    """Enumerate each number of true odd departures and its interleaved even runs."""
    limit = ((source_limit << (2 * budget)) // target).bit_length() - 1
    best = {}

    def extend(current, depth, spent):
        source = current
        for _ in range(limit - spent + 1):
            if source > source_limit:
                break
            if best.get(source, budget + 1) > depth:
                best[source] = depth
            source *= 2
        if depth == budget:
            return
        # A missing intermediate above source_limit may still have a smaller
        # odd predecessor. The total native-clock bound covers these cases.
        for exponent in range(1, limit - spent + 1):
            numerator = (current << exponent) - 1
            if numerator % 3:
                continue
            previous = numerator // 3
            require(previous > 0 and previous % 2 == 1, "illegal odd inverse")
            extend(previous, depth + 1, spent + exponent)

    if limit >= 0:
        extend(target, 0, 0)
    return best


def bounded_controls():
    targets = [(1, 1), (1, 2), (8, 2), (5, 8), (2, 5), (113, 509), (3, 9)]
    limit = 4096
    budget = 9
    cache = {}
    for target in sorted({t for pair in targets for t in pair}):
        by_inverse = inverse_grades(target, 3 * limit, budget)
        for x in range(1, 3 * limit + 1):
            physical = direct_grade(x, target, budget)
            require(by_inverse.get(x, budget + 1) == physical,
                    f"grade mismatch at source {x}, target {target}")
        cache[target] = by_inverse
    checks = []
    for a, b in targets:
        grades = Counter()
        for s in range(1, limit + 1):
            total = cache[a].get(s, budget + 1) + cache[b].get(3 * s, budget + 1)
            if total <= budget:
                grades[total] += 1
        rows = {}
        for X in (64, 256, 1024, 2048):
            rows[str(X)] = [sum(cache[a].get(s, budget + 1) +
                                cache[b].get(3 * s, budget + 1) <= cutoff
                                for s in range(X, 2 * X)) for cutoff in (5, 7, 9)]
        checks.append({"targets": [a, b], "full_source_grade_histogram": dict(sorted(grades.items())),
                       "octaves_at_budgets_5_7_9": rows})
    return {"source_limit": limit, "individual_target_source_limit": 3 * limit,
            "individual_first_grade_comparisons": len(cache) * 3 * limit, "pairs": checks}


def leading_calendars(upstream, odd_count, limit):
    """Count legal leading-cylinder residue calendars of total clock at most limit.

    This counts the simplex with all e_j >= 1, j >= 1, and e_0 >= 0.
    Short-coordinate boundary cases are included, so it is a test of the
    residue coefficient, not a replacement for the physical first-hit tests.
    """
    start_class = {pow(2, j, 27): j for j in range(18)}
    require(len(start_class) == 18, "wrong ternary unit group at modulus 27")
    solve = {x: start_class[(20 * pow(x, -1, 27)) % 27]
             for x in range(27) if x % 3}
    periods = {j: 3 ** (3 + j) for j in range(1, odd_count + 1)}
    powers = {j: [pow(2, e, mod) for e in range(limit + 1)] for j, mod in periods.items()}

    def count(value, remaining, room):
        if remaining == 0:
            first = solve[value % 27]
            return 0 if first > room else 1 + (room - first) // 18
        answer = 0
        modulus = periods[remaining]
        for e in range(1, room - remaining + 2):
            residue = (powers[remaining][e] * value - 1) % modulus
            if residue % 3 or residue % 9 == 0:
                continue
            answer += count(residue // 3, remaining - 1, room - e)
        return answer

    return count(upstream, odd_count, limit)


def simplex_controls():
    rows = []
    for p in (0, 1, 2):
        for length in (36, 144, 576, 2304):
            count = leading_calendars(1, p, length)
            scaled = Fraction(18 * 3**p * factorial(p + 1) * count, length**(p + 1))
            rows.append({"common_odd_count": p, "native_sum_cutoff": length,
                         "calendar_count": count, "ratio_to_leading_term": str(scaled)})
    return rows


def main():
    result = {"bounded_physical_comparison": bounded_controls(),
              "leading_simplex": simplex_controls()}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
