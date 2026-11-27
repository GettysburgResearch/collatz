"""Cross-check stopping scores against the augmented state at a single clock."""

import json
from math import comb
from collections import defaultdict
from fractions import Fraction


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(value):
    return (3 * value + 1) // 2 if value % 2 else value // 2


def first_hit(value):
    clock = 0
    odds = 0
    while value != 1:
        # Fail closed on an unexpected trajectory in this specific finite check.
        require(clock < 100_000, "first-hit clock exceeded the finite replay limit")
        odds += value % 2
        value = step(value)
        clock += 1
    return clock, odds


def direct_state(value, clock, initial_grade):
    grade = initial_grade
    for _ in range(clock):
        if value % 2:
            grade += 1
            value = (3 * value + 1) // 2
        else:
            value //= 2
    return value, grade


def check_tower(base, last_rank):
    starts = [base * 3**rank for rank in range(last_rank + 1)]
    hits = [first_hit(value) for value in starts]
    common_clock = max(clock for clock, _ in hits)
    by_score = defaultdict(list)
    by_state = defaultdict(list)
    for rank, (value, (clock, odds)) in enumerate(zip(starts, hits)):
        by_score[2 * (rank + odds) - clock].append(rank)
        by_state[direct_state(value, common_clock, rank)].append(rank)
    require(sorted(by_score.values()) == sorted(by_state.values()),
            f"score and direct-state partitions disagree at base {base}")
    records = sorted(ranks[0] for ranks in by_score.values())
    return {
        "base": base,
        "last_rank": last_rank,
        "common_clock": common_clock,
        "class_count_in_sample": len(by_score),
        "largest_class_in_sample": max(map(len, by_score.values())),
        "first_class_members": records,
    }


def high_gate_bound():
    last = 2000
    numerator = 480 * 2**(last - 25)
    for clock in range(65, last + 1):
        threshold = 3 * clock // 5 - 1
        coefficient = comb(clock - 1, threshold)
        heavy = 0
        for index in range(threshold, clock):
            heavy += coefficient
            coefficient = coefficient * (clock - 1 - index) // (index + 1)
        power = 3**threshold
        count = clock + heavy + power + power // 2**threshold
        numerator += count * 2**(last - clock)
    require(10 * numerator < 29 * 2**last, "high-gate bound exceeds 29/10")
    return {
        "cutoff_exponent": 64,
        "last_dyadic_exponent": last,
        "upper_bound_times_1000000_rounded_up": (10**6 * numerator + 2**last - 1) // 2**last,
    }


def main():
    q = Fraction(5, 4) ** 10 / Fraction(3, 2) ** 6
    a = Fraction(729, 1024)
    require(q**4 < Fraction(1, 2) and a**4 < Fraction(1, 2),
            "heavy or light ratio fails its fourth-power inequality")
    require(Fraction(4, 3) ** 4 > 2, "dyadic constant estimate failed")
    print(json.dumps({
        "high_gate": high_gate_bound(),
        "heavy_ratio": str(q),
        "light_ratio": str(a),
        "towers": [check_tower(1, 1024), check_tower(5, 256), check_tower(10, 256)],
    }, indent=2))


if __name__ == "__main__":
    main()
