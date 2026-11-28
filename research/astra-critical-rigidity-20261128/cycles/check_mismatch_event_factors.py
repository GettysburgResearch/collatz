"""Exact physical gcd, weighted arc overlap, and reduced-denominator rank controls."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, prod
import json

from check_rotation_occupation import lifted, primitive_necklace, require


def factors(value):
    result = {}
    prime = 2
    while prime * prime <= value:
        while value % prime == 0:
            result[prime] = result.get(prime, 0) + 1
            value //= prime
        prime = prime + 1 if prime == 2 else prime + 2
    if value > 1:
        result[value] = 1
    return result


def valuation_rank(rows):
    basis = {}
    for row in rows:
        row = {p: Fraction(e) for p, e in row.items()}
        for p in sorted(basis):
            if p in row:
                coefficient = row[p]
                for v, e in basis[p].items():
                    row[v] = row.get(v, 0) - coefficient * e
                row = {v: e for v, e in row.items() if e}
        if row:
            pivot = min(row)
            basis[pivot] = {v: e / row[pivot] for v, e in row.items()}
    return len(basis)


def actual_pair_cost(y, q, word, cyclic, counts):
    date = [Fraction(1)]
    last = len(word) if cyclic else len(y) - 1
    for i in range(last):
        z = y[(i+1) % len(y)]
        a = word[i]
        require(2**a*z == 3*y[i]+q, "genuine scaled odd transition")
        edge = Fraction((3*y[i]+q)*2**(a-1), y[i])
        require(max(Fraction(y[i], z), Fraction(z, y[i])) <= edge,
                "two-sided physical numerator Lipschitz bound")
        date.append(date[-1]*edge)
    for i in range(len(y)):
        z = y[i]
        carry, native_clock, cost = 0, 0, 1
        stop = len(y) if cyclic else last-i
        for d in range(1, stop+1):
            a = word[(i+d-1) % len(word)]
            carry = 3*carry + 2**native_clock
            native_clock += a
            z = y[(i+d) % len(y)]
            cost *= 3*2**(a-1)
            require(2**native_clock*z-3**d*y[i] == q*carry,
                    "full actual pair numerator identity")
            require(carry % gcd(y[i], z) == 0 and carry < cost,
                    "reduction removes the entire q from the gcd bound")
            counts["physical_pair_gcd_returns"] += 1
    if cyclic:
        require(date[-1] == 2**(2*sum(word)-len(word)), "full rational cost")
    return date


def max_overlap(intervals):
    events = []
    for left, right in intervals:
        events.extend(((left, 0), (right, 1)))
    active = maximum = 0
    for _, kind in sorted(events):
        active += 1 if kind == 0 else -1
        maximum = max(maximum, active)
    return maximum


def verify_filtered(y, u, rank, chosen, date, cyclic, counts):
    for m, n in ((1, 1), (1, 2), (2, 3)):
        scale = n*(rank+2)
        selected = [i for i in chosen if y[i] > 1 and u[i]**n >= y[i]**m]
        require(all(y[i] % u[i] == 0 for i in chosen), "chosen genuine divisors")
        intervals = []
        circle = date[-1]**scale
        for i in selected:
            end = date[i]**scale
            start = end/y[i]**m
            if cyclic and start < 1:
                intervals.extend(((start*circle, circle), (Fraction(1), end)))
                counts["intervals_wrapping_true_cyclic_seam"] += 1
            else:
                intervals.append((start, end))
        overlap = max_overlap(intervals)
        require(overlap <= rank, "actual interval overlap respects multiplicative rank")
        counts["filtered_rank_systems"] += 1
        counts["systems_attaining_overlap_at_least_two"] += overlap >= 2
        counts["positive_rank_zero_controls"] += rank == 0 and bool(chosen)
        total = prod(y[i] for i in selected)**m
        cap = date[-1]**(n*rank*(rank+2))
        if not cyclic:
            cap *= max(y)**(m*rank)
        require(total <= cap, "integer-power filtered-height bound")


def restricted_divisors(y, prime_factors):
    pooled = sorted(set().union(*(v.keys() for v in prime_factors)))
    for group in (pooled[:1], pooled[-2:], pooled[:3]):
        yield [prod(p**v.get(p, 0) for p in group) for v in prime_factors]
    base = next((n for n, f in zip(y, prime_factors) if len(f) >= 2), y[0])
    if base > 1:
        values = []
        for n in y:
            value = 1
            while n % (value*base) == 0:
                value *= base
            values.append(value)
        yield values
    yield [1]*len(y)


def run_path(y, word, q, cyclic, counts):
    date = actual_pair_cost(y, q, word, cyclic, counts)
    rows = [factors(n) for n in y]
    if cyclic:
        rank = valuation_rank(rows)
        p, clock = len(word), sum(word)
        require(q**p <= 2**(clock+rank*(rank+2)*(2*clock-p)),
                "complete-denominator and full numerator rank")
        require(q**p <= 2**clock*prod(y), "whole-cycle reciprocal product")
        counts["full_reduced_denominator_rank_bounds"] += 1
        counts["proper_complete_cancellations"] += 1 < q < 2**clock - 3**p
        selections = {tuple(range(p))}
        for lag in range(1, p):
            marks = tuple(i for i in range(p) if word[i-1] != word[(i+lag-1) % p])
            selections.update((marks, tuple(sorted((i+lag) % p for i in marks))))
    else:
        selections = (tuple(range(len(y))), tuple(range(1, len(y), 3)))
        counts["ordinary_open_paths"] += 1
    for divisors in {tuple(u) for u in restricted_divisors(y, rows)}:
        rank = valuation_rank([factors(u) for u in divisors])
        counts["rank_one_groups_with_composite_support"] += (
            rank == 1 and any(len(factors(u)) >= 2 for u in divisors)
        )
        for chosen in selections:
            verify_filtered(y, divisors, rank, chosen, date, cyclic, counts)


def main():
    counts = Counter()
    for p in range(2, 7):
        for word in product((1, 2, 3), repeat=p):
            if not primitive_necklace(word):
                continue
            data = lifted(word)
            if data is not None:
                q, y = data
                run_path(y, word, q, True, counts)
    for start in (27, 97, 129, 255, 447, 639, 703, 1009, 6171, 703999):
        y, word = [start], []
        for _ in range(18):
            odd_step = 3*y[-1]+1
            a = (odd_step & -odd_step).bit_length()-1
            z = odd_step >> a
            if z in y:
                break
            word.append(a)
            y.append(z)
        run_path(y, word, 1, False, counts)
    require(len(counts) == 9 and all(counts.values()), "all rank and trajectory regimes occurred")
    return counts


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
