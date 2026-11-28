#!/usr/bin/env python3
"""Check the primitive three-variable product and the extremal physical family."""

import json
from math import gcd

from check_reduced_core_transport import ramp, require, strip


def main():
    pools = [(2, 3), (2, 3, 5, 7), (2, 3, 5, 7, 11, 13, 17, 19)]
    examples = []
    for primes in pools:
        for x in range(1, 131072, 2):
            n, xnext = ramp(x)
            v = (n-1)//xnext
            r = v*(xnext+1)
            b, bnext = strip(x+1, primes), strip(xnext+1, primes)
            finite_denominator = (n//b)*v*(r//bnext)
            require(n*v*r == finite_denominator*b*bnext, x)

        for m in (0, 1, 7, 31, 127):
            f = 6*m+2
            v = 2**f
            n = (v-1)*(2*v-1)
            x = 2*(n//3)-1
            actual, xnext = ramp(x)
            require(n % 9 == 3 and actual == n and xnext == 2*v-3, m)
            b, bnext = strip(x+1, primes), strip(xnext+1, primes)
            shared = gcd(b, bnext)
            require(shared == bnext == strip(v-1, primes), (m, primes))
            require(b == shared*strip(2*v-1, primes), (m, primes))
            if primes == (2, 3):
                require(3*shared == v-1 and 3*b == n, m)
                examples.append([f, n.bit_length(), b.bit_length(), shared.bit_length()])

    print(json.dumps({'pools': pools, 'odd_starts_per_pool': 65536,
                      'retention_family_exponent_and_bit_lengths': examples},
                     sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
