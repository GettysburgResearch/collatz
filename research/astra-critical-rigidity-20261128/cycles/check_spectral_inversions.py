"""Check the minimal positive denominator divisor and true bounded-sheet polynomial decomposition."""

import hashlib
import json
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path

from sympy import Poly, Symbol, cyclotomic_poly, divisors

from check_near_octave_cycle_denominators import factors, orbit, primitive, remainder
from check_native_return_curvature import require

X, Z = Symbol("x"), Symbol("z")


def rank_polynomial(p,A,factors_list,E):
    # At each root of the clock binomial this is its actual input Fourier
    # coefficient, up to a common nonzero scalar and the conventional 1/p.
    U=[1<<e for e in E]
    f=Poly(1,X)
    for coeff in factors_list:
        if any(remainder(U,coeff)):
            f*=Poly.from_list(coeff,X)
    return f


def integer_divisor():
    counts=Counter()
    witness=None
    for p in range(2,10):
        for word in product((1,2,3),repeat=p):
            A=sum(word)
            if (1<<A)<=3**p or not primitive(word):
                continue
            q,ys,E=orbit(word)
            f=rank_polynomial(p,A,factors(p,A),E)
            r=f.degree()
            f3=int(f.eval(3))
            G=(f-Poly(f3,X)).exquo(Poly(X-3,X))
            numerator=-sum(int(G.nth(i))*(1<<E[i]) for i in range(r))
            require(Fraction(numerator,f3)==Fraction(ys[0],q),"exact minimal polynomial numerator")
            require(abs(f3)//gcd(numerator,f3)==q,"full rational denominator at minimal recurrence")
            P=p//gcd(A,p)
            e=P//gcd(2,P)  # sqrt(2) lies in Q^ab; the field degree lower bound is sharp.
            require(r%e==0,"rational e-gons in actual active characteristic roots")
            counts["total"]+=1
            if r<p:
                counts["proper"]+=1
            if r<p and q<abs(f3) and witness is None:
                witness={"word":word,"p":p,"rank":r,"value":abs(f3),"q":q}
    require(counts["proper"]>0 and witness is not None,"both inactive modes and numerical cancellation")
    return {"counts":dict(counts),"proper_rank_residual_gcd":witness}


def sparse_sheet(g,P,B):
    p,A=g*P,g*B
    def mark(i):
        j,sh=i*B%P,i//P
        return ((g%2==0 and j==1 and sh%2==0)
                or (g%3==0 and j==4 and sh%3==0))
    E=[i*B//P-int(mark(i)) for i in range(p+1)]
    word=tuple(b-a for a,b in zip(E,E[1:]))
    q,ys,_=orbit(word)
    anchor=ys.index(min(ys))
    word=word[anchor:]+word[:anchor]
    q,ys,E=orbit(word)
    m=min(ys); ymax=max(ys)
    folded=sorted(Fraction(y,2 if y>=2*m else 1) for y in ys)
    rank={z:i for i,z in enumerate(folded)}
    beta=[int(y>=2*m) for y in ys]
    lifted=[rank[Fraction(y,1<<b)]+p*(e+b) for y,b,e in zip(ys,beta,E)]
    require(lifted[0]==0,"absolute true minimum is the chronological cut")
    pairs=sum(0<3*(y-2*x)<q for x in ys for y in ys)
    rank_error=max(abs(z-i*A) for i,z in enumerate(lifted))
    require(rank_error<=2*pairs,"full true-lap error controlled by inversion classes")
    K=sum(2*z<=ymax for z in folded)
    k0=(K+g-1)//g
    h0=(2*pairs+g-1)//g+2
    require(k0+2*h0<P,"seam end supports disjoint in this actual fixture")
    u,v=(1-B*pow(B,-1,P))//P,pow(B,-1,P)
    dis=[e-i*B//P for i,e in enumerate(E)]
    require(set(dis)<={-2,-1,0,1},"all four permitted physical deviations")
    M=sum(3**(p-1-i)*(1<<e) for i,e in enumerate(E))
    delta=(1<<A)-3**p
    degree=0; support=[]; component_rows=[]
    f=Poly(1,X)
    product_lower=1
    for d in divisors(g):
        phi=Poly(cyclotomic_poly(d,Z),Z)
        def zp(a):
            return Poly(Z**(a%d),Z).rem(phi)
        coeffs=[Poly(0,Z) for _ in range(P)]
        for i,err in enumerate(dis):
            j=i*B%P
            coeffs[j]+=(1<<(4+err))*zp(v*(i*B//P)+u*i)
        # On Q^ab, P is odd in these fixtures, so each order class is
        # an entire irreducible cyclotomic block over the radical extension.
        block=Poly.from_dict({(P*j,):int(phi.nth(j))*2**(B*(phi.degree()-j))
                              for j in range(phi.degree()+1)},X)
        active_raw=any(remainder([1<<e for e in E],block.all_coeffs()))
        short={}
        def add(j,z):
            short[j]=short.get(j,Poly(0,Z))+z
        if d==1:
            add(h0,Poly(-8*g,Z))
        for j,c in enumerate(coeffs):
            val=c-Poly(16*g if d==1 else 0,Z)
            if j>=P-h0:
                val=(val*zp(v)).rem(phi).exquo_ground(2)
                k=j-P+h0
            else:
                k=j+h0
            if val:
                require(0<=k<k0+2*h0,"actual folded support")
                add(k,-val)
                add(k+1,val)
        F=sum(cf.as_expr()*X**j for j,cf in short.items() if not cf.is_zero)
        D=abs(int(block.eval(3)))
        G=gcd(D,M)
        require(bool(F)==active_raw,"computed spectral support matches true Fourier reconstruction")
        row={"d":int(d),"G_bits":G.bit_length(),"active":bool(F)}
        if F:
            support.append(int(d))
            f*=block; degree+=block.degree()
            product_lower*=D//G
            norm=Poly(Poly(F,Z).resultant(Poly(phi.as_expr(),Z)),X)
            # A single rational resultant taking the dth power of the twisted
            # binomial. The exact integer is divisible by all of G on the fixtures.
            H=P//2
            b=min(range(1,H+1),key=lambda j:min((B*j)%P,(-B*j)%P))
            a=(2*B*b+P)//(2*P)
            t0=gcd(a,b);a//=t0;b//=t0
            diff=b*B-a*P
            binom=Poly((3**(b*d)*X**(d*diff)-2**(a*d)) if diff>0 else
                       (2**(a*d)*X**(-d*diff)-3**(b*d)),X)
            R=abs(int(norm.resultant(binom)))
            require(R>0 and R%G==0,"nonzero twisted integral norm contains full gcd")
            row["norm_resultant_bits"]=R.bit_length()
        else:
            require(G==D,"whole zero sheet canceled in this actual experiment")
        component_rows.append(row)
    f3=abs(int(f.eval(3)))
    require(q%product_lower==0 and f3%q==0,"component lower and minimal upper divisors")
    require(degree==(P*(g if g<6 else 4)),"independent row-clock spectral dimension")
    return {"p":p,"A":A,"g":g,"rank":degree,"I":pairs,"K":K,"whole_q_bits":q.bit_length(),
            "max_absolute_full_lap_rank_error":rank_error,"rotation_to_true_minimum":anchor,
            "active_orders":support,"cyclotomic_components":component_rows,
            "upper_remainder_bits":(f3//q).bit_length()}


if __name__=="__main__":
    root=Path(__file__).parent
    files=("SPARSE_PHYSICAL_INVERSIONS.md","MINIMAL_RECURRENCE_DENOMINATOR.md")
    print(json.dumps({
        "source_sha256":{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in files},
        "minimal_divisor":integer_divisor(),
        "true_clock_components":[sparse_sheet(2,41,65),sparse_sheet(3,41,65),
                                 sparse_sheet(6,41,65),sparse_sheet(6,73,116)],
    },indent=2,sort_keys=True))
