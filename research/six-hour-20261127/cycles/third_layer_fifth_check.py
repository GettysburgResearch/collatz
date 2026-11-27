"""Exact two-edge path, rare-rank geometry, and a genuine above-two word control."""
from fractions import Fraction as Q
from itertools import product
from math import gcd
import json


def run():
    alpha_lo,alpha_hi=Q(584961,10**6),Q(584964,10**6);c=Q(1,100000)
    # Before an eligible phase f, the previous mechanical phase is 1+f-alpha;
    # after it, the next is f+alpha. Both are outside the eligible arc.
    assert c<alpha_lo and c<1-alpha_hi
    up=[[int(y==x or y==x+1) for x in range(2)] for y in range(3)]
    down=[[int(y==x or y==x-1) for x in range(3)] for y in range(2)]
    pairs=[[sum(down[y][u]*up[u][x] for u in range(3)) for x in range(2)] for y in range(2)]
    assert pairs==[[2,1],[1,2]] and all(sum(v)==3 for v in pairs)
    for m in [1,2]:
        for s in range(19):
            # Fine roots of 3u=s/19 double bijectively to roots of 3u=2s/19.
            native={(2*(s+19*j))%57 for j in range(3)}
            comparison={i for i in range(57) if (3*i-6*s)%57==0}
            assert native==comparison and len(native)==3
    charge=3*3**5/Q(9,100)/4; assert charge==2025
    # e^8 > 2025 follows from e>8/3 (finite Taylor sum through order 4).
    assert sum(Q(1,a) for a in (1,1,2,6,24))>Q(8,3) and Q(8,3)**8>charge
    assert Q(1,7000)-8*c>Q(1,16000)
    assert Q(11,10)/20000 < Q(1,16000)
    # Physical fourth-height-free witness strictly outside W<2 but inside the new class.
    p,q=111457,190537
    assert gcd(p,q)==1 and alpha_lo<Q(p,q)<alpha_hi and (1<<(p+q))>3**q
    i=pow(p,-1,q);z=[0]*q
    for h,k in ((-1,1),(0,2),(1,1),(2,1)):z[(i+h)%q]=k
    es=[]
    for j in range(q):
        m=1+((j+1)*p//q-j*p//q)
        es.append(m+z[j]-z[(j+1)%q])
    assert set(es)=={1,2} and sum(es)==p+q and max(z)==2
    scale=[(j*p)%q+q*z[j] for j in range(q)]
    assert min(scale)==0 and max(scale)==2*q+1 and Q(max(scale),q)<2+c
    return {'eligible_arc':str(c),'mechanical_bracket':[str(alpha_lo),str(alpha_hi)],'three_to_two':down,'two_to_three':up,'entrywise_absolute_composite':pairs,'two_edge_cost_ratio':int(charge),'single_site_natural_log_cost_upper':8,'remaining_natural_gap_lower':'1/16000','base_three_gap':'1/20000','above_two_positive_rational_word':{'period':q,'clock':p+q,'grade_two_site':i,'real_width':str(Q(max(scale),q)),'period_primitive_by_coprime_clocks':True}}

if __name__=='__main__': print(json.dumps(run(),sort_keys=True,indent=2))
