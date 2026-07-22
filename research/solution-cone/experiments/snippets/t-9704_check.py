# T-9704 finite sanity checks (exact arithmetic; stdlib only; deterministic).
# Checks the *finite shadows* of claims (1)-(5) for the shortcut Collatz map T
# and for the 3n-1 control map U.  Numerics are sanity checks, NOT proof.
from fractions import Fraction

def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2   # on N_0
def U(n): return n // 2 if n % 2 == 0 else (3 * n - 1) // 2   # on N_{>=1}

# ---- Lemma 1 (preimage structure), brute force vs formula ----
def pre_T(n):
    s = [2 * n]
    if n % 3 == 2:
        s.append((2 * n - 1) // 3)
    return sorted(s)

def pre_U(n):
    s = [2 * n]
    if n % 3 == 1:
        s.append((2 * n + 1) // 3)
    return sorted(s)

M = 3000
for n in range(M):
    assert pre_T(n) == sorted(m for m in range(2 * M + 2) if T(m) == n)
for n in range(1, M):
    assert pre_U(n) == sorted(m for m in range(1, 2 * M + 2) if U(m) == n)

# ---- pushforward P on finitely supported vectors (exact) ----
def push(f, b):
    out = {}
    for m, v in b.items():
        out[f(m)] = out.get(f(m), Fraction(0)) + v
    return {k: v for k, v in out.items() if v != 0}

CYC_T = [(0,), (1, 2)]
CYC_U = [(1,), (5, 7, 10), (17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34)]

for f, pre, cycles in ((T, pre_T, CYC_T), (U, pre_U, CYC_U)):
    cyc_elems = {x for Z in cycles for x in Z}
    for Z in cycles:
        for i, x in enumerate(Z):
            assert f(x) == Z[(i + 1) % len(Z)]              # really a cycle
        mu = {x: Fraction(1) for x in Z}
        assert push(f, mu) == mu                            # (2): P mu_Z = mu_Z
        # Lemma 3: each cycle point has exactly ONE periodic preimage = its
        # cycle predecessor; all other preimages are off every known cycle.
        for i, x in enumerate(Z):
            inZ = [m for m in pre(x) if m in Z]
            assert inZ == [Z[(i - 1) % len(Z)]]
            for m in pre(x):
                if m not in Z:
                    assert m not in cyc_elems

# (2)/(3): rational combinations of cycle measures are fixed (nonneg and signed)
b = {}
for Z, c in zip(CYC_U, (Fraction(2), Fraction(1, 3), Fraction(-7, 5))):
    for x in Z:
        b[x] = c
assert push(U, b) == b
# delta at a non-periodic point is NOT fixed
assert push(U, {3: Fraction(1)}) != {3: Fraction(1)}
assert push(T, {4: Fraction(1)}) != {4: Fraction(1)}

# ---- (1) norm / mass conservation and (4) duality, exact ----
def a_val(n):  # deterministic bounded "l-infinity" test function
    return Fraction((1103515245 * n + 12345) % 2001 - 1000, 1000)

btest = {n: Fraction((-1) ** n * (n % 13 + 1), n + 1) for n in range(1, 60)}
for f in (T, U):
    pb = push(f, btest)
    assert sum(pb.values()) == sum(btest.values())          # signed mass conservation
    assert sum(abs(v) for v in pb.values()) <= sum(abs(v) for v in btest.values())  # contraction
    nn = {k: abs(v) for k, v in btest.items()}
    assert sum(push(f, nn).values()) == sum(nn.values())    # equality on nonneg => ||P||_1 = 1
    lhs = sum(a_val(f(m)) * v for m, v in btest.items())    # <Fa, b>
    rhs = sum(a_val(n) * v for n, v in pb.items())          # <a, Pb>
    assert lhs == rhs                                       # (4)

# ---- (5) components vs cycles on truncations (union-find on touched vertices) ----
class DSU:
    def __init__(self): self.p = {}
    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, x, y): self.p[self.find(x)] = self.find(y)

def survey(f, start_iter, cycles):
    cyc_elems = {x for Z in cycles for x in Z}
    dsu = DSU()
    for n in start_iter:
        x, path = n, set()
        while x not in cyc_elems:
            assert x not in path, "unexpected new cycle"
            path.add(x)
            dsu.union(x, f(x))
            x = f(x)
    for Z in cycles:
        for i, x in enumerate(Z):
            dsu.union(x, Z[(i + 1) % len(Z)])
    roots = {dsu.find(x) for x in list(dsu.p)}
    cyc_roots = {dsu.find(Z[0]) for Z in cycles}
    assert len(cyc_roots) == len(cycles)   # distinct cycles in distinct components
    assert roots == cyc_roots              # every touched vertex joins a cycle's component
    return len(roots)

# every U-orbit started in [1,20000] falls into one of the 3 known cycles;
# the truncated graph has exactly 3 weak components, one per cycle:
assert survey(U, range(1, 20001), CYC_U) == 3
# every T-orbit started in [0,20000] falls into {0} or {1,2}; 2 components:
assert survey(T, range(0, 20001), CYC_T) == 2

print("all T-9704 finite checks passed")