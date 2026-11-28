#!/usr/bin/env python3
"""Exact finite phase clamps and pinned concatenation, not infinite limits."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import comb


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def floor_log2_fraction(p, q):
    e = p.bit_length() - q.bit_length()
    if e >= 0:
        if p < (q << e):
            e -= 1
    else:
        if (p << (-e)) < q:
            e -= 1
    require(e >= 0, 'nonnegative ceiling in these fixtures')
    require((q << e) <= p < (q << (e + 1)), 'exact floor')
    return e


def ceiling(a, t):
    return floor_log2_fraction(3**t * a.denominator, a.numerator)


def phase_at(a, t):
    return a * F(2**ceiling(a, t), 3**t)


@lru_cache(None)
def words(a, n):
    b = [ceiling(a, t) for t in range(n + 1)]
    found = []
    def visit(prefix):
        t = len(prefix)
        if t == n:
            found.append(tuple(prefix + [b[n]]))
            return
        for x in range(prefix[-1] + 1, b[t] + 1):
            visit(prefix + [x])
    visit([0])
    return tuple(found)


def reward(a, K):
    return sum((a * F(2**k, 3**t) for t, k in enumerate(K[:-1])), F(0))


def legal(a, K):
    n = len(K) - 1
    return (K[0] == 0 and K[-1] == ceiling(a, n)
            and all(K[t] < K[t+1] for t in range(n))
            and all(K[t] <= ceiling(a, t) for t in range(n+1)))


def main():
    weights = tuple(map(F, (1,))) + (F(7,8), F(3,4), F(5,8), F(9,16))
    phases = clamps = lifted = changed = fibres = concatenations = rotations = 0
    for n in range(1, 13):
        for a in weights:
            W = words(a, n)
            require(len(set(W)) == len(W), 'distinct direct words')
            require(all(legal(a, K) for K in W), 'direct legal words')
            phases += 1
        for a, b in combinations(weights, 2):
            require(a > b, 'lower phase has larger weight')
            low, high = words(a, n), words(b, n)
            lowset, highset = set(low), set(high)
            lo = [ceiling(a, t) for t in range(n+1)]
            hi = [ceiling(b, t) for t in range(n+1)]
            D = [y-x for x,y in zip(lo,hi)]
            require(all(d in (0,1) for d in D), 'unit ceiling differences')
            Q = sum(D[1:n])
            fibre = Counter()
            for K in high:
                Kp = tuple(min(x,c) for x,c in zip(K,lo))
                require(Kp in lowset, 'clamp lands in lower pinned family')
                sites = [t for t in range(n) if K[t] != Kp[t]]
                correction = sum((phase_at(b,t)/2 for t in sites), F(0))
                require(reward(b,K) == b/a*reward(a,Kp)+correction, 'reward identity')
                require(0 <= correction <= F(Q,2), 'entry correction bound')
                require(all(K[t]==lo[t]+1 and Kp[t]==lo[t] for t in sites), 'clamp bits')
                fibre[Kp] += 1
                clamps += 1
                changed += len(sites)
            require(max(fibre.values()) <= 2**Q, 'fibre multiplicity')
            fibres += len(fibre)
            images = set()
            for K in low:
                Ku = K[:-1] + (K[-1] + D[-1],)
                require(Ku in highset, 'last-coordinate injection')
                require(reward(b,Ku) == b/a*reward(a,K), 'injected reward')
                images.add(Ku)
                lifted += 1
            require(len(images) == len(low), 'injection distinctness')

    for a in weights:
        for n in range(1, 7):
            for m in range(1, 7):
                an = phase_at(a, n)
                images = set()
                for K in words(a,n):
                    for J in words(an,m):
                        joined = K + tuple(K[-1]+x for x in J[1:])
                        require(legal(a,joined), 'pinned concatenation legal')
                        require(reward(a,joined)==reward(a,K)+reward(an,J), 'additive reward')
                        images.add(joined)
                        concatenations += 1
                require(len(images)==len(words(a,n))*len(words(an,m)), 'concatenation injection')

    for n in range(1,13):
        M = ceiling(F(1), n)
        valid = set(words(F(1),n))
        number = 0
        for cuts in combinations(range(1,M),n-1):
            K = (0,)+cuts+(M,)
            letters = tuple(K[t+1]-K[t] for t in range(n))
            # Maximize n*K_t-M*t, all integers. Rotate after that maximum.
            start = max(range(n),key=lambda t:n*K[t]-M*t)
            rotated = letters[start:]+letters[:start]
            cumulative = [0]
            for k in rotated:
                cumulative.append(cumulative[-1]+k)
            require(tuple(cumulative) in valid, 'cyclic ceiling rotation')
            number += 1
            rotations += 1
        require(number==comb(M-1,n-1), 'all positive compositions')
        require(number <= n*len(valid), 'cyclic count lower bound')
    print({'phase_length_cases':phases,'clamped_words':clamps,
           'clamped_coordinates':changed,'clamp_fibres':fibres,
           'injected_words':lifted,'pinned_concatenations':concatenations,
           'cyclic_composition_rotations':rotations,
           'scope':'Exact finite identities and injections only; no infinite pressure or entropy verification.'})


if __name__ == '__main__':
    main()
