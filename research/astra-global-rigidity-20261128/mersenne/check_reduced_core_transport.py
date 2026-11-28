#!/usr/bin/env python3
"""Check the exact integer identities used before the subspace estimates."""

import json
from collections import Counter
from math import gcd, prod


def require(condition, detail):
    if not condition:
        raise ValueError(detail)


def strip(n, primes):
    for p in primes:
        while n % p == 0:
            n //= p
    return n


def shortcut(x):
    return (3*x+1)//2 if x % 2 else x//2


def ramp(x):
    z = x
    while z % 2:
        z = shortcut(z)
    crest = z + 1
    while z % 2 == 0:
        z = shortcut(z)
    return crest, z


def product_identities(x, primes):
    n, future = ramp(x)
    w = future + 1
    v = (n - 1)//future
    r = v*w
    g = gcd(r, n)
    uraw, vraw = strip(w, primes), strip(x+1, primes)
    common = gcd(uraw, vraw)
    u, denominator = uraw//common, vraw//common
    ar, br = r//g, n//g
    require(r == n + v - 1 and 2 <= v < n and v & (v-1) == 0, x)
    require(uraw == strip(r, primes) and vraw == strip(n, primes), x)
    require((u, denominator) == (strip(ar, primes), strip(br, primes)), x)
    require(gcd(u, denominator) == 1 and w % (common*u) == 0, x)

    # Multiply the real-place determinant by the reciprocals of the finite
    # S-parts. Cross multiplication keeps these two field products exact.
    real_product = (ar-br)*br
    finite_denominator = (ar//u)*(br//denominator)
    require(real_product*r == finite_denominator*(v-1)*u*denominator, x)
    require(real_product*w < finite_denominator*u*denominator, x)
    local_denominator = (n//vraw)*v
    require(n*v == local_denominator*vraw, x)
    require(vraw*u <= w*denominator, x)
    return n, future, u, denominator, common


def main():
    pools = [(2, 3), (2, 3, 5, 7), (2, 3, 5, 7, 11, 13, 17, 19)]
    counts = {}
    for primes in pools:
        census = Counter()
        for x in range(1, 131072, 2):
            _, _, u, v, common = product_identities(x, primes)
            side = {(False, False): 'neither', (True, False): 'numerator',
                    (False, True): 'denominator', (True, True): 'both'}[u > 1, v > 1]
            census[side] += 1
            census['common_above_one'] += common > 1
        counts[str(primes[-1])] = dict(sorted(census.items()))

    paths = []
    for x0 in (27, 97, 871, 6171, 2**127-1):
        primes = pools[1]
        start, united, removed = x0, [], []
        seen = set()
        while start not in seen:
            seen.add(start)
            _, start, u, v, _ = product_identities(start, primes)
            united.append(u)
            removed.append(v)
        b0, bk = strip(x0+1, primes), strip(start+1, primes)
        require(prod(united)*b0 == prod(removed)*bk, x0)
        paths.append([x0, len(united), start])

    # Every source in this family returns to 5 on its next odd ramp start.
    for m in (0, 1, 7, 31, 127):
        f = 6*m+2
        n = 5*2**f+1
        x = 2*(n//3)-1
        actual, future, u, _, _ = product_identities(x, pools[1])
        require((actual, future, u) == (n, 5, 1), x)

    print(json.dumps({'largest_tested_start': 131071,
                      'odd_starts_per_pool': 65536, 'pools_by_largest_prime': counts,
                      'telescoping_paths': paths, 'denominator_only_parameters': [0,1,7,31,127]},
                     sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
