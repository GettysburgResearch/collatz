#!/usr/bin/env python3
# X-9701: coefficient identity checker + truncated-kernel boundary-artifact accounting.
# EMPIRICAL experiment. Exact integer arithmetic only. Deterministic (fixed LCG seed).
# python3 standard library only.

import sys
sys.setrecursionlimit(10000)

N = 100000  # main verification bound for parts (1), (2), (4)

# ---------- Two independent implementations of the shortcut map T ----------
def T_arith(n):
    """Arithmetic implementation: n/2 if even, (3n+1)/2 if odd."""
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n + 1) // 2

def T_bits(n):
    """Bit-operation implementation (different code path):
       even: n >> 1 ; odd: (n + 2n + 1) >> 1 using shift for 2n."""
    if n & 1:
        return (n + (n << 1) + 1) >> 1
    else:
        return n >> 1

# ---------- Deterministic test vector (explicit LCG, no library RNG) ----------
def make_vector(length, seed=987654321):
    a = [0] * length
    s = seed
    for i in range(length):
        s = (1103515245 * s + 12345) % (1 << 31)
        a[i] = s  # arbitrary nonneg integers, exact
    return a

# a must be defined up to max T(m) for m <= N: max is T(N-1 or N odd) = (3m+1)/2 <= (3N+1)/2
LEN = (3 * N + 1) // 2 + 2
a = make_vector(LEN)

# ================= PART 1: F coefficientwise, two code paths =================
def apply_F(vec, upto, Timpl):
    """(F a)_m = a_{T(m)} for m = 0..upto. Requires len(vec) > max T(m)."""
    return [vec[Timpl(m)] for m in range(upto + 1)]

Fa1 = apply_F(a, N, T_arith)
Fa2 = apply_F(a, N, T_bits)
part1_agree = (Fa1 == Fa2)
assert part1_agree, "PART 1 FAILURE: implementations disagree"

