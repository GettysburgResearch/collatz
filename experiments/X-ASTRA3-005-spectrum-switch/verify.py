#!/usr/bin/env python3
"""Separate reconstruction: literal T, exhaustive rank sublevels, inverse merging trees.
No generator or repository imports. Checks remain active under Python -O.
"""
from __future__ import annotations
import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path
from math import isqrt

SCHEMA='X-ASTRA3-005/v1'
SCOPE='finite exact interfaces; universal statements require written proofs; Collatz not proved'
LIMIT=16384
SCALE=10**24


def check(ok, message):
    if not ok: raise ValueError(message)


def seal(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def valuation(x,p):
    x=abs(x)
    check(x!=0,'zero valuation')
    power=1; e=0
    while x%(power*p)==0:
        power*=p; e+=1
    return e


def T(x):
    if x%2==0:return x//2
    return x+(x+1)//2


def linear(x,a):
    return (3**a-2**(a+1))*x+(3**a-2**a)


def component(x,a):
    q=linear(x,a)
    if q==0:return 0
    e=valuation(q,3)
    return q*(q//3**e)


@lru_cache(None)
def R(x):
    # Complete dictionary evaluation, rather than the four-entry collapse.
    if x==1:return 0
    best=min(component(x,0),component(x,1))
    a=2
    while True:
        z=linear(x,a)
        if z>=x*x: break
        best=min(best,component(x,a))
        a+=1
    return best


def refined(x):
    return R(x)*(R(x)+1)+(1-x)


def mode(x):
    if x%2==0:return 0
    return valuation(x+1,2)


@lru_cache(None)
def A(x):
    if x==1:return (1,-1,0,0)
    a=mode(x); y=x; copies=clock=0
    while y!=1 and mode(y)==a:
        for _ in range(a):
            check(y%2==1,'odd-run bit');y=T(y);clock+=1
        check(y%2==0,'terminal even bit');y=T(y);clock+=1
        copies+=1
    return y,a,copies,clock


def good(x):
    return x>1 and R(A(x)[0])<=R(x)


@lru_cache(None)
def exit_good(x):
    y=x; length=clock=0; visited=set()
    while good(y):
        check(y not in visited,'safe loop')
        visited.add(y)
        v,a,k,cost=A(y)
        check(refined(v)<refined(y),'refined rank')
        y=v;length+=1;clock+=cost
    check(length*length<=81*R(x),'complete safe clock')
    return y,length,clock


def J(x):
    if x==1:return 1
    check(not good(x),'unsafe domain')
    return exit_good(A(x)[0])[0]


def ranks_below(M):
    return [n for n in range(2,M+2) if R(n)<=M]


def spectrum():
    rows=[]
    for j in range(9):
        m=4**j
        values=ranks_below(m)
        check(len(values)**2<=81*m,'spectrum upper')
        check(len(values)>=max(0,isqrt(m)-1),'spectrum lower')
        rows.append(dict(M=m,count=len(values),values_sha256=seal(values),
                         largest_source=max(values,default=0)))
    return rows


def census():
    flats=[]; bad=quarter=0; hist=Counter();exits=Counter();rows=[]
    for x in range(2,LIMIT+1):
        y,a,k,l=A(x);r=R(x);s=R(y)
        if s==r:
            check(y>x,'flat-edge direction');flats.append([x,y,r])
        if s>r:bad+=1
        if 4*s<=r:quarter+=1
        target,count,clock=exit_good(x)
        hist[count]+=1;exits['one' if target==1 else 'unsafe']+=1
        rows.append([x,y,r,s,target,count,clock])
    return dict(N=LIMIT,safe=LIMIT-1-bad,quarter_safe=quarter,unsafe=bad,
                flat_edges=flats,safe_run_histogram=dict(sorted(hist.items())),
                exits=dict(exits),max_safe_modules=max(hist),transcript_sha256=seal(rows))


def rational(x):return [x.numerator,x.denominator]


def mass():
    tail=Fraction(12,LIMIT*isqrt(LIMIT))
    rows=[]
    for r in (0,1,2,4,8,16):
        lower_int=terms=0
        for x in range(2,LIMIT+1):
            if exit_good(x)[1]>r:
                q,rem=divmod(SCALE,R(x)*R(x))
                lower_int+=q;terms+=1
        rows.append(dict(r=r,enumerated_survivors=terms,
                         lower=rational(Fraction(lower_int,SCALE)),
                         upper=rational(Fraction(lower_int+terms,SCALE)+tail)))
    spikes=[]
    for e in range(4,197,16):
        x=3**e
        y=x
        # Exactly two literal '10' copies.
        for bit in (1,0,1,0):
            check(y%2==bit,'spike word');y=T(y)
        check(A(x)[0]==y and A(y)[0]==y//2,'maximal spike modules')
        check(y%4==2 and not good(x) and not good(y),'unsafe spike endpoints')
        check(J(x)==y and R(x)==x,'induced spike')
        check(R(y)*256==9*(x-1)**2,'spike endpoint rank')
        spikes.append(dict(e=e,source=x,endpoint=y,rank_source=R(x),rank_endpoint=R(y),
                           inverse_weight_ratio_lower_p2=rational(Fraction(R(y),R(x))**2)))
    return dict(scale=SCALE,source_cutoff=LIMIT,omitted_source_tail=rational(tail),
                safe_mass_intervals=rows,induced_spikes=spikes,
                global_rank_counterexample=[9,J(9),R(9),R(J(9))])


def egcd(a,b):
    old_r,r=a,b;old_s,s=1,0
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r;old_s,s=s,old_s-q*s
    check(old_r==1,'coprime CRT moduli')
    return old_s%b


def lift_parities(bits):
    residue=0;modulus=1
    for i,bit in enumerate(bits):
        y=residue
        for _ in range(i): y=T(y)
        if y%2!=int(bit):residue+=modulus
        modulus*=2
    y=residue
    for bit in bits:
        check(y%2==int(bit),'bit-by-bit source lift');y=T(y)
    return residue,modulus


def make_source(bits,b,t,lift=0):
    r,m=lift_parities(bits)
    p=3**(t+1)
    v=((3**t-(3**b-2**b))*egcd(3**b-2**(b+1),p))%p
    q=((v-r)*egcd(m,p))%p
    x=r+m*q
    if x<2:x+=m*p
    return x+lift*m*p


def repayment():
    special=[];general=[]
    for t in range(3,25):
        for lift in (0,1):
            n=make_source('1110'+'110'*t+'0',2,t,lift)
            y,a,k,c=A(n);m,b,l,d=A(y)
            check((a,k,b,l)==(3,1,2,t),'special modes')
            check(R(n)*3**t==(n+5)**2 and R(y)*9==(y+5)**2,'special minima')
            check(R(y)>2*3**(t-2)*R(n),'unbounded spike')
            check(256*64**t*R(m)<81*27**t*R(n),'net repayment')
            check(n<y<m,'growth across repayment')
            special.append(dict(t=t,lift=lift,n=n,spike=y,endpoint=m,ranks=[R(n),R(y),R(m)]))
    for a in (2,3,4):
        for b in (2,3,5):
            if a==b:continue
            for k in (1,2):
                for extra in (0,2):
                    t=2*b+4+extra;l=t+a*k+4
                    bits=('1'*a+'0')*k+('1'*b+'0')*l+'0'
                    n=make_source(bits,b,t)
                    y,aa,kk,_=A(n);m,bb,ll,_=A(y)
                    check((aa,kk,bb,ll)==(a,k,b,l),'general modes')
                    check(valuation(linear(n,b),3)==t and R(n)==component(n,b),'initial component')
                    check(valuation(linear(y,b),3)==min(a,b),'switch precision')
                    check(valuation(linear(m,b),3)==min(a,b)+b*l,'repayment precision')
                    check(16*R(m)<R(n) and m>y>n,'general net rank')
                    general.append(dict(a=a,b=b,k=k,t=t,ell=l,n=n,spike=y,endpoint=m,
                                        ranks=[R(n),R(y),R(m)]))
    alternative=dict(n=103,ternary_depth=valuation(108,3),endpoint=A(103)[0],
                     next_mode=mode(A(103)[0]))
    check(alternative==dict(n=103,ternary_depth=3,endpoint=175,next_mode=4),'unforced mode')
    return dict(special=special,general=general,alternative_mode=alternative)


def predecessors(y):
    out=[2*y]
    if y%3==2 and y>=2:out.append((2*y-1)//3)
    return out


def merging():
    cap=6;rows=[]
    for n in (3,7,9,13,27,46,81,121,703,2223):
        candidates=[x for x in range(1,R(n)+2) if refined(x)<refined(n)]
        diagrams=[];endpoint=n
        for r in range(cap+1):
            layer={endpoint}
            for s in range(cap+1):
                for x in layer:
                    if refined(x)<refined(n):
                        diagrams.append([r,s,x,endpoint])
                layer={u for y in layer for u in predecessors(y)}
            endpoint=T(endpoint)
        diagrams.sort(key=lambda q:(q[0]+q[1],max(q[0],q[1]),q[0],q[1],q[2]))
        rows.append(dict(n=n,rank=R(n),candidate_count=len(candidates),
                         candidate_sha256=seal(candidates),diagram_count=len(diagrams),
                         diagram_sha256=seal(diagrams),best=diagrams[0] if diagrams else None))
    return dict(clock_cap=cap,rows=rows)


def reconstruct():
    return dict(schema=SCHEMA,scope=SCOPE,spectrum=spectrum(),census=census(),mass=mass(),
                repayment=repayment(),merging=merging())


def validate(report,expected):
    check(set(report)=={'payload','sha256'},'top-level schema')
    check(report['sha256']==seal(report['payload']),'payload digest')
    check(report['payload']==expected,'independent reconstruction mismatch')


def corruptions(report,expected):
    variants=[]
    for i in range(8):
        r=deepcopy(report);p=r['payload']
        if i==0:p['scope']='Collatz proved'
        if i==1:p['spectrum'].pop()
        if i==2:p['census']['safe']+=1
        if i==3:p['census']['flat_edges'][0][1]=2
        if i==4:p['mass']['omitted_source_tail']=[0,1]
        if i==5:p['mass']['induced_spikes'][0]['endpoint']+=1
        if i==6:p['repayment']['special'][0]['ranks'][-1]=0
        if i==7:p['merging']['clock_cap']=7
        r['sha256']=seal(p);variants.append(r)
    for i,r in enumerate(variants):
        try:validate(r,expected)
        except ValueError:continue
        raise ValueError(f'resealed corruption {i} accepted')
    return len(variants)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('report',type=Path)
    ap.add_argument('--self-test',action='store_true');ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    expected=json.loads(json.dumps(reconstruct(),sort_keys=True))
    report=json.loads(args.report.read_text());validate(report,expected)
    if args.output:
        args.output.write_text(json.dumps(dict(payload=expected,sha256=seal(expected)),
                                          sort_keys=True,separators=(',',':'))+'\n')
    print(seal(expected));print('separate finite reconstruction passed')
    if args.self_test:print(f'{corruptions(report,expected)} resealed corruptions rejected')

if __name__=='__main__':main()
