#!/usr/bin/env python3
# X-9702 condensed check (exact arithmetic, stdlib only, deterministic; ~1 s).
# Full pipeline is in proof_markdown; this snippet re-verifies the headline facts at N=50000.
from fractions import Fraction
from collections import deque, Counter

def U(n): return n // 2 if n % 2 == 0 else (3 * n - 1) // 2
def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2
N = 50000
CYC_U = [[1], [5, 7, 10], [17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34]]
for cyc in CYC_U:
    for i, c in enumerate(cyc): assert U(c) == cyc[(i + 1) % len(cyc)]
assert T(0) == 0 and T(1) == 2 and T(2) == 1

def analyze(f, lo, n_max):
    color = bytearray(n_max + 1); reach = [-2] * (n_max + 1); cycles = []
    par = list(range(n_max + 1)); pre = [[] for _ in range(n_max + 1)]
    def find(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    for m in range(lo, n_max + 1):
        fm = f(m)
        if fm <= n_max:
            pre[fm].append(m)
            ra, rb = find(m), find(fm)
            if ra != rb: par[ra] = rb
    for s in range(lo, n_max + 1):
        if color[s]: continue
        path, onpath, v = [], {}, s
        while True:
            if v > n_max: res = -1; break
            if color[v]: res = reach[v]; break
            if v in onpath: cycles.append(path[onpath[v]:]); res = len(cycles) - 1; break
            onpath[v] = len(path); path.append(v); v = f(v)
        for u in path: color[u] = 1; reach[u] = res
    return cycles, reach, find, pre

# (1) U components at N=50000
cyc_u, reach_u, find_u, pre_u = analyze(U, 1, N)
assert sorted(map(sorted, cyc_u)) == sorted(map(sorted, CYC_U))
root = [0] + [find_u(v) for v in range(1, N + 1)]
size = Counter(root[1:]); r1, r5, r17 = root[1], root[5], root[17]
assert (size[r1], size[r5], size[r17]) == (9514, 9923, 10023)
arts = [r for r in size if r not in (r1, r5, r17)]
assert len(arts) == 8333 and sum(size[r] for r in arts) == 20540
assert all(reach_u[v] == -1 for v in range(1, N + 1) if root[v] in arts)
# (2) exact fixed measures + fixed-space dim 3 via acyclic propagation
for cyc in CYC_U:
    w = Fraction(1, len(cyc)); mu = {c: w for c in cyc}
    for n in range(1, N + 1):
        assert sum((mu.get(m, Fraction(0)) for m in pre_u[n]), Fraction(0)) == mu.get(n, Fraction(0))
cv = set(c for cyc in cyc_u for c in cyc)
cnt = [0] * (N + 1); q = deque(); nf = 0
for v in range(1, N + 1):
    if v not in cv:
        cnt[v] = len(pre_u[v])
        if cnt[v] == 0: q.append(v)
while q:
    v = q.popleft(); nf += 1; w = U(v)
    if w <= N and w not in cv:
        cnt[w] -= 1
        if cnt[w] == 0: q.append(w)
assert nf == N - 15   # => dim ker(P_U - I) = 3, basis = cycle indicators
# (3) Z[omega] eigenvector on comp(5); no Z[i] eigenvector there
def wmul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)
OM = {0: (1, 0), 1: (0, 1), 2: (-1, -1)}
comp5 = [v for v in range(1, N + 1) if root[v] == r5]
edges5 = [(m, U(m)) for m in comp5 if U(m) <= N]
assert len(edges5) == len(comp5) == 9923           # zero sinks: whole component is interior
g = {5: 0}; k = {5: 0}; dq = deque([5])
while dq:
    v = dq.popleft(); w = U(v)
    nb = ([(w, 1)] if w <= N else []) + [(p, -1) for p in pre_u[v]]
    for u, d in nb:
        if u not in g: g[u] = (g[v] + d) % 3; k[u] = (k[v] + d) % 4; dq.append(u)
for m, w in edges5:
    assert g[w] == (g[m] + 1) % 3
    assert OM[g[w]] == wmul((0, 1), OM[g[m]])      # a_{U(m)} = omega*a_m exactly in Z[omega]
bad = [(m, w) for m, w in edges5 if k[w] != (k[m] + 1) % 4]
assert bad == [(7, 10)]                            # one inconsistent edge => lambda=i space is {0}
# (4) T truncation and lambda=-1 eigenvector
cyc_t, reach_t, find_t, pre_t = analyze(T, 0, N)
assert sorted(map(sorted, cyc_t)) == [[0], [1, 2]]
rt = [find_t(v) for v in range(N + 1)]
st = Counter(rt); t0, t1 = rt[0], rt[1]
assert st[t0] == 1 and st[t1] == 29778
artsT = [r for r in st if r not in (t0, t1)]
assert len(artsT) == 8333 and sum(st[r] for r in artsT) == 20222
compT1 = [v for v in range(N + 1) if rt[v] == t1]
h = {1: 0}; dq = deque([1])
while dq:
    v = dq.popleft(); w = T(v)
    if w <= N and w not in h: h[w] = (h[v] + 1) % 2; dq.append(w)
    for p in pre_t[v]:
        if p not in h: h[p] = (h[v] + 1) % 2; dq.append(p)
assert set(h) == set(compT1)
for m in compT1:
    if T(m) <= N: assert (-1) ** h[T(m)] == -((-1) ** h[m])   # a_{T(m)} = -a_m exactly
# full-orbit convergence below N for both maps
good_u = set(c for cyc in CYC_U for c in cyc); good_t = {1, 2}
for f, good in ((U, good_u), (T, good_t)):
    for n in range(1, N + 1):
        seen, v = [], n
        while v not in good: seen.append(v); v = f(v)
        good.update(seen)
print("X-9702 condensed check: ALL PASSED")