"""Q-6174 addendum: the itinerary carries no information about odd-modulus residues.

Every length-L itinerary occurs together with EVERY residue class mod M for odd M, so no
congruence condition at an odd modulus can shrink the itinerary constraint set.  (Immediate
from CRT + the Terras bijection; verified here because the first version of this check had an
off-by-one that made it report False.)
"""
from collections import defaultdict


def T(n):
    return (3*n + 1)//2 if n % 2 else n//2


def check(L, M):
    period = M * 2**L
    seen = defaultdict(set)
    for n in range(period):          # FULL period — an off-by-one here fakes a dependence
        w, v = [], n
        for _ in range(L):
            w.append(v % 2)
            v = T(v)
        seen[tuple(w)].add(n % M)
    return len(seen), all(len(v) == M for v in seen.values())


if __name__ == "__main__":
    for L, M in [(10, 27), (12, 27), (8, 81), (10, 5), (10, 7), (9, 35)]:
        n_it, full = check(L, M)
        print(f"L={L:>3}  M={M:>3}: {n_it:>5} itineraries (expect {2**L:>5}); "
              f"every itinerary pairs with all {M} residues mod {M}: {full}")
    print("\nAlso: after any odd step the value is == 2 mod 3, so the orbit never meets a")
    print("multiple of 3 again -- a real fact, but one that constrains the VALUE, not the")
    print("itinerary, and is therefore invisible to any dimension argument.")
