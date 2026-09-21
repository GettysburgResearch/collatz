#!/usr/bin/env python3
"""Bounded pointwise-signature experiments; NOT a universal Collatz solver.

All stopping times used here are certified by literal finite paths. The default
corpus is fixed. Unknown/budget outcomes are never classified as convergence.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path

LIMIT=10000

def require(ok, message):
    if not ok:
        raise ValueError(message)

def integer(n, minimum=0):
    require(type(n) is int and n>=minimum, 'invalid integer')
    return n

def step(n):
    return (3*n+1)//2 if n&1 else n//2

def trace(n, budget=LIMIT):
    integer(n,1); integer(budget)
    x=n; word=[]
    for _ in range(budget):
        if x==1:
            return ''.join(word)
        word.append(str(x&1)); x=step(x)
    require(x==1, 'UNRESOLVED: finite path budget exhausted')
    return ''.join(word)

def valuations(a):
    integer(a,1); u=v=0
    while a%2==0: u+=1; a//=2
    while a%3==0: v+=1; a//=3
    return u,v,a

def sig(n):
    w=trace(n)
    return [len(w), w.count('1'), 2*w.count('1')-len(w)]

def data(w):
    a=q=0
    for j,c in enumerate(w):
        require(c in '01','bad word')
        if c=='1': q+=1; a=3*a+(1<<j)
    return len(w),q,a

def endpoint(n,w):
    for c in w:
        require(n>0 and n%2==int(c),'nonphysical word')
        n=step(n)
    return n

def prefix_balance_max(w):
    cur=ans=0
    for c in w:
        cur+=1 if c=='1' else -1; ans=max(ans,cur)
    # After the first visit to 1, the balance alternates cur,cur+1.
    return max(ans,cur+1)

def germ(forms, point=0):
    integer(point)
    require(type(forms) is list and len(forms)>=2,'bad family')
    ws=[]; vs=[]; values=[]; charges=[]
    for f in forms:
        require(type(f) is list and len(f)==2,'bad affine')
        a,b=f; integer(a,1); require(type(b) is int,'bad intercept')
        n=a*point+b; integer(n,1)
        w=trace(n); u,v,c=valuations(a)
        ws.append(w); vs.append([u,v,c]); values.append(n)
        charges.append(u+2*v+2*w.count('1')-len(w))
    row=dict(forms=forms,point=point,values=values,stopping_words=ws,
             weighted_charges=charges)
    if len({v[2] for v in vs})>1:
        return dict(row,status='incompatible_slope_cores')
    if len({z%2 for z in charges})>1:
        return dict(row,status='phase_blocked_at_forced_clocks')
    S=max([0]+[len(w)-v[0] for w,v in zip(ws,vs)])
    while (S+charges[0])%2: S+=1
    words=[]
    for w,v in zip(ws,vs):
        extra=S+v[0]-len(w)
        require(extra>=0 and extra%2==0,'padding parity')
        words.append(w+'10'*(extra//2))
    if len(set(charges))>1:
        return dict(row,status='isolated_at_forced_clocks',words=words)
    return dict(row,status='uniform_at_point',words=words,
                progression=[point,1<<S])

def lift(n,m,w,z):
    integer(n,2); integer(m,1); require(m<n,'root order')
    E=endpoint(n,w); require(endpoint(m,z)==E,'not a merger')
    L,q,_=data(w); J,p,_=data(z)
    A=(1<<L)*3**max(p-q,0); B=(1<<J)*3**max(q-p,0)
    c=0; supercritical=True
    for j,bit in enumerate(w,1):
        c+=bit=='1'
        if 3**c <= 1<<j: supercritical=False
    last=None if A>=B else (n-m-1)//(B-A)
    return dict(n=n,m=m,words=[w,z],endpoint=E,steps=[A,B],
                endpoint_step=3**max(q,p),
                order_last_parameter=last,
                all_prefix_coefficients_above_one=supercritical)

def mine_roots(bound=4096):
    # For each endpoint, maximize the exact word derivative among earlier roots.
    best={1:(Fraction(1),1,'')}; rows=[]
    for n in range(2,bound+1):
        whole=trace(n); x=n; w=''; q=0; candidates=[]
        for j,bit in enumerate(whole,1):
            w+=bit; q+=bit=='1'; x=step(x)
            if 3**q <= 1<<j: break
            if x in best:
                coeff,m,z=best[x]
                ratio=Fraction(3**q,1<<j)/coeff
                candidates.append((ratio,j+len(z),j,m,z,w))
        if candidates:
            _,_,_,m,z,w=min(candidates)
            certificate=lift(n,m,w,z)
            status='infinite_family' if certificate['steps'][0]>=certificate['steps'][1] else 'finite_parameter_segment'
            rows.append(dict(source=n,status=status,certificate=certificate))
        else:
            rows.append(dict(source=n,status='no_hit_before_coefficient_crossing'))
        x=n; w=''; q=0
        # These earlier roots have literal complete traces; after 1 no endpoint
        # above the new root is possible, so no useful post-core visit is omitted.
        for j in range(len(whole)+1):
            coeff=Fraction(3**q,1<<j)
            old=best.get(x)
            if old is None or coeff>old[0] or (coeff==old[0] and (j,n)<(len(old[2]),old[1])):
                best[x]=(coeff,n,w)
            if j<len(whole):
                bit=whole[j]; w+=bit; q+=bit=='1'; x=step(x)
    return rows

def corpus():
    # Store compact stopping-time receipts. The verifier literally recomputes
    # both complete trajectories, not only checks hashes or generator formulas.
    h=[]
    for c in range(1,65537):
        a,b= sig(9*c+2),sig(c)
        defect=4+a[2]-b[2]
        kind='uniform' if defect==0 else 'isolated' if defect%2==0 else 'phase'
        h.append([c,a[0],a[1],b[0],b[1],defect,kind])
    forms=[[[9,2],[1,0]], [[8,-5],[4,-1],[3,-5]],
           [[1,1],[1,2],[1,3],[1,4]], [[5,1],[30,-3],[90,7]],
           [[1,1],[5,1]], [[2,1],[1,2]], [[12,-1],[18,-5],[27,2]]]
    families=[]
    for fs in forms:
        for t in range(1,65):
            if min(a*t+b for a,b in fs)>0: families.append(germ(fs,t))
    for k in range(1,33):
        families.append(germ([[1,1],[1,1<<k]],0))
    w='111101'; z='11011111010110111011110100111011011111100111100'
    seed=lift(303,27,w,z)
    escape=[]
    for t in [0,1,2,3,7,31,255,2**64,2**128,2**256]:
        n=303+16*seed['steps'][0]*t; m=27+16*seed['steps'][1]*t
        E=endpoint(n,w); require(endpoint(m,z)==E,'escape replay')
        x=n; minimum=None
        for bit in w:
            x=step(x); minimum=x if minimum is None else min(minimum,x)
        C=(27*n+11)//64
        escape.append(dict(t=t,n=n,m=m,C=C,endpoint=E,minimum=minimum))
    # Exact finite-prefix version of the rational 1/7 drift theorem.
    drift=[]
    for n in range(3,2050,2):
        w=trace(n); x=n; q=0; times=[]
        for a,bit in enumerate(w,1):
            q+=bit=='1';x=step(x)
            if x<n: break
            require(7*(2*q-a)>a,'rational drift failed')
            times.append([a,q,x])
        m=(n-1)//2; wm=trace(m); mu=prefix_balance_max(wm)
        for a,q,x in times:
            for b in [0,1,len(wm)//2,len(wm),len(wm)+1,len(wm)+10]:
                if b<=len(wm): p=wm[:b].count('1')
                else: p=wm.count('1')+(b-len(wm)+1)//2
                D=q-p; offset=b-a
                require(7*(2*D+offset+mu)>a,'portfolio drift')
        drift.append([n,m,len(wm),wm.count('1'),mu,times])
    return dict(schema='PSS-1',H_grid=h,families=families,seed=seed,
                escape=escape,root_mine=mine_roots(),drift=drift,
                control_lifts=[lift(3,1,'11000','10'*5),
                               lift(5,4,'100','001'),
                               lift(351,27,'1111100','110111110101101110111101')])

def summary(obj):
    raw=json.dumps(obj,sort_keys=True,separators=(',',':')).encode()
    hs=Counter(r[6] for r in obj['H_grid'])
    return dict(schema='PSS-1',sha256=hashlib.sha256(raw).hexdigest(),
                H_grid=len(obj['H_grid']),H_counts=dict(sorted(hs.items())),
                H_ternary_counts=dict(sorted(Counter(r[6] for r in obj['H_grid'] if r[0]%3==2).items())),
                families=len(obj['families']),family_counts=dict(sorted(Counter(r['status'] for r in obj['families']).items())),
                root_mine=len(obj['root_mine']),root_counts=dict(sorted(Counter(r['status'] for r in obj['root_mine']).items())),
                escape_examples=len(obj['escape']),drift_sources=len(obj['drift']),
                drift_observations=sum(len(r[5])*6 for r in obj['drift']),
                scope='finite exact corpus, not universal convergence or independent review')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--full',type=Path);p.add_argument('--check',type=Path)
    p.add_argument('--summary',type=Path)
    a=p.parse_args();obj=corpus();s=summary(obj)
    if a.check:require(json.dumps(json.loads(a.check.read_text()),sort_keys=True)==json.dumps(s,sort_keys=True),'canonical mismatch')
    if a.full:a.full.write_text(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n')
    if a.summary:a.summary.write_text(json.dumps(s,indent=2,sort_keys=True)+'\n')
    print(json.dumps(s,sort_keys=True))
if __name__=='__main__':main()
