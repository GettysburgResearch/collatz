"""Exact finite controls for inverse-word counts and marked ordinary clocks."""

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb
import json


def require(condition):
    if not condition:
        raise ValueError('finite arithmetic identity failed')


def step(x):
    return (3*x+1)//2 if x % 2 else x//2


def trace(x, length):
    bits = []
    for _ in range(length):
        bits.append(x % 2)
        x = step(x)
    return tuple(bits), x


def profile(word):
    carry = odds = 0
    for j, bit in enumerate(word):
        if bit:
            carry = 3*carry + 2**j
            odds += 1
    return odds, carry


def ordinary_cells(max_clock=14):
    words = lifts = cells = localized = 0
    for e in range(1, max_clock+1):
        grouped = defaultdict(list)
        for tail in product((0, 1), repeat=e-1):
            word = (1,) + tail
            k, carry = profile(word)
            modulus = 3**k
            a = (carry*pow(2, -e, modulus)) % modulus
            require(a % 3 and carry >= 3**(k-1))
            reversed_offset = sum(3**j * 2**(e-i) for j, i in enumerate(
                (i for i, b in enumerate(reversed(word), 1) if b)))
            require(reversed_offset == carry)
            grouped[k, a].append((word, carry))
            words += 1
        for (k, a), entries in grouped.items():
            modulus = 3**k
            for q in (a, a+modulus, a+1001*modulus):
                sources = set()
                for word, carry in entries:
                    x, remainder = divmod(2**e*q-carry, modulus)
                    require(remainder == 0 and x > 0 and x % 2)
                    require(trace(x, e) == (word, q))
                    require(x not in sources)
                    sources.add(x)
                    lifts += 1
                require(modulus*len(sources) <= 2**e*q)
                cells += 1
            for bound in (1, 2, 5, 19, 64):
                count = sum(carry <= bound*2**e for _word, carry in entries)
                require(count <= (bound*2**e)//modulus + 1)
                if count:
                    require(modulus <= 3*bound*2**e)
                    require(count*modulus <= 4*bound*2**e)
                localized += 1
    return dict(max_clock=max_clock, all_chronological_words_starting_odd=words,
                positive_integer_lifts=lifts, fixed_clock_height_counts=cells,
                localized_fiber_counts=localized)


def marked_times(x, horizon):
    y = 5*x
    odd_x = odd_y = 0
    marks = []
    for h in range(1, horizon+1):
        odd_x += x % 2
        odd_y += y % 2
        x, y = step(x), step(y)
        if x % 2 and odd_x == odd_y and 5*x == y:
            marks.append((h, x))
    return marks


def marked_clock_controls():
    horizon = 10
    modulus = 2**(horizon+1)
    cylinders = floor_tests = targets = 0
    for x in range(1, modulus, 2):
        base = marked_times(x, horizon)
        for shift in (modulus, 3*modulus):
            moved = marked_times(x+shift, horizon)
            require([h for h, _ in base] == [h for h, _ in moved])
            cylinders += 1
    for x in range(1, 4097, 2):
        if x % 3 == 0:
            continue
        marks = marked_times(x, 80)
        for j, (t, q) in enumerate(marks, 1):
            for h in (0, 3, 8, 12, 20):
                require(x <= 2**t*q)
                if x > 2**h*q:
                    require(t > h and sum(time <= h for time, _ in marks) < j)
                floor_tests += 1
            targets += 1
    partial = tuple(map(int, '1000'))
    full = tuple(map(int, '101000'))
    require(trace(49, 6) == (full, 7) and trace(245, 6)[1] == 35)
    require(marked_times(49, 6) == [(6, 7)])
    require(trace(37, 4) == (partial, 7) and trace(185, 4)[1] == 314)
    require((16*7-1)//3 == 37)
    return dict(mark_test_horizon=horizon, positive_binary_translates=cylinders,
                ordinary_starts_max=4096, physical_witness_clock_cap=80,
                observed_marks=targets, deterministic_clock_tests=floor_tests,
                partial_mark_counterexample=dict(q=7, x=37, second_endpoint=314))


def central_rows():
    targets = (1, 5, 7, 13, 19, 43, 205, 853)
    result = []
    for p in range(2, 10):
        e, count = 2*p, 0
        cells = {q: 0 for q in targets}
        for r in range(1, 2**e, 2):
            w, h = trace(r, e)
            if sum(w) != p:
                continue
            v, y = trace(5*r, e)
            if 5*h != y or sum(v) != p:
                continue
            count += 1
            c = 2**e*h-3**p*r
            for q in targets:
                x, rem = divmod(2**e*q-c, 3**p)
                if rem or x % 3 == 0:
                    continue
                require(x > 0 and x % 2 and marked_times(x, e)[-1] == (e, q))
                cells[q] += 1
        result.append(dict(odd_count=p, symbolic_words=count, ordinary_counts=cells))
    for x, q, e, p in ((647, 205, 8, 4), (3593, 853, 10, 5)):
        w, y = trace(x, e)
        require(y == q and sum(w) == p and marked_times(x, e) == [(e, q)])
    require(all(any((p-4*j) % 5 == 0 for j in range(p//4+1)) for p in range(12,16)))
    return result


def fixed_target_central_rows():
    max_odd_count = 32
    targets = (1, 5, 7)
    ceiling = max(targets)*4**max_odd_count // 3**max_odd_count
    counts = {q: [0]*max_odd_count for q in targets}
    first = {}
    for x in range(1, ceiling+1, 2):
        if x % 3 == 0:
            continue
        a, b = x, 5*x
        p = k = 0
        for t in range(1, 2*max_odd_count+1):
            p += a % 2
            k += b % 2
            a, b = step(a), step(b)
            if p == k and t == 2*p and a in counts and b == 5*a:
                require(x <= a*4**p // 3**p)
                counts[a][p-1] += 1
                first.setdefault(a, (x, t, p))
            if b in (1, 2):
                break  # No future state in this cycle is 5, 25 or 35.
    require(first == {7: (511, 30, 15), 1: (3733, 58, 29)})
    return dict(max_odd_count=max_odd_count, inclusive_ordinary_source_ceiling=ceiling,
                counts_indexed_from_one=counts, least_source_witness=first)


def dyadic_tail_controls():
    exact = Fraction(4*5**8, 8**8)
    require(3*exact < 1)
    for k in range(1, 25):
        bad = Fraction(sum(comb(8*k, j) for j in range(k)), 2**(8*k))
        require(bad <= exact**k < Fraction(1, 3**k))
    checked = 0
    for gaps in product(range(1, 11), repeat=3):
        for horizon in range(1, 16):
            require(min(horizon, sum(gaps)) <= sum(min(horizon, v) for v in gaps))
            checked += 1
    return dict(checked_binomial_cutoffs=24, exact_markov_base=str(exact),
                checked_truncated_gap_sums=checked)


if __name__ == '__main__':
    print(json.dumps(dict(ordinary=ordinary_cells(), marked=marked_clock_controls(),
                          tail=dyadic_tail_controls(), central=central_rows(),
                          fixed_target_central=fixed_target_central_rows()), indent=2))
