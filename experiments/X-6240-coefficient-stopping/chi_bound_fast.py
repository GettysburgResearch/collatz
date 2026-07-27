"""Log-space vectorised version of chi_bound.py, to locate where Bmax(j) crosses V.

State: for each k, the max over above-line prefixes of log2(c).  Transitions
  0-step: log2(c) unchanged, k unchanged
  1-step: c <- 3c + 2^t, i.e. log2 -> logaddexp2(log2(c)+log2(3), t)
Both are monotone in c, so tracking the max of log2(c) is exact for the max of c.
Bmax(j) = max over dropped k of  c/D  with log2(D) = j + log2(1 - 2^(k*log2 3 - j)).
"""
import numpy as np, math, sys

J = int(sys.argv[1]) if len(sys.argv) > 1 else 25000
V = 2e9
L3 = math.log2(3.0)
ALPHA = math.log(2)/math.log(3)
NEG = -1e18

logc = np.full(J+2, NEG)
logc[0] = NEG                     # c = 0 at the root; represent 0 as NEG
logc[0] = -1e18
cur = np.full(J+2, NEG); cur[0] = -1e18   # k index -> max log2(c)
cur[0] = -np.inf if False else -1e18

records = []
runmax = -np.inf; runj = None
for t in range(J):
    j = t+1
    # 1-step: from k to k+1 with c -> 3c + 2^t
    a = cur + L3
    one = np.logaddexp2(a, np.full_like(a, float(t)))
    nxt = cur.copy()                                   # 0-step keeps k
    nxt[1:] = np.maximum(nxt[1:], one[:-1])            # 1-step raises k by 1
    need = math.ceil(ALPHA*j - 1e-12)
    ks = np.arange(J+2)
    dropped = ks < need
    logD = j + np.log2(np.maximum(1.0 - np.exp2(np.minimum(ks*L3 - j, -1e-12)), 1e-300))
    ratio = np.where(dropped & (nxt > NEG/2) & (ks*L3 < j), nxt - logD, -np.inf)
    b = float(np.max(ratio)) if ratio.size else -np.inf
    records.append((j, b))
    if b > runmax:
        runmax, runj = b, j
    cur = np.where(ks >= need, nxt, NEG)

print(f"{'j':>7} {'log2 Bmax':>12} {'Bmax':>14}")
run = -np.inf
cross = None
for j, b in records:
    if b > run:
        run = b
        if j in (2,5,8,27,50,100) or (run > 10 and j % 1 == 0 and math.log2(V) - run < 40 and j % 500 == 0):
            pass
    if run >= math.log2(V) and cross is None:
        cross = j
for jm in (100, 1000, 5000, 10000, 15000, 18000, 20000, J):
    if jm <= J:
        r = max(b for j, b in records if j <= jm)
        print(f"{jm:>7} {r:>12.4f} {2**r:>14.4g}")
print(f"\nV = {V:.3g}  (log2 V = {math.log2(V):.4f})")
print(f"running max first reaches V at j = {cross}" if cross else
      f"running max never reaches V for j <= {J}: max = {2**run:.4g} at j = {runj}")
if cross:
    print(f"=> no counterexample to chi = sigma has chi(n) <= {cross-1}")
