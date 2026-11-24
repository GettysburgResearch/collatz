#!/usr/bin/env python3
"""Bounded independent replay of the two physical head arms and their grade shifts."""
from collections import Counter
from fractions import Fraction
import json


def require(condition, explanation):
    if not condition:
        raise ValueError(explanation)


def step(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def hit(n, target):
    """A repeated state without a prior entrance is an exact missing witness."""
    visited = set()
    time = odds = 0
    while n not in visited:
        if n in target:
            return n, time, odds
        visited.add(n)
        odds += n % 2
        n = step(n)
        time += 1
    return None


def arm_certificate(z, new_z, c, limit, ceiling):
    """Look for a same-profile fusion after the prescribed 0/1 initial clocks."""
    shift_time = int(c == 2)
    shift_odds = -int(c == 3)
    base_odds = 0
    new_odds = (new_z % 2) if shift_time else 0
    if min(z, new_z) <= ceiling:
        return False
    if shift_time:
        new_z = step(new_z)
    for _ in range(limit + 1):
        if min(z, new_z) <= ceiling:
            return False
        if z == new_z and new_odds == base_odds + shift_odds:
            return True
        base_odds += z % 2
        new_odds += new_z % 2
        z, new_z = step(z), step(new_z)
    return False


def group_control():
    # A finite nonuniform law, with two retained categories and a missing atom.
    m = 7
    grade = [(i, j) for i in range(m) for j in range(m)]
    mass = {(k, i, j): (5*k + i*i + 3*i*j + 7*j) % 13
            for k in range(2) for i, j in grade}
    averaged = {(k, i, j): Fraction(sum(mass[k, x, y] for x, y in grade), m*m)
                for k, i, j in mass}
    distances = []
    for u, v in grade:
        distances.append(sum(abs(mass[k, i, j] - mass[k, (i+u) % m, (j+v) % m])
                             for k, i, j in mass))
    l1 = sum(abs(mass[key] - averaged[key]) for key in mass)
    require(l1 <= Fraction(sum(distances), len(grade)), "translation averaging")
    return {"modulus": m, "l1_to_product": str(l1),
            "mean_translated_l1": str(Fraction(sum(distances), len(grade)))}


def main():
    counts = Counter()
    cases = Counter()
    sample = list(range(320, 1600, 3))
    for r in range(81):
        for n in sample:
            for c in (2, 3):
                for digit in range(c):
                    new_n = c*n + digit
                    old_pair = (81*n+r, n)
                    new_pair = (81*new_n+r, new_n)
                    counts["digit_trials"] += 1
                    if not all(arm_certificate(z, y, c, 34, 25)
                               for z, y in zip(old_pair, new_pair)):
                        continue
                    counts["certified_pairs"] += 1
                    # Distinct target sets test both-miss and one-hit records.
                    target_pairs = (({1}, {1}), ({11}, {13}), ({3, 6}, {3, 5, 10}),
                                    ({7, 14}, {11, 22}))
                    for targets in target_pairs:
                        before = [hit(z, s) for z, s in zip(old_pair, targets)]
                        after = [hit(z, s) for z, s in zip(new_pair, targets)]
                        key = ''.join('H' if x else 'M' for x in before)
                        cases[str(c) + key] += 1
                        for a, b in zip(before, after):
                            require((a is None) == (b is None), "missing tag")
                            if a is not None:
                                require(b == (a[0], a[1] + int(c == 2), a[2] - int(c == 3)),
                                        "first entrance or exact grade shift")
                        if all(before):
                            require(tuple(before[0][i]-before[1][i] for i in (1,2)) ==
                                    tuple(after[0][i]-after[1][i] for i in (1,2)), "paired gaps")
    require(all(str(c) + pattern in cases for c in (2,3)
                for pattern in ('MM','MH','HM','HH')), "hit-pattern coverage")
    return {"head_controls": dict(counts), "record_patterns": dict(sorted(cases.items())),
            "finite_group": group_control()}


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, sort_keys=True))
