"""Sort complete rational angular tilings without floating-point or logarithms."""

from fractions import Fraction
from itertools import combinations
from math import gcd
from random import Random
import json


def require(check, detail):
    if not check:
        raise ArithmeticError(detail)


def rays(x):
    x=Fraction(x)
    e=x.numerator.bit_length()-x.denominator.bit_length()
    scale=Fraction(2)**e
    if x<scale:
        scale/=2
    return x/scale


def circuit(word):
    A=K=0
    for e in word:
        K=3*K+2**A;A+=e
    D=2**A-3**len(word)
    q=D//gcd(D,K);x=K//gcd(D,K)
    out=[]
    for e in word:
        require(x%6 in (1,5) and gcd(x,q)==1,"full primitive reduced odd phase")
        out.append(x)
        y,rem=divmod(3*x+q,2**e)
        require(rem==0 and y%2==1,"actual rational valuation")
        x=y
    require(x==out[0] and len(set(out))==len(out),"closed primitive circuit")
    return out,q,D


def verify(word,A,p,a,b):
    odd,q,D=circuit(word)
    powers=[3**j for j in range(b+1)]
    starts=sorted((rays(Fraction(x,powers[j])),i,j) for i,x in enumerate(odd) for j in range(b+1))
    require(len({v for v,_,_ in starts})==p*(b+1),"all multiplied rays distinct")
    for h,(z,i,j) in enumerate(starts):
        zz,ii,jj=starts[(h+1)%len(starts)]
        if h+1==len(starts):
            zz*=2
        if j<b:
            require((ii,jj)==((i+1)%p,j+1),"exact next angular tile")
            require((3*odd[i]+q)*z==3*odd[i]*zz,"unit-correction tile ratio")
        else:
            require((ii,jj)==(i,0) and z*3**b==zz*2**a,"constant terminal tile")
    return q,D,len(starts)


def tests():
    rng=Random(3317)
    covered=balanced_cases=nonbalanced=0
    tiles=0;example=None
    for p in range(2,101):
        A=(3**p).bit_length()
        if gcd(A,p)!=1:
            continue
        b=pow(A,-1,p);a=(A*b-1)//p
        if 2**a>3**b:
            continue
        mech=tuple(((i+1)*A)//p-(i*A)//p for i in range(p))
        mechanical={mech[j:]+mech[:j] for j in range(p)}
        words={mech}
        if A<=17:
            for fs in combinations(range(1,A),p-1):
                h=(0,)+fs+(A,)
                w=tuple(h[i+1]-h[i] for i in range(p))
                words.add(min(w[j:]+w[:j] for j in range(p)))
        else:
            for _ in range(20):
                h=[0]+sorted(rng.sample(range(1,A),p-1))+[A]
                words.add(tuple(h[i+1]-h[i] for i in range(p)))
        for w in sorted(words):
            q,D,n=verify(w,A,p,a,b)
            covered+=1;tiles+=n
            if w in mechanical:
                balanced_cases+=1
                require(q==D,"full mechanical determinant")
            else:
                nonbalanced+=1
                if example is None and q>1:
                    odd,_,_=circuit(w)
                    example={"clock":[A,p],"lower_parent":[a,b],"word":w,"ordinary_numerators":odd,
                             "complete_denominator":q,"tiles":n}
    require(nonbalanced>0 and example and balanced_cases>0,"both model types")
    return {"primitive_closed_rational_circuits":covered,"angular_tiles_sorted":tiles,
            "mechanical_controls":balanced_cases,"nonmechanical_controls":nonbalanced,"nonmechanical_example":example}


if __name__=="__main__":
    print(json.dumps(tests(),indent=2,sort_keys=True))
