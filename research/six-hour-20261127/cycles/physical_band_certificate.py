"""Exact sparse physical-band graph repair, full source translation and margin checks."""
from fractions import Fraction as Q
from itertools import product
from math import comb
from collections import Counter
import json


def pathcheck(grades,alph,phase,stats):
    n=len(grades)-1;f=[(phase+i*alph)%1 for i in range(n+1)]
    m=[1+int(f[j]+alph>=1) for j in range(n)]
    es=[m[j]+grades[j]-grades[j+1] for j in range(n)]
    if min(es)<1:return
    cap=[1+int(x<=Q(1,100000)) for x in f]
    clipped=[min(x,k) for x,k in zip(grades,cap)]
    # Distance on the finite chronologically ordered vertex path is explicit.
    forward=[0]+[int(v==1) for v in m];backward=[0]+[int(v==2) for v in m]
    for i in range(1,n+1):forward[i]+=forward[i-1];backward[i]+=backward[i-1]
    def dist(i,j):return forward[j]-forward[i] if i<=j else backward[i]-backward[j]
    u=[min(v+dist(i,j) for j,v in enumerate(clipped)) for i in range(n+1)]
    pred=[m[j]+u[j]-u[j+1] for j in range(n)]
    assert min(pred)>=1 and max(pred)<=2
    bad={i for i,e in enumerate(es) if e>=3}
    for i,(a,b) in enumerate(zip(clipped,u)):
        if a!=b: assert any(abs(i-j)<=6 for j in bad)
    stats['positive_paths']+=1;stats['nontrivial_graph_repairs']+=clipped!=u
    if grades[0]!=u[0] or grades[-1]!=u[-1]:return
    M=1<<sum(es);assert M==1<<sum(pred);x=y=C=0;d=7;t=q=0
    for j in range(n):
        inv=d*pow(3,-j-1,M);x-=inv*(1<<t);y-=inv*(1<<q)
        if grades[j]!=u[j]:C-=inv*((1<<t)-(1<<q))
        else:assert t==q
        t+=es[j];q+=pred[j]
    assert (x-y-C)%M==0;stats['end_matched_translations']+=1;stats['nonzero_translations']+=C%M!=0


def run():
    c=Q(1,10**10);eta=Q(1,10**6);tau=Q(1,10**7);g=Q(4,3)-Q(1,20000)
    upper=(6*eta+g*(1-eta)+(5+eta)*26*tau)/(4+eta)
    target=1-(3+c)*upper;assert target>0 and (4+eta)*c<eta/2
    weights=1-26*c-13*c/tau;assert weights>Q(98,100)
    for j in range(1,128):assert comb(2*j+2,j)<=2**(4*j)
    stats=Counter()
    for phase in [Q(0),Q(1,100000),Q(1,3),Q(5,12),Q(3,4)]:
        for z in product(range(4),repeat=6):pathcheck(z,Q(7,12),phase,stats)
    return {'global_delta':str(c),'physical_threshold':'4*2^(1/200000)','good_start_fraction_lower':str(weights),'sparse_source_exponent_upper':str(upper),'product_slack':str(target),'fixed_stage_controls':dict(stats),'ratio_four_located_exponent_limit':'1/3 - 1/80000','full_bounded_branch_located_exponent_limit':'2/5'}

if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
