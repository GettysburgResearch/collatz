"""Decisive test of the digit-consumption claim: does a mod-3^k residue chain converge
to the measured descent distribution as k grows?

State = node residue mod 3^k.
  doubling : r -> 2r mod 3^k                                (exact)
  descent  : available iff r = 2 mod 3; child is determined mod 3^(k-1) only, so the
             top 3-adic digit is unknown -- modelled as uniform on the 3 lifts.
If each descent really consumes one 3-adic digit, larger k should track the measurement
further into the tail.
"""
from collections import Counter

D = 30


def measured(D):
    def kids(n):
        out = [(2*n, 0)]
        if n % 3 == 2:
            c = (2*n-1)//3
            if c != 1:
                out.append((c, 1))
        return out
    lvl = [(1, 0)]
    for _ in range(D):
        lvl = [(m, b+t) for n, b in lvl for m, t in kids(n)]
    c = Counter(b for _, b in lvl)
    N = len(lvl)
    return [c.get(b, 0)/N for b in range(D+1)], N


obs, NM = measured(D)


def model(k):
    M = 3**k
    Mk = 3**(k-1)
    cur = [[0.0]*(D+1) for _ in range(M)]
    cur[1 % M][0] = 1.0                        # root n = 1
    for _ in range(D):
        nxt = [[0.0]*(D+1) for _ in range(M)]
        for r in range(M):
            row = cur[r]
            s = sum(row)
            if s == 0.0:
                continue
            r2 = (2*r) % M
            for b in range(D+1):
                if row[b]:
                    nxt[r2][b] += row[b]
            if r % 3 == 2:
                c0 = ((2*r - 1)//3) % Mk
                for u in range(3):
                    rc = (c0 + Mk*u) % M
                    for b in range(D):
                        if row[b]:
                            nxt[rc][b+1] += row[b]/3.0
        cur = nxt
    tot = sum(sum(row) for row in cur)
    return [sum(cur[r][b] for r in range(M))/tot for b in range(D+1)]


print(f"depth {D}, measured over {NM:,} paths; max measured b = "
      f"{max(b for b in range(D+1) if obs[b] > 0)}\n")
print(f"{'b':>4} {'measured':>10} " + " ".join(f"{'k='+str(k):>9}" for k in (1, 3, 5, 7, 9)))
mods = {k: model(k) for k in (1, 3, 5, 7, 9)}
for b in range(0, 17):
    if obs[b] > 0 or any(mods[k][b] > 1e-4 for k in mods):
        print(f"{b:>4} {obs[b]:>10.5f} " + " ".join(f"{mods[k][b]:>9.5f}" for k in (1,3,5,7,9)))
mo = sum(b*obs[b] for b in range(D+1))
print(f"\n{'mean b':>10}: measured {mo:.4f}   " +
      "   ".join(f"k={k}: {sum(b*mods[k][b] for b in range(D+1)):.4f}" for k in (1,3,5,7,9)))
print(f"{'L1 error':>10}: " +
      "   ".join(f"k={k}: {sum(abs(mods[k][b]-obs[b]) for b in range(D+1)):.4f}"
                 for k in (1,3,5,7,9)))
