"""All-positive valuation three-grade dyadic energy at width 21/10."""
from collections import defaultdict, Counter
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
import json

N=64; C=Q(1,10)
SL=(Q(584961,10**6),Q(584964,10**6))

def arrangement(a):
    fibers=defaultdict(list)
    for i in range(N+1):
        for name,v in [('wrap',0),('cap',C)]:
            x=v-i*a;fibers[x%1].append((name,i,x//1))
    pts=sorted(fibers);end=pts+[Q(1)]; faces=[p for i,z in enumerate(pts) for p in (z,(z+end[i+1])/2)]
    def schedule(f):
        steps=[]
        for j in range(N):
            new=f+a; m=1+(new>=1);f=new%1;steps.append((m,1+(f<=C)))
        return tuple(steps)
    return [tuple(sorted(fibers[p])) for p in pts],[(1+(v<=C),schedule(v)) for v in faces]

@lru_cache(None)
def adv(z,m,h):
    d=(4>>z[0])+(4>>z[1])-(4>>z[2])-(4>>z[3]); opts=tuple(product(*(range(1+min(h,x+m-1)) for x in z)))
    return d,opts

def energy(h,steps):
    counts={(z,0):1 for z in product(range(h+1),repeat=4)}
    for m,cap in steps:
        out=defaultdict(int)
        for (z,k),cnt in counts.items():
            d,opts=adv(z,m,cap);u=3*k+d
            if u%(1<<m):continue
            nn=u>>m
            for v in opts:out[v,nn]+=cnt
        counts=out
    return sum(counts.values())

def small(h,steps):
    paths=[(z,0) for z in range(h+1)];clock=0
    for m,cap in steps:
        paths=[(t,3*b+(4>>z)*(1<<clock))for z,b in paths for t in range(1+min(cap,z+m-1))];clock+=m
    mod=1<<clock; f=Counter(b%mod for z,b in paths);two=Counter()
    for x,c in f.items():
        for y,k in f.items():two[(x+y)%mod]+=c*k
    assert energy(h,steps)==sum(v*v for v in two.values())

def run():
    assert (1<<1584961)<3**1000000<(1<<1584964)
    a,b=SL;mid=(a+b)/2;r,s=arrangement(mid);assert arrangement(a)==(r,s)==arrangement(b)
    short=set((h,w[:5]) for h,w in s)
    for h,w in short:small(h,w)
    vals=[energy(*t) for t in set(s)];v=max(vals)
    assert v**20<3**(29*N)
    return {'length':N,'width':'21/10','mechanical_rotation_bracket':[str(a),str(b)],'point_and_open_faces':len(s),'distinct_schedules':len(vals),'short_exact_checks':len(short),'max_modular_fourth_energy':v,'min_modular_fourth_energy':min(vals),'power_inequality':'E^20 < 3^(29*64)','height_exponent_lower':'60/29','microscopic_entropy_budget_ratio':'2/31','microscopic_signed_source_upper':'1/18','macroscopic_gap':'3/5.116201 > 1/2'}
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
