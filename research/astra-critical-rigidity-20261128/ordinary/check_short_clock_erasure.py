"""Exact native and divisor checks for simultaneous erasure of shorter clocks."""
from collections import Counter
import json
from math import gcd

from check_prime_grade_denominators import carry, replay, require


def check(n, m, counts):
    t = n-1
    p = t*m
    x = 2**n
    bits = [i for i in range(n) if ((x-3)>>i)&1]
    require(len(bits) == t and bits[0] == 0 and bits[-1] == n-1, "wrong bit template")
    dates = [(i*m+r)*n+shift for i,shift in enumerate(bits) for r in range(m)]
    q = replay(p*n, dates, counts)
    d1 = x-3
    dm = x**m-3**m
    dp = x**p-3**p
    sm = dm//d1
    block = sum(3**(m*(t-1-i))*x**(m*i)*2**shift for i,shift in enumerate(bits))
    require(sm*block == carry(dates), "group carry factorization")
    require(carry(dates)%dm == 0 and (dp//dm)%q == 0, "short clock factor persists in raw quotient")
    require(t%gcd(dm,q) == 0 and gcd(dp//dm,dm) == gcd(t,dm), "uncontrolled complete overlap")
    h = gcd(dp//sm, block)
    require((3**m*(x-1)-2*x**m)%h == 0, "auxiliary binomial not divisible")
    require(8*q*x**(2*m-1) >= x**p, "lower q exponent")
    if m == 1:
        require(q == dp//d1, "one-group exact denominator")
    for k in range(1, m+1):
        if not m%k:
            require(t%gcd(q,x**k-3**k) == 0, "proper subclock retained an extra factor")
            counts["subclock_tests"] += 1
    counts["nontrivial_shared_factors"] += gcd(dm,q)>1


def main():
    counts = Counter()
    for n in range(4, 12):
        for m in (1,2,3,4,6,12):
            check(n, m, counts)
    require(counts["nontrivial_shared_factors"] > 0, "no nontrivial sharp overlap example")
    print(json.dumps(dict(counts), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
