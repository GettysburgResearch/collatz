#!/usr/bin/env python3
"""Independent exact verifier. No imports from the generator or repository."""
from __future__ import annotations
import argparse, copy, hashlib, json
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import Path

SCHEMA='X-ASTRA3-005/v1'
SCOPE='finite exact interfaces; universal statements require the written proofs; Collatz not proved'

def check(test: bool, explanation: str) -> None:
    if not test:raise ValueError(explanation)

def hash_json(x: object) -> str:
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def order(x: int,p: int) -> int:
    x=abs(x);check(x>0,'zero has no finite order');k=0
    while x%p==0:x//=p;k+=1
    return k

def step(n: int) -> int:
    return (3*n+1)//2 if n%2 else n//2

def affine_value(n: int,a: int) -> int:
    return (3**a-2**(a+1))*n+3**a-2**a

@lru_cache(None)
def score(n: int) -> int:
    check(n>=1,'nonpositive source')
    if n==1:return 0
    def r(z):return z*z//3**order(z,3)
    best=min(r(n),r(n-1));a=2
    # Search the infinite dictionary. Once z>best, monotonic z makes all
    # future components impossible minimizers. No four-entry lookup is used.
    while True:
        z=affine_value(n,a)
        if z>best:return best
        best=min(best,r(z));a+=1

@lru_cache(None)
def accelerate(n: int) -> tuple[int,int,int]:
    if n==1:return 1,0,0
    a=0 if n%2==0 else order(n+1,2)
    cur=n;k=0;spent=0
    while True:
        for _ in range(a):
            check(cur%2==1,'illegal odd step');cur=step(cur);spent+=1
        check(cur%2==0,'illegal even step');cur=step(cur);spent+=1;k+=1
        check(spent<=3*(n+5).bit_length()+3,'module clock')
        if cur==1:break
        next_a=0 if cur%2==0 else order(cur+1,2)
        if next_a!=a:break
    return cur,a,k

def good(n: int) -> bool:
    return n>1 and 4*score(accelerate(n)[0])<=score(n)

