"""Lebesgue-weighted, complete first-return certificate for real width 397/200."""
from collections import Counter
from fractions import Fraction as F
from math import ceil, floor
import json
from itertools import product


def need(truth, message):
    if not truth:
        raise ValueError(message)

A, B = F(5849625007,10**10), F(5849625008,10**10)
CAP, DEPTH, SCALE = F(197,200), 147, 1024
BITS = [s for s in product((0,1),repeat=4) if sum(s[:2])==sum(s[2:])]
EDGES={m:[[t for t,v in enumerate(BITS) if all(1<=m+x-y<=2 for x,y in zip(u,v))]
           for u in BITS] for m in (1,2)}

def ln_bounds(x, k=32):
    # Positive log series at u=(x-1)/(x+1).
    u = F(x-1,x+1)
    z = sum(2*u**(2*i+1)/(2*i+1) for i in range(k))
    return z,z+2*u**(2*k+1)/((2*k+1)*(1-u*u))


def phase_lines(alpha):
    cuts = [(F(0),(0,0,0)),(F(1),(0,0,1))]
    for t in range(DEPTH+1):
        for which,c in enumerate((F(0),CAP)):
            if t==0 and c==0:
                continue
            h = ceil(t*alpha-c)
            cuts.append((c+h-t*alpha,(t,which,h)))
    cuts.sort()
    need(len(cuts)==len(set(f for f,_ in cuts)),'coincident lines')
    return cuts


def return_word(alpha, f):
    base=[floor(f+j*alpha) for j in range(DEPTH+1)]
    forced=[f+j*alpha-base[j]>CAP for j in range(DEPTH+1)]
    end=next(j for j in range(1,DEPTH+1) if forced[j])
    return forced[0], tuple(1+y-x for x,y in zip(base[:end],base[1:end+1]))


def count_energy(word):
    v = [1]+[0]*(len(BITS)-1)
    for m in word:
        w = [0]*len(BITS)
        for i, nbr in enumerate(EDGES[m]):
            for j in nbr:
                w[j] += v[i]
        v=w
    return v[0]


def slice_frequencies(alpha):
    cuts=phase_lines(alpha)
    freq=Counter()
    nonreturn_max=0
    profiles=[]
    for (lo,_),(hi,_) in zip(cuts,cuts[1:]):
        for t,wt in [(lo,F(0)),((lo+hi)/2,hi-lo)]:
            forced,word=return_word(alpha,t)
            profiles.append((forced,word))
            if forced:
                E=count_energy(word)
                freq[(len(word),E)] += wt
            else:
                nonreturn_max=max(nonreturn_max,len(word))
    need(sum(freq.values())==1-CAP, 'forced mass')
    need(sum(n*x for (n,E),x in freq.items())==1,'all-site renewal mass')
    return ([name for _,name in cuts],profiles,nonreturn_max,freq)


def discretized_excess(n,E):
    # Least integer k with E^SCALE <= 3^(n*SCALE+k).
    u = E**SCALE
    lo,hi=-n*SCALE, n*SCALE
    need(1<u<=3**(n*SCALE+hi),'power comparison bracket')
    while hi-lo>1:
        k=(lo+hi)//2
        if u<=3**(n*SCALE+k):
            hi=k
        else:
            lo=k
    return hi


def run():
    l2,h2=ln_bounds(2); l3,h3=ln_bounds(3)
    need(1+A < l3/h2 <= h3/l2 < 1+B, 'logarithm ratio not bracketed')
    ua,va,da,fa=slice_frequencies(A)
    ub,vb,db,fb=slice_frequencies(B)
    need(ua==ub and va==vb and da==db and set(fa)==set(fb),'changing arrangement')
    ks={t:discretized_excess(*t) for t in fa}
    ua=1+sum(v*ks[t]/SCALE for t,v in fa.items())
    ub=1+sum(v*ks[t]/SCALE for t,v in fb.items())
    # Each return type's total mass is affine in alpha across the closed slab.
    need(max(ua,ub)<F(9999,10000), 'exponent margin')
    return dict(width='397/200',alpha_bracket=[str(A),str(B)],
        intercept_cells_including_point_faces=len(va),max_initial_free_delay=da,
        upper_exponent='9999/10000', log3_excess_scale=SCALE,
        upper_exponent_at_slope_bracket_ends=[str(ua),str(ub)],
        returns=[dict(length=n,energy=str(E),k=ks[(n,E)],
                      left_mass=str(fa[(n,E)]),right_mass=str(fb[(n,E)])) for n,E in sorted(fa)])

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
