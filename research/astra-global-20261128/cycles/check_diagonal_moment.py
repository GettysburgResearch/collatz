"""Exact return-atom and cycle-moment controls."""

from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json


def require(test, message):
    if not test:
        raise ValueError(message)


def native_returns():
    counts = Counter()
    largest_depth = 12
    weighted = [Q(0)]*(largest_depth+1)
    for start in range(1, 10001, 2):
        if start % 3 == 0:
            continue
        y = start
        total = 0
        A = Q(1)
        for d in range(1, largest_depth+1):
            value = 3*y + 1
            e = (value & -value).bit_length() - 1
            y = value >> e
            total += e
            A *= Q(3,2**e)
            B = A*Q(start,y)
            # A pure-slope atom must have odd part of the dyadic numerator
            # equal to 3^d. The normalized fraction is already reduced.
            pure = B.numerator == 3**d and B.denominator.bit_count() == 1
            require(pure == (start == y), "pure-slope atom equals a true return")
            counts["ordinary_native_paths"] += 1
            if pure:
                require(B.denominator == 2**total and Q(3**d,2**total) == A,
                        "exact total clock")
                weighted[d] += Q(start%3, y*(3*y+1))*A
                counts["ordinary_diagonal_atoms"] += 1
    for d in range(1, largest_depth+1):
        require(weighted[d] == Q(1,4)*Q(3,4)**d, "known cycle contribution")
    partial = sum(d*weighted[d] for d in range(1,largest_depth+1))
    lam = Q(3,4)
    tail = Q(1,4)*lam**(largest_depth+1)*(largest_depth+1-largest_depth*lam)/(1-lam)**2
    require(partial+tail == 3, "exact known-cycle moment")
    counts["ordinary_sources_through"] = 10000
    counts["maximum_odd_depth"] = largest_depth
    return counts


def rational_lap_checks():
    counts = Counter()
    for p in range(1,6):
        for word in product(range(1,5),repeat=p):
            rotations = [word[j:]+word[:j] for j in range(p)]
            if word != min(rotations) or len(set(rotations)) < p:
                continue
            h = sum(word)
            if 2**h <= 3**p:
                continue
            carry = elapsed = 0
            for e in word:
                carry = 3*carry+2**elapsed
                elapsed += e
            initial = Q(carry,2**h-3**p)
            sites,selectors = [],[]
            x = initial
            for e in word:
                sites.append(x)
                x = (3*x+1)/2**e
                # In Z/3, reduce numerator times inverse denominator.
                selectors.append(x.numerator*pow(x.denominator,-1,3) % 3)
                require(selectors[-1] == (2 if e%2 else 1), "native odd-gap selector")
            require(x == initial, "primitive rational loop")
            require(sum(1/Q(v) for v in selectors) <= Q(h,2), "physical residue improvement")
            for y in sites:
                w = 3*y/(3*y+1)
                require(1/(y*(3*y+1)) == 3*(1-w)**2/w, "exact weight kernel")
            counts["rational_selector_tests"] += p
            counts["rational_test_cycles"] += 1
    return counts


def main():
    require(Q(3001,1000)**100 < 2**159, "high-minimum clock")
    require(Q(600,159)*(1-Q(3,250)**2)**2 > Q(15,4), "single-cycle gap")
    print(json.dumps({
        "integer_return_atoms": native_returns(),
        "rational_algebra": rational_lap_checks(),
        "known_cycle_exact_first_moment": 3,
        "strict_extra_cycle_lower_bound": "15/4",
        "scope": "Finite arithmetic controls; they do not sum the full unknown return trace."
    },indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
