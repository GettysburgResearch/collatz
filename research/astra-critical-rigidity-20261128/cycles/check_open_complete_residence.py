"""Finite exact checks for rational return sectors and the matched-width thresholds."""

import json
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations_with_replacement
from math import gcd

from check_native_return_curvature import binary_floor, dates_and_lift, mechanical_numerator, require


def square_modulus(q):
    n, ans, ell = q, 1, 2
    while ell*ell<=n:
        count=0
        while n%ell==0:
            n//=ell
            count+=1
        ans*=ell**((count+1)//2)
        ell+=1
    return ans*n


def residue_order(element, q):
    if q==1:
        return 1
    current=element%q
    d=1
    while current!=1:
        current=current*element%q
        d+=1
    return d


def rational_run(q):
    h,b,b_next=1054,665,15601
    length=8001
    power=1
    E0=[0]
    for _ in range(length-1):
        power*=3
        E0.append(power.bit_length()-1)
    tolls=[z-v for v,z in zip(E0,E0[1:])]
    begin,_=mechanical_numerator(tolls,q)
    nums,E=dates_and_lift(begin,q,length)
    require(E==E0 and len(set(nums))==length and max(nums)<3*min(nums),
            "genuine confined distinct complete-Q physical run")
    modulus=square_modulus(q)
    unit=(pow(3,b,q)*pow(2,-h,q))%q
    d=residue_order(unit,modulus)
    require(d>1 and pow(unit,d,q)!=1 and (pow(unit,d,q)-1)**2%q==0,
            "proper square-only resonance at a nontrivial sheet stride")
    require(d*b<length<b_next, "several vertical observations inside genuine CF gap")
    anchor=length//2
    L=Fraction(7*min(nums),4*q)
    F=binary_floor(Fraction(nums[anchor]<<E[anchor],q)/L)
    ranks=defaultdict(list)
    for s in range(-anchor+10,anchor-9):
        j=s*h%b
        if j>=15:
            continue
        k=(s*h-j)//b
        tag=E[anchor+s]-k-F
        require(tag in (0,1), "true normalized positive binary tag")
        ranks[j].append((s,nums[anchor+s]<<tag))
    discarded=kept=pair_count=second_count=0
    original_defects=0
    for j,entries in ranks.items():
        original_defects+=sum((x+z-2*y)%q!=0 for (_,x),(_,y),(_,z) in
                              zip(entries,entries[1:],entries[2:]))
        buckets=defaultdict(list)
        origin=entries[0][0]
        for time,value in entries:
            buckets[((time-origin)//b)%d].append(value)
        best=max(buckets.values(),key=len)
        kept+=len(best)
        discarded+=len(entries)-len(best)
        require(d*len(best)>=len(entries), "at most complete sheet-order population loss")
        sums=[x+y for x,y in combinations_with_replacement(best,2)]
        require(len(sums)==len(set(sums)), "actual retained fiber pair sums are Sidon")
        gap2=[x+z-2*y for x,y,z in zip(best,best[1:],best[2:])]
        require(gap2 and all(v%q==0 for v in gap2), "original complete q divides square curvature")
        require(min(gap2)>0 or max(gap2)<0, "one true native sign on retained fiber")
        pair_count+=len(sums)
        second_count+=len(gap2)
    require(original_defects>0, "keeping all uncolored sheets fails full-Q integrality")
    return {"Q":q,"Q_s":modulus,"d":d,"linear_residue_mod_Q":pow(unit,d,q),
            "true_states":length,"reduced_ranks":len(ranks),"kept_sources":kept,
            "discarded_sources":discarded,"checked_retained_pair_sums":pair_count,
            "retained_exact_integral_curvatures":second_count,
            "unthinned_nonintegral_curvatures":original_defects}


def modular_cases():
    tests=0
    for q in range(1,350):
        if gcd(q,6)!=1:
            continue
        r=square_modulus(q)
        for unit in range(1,q+1):
            if gcd(unit,q)!=1:
                continue
            d=residue_order(unit,r)
            require((pow(unit,d,q)-1)**2%q==0, "whole-Q square resonance after exact order")
            tests+=1
    return tests


def thresholds():
    with localcontext() as ctx:
        ctx.prec=60
        two,one=Decimal(2),Decimal(1)
        g=Decimal(3).ln()/two.ln()
        def rate(R):
            eta=(R/two).ln()/two.ln()
            f=max(Decimal(0),eta-g+1)
            s=eta-2*f
            return min(Decimal('0.5753')*eta,
                       max(Decimal(3)*(s+g*f)/5,9*s/16+5*g*f/8))/g
        theta=rate(Decimal(4))
        full=one/(3*theta)-one
        residence=(7*theta-one)/3
        require(full < (3*Decimal('0.5')-7*theta+1)/(3+7*theta),
                "full-Q half-scale consequence uses the first branch")
        cross=[]
        for mu,lo,hi in [('3','3.28052','3.28053'),('5.116201','2.73292','2.73293')]:
            m,l,r=map(Decimal,(mu,lo,hi))
            require((m+1)*rate(l)<1<(m+1)*rate(r), "rate threshold between fixed decimal widths")
            cross.append({"mu":mu,"width_bracket":[lo,hi]})
        return {"matched_width_three_rate":str(+rate(Decimal(3))),
                "limiting_open_exponent":str(+residence),"complete_q_threshold":str(+full),
                "threshold_crossings":cross}


if __name__=="__main__":
    print(json.dumps({"complete_square_resonance_units":modular_cases(),
                      "physical_runs":[rational_run(25),rational_run(49)],
                      "rate_crossings":thresholds()},sort_keys=True,indent=2))
