"""Exact closed native words, full-gcd Sylvester divisors and real order controls."""

import hashlib
import json
from fractions import Fraction
from itertools import combinations
from math import gcd
from pathlib import Path

from sympy import Poly, Symbol

from check_near_octave_cycle_denominators import orbit, primitive
from check_native_return_curvature import require


def generators(A, p):
    v=pow(A,-1,p)
    return (1-A*v)//p, v


def case(p,A,S):
    E=[i*A//p-int(i*A%p in S) for i in range(p+1)]
    w=tuple(b-a for a,b in zip(E,E[1:]))
    require(min(w)>0 and gcd(A,p)==1,"primitive positive actual word")
    Q,ys,_=orbit(w)
    delta=2**A-3**p
    M=sum(3**(p-1-i)*(1<<e) for i,e in enumerate(E[:-1]))
    G=gcd(delta,M)
    require(Q*G==delta,"full canceled factor of actual determinant")
    # Compute the full adjacent-inversion criterion on the original rational states.
    near_pairs=sum(0<3*(y-2*x)<Q for x in ys for y in ys)
    folded=[0]*p
    for i,y in enumerate(ys):
        r=i*A%p
        folded[r]=Fraction(y,2**int(r in S))
    ranked=(min(ys)==ys[0] and folded[-1]<2*folded[0]
            and all(a<b for a,b in zip(folded,folded[1:])))
    if ranked:
        require(not near_pairs,"actual ordered lift has no physical reversal")
        for j in S:
            if j-1 not in S:
                require(j>=1 and 6*(folded[j]-folded[j-1])>Q,"genuine 1/6 birth gap")
    t=Symbol("t")
    F=Poly(1+(t-1)*sum(t**j for j in S),t)
    resultants=[]
    if S:
        require(F.LC()==1,"short polynomial monic")
    if G>1:
        u,v=generators(A,p)
        base=(pow(2,u,G)*pow(3,v,G))%G
        require(pow(base,p,G)==2%G and pow(base,A,G)==3%G,"both complete-modulus powers")
        tip=pow(base,-1,G)
        require(int(F.eval(tip))%G==0,"short polynomial vanishes modulo full cancellation")
    for H in sorted({1,max(1,p//7),max(1,p//3)}):
        b=min(range(1,H+1),key=lambda j: min((j*A)%p,(-j*A)%p))
        a=(2*b*A+p)//(2*p)
        diff=b*A-a*p
        require(a>0 and 0<abs(diff)*H<=p,"Dirichlet area")
        ell=abs(diff)
        B=Poly((3**b*t**ell-2**a) if diff>0 else (2**a*t**ell-3**b),t)
        resultant=abs(int(F.resultant(B)))
        require(resultant>0 and resultant%G==0,"nonzero resultant contains full prime powers")
        bound_F=sum(int(c)**2 for c in F.all_coeffs())
        bound_B=3**(2*b)+2**(2*a)
        require(resultant*resultant<=bound_F**ell*bound_B**F.degree(),
                "exact squared Hadamard bound")
        resultants.append(resultant.bit_length())
    return {"p":p,"A":A,"marked_ranks":list(S),"G":G,"complete_q_bits":Q.bit_length(),
            "ordered_at_furnished_cut":ranked,"physical_reversal_pairs":near_pairs,
            "true_m_approx":round(min(ys)/Q,4),"width_approx":round(max(ys)/min(ys),6),
            "three_resultant_bit_lengths":resultants}


if __name__=="__main__":
    # Includes prime-power cancellation (125), both real order signs, and
    # actual positive small-m/p and large-m/p nonmechanical high-period examples.
    examples=[(7,13,(3,4)),(8,13,(1,)),(9,17,(3,4)),(9,17,(2,5)),
              (19,33,(10,)),(19,33,(3,4)),(19,33,(1,3,6)),
              (41,65,(1,2,4)),(53,85,(1,2,4)),(73,116,(2,4,6,8)),
              (306,485,(1,2,4)),(41,65,())]
    rows=[case(p,A,sub) for p,A,sub in examples]
    require(any(row["G"]%125==0 for row in rows),"repeated prime in full canceled factor")
    require(any(row["physical_reversal_pairs"] for row in rows)
            and any(row["ordered_at_furnished_cut"] for row in rows),"both physical-order outcomes")
    src=Path(__file__).with_name("SPATIAL_DEFECT_RESULTANT.md")
    print(json.dumps({"source_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),
                      "genuine_cycles":rows},sort_keys=True,indent=2))
