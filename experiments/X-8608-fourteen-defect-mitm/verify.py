#!/usr/bin/env python3
"""Independent combinatorial/window audit for X-8608."""
from __future__ import annotations
from functools import lru_cache
from math import comb
from pathlib import Path
import sys

@lru_cache(None)
def defects(n: int, total: int) -> int:
    if n == 0:
        return int(total == 0)
    return sum(defects(n - 1, total - a)
               for a in range(1, total + 1) if a != 2)

def windows():
    out=[]
    for r in range(100):
        for b in range(14,100):
            A=b+2*r; k=14+r
            if (1<<A)*7**k > 22**k:
                break
            if 3**k < (1<<A) and defects(14,b):
                out.append((r,b))
    return out

def counts():
    conceptual=left=right=0
    for r,b in windows():
        conceptual += defects(14,b)*comb(r+13,13)
        for bl in range(7,b-6):
            nl=defects(7,bl); nr=defects(7,b-bl)
            if not nl or not nr: continue
            for u in range(r+1):
                left += nl*comb(u+6,6)
                right += nr*comb(r-u+6,6)
    return conceptual,left,right

def C(word):
    c=0; A=0
    for a in word:
        c=3*c+(1<<A); A+=a
    return c,A

def comps(total,parts,prefix=()):
    if parts==1:
        yield prefix+(total,); return
    for x in range(total+1):
        yield from comps(total-x,parts-1,prefix+(x,))

def defect_words(n,total,prefix=()):
    if n==0:
        if total==0: yield prefix
        return
    for a in range(1,total+1):
        if a==2: continue
        yield from defect_words(n-1,total-a,prefix+(a,))

def small_direct():
    for r,b in [x for x in windows() if x[0] <= 2]:
        D=(1<<(b+2*r))-3**(14+r)
        for ds in defect_words(14,b):
            for gs in comps(r,14):
                word=[]
                for a,g in zip(ds,gs):
                    word.append(a); word.extend([2]*g)
                c,A=C(word)
                assert A==b+2*r
                assert c % D != 0

def main():
    path=Path(sys.argv[1] if len(sys.argv)>1 else 'results/canonical.txt')
    text=path.read_text()
    expected={
        'windows':'37',
        'conceptual_words':'50008555902',
        'left_states':'62907549',
        'right_states':'62907549',
        'queries':'62907549',
        'hits':'0',
    }
    for key,value in expected.items():
        assert f'{key}={value}' in text, (key,value)
    conceptual,left,right=counts()
    assert (len(windows()),conceptual,left,right)==(
        37,50_008_555_902,62_907_549,62_907_549)
    small_direct()
    print('X-8608 independent window/count/small-direct audit passed')

if __name__=='__main__':
    main()
