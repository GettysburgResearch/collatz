"""Replay all-origin averaging, fiber joins and the two pressure-window unions."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, prod
import json

from check_rotation_occupation import lifted, primitive_necklace, require


def all_origins(word, q, states, lag, counts):
    p = len(word)
    flag = [a != word[(i+lag) % p] for i, a in enumerate(word)]
    s = sum(flag)
    source = [max(states[i], states[(i+lag) % p])+q for i in range(p)]
    terminal = [min(states[i], states[(i+lag) % p])+q for i in range(p)]
    for length in sorted({1, 2, p-1, p, p+3, 2*p+1}):
        budget = [sum(flag[(i+j) % p] for j in range(length)) for i in range(p)]
        require(sum(budget) == length*s, "all odd origins count true mismatches")
        payments = [source[i]*terminal[(i+length) % p] for i in range(p)]
        require(prod(payments) == prod(y+q for y in states)**2,
                "all-origin exact physical endpoint sum")
        require(all(2**length*terminal[(i+length) % p] <= 3**length*terminal[i]
                    for i in range(p)), "the smaller trajectory height grows at most 3/2")
        counts["all_origin_lengths"] += 1
        counts["lengths_longer_than_a_full_lap"] += length > p
        for m in sorted({0, 1, 2, max(budget), (length*s+p-1)//p}):
            good = [i for i in range(p) if budget[i] <= m]
            require((p-len(good))*(m+1) <= length*s, "Markov bound at a fixed local budget")
            if good:
                require(min(payments[i] for i in good)**len(good) <= prod(payments),
                        "an actual good origin has the claimed endpoint-cost bound")
            counts["threshold_and_good_origin_ledgers"] += 1


def grade_cost(y, m):
    grade = 0
    while (2**(grade+1))*m <= y:
        grade += 1
    return Fraction((2**grade-1)*m, y)


def join_windows(word, q, states, lag, counts):
    p = len(word)
    d = gcd(lag, p)
    mins = [min(range(r, p, d), key=lambda i: states[i]) for r in range(d)]
    z = [states[i] for i in mins]
    joins = [r for r in range(d) if (mins[r]+1) % p != mins[(r+1) % d]]
    mark_count = sum(a != word[(i+lag) % p] for i, a in enumerate(word))
    require(2*len(joins) <= mark_count, "actual switches of the minimum")
    D = [grade_cost(y, min(states)) for y in states]
    u = Fraction(1, 40)
    for n in sorted({1, min(2, d), min(3, d)}):
        original_bad = {i for i in range(p) if sum(D[(i+j) % p] for j in range(n)) <= n*u}
        for Y in sorted({min(z), max(z), (min(z)+max(z))//2}):
            low = [r for r in joins if z[r] <= Y]
            high = [r for r in joins if z[r] > Y]
            F = {(r+j) % d for r in low for j in range(1, n+1)}
            B = {(r-j) % d for r in low for j in range(n)}
            E = {(r-j) % d for r in high for j in range(n)}
            expanded = {(r-j) % d for r in E for j in range(n)}
            require(F == {(r+n) % d for r in B}, "low switch forward/backward sets translate")
            require(len(expanded) <= 2*len(E), "enlarging high buffers costs at most twice")
            for r in F:
                low_count = sum((states[i]+q)*2**n <= (Y+q)*3**n for i in range(r, p, d))
                require(low_count >= 2, "two actual low-track successors throughout forward buffer")
            for r in E:
                require((z[r]+q)*3**n > (Y+q)*2**n, "every high backwards-buffer date is high")
            remaining = set(range(d)) - B - expanded
            valid = [r for r in remaining if mins[r] not in original_bad]
            for r in remaining:
                require(all(mins[(r+j) % d] == (mins[r]+j) % p for j in range(n)),
                        "retained window follows one actual positive rational trajectory")
                require(all((r+j) % d not in E for j in range(n)), "cost disjoint from E")
            require(sum(D[mins[r]] for r in range(d) if r not in E) >= u*len(valid),
                    "summed retained windows charge only the complement")
            floor_cost = min((D[mins[r]] for r in E), default=Fraction(0))
            lower = u*(d-2*len(E)-len(B)-len(original_bad)) + floor_cost*len(E)
            require(sum(D[i] for i in mins) >= lower, "exact finite low/high pressure ledger")
            counts["join_buffer_ledgers"] += 1
            counts["nonempty_high_buffers"] += bool(E)
            counts["nonempty_low_buffers"] += bool(B)
            counts["positive_retained_pressure_windows"] += len(valid)


def main():
    counts = Counter()
    for p in range(2, 9):
        alphabet = (1, 2, 3) if p <= 7 else (1, 2)
        for word in product(alphabet, repeat=p):
            if not primitive_necklace(word):
                continue
            src = lifted(word)
            if src is None:
                continue
            q, states = src
            counts["genuine_rational_cycles"] += 1
            for lag in range(1, p):
                all_origins(word, q, states, lag, counts)
                join_windows(word, q, states, lag, counts)
    require(len(counts) == 8 and all(counts.values()), "all calibration cases occurred")
    return counts


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
