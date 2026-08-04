#!/usr/bin/env python3
"""Independent coverage and small-window audit for X-8609."""
from __future__ import annotations
from functools import lru_cache
from math import comb
from pathlib import Path
import sys

@lru_cache(None)
def defects(n,total):
    if n==0: return int(total==0)
    return sum(defects(n-1,total-a) for a in range(1,total+1) if a!=2)

def windows():
    out=[]
    for r in range(100):
        for b in range(15,100):
            A=b+2*r; k=15+r
            if (1<<A)*7**k > 22**k: break
            if 3**k < (1<<A) and defects(15,b): out.append((r,b))
    return out

def totals():
    conceptual=left=right=0
    for r,b in windows():
        conceptual += defects(15,b)*comb(r+14,14)
        for bl in range(7,b-7):
            nl=defects(7,bl); nr=defects(8,b-bl)
            if not nl or not nr: continue
            for u in range(r+1):
                left += nl*comb(u+6,6)
                right += nr*comb(r-u+7,7)
    return conceptual,left,right

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
        if a!=2:
            yield from defect_words(n-1,total-a,prefix+(a,))

def cdata(word):
    C=A=0
    for a in word:
        C=3*C+(1<<A); A+=a
    return C,A

def direct_small():
    for r,b in [x for x in windows() if x[0] <= 1]:
        D=(1<<(b+2*r))-3**(15+r)
        for ds in defect_words(15,b):
            for gs in comps(r,15):
                w=[]
                for a,g in zip(ds,gs): w += [a]+[2]*g
                C,A=cdata(w)
                assert A==b+2*r and C%D

def main():
    path=Path(sys.argv[1] if len(sys.argv)>1 else 'results/canonical.txt')
    text=path.read_text()
    expected_windows=windows()
    seen=[]
    for line in text.splitlines():
        if line.startswith('window R='):
            fields=dict(part.split('=') for part in line.split()[1:])
            assert fields['hits']=='0'
            seen.append((int(fields['R']),int(fields['B'])))
    assert sorted(seen)==expected_windows
    conceptual,left,right=totals()
    assert (conceptual,left,right)==(355_362_127_531,126_760_223,475_187_506)
    required={
        'windows=42',
        'conceptual_words=355362127531',
        'left_states=126760223',
        'right_states=475187506',
        'queries=126760223',
        'hits=0',
    }
    assert required.issubset(set(text.splitlines()))
    direct_small()
    print('X-8609 independent window/count/small-direct audit passed')
if __name__=='__main__': main()
