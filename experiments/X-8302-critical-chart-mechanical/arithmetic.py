from __future__ import annotations
import math
from mechanical import (
    A, ACH, CHART_MASK_HI, CHART_MASK_LO, EXCESS, FACTORS, K, MODULUS,
    NCH, accel_delta, accel_letter, chart_delta, chart_letter,
    disjoint_sites, identity, mechanical_product,
)
def is_prime64(n:int)->bool:
    if n<2:return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%p==0:return n==p
    d=n-1;s=0
    while d%2==0:s+=1;d//=2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a%n==0:continue
        x=pow(a,d,n)
        if x in (1,n-1):continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True
def exact_order_2(p:int)->int:
    if not is_prime64(p):raise AssertionError(f'nonprime {p}')
    n=p-1;fac=[];d=2
    while d*d<=n:
        if n%d==0:
            fac.append(d)
            while n%d==0:n//=d
        d+=1 if d==2 else 2
    if n>1:fac.append(n)
    order=p-1
    for f in fac:
        while order%f==0 and pow(2,order//f,p)==1:order//=f
    assert pow(2,order,p)==1
    return order
def crt_pairwise(moduli,residues):
    M=math.prod(moduli);x=0
    for m,r in zip(moduli,residues):
        q=M//m;x=(x+r*q*pow(q,-1,m))%M
    return x
def quotient_rows(kind:str, positions, floor_value:int):
    if kind=='accel':
        ones,length=EXCESS,K;sites=disjoint_sites(ones,length,80);posmap={s[0]:i for i,s in enumerate(sites)};idxs=[posmap[p] for p in positions]
        letter=accel_letter;delta=accel_delta
    else:
        ones,length=ACH,NCH;sites=disjoint_sites(ones,length,80);mask=CHART_MASK_LO+(CHART_MASK_HI<<64);idxs=[i for i in range(80) if mask>>i&1]
        letter=chart_letter;delta=chart_delta
    rows=[];res=[]
    for p in FACTORS:
        mod=p*p
        base=mechanical_product(ones,length,False,letter(0,mod),letter(1,mod),identity(mod),lambda x,y:x*y).constant
        c=(base+sum(delta(sites[i],mod) for i in idxs))%mod
        d=(pow(2,A,mod)-pow(3,K,mod))%mod
        assert c%p==0 and d%p==0 and (d//p)%p
        cp,dp=c//p,d//p;q=cp*pow(dp,-1,p)%p;res.append(q)
        rows.append({'prime':p,'C_mod_p2':c,'D_mod_p2':d,'C_over_p_mod_p':cp,'D_over_p_mod_p':dp,'quotient_mod_p':q})
    return rows,crt_pairwise(FACTORS,res),floor_value%MODULUS,(floor_value+1)%MODULUS
