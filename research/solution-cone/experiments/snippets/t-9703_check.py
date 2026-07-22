# Exact-arithmetic finite checks for T-9703 (deterministic, stdlib only).
def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2
def U(n): return n // 2 if n % 2 == 0 else (3 * n - 1) // 2  # 3n-1 control, n >= 1

def cycles_pos(cycles):
    d = {}
    for cid, cyc in enumerate(cycles):
        p = len(cyc)
        for i, z in enumerate(cyc):
            d[z] = (cid, i, p)
    return d

def locate(f, m, cpos, maxsteps=100000):
    # returns (component id, depth d(m) mod p, p) where d(m) = (k - i) mod p
    # for any k with f^k(m) = z_i on the component's cycle.
    x, k = m, 0
    while x not in cpos:
        x = f(x); k += 1
        if k > maxsteps:
            return None
    cid, i, p = cpos[x]
    return cid, (k - i) % p, p

N = 20000

# --- Collatz T: cycles {0} (p=1) and {1,2} (p=2) ---
assert T(0) == 0 and T(1) == 2 and T(2) == 1
cposT = cycles_pos([[0], [1, 2]])
for m in range(0, N + 1):
    cid, d, p = locate(T, m, cposT)
    cid2, dT, p2 = locate(T, T(m), cposT)
    assert cid2 == cid and p2 == p
    assert (dT - (d - 1)) % p == 0          # cocycle d(T(m)) = d(m) - 1 (mod p)
# hence a_m = lam**(-d(m)) is an exact eigenvector on each truncated component
# for every lam with lam**p = 1; for {1,2} (p=2) this realizes lam = -1.

# uniqueness of 1- and 2-cycles of T up to N (supports Corollary 5a):
for n in range(0, N + 1):
    if T(n) == n: assert n == 0
    if T(T(n)) == n: assert n in (0, 1, 2)

# --- 3n-1 control U: cycles {1} (p=1), {5,7,10} (p=3), 11-cycle at 17 ---
c11 = [17]
x = U(17)
while x != 17:
    c11.append(x); x = U(x)
assert c11 == [17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34] and len(c11) == 11
assert U(5) == 7 and U(7) == 10 and U(10) == 5 and U(1) == 1
cposU = cycles_pos([[1], [5, 7, 10], c11])
members3 = []
cnt11 = 0
for m in range(1, N + 1):
    cid, d, p = locate(U, m, cposU)
    cid2, dU, p2 = locate(U, U(m), cposU)
    assert cid2 == cid and p2 == p          # U preserves components
    assert (dU - (d - 1)) % p == 0          # cocycle, exact, in all three components
    if cid == 1: members3.append((m, d))
    if cid == 2: cnt11 += 1
assert (5, 0) in members3 and len(members3) > 50 and cnt11 > 50
# The cocycle check above IS the eigenvector identity for every lam with
# lam^p = 1 (p = 3 resp. 11), verified as an integer congruence: e.g. it
# certifies a primitive 11th root of unity on the 17-component truncation.

# Exact eigenvector check for lam = omega (primitive cube root of unity) on the
# {5,7,10} component, computed in Z[omega] with omega^2 = -1 - omega (no floats):
def wmul(u, v):  # (a + b*omega)(c + d*omega)
    a, b = u; c, d = v
    return (a * c - b * d, a * d + b * c - b * d)
wpow = [(1, 0), (0, 1), (-1, -1)]                 # omega^0, omega^1, omega^2
assert wmul(wpow[1], wpow[1]) == wpow[2] and wmul(wpow[1], wpow[2]) == wpow[0]
aval = {m: wpow[(-d) % 3] for m, d in members3}   # a_m = omega^{-d(m)}
omega = wpow[1]
checked = 0
for m, d in members3:
    um = U(m)
    if um in aval:
        assert aval[um] == wmul(omega, aval[m])   # a_{U(m)} = omega * a_m, exactly
        checked += 1
assert checked > 50

# lam = i does NOT admit an eigenvector on the {5,7,10} component: around the
# 3-cycle any eigenvector satisfies a_5 = i^3 a_5, and i^3 != 1 in Z[i]:
def imul(u, v):
    a, b = u; c, d = v
    return (a * c - b * d, a * d + b * c)
ii = (0, 1)
i3 = imul(imul(ii, ii), ii)
assert i3 == (0, -1) and i3 != (1, 0)
# so (1 - i^3) a_5 = 0 forces a_5 = 0, hence a_7 = a_10 = 0, and the pullback
# identity a_m = i^{-k} a_{U^k(m)} kills every certified member of the
# component: the only solution of the eigen-equation for lam = i there is 0.

print("T-9703 finite checks: all passed;",
      f"|C(5) cap [1,{N}]| = {len(members3)}, |C(17) cap [1,{N}]| = {cnt11}")
# Observed output:
# T-9703 finite checks: all passed; |C(5) cap [1,20000]| = 6451, |C(17) cap [1,20000]| = 7047