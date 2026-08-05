#!/usr/bin/env python3
"""Independent exact verifier for X-9606."""
from __future__ import annotations
import argparse,itertools,json
from pathlib import Path
from typing import Iterator,Sequence
S=8

def bars(total:int,parts:int)->Iterator[tuple[int,...]]:
    for cuts in itertools.combinations(range(total+parts-1),parts-1):
        pts=(-1,)+cuts+(total+parts-1,)
        yield tuple(pts[i+1]-pts[i]-1 for i in range(parts))

def arrangements(kind:str):
    if kind=='1^8': yield (1,)*S; return
    if kind.startswith('1^7,'):
        high=int(kind.rsplit(',',1)[1])
        for p in range(S):
            a=[1]*S;a[p]=high;yield tuple(a)
        return
    if kind=='1^6,3,3':
        for p,q in itertools.combinations(range(S),2):
            a=[1]*S;a[p]=a[q]=3;yield tuple(a)
        return
    if kind=='1^6,3,4':
        for p in range(S):
            for q in range(S):
                if p==q:continue
                a=[1]*S;a[p]=3;a[q]=4;yield tuple(a)
        return
    raise ValueError(kind)

def cd(word:Sequence[int]):
    k=len(word);pref=0;c=0
    for i,a in enumerate(word):
        c+=3**(k-1-i)*2**pref;pref+=a
    return c,2**pref-3**k

def sparse(word:Sequence[int]):
    k=len(word);pref=0;e=0
    for i,a in enumerate(word):
        e+=3**(k-1-i)*2**pref*(4-2**a);pref+=a
    return e

def main():
    ap=argparse.ArgumentParser();ap.add_argument('canonical',type=Path);args=ap.parse_args()
    payload=json.loads(args.canonical.read_text())
    ranges={}
    for row in payload['finite_rows']:ranges.setdefault(row['type'],[]).append(row['R'])
    result=[]
    for kind in ranges:
        # Recover B from the frozen cutoff packet rather than sharing source constants.
        B=next(row['B'] for row in payload['cutoff_packet'] if row['type']==kind)
        for R in ranges[kind]:
            D=2**B*4**R-3**S*3**R
            count=height=0;mx=None;rho=None
            for gaps in bars(R,S):
                if gaps[-1]!=max(gaps):continue
                for exceptional in arrangements(kind):
                    count+=1;core=[]
                    for i,a in enumerate(exceptional):
                        core.append(a)
                        if i<S-1:core.extend([2]*gaps[i])
                    C,Dcore=cd(core);E=C-Dcore
                    if E!=sparse(core):raise AssertionError('sparse mismatch')
                    mx=E if mx is None else max(mx,E)
                    rem=E%D
                    if rem==0:
                        full=core+[2]*gaps[-1];Cf,Df=cd(full)
                        raise AssertionError(f'unexpected divisor hit start={Cf//Df}')
                    if E>=2*D:
                        height+=1;circ=min(rem,D-rem);rho=circ if rho is None else min(rho,circ)
            result.append({'type':kind,'R':R,'D':D,'largest_gap_candidates':count,'max_E_core':mx,'height_survivors':height,'least_nonzero_circular_remainder':rho})
    if result!=payload['finite_rows']:raise SystemExit('independent rows differ')
    print('independent X-9606 verification passed')
if __name__=='__main__':main()
