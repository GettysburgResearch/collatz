"""Reconstruct all odd states from shifted Apéry ray coefficients."""

from fractions import Fraction
from itertools import combinations
from math import gcd
from pathlib import Path
from runpy import run_path

semigroup = run_path(str(Path(__file__).resolve().parents[1] / 'phase2' / 'semigroup_controls.py'))
build = semigroup['build']
numerator = semigroup['physical_numerator']
need = semigroup['need']


def check_necklace(w):
    n, u = len(w), sum(w)
    D = 2**n-3**u
    _, _, holes, _ = build(w)
    L = [0]*u
    for j, _ in holes:
        L[j % u] += 1
    c = max((h+1 for h, _ in holes), default=0)
    need((c <= u) == (max(L) <= 1), 'conductor at most u')
    j = 0
    scale, shift = Fraction(1), Fraction(0)
    for _ in range(u):
        d, j = divmod(j+n, u)
        scale *= Fraction(2**d, 3)
        shift = (2**d*shift-2**L[j])/3
    need(j == 0 and scale == Fraction(2**n, 3**u), 'full scheduled multiplier')
    k0 = shift/(1-scale)
    k = k0
    actual = []
    for _ in range(u):
        d, nxt = divmod(j+n, u)
        actual.append(k/2**L[j])
        k_next = (2**d*k-2**L[nxt])/3
        e = d+L[j]-L[nxt]
        need(e >= 1 and 2**e*actual[-1] == 3*k_next/2**L[nxt]+1, 'physical odd recurrence')
        k, j = k_next, nxt
    need(k == k0 and min(actual) > 0, 'positive cyclic carry')
    expected = [Fraction(numerator(w[i:]+w[:i]), D) for i in range(n) if w[i]]
    need(sorted(expected) == sorted(actual), 'all physical odd phases')
    q = Fraction(numerator(w), D).denominator
    need(all(x.denominator == q for x in actual), 'all full reduced denominators')
    return int(c <= u)


def floor_candidates(n, u):
    D = 2**n-3**u
    limit = 4*u*2**n//(3*D)
    hits = []
    for k0 in range(1, limit+1):
        k, j, labels = k0, 0, [0]*u
        for _ in range(u):
            d, j = divmod(j+n, u)
            k, labels[j] = divmod(2**d*k, 3)
            if not labels[j]:
                break
        else:
            if k == k0:
                holes = tuple(i for i,r in enumerate(labels) if r == 2)
                normal = 0 not in holes
                v = n-u
                ideal = all(h-v in holes for h in holes if h >= v)
                hits.append((n,u,k0,holes,normal,ideal))
    return limit, hits


def main():
    count = binary = 0
    for n in range(2, 15):
        for u in range(1, n):
            if gcd(n,u) != 1 or 2**n < 3**u:
                continue
            for ones in combinations(range(n), u):
                chosen = set(ones)
                w = tuple(int(i in chosen) for i in range(n))
                if w != min(w[i:]+w[:i] for i in range(n)):
                    continue
                count += 1
                binary += check_necklace(w)
    tried = 0
    hits = []
    for n in range(3,121):
        for u in range(1,n):
            if gcd(n,u) == 1 and 3*u < 2*n < 4*u and 2**n > 3**u:
                tests, found = floor_candidates(n,u)
                tried += tests
                hits += found
    need([(n,u,k) for n,u,k,*_ in hits] == [(5,3,13),(8,5,61),(8,5,70)], 'nonzero-digit fixed points')
    need(not any(normal and ideal for *_,normal,ideal in hits), 'spurious fixed points')
    need([h for h in floor_candidates(2,1)[1] if h[-2] and h[-1]] == [(2,1,1,(),True,True)], 'ordinary anchor')
    print(f'{count} coprime positive necklaces through n=14 matched all native odd phases; {binary} had W<=1.')
    print(f'{tried} candidate integer coefficients tested at 3/2<n/u<2 through n=120.')
    for n,u,k,holes,normal,ideal in hits:
        print(f'n={n}, u={u}, k0={k}, holes={holes}, normalized={normal}, downward_closed={ideal}')
    print('n=2,u=1 recovers the ordinary anchor k0=1.')


if __name__ == '__main__':
    main()
