"""Complete binary-native four-sheet controls with the actual reduced denominator."""
import json
from math import gcd
from check_rational_six_sum import native_cycle, require
from check_four_sheet_pair_collisions import perm


def binary(P,B):
    period=4*P
    def winding(t):
        return (t+1)*B//P-t*B//P
    gate=[(2,2,4,2),(4,4,4,2),(2,2,4,2),(4,4,4,2),(2,2,4,2),
          (1,2,4,2),(2,4,4,2),(2,2,2,2),(4,4,4,4),(2,2,4,4),(4,2,4,4)]
    hg=[2,2,2,2,2,1,0,0,0,0,-2]
    cs=[]; hs=[]
    for t in range(period):
        j,r=divmod(t+5,P)
        if r<len(gate): c,h=gate[r],hg[r]
        else:
            c=(2,2,4,2) if winding(t)==1 else (4,4,4,2)
            h=2;j+=1
        for _ in range(j%4):c=perm(c)
        cs.append(c[0]);hs.append((-1)**j*h)
    exponents=[winding(t)+cs[(t+1)%period].bit_length()-cs[t].bit_length()
               for t in range(period)]
    require(set(exponents)=={1,2}, "all binary native valuations")
    E,q,y=native_cycle(exponents)
    require(gcd(period,E[-1])==4 and pow(3,4*P,q)==pow(2,4*B,q) and
            pow(3,2*P,q)!=pow(2,2*B,q),"exact reduced clock and full order four")
    Z=[x*c for x,c in zip(y,cs)]
    for t,h in enumerate(hs):
        require(Z[t]+Z[(t+2*P)%period]-Z[(t+P)%period]-Z[(t+3*P)%period]==q*h,
                "signed identity on true numerator shifts")
    zeros={(t*B)%P for t in range(period) if hs[t]==0}
    require(zeros=={(i*B)%P for i in range(1,5)} and hs.count(0)==16,
            "exact four-rank zero support")
    return dict(primitive_odd_period=period,reduced_odd_clock=P,reduced_division_clock=B,
                denominator_bits=q.bit_length(),width_millionths=max(y)*10**6//min(y),
                valuations_one=exponents.count(1),valuations_two=exponents.count(2),
                zero_dates=hs.count(0),zero_reduced_ranks=sorted(zeros))


if __name__=="__main__":
    print(json.dumps([binary(P,B) for P,B in ((41,65),(306,485),(971,1539))],indent=2))
