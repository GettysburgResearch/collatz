"""Exact finite controls for strict centered-carry losses on positive odd trajectories."""
from fractions import Fraction
from functools import cache
import json


def check(condition, label):
    if not condition:
        raise ArithmeticError(label)


def step(q):
    numerator = 3 * q + 1
    gap = (numerator & -numerator).bit_length() - 1
    return gap, numerator >> gap


@cache
def scalar(q):
    if q == 1:
        return Fraction(1)
    gap, endpoint = step(q)
    return (gap + scalar(endpoint)) / 3


def carry(q):
    y = scalar(q) - Fraction(1, 2)
    return (y.numerator - 1) // y.denominator


def canonical(q):
    phase = scalar(q) - carry(q)
    x = 3 * (phase - Fraction(1, 2))
    return -(-x.numerator // x.denominator)


def slack(c, d):
    return Fraction(3) ** (3*c - d) * Fraction(d + 1, c + 1) ** 2


def local_bound(k):
    m = max(0, -(-k // 3))
    return Fraction(3) ** k * Fraction(3*m-k+1, m+1) ** 2


def run():
    local_edges = 0
    for c in range(129):
        for d in range(3*c + 3):
            r = slack(c, d)
            k = 3*c - d
            lower = local_bound(k)
            strict = not (c == d == 0 or d == 3*c + 2)
            check(lower <= r and (r > 1) == strict, (c, d))
            check(not strict or r >= Fraction(4, 3), (c, d))
            check(k < 1 or r >= Fraction(27, 4), (c, d))
            local_edges += 1
    prefixes = 0
    witnesses = {}
    for start in range(1, 2048, 2):
        q = start
        a_sum = b_sum = strict_count = debit_count = 0
        c0 = carry(q)
        while q != 1:
            a, destination = step(q)
            b = canonical(q)
            c, d = carry(q), carry(destination)
            check(a + d == b + 3*c, q)
            r = slack(c, d)
            if r in (Fraction(4, 3), Fraction(27, 4)):
                witnesses.setdefault(str(r), [q, destination, a, b, c, d])
            strict_count += r != 1
            debit_count += a > b
            a_sum += a
            b_sum += b
            bound = Fraction(4, 3) ** (strict_count-debit_count) * Fraction(27, 4) ** debit_count
            product = Fraction(3) ** (a_sum - b_sum) * Fraction(d+1, c0+1)**2
            check(product >= bound, (start, destination))
            q = destination
            prefixes += 1
    check(set(witnesses) == {"4/3", "27/4"}, witnesses)
    return {"local_edges": local_edges, "largest_initial_carry": 128,
            "positive_odd_starts": 1024, "largest_start": 2047,
            "ordinary_prefixes": prefixes, "sharp_witnesses_q_r_a_b_c_d": witnesses}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
