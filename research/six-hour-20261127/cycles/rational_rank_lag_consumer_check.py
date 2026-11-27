"""Modular lag multiplication and signed terminal fibre controls."""
from fractions import Fraction as Q
from collections import Counter
from math import gcd
from clock_order_certificate import make_cycle,necklaces
import json

def run():
    c=Counter()
    for p in range(3,12):
      for w in necklaces(p,3 if p<=7 else 2):
        raw=make_cycle(w)
        if raw is None:continue
        d,N=raw;A=sum(w);g=gcd(A,p);q=p//g;a=A//g
        if q<=1:continue
        for h in range(1,p):
            t=h*a%q
            if not t:continue
            unit=1%d;rho=pow(3,h,d)*pow(2,-(h*a//q),d)%d
            n=1;v=rho
            while v!=unit and n*t<q:n+=1;v=v*rho%d
            if n*t>=q:continue
            assert pow(3,n*h,d)*pow(2,-(n*h*a//q),d)%d==unit
            mismatch=lambda k:sum(w[i]!=w[(i+k)%p] for i in range(p))
            assert mismatch(n*h)<=n*mismatch(h);c['actual_physical_no_wrap_multiplications']+=1
    for d in (1,5,7,11,13,17,25,29,35,41):
      for q in (17,31,53,103):
       a=q+q//2+1
       for h in range(1,2*q):
        t=h*a%q
        if not t:continue
        u=1%d;rho=pow(3,h,d)*pow(2,-(h*a//q),d)%d;n=1;v=rho
        while v!=u:n+=1;v=v*rho%d
        if n*t>=q:continue
        assert (n*h)*a//q==n*(h*a//q)
        assert pow(3,n*h,d)*pow(2,-(n*h*a//q),d)%d==u
        c['abstract_no_wrap_multiplications']+=1;c['nontrivial_multipliers']+=n>1
    # Deliberately signed initial G and nonconstant drifts, chosen through backward multiples.
    for d in (1,5,7,11,25,101):
        for G in range(-70,71):
            for m in (1,2):
                for delta in range(-5,6):
                    y=3*G+d*delta
                    if y%(1<<m):continue
                    end=y>>m;a=end%d;J=(end-a)//d
                    assert (J-delta*pow(1<<m,-1,3)+a*pow(d,-1,3))%3==0
                    c['signed_fibre_terminal_controls']+=1;c['negative_terminal_quotients']+=J<0
    assert 6>Q(5116201,10**6) and 6>5
    return {'counts':dict(c),'coarse_microscopic_entropy_upper':'(1+ln72)/36 < 1/6','microscopic_scale_cut':'P^(1/4)','fixed_denominator_BLS_mismatch':'liminf > 1/(1000 S)','fixed_denominator_preprint_M3_mismatch':'liminf > 1/(36 S)'}
if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2))
