#!/usr/bin/env python3
"""Replay mixed distortion records and a paid-rank recovery on an actual upper word."""
import json
from fractions import Fraction


def require(condition, explanation):
    if not condition:
        raise ArithmeticError(explanation)


def step(value):
    return (3 * value + 1) // 2 if value % 2 else value // 2


def first_hit(start):
    values = [start]
    grades = [0]
    while values[-1] != 1:
        require(len(values) < 2000, f"first-hit bound at {start}")
        grades.append(grades[-1] + values[-1] % 2)
        values.append(step(values[-1]))
    return values, grades


def offsets(clock, target):
    found = []
    for word in range(1 << clock):
        offset = 0
        for j in range(clock):
            if (word >> j) & 1:
                offset = 3 * offset + (1 << j)
        if offset == target:
            found.append(word.bit_count())
    return sorted(set(found))


def record(start, expected):
    lower, pl = first_hit(start)
    upper, pu = first_hit(3 * start)
    j, wanted_t, wanted_y, wanted_x, wanted_k, wanted_r = expected
    level = Fraction(2**j * upper[j], 3**(pu[j] + 1) * start)
    require(level > 1, "upper distortion positive")
    t = next((i for i, value in enumerate(lower)
              if Fraction(2**i * value, 3**pl[i] * start) >= level), None)
    require(t == wanted_t and t > j, "lower first-passage time")
    x = lower[t]
    y = upper[j]
    a = t - j
    k = pl[t] - pu[j] - 1
    residue = (1 << a) * x - 3**k * y
    require((y, x, k, residue) == (wanted_y, wanted_x, wanted_k, wanted_r),
            "wrong physical data at matching clocks")
    require(0 <= 2 * residue < (1 << a), "half-unit rounding")
    require(all(value % 4 for value in lower[:t]), "two consecutive even departures")
    require(set(lower[:t+1]).isdisjoint(upper[:j+1]), "earlier physical meeting")
    grades = offsets(a, residue)
    repaired = []
    for r in grades:
        if r <= k:
            source = 3**(k-r) * y
            value, spent = source, 0
            for _ in range(a):
                spent += value % 2
                value = step(value)
            require((value, spent) == (x, r), "bad residual decode")
            require(source > 2 * lower[t-1], "strict ancestor size bound")
            repaired.append(source)
    return {"z": start, "upper_clock": j, "upper": y, "lower_clock": t, "lower": x,
            "lag": a, "grade_difference": k, "residual": residue,
            "offset_grades": grades, "actual_decodes": repaired,
            "lower_hit": len(lower)-1, "upper_hit": len(upper)-1}


def recovered_center():
    source = 314071486163623
    neighbor = (source - 1) // 2
    canonical = 1 + 16 * ((source - 1) // 9)
    require(source % 108 == 91 and canonical % 48 == 17, "original reduced row")
    lower, _ = first_hit(source)
    upper, _ = first_hit(neighbor)
    true_upper, true_grade = first_hit(3 * canonical)
    lower_clocks = [i + 1 for i, value in enumerate(lower[:-1]) if value % 2]
    upper_clocks = [i for i, value in enumerate(upper[:-1]) if value % 2]
    require((len(lower) - 1, len(upper) - 1) == (199, 198), "actual control hits")
    require(true_upper[6:] == upper[1:] and true_grade[6] == 2,
            "original triple has the supplied good suffix")
    require(all(value >= source for value in lower[:46]), "control strip floor")
    require(all(3 * value <= 16 * source + 7 for value in lower[:46] if value % 2),
            "control strip ceiling")
    require(all(value % 4 for value in lower[:45]), "control restricted prefix")
    states = []
    for rank in range(1, 29):
        time = lower_clocks[rank - 1]
        next_time = upper_clocks[rank]
        reserve = next_time + 1 - time
        center = lower[time] - Fraction(2) ** reserve * upper[next_time]
        states.append((rank, time, next_time, reserve, center))
    first_unpaid = next((state for state in states if state[3] < 0), None)
    require(first_unpaid == (10, 14, 12, -1, Fraction(-13, 2)), "first lost rank")
    require(states[26] == (27, 41, 41, 1, 3), "recovered positive center")
    require(states[27] == (28, 42, 42, 1, 4), "second positive center")
    return {"reduced_source": source, "canonical": canonical, "upper_neighbor": neighbor,
            "neighbor_hit": len(upper)-1, "lower_hit": len(lower)-1,
            "first_unpaid_rank": 10, "upper_at_first_unpaid": upper[12],
            "recovered_rank_and_center": [[27, 3], [28, 4]]}


def main():
    first = record(161, (10, 13, 13, 395, 5, 1))
    second = record(164513, (10, 17, 39041, 74117, 5, 13))
    require(first["actual_decodes"] == [1053], "positive repair control")
    require(not second["actual_decodes"], "non-offset control")
    print(json.dumps([first, second, recovered_center()], indent=2))


if __name__ == "__main__":
    main()
