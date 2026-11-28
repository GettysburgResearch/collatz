"""Exact native common-carry and marker Fourier support checks."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd
import json


def require(flag):
    if not flag:
        raise ValueError('failed exact shared-background identity')


def monic(coefficients):
    a = list(map(F,coefficients))
    while a and not a[-1]:
        a.pop()
    return [v/a[-1] for v in a] if a else []


def polynomial_gcd(a, b):
    a,b = monic(a),monic(b)
    while b:
        while len(a)>=len(b):
            shift = len(a)-len(b)
            factor = a[-1]
            for i,t in enumerate(b):
                a[shift+i]-=factor*t
            while a and not a[-1]:
                a.pop()
        a,b=b,monic(a)
    return a


def prime(n):
    return n>=2 and all(n%i for i in range(2,n) if i*i<=n)


def control(markers):
    M, T = len(markers), sum(markers)
    base = [1 << sum(markers[:j]) for j in range(M)]
    Fpoly = [-1]+[0]*(M-1)+[1<<T]
    e = M+1-len(polynomial_gcd(Fpoly,base))
    require(e>=2)
    if prime(M) or gcd(T,M)==1:
        require(e==M)
    partitions = [[j%2 for j in range(M)], [j%3 for j in range(M)], list(markers)]
    for parts in partitions:
        common = Fpoly
        for part in set(parts):
            common = polynomial_gcd(common,[a if parts[i]==part else 0 for i,a in enumerate(base)])
        require(M+1-len(common)>=e)
    # U is arbitrary; this common prefix spans multiple valuations.
    U = (1,3,2,1) if M%2 else (2,1,4)
    A,d = sum(U),len(U)+1
    B = [j*A+sum(markers[:j]) for j in range(M)]
    h,p = M*A+T,M*d
    E = [sum(U[:k]) for k in range(d)]
    C = sum(2**u*3**(d-1-k) for k,u in enumerate(E))
    D = 2**h-3**p
    if D<=0:
        return e,False
    S = sum(2**v*3**(d*(M-1-j)) for j,v in enumerate(B))
    common = gcd(D,C*S)
    q,y = D//common,C*S//common
    y0=y
    for a in markers:
        old=y
        for u in (*U,a):
            numer = 3*y+q
            require(numer%(1<<u)==0)
            y = numer>>u
            require(y%2==1 and gcd(q,y)==1)
        require((1<<(A+a))*y==3**d*old+q*C)
    require(y==y0 and q*(C*gcd(D,S))>=D)
    return e,True


def main():
    cases = [2,3,4,5,6,7,8,9,10,12]
    counts=Counter()
    support={}
    for M in cases:
        words = set(product((1,2,3),repeat=M)) if M<=5 else set()
        if M<=8:
            words.update(product((1,2),repeat=M))
        # Canonical marked words exhibiting highly unbalanced exits and composite orders.
        for j in range(M):
            for a in (2,5,17,61):
                words.add(tuple(a if k==j else 1+(k%3==0) for k in range(M)))
        for a in (3,11):
            words.add(tuple(a+(j%2)+2*(j%3==0) for j in range(M)))
        dist=Counter()
        for marks in sorted(words):
            if any(marks==marks[k:]+marks[:k] for k in range(1,M)):
                continue
            e,positive=control(marks)
            dist[e]+=1
            counts['primitive_marker_words']+=1
            counts['group_partitions']+=3
            counts['positive_native_cell_cycles']+=positive
            counts['proper_fourier_support']+=(e<M)
            counts['coprime_clock']+=(gcd(M,sum(marks))==1)
        support[M]=dict(sorted(dist.items()))
    print(json.dumps(dict(totals=dict(counts),support_size_by_order=support),indent=2))


if __name__ == '__main__':
    main()
