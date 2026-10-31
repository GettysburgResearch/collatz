#!/usr/bin/env python3
"""Fresh, self-contained reconstruction checks. Not a restoration of old bytes.

Python 3.10+, standard library only. Exact integers; checks survive python -O.
No numerical experiment in this program proves an all-integer claim.
"""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path


def require(condition: bool, message: object) -> None:
    if not condition:
        raise RuntimeError(str(message))


def v2(n: int) -> int:
    require(n > 0, ('v2 domain', n))
    return (n & -n).bit_length() - 1


def T(n: int) -> int:
    require(n > 1, ('killed shortcut domain', n))
    return (3*n+1)//2 if n & 1 else n//2


def U(n: int) -> int:
    require(n > 1 and n & 1, ('odd domain', n))
    q = 3*n+1
    return q >> v2(q)


def K(n: int) -> int:
    require(n > 0 and n & 1, ('rank domain', n))
    s = n.bit_count()
    return s*(s-1)//2 + v2(n+1)


def B(n: int) -> int:
    require(n > 0 and n & 1, ('companion domain', n))
    d = 1 << (n.bit_count()-1)
    a, b, k = d, n+1-d, 0
    while a < b:
        a *= 4
        b *= 3
        k += 1
    return k


def F(p: int) -> int:
    require(p >= 0, ('section domain', p))
    if p == 0:
        return 0  # bookkeeping only; physical trajectories stop at 1
    if p % 4 == 1:
        return (p-1)//4
    if p % 2 == 0:
        r = v2(3*p+2)
        t = (3*p+2) >> r
    else:
        r = v2(p+1)
        t = (p+1) >> r
    return (3**(r-1)*t-1)//2


def section_clock(p: int) -> int:
    require(p > 0, ('clock domain', p))
    if p == 1:
        return 3
    if p % 4 == 1:
        return 2
    return 1 + (v2(3*p+2) if p % 2 == 0 else v2(p+1))


def literal_section(p: int) -> tuple[int, int]:
    n, clock = 6*p+2, 0
    while True:
        n = T(n)
        clock += 1
        if n == 1:
            return 0, clock
        if n >= 8 and n % 6 == 2:
            return (n-2)//6, clock


