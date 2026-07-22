#!/usr/bin/env python3
from __future__ import annotations
import argparse,itertools,json,math
from decimal import Decimal,localcontext
from pathlib import Path

K=3_149_971_404_836;A=4_992_586_555_009;E=A-K
P=(7,191,281,28_591,136_398_329);M=math.prod(P)
N=K//2;W=2*K-A
PRPOS=(2,4,6,23,30,35,39,42,44,47,54,59,61,64,71,78,80,83,85,92,95,97,102,107,112,117,121,138,141,143,145,148,150,158,165,167,174,177,179,182,184,186,189)
CHPOS=(0,4,22,69,75,81,87,93,99,134,140,146,163,169,193,199,204,216,228,240,246,252,263,269,281,305,310,328,346,352,357,363,381,387,393,416,422,434,446,452,463)

def mul(x,y,m):
    return (x[0]+y[0],x[1]+y[1],x[2]*y[2]%m,x[3]*y[3]%m,(y[2]*x[4]+x[3]*y[4])%m)
def power(x,n,m):
    z=(0,0,1%m,1%m,0)
    while n:
        if n&1:z=mul(z,x,m)
        x=mul(x,x,m);n//=2
    return z
def mech(ones,length,upper,x0,x1,m):
    if ones==0:return power(x0,length,m)
    if ones==length:return power(x1,length,m)
    q,r=divmod(length,ones)
    if upper:
        y0=mul(x1,power(x0,q-1,m),m);y1=mul(x1,power(x0,q,m),m)
        return mech(r,ones,False,y0,y1,m)
    y0=mul(power(x0,q-1,m),x1,m);y1=mul(power(x0,q,m),x1,m)
    return mech(r,ones,True,y0,y1,m)
def bit(ones,length,i):return ((i+1)*ones)//length-(i*ones)//length
def sites(ones,length,n):
    out=[];prev=-2;i=0
    while len(out)<n:
        a,b=bit(ones,length,i),bit(ones,length,i+1)
        if a!=b and i>prev+1:out.append((i,a,b));prev=i
        i+=1
    return out
def accel_delta(s,m):
    i,a,b=s;pref=(i+1)+((i+1)*E)//K;z=pow(3,K-i-2,m)
    return (z*pow(2,pref,m) if (a,b)==(0,1) else -z*pow(2,pref-1,m))%m
def chart_delta(s,m):
    i,a,b=s;pref=4*i-(i*W)//N;sgn=-1 if (a,b)==(0,1) else 1
    return sgn*21*pow(9,N-i-2,m)*pow(2,pref,m)%m
def summary(kind,m):
    if kind=='pr':return mech(E,K,False,(1,1,3%m,2%m,1%m),(1,2,3%m,4%m,1%m),m)
    return mech(W,N,False,(1,4,9%m,16%m,0),(1,3,9%m,8%m,3%m),m)
def modified(kind,m,positions):
    if kind=='pr':
        ss=sites(E,K,80);mp={s[0]:s for s in ss};return (summary(kind,m)[4]+sum(accel_delta(mp[p],m) for p in positions))%m
    ss=sites(W,N,80);mp={s[0]:s for s in ss};return (summary(kind,m)[4]+sum(chart_delta(mp[p],m) for p in positions))%m
def crt(ms,rs):
    Q=math.prod(ms);x=0
    for m,r in zip(ms,rs):
        t=Q//m;x=(x+r*t*pow(t,-1,m))%Q
    return x
