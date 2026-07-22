#!/usr/bin/env python3
# L-9706 verification: exact coefficientwise check of the single-valued
# functional equation for F-fixed sequences of the shortcut Collatz map,
# plus 3n-1 control and the 6-term original-map (3n+1) equation.
# Exact arithmetic in Z[omega], omega = exp(2*pi*i/3), omega^2 = -1 - omega.
# Deterministic (seeded). Standard library only.
import random

M = 1500   # a_0..a_M are known exactly
D = 3000   # coefficients of z^N checked for N = 0..D (fully determined by a_0..a_M)

def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2
def U(n): return n // 2 if n % 2 == 0 else ((3 * n - 1) // 2 if n > 0 else 0)

WP = [(1, 0), (0, 1), (-1, -1)]   # omega^0, omega^1, omega^2 as x + y*omega

def check_eq(a, pref, name):
    """pref=+1: shortcut Collatz equation  f(z^3) = f(z^6) + (1/(3z)) B(z),
           B(z) = sum_{j=0..2} omega^{ j} f(omega^j z^2)  [exponents == 4 mod 6]
       pref=-1: 3n-1 control equation      f(z^3) = f(z^6) + (z/3) C(z),
           C(z) = sum_{j=0..2} omega^{-j} f(omega^j z^2)  [exponents == 2 mod 6]
       Exact check of z^N coefficients, N = 0..D. Returns list of failing N."""
    s = -1 if pref == 1 else 1          # exponent shift of the bracket term
    L = [0] * (D + 1)
    R = [0] * (D + 1)
    for m in range(M + 1):
        if 3 * m <= D: L[3 * m] += a[m]
        if 6 * m <= D: R[6 * m] += a[m]
    for n in range(M + 1):
        e = 2 * n
        x, y = 0, 0                     # bracket coeff at z^e, summed honestly
        for j in range(3):
            wx, wy = WP[(j * (n + pref)) % 3]   # omega^{pref*j} * omega^{j*n}
            x += a[n] * wx; y += a[n] * wy
        if x == 0 and y == 0: continue
        assert y == 0 and x % 3 == 0, ("bracket coeff not 3*(real integer)", e, x, y)
        assert e % 6 == (4 if pref == 1 else 2), ("unexpected surviving exponent", e)
        Ne = e + s
        assert Ne >= 0, "negative exponent survived"
        if Ne <= D: R[Ne] += x // 3
    bad = [N for N in range(D + 1) if L[N] != R[N]]
    print(f"{name}: {'PASS' if not bad else 'FAIL at N=' + str(bad[:5])}")
    return bad

def check_eq6(a, name):
    """Unshortened 3n+1 map equation (star-star):
       f(z^3) = f(z^6) + (1/(6z)) sum_{j=0..5} mu^{2j} f(mu^j z), mu = exp(pi*i/3).
       mu^{2j} * mu^{jn} = (-1)^{jn} * omega^{j(2n+1)}. Bracket coeff at z^n needs
       a_n, so only N <= M-1 are fully determined; we check N = 0..M-1."""
    D6 = M - 1
    L = [0] * (D6 + 1); R = [0] * (D6 + 1)
    for m in range(M + 1):
        if 3 * m <= D6: L[3 * m] += a[m]
        if 6 * m <= D6: R[6 * m] += a[m]
    for n in range(M + 1):
        x, y = 0, 0
        for j in range(6):
            sgn = -1 if (j * n) % 2 else 1
            wx, wy = WP[(j * (2 * n + 1)) % 3]
            x += sgn * a[n] * wx; y += sgn * a[n] * wy
        if x == 0 and y == 0: continue
        assert y == 0 and x % 6 == 0, ("bracket coeff not 6*(real integer)", n, x, y)
        assert n % 6 == 4, ("unexpected surviving exponent", n)
        if n - 1 <= D6: R[n - 1] += x // 6
    bad = [N for N in range(D6 + 1) if L[N] != R[N]]
    print(f"{name}: {'PASS' if not bad else 'FAIL at N=' + str(bad[:5])}")
    return bad

def orbit_label_T(n):
    if n == 0: return 'zero'
    for _ in range(10**6):
        if n in (1, 2): return 'one'
        n = T(n)
    raise RuntimeError("T-orbit did not resolve")

CYC_U = {1: 'c1'}
for c in (5, 7, 10): CYC_U[c] = 'c5'
for c in (17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34): CYC_U[c] = 'c17'
def orbit_label_U(n):
    if n == 0: return 'zero'
    for _ in range(10**6):
        if n in CYC_U: return CYC_U[n]
        n = U(n)
    raise RuntimeError("U-orbit did not resolve")

def uf_projection(step, seed):
    """Random sequence exactly projected onto {Fa=a} restricted to [0,M]:
    union-find over {0..M} with an edge n ~ step(n) whenever step(n) <= M,
    then one independent random integer per class. Every constraint the
    degree-D check uses has both endpoints <= M, hence lies in one class."""
    parent = list(range(M + 1))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for n in range(M + 1):
        t = step(n)
        if t <= M: parent[find(n)] = find(t)
    rng = random.Random(seed)
    val, a = {}, []
    for n in range(M + 1):
        r = find(n)
        if r not in val: val[r] = rng.randrange(-9, 10)
        a.append(val[r])
    return a

fails = 0
# --- shortcut Collatz map T (main claim, eq. (star)) ---
aC1 = [1 if orbit_label_T(n) == 'one' else 0 for n in range(M + 1)]  # indicator of C1 (boundary-aware truncation)
a0  = [1 if n == 0 else 0 for n in range(M + 1)]                     # indicator of component {0}
aRP = uf_projection(T, 97061)                                        # random Fa=a-projected sequence
fails += len(check_eq(aC1, +1, "T: indicator of component of 1, deg 3000"))
fails += len(check_eq(a0,  +1, "T: indicator of {0}, deg 3000"))
fails += len(check_eq(aRP, +1, "T: random union-find projected sequence, deg 3000"))
# --- unshortened 3n+1 map: 6-term equation (star-star), same solution set ---
fails += len(check_eq6(aRP, "C (3n+1 unshortened): 6-term eq on same random projected seq"))
fails += len(check_eq6(aC1, "C (3n+1 unshortened): 6-term eq on indicator of C1"))
# --- negative control: corrupted sequence must FAIL ---
aBad = list(aRP); aBad[7] += 1
neg = check_eq(aBad, +1, "T: corrupted sequence (FAIL expected)")
assert neg == [21, 42], "negative control did not fail exactly at the predicted coefficients"
# --- 3n-1 control map U (eq. (star_U)) ---
aU5  = [1 if orbit_label_U(n) == 'c5'  else 0 for n in range(M + 1)]
aU17 = [1 if orbit_label_U(n) == 'c17' else 0 for n in range(M + 1)]
aURP = uf_projection(U, 97062)
fails += len(check_eq(aU5,  -1, "U (3n-1): indicator of component of 5, deg 3000"))
fails += len(check_eq(aU17, -1, "U (3n-1): indicator of component of 17, deg 3000"))
fails += len(check_eq(aURP, -1, "U (3n-1): random union-find projected sequence, deg 3000"))
print("ALL CHECKS PASSED" if fails == 0 else "FAILURES PRESENT")