def fan(q: int) -> tuple[int, ...]:
    require(q > 0, ('fan domain', q))
    t, k = 2*q+1, 0
    while t % 3 == 0:
        t //= 3
        k += 1
    values = [4*q+1]
    values.extend(2**(i+1)*3**(k-i)*t-1 for i in range(1, k+1))
    if t % 3 == (-1)**k % 3:
        values.append((2**(k+1)*t-2)//3)
    require(len(set(values)) == len(values), ('duplicate fan', q))
    return tuple(sorted(values))


def minimum(q: int) -> int:
    return min(fan(q)) if q else 0


def reduction(p: int) -> int:
    q, z = F(p), F(F(p))
    return min(q, minimum(p), minimum(q), z, minimum(z))


def kernel(p: int) -> bool:
    b = p % 32 in (2, 30) or p % 64 in (42, 58) or p % 256 in (10, 74, 138)
    removed = p % 9 == 7 or p % 27 == 4 or p % 81 in (67, 40)
    odd = p % 768 in (159, 447, 255) or p % 1536 == 639
    return (b and not removed) or odd


RULES = (('ad','d'),('bd','gd'),('ae','ea'),('af','eb'),('ag','fa'),
         ('be','fb'),('bf','ga'),('bg','gb'),('ce','cb'),('cf','caa'),('cg','cab'))


def word_features(word: str) -> tuple[int, int]:
    require(word[0] == 'c' and word[-1] == 'd', ('proper word', word))
    n, h = 1, 0
    for letter in word[1:-1]:
        if letter in 'ab':
            n = 2*n + (letter == 'b')
        else:
            require(letter in 'efg', ('letter', letter))
            h += n.bit_length()
            n = 3*n + 'efg'.index(letter)
    return n, h


def micro(word: str) -> tuple[tuple[int,int,int], tuple[int,int,int]]:
    n, h = word_features(word)
    a = v2(n)
    m = n >> a
    return (K(m), a, h), (B(m), a, h)


def trace(n: int, steps: int) -> int:
    for _ in range(steps):
        n = T(n)
    return n


def cone_compile(t: int, c: int) -> tuple[int, int, tuple[int, ...]]:
    require(t > 0 and 0 <= c < 3**t and c % 3 != 0, ('cone domain',t,c))
    coefficient, constant, k, blocks = 3**t, c, 0, []
    for left in range(t, 0, -1):
        a = 1 if constant % 3 == 2 else 2
        if left > 1 and ((2**a*constant-1)//3) % 3 == 0:
            a += 2
        coefficient = coefficient*2**a//3
        constant = (constant*2**a-1)//3
        k += a
        blocks.append(a)
    require(coefficient == 2**k and 0 < constant < 2**k, ('cone form',t,c))
    require(k <= 4*t-2, ('cone budget',t,c,k))
    return k, constant, tuple(blocks)


def run(limit: int) -> dict:
    section_count, inverse_candidates = 0, 0
    for p in range(1, limit+1):
        require(literal_section(p) == (F(p), section_clock(p)), ('section',p))
        require((F(p)<p) == (p % 4 != 2 and p % 32 != 31), ('descent',p))
        require(reduction(p) <= p, ('reduction bound',p))
        section_count += 1
        for x in fan(p):
            require(F(x) == p, ('fan soundness',p,x))
            inverse_candidates += 1
    for p in range(1, 2*41472+1):
        require((reduction(p) == p) == kernel(p), ('kernel',p))
    kernel_count = sum(kernel(p) for p in range(1,41473))
    require(kernel_count == 3807, ('kernel period count',kernel_count))
    for p in range(1, 2*limit+1):
        require(p in fan(F(p)) if F(p) else p == 1, ('fan completeness sample',p))
    require(F(42) == 364 and reduction(364) == 42, 'moving-floor false cycle')
    actual = [42]
    while actual[-1]:
        actual.append(F(actual[-1]))
    require(actual == [42,364,273,68,51,19,7,4,3,1,0], '42 actual path')

    counts = Counter()
    for n in range(3, 2*limit+2, 2):
        z = n.bit_length()-n.bit_count()
        require(B(n) <= 3*z+1, ('zero bound',n))
        if K(U(n)) >= K(n):
            require(B(U(n)) < B(n), ('companion',n))
            counts['bad'] += 1
        else:
            counts['good'] += 1
        q, j, budget = n, 0, B(n)+1
        while True:
            m = U(q)
            j += 1
            if K(m)<K(q):
                break
            q = m
            require(j < budget, ('first local good bound',n,j,budget))
        counts['first_good_returns'] += 1
    for r in range(3,100):
        n = 21*2**r-1
        a,b = U(n),U(U(n))
        require((B(n),B(a),B(b)) == (8,4,9), ('fusion barrier B',r))
        require(K(b)-K(n) == r, ('fusion barrier K',r))
        require(K(a)>=K(n) and K(b)<K(a), ('first good',r))

    from itertools import product
    words, edges = 0, 0
    for length in range(5):
        for interior in product('abefg', repeat=length):
            w = 'c'+''.join(interior)+'d'
            n,h = word_features(w)
            kr,br = micro(w)
            words += 1
            for left,right in RULES:
                start = 0
                while True:
                    pos = w.find(left,start)
                    if pos < 0:
                        break
                    y = w[:pos]+right+w[pos+len(left):]
                    ny,hy = word_features(y)
                    ky,by = micro(y)
                    if left in ('ad','bd'):
                        require(ny == T(n), ('dynamic',w,y))
                        require(ky < kr or by < br, ('two-rank cover',w,y))
                    else:
                        require(ny==n and hy==h-1 and ky<kr and by<br, ('admin',w,y))
                    edges += 1
                    start = pos+1

    run_checks = 0
    for h in range(1,65):
        core = (4**h-1)//3
        for r in (h+1,h+8,1000+h):
            n = (core << r)-1
            initial = K(n)
            for j in range(1,h+1):
                m = (3**j*core << (r-j))-1
                require((K(m)<initial) == (j==h), ('run first return',h,r,j))
                if j==h:
                    require(initial-K(m)==h, ('run credit',h,r))
                run_checks += 1
    cone_count = 0
    for t in range(1,7):
        for c in range(1,3**t):
            if c % 3:
                k,r,blocks = cone_compile(t,c)
                for x in (1,2,7):
                    require(trace(2**k*x+r,k) == 3**t*x+c, ('cone',t,c,x))
                    cone_count += 1
    for h in range(1,80):
        for x in (1,7,2**31+1):
            n = 3**h*x+(3**h-1)//2
            m = 2**(h+1)*x+2**h-1
            require(trace(m,h+1)==n, ('f suffix',h,x))
            require((m<n)==(h>=2), ('f suffix descent',h,x))
    basin = set()
    for n in range(1,27):
        while n not in basin:
            basin.add(n)
            if n==1:
                break
            n = T(n)
    n, first = 27, 0
    while n not in basin:
        n = T(n)
        first += 1
    require((len(basin),first,n)==(34,59,23), ('27 obstruction',len(basin),first,n))
    return {'status':'EMPIRICAL replay of reconstructed PROPOSED lemmas; not a Collatz proof',
            'section_sources':section_count,'inverse_candidates':inverse_candidates,
            'kernel_checks':82944,'kernel_period':41472,'kernel_residues':kernel_count,
            'kernel_density':'47/512','false_greedy_cycle':[42,364,42],
            'actual_42_section_path':actual,'carry_checks':dict(counts),
            'micro_words':words,'micro_edges':edges,'run_endpoint_checks':run_checks,
            'cone_identity_checks':cone_count,'opaque_27_basin_size':34,
            'opaque_27_first_meeting_shortcut_clock':59}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--limit', type=int, default=10000)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    require(args.limit >= 1, 'limit must be positive')
    data = json.dumps(run(args.limit), sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.write_text(data, encoding='utf-8')
    else:
        print(data, end='')

if __name__ == '__main__':
    main()
