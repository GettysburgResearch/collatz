"""Exact arithmetic for the single-crossing obstruction and unrestricted B4."""
from collections import defaultdict
from itertools import combinations_with_replacement, product
from fractions import Fraction as F
from math import prod

from check_unrestricted_triple_products import clocks, offsets, require, verify_aligned


def inspect(word):
    times = clocks(word)
    buckets = defaultdict(list)
    pairs = special = zero_prefixes = 0
    for inds in combinations_with_replacement(range(len(times)), 4):
        key = sum(inds), sum(times[i] for i in inds)
        for other in buckets[key]:
            pairs += 1
            a, b = inds, other
            c = [a.count(i)-b.count(i) for i in range(len(times))]
            m = max(i for i,v in enumerate(c) if v)
            if c[m] < 0:
                a, b = b, a
                c = [-v for v in c]
            if c[m] % 3:
                verify_aligned(word, a, b)
                continue
            special += 1
            i = next(i for i,v in enumerate(c) if v)
            require(c[m] == 3 and c[i] == 1 and all(i < j < m for j in b), 'exception shape')
            s = offsets(times, m)
            G = sum(v*w for v,w in zip(c, s))
            ds = [sum(c[:m-j]) for j in range(m)]
            require(not any(x>0 and y<0 for j,x in enumerate(ds) for y in ds[j+1:]), 'single crossing')
            increments = [s[m-1-j]-s[m-j] for j in range(m)]
            partial = F()
            for d,w in zip(ds, increments):
                partial += d*w
                if partial == 0:
                    zero_prefixes += 1
                require(G >= 0 or partial < 0, 'negative G gives negative prefixes')
            for Z in (s[i]+1, 2*s[i]+5):
                if G >= 0:
                    require(prod(Z-s[n] for n in a) < prod(Z-s[n] for n in b), 'convexity sign')
        buckets[key].append(inds)
    return pairs, special, zero_prefixes


def main():
    words = [w for L in range(3,6) for w in product((1,2,3), repeat=L)]
    words += [(1,)*10, (2,)*10, (100,1,100,1,100,1,100), (1,1,1,401,1,1,1,401)]
    totals = [sum(group) for group in zip(*(inspect(w) for w in words))]
    require(totals[1] > 0, 'missing special cases')
    print(f'{totals[0]} aligned quadruples, {totals[1]} terminal-three cases, {totals[2]} zero prefixes checked')


if __name__ == '__main__':
    main()
