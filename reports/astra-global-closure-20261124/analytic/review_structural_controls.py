from fractions import Fraction as F
from collections import defaultdict
from math import prod
import json

def T(x): return (3*x+1)//2 if x%2 else x//2

def S(b): return -T(-b)

def parity_at(x,p): return x.numerator * pow(x.denominator,-1,p) %p

def req(v,msg):
    if not v: raise ValueError(msg)

def mixed(maxdepth):
    counts={}
    for z in (0,1):
        nwords=0
        x,y=F(-17),F(z)
        for p in range(maxdepth+1):
            pending=[(x,y,0)]
            while pending:
                a,b,q = pending.pop()
                nwords+=1
                slope=(b-a)/(17+z)
                req(slope>=1 and b>=z,(p,q,a,b,z,slope))
                if p+q==maxdepth: continue
                # Eliminate exact retrace only on the first inverse if a forward preceded it.
                if not(p and not q and not previous_bit):
                    pending.append((2*a,2*b,q+1))
                if parity_at(b,3)==2 and not(p and not q and previous_bit):
                    pending.append(((2*a-1)/3,(2*b-1)/3,q+1))
            previous_bit=parity_at(x,2)
            if previous_bit: x,y=(3*x+1)/2,(3*y+1)/2
            else: x,y=x/2,y/2
        counts[z]=nwords
    return counts

def prefixes():
    c,b=(25,37,55,82),(31,34,46,124)
    return [str(prod(F(2*v+1,2*v) for v in c[:i])/prod(F(2*v+1,2*v) for v in b[:i])) for i in range(1,5)]

def tables():
    cycle=set()
    v=17
    while v not in cycle:
        cycle.add(v); v=S(v)
    rows=defaultdict(list)
    maxd=0
    for s in range(1,137):
        v=s; path=[]
        while v not in cycle|{1,5}:
            path.append(v); v=S(v)
        maxd=max(maxd,len(path))
        if v in cycle: req(s>=17,s)
        if v in cycle and path and s%3==1: rows[str((path[-1],v))].append(s)
    tail={}
    for z in (0,1):
        cases=set()
        for v in range(1,17+z):
            a=v; coef=F(1)
            for t in range(24):
                req(coef<16,'coefficient')
                if t==23: req(a in (1,2),'tail')
                for m in (1,2,3):
                    if coef>=2**m and (17+z)*2**m-a>=17:
                        cases.add((m,(17+z)*2**m-a))
                coef*=F(3 if a%2 else 1,2)
                a=T(a)
        tail[z]=sorted(cases)
    return {'first_entrances':rows,'max_steps':maxd,'late_candidates':tail}

def lifts():
    # x and y need not materialize the pure-power-family member; this tests CS1's stronger 1024-guard on ordinary integers.
    u=69 * pow(3,-21*148,1024)%1024
    rows=0
    for k in [148,404,660]:
      for delta in [0,1,17]:
        j=u+1024*delta
        x=2**(33*k)*j-17; y=3*x-1; m=2**(21*k)*j-1
        X=x
        for _ in range(33*k): X=T(X); y=T(y)
        req(y==3**(22*k-1)*j-7 and y%1024==0,'member')
        req(X==3**(21*k)*j-17,'source')
        w=m
        for _ in range(21*k): w=T(w)
        req(w==X+16 and m<x,'partner')
        for _ in range(10): X=T(X); w=T(w)
        req(X==w,'clock')
        rows+=1
    return rows
print(json.dumps({'mixed_normal_words_depth_30':mixed(30),'strict_prefix_ratios':prefixes(),'finite_tables':tables(),'ordinary_full_clock_replays':lifts()}, indent=2))
