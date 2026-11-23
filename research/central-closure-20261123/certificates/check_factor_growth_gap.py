#!/usr/bin/env python3
"""Exact arithmetic for the uniform factor-growth theorem.

The coverage proof and analytic input are in PRIMITIVE_DENOMINATOR_GROWTH.md.
No floating point, CAS, or Python assert is used. Matveev, Legendre,
the logarithm series and the written polynomial arguments are external
to this executable finite certificate.
"""

from fractions import Fraction as F
from math import gcd
import hashlib
import json

N = 128
K = 10**12
C = 10**10


def require(condition, message):
    if not condition:
        raise ValueError(message)


def log_interval(y):
    require(isinstance(y, int) and y >= 2, "integer logarithm argument must be >=2")
    require(isinstance(N, int) and N >= 1, "positive series length required")
    z = F(y-1, y+1)
    lo = 2*sum((z**(2*j+1)/(2*j+1) for j in range(N)), F(0))
    return lo, lo+2*z**(2*N+1)/((2*N+1)*(1-z*z))


def common_cf(lo, hi, bound):
    require(0 < lo < hi, "positive increasing interval required")
    require(isinstance(bound, int) and bound >= 1, "positive denominator bound required")
    partials, conv = [], []
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    while True:
        a0, a1 = lo.numerator//lo.denominator, hi.numerator//hi.denominator
        require(a0 == a1, "interval cannot certify next quotient")
        partials.append(a0)
        p, q = a0*pm1+pm2, a0*qm1+qm2
        conv.append((p, q))
        if q > bound:
            return partials, conv
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
        lo, hi = lo-a0, hi-a0
        require(0 < lo <= hi, "invalid residual interval")
        lo, hi = 1/hi, 1/lo


def admissible(a, b):
    return a >= 1 and b >= 1 and gcd(a, b) == 1 and 2**a > 3**b and (a, b) != (2, 1)


def verify_gap(a, b):
    require(admissible(a, b), "inadmissible reduced pair or explicit exception")
    e = gcd(b, 2)
    t = b//e
    if e == 1:
        require(F(2**a-3**b) > F(3, 2)**b, "odd-denominator factor gap")
    else:
        require(F(2**a) > (3**t+F(3, 2)**t)**2, "even-denominator factor gap")


def run():
    l2, u2 = log_interval(2)
    l3, u3 = log_interval(3)
    require(F(2, 3) < l2 < u2 < 1, "log2 constants")
    require(1 < l3 < u3 < 2, "log3 constants")
    lo, hi = l3/u2, u3/l2
    partials, conv = common_cf(lo, hi, K)
    upper = []
    for a, b in conv:
        if b <= K and F(a, b) > hi:
            upper.append((a, b))
        elif b <= K:
            require(F(a, b) < lo, "unclassified convergent")
    expected = [
        (2,1), (8,5), (65,41), (485,306), (24727,15601),
        (125743,79335), (301994,190537), (17087915,10781274),
        (272500658,171928773), (630138897,397573379),
        (10439860591,6586818670), (217976794617,137528045312),
    ]
    require(upper == expected, "complete upper-convergent list")
    verify_gap(65, 41)
    large = [(a,b) for a,b in upper if b >= 14 and (a,b) != (65,41)]
    require(len(large) == 9, "large candidate count")
    for a, b in large:
        require(b >= 306, "large candidate cutoff")
        require(a*l2-b*u3 > F(1, 2**100), "large candidate lower bound")
    require(F(1, 2**152) < F(1, 2**100), "large candidate contradiction")

    small = []
    for b in range(1, 14):
        a = 1
        while not admissible(a, b):
            a += 1
        require(all(not admissible(j,b) for j in range(1,a)), "least admissible exponent")
        verify_gap(a, b)
        small.append((a,b))

    # If b>=14 and the factor gap fails, a<2b follows from
    # 3**t+(3/2)**t<4**t for t>=2. Base plus termwise growth<4.
    require(3**2+F(3,2)**2 < 4**2, "exponent cap base")
    require(F(3,2) <= 3 < 4, "exponent cap induction")
    # Legendre denominator condition, for both parities, then b -> b+2.
    require(2**14 > (6*14)**2, "Legendre even base")
    require(2**15 > (6*15)**2, "Legendre odd base")
    require(2*14 > 14+2, "Legendre induction")

    require(F(7,5)*30**5*32*2 < C, "Matveev prefactor")
    require(sum((F(1,t) for t in (1,1,2,6,24)),F(0)) > F(8,3), "exp(1)>8/3")
    require(F(8,3)**30 > 2*K, "log(2K)<30")
    require(F(K,3)-2 > 31*C, "infinite tail base")
    require(F(1,3)-F(C,K) > 0, "infinite tail derivative")

    # A=2p cyclotomic constants. The written proof uses exp(1)<3.
    require(F(8,3)**4 > 27, "degree>=4 cyclotomic bound")
    for h, phi, value in [(2,1,7),(3,2,37),(4,2,25),(6,2,13)]:
        require(value > F(3,2)**phi, "small cyclotomic factor bound")

    malformed = [
        lambda: log_interval(1),
        lambda: common_cf(F(0),F(1),10),
        lambda: common_cf(F(2),F(1),10),
        lambda: common_cf(F(1),F(2),0),
        lambda: common_cf(F(3,2),F(7,4),10),
        lambda: verify_gap(2,1),
        lambda: verify_gap(4,2),
    ]
    rejected = 0
    for bad in malformed:
        try:
            bad()
        except ValueError:
            rejected += 1
    require(rejected == len(malformed), "invalid input accepted")
    interval_data = [[str(l2),str(u2)],[str(l3),str(u3)]]
    return {
        "status": "PASS",
        "claim": "uniform reduced factor gap beyond the explicit (2,1) exception",
        "arithmetic": "integer/Fraction only",
        "log_series_terms": N,
        "tail_cutoff": K,
        "matveev_constant": C,
        "common_cf_partials": partials,
        "first_denominator_above_cutoff": conv[-1][1],
        "upper_convergents_below_cutoff": upper,
        "small_least_admissible_pairs_a_b": small,
        "direct_large_check": [65,41],
        "linear_form_candidate_count": len(large),
        "linear_form_lower_bound": "2^-100",
        "assumed_gap_upper_bound_at_large_candidates": "2^-152",
        "log_interval_sha256": hashlib.sha256(json.dumps(interval_data,separators=(",",":")).encode()).hexdigest(),
        "malformed_inputs_rejected": rejected,
        "external_coverage": ["Matveev real two-logarithm theorem", "Legendre criterion", "written root and cyclotomic arguments"],
        "scope": "exact finite component; not a Lean proof or integer-gcd bound",
    }


if __name__ == "__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
