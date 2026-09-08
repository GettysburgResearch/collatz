#!/usr/bin/env python3
"""Independent bounded integration-review checks. No repository modules imported."""
from __future__ import annotations
from collections import deque
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import isqrt
import argparse, json, time


def need(ok, why):
    if not ok: raise ValueError(why)


def val(n, p):
    n=abs(n); need(n!=0, 'valuation at zero')
    e=0
    while n%p==0: n//=p; e+=1
    return e


def T(n): return (3*n+1)//2 if n%2 else n//2

def g(n): return n*n//3**val(n,3) if n else 0

@lru_cache(None)
def R(n):
    if n==1: return 0
    h=val(2*n+1,3)
    return min(g((3**a-2**(a+1))*n+3**a-2**a) for a in {0,1,2,h})

@lru_cache(None)
def Gamma(n):
    if n==1:return 0
    best=g(n); ks=[0]; x=n; k=0; power=1
    while power*4<=best:
        power*=4; k+=1; x=T(x)
        if x==n:continue
        score=power*g(x-n)
        if score<best:best=score;ks=[k]
        elif score==best:ks.append(k)
    return best


def Gamma_detail(n):
    if n==1:return 0,[0]
    best=g(n); ks=[0]; x=n
    for k in range(1,n.bit_length()):
        x=T(x)
        if x==n:continue
        score=4**k*g(x-n)
        if score<best:best=score;ks=[k]
        elif score==best:ks.append(k)
    return best,ks


def affine(bits):
    P,A,D=1,0,1
    for b in bits:
        if b:P,A=3*P,3*A+D
        D*=2
    return P,D,A


def rho(n):
    if n==1:return 0
    best=min(g(n),g(n-1),g(n+5)); level=[(1,0)];D=1
    while n*(D*2)<4*best:
        need(D < 2**20, 'bounded word budget exhausted; no rank conclusion')
        next_level=[]
        for p,a in level:next_level.extend(((p,a),(3*p,3*a+D)))
        level=next_level;D*=2
        for p,a in level:
            if 4*p>=5*D:best=min(best,g((p-D)*n+a))
    return best


def P(n):return g(2*n+1)


def section_fan(y):
    h=val(2*y+1,3);u=(2*y+1)//3**h
    out=[2**(j+1)*3**(h-j)*u-2 for j in range(h)]
    z=2**h*u-1
    if z%3==1:out.append(z)
    return out


def inverse_ball(y,d):
    ball={y};front={y}
    for _ in range(d):
        front={x for v in front for x in section_fan(v)}-ball
        ball|=front
    return ball


def inverse_min(y,d):
    if not d:return P(y)
    h=val(2*y+1,3);u=(2*y+1)//3**h
    children=[2**(h-gap+1)*3**gap*u-2 for gap in range(1,min(h+1,4*d-2))]
    z=2**h*u-1
    if z%3==1:children.append(z)
    return min([P(y)]+[inverse_min(x,d-1) for x in children])


