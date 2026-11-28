"""Actual one- and multi-sheet grids, native chain counts, and entropy constants."""
import json
from collections import Counter
from itertools import combinations_with_replacement, product
from math import gcd
from check_rational_six_sum import floor_log2, native_cycle, require


def cycle(P,B,sheets):
    p=P*sheets
    gap=max(2,P//80)
    off=P//7
    grade=[2]*p
    for j in range(sheets):
        displacement=j%3
        for r in [off+displacement,off+2*gap+displacement]:
            t=j*P+(r*pow(B,-1,P))%P
            grade[t]=grade[(t+1)%p]=4
        for r in [off+gap+displacement,off+3*gap+1+displacement]:
            t=j*P+(r*pow(B,-1,P))%P
            grade[t]=1
    native=[(t+1)*B//P-t*B//P+grade[(t+1)%p].bit_length()-grade[t].bit_length()
            for t in range(p)]
    require(min(native)>=1,"positive native valuation")
    E,q,y=native_cycle(native)
    require(gcd(E[-1],p)==sheets,"full clock gcd")
    return E,q,y


def grid(P,B,sheets):
    E,q,y=cycle(P,B,sheets)
    p=len(y);A=E[-1];T=pow(B,-1,P);k=(T*B-1)//P
    W=max(3,P//32)
    def clock(t):
        v,r=divmod(t,p)
        return v*A+E[r]
    def floor(t):
        return clock(t)+floor_log2(y[t%p],4*max_y)
    max_y=max(y)
    def raw_tag(t,j):
        power=clock(t+j*T)-floor(t)-j*k
        require(power>=0,"integral q-scaled raw lift")
        return 1<<power
    forbidden={}
    for d in range(1,W+1):
        for t in range(p):
            u,v=raw_tag(t,0),raw_tag(t,d)
            if max(u,v)<4*min(u,v):continue
            j=(t+d*T)%p
            pair=tuple(sorted((t,j)))
            exponent=abs(u.bit_length()-v.bit_length())
            lo,hi=sorted((y[t],y[j]))
            # W/P≤1/30 in these explicitly named fixtures.  The finite
            # witness checks the actual pair against a rational 3% band.
            require(exponent>=2 and 97*(lo<<exponent)<100*hi<103*(lo<<exponent),
                    "true odd pair close to the indicated power of two")
            forbidden[d]=pair
            break
    require(len(set(forbidden.values()))==len(forbidden),"distinct true unordered pairs")
    S=[]
    for j in range(W+1):
        if all(j-i not in forbidden for i in S):S.append(j)
    require(len(S)*(2*len(forbidden)+1)>=W+1 and len(S)>=2,"large independent set")
    C=[];Y=[];scales=[]
    for t in range(p):
        c=[raw_tag(t,j) for j in S];scale=min(c);scales.append(scale)
        row=[u//scale for u in c]
        require(set(row)<={1,2},"universal binary row after true scale division")
        C.append(row);Y.append([v*y[(t+j*T)%p] for v,j in zip(row,S)])
    pairs=list(combinations_with_replacement(range(len(S)),2))
    heights=Counter()
    for t in range(p):
        n=(t+1)%p
        h=floor(t+1)-floor(t)+scales[n].bit_length()-scales[t].bit_length()
        require(h>=0,"adjusted native winding")
        heights[h]+=1
        require(all((1<<h)*v==3*u+q*c for u,v,c in zip(Y[t],Y[n],C[t])),
                "actual adjusted affine recursion")
        require(all(h+w.bit_length()-v.bit_length()>=1 for v,w in zip(C[t],C[n])),
                "positive native grade after normalization")
        require(len({Y[t][i]+Y[t][j] for i,j in pairs})==len(pairs),
                "actual pair sums on whole independent-set physical circuit")
    return dict(odd_period=p,clock_gcd=sheets,reduced_period=P,full_denominator_bits=q.bit_length(),
                width_millionths=10**6*max_y//min(y),offset_window=W,
                forbidden_positive_differences=list(forbidden),independent_set=S,
                tested_physical_pair_sums=p*len(pairs),adjusted_windings=dict(heights))


def chains():
    counts=Counter()
    for n in range(2,8):
        for h in product(range(4),repeat=n-1):
            words=[z for z in product(range(2),repeat=n)
                   if all(B+w-v>=1 for B,v,w in zip(h,z,z[1:]))]
            if not words:continue
            count=1;i=0
            while i<n:
                j=i
                while j+1<n and h[j]<=1:j+=1
                strict=h[i:j].count(0)
                require(strict<=1,"feasible block at most one strict rise")
                count*=1 if strict else j-i+2
                i=j+1
            require(count==len(words),"staircase product equals actual path count")
            require(h.count(1)+2*h.count(0)>=2*(n-1)-sum(h),"native deficit ledger")
            counts["feasible_winding_strings"]+=1
            counts["binary_native_words"]+=len(words)
            counts["calendars_with_strict_rise"]+=int(0 in h)
            counts["calendars_with_winding_three"]+=int(3 in h)
    # No floating point is involved in the binomial entropy control or in
    # the elementary bracket on gamma=log2(3).
    require(100**100000 < (1<<95100)*63**63000*37**37000,"H2(63/100)<.951")
    require(1<<1584962 < 3**1000000 < 1<<1584963,"direct rational bracket on log2(3)")
    return counts


if __name__=="__main__":
    print(json.dumps(dict(chains=chains(),
                          grids=[grid(P,B,s) for P,B,s in
                                 ((306,485,1),(306,485,2),(306,485,3),(971,1539,1))]),
                     indent=2,sort_keys=True))
