"""Finite residue, seam, and exact-clock controls for strict rank convexity."""
from collections import Counter
from itertools import combinations,product
from math import gcd
import json

def require(v,msg):
    if not v:raise ValueError(msg)
def low(x):return x&-x
def run():
    c=Counter();c['ordinary_counterexample_assumptions']=0
    # Integer seam options, including all signs and the indispensable output divisibility.
    d1={4-lowbit for lowbit in (1,2)}
    da={a-2*b+4 for a,b in product((1,2),repeat=2)}
    db={a-8+2*b for a,b in product((1,2),repeat=2)}
    require((d1,da,db)==({2,3},{1,2,3,4},{-5,-4,-3,-2}),'seam sets')
    for where,ds in [('ordinary',range(-2,3)),('penultimate',da),('last',db)]:
        for H,d,m in product(range(-12,13),ds,(1,2) if where=='ordinary' else (2,)):
            v=3*H+d;q=2**m
            if v%q:continue
            t=v//q
            require(not H*t<0,'strict reversal')
            if H<0 and t==0:require((where,H,d)==('penultimate',-1,3),'negative exit')
            if H>0 and t==0:require((where,H,d)==('last',1,-3),'positive exit')
            if H==0 and where=='last':require(t==-1,'last zero creates negative')
            c['admissible_second_difference_interfaces']+=1
    # Raw modulo-four admissibility on unextended labels.
    for length in (3,4):
        for x,g in product(range(1,129),range(1,65)):
            B=[x+i*g for i in range(length)]
            if any(low(u)>2 for u in B):continue
            c['admissible_AP'+str(length)]+=1
            if length==4:require(g%2==0 and len(set(map(low,B)))==1,'AP4 rigidity')
            elif g%2:
                require(list(map(low,B))==[1,2,1],'odd AP3 pattern')
                f=[3*v+low(v) for v in B]
                require(f[2]-2*f[1]+f[0]==-2,'convexity obstruction')
            for m in (1,2):
                f=[3*v+low(v) for v in B];q=2**m
                if not any(v%q for v in f) and g%2==0:
                    z=[v//q for v in f]
                    require(all(q*(v-u)==3*g for u,v in zip(z,z[1:])),'AP propagation')
                    c['integer_progression_transfers']+=1
    # Exhaustive actual rational word model to test identity at every seam.
    # At drift d the label lowbit term is d times ell, so this cannot assert the ordinary sign test.
    for P in range(4,12):
      for s in range(2,P-1):
       if gcd(P,s)!=1:continue
       A=P+s;D=2**A-3**P
       if D<=0:continue
       m=[1+int(r+s>=P) for r in range(P)]
       for tail in product((0,1),repeat=P-1):
        z=(0,)+tail;e=[m[r]+z[r]-z[(r+s)%P] for r in range(P)]
        if min(e)<1:continue
        idx=[(i*s)%P for i in range(P)];h=0;N=0
        for i,r in enumerate(idx):N+=3**(P-1-i)*2**h;h+=e[r]
        a=gcd(N,D);d=D//a;u=N//a;L=[0]*P
        for r in idx:
            L[r]=(2-z[r])*u
            w=3*u+d;require(w%2**e[r]==0,'rational raw date');u=w//2**e[r]
        require(u==N//a,'rational closure')
        Lf=lambda r: (2**(r//P))*L[r%P]
        lf=lambda r:2**(r//P)*(2-z[r%P])
        for r in range(P):
            for k,co in [(1,[-1,1]),(2,[1,-2,1])]:
                src=sum(a*Lf(r+j) for j,a in enumerate(co));dst=sum(a*Lf((r+s)%P+j) for j,a in enumerate(co));dr=sum(a*lf(r+j) for j,a in enumerate(co))
                require(2**m[r]*dst==3*src+d*dr,'extended ranked recurrence')
                if r>=P-k:
                    c['genuine_wrapped_interfaces']+=1
                    bad=sum(a*(2-z[(r+j)%P]) for j,a in enumerate(co))
                    if dr!=bad:c['detect_forgotten_lowbit_doubling']+=1
        c['positive_rational_word_models']+=1
    return dict(c)
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
