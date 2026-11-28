"""Exact signed-time rectangle and convergent-cell checks for the open theorem."""
from fractions import Fraction
from itertools import combinations, product
import json
from math import gcd

from check_rational_six_sum import floor_log2


def require(condition, description):
    if not condition:
        raise ValueError(description)


def factor(s, k):
    # 2^(s*log_2(3)-k) is rational, including for negative s or k.
    return Fraction(3) ** s / Fraction(2) ** k


def convergent_case(h, q, next_h, next_q):
    require(abs(h * next_q - next_h * q) == 1 and gcd(h, q) == 1,
            "unimodular consecutive clocks")
    # Check exact upper/lower bracketing of the physical log slope.
    require(((1 << h) > 3 ** q) != ((1 << next_h) > 3 ** next_q),
            "true slope bracketing")

    radius = min(180, (q - 1) // 5)
    positions = sorted((h * s % q, s) for s in range(radius + 1))
    origin_j, origin_s = positions[len(positions) // 3]
    data = {}
    for raw_j, raw_s in positions:
        j, s = raw_j - origin_j, raw_s - origin_s
        k, rem = divmod(h * s - j, q)
        require(rem == 0, "signed grade exactly integral")
        data[j] = (s, k)

    ranks = sorted(data)
    rectangles = negative = repeated = 0
    for ix, i in enumerate(ranks):
        for j in ranks[ix + 1:]:
            for k in ranks:
                if k < j or i + (j - i) + (k - i) not in data:
                    continue
                l = j + k - i
                quadruple = (i, j, k, l)
                clocks = [data[r][0] for r in quadruple]
                grades = [data[r][1] for r in quadruple]
                require(clocks[0] + clocks[3] == clocks[1] + clocks[2] and
                        grades[0] + grades[3] == grades[1] + grades[2],
                        "true chronological and grade rectangle after lift")
                terms = [factor(s, g) for s, g in zip(clocks, grades)]
                require(terms == sorted(terms), "strict true order from convergent")
                require(terms[0] * terms[3] == terms[1] * terms[2] and
                        terms[0] + terms[3] - terms[1] - terms[2] ==
                        (terms[1] - terms[0]) * (terms[2] - terms[0]) / terms[0] > 0,
                        "exact slope-factor cancellation and curvature")
                rectangles += 1
                negative += min(clocks) < 0
                repeated += j == k
    require(rectangles and negative and repeated, "nonvacuous signed and inner-double cases")
    # Deliberate wrap control: if 4U<q is dropped, congruent times need not add exactly.
    fail_without_window = 0
    if q <= 100:
        all_data = {h * s % q: s for s in range(q)}
        for i, j, k in combinations(range(q), 3):
            l = j+k-i
            if l < q and all_data[i] + all_data[l] != all_data[j] + all_data[k]:
                fail_without_window += 1
        require(fail_without_window > 0, "necessity of signed-time range")
    return dict(q=q, next_q=next_q, rational_approximant_numerator=h,
                sampled_offsets=len(ranks), exact_rectangles=rectangles,
                with_negative_time=negative, with_repeated_inner_rank=repeated,
                unrestricted_time_wrap_failures=fail_without_window)


def actual_open():
    cases = tests = 0
    for start in range(101, 12000, 2):
        x = [start]
        E = [0]
        for _ in range(8):
            value = 3*x[-1]+1
            a = (value & -value).bit_length()-1
            E.append(E[-1]+a)
            x.append(value >> a)
        lo, hi = min(x), max(x)
        if len(set(x)) != len(x) or 2*hi > 7*lo:
            continue
        L = Fraction(15*lo, 8)
        base = 4
        F = E[base] + floor_log2(x[base]*L.denominator, L.numerator)
        for s in (-3, -2, -1, 0, 1, 2, 3):
            # All these tests use one actual finite open orbit and no period.
            k = (65*s)//41
            Z = Fraction(2)**(E[base+s]-F-k) * x[base+s]
            Z0 = Fraction(2)**(E[base]-F) * x[base]
            correction = Fraction(1)
            for t in range(min(base, base+s), max(base, base+s)):
                correction *= Fraction(3*x[t]+1, 3*x[t])
            if s < 0:
                correction = 1/correction
            require(Z/Z0 == factor(s,k)*correction, "signed open native shape identity")
            tests += 1
        cases += 1
    require(cases > 0, "genuine ordinary source cases")
    return dict(distinct_confined_eight_step_segments=cases, true_lift_ratios=tests)


if __name__ == "__main__":
    clocks = [(65, 41, 84, 53), (84, 53, 485, 306), (485, 306, 1054, 665)]
    print(json.dumps(dict(convergent_controls=[convergent_case(*a) for a in clocks],
                          ordinary=actual_open()), indent=2, sort_keys=True))