def euclid(a: int,b: int) -> tuple[int,int,int]:
    if b==0:return a,1,0
    g,x,y=euclid(b,a%b);return g,y,x-(a//b)*y

def chinese(a: int,m: int,b: int,q: int) -> int:
    g,inv,_=euclid(m,q);check(g==1,'CRT moduli not coprime')
    return a+m*((b-a)*inv%q)

def binary_root(word: str) -> tuple[int,int]:
    r=0;mod=1
    for i,bit in enumerate(word+'1'):
        choices=[]
        for x in (r,r+mod):
            y=x
            for _ in range(i):y=step(y)
            if y%2==int(bit):choices.append(x)
        check(len(choices)==1,'parity lift not unique')
        r=choices[0];mod*=2
    return r,mod

def make_source(word: str,residue: int,three: int) -> tuple[int,int]:
    r,two=binary_root(word);n=chinese(r,two,residue,three)
    stride=two*three
    while n<11:n+=stride
    return n,stride

def by_components(B: int) -> list[int]:
    out=set();E=0
    while 3**(E+1)<=B:E+=1
    for a in range(max(3,E+1)):
        first_e=0 if a<3 else a
        for e in range(first_e,E+1):
            for u in range(1,isqrt(B//3**e)+1):
                if u%3==0:continue
                Z=3**e*u;value=3**e*u*u
                if a==0:n=Z
                elif a==1:n=Z+1
                elif a==2:n=Z-5
                else:
                    d=3**a-2**(a+1);c=3**a-2**a
                    if (Z-c)%d:continue
                    n=(Z-c)//d
                if n>=2 and score(n)==value:out.add(n)
    return sorted(out)

def volumes() -> dict:
    rows=[]
    for B in (1,16,256,4096,65536,2**24):
        xs=by_components(B)
        if B<=65536:
            direct=[n for n in range(2,B+2) if score(n)<=B]
            check(xs==direct,'complete rank ball differs from direct interval')
        check(len(xs)**2<=81*B and len(xs)>=max(0,isqrt(B)-1),'volume bounds')
        rows.append(dict(B=B,count=len(xs),maximum=max(xs,default=0),digest=hash_json(xs)))
    check(147>144,'square-root enclosure')
    check(Fraction(36,5)+Fraction(343,300)<9,'constant-nine sum')
    check(Fraction(9,2)+Fraction(1,12)==Fraction(55,12),'reciprocal-rank sum')
    return dict(rows=rows,integer_comparisons=3)

def operators() -> dict:
    sources={n:1+n%7 for n in range(2,2049) if good(n)};count=len(sources);rows=[]
    for r in range(9):
        total=sum(score(n)*mass for n,mass in sources.items())
        forward={};outside=0
        for n,mass in sources.items():
            y=accelerate(n)[0]
            if y==1:continue
            if good(y):forward[y]=forward.get(y,0)+mass
            else:outside+=score(y)*mass
        left=sum(score(n)*mass for n,mass in forward.items())
        check(left+outside<=Fraction(total,4),'safe mass inequality')
        rows.append([r,len(sources),total,left,outside]);sources=forward
    spikes=[]
    for e in range(4,117,16):
        x=3**e;walk=[x]
        for _ in range(4):walk.append(step(walk[-1]))
        y=walk[-1]
        check(y==(9*x+7)//16 and accelerate(x)==(y,1,2),'spike physical path')
        check(score(x)==x and 256*score(y)==9*(x-1)**2,'spike rank equation')
        check(not good(x) and not good(y),'unsafe endpoint')
        check(accelerate(y)==(y//2,0,1) and score(y//2)==(y//2-1)**2,'unsafe next endpoint')
        check(Fraction(score(y),x*x)>Fraction(1,32),'moment lower bound')
        spikes.append([e,x,y,score(y)])
    return dict(seed_support=count,safe_rows=rows,spikes=spikes)

def barriers() -> dict:
    rows=[];positions=ancestors=0
    for H in range(2,17):
        p=3**(H+1);q=2**(2*H+1)
        base=chinese(3**H,p,1+4**H,q)
        for lift in (0,1,7):
            n=base+p*q*lift;initial=score(n)
            check(order(n,3)==H and order(n-1,2)==2*H,'barrier guards')
            cur=n;maximum=0
            for i in range(2*H+1):
                maximum=max(maximum,score(cur));positions+=1
                if i<2*H:
                    check(cur%2==(1-i%2),'alternating repayment word');cur=step(cur)
            y=cur
            check(accelerate(n)==(y,1,H),'maximal repeated corridor')
            check(Fraction(score(y),initial)<Fraction(9,16)**H,'common-rank reduction')
            lo=((3*n-1)//2)**2;hi=((3*n+1)//2)**2
            check(score(step(n))==lo and lo<=maximum<=hi,'all-diagram resource interface')
            for j in range(9):
                x=2**j*n
                check(x%3==0 and score(x)==4**j*initial,'reverse ray rank')
                # T has no odd predecessor at a multiple of three.
                check((2*x-1)%3!=0,'unexpected odd inverse')
                ancestors+=1
            rows.append([H,lift,n,initial,y,score(y),maximum,lo,hi])
    return dict(cases=len(rows),positions=positions,ancestor_checks=ancestors,digest=hash_json(rows),examples=rows[:3])

def switches() -> dict:
    inv=euclid(17,243)[1];residue=-73*inv%243
    rows=[];examples=[];weights=[];count=unsafe_count=0
    for K in range(1,17):
        for extra in (0,2):
            L=K+4+extra;word='111010'*K+'0'*L
            base,stride=make_source(word,residue,243)
            for lift in (0,1,3):
                n=base+stride*lift;cur=n;history=[n]
                check(order(17*n+73,2)==6*K,'counter not intrinsic')
                for i in range(2*K):
                    desired=(3,1) if i%2==0 else (1,1)
                    dest,a,k=accelerate(cur)
                    check((a,k)==desired and not good(cur),'unsafe phase guard')
                    check(score(cur)==((cur-1)**2//9 if i%2==0 else (cur+5)**2//9),'phase score formula')
                    count+=1;unsafe_count+=1;cur=dest;history.append(cur)
                high=cur
                check(Fraction(score(high),score(n))>Fraction(81,64)**(2*K),'repeated unsafe growth')
                out,a,k=accelerate(high)
                check((a,k)==(0,L) and 4*score(out)<score(n),'total guarded repayment')
                check(good(high),'terminal phase should be safe');count+=1
                rows.append([K,L,lift,n,high,out,score(n),score(high),score(out)])
                if lift==0 and extra==0 and K in (1,2,4,8):examples.append(rows[-1])
                if (K,lift,extra)==(2,0,0):
                    for s,t in ((0,1),(2,0),(4,-1),(3,1),(-1,2)):
                        found=None
                        for x,y in zip(history[:-2],history[1:-1]):
                            wx=Fraction(x)**(-s)*Fraction(score(x))**(-t)
                            wy=Fraction(y)**(-s)*Fraction(score(y))**(-t)
                            if not good(y) and wx>wy:found=[s,t,x,y];break
                        check(found is not None,'missing induced weight violation');weights.append(found)
    controls=[[n,accelerate(n)[0],score(n),score(accelerate(n)[0])] for n in (3,7,9,81)]
    return dict(cases=len(rows),modules=count,unsafe_sources=unsafe_count,digest=hash_json(rows),examples=examples,power_weight_failures=weights,residual_controls=controls)

def reconstruct() -> dict:
    return dict(schema=SCHEMA,scope=SCOPE,volume=volumes(),operator=operators(),barriers=barriers(),switches=switches())

def adjudicate(report: dict, expected: dict) -> None:
    check(set(report)=={'payload','sha256'},'envelope keys')
    check(report['sha256']==hash_json(report['payload']),'digest mismatch')
    check(report['payload']==expected,'independent reconstruction mismatch')

def self_test(report: dict,expected: dict) -> int:
    alterations=[
      lambda p:p.update(scope='Collatz proved'),
      lambda p:p['volume']['rows'][0].update(count=0),
      lambda p:p['volume']['rows'][-1].update(maximum=0),
      lambda p:p['operator']['spikes'][0].__setitem__(3,0),
      lambda p:p['operator']['safe_rows'][0].__setitem__(3,10**30),
      lambda p:p['barriers'].update(cases=44),
      lambda p:p['switches'].update(unsafe_sources=0),
      lambda p:p['switches']['examples'][0].__setitem__(2,1),
      lambda p:p['switches']['power_weight_failures'].pop(),
      lambda p:p['switches']['residual_controls'][0].__setitem__(3,0),
    ]
    for alter in alterations:
        bad=copy.deepcopy(report);alter(bad['payload']);bad['sha256']=hash_json(bad['payload'])
        try:adjudicate(bad,expected)
        except ValueError:continue
        raise ValueError('resealed corruption accepted')
    return len(alterations)

def main() -> None:
    p=argparse.ArgumentParser();p.add_argument('report',type=Path);p.add_argument('--self-test',action='store_true');args=p.parse_args()
    data=json.loads(args.report.read_text());expected=reconstruct();adjudicate(data,expected)
    print('independent finite verifier passed',hash_json(expected))
    if args.self_test:print('resealed corruptions rejected:',self_test(data,expected))

if __name__=='__main__':main()
