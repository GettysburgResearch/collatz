"""Exact full-denominator controls for sparse edits of upper mechanical clocks."""
from bisect import bisect_right
from fractions import Fraction
from math import gcd
import json


def require(ok, reason):
    if not ok:
        raise ArithmeticError(reason)


def log_bounds(reciprocal):
    x=Fraction(1,reciprocal)
    low=2*sum(x**(2*j+1)/(2*j+1) for j in range(40))
    return low,low+2*x**81/(81*(1-x*x))


def create(p,A):
    require(gcd(p,A)==1 and 2**A>3**p,"positive reduced clock")
    b=[((i+1)*A)//p-(i*A)//p for i in range(p)]
    j=[z-1 for z in b]
    for index,tag in zip(range(-3,3),(1,2,2,2,2,1),strict=True):
        j[index%p]=tag
    e=[b[i]+j[(i+1)%p]-j[i] for i in range(p)]
    changes=[i for i,z in enumerate(e) if z!=b[(i+1)%p]]
    require(all(z in (1,2) for z in e) and sum(e)==A and len(changes)==4,"literal binary edit")
    carry=elapsed=0
    for z in e:
        carry=3*carry+(1<<elapsed)
        elapsed+=z
    D=(1<<A)-3**p
    common=gcd(carry,D)
    q=D//common
    first=carry//common
    n=first
    maximum=minimum=n
    for z in e:
        raw=3*n+q
        require(raw%(1<<(z+1))==1<<z,"true native numerator valuation")
        n=raw>>z
        maximum=max(n,maximum)
        minimum=min(n,minimum)
    require(n==first==minimum and q>1 and gcd(q,6)==1,"closed tagged control at true minimum")
    require(3*maximum<16*minimum,"strict physical band")
    # Find two explicitly unedited identical forward windows via equal angular cuts.
    k=(p-8)//2
    cuts=sorted({(-t*A)%p for t in range(k+1)})
    seen={}
    pair=None
    for i in range(p):
        if any((v-i)%p<k for v in changes):
            continue
        slot=bisect_right(cuts,((i+1)*A)%p)
        if slot in seen:
            pair=seen[slot],i
            break
        seen[slot]=i
    require(pair is not None,"pigeonhole on clean mechanical words")
    u,v=pair
    eu=[e[(u+t)%p] for t in range(k)]
    ev=[e[(v+t)%p] for t in range(k)]
    require(eu==ev,"literal equal native words")
    n=first
    saved=[]
    for i in range(v+1):
        if i==u or i==v:
            saved.append(n)
        n=(3*n+q)>>e[i]
    gap=abs(saved[1]-saved[0])
    clock=sum(eu)
    require(gap and gap%(1<<clock)==0 and 2*maximum>=3**k,"full-denominator gap")
    l2,u2=log_bounds(3)
    l3,u3=log_bounds(2)
    s=Fraction(minimum,q)
    low=24*s*l2*(A*l2/p-u3)
    high=24*s*u2*(A*u2/p-l3)
    require(0<low<=high<2,"physical observable below the ordinary conditional threshold")
    return {"period":p,"clock":A,"edited_edges":len(changes),"determinant_bits":D.bit_length(),
            "gcd_bits":common.bit_length(),"reduced_denominator_bits":q.bit_length(),
            "integer_part_of_minimum":int(s),
            "physical_ratio_millionths_floor":(10**6*maximum)//minimum,
            "clock_observable_millionths_lower":(10**6*low)//1,
            "clock_observable_millionths_upper":-((-10**6*high)//1),
            "repeated_word_length":k,"two_clean_origins":list(pair),"repeated_native_clock":clock,
            "gap_two_adic_valuation":(gap&-gap).bit_length()-1}


if __name__=="__main__":
    print(json.dumps([create(p,h) for p,h in ((41,65),(306,485),(15601,24727))],
                     indent=2,sort_keys=True))
