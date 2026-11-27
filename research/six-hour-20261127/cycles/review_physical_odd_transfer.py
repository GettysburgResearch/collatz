"""Independent physical-depth and earlier-source checks, using rational arithmetic."""
from fractions import Fraction as Q
from itertools import product
from math import gcd, prod
import json

def divpower(k):
    return Q(2)**k

def logunit(v, terms=23):
    assert 1 <= v <= 2
    z=(v-1)/(v+1)
    low=2*sum(z**(2*j+1)/(2*j+1) for j in range(terms))
    return low,low+2*z**(2*terms+1)/((2*terms+1)*(1-z*z))

def lg(v):
    v=Q(v)
    k=v.numerator.bit_length()-v.denominator.bit_length()
    if v<divpower(k):k-=1
    lo,hi=logunit(v/divpower(k))
    lo2,hi2=logunit(Q(2))
    den=10**9
    return Q((den*(k+lo/hi2)).__floor__(),den),Q((den*(k+hi/lo2)).__ceil__(),den)

def source_bound(R,delta,M):
    K=3*R/2+Q(1,1000);rho=3*delta;sigma=100*rho
    gamma,G=lg(3); alpha,A=1/G,1/gamma
    low,high=lg(K/3); d,D=low/G,high/gamma
    p=max(0,d-1+alpha);P=max(0,D-1+A)
    s,S=d-2*P,D-2*p
    cap=S+G*P
    J=s*lg(Q(8,3))[0]+p*lg(Q(27,5))[0]
    entropy=rho*(lg(1/rho)[1]+2)
    upper=Q(4,3)*(cap-J*(1-sigma)/(4+sigma)+entropy+9*rho)
    grid=10**5
    upper=Q((grid*upper).__ceil__(),grid)
    assert upper<Q(1)/(M+Q(1,1000))
    assert Q(3,2)*rho/(4*(1+rho))>delta
    return dict(K=str(K),rho=str(rho),source_exponent_upper=str(upper),lower_exponent=str(1/(M+Q(1,1000))))

def odd_period(word):
    n=len(word);A=sum(word);den=2**A-3**n
    if den<=0 or any(word==word[i:]+word[:i] for i in range(1,n)):return None
    if word!=min(word[i:]+word[:i] for i in range(n)):return None
    B=0;h=0
    for e in word:
        B=3*B+2**h
        h+=e
    g=gcd(B,den);N=B//g;d=den//g;ans=[]
    for e in word:
        ans.append(Q(N,d))
        N0=3*N+d
        assert (N0&-N0)==2**e
        N=N0//2**e
    assert Q(N,d)==ans[0] and len(set(ans))==n
    return ans,d

def main():
    rows=[(Q(12,5),Q(1,5000),Q(5116201,10**6)),(Q(5,2),Q(1,10000),Q(5116201,10**6)),(Q(3),Q(1,100000),Q(3)),(Q(31,10),Q(1,10000000),Q(3))]
    res=[source_bound(*row) for row in rows]
    count=arcs=charges=active=0
    for n in range(1,7):
        for w in product(range(1,4),repeat=n):
            cy=odd_period(w)
            if cy is None:continue
            vs,d=cy;count+=1;s=min(vs);A=sum(w)
            corr=[1+1/(3*v) for v in vs];lap=prod(corr)
            for i in range(n):
                v=vs[i];h=0;num=Q(1)
                for k in range(n+1):
                    j=(i+k)%n
                    u=divpower(n*h-k*A)*(vs[j]/v)**n
                    assert u==num**n/lap**k
                    bound=max(corr)**(k*(n-k))
                    assert 1/bound<=u<=bound
                    arcs+=1
                    h+=w[j];num*=corr[j]
            if s<1:continue
            sh=[]
            for i,(v,e) in enumerate(zip(vs,w)):
                sh.append(v)
                for k in range(1,e):
                    sh.append((3*v+1)/2**k)
            assert len(sh)==A
            for K in [Q(101,100),Q(6,5),Q(3,2),Q(2),Q(3),*(3*r[0]/2+Q(1,1000) for r in rows)]:
                np=sum(v>K*s for v in sh)
                no=sum((3*v+1)/2>K*s for v in vs)
                assert np<=2*no
                charges+=1;active+=int(np>0)
    eta=Q(1,1000);tau=Q(1,10000);delta=Q(1,100000)
    C=(5*eta*Q(2,3)+Q(49,50)*(1-eta)+(4+eta)*20*tau*Q(2,3))/(3+eta)
    assert C==Q(123461,375125)
    assert 1-(3+delta)*C==Q(474076539,37512500000)
    assert eta-delta*(3+eta)-tau*(4+eta)*Q(2,3)==Q(210977,300000000)
    print(json.dumps(dict(primitive_rational_cycles=count,exact_cyclic_arcs=arcs,
      charged_cutoffs=charges,nonempty_high_cutoffs=active,earlier_source_181_rows=res),indent=2))
if __name__=='__main__':main()