def rank_ball(Y):
    # Enumerate every component and both possible signs, independently of the
    # minimizer-fiber theorem. Each omitted component is ruled out by g(z)>=z.
    out=set(); a=0
    while True:
        d,c=3**a-2**(a+1),3**a-2**a
        if a>=2 and 2*d+c>Y:break
        p=1
        while p<=Y:
            hi=isqrt(Y//p)
            if a<2:
                for u in range(1,hi+1):
                    if u%3:
                        n=(-p*u-c)//d
                        if n>=2:out.add(n)
            else:
                lo=max(1,(2*d+c+p-1)//p)
                residue=(c*pow(p,-1,d))%d if d>1 else 0
                for u in range(lo+(residue-lo)%d,hi+1,d):
                    if u%3:out.add((p*u-c)//d)
            p*=3
        a+=1
    need(all(R(n)<=Y for n in out),'rank ball includes invalid source')
    return sorted(out)

@lru_cache(None)
def A(n):
    need(n>1,'absorbed acceleration source')
    mode=val(n+1,2) if n%2 else 0
    x=n; clock=0; peak=n
    while True:
        for b in [1]*mode+[0]:
            need(x>1 and x%2==b,'illegal module')
            x=T(x);clock+=1;peak=max(peak,x)
        if x==1 or (val(x+1,2) if x%2 else 0)!=mode:return x,clock,peak


def safe(n):return n>1 and 4*R(A(n)[0])<=R(n)

@lru_cache(None)
def B(n):
    need(n>1 and not safe(n),'wrong unsafe input')
    y,clock,peak=A(n); count=0
    while y>1 and safe(y):
        prev=R(y);y,c,p=A(y);clock+=c;peak=max(peak,p);count+=1
        need(4*R(y)<=prev,'safe decrease')
    return y,clock,count,peak


def forest_check(power):
    ball=rank_ball(2**power);roots=[n for n in ball if not safe(n)]
    edges={};labels={1:(0,0,1)}
    for n in roots:
        x=n;path=[];seen=set()
        while x not in labels:
            need(x not in seen,'cycle in finite forest');seen.add(x)
            edge=B(x);edges[x]=edge;path.append(x);x=edge[0]
            need(len(path)<2000,'review path resource cap')
        for x in reversed(path):
            y,c,sg,p=edges[x];l,k,pk=labels[y];labels[x]=(l+1,k+c,max(pk,p))
    # Independent literal full T orbit for extreme roots; counts retain every B edge.
    J=max(labels[n][0] for n in roots);K=max(labels[n][1] for n in roots);peak=max(labels[n][2] for n in roots)
    jm=next(n for n in roots if labels[n][0]==J);pm=next(n for n in roots if labels[n][2]==peak)
    for n in (jm,pm):
        x=n;c=0;p=n
        while x!=1:x=T(x);c+=1;p=max(p,x);need(c<10000,'literal review cap')
        need((c,p)==labels[n][1:],'literal T and B labels disagree')
    # Classify first exits separately by following the finite rank-ball graph.
    rootset=set(roots);cls={}
    for n in roots:
        x=n;path=[];seen=set()
        while x in rootset and x not in cls:
            if x in seen:break
            seen.add(x);path.append(x);x=B(x)[0]
        kind=cls.get(x, 'kill' if x==1 else ('cycle' if x in seen else 'exit'))
        for x in path:cls[x]=kind
    return dict(power=power,ball=len(ball),unsafe=len(roots),forest=len(edges),outside=sum(R(n)>2**power for n in edges),
                B_clock=J,T_clock=K,peak=peak,largest_initial=max(ball),first_clock_source=jm,first_peak_source=pm,
                exits=sum(v=='exit' for v in cls.values()),cycles=sum(v=='cycle' for v in cls.values()))


def small_checks():
    rows=[]; guards=0; failures=[]; relation=[]
    for n in range(2,8193):
        z=Gamma(n); full,ks=Gamma_detail(n)
        need(z==full and n<=z<=n*n,'prefix bound/evaluator')
        if (0 in ks and n%2==0) or any(k and (iterate(n,k)-n)%2==0 for k in ks):
            need(Gamma(T(n))<z,'rotation guard');guards+=1
        if Gamma(T(n))>=z:failures.append(n)
        if n<=1024:
            r=rho(n)
            need(n-1<=r<=R(n),'rho bounds')
            if len(relation)<20 and r!=z:relation.append([n,r,z])
        rows.append([n,z,ks])
    powers=[]
    for h in range(1,41):
        n=3**h; gy=Gamma(T(n))
        need(Gamma(n)==n and Gamma_detail(n)[1]==[0],'power baseline')
        need(gy**10>n**11,'power spike 11/10')
        powers.append([h,n,gy])
    neg=[]
    for radius in range(11):
        # reconstruct actual physical path of every negative node to -2
        ball=inverse_ball(-2,radius);maximum=0
        for n in ball:
            x=n;q=0;k=0
            while x!=-2:
                q+=x%2!=0;x=T(x);k+=1;need(k<10000,'negative path cap')
            maximum=max(maximum,q+val(2*n+1,3))
        budget=maximum+1
        need(radius//3+2<=budget<=4*radius+2,'negative budget')
        neg.append([radius,len(ball),budget])
    comparisons=0
    for y in range(4,901,3):
        for radius in range(4):
            need(inverse_min(y,radius)==min(map(P,inverse_ball(y,radius))),'pruning minimum')
            comparisons+=1
    need(4**9>3**11,'kappa margin')
    need(3**13>34**2*1296 and 4352*3**18>5992704*2**18,'rho phase margins')
    need((2**19-262087)**2-3*151316**2==59768833,'entropy margin')
    need(2**19*3**20>5**20 and 30**20<2*29**20,'spectrum margins')
    need(3**17<2**27 and 3**2>2**3,'9/4 ceiling margins')
    witness=[Gamma_detail(x) for x in (1932103,2445319,3667979)]
    need(iterate(1932103,6)==2445319 and T(2445319)==3667979,'switch physical example')
    need([w[0] for w in witness]==[1479901446144,29265629184,4484692426800],'switch rank values')
    return dict(source_checks=len(rows),rotation_guards=guards,first_non_decreases=failures[:20],rho_Gamma_controls=relation,
                prefix_transcript=sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest(),
                power_spikes=powers,negative_budgets=neg,inverse_comparisons=comparisons,switch=witness)


def iterate(n,k):
    for _ in range(k):n=T(n)
    return n


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--forest',action='store_true');args=ap.parse_args()
    if args.forest:out={'forests':[forest_check(p) for p in (24,28,32)]}
    else:out=small_checks()
    print(json.dumps(out,sort_keys=True,indent=2))

if __name__=='__main__':main()
