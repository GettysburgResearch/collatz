"""Exact finite checks of physical carries, multiplicative collisions, and ordinary siblings."""
from __future__ import annotations

import json
from collections import Counter
from math import gcd


def require(condition, message):
    if not condition:
        raise ValueError(message)


def step(z):
    return z // 2 if z % 2 == 0 else (3 * z + 1) // 2


def odd_step(z):
    a = 3 * z + 1
    return a // (a & -a)


def is_independent_by_prime_elimination(values):
    """A distinct pivot prime in each remaining family proves independence."""
    columns = []
    for value in values:
        factors = set()
        p = 2
        while p * p <= value:
            if value % p == 0:
                factors.add(p)
                while value % p == 0:
                    value //= p
            p += 1 if p == 2 else 2
        if value > 1:
            factors.add(value)
        columns.append(factors)
    while columns:
        counts = Counter(p for column in columns for p in column)
        i = next((i for i, col in enumerate(columns) if any(counts[p] == 1 for p in col)), None)
        if i is None:
            return False
        del columns[i]
    return True


def carry_controls():
    windows = collisions = 0
    for n in range(1, 513):
        for a, c in ((2, 1), (64, 21)):
            z = n
            carry = 0
            odds = 0
            for d in range(1, 14):
                e = z % 2
                carry = (3 ** e) * carry + (2 ** (d - 1)) * ((a - c) if e else c)
                odds += e
                z = step(z)
                common = gcd(a * n + c, a * z + c)
                require((2**d) * (a * z + c) == (3**odds) * (a * n + c) + carry, 'affine identity')
                require(0 < carry <= max(a - c, c) * (3**d - 2**d), 'carry bounds')
                require(carry % common == 0, 'common divisor')
                collisions += int(common > 1)
                windows += 1
    return {'windows': windows, 'nontrivial_gcds': collisions}


def terminating_controls():
    rows = []
    for s, multipliers in ((3, (1,3,5)), (4, (1,3,5)), (5, (1,3)), (6, (1,3)), (7, (1,))):
        for h in multipliers:
            f = h * 3 ** (s - 1)
            crest = 2**f
            require((crest + 1) % 3**s == 0, 'positive lift')
            b = (crest + 1) // 3**s
            x = [2**(s-i) * 3**i * b - 1 for i in range(s+1)]
            require(x[-1] == crest and all(step(u) == v for u,v in zip(x,x[1:])), 'ordinary segment')
            q = x[-2]
            require(q == (2**(f+1)-1)//3 and q%3 == 2 and odd_step(q) == 1, 'distinct final branch')
            siblings = [64*z+21 for z in x[1:-2]]
            require(len(siblings) == s-2, 'number of siblings')
            require(all(w%6 in (1,5) and odd_step(w)==u for w,u in zip(siblings,x[2:-1])), 'sibling first hits')
            require(len(set(siblings)) == len(siblings) and not set(siblings).intersection(x), 'off the spine')
            divisors = []
            for i, w in enumerate(siblings):
                p = 1
                for j, other in enumerate(siblings):
                    if i != j:
                        p *= gcd(w,other)
                divisors.append(p)
                require(w > p, 'finite independence certificate')
            if max(siblings).bit_length() <= 30:
                require(is_independent_by_prime_elimination(siblings), 'independent factor controls')
            rows.append({'s':s,'f':f,'n_bits':x[0].bit_length(),'siblings':len(siblings),
                         'maximum_gcd_product_bits': max(divisors).bit_length()})
    return rows


def short_relation():
    # 2z+1 at z=1 and 2z+1 at z=13 are powers of 3 on one physical trajectory.
    z = 13
    path = [z]
    while z != 1:
        z = step(z)
        path.append(z)
    require(2 * path[0] + 1 == (2 * path[-1] + 1)**3, 'exact relation')
    return {'source':path[0],'last':path[-1],'native_distance':len(path)-1,'ratio_of_exponents':3}


if __name__ == '__main__':
    print(json.dumps({'carries':carry_controls(),'terminating_branches':terminating_controls(),
                      'real_relation':short_relation()},sort_keys=True,indent=2))
