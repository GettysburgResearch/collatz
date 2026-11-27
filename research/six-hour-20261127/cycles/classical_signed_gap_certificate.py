"""Dual certificates for orientation charges, signed modular blocks and translated strips."""
from fractions import Fraction as Q
from collections import Counter
from itertools import product
from math import gcd
import json


def branches(u0,u1,w):
    L=Q(121,50); D=max(Q(0),L-min(abs(u0+w),abs(u1+w)))
    cap=Q(6,5)
    if D<=Q(99,50):cap=min(cap,Q(1))
    # Outside this two-grade regime the linear bound is never used as an improvement.
    return min(cap,max(0,(D-1)*Q(5,3)))

def run():
    dual=[(469,137),(455,50),(439,-35),(408,-102),(377,-170),(357,-214),(357,-214),(357,-214)]
    rows=[]
    for j,(theta,slope) in enumerate(dual):
        t=Q(theta,1000);m=Q(slope,1000);lo,hi=Q(j,16),Q(j+1,16)
        best=Q(0)
        for w,u in product(range(-3,3),(lo,hi)):
            g=branches(lo,hi,w);cost=g*((1-t)*(w!=0)+t*(w!=-1));best=max(best,cost-m*(w+u))
        assert best<Q(23,40)
        rows.append({'u_range':[str(lo),str(hi)],'orientation_weight':str(t),'linear_tilt':str(m),'largest_intercept':str(best)})
    M=Q(5116201,1000000);assert Q(23,40)*M<3
    cases=0;checks=0
    for phase,u,w in product((Q(0),Q(1,13),Q(4,13)),(Q(1,13),Q(6,13)),range(-3,3)):
        if not w:continue
        a=Q(7,12);L=Q(121,50);bottom=max(Q(0),-u-w);top=min(L,L-u-w)
        if bottom>top:continue
        opts=[];floors=[];rr=[];correct=(phase-bottom)//1
        for j in range(7):
            flow=phase+j*a;f=flow%1; fp=(f-bottom)%1; M0=j+(flow//1);Mp=j+( (flow-bottom)//1)-correct
            poss=[]
            for z in range(3):
                if not bottom<=f+z<=top:continue
                zp=z+(f-bottom)//1
                assert 0<=fp+zp<=top-bottom and M0-z==Mp-zp+correct
                poss.append(z)
            opts.append(poss);floors.append(M0)
        v=[]
        for word in product(*opts):
            if not all(floors[i+1]-floors[i]+word[i]-word[i+1] in (1,2) for i in range(6)):continue
            delta=[(Q(2)**(-w)-1)*Q(4,2**z) for z in word[:-1]]
            if any(x.denominator!=1 for x in delta):continue
            val=sum(int(delta[j])*3**(5-j)*2**floors[j] for j in range(6));v.append(val)
        vals=Counter(v);pairs=Counter()
        for x,c in vals.items():
            for y,k in vals.items():pairs[x+y]+=c*k
        raw=Counter();mod=Counter();N=2**floors[-1]
        for x,c in pairs.items():
            for y,k in pairs.items():raw[x-y]+=c*k;mod[(x-y)%N]+=c*k
        if mod:
            assert max(mod.values())==mod[0] and max(raw.values())==raw[0]
            assert mod[0]<=len({k//N for k in raw if k%N==0})*raw[0]
            checks+=len(v)
        cases+=1
    return {'orientation_duals':rows,'worst_dual':str(max(Q(x['largest_intercept']) for x in rows)),'certified_average_energy':'23/40','critical_margin':str(3-M*Q(23,40)),'translated_chart_configurations':cases,'admitted_paths_in_tests':checks}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
