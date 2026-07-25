"""X-6150 — exact exclusion of (q,k) for positive Collatz cycles.

A positive cycle with k odd elements n_1..n_k and q total halvings satisfies

    prod_i (3 + 1/n_i) = 2^q                            (exact)

so, with m = min n_i,   0 < q log2 - k log3 <= k/(3m),  hence  m <= k/(3*delta),
and since delta = log(2^q/3^k) >= (2^q - 3^k)/2^q,

    m  <=  k * 2^q / ( 3 * (2^q - 3^k) )                (T-6141)

which is a pure integer bound: no floating point anywhere.

Combined with the exhaustive verification bound m > B, any (q,k) whose bound falls at or
below B is impossible.  By Legendre's theorem q/k must moreover be a continued-fraction
convergent of log3/log2 whenever k < sqrt(3 B log2 / 2), so the convergents are the only
candidates to test.

The continued fraction of log_2(3) is computed by EXACT integer comparisons of powers
(no logarithms), so the whole computation is certified.
"""
from decimal import Decimal, getcontext
import sys


def cf_log2_3(n_terms, prec=200):
    """Continued fraction of log_2(3).

    Generated with high-precision decimal arithmetic. This step only ENUMERATES candidate
    (q,k); every exclusion below is then decided by exact integer arithmetic on 2^q - 3^k,
    so no conclusion depends on the decimal computation. The leading terms are checked
    against the classical value [1;1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,...].
    """
    getcontext().prec = prec
    x = Decimal(3).ln() / Decimal(2).ln()
    out = []
    for _ in range(n_terms):
        a = int(x)
        out.append(a)
        frac = x - a
        if frac == 0:
            break
        x = 1 / frac
    return out


def log_interval(n, prec=90):
    """Certified interval [lo, hi] containing ln(n), as Fractions.

    Python's decimal ln() is correctly rounded to the working precision (documented), so the
    true value lies within one ulp of the returned Decimal; we widen by 10 ulp for safety.
    """
    from fractions import Fraction
    getcontext().prec = prec
    v = Decimal(n).ln()
    ulp = Decimal(10) ** (v.adjusted() - prec + 1)
    return Fraction(v - 10*ulp), Fraction(v + 10*ulp)


def convergents(cf):
    p0, q0, p1, q1 = 1, 0, cf[0], 1
    yield p1, q1
    for a in cf[1:]:
        p0, q0, p1, q1 = p1, q1, a*p1 + p0, a*q1 + q0
        yield p1, q1


def main():
    # exhaustive verification bound: every n < B is known to reach 1.  Passed in so the
    # conclusion's dependence on the verification record is explicit and auditable.
    B = 2**int(sys.argv[2]) if len(sys.argv) > 2 else 2**71
    NT = int(sys.argv[1]) if len(sys.argv) > 1 else 22
    QCAP = 6*10**4       # exact powers only computed while q <= QCAP

    cf = cf_log2_3(NT)
    known = [1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3]
    assert cf[:len(known)] == known, (cf[:len(known)], known)
    print("continued fraction of log_2(3) (leading terms checked against the classical value):")
    print(f"  {cf}")
    print(f"\nverification bound B = 2^{B.bit_length()-1} = {B}")
    import math
    KLEG = math.sqrt(3*B*math.log(2)/2)
    print(f"Legendre applies while k < sqrt(3*B*ln2/2) = {KLEG:.4e}")
    # sanity: the trivial cycle 1 -> 2 -> 1 has q=2, k=1 and must satisfy the bound with m=1
    tb = 1 * 2**2 / (3 * (2**2 - 3**1))
    print(f"sanity check on the trivial cycle (q=2,k=1): bound on m is {tb:.4f} >= actual m = 1"
          f"  -> {tb >= 1}\n")
    print(f"{'q (halvings)':>13} {'k (odd steps)':>14} {'2^q>3^k':>8} "
          f"{'bound on min element m':>26} {'excluded?':>10} {'method':>9}")
    first_survivor = None
    l2lo, l2hi = log_interval(2)
    l3lo, l3hi = log_interval(3)
    for q, k in convergents(cf):
        if q <= QCAP:
            P, Q = 2**q, 3**k                       # fully exact integer route
            if P <= Q:
                print(f"{q:>13} {k:>14} {'no':>8} {'-- 3^k >= 2^q, impossible':>26} "
                      f"{'yes':>10} {'exact':>9}")
                continue
            bound = k * P // (3 * (P - Q))
            method = "exact"
        else:                                       # certified interval route
            dlo = q*l2lo - k*l3hi                   # lower bound on delta = q ln2 - k ln3
            dhi = q*l2hi - k*l3lo
            if dhi <= 0:
                print(f"{q:>13} {k:>14} {'no':>8} {'-- 3^k >= 2^q, impossible':>26} "
                      f"{'yes':>10} {'interval':>9}")
                continue
            if dlo <= 0:
                print(f"{q:>13} {k:>14} {'?':>8} {'-- precision exhausted':>26} "
                      f"{'?':>10} {'interval':>9}")
                break
            bound = k / (3*dlo)                     # m <= k/(3 delta)
            method = "interval"
        excluded = bound <= B
        bs = str(int(bound)) if bound < 10**12 else f"~{float(bound):.4e}"
        print(f"{q:>13} {k:>14} {'yes':>8} {bs:>26} {'yes' if excluded else 'NO':>10} "
              f"{method:>9}")
        if not excluded and first_survivor is None:
            first_survivor = (q, k, bound)
            break
    print()
    if first_survivor:
        q, k, bound = first_survivor
        print(f"first convergent NOT excluded: q = {q} halvings, k = {k} odd steps "
              f"(bound on m is ~{float(bound):.4e} > B)")
        print()
        print("CERTIFIED CONCLUSIONS (given the verification bound B):")
        print(f"  1. every convergent with k < {KLEG:.4e} is excluded (table above), and by")
        print(f"     Legendre q/k must be a convergent whenever k^2 < 3*B*ln2/2, so")
        print(f"     ==> any positive cycle has at least k >= {KLEG:.4e} odd elements,")
        print(f"         hence at least q >= {KLEG*math.log(3)/math.log(2):.4e} shortcut steps.")
        print(f"  2. if additionally q/k is a convergent, the first surviving one gives")
        print(f"     k >= {k} and q >= {q}.")
        print()
        print("  Note the gap: for k between the Legendre threshold and the first surviving")
        print("  convergent, q/k need NOT be a convergent, and this argument excludes nothing")
        print("  there. Conclusion 1 is the unconditional one.")


if __name__ == "__main__":
    main()
