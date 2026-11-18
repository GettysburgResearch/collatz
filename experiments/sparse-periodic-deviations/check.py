"""Exact finite checks for the shifted block algebra; no cutoff for the theorem."""
from itertools import product
from math import prod


def affine(word):
    p, c, q = 1, 0, 1
    for bit in word:
        if bit:
            p, c = 3*p, 3*c+q
        q *= 2
    return p, c, q


def block(n, length):
    word = []
    for _ in range(length):
        word.append(n % 2)
        n = (3*n+1)//2 if n % 2 else n//2
    return tuple(word), n


def main():
    menus = groups = traces = 0
    for length in range(1, 6):
        menu = list(product(range(2), repeat=length))
        table = {w: affine(w) for w in menu}
        for w in menu:
            P, C, Q = table[w]
            if P <= Q:
                continue
            menus += 1
            p, b = {}, {}
            for v, (pv, cv, _) in table.items():
                p[v] = pv
                b[v] = (P-Q)*cv + (Q-pv)*C
                assert (b[v] == 0) == (v == w)
            for first, second in product(menu, repeat=2):
                for a in (0, 1, 3):
                    cp, cc, cq = affine(first+w*a+second)
                    expected = (P-Q)*cc+(cq-cp)*C
                    assert expected == p[second]*P**a*b[first]+Q**(a+1)*b[second]
                    assert (expected == 0) == (first == second == w)
                    groups += 1
            for x in range(1, 91):
                n, runs, mismatches, units = x, [], [], []
                for _ in range(5):
                    entry, a = (P-Q)*n+C, 0
                    v, endpoint = block(n, length)
                    while v == w:
                        n, a = endpoint, a+1
                        v, endpoint = block(n, length)
                    assert entry % Q**a == 0
                    runs.append(a)
                    mismatches.append(v)
                    units.append(entry//Q**a)
                    n = endpoint
                k = 4
                factors = [p[v]*P**a for v, a in zip(mismatches, runs)]
                lhs = Q**sum(b+1 for b in runs[1:]) * units[k]
                total = units[0]*prod(factors[:k])
                for i in range(k):
                    weight = Q**sum(b+1 for b in runs[1:i+1]) * prod(factors[i+1:k])
                    total += weight*b[mismatches[i]]
                assert total == lhs
                traces += 1
    print(f"{menus} expanding templates; {groups} composite constants; {traces} four-transition identities")


if __name__ == "__main__":
    main()
