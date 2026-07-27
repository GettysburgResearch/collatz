"""T-6141(f) used eps_n > 1/(K_{n+1}+K_n).  Using the EXACT eps_n = |K_n*theta - P_n| gives a
weaker requirement and hence a stronger exclusion.  How much margin does that recover?

Exclusion condition, exact form:   K_{n+1} / eps_n  <=  3 B ln2 .
"""
from decimal import Decimal, getcontext
from fractions import Fraction
import math

getcontext().prec = 140


def cf(n_terms):
    x = Decimal(3).ln()/Decimal(2).ln()
    out = []
    for _ in range(n_terms):
        a = int(x); out.append(a); f = x - a
        if f == 0: break
        x = 1/f
    return out


def convs(c):
    p0,q0,p1,q1 = 1,0,c[0],1
    yield p1,q1
    for a in c[1:]:
        p0,q0,p1,q1 = p1,q1,a*p1+p0,a*q1+q0
        yield p1,q1


C = cf(40)
PQ = list(convs(C))
v = Decimal(3).ln()/Decimal(2).ln()
ulp = Decimal(10)**(v.adjusted()-getcontext().prec+1)
th_lo, th_hi = Fraction(v-10*ulp), Fraction(v+10*ulp)
l2 = Decimal(2).ln(); u2 = Decimal(10)**(l2.adjusted()-getcontext().prec+1)
ln2_lo = Fraction(l2-10*u2)

print(f"{'K_n':>14} {'K_{n+1}':>14} {'1/(Kn1+Kn)':>13} {'exact eps_n':>13} "
      f"{'K_{n+1}/eps_n':>15} {'excluded at B=2^71':>19}")
for e in (71,):
    B = 2**e
    RHS = 3*B*ln2_lo
    for i in range(len(PQ)-1):
        Pn, Kn = PQ[i]; Pn1, Kn1 = PQ[i+1]
        if Kn1 == Kn or Kn1 < 10**9: continue
        lo = abs(Kn*th_lo - Pn); hi = abs(Kn*th_hi - Pn)
        eps_lo, eps_hi = min(lo,hi), max(lo,hi)
        crude = Fraction(1, Kn1+Kn)
        val = Fraction(Kn1)/eps_lo            # worst case (largest ratio)
        print(f"{Kn:>14} {Kn1:>14} {float(crude):>13.4e} {float(eps_lo):>13.4e} "
              f"{float(val):>15.4e} {str(val <= RHS):>19}")
        if Kn1 > 2*10**11: break

# threshold B at which the improvement survives, using exact eps
Pn,Kn = PQ[[i for i,(p,q) in enumerate(PQ) if q==6586818670][0]]
Pn1,Kn1 = PQ[[i for i,(p,q) in enumerate(PQ) if q==65470613321][0]]
lo = abs(Kn*th_lo-Pn); hi = abs(Kn*th_hi-Pn); eps = min(lo,hi)
need_crude = Fraction(Kn1*(Kn1+Kn))
need_exact = Fraction(Kn1)/eps
print(f"\ncritical step  K_n={Kn}, K_{{n+1}}={Kn1}:")
print(f"  crude requirement  3B ln2 >= {float(need_crude):.5e}  -> B >= 2^{math.log2(float(need_crude)/(3*math.log(2))):.3f}")
print(f"  exact requirement  3B ln2 >= {float(need_exact):.5e}  -> B >= 2^{math.log2(float(need_exact)/(3*math.log(2))):.3f}")
print(f"  margin at B=2^71: crude {float(3*2**71*ln2_lo/need_crude):.3f}x, "
      f"exact {float(3*2**71*ln2_lo/need_exact):.3f}x")
