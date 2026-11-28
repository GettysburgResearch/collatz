"""Exact finite nearcritical rational cycles and all sheet Fourier/rank factors."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path

from sympy import Poly, Symbol, cyclotomic_poly, divisors

from check_near_octave_cycle_denominators import orbit
from check_native_return_curvature import require

T=Symbol("t")


def block_nonzero(desc, divisor):
    """Remainder at a sparse monic rational cyclotomic clock polynomial."""
    a=desc[:]
    sparse=[(i,c) for i,c in enumerate(divisor) if c]
    for k in range(len(a)-len(divisor)+1):
        v=a[k]
        for j,c in sparse:
            a[k+j]-=v*c
    return any(a[len(a)-len(divisor)+1:])


def finite_case(a,L,t,P,B,crossed=False):
    g=(1<<a)*L
    p,A=g*P,g*B
    require(3**(P*P)<1<<(B*P)<2*3**(P*P),"strict upper convergent clock inequality")
    def half(s,j):
        return s%(1<<j)<1<<(j-1)
    rows=[tuple(s%L==0 for s in range(g)),tuple(half(s,a) and (not crossed or s%L==0) for s in range(g))]
    for j in range(1,a):
        if t>>(j-1)&1:
            rows.append(tuple(s%L==0 and half(s,j) for s in range(g)))
    require(not any(all(all(row[s]==row[(s+d)%g] for s in range(g)) for row in rows)
                    for d in range(1,g)),"literal common translation period")
    K=len(rows)
    def tip(i):
        r=i*B%P
        return int(rows[r-1][i//P%g]) if 1<=r<=K else 0
    E=[i*B//P-tip(i) for i in range(p+1)]
    w=tuple(b-a0 for a0,b in zip(E,E[1:]))
    require(min(w)>=1,"all actual positive valuation exponents")
    q,y,ee=orbit(w)
    require(ee==E[:-1],"unmodified true cumulative calendar")
    m=min(y);X=max(y)
    rho=Fraction(1<<A,3**p)
    require(Fraction(X,m)**P<=(1<<(P+K))*rho**(2*P),"exact upper physical width estimate")
    require(Fraction(X,m)**P*rho**(2*P)>=1<<(P-1),"exact lower physical width estimate")
    input_poly=[1<<v for v in ee]
    support=[]; degree=0; spectral=1
    for d in divisors(g):
        phi=Poly(cyclotomic_poly(d,T),T)
        synthetic=(d==1 or any(not Poly.from_list(list(map(int,row)),T).rem(phi).is_zero for row in rows))
        factor=Poly.from_dict({(P*j,):int(phi.nth(j))*2**(B*(phi.degree()-j))
                               for j in range(phi.degree()+1)},T)
        actual=block_nonzero(input_poly,list(map(int,factor.all_coeffs())))
        require(actual==synthetic,"native cumulative term has exactly the predicted sheet support")
        if actual:
            support.append(int(d))
            degree+=factor.degree()
            spectral*=abs(int(factor.eval(3)))
    k=L+(L if crossed else 1)*(1<<(a-1))+L*t
    require(degree==k*P and spectral%q==0,"full degree and complete minimal denominator divisor")
    return {"a":a,"crossed_top_level":crossed,"odd_factor":L,"binary_level_selector":t,"reduced_period":P,"reduced_grade":B,
            "true_period":p,"true_dimension":degree,"active_orders":support,
            "predicted_normalized_dimension":str(Fraction(k,g)),"whole_q_bits":q.bit_length(),
            "numerical_cancel_after_spectral_bits":(spectral//q).bit_length(),
            "true_minimum_approx":round(m/q,3),"real_width_approx":round(X/m,7)}


if __name__=="__main__":
    root=Path(__file__).parent
    sources=("NEARCRITICAL_DENOMINATOR_SPECTRUM.md","SYNCHRONIZED_NEARCRITICAL_SPECTRA.md")
    cases=[(3,1,0,41,65),(3,1,2,41,65),(3,1,3,41,65),
           (2,3,0,41,65),(2,5,0,41,65),(2,5,1,41,65),(2,3,1,306,485)]
    cases.extend((3,3,t,41,65,crossed) for t in range(4) for crossed in (False,True))
    out=[finite_case(*r) for r in cases]
    synced=[v for v in out if v["a"]==3 and v["odd_factor"]==3]
    require(len(synced)==8 and len({(v["true_period"],v["true_period"]*v["reduced_grade"]//v["reduced_period"]) for v in synced})==1,
            "all sheet masks literally at one common pair of native clocks")
    print(json.dumps({"source_sha256":{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in sources},
        "scope":"Finite normalized dimensions and true complete denominators on two upper convergents. The continuum and diagonal assertions are written theorems.",
        "true_cycles":out},sort_keys=True,indent=2))
