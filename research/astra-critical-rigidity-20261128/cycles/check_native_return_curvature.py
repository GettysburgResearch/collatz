"""Exact finite controls on native ordinary and complete-denominator runs."""

import json
from fractions import Fraction
from math import gcd


def require(condition, description):
    if not condition:
        raise ArithmeticError(description)


def binary_floor(value):
    num, den = value.numerator, value.denominator
    guess = num.bit_length() - den.bit_length()
    if guess >= 0:
        return guess - (num < den << guess)
    return guess - (num << -guess < den)


def two_power(exponent):
    return Fraction(2) ** exponent


def dates_and_lift(y0, q, length):
    exponents = [0]
    nums = [y0]
    for _ in range(length - 1):
        update = 3 * nums[-1] + q
        toll = (update & -update).bit_length() - 1
        require(toll >= 1, "odd-source domain")
        exponents.append(exponents[-1] + toll)
        nums.append(update >> toll)
    for y in nums:
        require(y % 2 and gcd(y, q) == 1, "all phases keep complete denominator")
    return nums, exponents


def mechanical_numerator(tolls, q, extra=0):
    total, intercept = 0, 0
    for toll in tolls:
        intercept = 3 * intercept + (1 << total)
        total += toll
    modulus = 1 << (total + 1)
    base = ((1 << total) - q * intercept) * pow(3, -len(tolls), modulus) % modulus
    y = base + modulus * ((1 << total) * q + extra)
    while gcd(y, q) > 1:
        y += modulus
    return y, modulus


def curvature_fixture(s, h, q, length=145):
    tolls = [binary_floor(Fraction(3 ** (j + 1))) - binary_floor(Fraction(3 ** j))
             for j in range(length - 1)]
    y, _ = mechanical_numerator(tolls, q)
    nums, E = dates_and_lift(y, q, length)
    require([b - a for a, b in zip(E, E[1:])] == tolls, "realized exact calendar")
    require(len(set(nums)) == length, "distinct native dates")
    m = Fraction(min(nums), q)
    require(max(nums) < 3 * min(nums), "run confined below width three")
    L = m * Fraction(7, 4)
    V = [Fraction(num << grade, q) for num, grade in zip(nums, E)]
    F = [binary_floor(v / L) for v in V]
    H, tags, G = [], [], [v / 3 ** t for t, v in enumerate(V)]
    for t in range(length - 2 * s):
        row = [two_power(E[t + j * s] - j * h - F[t]) for j in range(3)]
        require(set(row) <= {1, 2}, "actual binary triple chart")
        tags.append(row)
        H.append(two_power(-F[t]) * (
            V[t + 2 * s] * two_power(-2 * h)
            - 2 * V[t + s] * two_power(-h) + V[t]))
    for i in range(len(H) - 1):
        a, b, c = tags[i]
        require(two_power(F[i + 1] - F[i]) * H[i + 1] == 3 * H[i] + c - 2*b + a,
                "signed recurrence from distinct genuine origins")
    gap = 3 ** s - 2 ** h
    resonant = gap * gap % q == 0
    if resonant:
        require(all(x.denominator == 1 for x in H), "complete square-resonant integrality")
        signs = {(x > 0) - (x < 0) for x in H[s:]}
        require(len(signs) == 1 and 0 not in signs, "single common strict sign")
    else:
        require(all((q*x).denominator == 1 for x in H), "scaled integer comparison")
        require(any(x.denominator > 1 for x in H), "nonresonant negative control")
    stride = Fraction(3 ** s, 2 ** h)
    interval = range(s, length-2*s)
    total = sum(two_power(F[t]) * H[t] / 3 ** t for t in interval)
    boundary = (sum(G[t+s]-G[t] for t in range(interval.stop, interval.stop + s))
                - sum(G[t+s]-G[t] for t in range(interval.start, interval.start + s)))
    expanded = (stride**2 * boundary
                + 2*stride*(stride-1)*sum(G[t+s]-G[t] for t in interval)
                + (stride-1)**2 * sum(G[t] for t in interval))
    require(total == expanded, "telescoped signed sum including both endpoint intervals")
    return {"stride": s, "h": h, "q": q, "states": length,
            "interior_origins": len(interval), "square_resonant": resonant,
            "linear_resonant": gap % q == 0, "distinct_H_denominators":
            sorted({x.denominator for x in H}),
            "interior_signs": sorted({(x > 0) - (x < 0) for x in H[s:]})}


def physical_packing_fixture():
    edge_count, fourth_offsets = 70, (0, 1, 3, 4)
    tolls = [binary_floor(Fraction(3 ** (j + 1))) - binary_floor(Fraction(3 ** j))
             for j in range(edge_count)]
    y, step = mechanical_numerator(tolls, 1)
    sources = [y+j*step for j in fourth_offsets]
    runs = [dates_and_lift(source, 1, edge_count+1) for source in sources]
    for _, E in runs:
        require([b-a for a,b in zip(E, E[1:])] == tolls, "same actual two-sided itinerary")
    require(max(max(nums) for nums, _ in runs) < 3*min(min(nums) for nums, _ in runs),
            "joint positive physical band")
    for t in range(edge_count+1):
        a,b,c,d = [nums[t] for nums, _ in runs]
        require(a < b < c < d and a+d == b+c, "four-distinct actual pair equality")
        require((d-a)*10**6 < a, "small physical spread")
    return {"center_date": edge_count//2, "left_edges": edge_count//2,
            "right_edges": edge_count//2, "nonrepeated_true_equalities": edge_count+1}


if __name__ == "__main__":
    cases = [(5, 8, 1), (5, 8, 13**2), (5, 8, 17), (12, 19, 1), (12, 19, 7153**2)]
    print(json.dumps({"native_runs": [curvature_fixture(*case) for case in cases],
                      "transported_positive_quartet": physical_packing_fixture()},
                     sort_keys=True, indent=2))