def lower(p,q):return [((i+1)*p)//q-(i*p)//q for i in range(q)]
def cword(vals):
    C=0;e=0
    for a in vals:C=3*C+(1<<e);e+=a
    return e,C
def affmul(x,y):return (y[0]*x[0],y[0]*x[1]+y[1])
def apow(x,n):
    z=(Decimal(1),Decimal(0))
    while n:
        if n&1:z=affmul(z,x)
        x=affmul(x,x);n//=2
    return z
def amechanical(ones,length,upper,x0,x1):
    if ones==0:return apow(x0,length)
    if ones==length:return apow(x1,length)
    q,r=divmod(length,ones)
    if upper:return amechanical(r,ones,False,affmul(x1,apow(x0,q-1)),affmul(x1,apow(x0,q)))
    return amechanical(r,ones,True,affmul(apow(x0,q-1),x1),affmul(apow(x0,q),x1))
def fixed_decimal(kind,positions):
    with localcontext() as ctx:
        ctx.prec=180
        if kind=='pr':
            base=amechanical(E,K,False,(Decimal(3)/2,Decimal(1)/2),(Decimal(3)/4,Decimal(1)/4));ss={s[0]:s for s in sites(E,K,80)};d=Decimal(0)
            for p in positions:
                _,a,b=ss[p];pref=(p+1)+((p+1)*E)//K;term=base[0]*Decimal(2**(pref if (a,b)==(0,1) else pref-1))/Decimal(3**(p+2));d+=term if (a,b)==(0,1) else -term
        else:
            base=amechanical(W,N,False,(Decimal(9)/16,Decimal(0)),(Decimal(9)/8,Decimal(3)/8));ss={s[0]:s for s in sites(W,N,80)};d=Decimal(0)
            for p in positions:
                _,a,b=ss[p];pref=4*p-(p*W)//N;term=base[0]*Decimal(21*(2**pref))/Decimal(9**(p+2));d+=-term if (a,b)==(0,1) else term
        return (base[1]+d)/(Decimal(1)-base[0])
def main():
    ap=argparse.ArgumentParser();ap.add_argument('canonical',type=Path);a=ap.parse_args();data=json.loads(a.canonical.read_text())
    assert data['experiment_id']=='X-8302' and M==data['negative_three_chart']['crt_modulus']
    for n in range(1,10):
      for bits in itertools.product((0,1),repeat=n):
        ce=cc=0;vals=[]
        for b in bits:cc=9*cc+3*b*(1<<ce);ce+=4-b;vals+=(2-b,2)
        ae,ac=cword(vals);D=(1<<ce)-9**n;assert ae==ce and ac==D+2*cc
    ct=0
    for q in range(2,37):
      for p in range(1,q):
       if math.gcd(p,q)>1:continue
       for s in range(2,37):
        for r in range(1,s):
         if math.gcd(r,s)>1 or r*q-p*s!=1 or p*s>=r*q:continue
         u,v=lower(p,q),lower(r,s);x,y=u+v,v+u
         assert x==lower(p+r,q+s) and [i for i,(c,d) in enumerate(zip(x,y)) if c!=d]==[s-1,s]
         assert cword([1+b for b in x])[1]-cword([1+b for b in y])[1]==-(1<<(r+s-1))*3**(q-1);ct+=1
    assert ct==data['farey_mechanical_commutator']['small_neighbor_pairs_checked']
    for kind,positions,key in [('pr',PRPOS,'pr45_quotient_cylinder'),('chart',CHPOS,'negative_three_chart')]:
        rs=[];assert modified(kind,M,positions)==0;rows=data[key]['rows' if kind=='pr' else 'quotient_rows']
        for row,p in zip(rows,P):
            c=modified(kind,p*p,positions);d=(pow(2,A,p*p)-pow(3,K,p*p))%(p*p);assert c==row['C_mod_p2'] and d==row['D_mod_p2'] and c%p==d%p==0
            q=(c//p)*pow(d//p,-1,p)%p;assert q==row['quotient_mod_p'];rs.append(q)
        assert crt(P,rs)==data[key]['crt_quotient_residue']
    for kind,positions,key in [('pr',PRPOS,'pr45_quotient_cylinder'),('chart',CHPOS,'negative_three_chart')]:
        x=fixed_decimal(kind,positions);lo=Decimal(data[key]['fixed_point_lower']);hi=Decimal(data[key]['fixed_point_upper']);assert lo<x<hi and int(x)==data[key]['unique_floor']
    print(json.dumps({'verified':True,'short_chart_words':2**10-2,'farey_pairs':ct,'modular_words':2,'quotient_prime_rows':10},sort_keys=True))
if __name__=='__main__':main()
