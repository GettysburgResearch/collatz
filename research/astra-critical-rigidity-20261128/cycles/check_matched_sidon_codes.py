"""Finite mixed-alphabet entropy and actual matched calendar checks."""
import json
from collections import Counter
from itertools import combinations_with_replacement, product
from math import log2

from check_rational_six_sum import require


def calendar(P, B, lo, hi, scale):
    n = 3*P+1
    alpha = B-P
    active = [lo*P <= (t*B % P)*scale <= hi*P for t in range(n)]
    starts = [t for t in range(n-1)
              if active[t] and active[t+1] and (t*B % P)+alpha<P]
    require(all(v-u>1 for u,v in zip(starts,starts[1:])), "true disjoint pairs")
    require(all((t*B % P)*scale >=lo*P and
                ((t*B % P)+alpha)*scale <=hi*P for t in starts),
            "pair interval")
    exact = sum(lo*P<=i*scale and (i+alpha)*scale<=hi*P for i in range(P))
    require(len(starts) == 3*exact, "three reduced laps, exact pair count")
    singles=sum(active)-2*len(starts)
    require(singles>=0, "physical singleton count")
    return dict(P=P,B=B,interval=[lo,hi,scale],rows=n,pairs=len(starts),singles=singles)


def profile_entropy(counts):
    t=sum(counts)
    return sum(c*log2(t/c) for c in counts if c)/t


def code(qs, order):
    words=list(product(*(range(q) for q in qs)))
    # Add complete words only when cross sums, including doubles, remain unique.
    def signature(a,b):
        return tuple(tuple(sorted((x,y))) for x,y in zip(a,b))
    C=[]; sums=set()
    for i in order:
        w=words[i]
        new={signature(w,v) for v in C+[w]}
        if new.isdisjoint(sums):
            C.append(w); sums.update(new)
    require(len(sums)==len(C)*(len(C)+1)//2, "true multiset Sidon code")
    tested=0
    for t in range(len(qs)+1):
        fibers={}
        for w in C:
            fibers.setdefault(w[:t],[]).append(w)
        allpairs=[(u,v) for V in fibers.values() for u in V for v in V]
        D=[tuple(None if a==b else (a,b) for a,b in zip(u[t:],v[t:]))
           for u,v in allpairs]
        mult=Counter(D)
        require(all((k==(None,)*(len(qs)-t) and h==len(C)) or h==1
                    for k,h in mult.items()), "all output fibers exact")
        require(abs(log2(len(allpairs))-profile_entropy(mult.values())
                    -len(C)/len(allpairs)*log2(len(C)))<1e-10,
                "joint suffix difference entropy decomposition")
        for j,q in enumerate(qs[t:]):
            counts=Counter(row[j] for row in D)
            require(q*counts[None]>=len(allpairs) and
                    profile_entropy(counts.values()) <= (2-1/q)*log2(q)+1e-10,
                    "each physical difference alphabet entropy cap")
        tested+=len(allpairs)
    # Ternary symbol codes are 00,01,11, making their integer two-bit
    # sums distinct on each unordered symbol-pair.
    tri=[(0,0),(0,1),(1,1)]
    require(len({(tri[a][0]+tri[b][0],tri[a][1]+tri[b][1])
                 for a,b in combinations_with_replacement(range(3),2)})==6,
            "actual matched states")
    return dict(alphabets=qs,words=len(C),ordered_pairs_across_prefixes=tested)


if __name__=="__main__":
    codes=[]
    for qs in ((3,3,2),(3,2,2,2),(3,3,3,2),(3,3,2,2,2)):
        n=1
        for q in qs:n*=q
        for order in (range(n),range(n-1,-1,-1),sorted(range(n),key=lambda i:(17*i)%n)):
            codes.append(code(qs,order))
    cases=[(41,65,1,15,16),(306,485,1,31,32),(306,485,9,23,32),
           (306,485,9,91,100),(41,65,20,80,100)]
    print(json.dumps(dict(codes=codes,calendars=[calendar(*c) for c in cases]),indent=2))
