"""Integer-only cutoff, own-label and exact tilted-grade slice controls."""

from collections import Counter
from fractions import Fraction
from math import comb
import json


def require(truth, message):
    if not truth:
        raise ValueError(message)


def step(n):
    return (3*n + 1) // 2 if n % 2 else n // 2


def records(n, bound):
    values = [n]
    grades = [0]
    for _ in range(bound):
        grades.append(grades[-1] + values[-1] % 2)
        values.append(step(values[-1]))
    return values, grades


def native_deadline(n, targets):
    x, m, four, three = n, 0, 1, 1
    visited = set()
    while four <= three*n*n:
        if x in targets:
            visited.add(x)
        x, m = step(x), m+1
        four *= 4
        three *= 3
    return visited, m


def deadline_controls():
    labels = {1, 3, 5, 27, 85}
    checks, clock_dates = 0, 0
    for n in range(1, 2049):
        observed, end = native_deadline(n, labels)
        B = n.bit_length()
        values, _ = records(n, 5*B)
        direct = {x for m, x in enumerate(values) if x in labels and 4**m <= 3**m*n*n}
        require(end <= 5*B, 'five-bit search completeness')
        require(direct == observed, 'two native deadline tests disagree')
        for m in range(10*B):
            require((m < end) == (4**m <= 3**m*n*n), 'integer deadline interval')
            clock_dates += 1
        checks += len(labels)
    require(1 in native_deadline(3, labels)[0], '3 reaches 1 before its cutoff')
    require(1 not in native_deadline(27, labels)[0], '27 misses its cutoff for 1')
    require(records(27, 70)[0][-1] == 1, 'actual late visit from 27')
    patterns = {}
    for p in (5, 7):
        c = Counter()
        for n in range(1024, 2048):
            row = tuple(int(1 in native_deadline(p**j*n, {1})[0]) for j in range(4))
            c[''.join(map(str,row))] += 1
        require(sum(c.values()) == 1024, 'octave pattern total')
        patterns[str(p)] = dict(sorted(c.items()))
    return {'integer_deadline_tests': checks, 'integer_clock_comparisons':clock_dates,
            'target_1_deadline_patterns_at_four_dilations':patterns}


def tilt_controls():
    slice_checks = predecessor_checks = mixed_checks = 0
    for A, a, B, b in ((1, 0, 5, 0), (3, 2, 11, 5), (5, 7, 13, 2)):
        for t in (4, 6, 8, 10):
            cells = Counter()
            for n in range(2**t):
                x, xg = records(A*n+a, t)
                y, yg = records(B*n+b, t)
                mixed = sum((u-v) % 2 for u,v in zip(x[:-1], y[:-1]))
                cells[xg[-1], yg[-1], mixed] += 1
                for m in range(t):
                    xx, _ = records(A*(n+2**m)+a, m)
                    yy, _ = records(B*(n+2**m)+b, m)
                    require((xx[-1]-yy[-1]-x[m]+y[m]) % 2 == 0,
                            'disagreement must be predictable')
                    require((xx[-1]-x[m]) % 2 == 1, 'complementary first parity')
                    mixed_checks += 1
            for k in range(t+1):
                mass = sum(v for (i,j,h),v in cells.items() if i == k)
                require(mass == comb(t,k),'exact grade slice cardinality')
                for p in (Fraction(1,3),Fraction(2,3),Fraction(3,4)):
                    word_mass = p**k*(1-p)**(t-k)
                    for (i,j,h),v in cells.items():
                        if i == k:
                            conditional = word_mass*v/(comb(t,k)*word_mass)
                            require(conditional == Fraction(v, mass),'tilted disintegration')
                            slice_checks += 1
                    predecessor_checks += mass
    return {'conditional_slice_cells':slice_checks,'weighted_source_occurrences':predecessor_checks,
            'native_predictability_tests':mixed_checks}


if __name__ == '__main__':
    print(json.dumps({**deadline_controls(),**tilt_controls()},indent=2,sort_keys=True))
