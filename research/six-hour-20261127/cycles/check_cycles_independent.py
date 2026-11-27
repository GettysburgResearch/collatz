"""Independent direct-word checks. No imports from proposed manuscripts."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import gcd, lcm, prod
import json


def insist(test):
    if not test:
        raise ArithmeticError('control failed')


def divisors(n):
    return [j for j in range(1,n+1) if n%j==0]


def native(w):
    a=sum(w); b=len(w); D=(1<<b)-3**a
    P=1
    C=0
    for k,odd in enumerate(w):
        if odd:
            C=3*C+(1<<k)
            P*=3
    insist(P==3**a and D>0)
    common=gcd(C,D); d=D//common; y=C//common
    initial=y; odd_heights=[]
    for odd in w:
        insist((y&1)==odd and gcd(y,d)==1)
        if odd: odd_heights.append(y)
        y=(3*y+d if odd else y)//2
    insist(y==initial)
    return D,C,d,odd_heights


def gap_word(w):
    dates=[k for k,z in enumerate(w) if z]
    return [r-l for r,l in zip(dates[1:]+[len(w)+dates[0]],dates)]


def resonant(a,b,primes):
    R=prod(primes); n=6*R; B=n//3
    periods=[n//2]+[n//(3*r) for r in primes]; L=len(periods)
    blocks=[]
    for j in range(n):
        bits=[]
        for t in periods:
            e=int(j%t==0); bits.extend((1-e,e))
        bits.extend([1]*(a-L)); bits.extend([0]*(b-a-L)); blocks.extend(bits)
    D,C,d,nums=native(blocks); gaps=gap_word(blocks); p=len(gaps)
    insist(len(set(nums))==p)
    dates=[0]
    for e in 2*gaps: dates.append(dates[-1]+e)
    J=[i for i in range(p) if dates[i+a*B]-dates[i]!=b*B]
    spacing=[(J[(j+1)%len(J)]-i)%p for j,i in enumerate(J)]
    insist(len(J)==4 and max(spacing)*3==p)
    # Rebuild the signed residual using its literal defect-row formula after the widest cut.
    origin=J[(spacing.index(max(spacing))+1)%len(J)]; g=gaps[origin:]+gaps[:origin]
    E=[0]
    for e in g*2: E.append(E[-1]+e)
    Rz=p-max(spacing); u=b*B; v=a*B; base=min(u,E[v]); Z=0
    for i in range(Rz+1):
        if E[i+v]-E[i]!=u:
            Z+=3**(Rz-i)*((1<<(E[i]+u-base))-(1<<(E[i+v]-base)))
    insist(Z%2==1)
    P=3**a; Q=1<<b; M={}; ks=[3**(L-1-i)*4**i for i in range(L)]
    for k in divisors(n):
        M[k]=(Q**k-P**k)//prod(M[j] for j in M if k%j==0)
    active=[k for k in M if any(t%k==0 for t in periods)]; inactive=set(M)-set(active)
    K={k:sum((n//t)*z for t,z in zip(periods,ks) if t%k==0) for k in active if k>1}
    insist(C%prod(M[k] for k in inactive)==0)
    insist(all(k0%gcd(C,M[k])==0 for k,k0 in K.items()))
    remaining={k for k in M if periods[0]%k==0 and B%k!=0}
    insist(Z%prod(M[k] for k in set(M)-remaining)==0)
    insist(gcd(D,Z)==gcd(D,(Q**B-P**B)*C))
    overlaps=[(i,j,gcd(M[i],M[j])) for i,j in combinations(M,2) if gcd(M[i],M[j])!=1]
    return {'clocks':[p,b*n],'prime_set':primes,'denominator_bits':d.bit_length(),'residual_gcd_bits':gcd(D,Z).bit_length(),'overlapping_orders':overlaps,'mixed_activity_overlap':sum((i in active)!=(j in active) for i,j,_ in overlaps),'inactive_joint_overlap':sum(i in inactive and j in inactive for i,j,_ in overlaps)}


def dense_all(a,b,q,r):
    n=q*r; p=a*n; ds=[(i*b+a-1)//a for i in range(a+1)]; base=[v-u for u,v in zip(ds,ds[1:])]
    centers=[i for i in range(1,a) if base[i-1:i+1]==[1,2]]
    groups=[q if j%2==0 else r for j in range(len(centers))]
    bits=[(i,j) for i,t in zip(centers,groups) for j in range(t)]
    eligible=0; least_d=None; record=Counter(); hamming=[0]*p
    P=3**a; Q=1<<b; bound=lcm(Q**q-P**q,Q**r-P**r)
    for assignment in product(range(2),repeat=len(bits)):
        chosen=dict(zip(bits,assignment)); gaps=[]
        for j in range(n):
            window=base.copy()
            for i,t in zip(centers,groups):
                z=chosen[i,j%t]; window[i-1]+=z; window[i]-=z
            gaps.extend(window)
        word=[]
        for e in gaps: word.extend([1]+[0]*(e-1))
        D,C,d,ys=native(word); insist(bound%d==0)
        W=[0]; hh=0
        for i,e in enumerate(gaps,1): hh+=e; W.append(a*hh-b*i)
        insist(max(W)-min(W)<2*a)
        mask=sum((z-1)<<i for i,z in enumerate(gaps)); full=(1<<p)-1
        hvals=[(mask^((mask>>v)|((mask<<(p-v))&full))).bit_count() for v in range(1,p)]
        for v,h in enumerate(hvals,1): hamming[v]+=h
        if min(hvals)*32>=p:
            eligible+=1; least_d=d if least_d is None else min(d,least_d)
            E=[0]
            for t in 2*gaps:E.append(E[-1]+t)
            for v,h in enumerate(hvals,1):
                hist=Counter(E[i+v]-E[i] for i in range(p)); miss=p-max(hist.values()); insist(2*miss>=h and 64*miss>=p)
            insist(len(set(ys))==p)
        record[min(hvals)]+=1
    total=2**len(bits); insist(min(hamming[1:])*16>=p*total)
    return {'clock':[p,b*n],'assignments':total,'simultaneous_hamming_event':eligible,'smallest_denominator_in_event':str(least_d),'worst_mean_hamming':str(Fraction(min(hamming[1:]),total)),'min_distance_histogram':dict(sorted(record.items()))}


if __name__=='__main__':
    print(json.dumps({'resonance':[resonant(a,b,S) for a,b,S in [(17,27,[5]),(19,31,[5]),(23,37,[7]),(19,31,[7]),(19,31,[5,7]),(17,27,[5,7])]],'dense':dense_all(11,18,2,3)},sort_keys=True,indent=2))
