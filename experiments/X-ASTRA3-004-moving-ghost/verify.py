#!/usr/bin/env python3
"""Independent finite reconstruction. No imports from run.py or the repository."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import Path

SCHEMA='X-ASTRA3-004/v1'
SCOPE='finite interfaces and stated analytic tails; no global Collatz certificate'
NMAX=16384

def check(ok: bool, msg: str) -> None:
    if not ok: raise AssertionError(msg)

def hashed(x: object) -> str:
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def power_count(x: int,p: int) -> int:
    if not x: raise ValueError('zero is not a finite valuation')
    x=abs(x);q=p;k=0
    while x%q==0:
        k+=1;q*=p
    return k

def branch(x: int) -> int:
    return x//2 if (x & 1)==0 else x+(x+1)//2

def mode(x: int) -> int:
    if not x&1:return 0
    k=0;y=x+1
    while not y&1:y//=2;k+=1
    return k

def try_word(x: int,a: int) -> int | None:
    for bit in [1]*a+[0]:
        if x&1 != bit:return None
        x=branch(x)
    return x

@lru_cache(maxsize=None)
def physical(x: int) -> tuple[int,int,int]:
    if x==1:return 1,0,0
    a=mode(x);k=0;y=x
    while True:
        z=try_word(y,a)
        if z is None:break
        y=z;k+=1
        # Explicit finite safety check, not used as a theorem of termination.
        check(k<=4*(x+5).bit_length(),'unexpected finite replay overflow')
    check(k>0 and y>0,'physical maximal block')
    return y,a,k

def displacement(a: int,n: int) -> int:
    # z_(a+1)=3z_a+2^a(2n+1), avoiding the generator's closed form.
    w=-n
    for b in range(a):w=3*w+2**b*(2*n+1)
    return w

def component(a: int,n: int) -> int:
    w=displacement(a,n)
    if not w:return 0
    u=abs(w)
    while u%3==0:u//=3
    return abs(w)*u

@lru_cache(maxsize=None)
def minimum(n: int) -> int:
    h=power_count(2*n+1,3)
    inds=list(range(3))
    if h>2:inds.append(h)
    return min(component(a,n) for a in inds)

def reverse_word(y: int,a: int) -> int | None:
    x=2*y
    for unused in range(a):
        q=2*x-1
        if q%3:return None
        x=q//3
        if x<1:return None
    return x

def predecessors(y: int,cap: int) -> list[list[int]]:
    out=[]
    if y&1:
        j=1
        while y*2**j<=cap:
            out.append([y*2**j,0,j]);j+=1
    for a in range(1,power_count(2*y+1,3)+1):
        if try_word(y,a) is not None:continue
        x=y;k=0
        while True:
            x=reverse_word(x,a)
            if x is None or x<=1:break
            k+=1
            check(k<=(2*y+5).bit_length()*4,'inverse finite safety bound')
            if x<=cap:out.append([x,a,k])
    return sorted(out)

def rank_fiber(m: int) -> list[int]:
    if not m:return [1]
    e=power_count(m,3); Z=isqrt(m*3**e)
    if Z*Z!=m*3**e:return []
    ans=set()
    for a in range(max(2,e)+1):
        d=3**a-2**(a+1);c=3**a-2**a
        for sign in (-1,1):
            if (sign*Z-c)%d==0:
                x=(sign*Z-c)//d
                if x>=2 and minimum(x)==m:ans.add(x)
    return sorted(ans)

def inverse_mod(a: int,m: int) -> int:
    r0,r1=a,m;s0,s1=1,0
    while r1:
        q=r0//r1;r0,r1=r1,r0-q*r1;s0,s1=s1,s0-q*s1
    check(r0==1,'coprime CRT coefficient')
    return s0%m

def source(a: int,k: int,t: int) -> int:
    d=3**a-2**(a+1);c=3**a-2**a
    M=2**((a+1)*k+1);N=3**(t+1)
    r=((M//2-c)*inverse_mod(d%M,M))%M
    s=((N//3-c)*inverse_mod(d%N,N))%N
    x=(r*N*inverse_mod(N%M,M)+s*M*inverse_mod(M%N,N))%(M*N)
    return x+M*N

def renewals() -> dict:
    J=4096;den=10**12
    q=Fraction()
    for t in reversed(range(1,J+1)):q+=Fraction(1,t*t)
    lo=q+Fraction(1,J+1);hi=q+Fraction(1,J)
    intervals=[]
    for lam in [1,2,16,32]:
        p1,p2=lo*den/(64-lam),hi*den/(64-lam)
        intervals.append([lam,p1.numerator//p1.denominator,
                          -(-p2.numerator//p2.denominator)])
    rows=[]
    for k in range(1,10):
        for m in range(1,65):
            n=8**k*m-5;y,a,kk=physical(n)
            x=n
            for step in range(3*k):
                check(x%2==[1,1,0][step%3],'ordinary renewal word')
                x=branch(x)
            check(x==9**k*m-5 and x>n and a==2 and kk>=k,'renewal lift')
            rows.append([k,m,n,kk])
    # Each lambda=64 layer contributes zeta(2)/64, so its total diverges.
    check(64*64**3==64**4,'critical layer identity')
    check(Fraction(64,63)*Fraction(1,48)*2==Fraction(8,189),'dictionary tail')
    return dict(scale=den,zeta_cutoff=J,occupation_intervals=intervals,
                progression_cases=len(rows),progression_digest=hashed(rows),
                lambda64_diverges=True,dictionary_upper=[8,189])

def arithmetic() -> dict:
    rows=[];na=0;up=0;steps=0;labels=Counter();seen=set()
    for n in range(2,NMAX+1):
        y,a,k=physical(n);s=minimum(n)
        check(s==min(component(b,n) for b in range(21)),'rank truncation interface')
        check(n-1<=s<=n*n,'properness')
        # Integer checking of the transport identity.
        check(component(a,y)*2**(2*(a+1)*k)==component(a,n)*3**(a*k),'transport')
        check(power_count(displacement(a,y),2)<a+1,'exit precision')
        check(y==1 or mode(y)!=a,'mode switch')
        aligned=component(a,n)==s
        if aligned:
            na+=1;check(4*minimum(y)<=s,'aligned contraction')
        check(y+5<=(n+5)**3,'uniform height')
        check((a+1)*k<=3*(n+4).bit_length(),'uniform finite clock')
        up+=y>n;steps+=(a+1)*k;labels[a]+=1;seen.add(s)
        rows.append([n,y,a,k,s,minimum(y),aligned])
    fs=[[m,rank_fiber(m)] for m in sorted(seen)]
    for n in range(2,NMAX+1):check(n in rank_fiber(minimum(n)),'fiber complete sample')
    for m,F in fs:check(len(F)<=max(3,power_count(m,3)+1),'fiber cap')
    return dict(limit=NMAX,sources=NMAX-1,raw_steps=steps,aligned=na,uphill=up,
                labels=dict(sorted(labels.items())),digest=hashed(rows),
                fibers=len(fs),fiber_digest=hashed(fs))

def families() -> dict:
    rows=[]
    for a in range(2,13):
        for k in [1,2,4,8]:
            for extra in [4,7]:
                t=2*a+extra;n=source(a,k,t);y,aa,kk=physical(n)
                check((aa,kk)==(a,k),'CRT trajectory')
                check(power_count(displacement(a,n),3)==t,'CRT precision')
                check(power_count(2*n+1,3)==a,'moving index')
                check(minimum(n)==component(a,n) and y>n,'uphill alignment')
                check(4*minimum(y)<minimum(n),'strict family decrease')
                check(all(component(b,n)>minimum(n) for b in range(a+9) if b!=a),'unique minimizer')
                rows.append([a,k,t,str(n),str(y),str(minimum(n)),str(minimum(y))])
    backward=[]
    for e in range(4,125,8):
        x=3**e;y=branch(branch(branch(branch(x))))
        check(y==(9*x+7)//16 and physical(x)==(y,1,2),'backward power diagram')
        check(minimum(x)==x and 256*minimum(y)==9*(x-1)**2,'backward power ranks')
        check(25*minimum(x)<=9*minimum(y),'backward uniform bound')
        backward.append([e,str(x),str(y),str(minimum(x)),str(minimum(y))])
    return dict(cases=len(rows),rows=rows,backward_cases=len(backward),backward_rows=backward)

def fans() -> dict:
    forward=defaultdict(list)
    for n in range(2,8193):
        y,a,k=physical(n)
        if 2<=y<=128:forward[y].append([n,a,k])
    rows=[]
    for y in range(2,129):
        got=predecessors(y,8192)
        check(got==forward[y],'full finite ordinary fan')
        check(len({x[0] for x in got})==len(got),'fan injective coding')
        for n,a,k in got:
            if a and a<power_count(2*y+1,3):check(k==1,'only one deep column')
        rows.append([y,got])
    counts=Counter();rem=[];witnesses=[]
    for n in range(2,NMAX+1):
        y,a,k=physical(n);s=minimum(n)
        if minimum(y)<s:counts['forward']+=1
        else:
            choices=[r for r in predecessors(n,s) if minimum(r[0])<s]
            if not choices:counts['residual']+=1;rem.append(n)
            else:
                counts['inverse_only']+=1
                r=min(choices,key=lambda r:(minimum(r[0]),r[0]))
                check(physical(r[0])[0]==n,'ordinary merging certificate')
                witnesses.append([n,r[0],s,minimum(r[0]),r[1],r[2]])
    return dict(cap=8192,endpoints=127,edges=sum(len(r[1]) for r in rows),digest=hashed(rows),
                local_limit=NMAX,classification=dict(counts),residual_digest=hashed(rem),
                first_residuals=rem[:32],inverse_digest=hashed(witnesses),first_inverse=witnesses[:16])

def escape() -> dict:
    rows=[];core=0;other=0;mx=0;safe=0
    for start in range(2,NMAX+1):
        n=start;r=minimum(n);budget=1;b=4
        while b<=r:budget+=1;b*=4
        safe+=4*minimum(physical(n)[0])<=r
        count=0;steps=0
        while n!=1:
            y,a,k=physical(n)
            if 4*minimum(y)>minimum(n):break
            n=y;count+=1;steps+=(a+1)*k
            check(count<=budget,'finite quarter-drop clock')
        check(steps<=3*budget*(r+5).bit_length(),'shortcut clock')
        core+=n==1;other+=n!=1;mx=max(mx,steps)
        rows.append([start,n,count,steps])
    controls=[]
    for n in [3,7,9,15,27]:
        y,a,k=physical(n)
        check(minimum(y)>=minimum(n),'unconditional-rank control')
        controls.append([n,y,minimum(n),minimum(y),a,k])
    return dict(sources=NMAX-1,safe_inputs=safe,core=core,unsafe=other,max_shortcut_steps=mx,
                digest=hashed(rows),controls=controls,tail_s2='2^(1-r), r>=1')

def reconstruct() -> dict:
    data=dict(schema=SCHEMA,scope=SCOPE,renewal=renewals(),arithmetic=arithmetic(),
              families=families(),fans=fans(),escape=escape())
    return json.loads(json.dumps(data))

def validate(report: dict, expected: dict) -> None:
    check(set(report)=={'payload','sha256'},'report keys')
    check(report['sha256']==hashed(report['payload']),'semantic hash')
    check(report['payload']==expected,'independent reconstruction mismatch')

def self_test(report: dict, expected: dict) -> int:
    count=0
    for case in range(8):
        bad=copy.deepcopy(report);p=bad['payload']
        if case==0:p['schema']='forged-schema'
        elif case==1:p['scope']='all ordinary Collatz orbits proved convergent'
        elif case==2:p['families']['rows'].pop()
        elif case==3:p['fans']['edges']-=1
        elif case==4:p['fans']['classification']['residual']=0
        elif case==5:p['renewal']['lambda64_diverges']=False
        elif case==6:p['escape']['core']=p['escape']['sources']
        else:p['renewal']['occupation_intervals'][0][2]=0
        bad['sha256']=hashed(p)
        try:validate(bad,expected)
        except AssertionError:count+=1
        else:raise AssertionError('accepted resealed corruption')
    return count

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('report',type=Path);ap.add_argument('--self-test',action='store_true')
    args=ap.parse_args();report=json.loads(args.report.read_text());expected=reconstruct()
    validate(report,expected)
    print(report['sha256']);print('independent finite reconstruction passed')
    if args.self_test:print(f'{self_test(report,expected)} resealed corrupt reports rejected')

if __name__=='__main__':main()
