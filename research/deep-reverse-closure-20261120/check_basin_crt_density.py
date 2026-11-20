#!/usr/bin/env python3
"""Exact finite formula audit for the elementary basin CRT-density lemma."""
import argparse
import hashlib
import json
from functools import lru_cache
from pathlib import Path


def need(test, message):
    if not test:
        raise ValueError(message)


def shortcut(n):
    return (3*n+1)//2 if n%2 else n//2


@lru_cache(None)
def log_table(m):
    modulus=3**m
    period=2*3**(m-1)
    result={}
    x=1
    for j in range(period):
        need(x not in result,'power of two repeated before the claimed order')
        result[x]=j
        x=2*x%modulus
    need(x==1 and len(result)==period,'wrong order of two')
    need(all(x%3 for x in result),'nonunit in power table')
    return modulus,period,result


def construct(a,b,r):
    w=r%(2**a) or 2**a
    L=a+1
    current=w
    bits=[]
    for _ in range(L):
        bits.append(current%2)
        current=shortcut(current)
    q=sum(bits)
    B=2**L*current-3**q*w
    need(q>=1 and B>0 and B%3!=0,'wrong affine prefix constant')
    modulus,period,logs=log_table(q+b)
    target=(B+3**q*r)%modulus
    need(target in logs,'target not a ternary unit')
    A=(logs[target]-L)%period
    while A<L or 2**(L+A)<=B:
        A+=period
    numerator=2**(L+A)-B
    need(numerator%3**q==0,'source is not integral')
    n=numerator//3**q
    need(n>0 and n%(2**a*3**b)==r%(2**a*3**b),'wrong source residue')
    current=n
    actual=[]
    for _ in range(L):
        actual.append(current%2)
        current=shortcut(current)
    need(actual==bits and current==2**A,'wrong literal source certificate')
    need(current>>A==1 and current&(current-1)==0,'terminal value not a power of two')
    # A second progression member checks the infinite-family step independently.
    next_n=(2**(L+A+period)-B)//3**q
    need(next_n>n and next_n%(2**a*3**b)==r%(2**a*3**b),'wrong infinite-family step')
    next_current=next_n
    for _ in range(L):
        next_current=shortcut(next_current)
    need(next_current==2**(A+period),'wrong next-member endpoint')
    return {'a':a,'b':b,'r':r,'q':q,'B':B,'A':A,'period':period,
            'source_bits':n.bit_length(),'next_source_bits':next_n.bit_length()}


def run():
    rows=[]
    for a in range(5):
        for b in range(4):
            for r in range(2**a*3**b):
                rows.append(construct(a,b,r))
    canonical=json.dumps(rows,sort_keys=True,separators=(',',':'))
    return {'status':'PASS','scope':'finite audit of an elementary all-parameter construction',
            'progressions':len(rows),'certified_sources':2*len(rows),
            'max_source_bits':max(x['next_source_bits'] for x in rows),
            'max_prefix_odd_inputs':max(x['q'] for x in rows),
            'rows_sha256':hashlib.sha256(canonical.encode()).hexdigest()}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=json.dumps(run(),sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(result,encoding='utf-8')
    else:print(result,end='')
