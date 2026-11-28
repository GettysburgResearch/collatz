"""Exact finite controls for the exceptional-graph center and its two-thirds restriction."""

import json
from collections import Counter
from fractions import Fraction


def require(condition, description):
    if not condition:
        raise ArithmeticError(description)


def edges(A,D,m,precision,horizon):
    modulus=1<<precision
    by_residue={}
    for i in range(m):
        by_residue.setdefault((A+D*i)%modulus,[]).append(i)
    out=[]
    for i in range(m):
        source=(A+D*i)%modulus
        for h in range(1,horizon+1):
            target=source*pow(3,h,modulus)%modulus
            for j in by_residue.get(target,[]):
                if i!=j:
                    out.append((i,j,h))
    return out


def max_valuation(v):
    return (v&-v).bit_length()-1


def exact_case(A,D,m,precision,horizon,center):
    ed=edges(A,D,m,precision,horizon)
    require(len(ed)>10,"nonvacuous exceptional graph")
    centers={Fraction(i)-Fraction(j-i,3**h-1) for i,j,h in ed}
    require(centers=={center},"common rational center of every modular edge")
    Q=center.denominator
    P=center.numerator
    require(Q%3!=0,"center denominator prime to three")
    deleted=P*pow(Q,-1,3)%3
    survivors={i for i in range(m) if i%3!=deleted}
    require(len(survivors)>=m-(m+2)//3 and
            all(not (i in survivors and j in survivors) for i,j,_ in ed),
            "one residue removes all exceptional pairs")
    checked=0
    for i,j,h in ed:
        z=3**h-1
        for k,l,h2 in ed:
            w=3**h2-1
            require((i-k)*z*w-(j-i)*w+(l-k)*z==0,
                    "four-term elimination for arbitrary oriented edges")
            checked+=1
    return {"source_A":str(A),"step_D":str(D),"indices":m,"binary_precision":precision,
            "oriented_edges":len(ed),"computed_center":str(center),
            "discarded_residue_mod_3":deleted,"surviving_indices":len(survivors),
            "arbitrary_edge_pair_identities":checked}


def sharp(m):
    groups=Counter()
    for u in range(1,2*m,2):
        while u%3==0:
            u//=3
        groups[u]+=1
    actual_pairs=sum(n*(n-1)//2 for n in groups.values())
    cap=m-(m+1)//3
    require(cap==len(groups),"at most one multiplier from each exact ternary ray")
    enumerated=sum(((2*m-1)//3**h+1)//2 for h in range(1,40))
    require(actual_pairs==enumerated,"all edges of the sharp example counted once")
    return {"indices":m,"largest_independent_set":cap,"exact_power_pairs":actual_pairs}


if __name__=="__main__":
    examples=[exact_case(1,2,135,62,17,Fraction(-1,2)),
              exact_case((1<<160)-3,8,147,90,23,Fraction(3,8)),
              exact_case((1<<135)+5,10,143,88,23,Fraction(-1,2))]
    small=edges(1,2,40,4,5)
    centers={Fraction(i)-Fraction(j-i,3**h-1) for i,j,h in small}
    require(len(centers)>1,"insufficient precision may produce incompatible finite centers")
    D=1<<72
    require(all(max_valuation(D*j)>=72 for j in range(1,40)),
            "large binary step admits unwanted zero-exponent edges")
    print(json.dumps({"deep_precision_examples":examples,"low_precision_center_count":len(centers),
                      "sharp_examples":[sharp(m) for m in (60,121,399,1024,10001)]},
                     indent=2,sort_keys=True))
