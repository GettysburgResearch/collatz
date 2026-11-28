"""Exhaust the physical endpoints underlying (2) and (3) at small sources.

No asymptotic logarithm bound or conclusion about future visits is assumed.
"""
from collections import defaultdict
from math import gcd
import json


def remove_twos(x):
    exponent = (x & -x).bit_length() - 1
    return exponent, x >> exponent


def step(x):
    return x // 2 if x % 2 == 0 else (3*x + 1) // 2


def check(limit=1024, deadline=128):
    targets = defaultdict(list)
    for upper in range(1, limit+1):
        max_p, _ = remove_twos(upper+1)
        y = upper
        for i in range(max_p+1):
            for p in range(max(1, i), max_p+1):
                a = (upper+1) >> p
                if a % 3:
                    targets[y].append((upper, p, a, i))
            y = step(y)
    counts = defaultdict(int)
    witnesses = {}
    for x in range(1, limit):
        n, b = remove_twos(x+1)
        y, q, carry = x, 0, 0
        for h in range(deadline+1):
            for upper, p, a, i in targets[y]:
                if x >= upper:
                    continue
                if h <= n:
                    raise AssertionError(("precrest meeting", x, upper, i, h))
                j = h-n
                z = 2**(p-i+j) * 3**i * a
                if not (z == 3**(n+q)*b + carry and y+1 == (z >> j)):
                    raise AssertionError(("shifted identity", x, upper, i, h))
                if not 0 < carry <= 3**q*(2**(j-q)-1):
                    raise AssertionError(("normalized carry", x, upper, i, h))
                # B_j/Z < (3/2)^(q-i)/(U+1), keeping q-i signed.
                if not carry * (upper+1) * 2**q * 3**i < z * 3**q * 2**i:
                    raise AssertionError(("relative bound", x, upper, i, h))
                if not n+q > i:
                    raise AssertionError(("total odd surplus", x, upper, i, h))
                counts["all_visits"] += 1
                g = gcd(a,b)
                c, d = a//g, b//g
                labels = []
                if n == 0:
                    labels.append("even_lower")
                if a % 5 == 0:
                    labels.append("upper_divisible_by_five")
                if c > 1 and d > 1:
                    labels.append("ratio_with_nontrivial_reduced_numerator_and_denominator")
                if a % 2 == 0:
                    labels.append("nonmaximal_upper_ramp")
                if q < i:
                    labels.append("negative_postcrest_surplus")
                if a == 1 and b == 1:
                    labels.append("two_mersennes")
                for label in labels:
                    counts[label] += 1
                    witnesses.setdefault(label, dict(x=x, upper=upper, p=p, a=a,
                                                     n=n, b=b, upper_clock=i,
                                                     lower_clock=h, postcrest_odds=q))
            if h >= n:
                j = h-n
                if y % 2:
                    q += 1
                    carry *= 3
                else:
                    carry += 2**j
            y = step(y)
    required = ["even_lower", "upper_divisible_by_five",
                "ratio_with_nontrivial_reduced_numerator_and_denominator",
                "nonmaximal_upper_ramp", "negative_postcrest_surplus"]
    if any(counts[label] == 0 for label in required):
        raise AssertionError(("missing strata", dict(counts)))
    return dict(limit=limit, deadline=deadline, counts=counts, first_examples=witnesses)


if __name__ == "__main__":
    print(json.dumps(check(), indent=2, sort_keys=True))
