"""Exact finite controls for the full colored boundary and the one-hole family."""

from itertools import product
from math import gcd


def need(test, name):
    if not test:
        raise ValueError(name)


def bezout(a, b):
    if not b:
        return 1, 0
    x, y = bezout(b, a % b)
    return y, x - a // b * y


def physical_numerator(word):
    carry = 0
    for clock, bit in enumerate(word):
        carry = 3**bit * carry + bit * 2**clock
    return carry


def build(word):
    n, u = len(word), sum(word)
    g = gcd(n, u)
    N, U = n // g, u // g
    a, b = bezout(U, N)
    before = 0
    phases = []
    for i, bit in enumerate(word):
        phases.append((i * U - N * before, (b * i + a * before) % g))
        before += bit
    floor = min(h for h, _ in phases)
    phases = [(h - floor, r) for h, r in phases]

    def ray_key(h, r):
        return h % N, (r + a * (h // N)) % g

    roots = {ray_key(h, r): h for h, r in phases}
    need(len(roots) == n, 'distinct colored rays')

    def occupied(h, r):
        return h >= roots[ray_key(h, r)]

    top = max(h for h, _ in phases)
    holes = {(h, r) for h in range(top) for r in range(g) if not occupied(h, r)}
    odds = {(h, r) for (h, r), x in zip(phases, word) if x}
    for h, r in phases:
        need(occupied(h + U, r + b), 'forward semigroup generator')
        need(occupied(h + N - U, r - a - b), 'backward semigroup generator')
    boundary = {(h, r) for h in range(top + U + 1) for r in range(g)
                if occupied(h, r) and not occupied(h - U, r - b)}
    check_odds = {(h + N - U, (r - a - b) % g) for h, r in boundary}
    need(check_odds == odds, 'physical odd set equals shifted boundary')
    return (g, N, U, a, b), phases, holes, boundary


def check_word(word):
    n, u = len(word), sum(word)
    D = abs(2**n - 3**u)
    C = physical_numerator(word)
    pars, phases, holes, boundary = build(word)
    g, N, U, a, b = pars
    if D == 1:
        return 0
    z = pow(2, a, D) * pow(3, b, D) % D
    t = pow(2, N, D) * pow(3, -U, D) % D

    def value(pts):
        return sum(pow(z, h, D) * pow(t, r, D) for h, r in pts) % D

    S = value(boundary)
    G = value(holes)
    total = sum(pow(z, j, D) for j in range(U)) * sum(pow(t, j, D) for j in range(g))
    need(S == (total + G) % D, 'colored holes identity')
    need(gcd(S, D) == gcd(C, D), 'full affine denominator')
    A, B = 2**N, 3**U
    Q = sum(A**r * B**(g-1-r) for r in range(g))
    need((S - G) % Q == 0, 'whole geometric-sum factor')
    if g == 1:
        gap_h = {h for h, _ in holes}
        maxh = max(gap_h, default=-1)
        coeff = [1 - int(0 in gap_h)] + [
            int(h - 1 in gap_h) - int(h in gap_h) for h in range(1, maxh + 2)]
        nz = [v for v in coeff if v]
        need(nz == [(-1)**j for j in range(len(nz))], 'alternating boundary')
        J = sum(v * pow(z, h, D) for h, v in enumerate(coeff)) % D
        need(gcd(J, D) == gcd(C, D), 'normalized rank-one denominator')
    return int(g > 1 and len({h for h, _ in holes}) == 1)


def special_word(n, u):
    v = n-u
    l, r = 2*v-u, u-v
    need(0 < l < r < v < u, 'family range')
    hs = [i*u % n + n*int(l <= i*u % n < r) for i in range(n)]
    return tuple((h + u - hs[(i+1) % n]) // n for i, h in enumerate(hs))


def determinant(mat):
    a = [row[:] for row in mat]
    n = len(a)
    sign, divisor = 1, 1
    for i in range(n-1):
        pivot = next((j for j in range(i, n) if a[j][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            a[pivot], a[i] = a[i], a[pivot]
            sign = -sign
        for j in range(i+1, n):
            for k in range(i+1, n):
                num = a[j][k]*a[i][i] - a[j][i]*a[i][k]
                need(num % divisor == 0, 'Bareiss division')
                a[j][k] = num // divisor
        divisor = a[i][i]
    return sign*a[-1][-1]


def norm(word):
    n, u = len(word), sum(word)
    pars, _, holes, _ = build(word)
    need(pars[0] == 1, 'norm coprime clock')
    exps = {h for h, _ in holes}
    j = [1] + [0] * (1 + max(exps, default=0))
    for h in exps:
        j[h] -= 1
        j[h+1] += 1
    cols = []
    for shift in range(n):
        col = [0]*shift + j + [0]*n
        for k in range(len(col)-1, n-1, -1):
            col[k-n] += col[k]
            col[k-n+u] += col[k]
        cols.append(col[:n])
    return abs(determinant(cols))


def main():
    words, single = 0, 0
    for n in range(2, 14):
        for w in product((0, 1), repeat=n):
            if min(w) == max(w):
                continue
            single += check_word(w)
            words += 1
    families, max_n = 0, 0
    for n in range(5, 203):
        for u in range(1, n):
            v = n-u
            if gcd(n, u) != 1 or not 0 < 2*v-u < u-v < v < u:
                continue
            w = special_word(n, u)
            D = abs(2**n-3**u)
            need(gcd(D, physical_numerator(w)) == gcd(D, 29), 'exact 29 family')
            ranks = {i*u % n for i in range(n) if w[i]}
            closest = min(len(ranks ^ {(i+j) % n for j in range(u)}) for i in range(n))
            l, r = 2*v-u, u-v
            need(closest >= 2*min(l, r-l, v-r, u-r), 'all mechanical phases')
            families += 1
            max_n = n
    norm_large = norm((1,1,1,1,0,1,0,0))
    norm_zero = norm((1,1,1,1,1,1,1,0,1,0,0,0,0))
    need(norm_large == 41 and norm_zero == 0, 'scalar norm barriers')
    x, w = -17, []
    while not w or x != -17:
        bit = x % 2
        w.append(bit)
        x = (3**bit*x + bit)//2
    need(len(w) == 11 and sum(w) == 7, 'signed anchor')
    check_word(w)
    need(gcd(139, physical_numerator(w)) == 139, 'signed full cancellation')
    print(f'All {words} mixed words through length 13 passed colored Apéry and full gcd checks.')
    print(f'{single} nontrivial-modulus colored tests had a single hole height.')
    print(f'{families} coprime explicit-family types through n={max_n} passed exact gcd and all-phase Hamming checks.')
    print('Trinomial norms: 41 at (n,u)=(8,5), 0 at (13,8). Signed -17 gives full cancellation 139.')


if __name__ == '__main__':
    main()
