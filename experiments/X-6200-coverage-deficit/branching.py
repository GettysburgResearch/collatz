"""X-6200 step 1: the backward tree's branching factor is exactly 4/3.

Predecessors of n under the shortcut map T:
  * 2n            (always;  T(2n) = n)
  * (2n-1)/3      (iff 3 | 2n-1, i.e. n = 2 mod 3; and then it is automatically odd)
So a node has 2 children iff n = 2 mod 3 -- density 1/3 -- giving mean branching 1 + 1/3 = 4/3.
"""
import math


def T(n):
    return (3*n + 1)//2 if n % 2 else n//2


def preds(n):
    out = [2*n]
    if (2*n - 1) % 3 == 0:
        x = (2*n - 1)//3
        if x >= 1 and x % 2 == 1 and T(x) == n:
            out.append(x)
    return out


N = 300000
two = sum(1 for n in range(1, N+1) if len(preds(n)) == 2)
cond = sum(1 for n in range(1, N+1) if n % 3 == 2)
agree = all((len(preds(n)) == 2) == (n % 3 == 2) for n in range(2, N+1))
print(f"n <= {N}: nodes with two predecessors = {two} ({two/N:.6f} of all)")
print(f"          nodes with n = 2 mod 3      = {cond} ({cond/N:.6f})")
print(f"          'two predecessors'  <=>  'n = 2 mod 3'  for all 2 <= n <= {N}: {agree}")
print(f"\nmean branching factor = 1 + 1/3 = {4/3:.10f}")
print(f"so a depth-d tree has ~(4/3)^d nodes, and reaching X^e nodes needs")
print(f"   d = e*lnX/ln(4/3),  i.e.  c_naive(e) = d/log2(X) = "
      f"{math.log(2)/math.log(4/3):.6f} * e")
# sanity: every predecessor really maps back
bad = [n for n in range(2, 20000) if any(T(p) != n for p in preds(n))]
print(f"\nall predecessors verified to map back: {not bad}")
