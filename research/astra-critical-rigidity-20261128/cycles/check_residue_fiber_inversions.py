"""Enumerate and sort the actual denominator-fiber inversions of rational cycles."""

import json
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd

from check_rational_six_sum import floor_log2, native_cycle, require


def direct_cycle(y0, q):
    y, seen, e = y0, set(), []
    while y not in seen:
        require(y % 2 and gcd(y,q)==1, "genuine reduced odd state")
        seen.add(y)
        t=3*y+q
        v=(t & -t).bit_length()-1
        y=t >> v
        e.append(v)
        require(len(e)<500, "specified start returns")
    require(y == y0, "primitive cycle anchored at supplied numerator")
    return e


def cycle_lengths(perm):
    seen=set()
    result=[]
    for j in range(len(perm)):
        if j in seen:
            continue
        u=j
        length=0
        while u not in seen:
            seen.add(u)
            length+=1
            u=perm[u]
        require(u==j, "true permutation")
        result.append(length)
    return sorted(result)


def residue_inversions(y,q,perm,wind):
    pairs=[]
    for i,x in enumerate(y):
        for j,z in enumerate(y):
            if i==j:
                continue
            # The strict upper endpoint is never a dyadic logarithm, since
            # distinct reduced odd numerators lie on different rays.
            hi=floor_log2(z,x)
            lo=wind[j]-wind[i]+floor_log2(y[perm[j]],y[perm[i]])+1
            for d in range(lo,hi+1):
                if (pow(2,d,q)*x-z) % q == 0:
                    ratio=Fraction(z << max(-d,0), x << max(d,0))
                    require(ratio>1,"strictly ordered input")
                    pairs.append((ratio,i,j,d))
    return pairs


def check(e):
    E,q,y=native_cycle(e)
    p,A=len(y),E[-1]
    g=gcd(p,A); B,P=A//g,p//g
    h=next(k for k in range(1,g+1) if pow(2,B*k,q)==pow(3,P*k,q))
    triples=[]
    for i,x in enumerate(y):
        for j,z in enumerate(y):
            for d in range(1,max(1,floor_log2(z,x))+1):
                hq,rem=divmod(z-(x << d),q)
                if rem==0 and hq>0 and hq%2==1 and 3*hq<(1<<d)-1:
                    triples.append((i,j,d))
    perm=list(range(1,p))+[0];wind=e.copy()
    edges=residue_inversions(y,q,perm,wind)
    require(set(triples)=={(i,j,d) for _,i,j,d in edges},"physical inversion formula")
    I=len(edges)
    require(I>=g//h-1 and (I-g//h+1)%2==0,"count and parity")
    if max(y)<=16*min(y):
        for i,j,d in triples:
            require(d==3 and y[j]==8*y[i]+q and
                    y[(j+1)%p]==6*y[i]+q and y[(j+2)%p]==9*y[i]+2*q,
                    "narrow exact two-successor chain")
    if max(y)<=9*min(y):
        require(h==g, "complete denominator order at width nine")
    changes=[]
    while edges:
        _,i,j,d=min(edges)
        before=len(cycle_lengths(perm))
        perm[i],perm[j]=perm[j],perm[i]
        wind[i],wind[j]=wind[j]-d,wind[i]+d
        require(sum(wind)==A,"winding preserved")
        require(all((pow(2,w,q)*y[k]-3*z)%q==0 for k,w,z in zip(perm,wind,y)),
                "full residue transport preserved")
        changes.append(len(cycle_lengths(perm))-before)
        require(abs(changes[-1])==1, "one ray transposition")
        after=residue_inversions(y,q,perm,wind)
        require(len(after)==len(edges)-1, "one inversion orbit removed")
        edges=after
    require(cycle_lengths(perm)==[h*P]*(g//h),"every sorted return has exact period")
    # Test all sorted lift returns, including independent scale corrections.
    for start in range(p):
        j=start; w=0
        for n in range(1,2*p+1):
            w+=wind[j];j=perm[j]
            for v in {-(n*A//p)-1,-(n*A//p),-(n*A//p)+1}:
                if (pow(2,v,q)*pow(3,n,q)-1)%q:
                    continue
                diff=(y[j] << max(w+v,0))-(y[start] << max(-(w+v),0))
                require((diff>0)-(diff<0)==(p*v+n*A>0)-(p*v+n*A<0),
                        "sorted all-cut sign of residue return")
    return dict(q=q,p=p,A=A,g=g,h=h,minimum_numerator=min(y),maximum_numerator=max(y),
                inversions=I,sorted_ray_period=h*P,splits=changes.count(1),
                joins=changes.count(-1))


if __name__=="__main__":
    counts=Counter()
    for p in range(1,6):
        for seq in product(range(1,6),repeat=p):
            if (1<<sum(seq))<=3**p:
                continue
            if any(seq>=seq[i:]+seq[:i] for i in range(1,p)):
                continue
            r=check(list(seq))
            counts["primitive_cycles"]+=1
            counts["physical_odd_phases"]+=p
            counts["actual_inversions"]+=r["inversions"]
            counts["clock_gcd_exceeds_one"]+=int(r["g"]>1)
            counts["unsorted_extra_cycles"]+=r["g"]//r["h"]-1
    cases=[(1,1),(5,7),(131,13),(7,25),(1,41),(25,47),(1,55),
           (19,73),(65,83),(1,91),(1015,233),(737,295)]
    print(json.dumps(dict(exhaustive=counts,examples=[check(direct_cycle(y,q))
                      for y,q in cases]),indent=2))
