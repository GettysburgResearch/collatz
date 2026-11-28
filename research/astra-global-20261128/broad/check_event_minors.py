"""Exact positive-source certificates for late Padé windows, convex minors and selected clock columns."""
from fractions import Fraction as F
from math import factorial, gcd
import json
from sympy import Matrix
from check_clock_discrepancy import positive_source, require, small_solution, val2


def tri(j):
    return j*(j-1)//2


def val3(x):
    n,d=F(x).as_integer_ratio()
    require(n!=0, 'nonzero ternary valuation')
    e=0
    while n%3==0:
        n//=3
        e+=1
    while d%3==0:
        d//=3
        e-=1
    return e


def native(u):
    t=[j+a for j,a in enumerate(u)]
    p=[F(2**i,3**a) for i,a in zip(t,u)]
    x,_=positive_source(t,u)
    s=[F(0)]
    for a in p:
        s.append(s[-1]+a)
    return t,p,x,s


def minors(g,H,n,quadratic):
    u=[0]
    for gap in g:
        u.append(u[-1]+gap)
    t,p,x,s=native(u)
    rows=[[p[H+i-k] for k in range(n+1)] for i in range(1,n+1)]
    minors=[F(Matrix([[v for k,v in enumerate(row) if k!=j] for row in rows]).det()) for j in range(n+1)]
    require(all(minors), 'nonzero convex minors')
    y=-(x+1)
    form=sum((-1)**k*mk*(y-s[H-k+1]) for k,mk in enumerate(minors))
    D=sum(u[H-n+2*i] for i in range(n+1))
    require(val2(form)==(n+1)*t[H+1] and val3(form)==-D,'exact binary and ternary rearrangements')
    G=abs(gcd(*(z.numerator for z in minors)))
    while G%2==0: G//=2
    while G%3==0: G//=3
    require((3**D*form).denominator==1 and (3**D*form).numerator%(G*2**((n+1)*t[H+1]))==0,'prime-to-six gcd')
    require(2**((n+1)*t[H+1])*G<=3**D*factorial(n+1)*(x+1+s[H+1])*p[H]**n,'archimedean cofactor bound')
    if quadratic:
        h=g[1]-g[0]
        V=1
        for j in range(1,n): V*=(3**(h*j)-2**(h*j))**(n-j)
        require(G==V, 'exact rational-unit Vandermonde content')
    return {'convex_sources':1,'convex_cofactors':len(minors),'quadratic_contents':int(quadratic),'nontrivial_contents':int(G>1)}


def late(b,h,n,m,mode,offset=0):
    U=lambda j:b*j+h*tri(j)
    T=lambda j:j+U(j)
    W=n*(b+1+h*(n+m))+T(m+n+1)
    K=m
    while T(K)<=W: K+=1
    u=[U(j) for j in range(K+1)]
    for j in range(m,K+1): u[j]+=offset
    require(u[m]>=0,"nonnegative offset clock")
    for j in range(1,m):
        if mode==0: u[j]=0
        elif mode==1: u[j]=u[m]
        else: u[j]=(j*u[m])//m
    t,p,x,s=native(u)
    q,z=F(3,2)**h,F(2**(b+1),3**b)
    c=[F(1)]
    for j in range(1,n+1):
        c=[u-q**j*v for u,v in zip(c+[0],[0]+c)]
    D=2**(n*(b+1)+h*n*(n+m))*3**U(m)
    coeff=[D*c[k]*z**(-k)*q**(tri(k)+m*k) for k in range(n+1)]
    a=[F(2**T(j),3**U(j)) for j in range(max(K,n+m)+1)]
    B=sum(coeff)
    A=sum(v*sum(a[:m+k+1]) for k,v in enumerate(coeff))
    ydash=F(3,2)**offset*(-(x+1)-s[m])+sum(a[:m])
    binary_clear=2**max(offset,0)
    require(all(c.denominator==1 and c.numerator%3**U(m)==0 for c in coeff),'available ternary absorption')
    require((binary_clear*3**U(m))%ydash.denominator==0,'corrected source denominator')
    form=binary_clear*(B*ydash-A)
    require(form.denominator==1 and val2(form)==W+max(offset,0),'exact late physical Padé integer')
    height=(n+m+1)*2**n*(2*3**b)**(n+m)*3**(h*(tri(m)+n*(n+m)))
    require(2**W<=abs(form)/binary_clear<=height*F(3,2)**max(offset,0)*(x+2+2**(m+1)),'late source inequality')
    return {'late_sources':1,'corrected_nonintegral_sources':int(ydash.denominator>1),'late_clocks':K-m+1,'late_omitted_clocks':m,'negative_offsets':int(offset<0),'positive_offsets':int(offset>0)}


def adaptive(keys,reflected):
    M,H=10,7
    r=M-H-1
    G=240
    u=[G*j+(j*j+2*j)%5 for j in range(M+1)]
    v={k:(u[H+1]-u[H+1-k] if reflected else G*k) for k in keys}
    rows=[]
    spreads=[]
    for ell in range(H+1,M):
        exps=[v[k]+u[ell-k] for k in keys]
        lo,hi=min(exps),max(exps)
        rows.append([2**(e-lo)*3**(hi-e) for e in exps]);spreads.append(hi-lo)
    height=3**max(spreads); m=len(keys); B=(2*m*height)**(r//(m-r)+1)
    require((B+1)**m>(m*height*B+1)**r,'active-box count')
    coeff=small_solution(rows,B)
    t,p,x,s=native(u)
    w=[F(2**(k+v[k]),3**v[k]) for k in keys]
    require(all(4*B*b<=a for a,b in zip(w,w[1:])),'selected-column weight slope')
    Q=sum(c*z for c,z in zip(coeff,w)); P=sum(c*z*s[H-k+1] for c,z,k in zip(coeff,w,keys))
    require(Q*P>0, 'sign of the two selected-column sums')
    theta=min(t[M]+min(k+v[k] for k in keys),min(k+v[k]+t[M-k] for k in keys))
    A=max(v[k]+u[H-k] for k in keys)
    I=3**A*(Q*(-(x+1))-P)
    require(I and I.denominator==1 and val2(I)>=theta and abs(I)<=3**A*2*B*w[0]*(x+1+s[H+1]),'active-column finite certificate')
    return {'selected_sources':1,'selected_equations':len(rows),'reflected_sources':int(reflected),'shifted_first_columns':int(keys[0]>0)}


def main():
    counts={}
    def add(data):
        for k,c in data.items(): counts[k]=counts.get(k,0)+c
    for n in (1,2,3,4,5):
        H=n+2
        for h in (1,2,3):
            add(minors([2+h*j for j in range(H+n+1)],H,n,True))
            g=[2];
            for j in range(H+n): g.append(g[-1]+1+(j*j+3*j+1)%(h+2))
            add(minors(g,H,n,False))
    for m in (2,4,7,10):
        for h in (1,3):
            for mode in (0,1,2):
                for offset in (0,-m,m): add(late(2,h,max(1,(87*m)//100),m,mode,offset))
    for keys in ([0,2,4,6],[1,3,5,7],[0,1,4,5,7]):
        for flag in (False,True): add(adaptive(keys,flag))
    require(3**29<2**46 and 42538*46<67507*29 and 67507*50<169*20000,'strict asymptotic interval constants')
    print(json.dumps(counts,sort_keys=True))

if __name__=='__main__': main()
