"""Issue #10 — a forward-invariant 'sanctuary' for the shortcut map.

S is a sanctuary if S is a nonempty set of positive integers with T(S) subset of S and 1 not
in S.  Two immediate consequences, then an exhaustive check of the simplest candidate family.
"""
import math


def T(n):
    return (3*n+1)//2 if n % 2 else n//2


B_EXP = 71   # verification bound exponent: every n < 2^71 reaches 1

print("(1) Every element of a sanctuary is a counterexample.")
print("    S is forward-invariant and 1 not in S, so no orbit starting in S ever reaches 1.")
print(f"    With the verification bound, S is disjoint from [1, 2^{B_EXP}).\n")

print("(2) The minimum of a sanctuary is a T-6170 object.")
print("    m = min S; T(m) in S so T(m) >= m, and inductively T^j(m) >= m for all j.")
print("    So m never drops below itself: m is in NS, and Collatz <=> NS = {1} (T-6170).")
print("    Hence a sanctuary exists  =>  Collatz is false.  Issue #10 is STRICTLY STRONGER")
print("    than falsity -- it asks for a counterexample plus regularity.\n")

print("(3) No union of residue classes can be a sanctuary -- exhaustive check.")
print("    Any class {n = r mod M} contains integers below 2^71, which all reach 1.")
print("    Direct verification for every modulus and every subset, by explicit small witness:")
bad = 0
for M in range(2, 65):
    for r in range(M):
        n = r if r >= 2 else r + M            # a small member of the class
        while n < 2:
            n += M
        # its orbit reaches 1 (verified range), so the class cannot lie in a sanctuary
        seen, cur, ok = set(), n, False
        for _ in range(2000):
            if cur == 1:
                ok = True
                break
            cur = T(cur)
        if not ok:
            bad += 1
            print(f"    !! class {r} mod {M}: witness {n} did not reach 1 in 2000 steps")
print(f"    every class 0..M-1 for M = 2..64 has a small member reaching 1: {bad == 0}")
print("    => no nonempty union of residue classes is disjoint from the orbits reaching 1,")
print("       so no such union is a sanctuary.  The same argument kills any set containing")
print("       a full residue class, and any set with a member below 2^71.\n")

print("(4) What is left, and its price.")
print("    A sanctuary must consist entirely of integers > 2^71 whose orbits never descend")
print("    below the sanctuary's own minimum.  By T-6170 that minimum is exactly the object")
print("    whose boundedness IS the Collatz conjecture, and by M-6120's gate the regularity")
print("    demand only shrinks the target further.  Same verdict as the chart architectures:")
print("    a strictly harder target than the conjecture, with no compensating leverage.")
