import sys
P = 3**12; Q = 2**19
A = [229376, 258048, 290304, 326592, 367416, 413343]
Aset = set(A)
invP = pow(P, -1, Q)

def digits_of(x, N):
    """deterministic digit sequence; returns number of legal steps (capped at N)"""
    k = 0
    for _ in range(N):
        d = (-P*x) % Q
        if d not in Aset: return k
        x = (P*x + d)//Q
        k += 1
    return k

# ---- brute force check for small depth ----
best = {}
for x in range(1, 3_000_000):
    k = digits_of(x, 4)
    for j in range(1, k+1):
        if j not in best: best[j] = x
print("brute force (x < 3e6):", {k: best[k] for k in sorted(best)})

# ---- lifting enumeration ----
BOUND = 1 << int(sys.argv[1]) if len(sys.argv) > 1 else 1 << 120
level = [(0, 0)]      # (r, X=x_k) ; depth 0 root class = all integers
mod = 1
print(f"\nlifting enumeration, bound = 2^{BOUND.bit_length()-1}")
ms = []
for k in range(0, 60):
    invPk1 = pow(invP, k+1, Q)
    nxt = []
    for (r, X) in level:
        base = (-P*X) % Q
        for a in A:
            t = ((base - a) % Q) * invPk1 % Q
            r2 = r + mod*t
            if r2 > BOUND or r2 == 0: continue
            xk = X + pow(P, k)*t
            assert (P*xk + a) % Q == 0
            nxt.append((r2, (P*xk + a)//Q))
    mod *= Q
    level = nxt
    if not level:
        print(f"depth {k+1}: NO survivor <= bound"); break
    m = min(r for r,_ in level)
    ms.append(m)
    print(f"depth {k+1:3d}: survivors<=bound = {len(level):>10}   m_{k+1} = {m}   ({m:.6e})"
          + (f"   ratio = {m/ms[-2]:.1f}" if len(ms) > 1 else ""))
