"""Finite exact controls for positive torsion filtering and genuine CF returns."""

import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement

from check_native_return_curvature import binary_floor, dates_and_lift, mechanical_numerator, require


def convolve(a,b):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c


def apply(poly, seq):
    return [sum(a*b for a,b in zip(poly,seq[t:t+len(poly)]))
            for t in range(len(seq)-len(poly)+1)]


def filters():
    y = [16*t*t+(-1)**t+3*(t%5) for t in range(350)]
    delta = [-1,1]
    sq = convolve(delta,delta)
    sieve = convolve([1]*2,[1]*5)
    require(min(apply(sq,y)) > 0, "all integer second differences have strict sign")
    require(set(apply(convolve(convolve(sq,delta),sieve),y)) == {0},
            "genuine strict-convex torsion annihilator retains the third root at one")
    weighted = apply(convolve(sq,sieve),y)
    require(set(weighted) == {320} and set(apply(convolve(sq,sieve),[-x for x in y])) == {-320},
            "removing the third root at unity leaves a strict signed weighted average")
    sqs = [t*t for t in range(15)]
    require(sqs[1]+sqs[8] == sqs[4]+sqs[7] and
            sqs[2]+sqs[9] != sqs[5]+sqs[8], "one pointwise square collision need not translate")
    tests = 0
    for a,b in combinations_with_replacement(range(15),2):
        for c,d in combinations_with_replacement(range(15),2):
            if (a,b) == (c,d):
                continue
            require((a+b,a*a+b*b) != (c+d,c*c+d*d), "pair polynomial order at one <= two")
            tests += 1
    return {"positive_filter_degree":len(sieve)-1, "weighted_second_difference":320,
            "ordered_pair_of_pair_moment_tests":tests,
            "pointwise_convex_non_Sidon_witness":[1,4,7,8]}


def actual(height, denominator, continued_next, length, sheets):
    powers = [1]
    for _ in range(length-1):
        powers.append(3*powers[-1])
    E0 = [a.bit_length()-1 for a in powers]
    tolls = [v-u for u,v in zip(E0,E0[1:])]
    y,_ = mechanical_numerator(tolls,1)
    nums,E = dates_and_lift(y,1,length)
    require(E == E0 and len(set(nums)) == length, "distinct true odd sources on prescribed return chart")
    m=min(nums)
    require(max(nums)<3*m and denominator<length<continued_next, "native width and CF gap")
    anchor=length//2
    L=Fraction(7*m,4)
    F=binary_floor(Fraction(nums[anchor]<<E[anchor],L))
    fibers=defaultdict(list)
    cap=min(denominator//25+1,40)
    for s in range(-sheets*denominator,sheets*denominator+1):
        j=(s*height)%denominator
        if j>=cap:
            continue
        k=(s*height-j)//denominator
        v=E[anchor+s]-k-F
        require(v in (0,1), "all true tags on one binary chart")
        Z=nums[anchor+s]<<v
        fibers[j].append((s,Z))
    total_pair_sums=0
    strict_triples=0
    all_values=[]
    for j,entries in fibers.items():
        values=[v for _,v in entries]
        pairs=[a+b for a,b in combinations_with_replacement(values,2)]
        require(len(set(pairs))==len(pairs), "true returns in each physical fiber are Sidon")
        diff2=[a+c-2*b for a,b,c in zip(values,values[1:],values[2:])]
        require(diff2 and (min(diff2)>0 or max(diff2)<0), "strict vertical discrete curvature")
        total_pair_sums+=len(pairs)
        strict_triples+=len(diff2)
        all_values.extend((j,v) for v in values)
    require(all(a[1] < b[1] for a in all_values for b in all_values if a[0]<b[0]),
            "strict physical order across coarse ranks")
    return {"convergent":[height,denominator], "next_denominator":continued_next,
            "true_odd_states":length, "local_samples":len(all_values), "coarse_fibers":len(fibers),
            "fiber_pair_sums":total_pair_sums, "vertical_strict_triples":strict_triples}


def mixed():
    # The shared positive difference five is represented over unequal sheet steps.
    fibers=[(100,102,107,115),(132,133,137,146)]
    lower,upper=fibers
    for values in fibers:
        differences=[b-a for a,b in combinations(values,2)]
        require(len(set(differences)) == len(differences), "both arithmetic test fibers are Sidon")
    number=unequal=0
    for i,j in combinations(range(len(lower)),2):
        top=[(u,v) for u,v in combinations(range(len(upper)),2)
             if upper[v]-upper[u]==lower[j]-lower[i]]
        require(len(top)<=1, "upper pair determined by actual difference")
        for u,v in top:
            require(lower[i]+upper[v]==lower[j]+upper[u], "true two-fiber equal sum")
            number+=1
            unequal+=int((v-u)!=(j-i))
    require(unequal>0,"imposing equal sheet steps misses a genuine arithmetic possibility")
    checks=0
    for a in range(1,8):
        for b in range(a,14):
            for d in (8,16,32,64):
                w0=Fraction(1)
                step1,step2=Fraction(a,d),Fraction(b,d)
                w1,w2,w3=w0+step1,w0+step2,w0+step1+step2
                gap=w0**11+w3**11-w1**11-w2**11
                require(gap >= 110*step1*step2, "integral Hessian bound in the tangent box")
                require(w1*w2-w0*w3==step1*step2, "product defect at an exact additive rectangle")
                checks+=1
    return {"arithmetic_cross_fiber_equalities":number,
            "equalities_with_different_sheet_separations":unequal,
            "eleventh_power_mixed_area_tests":checks}


if __name__ == "__main__":
    print(json.dumps({"filter":filters(), "mixed":mixed(),
                      "native":[actual(84,53,306,303,2),actual(1054,665,15601,8001,3)]},
                     indent=2,sort_keys=True))
