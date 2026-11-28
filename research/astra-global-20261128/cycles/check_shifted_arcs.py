"""Exact controls for endpoint transport and common-shift crossings."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, isqrt
import json


def require(claim, message):
    if not claim:
        raise ValueError(message)


def primitive_circle(word):
    h, p = len(word), sum(word)
    denominator = 2**h - 3**p
    if p == 0 or denominator <= 0:
        return None
    if any(word[i:]+word[:i] <= word for i in range(1,h)):
        return None
    first = 0
    for i, bit in enumerate(word):
        first = 3**bit*first + bit*2**i
    states = []
    x = first
    for bit in word:
        states.append(x)
        require(x % 2 == bit, "native rational parity")
        x = (3**bit*x + bit*denominator) // 2
    require(x == first and len(set(states)) == h, "primitive positive circle")
    return states, denominator


def crosses(left, right):
    return (left <= 0 <= right) or (right <= 0 <= left)


def check_circle(word, states, denominator, counts):
    h, p = len(word), sum(word)
    counts["primitive_positive_rational_circles"] += 1
    if gcd(h,p) == 1:
        counts["coprime_native_clocks"] += 1
    for r in range(1,h):
        odd_counts = [sum(word[(i+k)%h] for k in range(r)) for i in range(h)]
        endpoints = []
        for shift_denominator in (4,2):
            marks = [shift_denominator*x+denominator for x in states]
            values = [(marks[(i+r)%h], 3**odd_counts[i]*marks[i]) for i in range(h)]
            endpoints.append(values)
        left, right = endpoints
        for i,(a,b) in enumerate(right):
            c,d = left[(i+1)%h]
            require(a*d == b*c, "equal arc loss after endpoint rotation")
        counts["endpoint_transport_comparisons"] += h
        mean_signs = [a**h * 3**(r*p) - b**h for a,b in left]
        require(any(crosses(mean_signs[i],mean_signs[(i+1)%h]) for i in range(h)),
                "single-arc common shift")
        counts["single_arc_filters"] += 1
        for s in range(1,h):
            signs = []
            for i, (a,b) in enumerate(left):
                c,d = left[(i+s)%h]
                signs.append(a*d-b*c)
            candidates = [i for i in range(h) if crosses(signs[i],signs[(i+1)%h])]
            require(candidates, "paired-arc common shift")
            counts["paired_arc_filters"] += 1
            if gcd(h,p) == 1:
                counts["coprime_paired_arc_filters"] += 1
            for i in candidates:
                j = (i+s)%h
                if odd_counts[i] != odd_counts[j]:
                    continue
                a,b = states[(i+r)%h],states[j]
                c,d = states[i],states[(j+r)%h]
                linear = denominator*(a+b-c-d)
                require(linear != 0, "nonvanishing equal-count polynomial")
                root = Fraction(c*d-a*b,linear)
                require(Fraction(1,4) <= root <= Fraction(1,2), "exact linear root")
                counts["equal_count_crossing_witnesses"] += 1


def equal_count_counterexample():
    word = (0,0,0,0,1,1,1)
    states, denominator = primitive_circle(word)
    r, s = 2, 3
    counts = [sum(word[(i+k)%len(word)] for k in range(r)) for i in range(len(word))]
    roots = []
    for i in range(len(word)):
        j = (i+s)%len(word)
        if counts[i] == counts[j]:
            a,b = states[(i+r)%len(word)],states[j]
            c,d = states[i],states[(j+r)%len(word)]
            roots.append(Fraction(c*d-a*b,denominator*(a+b-c-d)))
    require(roots == [Fraction(-75,58)], "four-distinct-endpoint counterexample")
    return {"numerators":states,"denominator":denominator,"clock":[7,3],
            "arc_length":r,"lag":s,"equal_count_roots":[str(q) for q in roots]}


def integer_crossings():
    count = 0
    polynomials = set()
    for odd in range(1,200,2):
        for even in range(odd+1,3*odd+1,2):
            linear = even+3*odd-1
            discriminant = linear**2+16*even
            require(isqrt(discriminant)**2 != discriminant, "quadratic irrationality")
            require(3*(odd-even) < 0 < 3*odd+1-even, "interior crossing")
            require((linear,-even) not in polynomials, "distinct primitive roots")
            polynomials.add((linear,-even))
            count += 1
    return count


def main():
    counts = Counter()
    for h in range(2,12):
        for word in product(range(2),repeat=h):
            circle = primitive_circle(word)
            if circle is not None:
                check_circle(word,*circle,counts)
    print(json.dumps({"exhaustive_shortcut_periods_through":11,
                      "finite_rational_controls":counts,
                      "noncycle_integer_crossing_checks":integer_crossings(),
                      "equal_count_counterexample":equal_count_counterexample(),
                      "scope":"Exact finite controls. Rational circles may have denominator greater than one."},
                     indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