# even/odd split identity: (Fa)_{2k} = a_k ; (Fa)_{2k+1} = a_{3k+2}
split_even_ok = all(Fa1[2 * k] == a[k] for k in range(0, N // 2 + 1))
split_odd_ok = all(Fa1[2 * k + 1] == a[3 * k + 2] for k in range(0, (N - 1) // 2 + 1))
assert split_even_ok and split_odd_ok, "PART 1 FAILURE: even/odd split identity"
print("PART 1 OK: (Fa)_m = a_{T(m)} agrees between arithmetic and bit implementations "
      f"for all m <= {N}; even split (Fa)_2k = a_k and odd split (Fa)_(2k+1) = a_(3k+2) verified.")

# ============ PART 2: cube-root-of-unity filter, exact Z[omega] arithmetic ============
# Represent x = u + v*omega in Z[omega], omega = exp(2*pi*i/3), omega^2 = -1 - omega.
# omega^e for e mod 3: 0 -> (1,0), 1 -> (0,1), 2 -> (-1,-1).
OMEGA_POW = {0: (1, 0), 1: (0, 1), 2: (-1, -1)}

def filter_weight(n):
    """S(n) = sum_{j=0..2} omega^{j*(n-2)} computed exactly in Z[omega].
       Must equal 3 if n = 2 (mod 3), else 0."""
    u, v = 0, 0
    for j in range(3):
        e = (j * (n - 2)) % 3
        du, dv = OMEGA_POW[e]
        u += du
        v += dv
    return (u, v)

# Verify the filter is exactly 3 * [n = 2 mod 3] (rational integer, divisible by 3),
# and build the AP-extraction b_k = (1/3) * S applied at index 3k+2.
filter_ok = True
for n in range(0, LEN):
    u, v = filter_weight(n)
    if v != 0 or u % 3 != 0:
        filter_ok = False
        break
    ind = u // 3  # exact integer division
    if ind != (1 if n % 3 == 2 else 0):
        filter_ok = False
        break
assert filter_ok, "PART 2 FAILURE: omega-filter does not equal AP indicator"

# AP extraction via the exact filter: masked_n = a_n * (S(n)/3); b_k = masked_{3k+2}
masked = [a[n] * (filter_weight(n)[0] // 3) for n in range(LEN)]
Kmax = (N - 1) // 2  # odd m = 2k+1 <= N  =>  k <= (N-1)/2
b = [masked[3 * k + 2] for k in range(Kmax + 1)]  # extraction from AP n = 3k+2

# odd-branch of F equals AP-extraction composed with reindexing k -> 2k+1:
odd_branch_ok = all(Fa1[2 * k + 1] == b[k] for k in range(Kmax + 1))
assert odd_branch_ok, "PART 2 FAILURE: odd branch != AP extraction o reindex"
print(f"PART 2 OK: exact Z[omega] filter S(n) = 3*[n=2 mod 3] verified for all n < {LEN}; "
      f"odd-branch (Fa)_(2k+1) = (AP-extract a)_k for all k <= {Kmax} (all odd m <= {N}).")

# ================= PART 3: truncated-kernel accounting =================
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        p = self.p
        r = x
        while p[r] != r:
            r = p[r]
        while p[x] != r:
            p[x], x = r, p[x]
        return r
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.p[rx] = ry

def reaches_target(n, targets, Timpl, cache):
    """Iterate Timpl from n until hitting the target set; memoized. Returns hit target id."""
    path = []
    x = n
    while x not in cache:
        if x in targets:
            cache[x] = targets[x]
            break
        path.append(x)
        x = Timpl(x)
    res = cache[x]
    for y in path:
        cache[y] = res
    return res

def kernel_accounting(N3, Timpl, vertices, targets, label):
    """vertices: list of vertices (0..N3 for T, 1..N3 for U).
       targets: dict vertex -> component-tag for the known cycles.
       Returns (num_components, spurious, cut_edges)."""
    idx = {v: i for i, v in enumerate(vertices)}
    dsu = DSU(len(vertices))
    cut_edges = 0
    for m in vertices:
        t = Timpl(m)
        if t in idx:
            dsu.union(idx[m], idx[t])
        else:
            cut_edges += 1  # boundary-orphaned constraint: T(m) > N3, no constraint created
    comps = {}
    for v in vertices:
        comps.setdefault(dsu.find(idx[v]), []).append(v)
    ncomp = len(comps)
    # classify: which truncated components contain a known-cycle vertex
    cache = {}
    full_tags = {v: reaches_target(v, targets, Timpl, cache) for v in vertices}
    # every vertex must reach one of the known cycles (verified range)
    assert all(full_tags[v] is not None for v in vertices)
    # components of the FULL graph intersected with [range]: one per tag present
    tags_present = set(full_tags.values())
    # spurious components: truncated components containing no vertex of its cycle
    spurious = 0
    spurious_have_boundary = True
    for root, members in comps.items():
        member_tags = set(full_tags[v] for v in members)
        assert len(member_tags) == 1, "component mixes full-graph components (impossible)"
        if not any(v in targets for v in members):
            spurious += 1
            # each spurious component must contain >= 1 boundary-orphaned vertex
            if not any(Timpl(v) not in idx for v in members):
                spurious_have_boundary = False
    assert spurious_have_boundary, "spurious component without boundary exit (impossible)"
    identity = (ncomp == len(tags_present) + spurious)
    print(f"  {label} N={N3}: components={ncomp}, full-graph comps in range={len(tags_present)}, "
          f"spurious={spurious}, cut_edges={cut_edges}, identity ncomp={len(tags_present)}+spurious: "
          f"{'OK' if identity else 'FAIL'}")
    assert identity
    return ncomp, spurious, cut_edges

print("PART 3: truncated-kernel accounting for T (targets: {0} and cycle {1,2}):")
T_targets = {0: 'zero', 1: 'one', 2: 'one'}
results_T = {}
for N3 in (100, 1000, 5000, 20000, 100000):
    verts = list(range(0, N3 + 1))
    results_T[N3] = kernel_accounting(N3, T_arith, verts, T_targets, "T")

# ---- 3n-1 control map U on positive integers ----
def U(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n - 1) // 2

U_cycles = {1: 'c1', 5: 'c5', 7: 'c5', 10: 'c5',
            17: 'c17', 25: 'c17', 37: 'c17', 55: 'c17', 82: 'c17', 41: 'c17',
            61: 'c17', 91: 'c17', 136: 'c17', 68: 'c17', 34: 'c17'}
# sanity: verify the stated cycles really are cycles of U
def check_cycle(cyc):
    for x in cyc:
        assert U(x) in cyc
    x0 = cyc[0]; x = x0
    seen = set()
    while True:
        x = U(x)
        assert x not in seen
        seen.add(x)
        if x == x0:
            break
    assert seen == set(cyc)
check_cycle([1])
check_cycle([5, 7, 10])
check_cycle([17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34])
print("PART 3 control: U cycles {1},{5,7,10},{17,...,34} verified as cycles. Accounting for U:")
results_U = {}
for N3 in (100, 1000, 5000):
    verts = list(range(1, N3 + 1))
    results_U[N3] = kernel_accounting(N3, U, verts, U_cycles, "U")

# ================= PART 4: graph facts =================
# (a) every n <= N has preimage 2n
fact_a = all(T_arith(2 * n) == n for n in range(0, N + 1))
# (b) n has an odd preimage iff n = 2 (mod 3); the candidate is (2n-1)/3, odd, and unique among odds
fact_b = True
for n in range(0, N + 1):
    if n % 3 == 2:
        p = (2 * n - 1) // 3
        if (2 * n - 1) % 3 != 0 or p % 2 != 1 or T_arith(p) != n:
            fact_b = False; break
    else:
        # no odd p with (3p+1)/2 = n: p = (2n-1)/3 not an integer
        if (2 * n - 1) % 3 == 0:
            fact_b = False; break
assert fact_a and fact_b
# (c) all n in [1, N] reach 1 under T (memoized)
cache4 = {1: True, 2: True}
def reaches_one(n):
    path = []
    x = n
    while x not in cache4:
        assert x != 0
        path.append(x)
        x = T_arith(x)
    for y in path:
        cache4[y] = True
    return True
fact_c = all(reaches_one(n) for n in range(1, N + 1))
assert fact_c
print(f"PART 4 OK: (a) T(2n)=n for all n <= {N}; (b) odd preimage (2n-1)/3 exists iff n=2 mod 3, "
      f"is odd, maps to n; no odd preimage otherwise; (c) every n in [1,{N}] reaches 1 under T.")

print()
print("SUMMARY spurious(N) for T:", {k: v[1] for k, v in results_T.items()})
print("SUMMARY components(N) for T:", {k: v[0] for k, v in results_T.items()})
print("SUMMARY cut_edges(N) for T:", {k: v[2] for k, v in results_T.items()})
print("SUMMARY spurious(N) for U:", {k: v[1] for k, v in results_U.items()})
print("SUMMARY components(N) for U:", {k: v[0] for k, v in results_U.items()})
print("ALL CHECKS PASSED")