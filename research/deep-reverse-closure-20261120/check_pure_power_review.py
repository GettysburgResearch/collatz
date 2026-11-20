#!/usr/bin/env python3
"""Independent literal arithmetic checks for PP1 and PP2."""
import json
from math import lcm


def need(ok, msg):
    if not ok:
        raise ValueError(msg)


def strip(x, p):
    a = 0
    while x % p == 0:
        x //= p
        a += 1
    return a, x


def core(x, primes):
    for p in primes:
        _, x = strip(x, p)
    return x


def order(p):
    v = 3 % p
    a = 1
    while v != 1:
        v = (3*v) % p
        a += 1
    return a


def check(n, pool):
    a, u = strip(3*n+1, 2)
    need(a == 2 and u < n, "first-step valuation or descent")
    q = (3*n+5)//8
    need(8*q == 3*n+5, "shifted quotient integrality")
    need(core(u+1, pool) == q, "shifted outside-pool identity")
    return u


def main():
    progression_cases = pool_cases = 0
    for r in range(12):
        exponent = 108*r+80
        need(exponent == 27*(4*r+3)-1, "required exponent progression")
        check(3**exponent, [2, 3])
        progression_cases += 1
    for pool in [[2, 3], [2, 3, 5], [2, 3, 7],
                 [2, 3, 5, 7, 11, 13], [2, 3, 5, 7, 11, 13, 17]]:
        L = lcm(*(order(p) for p in pool if p not in (2, 3)))
        for multiplier in (1, 2, 3):
            k = L*multiplier
            n = 3**(4*k)
            u = check(n, pool)
            need(core(u, pool) == u, "unshifted outside-pool identity")
            for p in pool:
                if p not in (2, 3):
                    need(pow(3, 4*k+1, p) == 3 % p, "pool congruence")
            pool_cases += 1
    # The unrestricted-exponent construction cannot automatically be
    # intersected with PP1: p=7 forces 3|k, whereas PP1 requires k=20 mod 27.
    need(order(7) == 6 and all((20+27*j) % 6 != 0 for j in range(6)),
         "progression-scope control")
    print(json.dumps({"scope": "finite independent controls for the written elementary PP1--PP2 proofs",
                      "required_progression_cases": progression_cases,
                      "arbitrary_pool_cases": pool_cases,
                      "incompatible_progression_control": "prime 7",
                      "author_implementation_imported": False}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
