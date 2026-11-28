"""Exact finite checks for reduced denominators of actual prefix closures."""

from fractions import Fraction
from functools import cache
from math import gcd, lcm
import json


def require(condition):
    if not condition:
        raise ArithmeticError("prefix-closure control failed")


def step(x):
    bit = x.numerator % 2
    return ((3 * x + 1) / 2 if bit else x / 2), bit


@cache
def orders(q):
    two_powers, v = {1}, 2 % q
    while v not in two_powers:
        two_powers.add(v)
        v = 2 * v % q
    require(v == 1)
    three_order, v = 1, 3 % q
    while v != 1:
        three_order += 1
        v = 3 * v % q
    coset_order, v = 1, 3 % q
    while v not in two_powers:
        coset_order += 1
        v = 3 * v % q
    group = set(two_powers)
    frontier = list(two_powers)
    while frontier:
        v = 3 * frontier.pop() % q
        if v not in group:
            group.add(v)
            frontier.append(v)
    require(len(group) == len(two_powers) * coset_order)
    return three_order, len(group)


def visit(source, horizon, totals):
    x, grade, carry = source, 0, 0
    departures, bits, denominators, grades = [], [], [1], [0]
    repeated, seen = False, set()

    for t in range(1, horizon + 1):
        repeated |= x in seen
        seen.add(x)
        departures.append(x)
        bit = x % 2
        bits.append(bit)
        if bit:
            carry = 3 * carry + (1 << (t - 1))
        grade += bit
        x = ((1 + 2 * bit) * x + bit) // 2
        delta = (1 << t) - 3**grade
        center = Fraction(carry, delta)
        q = center.denominator
        require(q == abs(delta) // gcd(abs(delta), x - source))
        require((center.numerator - q * source) % (1 << t) == 0)
        if grade:
            require(gcd(6, q) == 1 and center.numerator % 3)
        now = center
        for expected in bits:
            now, actual = step(now)
            require(expected == actual)
        require(now == center)
        totals["closed_prefixes"] += 1
        totals["rational_departures"] += t
        totals["negative_centers"] += center < 0
        totals["proper_reduced_gcds"] += 1 < q < abs(delta)

        scale = max(departures) if repeated else source
        if x == source:
            totals["physical_returns"] += 1
            require(center == source and q == 1)
        else:
            totals["nonreturns_after_repetition"] += repeated
            require(q * 4800 * scale * t**14 >= (1 << t))
        for k in range(1, t):
            shared = gcd(q, denominators[k])
            gap_det = abs((1 << (t - k)) - 3**(grade - grades[k]))
            require(gap_det % shared == 0)
            require(shared <= 3**min(k, t-k))
            totals["overlap_pairs"] += 1
            totals["nontrivial_overlap_gcds"] += shared > 1
            if k == t - 1:
                require(shared == 1)
        denominators.append(q)
        grades.append(grade)
        if 1 < q <= 1000:
            three_order, size = orders(q)
            require(pow(3, three_order, q) == 1 and size % three_order == 0)
            totals["small_modulus_group_checks"] += 1

    for n in (8, 16, 32, 49):
        m = int(n**0.5)
        block = denominators[n:n+m]
        common = lcm(*block)
        prod, gcdprod = 1, 1
        for i, q in enumerate(block):
            prod *= q
            for other in block[:i]:
                gcdprod *= gcd(q, other)
        require(common * gcdprod >= prod)
        require(gcdprod <= 3**((m**3-m)//6))
        totals["lcm_bands"] += 1


def main():
    totals = dict.fromkeys(("closed_prefixes", "rational_departures",
                           "negative_centers", "proper_reduced_gcds",
                           "physical_returns", "nonreturns_after_repetition",
                           "overlap_pairs", "nontrivial_overlap_gcds",
                           "small_modulus_group_checks", "lcm_bands"), 0)
    for n in (*range(1, 129), 703, 871, 6171, 837799):
        visit(n, 72, totals)
    print(json.dumps(totals, sort_keys=True))


if __name__ == "__main__":
    main()

