"""Compare the proposed prime-power families with exact polynomial gcds and native cycles."""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd
from sympy import Poly, Symbol, ZZ, resultant


X=Symbol("X")


def verify(ok, explanation):
    if not ok:
        raise ArithmeticError(explanation)


def cycle(positions,length,stats):
    p=len(positions)
    verify(positions==sorted(set(positions)) and 0<=positions[0]<=positions[-1]<length,
           "strict native calendar")
    carry=0
    for i in positions:
        carry=3*carry+2**i
    D=2**length-3**p
    x=Fraction(carry,D)
    first=x
    seen=set()
    odd=set(positions)
    for t in range(length):
        verify(x not in seen and x>0,"positive least native period")
        seen.add(x)
        parity=x.numerator%2
        verify(parity==(t in odd),"physical native parity")
        x=(3**parity*x+parity)/2
        verify(x.denominator==first.denominator,"full denominator is preserved")
    verify(x==first,"true return")
    stats["distinct_positive_native_states"]+=length
    stats["primitive_cycles"]+=1


def spectrum(slopes,offsets,k,a,degree,stats):
    p=len(slopes)
    coeff=[0]*(k+1)
    for i,(c,b) in enumerate(zip(slopes,offsets)):
        coeff[c]+=3**(p-1-i)*2**b
    numerator=Poly.from_dict({(i,):u for i,u in enumerate(coeff) if u},X,domain=ZZ)
    denominator=Poly(2**a*X**k-3**p,X,domain=ZZ)
    G=numerator.gcd(denominator)
    V=denominator.exquo(G)
    B=numerator.exquo(G)
    verify(V.degree()==degree and V.gcd(B).degree()==0,"complete residual degree")
    fixed=abs(int(resultant(V,B)))
    verify(fixed>0,"coprime residual resultant")
    n=max(12,3+max(offsets))
    y=2**n
    got=gcd(int(V.eval(y)),int(B.eval(y)))
    verify(fixed%got==0,"complete residual gcd divides fixed resultant")
    positions=[c*n+b for c,b in zip(slopes,offsets)]
    cycle(positions,k*n+a,stats)
    stats["coprime_univariate_specializations"]+=1


def main():
    stats=Counter()
    for prime,exponents in ((2,range(1,6)),(3,range(1,4)),(5,range(1,3)),(7,range(1,3))):
        for a in exponents:
            p=prime**a
            for size in range(a):
                for sub in combinations(range(1,a),size):
                    orders=(*sub,a)
                    offsets=[sum(i//prime**(b-1)%prime==0 for b in orders) for i in range(p)]
                    degree=1+sum(prime**(b-1)*(prime-1) for b in orders)
                    spectrum(list(range(p)),offsets,p,0,degree,stats)
                    stats["whole_order_subsets"]+=1
    pairs=[(0,0),(0,1),(1,2),(2,3),(3,1),(4,3),(6,3),(7,3)]
    spectrum(*zip(*pairs),8,4,4,stats)
    for r in (2,3,4,7,8):
        motifs=[(0,1),(2,3),(0,5)]
        motifs=[(*w,*range(6,r+4)) for w in motifs]
        def carry(w):
            c=0
            for t in w:
                c=3*c+2**t
            return c
        carries=list(map(carry,motifs))
        verify(carries[2]-carries[1]==carries[1]-carries[0]>0,"literal progression")
        d=(1,1,0,-1,-1,-1,0,1)
        pairs=[(i,i//2+b) for i in range(8) for b in motifs[1+d[i]]]
        spectrum(*zip(*pairs),8,4,4,stats)
        stats["eight_cluster_families"]+=1
    for key in sorted(stats):
        print(f"{key}={stats[key]}")


if __name__=="__main__":
    main()
