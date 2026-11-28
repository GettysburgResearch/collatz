"""Exact native backward tag comparisons, including different rational histories."""

import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement
from math import gcd
from pathlib import Path

from check_native_return_curvature import (
    binary_floor, dates_and_lift, mechanical_numerator, require, two_power,
)


def pooled(m, r, q, depth, gap, order, divisor):
    low, high = m * q, int(m * q * r)
    by_endpoint = {}
    for start in range(low | 1, high + 1, 2):
        if gcd(start, q) > 1:
            continue
        nums, tolls = [start], [0]
        for _ in range(depth + gap - 1):
            lifted = 3 * nums[-1] + q
            grade = (lifted & -lifted).bit_length() - 1
            successor = lifted >> grade
            if not low <= successor <= high:
                break
            nums.append(successor)
            tolls.append(tolls[-1] + grade)
        else:
            by_endpoint.setdefault(nums[-1], (nums, tolls))
    bins = defaultdict(list)
    for end in by_endpoint:
        bins[(end - low) // divisor].append(end)
    outputs = defaultdict(int)
    lengths = set()
    for left, items in sorted(bins.items()):
        if len(items) < 2:
            continue
        items = sorted(items)
        count = depth + gap - 1
        # Rational J between RM/2 and 2M. All arithmetic is in numerator units.
        chart_level = Fraction(low) * (r + 4) / 4
        lower = low + left * divisor
        calendar = [binary_floor(Fraction(lower, 3 ** j) / chart_level)
                    for j in reversed(range(count + 1))]
        words, scaled = [], []
        for end in items:
            nums, tolls = by_endpoint[end]
            row = [two_power(t - tolls[-1] - f) for t, f in zip(tolls, calendar)]
            require(set(row) <= {1, 2}, 'whole actual past has binary dyadic tags')
            require(all(gcd(y, q) == 1 and y % 2 for y in nums), 'complete denominator')
            labels = [int(c) * y for c, y in zip(row, nums)]
            require(all((1 << (calendar[j+1] - calendar[j])) * labels[j+1]
                        == 3 * labels[j] + q * row[j] for j in range(count)),
                    'signed-time anchored recurrence in complete numerator units')
            words.append(tuple(int(c - 1) for c in row[-depth-1:-1]))
            scaled.append(labels[-1])
        active = [j for j in range(count) if len({
            tolls[j] - tolls[-1] - calendar[j] for _, tolls in
            (by_endpoint[end] for end in items)}) == 2]
        require(all(b - a >= gap for a, b in zip(active, active[1:])), 'actual row separation')
        # For these finite bins it is enough to dominate the observed endpoint spread.
        require(order * (max(scaled) - min(scaled)) < 3 ** depth, 'actual full ternary cutoff')
        physical_to_word, word_to_physical = {}, {}
        for indices in combinations_with_replacement(range(len(items)), order):
            physical = sum(items[j] for j in indices)
            code = tuple(sum(words[j][t] for j in indices) for t in range(depth))
            require(physical_to_word.setdefault(physical, code) == code, 'backward peeling')
            require(word_to_physical.setdefault(code, physical) == physical, 'converse full divisor')
            outputs['signed_multisets'] += 1
        outputs['bins'] += 1
        outputs['endpoints'] += len(items)
        outputs['active_rows'] += len(active)
        outputs['repeated_physical_sum_representations'] += (
            sum(1 for _ in combinations_with_replacement(items, order)) - len(physical_to_word))
        lengths.add(len(items))
        if order == 2:
            require(len(physical_to_word) ** 53 >= len(items) ** 84,
                    'exact rational exponent 84/53 below log2(3)')
    require(outputs['bins'] > 0 and outputs['active_rows'] > 0, 'nonvacuous pooled case')
    return dict(sorted(outputs.items())) | {'Q': q, 'M': m, 'R': str(r), 'h': order,
             'L': gap, 'encoded_rows': depth, 'largest_bin': max(lengths),
             'all_distinct_genuine_endpoints': len(by_endpoint)}


def sharp(q, n):
    tolls = [binary_floor(Fraction(3 ** (j+1))) - binary_floor(Fraction(3 ** j))
             for j in range(n)]
    y, modulus = mechanical_numerator(tolls, q, extra=10**6)
    runs = [dates_and_lift(y + j * q * modulus, q, n+1) for j in range(3)]
    require(all([b-a for a,b in zip(E,E[1:])] == tolls for _,E in runs), 'actual common itinerary')
    phases = [nums[-1] for nums,_ in runs]
    require(phases[2]-phases[1] == phases[1]-phases[0] == 2*q*3**n,
            'sharp exact ternary valuation of common numerator spacing')
    require(max(max(nums) for nums,_ in runs) * 32 < 65 * y, 'true common band under 65/32')
    return {'Q':q, 'n':n, 'v3_Qd':n, 'true_histories':3}


def threshold(gap):
    # The signed scalar recurrence can end at zero with |d_t|=3^L.
    # This tests only the arithmetic peeling cutoff, not physical realization of all tags.
    H = -2**(gap-1)
    for row in range(gap):
        d = 3**gap if row == gap-1 else 0
        require((3*H+d)%2 == 0,'threshold integral on all rows')
        H=(3*H+d)//2
    require(H==0, 'first allowed nonzero forcing')
    return {'L':gap,'first_allowed_abs_forcing':3**gap}


if __name__ == '__main__':
    paper = Path(__file__).with_name('POOLED_PAST_SUMSETS.md')
    data={'source_sha256':hashlib.sha256(paper.read_bytes()).hexdigest(),
          'pooled': [pooled(32768,Fraction(19,5),1,9,1,2,384),
                     pooled(8192,Fraction(3),7,8,1,2,512),
                     pooled(131072,Fraction(21,8),5,7,2,8,130)],
          'sharp': [sharp(q,n) for q in (1,5,35) for n in (1,6,17,65)],
          'scalar_threshold': [threshold(n) for n in (1,2,5)]}
    print(json.dumps(data,sort_keys=True,indent=2))
