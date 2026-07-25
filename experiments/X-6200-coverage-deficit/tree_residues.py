"""Why the escape model fails: the backward tree does NOT sample integers uniformly mod 3.

Backward step:  n -> 2n  always;  n -> (2n-1)/3  iff n = 2 (mod 3).
Under doubling the residue moves  1 -> 2 -> 1 -> ...  and  0 -> 0.
So residue 0 is ABSORBING: a node divisible by 3 has one child forever, and its entire
doubling subtree never branches again.  The density statement "1/3 of integers are 2 mod 3,
so mean branching is 4/3" is about integers, not about tree nodes -- and the tree is biased.

This measures the true per-level branching of the tree and the residue distribution.
"""
from collections import Counter

DEPTH = 46


def children(n):
    out = [2*n]
    if n % 3 == 2:
        out.append((2*n - 1)//3)
    return out


level = [1]
print(f"{'d':>4} {'nodes':>12} {'branching':>10} {'frac 0 mod 3':>13} "
      f"{'frac 1':>8} {'frac 2':>8}")
for d in range(DEPTH):
    c = Counter(n % 3 for n in level)
    N = len(level)
    nxt = [m for n in level for m in children(n)]
    if d % 4 == 0 or d == DEPTH-1:
        print(f"{d:>4} {N:>12,} {len(nxt)/N:>10.5f} {c[0]/N:>13.5f} "
              f"{c[1]/N:>8.5f} {c[2]/N:>8.5f}")
    level = nxt
print(f"\nnaive prediction (integers): branching 4/3 = {4/3:.5f}, each residue 1/3 = 0.33333")
print("measured: the tree's residue distribution drifts toward 0 mod 3, and the branching")
print("factor falls below 4/3 accordingly.  Residue 0 is absorbing under doubling, so every")
print("node divisible by 3 contributes a permanently non-branching doubling chain.")
