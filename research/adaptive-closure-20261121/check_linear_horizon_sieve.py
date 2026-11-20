#!/usr/bin/env python3
"""Exact first-crossing checks and bounded linear-horizon census."""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def need(ok, why):
    if not ok:
        raise ValueError(why)


def step(n):
    need(type(n) is int and n > 0, 'ordinary positive integer')
    return (3*n+1)//2 if n % 2 else n//2


def first_crossing(n, B, horizon):
    need(type(n) is int and n > 0, 'ordinary positive source')
    need(type(B) is int and B > 0, 'positive integer barrier')
    need(type(horizon) is int and horizon >= 0, 'nonnegative integer horizon')
    current, count, power3, power2 = n, 0, 1, 1
    for i in range(1, horizon+1):
        odd = current % 2
        count += odd
        if odd:
            power3 *= 3
        power2 *= 2
        current = (3*current+1)//2 if odd else current//2
        if (power3 << B) < power2:
            return {'source':n,'B':B,'clock':i,'odd_count':count,'endpoint':current}
    return None


def verify_crossing(row):
    n, B, clock = row['source'], row['B'], row['clock']
    actual = first_crossing(n, B, clock)
    need(actual is not None and actual == row, 'exact first-crossing witness')
    b, endpoint = row['odd_count'], row['endpoint']
    need(3*(1 << B)*endpoint < 3*n+(1 << B)*b, 'first-crossing affine bound')
    need(3*b < 2*clock, 'odd count below two thirds')


def census(limit):
    counts = {'eligible_indices':0,'old_discarded':0,'new_discarded':0,
              'discarded_by_both':0,'additional_new_discards':0,'retained_by_conjunction':0}
    examples, fixture = [], []
    for k in range(1, limit+1):
        if k % 4 == 0:
            continue
        counts['eligible_indices'] += 1
        n = 27*k+1
        old = first_crossing(n, 16, k.bit_length()-1)
        new = first_crossing(n, 17, k//1024)
        counts['old_discarded'] += int(old is not None)
        counts['new_discarded'] += int(new is not None)
        counts['discarded_by_both'] += int(old is not None and new is not None)
        counts['additional_new_discards'] += int(old is None and new is not None)
        counts['retained_by_conjunction'] += int(old is None and new is None)
        if new is not None:
            # No second trajectory replay is needed for every finite source:
            # first_crossing has literally generated its first witness.
            need(3*(1 << 17)*new['endpoint'] < 3*n+(1 << 17)*new['odd_count'],
                 'census first-crossing bound')
            need(176106*new['endpoint'] < 76*k, 'all-source height bound')
            need(8*176106*new['endpoint'] < 5*(128*k+1), 'smaller antecedent guard')
            if old is None and len(examples) < 12:
                examples.append({'index':k,**new})
            fixture.append((k,new['clock'],new['odd_count'],new['endpoint']))
    return counts, examples, hashlib.sha256(repr(fixture).encode()).hexdigest()


def run(limit):
    coefficient=176106*(Fraction(28,131072)+Fraction(2,9*1024))
    need(coefficient < 76, 'rational all-k inequality')
    firsts=[]
    for n in range(1,2049):
        for B in (1,2,5,9):
            row=first_crossing(n,B,600)
            if row is not None:
                verify_crossing(row)
                if len(firsts)<4:firsts.append(row)
    counts,examples,fixture=census(limit)
    rejected=0
    bad=copy.deepcopy(firsts[0]);bad['endpoint']+=1
    later=copy.deepcopy(firsts[0]);later['clock']+=1
    controls=[lambda:verify_crossing(bad),lambda:verify_crossing(later),
              lambda:first_crossing(True,17,50),lambda:first_crossing(1,17.0,50),
              lambda:first_crossing(1,17,-1)]
    for f in controls:
        try:f()
        except ValueError:rejected+=1
        else:raise ValueError('malformed control accepted')
    return {'status':'PASS','limit':limit,'counts':counts,'additional_discard_examples':examples,
            'exact_height_coefficient':str(coefficient),'fixture_sha256':fixture,
            'rejected_controls':rejected,
            'scope':'Exact bounded ordinary census and first-crossing inequalities; no new asymptotic count or universal convergence claim.',
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--limit',type=int,default=262144)
    p.add_argument('--output',type=Path)
    a=p.parse_args()
    need(a.limit>=1,'positive census limit')
    result=json.dumps(run(a.limit),indent=2,sort_keys=True)+'\n'
    if a.output:a.output.write_text(result,encoding='utf-8')
    print(result,end='')
