"""Adversarial validation of the T-6140/T-6141 cycle machinery on cycles that EXIST.

The machinery was derived for positive 3x+1 cycles, of which none are known. Here it is
tested against objects that do exist: the negative 3x+1 cycles, and the positive 5x+1 cycle.

Claimed identity (T-6141a, generalised to multiplier m):
    prod_i (m + 1/n_i) = 2^q          over the k odd elements of the cycle
Claimed formula (T-6140A, generalised):
    x_w = c_w / (2^q - m^k),   c_w = sum_{i=1..k} m^(k-i) 2^(e_i)
"""
from fractions import Fraction as F


def T(n, m):
    return (m*n + 1)//2 if n % 2 else n//2


def find_cycle(n0, m, cap=10**7):
    seen, order = {}, []
    n = n0
    while n not in seen:
        seen[n] = len(order)
        order.append(n)
        n = T(n, m)
        if abs(n) > cap:
            return None
    return order[seen[n]:]


def analyse(cycle, m, label):
    q = len(cycle)
    odd = [n for n in cycle if n % 2]
    k = len(odd)
    # parity word starting at cycle[0]; e_i = positions of the odd steps
    es = [i for i, n in enumerate(cycle) if n % 2]
    c_w = sum(m**(k-1-j) * 2**es[j] for j in range(k))
    den = 2**q - m**k
    x_w = F(c_w, den) if den else None
    prod = F(1)
    for n in odd:
        prod *= F(m*n + 1, n)
    print(f"{label}")
    print(f"   cycle           : {cycle}")
    print(f"   q={q}  k={k}   2^q - m^k = {2**q} - {m**k} = {den}")
    print(f"   prod (m + 1/n_i) = {prod}   == 2^q = {2**q} ?  {prod == 2**q}")
    print(f"   c_w = {c_w},  x_w = c_w/(2^q - m^k) = {x_w}   == cycle start {cycle[0]} ?"
          f"  {x_w == cycle[0]}")
    print(f"   sign check: cycle is {'negative' if cycle[0] < 0 else 'positive'}, "
          f"2^q {'<' if den < 0 else '>'} m^k  -> consistent: "
          f"{(cycle[0] < 0) == (den < 0)}")
    return prod == 2**q and x_w == cycle[0] and ((cycle[0] < 0) == (den < 0))


ok = True
print("=== 3x+1, the three known NEGATIVE cycles ===")
for start in (-1, -5, -17):
    cyc = find_cycle(start, 3)
    ok &= analyse(cyc, 3, f"3x+1 cycle through {start}")
print("\n=== 5x+1, the known POSITIVE cycles ===")
for start in (1, 13, 17):
    cyc = find_cycle(start, 5)
    if cyc:
        ok &= analyse(cyc, 5, f"5x+1 cycle through {start}")
print(f"\nALL CYCLE-MACHINERY CHECKS PASSED: {ok}")
