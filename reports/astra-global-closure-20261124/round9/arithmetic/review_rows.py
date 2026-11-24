"""Independent bounded audit of the reflected exact-row bound."""

from collections import Counter
from itertools import combinations
from math import comb
import json


def guard(value, message):
    if not value:
        raise ValueError(message)


def endpoint_count_bound(b, q, num, den):
    h = 0
    while 2*3**h * den < 2**h * (den+num*q):
        h += 1
    return comb(2*b-1,b-h-1) if h < b else 0


def row(b, limit=90):
    hist, positive = Counter(), Counter()
    mod = 3**b
    inv = pow(4**b, -1, mod)
    physical = 0
    thresholds = ((1,128),(1,32),(1,8),(1,4),(1,2),(3,4))
    for cuts in combinations(range(1,2*b), b-1):
        c = 0
        prior = 0
        height = 0
        for j, stop in enumerate((*cuts,2*b),start=1):
            c = 3*c + (1 << prior)
            height = max(height,stop - 2*j)
            prior = stop
        hist[height] += 1
        guard(c * 2**height <= 4**b * (2*3**height-2**height),'carry bound')
        q0 = (c*inv) % mod
        for q in range(q0, limit+1, mod):
            if q <= 1 or q%2==0 or q%3==0:
                continue
            x = (4**b*q - c) // mod
            if x <= 0 or x%2==0 or x%3==0:
                continue
            z = x
            last = 0
            for stop in (*cuts,2*b):
                lift = 3*z+1
                gap = (lift & -lift).bit_length()-1
                guard(stop-last == gap, 'reconstructed valuation')
                z = lift >> gap
                last = stop
            guard(z == q, 'reconstructed endpoint')
            physical += 1
            for num,den in thresholds:
                if c*den >= 4**b*num*q:
                    positive[(q,num,den)] += 1
    for h in range(b+2):
        true = sum(v for attained,v in hist.items() if attained>=h)
        expect = comb(2*b-1,b-h-1) if h<b else 0
        guard(true == expect, 'reflection threshold')
    data = {'words':sum(hist.values()),'height_cutoffs':b+2,
            'positive_physical_rows':physical,'positive_high_carry_triples':sum(positive.values()),
            'endpoint_bounds':0}
    for q in range(3,limit+1,2):
        if q%3==0:
            continue
        for num,den in thresholds:
            guard(positive[(q,num,den)] <= endpoint_count_bound(b,q,num,den), 'finite N bound')
            data['endpoint_bounds'] += 1
    return data


if __name__ == '__main__':
    out = Counter()
    for b in range(1,11):
        out.update(row(b))
    print(json.dumps(dict(sorted(out.items())), sort_keys=True))
