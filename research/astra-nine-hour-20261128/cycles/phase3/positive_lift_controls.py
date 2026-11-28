"""Exact independent full-lattice lift, semigroup-duality, and finite distinction controls."""

from itertools import combinations
from math import gcd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "phase2"))
from semigroup_controls import build, need, physical_numerator


def frobenius(support, u, n):
    """Apéry minimum in every residue from generators support, then +u and +n."""
    large = max(support) + 2*n*u
    ap = [large]*n
    inv = pow(u, -1, n)
    for h in support:
        i = h*inv % n
        ap[i] = min(ap[i], h)
    for i in range(2*n):
        ap[(i+1) % n] = min(ap[(i+1) % n], ap[i % n]+u)
    return max(ap)-n


def main():
    types = cuts = lifts = duals = 0
    for n in range(2, 13):
        for u in range(1, n):
            if 2**n <= 3**u:
                continue
            for pos in combinations(range(n), u):
                w = tuple(int(i in pos) for i in range(n))
                if any(w[i:]+w[:i] < w for i in range(1, n)):
                    continue
                raw = [physical_numerator(w[k:]+w[:k]) for k in range(n)]
                if gcd(u, n) == 1:
                    _, points, holes, _ = build(w)
                    support = {h for (h, _), bit in zip(points, w) if bit}
                    c = 1+max((h for h, _ in holes), default=-1)
                    F = frobenius(support, u, n)
                    need(F == n-u+c-1, "Frobenius number of the odd-support ideal")
                    need(u*n-u-n-F+max(support) == n*(u-1), "effective greatest height")
                    duals += 1
                for k in range(n):
                    elapsed = sorted((i-k) % n for i in pos)
                    canon = sum(2**a * 3**(u-1-j) for j, a in enumerate(elapsed))
                    need(canon == raw[k], "physical cut evaluation")
                    # All mixtures of a zero-lap and a one-lap term at this actual cut.
                    base = 2*u-1
                    original = sum(2**a * 3**(base-j) for j, a in enumerate(elapsed))
                    for mask in range(1 << u):
                        value = sum(2**(a+n*((mask>>j)&1)) *
                                    3**(base-j-u*((mask>>j)&1)) for j, a in enumerate(elapsed))
                        need(value >= original >= min(raw), "mixed independent formal lifts")
                        lifts += 1
                    cuts += 1
                types += 1
    # At D=7, the additional numerical relation 2^3=1 admits a smaller smooth lift.
    need(min(physical_numerator(w) for w in ((1,1,0,0),(1,0,0,1),(0,0,1,1),(0,1,1,0))) == 5,
         "formal optimum five")
    need((5*3) % 7 == 1 and (5*2) % 7 == 3 and 1+3 < 5, "finite numerical exception")
    print(f"{types} positive necklaces and {cuts} actual cuts through n=12 passed.")
    print(f"{lifts} independent zero/one-lap mixtures dominated their physical numerator.")
    print(f"{duals} coprime cases satisfied the exact Frobenius and effective-height formulas.")
    print("At n=4, u=2, D=7, an extra numerical relation gives smooth sum 4 below formal optimum 5.")


if __name__ == "__main__":
    main()
