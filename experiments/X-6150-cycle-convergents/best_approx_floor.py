"""T-6141(f): sharpen the cycle floor by replacing Legendre with the classical
best-approximation theorem.

Setup (T-6141): a positive cycle with k odd elements, q halvings, minimum m >= B satisfies
    0 < q ln2 - k ln3 <= k/(3m),   i.e.   |q - k*theta| <= k/(3 m ln2),   theta = ln3/ln2.

Legendre only says q/k is a convergent when k^2 < 3 B ln2 / 2.  The sharper classical fact
(best approximation of the second kind; Khinchin Thm 16) is

    for every 1 <= k < K_{n+1} and every integer q:   |k theta - q| >= |K_n theta - P_n| =: eps_n,

where P_n/K_n are the convergents.  With  1/(K_{n+1}+K_n) < eps_n,  a cycle with
K_n <= k < K_{n+1} forces

    1/(K_{n+1}+K_n)  <  eps_n  <=  k/(3 B ln2)  <  K_{n+1}/(3 B ln2),

i.e.  K_{n+1} (K_{n+1} + K_n)  >  3 B ln2.   Contrapositive: if K_{n+1}(K_{n+1}+K_n) <= 3B ln2
then NO k below K_{n+1} is possible at all -- convergent or not.  This closes the Legendre gap.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
import sys

getcontext().prec = 120


def cf_log2_3(n_terms):
    x = Decimal(3).ln() / Decimal(2).ln()
    out = []
    for _ in range(n_terms):
        a = int(x)
        out.append(a)
        f = x - a
        if f == 0:
            break
        x = 1/f
    return out


def denominators(cf):
    """K_n: denominators of the convergents of theta = log3/log2 (= odd-step counts)."""
    q0, q1 = 0, 1
    out = [q1]
    for a in cf[1:]:
        q0, q1 = q1, a*q1 + q0
        out.append(q1)
    return out


def main():
    e = int(sys.argv[1]) if len(sys.argv) > 1 else 71
    B = 2**e
    cf = cf_log2_3(40)
    known = [1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3]
    assert cf[:len(known)] == known
    K = denominators(cf)
    # certified lower bound on 3*B*ln2 as a Fraction (decimal ln is correctly rounded)
    v = Decimal(2).ln()
    ulp = Decimal(10) ** (v.adjusted() - getcontext().prec + 1)
    ln2_lo = Fraction(v - 10*ulp)
    RHS = 3 * B * ln2_lo

    print(f"B = 2^{e};   3*B*ln2 >= {float(RHS):.6e}")
    print(f"\n{'K_n':>16} {'K_{n+1}':>16} {'K_{n+1}(K_{n+1}+K_n)':>24} {'<= 3B ln2 ?':>13}"
          f" {'all k < K_{n+1} excluded':>26}")
    floor = 1
    for i in range(len(K)-1):
        Kn, Kn1 = K[i], K[i+1]
        if Kn1 == Kn:
            continue
        prod = Kn1 * (Kn1 + Kn)
        ok = prod <= RHS
        if ok:
            floor = Kn1
        if Kn1 > 10**8 or not ok:
            print(f"{Kn:>16} {Kn1:>16} {float(prod):>24.6e} {str(ok):>13}"
                  f" {str(ok):>26}")
        if not ok and Kn1 > 10**10:
            break
    print(f"\nUNCONDITIONAL FLOOR (no Legendre gap):  k >= {floor} = {float(floor):.4e}")
    import math
    leg = math.sqrt(3*B*math.log(2)/2)
    print(f"Legendre-only floor (T-6141d)        :  k >= {leg:.4e}")
    print(f"improvement factor                   :  {floor/leg:.3f}x")
    print(f"corresponding total shortcut steps   :  q >= {floor*math.log(3)/math.log(2):.4e}")


if __name__ == "__main__":
    main()
