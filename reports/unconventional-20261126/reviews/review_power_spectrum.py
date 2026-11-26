"""Exact finite controls for the power-spectrum and Bergman transfer arguments."""

if not __debug__:
    raise SystemExit("This independent assertion-based replay requires Python without -O or -OO.")

from collections import Counter
from math import comb
from fractions import Fraction


def inverse(y):
    yield 2*y, 0
    if y % 3 == 2:
        yield (2*y-1)//3, 1


def forward(x):
    return (3*x+1)//2 if x%2 else x//2


def run():
    checked = 0
    for k in range(1,9):
        module = 3**k
        total_weight = 0
        per_weight = Counter()
        for r in range(module):
            y = module*1000+r
            parents = [(y, 0)]
            for _ in range(k):
                parents = [(z, q+b) for a,q in parents for z,b in inverse(a)]
            assert len({x for x,_ in parents}) == len(parents)
            by_q = Counter(q for _,q in parents)
            for q, n_words in by_q.items():
                assert n_words <= 1+2**(k-q)
                per_weight[q] += n_words
                total_weight += n_words*2**k*3**(k-q)
            checked += len(parents)
        assert total_weight == 20**k    # divided by 3^(2k) gives the class mean
        assert all(per_weight[q] == comb(k,q)*3**(k-q) for q in range(k+1))
        # Build two disjoint explicit odd arms as in O8 at a large representative.
        a = (-pow(4,-1,3**(k+2))) % 3**(k+2) + 1000*3**(k+2)
        b = (2*a, (2*a-1)//3)
        nodes = {a, *b}
        assert all(forward(z)==a for z in b)
        for z in b:
            u = 2*z
            assert forward(u)==z and u not in nodes
            nodes.add(u)
            for j in range(k):
                v = 2*(u+1)//3-1
                assert v not in nodes and v%2 and forward(v)==u
                u=v
                nodes.add(u)
    print(f"verified {checked} ordinary inverse endpoints over full residues through k=8; eight two-arm patches")


if __name__ == "__main__":
    run()
