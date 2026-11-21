#!/usr/bin/env python3
"""
E3 (EMPIRICAL): numeric checks behind NOTES.md.
(a) the dyadic family 3^(4^t u) ~ 3^(4^t u - 1) (proved in Lean for all t; here: merge step and controls);
(b) the normal forms of the pair (3^(N-1), 3^N) and of 2^N - 1 after the structured phase;
(c) the exchange invariants e_m (for 3^m) and f_m (for 3^m - 1) and their coincidences;
(d) reach of bounded-depth certificates 3^i ~ 3^(i +- delta), delta <= 8, on random exponents;
(e) exponents 2-adically close to -1: no certificate of depth below the distance;
(f) how often two consecutive powers of three coalesce above 2^44 (a finite fact, not an identity);
(g) the first tail class without a certificate: the pair becomes a closure pair (m, 3m-1).
Map: T(n) = n/2 (even), (3n+1)/2 (odd).  Finite computation; evidence only.
"""
import random
from collections import Counter
random.seed(20261121)

def T(n): return n >> 1 if n & 1 == 0 else (3*n + 1) >> 1

def to_one(x, cap=10**6):
    n = o = 0
    while x != 1:
        o += x & 1; x = T(x); n += 1
        if n > cap: return None
    return n, o

def merge_time(cF, dF, cG, dG, i, Tmax):
    """first t <= Tmax with T^t(cF*3^i+dF) = T^t(cG*3^i+dG) identically on the class of i (symbolic)."""
    MOD = 1 << (Tmax + 8)
    p = pow(3, i, MOD)
    x = (cF*p + dF) % MOD; y = (cG*p + dG) % MOD
    ax, bx, ay, by = cF, dF, cG, dG
    for t in range(Tmax):
        pw = 1 << t
        if x & 1: x = (3*x + 1) >> 1; ax *= 3; bx = 3*bx + pw
        else: x >>= 1
        if y & 1: y = (3*y + 1) >> 1; ay *= 3; by = 3*by + pw
        else: y >>= 1
        if ax == ay and bx == by: return t + 1
    return None

print("(a) dyadic family: pair (3^(N-1), 3^N), N = 4^t u; predicted merge step 2t+5 for u = 7 (t odd) / 5 (t even) mod 8")
for t in range(1, 13):
    r = 7 if t % 2 else 5
    ok = 0
    for _ in range(40):
        u = r + 8*random.randrange(1 << 20)
        ok += (merge_time(1, 0, 3, 0, 4**t*u - 1, 2*t + 12) == 2*t + 5)
    other = 0
    for rr in (1, 3, 5, 7):
        if rr == r: continue
        for _ in range(10):
            u = rr + 8*random.randrange(1 << 20)
            other += (merge_time(1, 0, 3, 0, 4**t*u - 1, 2*t + 5) is not None)
    print(f"  t={t:<2} u={r} mod 8: {ok}/40 merge exactly at step {2*t+5};  other odd residues merged by then: {other}/30")
for t, u in ((1, 7), (1, 15), (2, 5), (2, 13), (3, 7)):
    N = 4**t*u; a = 3**N; b = 3**(N-1)
    for _ in range(2*t + 5): a = T(a); b = T(b)
    print(f"  exact integers: t={t} u={u} N={N}: T^{2*t+5}(3^N) == T^{2*t+5}(3^(N-1)): {a == b}")

print("(b) normal forms, N = 2^k u, q = (3^N - 1)/2^(k+2):")
allok = True
for k in range(1, 9):
    for u in (1, 3, 5, 7, 9):
        N = 2**k*u; X = 3**N; q = (X - 1) >> (k + 2)
        assert (X - 1) == q << (k + 2) and q & 1
        a, b, m = X, 3**(N-1), 2**N - 1
        for _ in range(N + k + 2): m = T(m)
        ok = (m == q)                                   # Mersenne: T^(N+k+2)(2^N - 1) = q
        if k % 2 == 0:
            s = (k + 2)//2
            for _ in range(2*s): a = T(a)
            for _ in range(2*s - 1): b = T(b)
            ok &= (a == 1 + 3**s*q) and (b == 1 + 2*3**(s-1)*q)
        else:
            s = (k + 1)//2
            for _ in range(2*s): a = T(a)
            for _ in range(2*s + 1): b = T(b)
            y = T(q)
            for _ in range(s - 1): y = 3*y - 1          # phi^(s-1)(T(q)), phi(y) = 3y - 1
            ok &= (a == 1 + 2*3**s*q) and (b == 1 + 3**s*q) and (1 + 3**s*q == 2*y)
        allok &= ok
print("  all 40 cases (k=1..8, u in 1,3,5,7,9) agree:", allok)

print("(c) exchange invariants: e_m = 2(o+m) - n for 3^m, f_m = 2o - n + 2m for 3^m - 1  ((n,o) = total steps, odd steps to reach 1)")
M = 600
e = {}; f = {}
for m in range(0, M + 1):
    n, o = to_one(3**m); e[m] = 2*(o + m) - n
    if m >= 1:
        n, o = to_one(3**m - 1); f[m] = 2*o - n + 2*m
print("  m  :", " ".join(f"{m:>3}" for m in range(0, 21)))
print("  e_m:", " ".join(f"{e[m]:>3}" for m in range(0, 21)))
print("  f_m:", "   " + " ".join(f"{f[m]:>3}" for m in range(1, 21)))
seen_e = {}; lower_e = 0; eq_f = 0; fold = 0
for m in range(1, M + 1):
    if e[m] in seen_e.values() or e[m] == e[0]: lower_e += 1
    seen_e[m] = e[m]
    eq_f += (e[m] == f[m]); 
for j in range(1, M//2):
    fold += (f[2*j - 1] == f[2*j])
print(f"  m in 1..{M}: e_m equals some e_m' with m' < m: {lower_e};  e_m = f_m: {eq_f};  f_(2j-1) = f_(2j) (Mersenne fold): {fold}/{M//2 - 1}")
cls = Counter(m % 4 for m in range(1, M + 1) if e[m] == f[m])
print("  residues m mod 4 with e_m = f_m:", sorted(cls.items()), " (m = 1 mod 4 is the proved class)")
for m, k, u in ((1, 3, 1), (1, 5, 3), (2, 11, 1), (4, 14, 1)):
    n, o = to_one(3**m); N = 2**k*u; x = 3**(m + N); q = (3**N - 1) >> (k + 2)
    for _ in range(n): x = T(x)
    print(f"  shadow m={m} N=2^{k}*{u}: T^{n}(3^(m+N)) == 1 + 3^(o+m) 2^(k+2-n) q : {x == 1 + 3**(o+m)*2**(k+2-n)*q}")

print("(d) reach of bounded-depth certificates on 2000 random 64-bit exponents i (delta = 1..8)")
S = 2000; TM = 64
down = []; anyd = []
for _ in range(S):
    i = random.randrange(1 << 63, 1 << 64)
    td = [merge_time(1, 0, 3**dl, 0, i - dl, TM) for dl in range(1, 9)]
    tu = [merge_time(1, 0, 3**dl, 0, i, TM) for dl in range(1, 9)]
    d = min([t for t in td if t is not None], default=None)
    a = min([t for t in td + tu if t is not None], default=None)
    down.append(d); anyd.append(a)
for Tc in (8, 12, 16, 24, 32, 48, 64):
    cd = sum(1 for t in down if t is not None and t <= Tc)/S
    ca = sum(1 for t in anyd if t is not None and t <= Tc)/S
    print(f"  depth <= {Tc:<2}: 3^i ~ 3^(i-delta) for some delta: {cd:.3f}   some delta of either sign: {ca:.3f}")

print("(e) exponents i = 2^K u - 1 (K = 40, u odd random): earliest certificate, as depth - K")
K = 40; hist_up = Counter(); hist_dn = Counter()
for _ in range(300):
    u = 2*random.randrange(1 << 30) + 1
    i = 2**K*u - 1
    tu = merge_time(1, 0, 3, 0, i, K + 24)
    td = min([t for t in (merge_time(1, 0, 3**dl, 0, i - dl, K + 24) for dl in range(1, 9)) if t is not None], default=None)
    hist_up[None if tu is None else tu - K] += 1
    hist_dn[None if td is None else td - K] += 1
print("  pair (3^i, 3^(i+1)):        ", sorted(hist_up.items(), key=lambda kv: (kv[0] is None, kv[0])))
print("  pairs (3^(i-delta), 3^i):   ", sorted(hist_dn.items(), key=lambda kv: (kv[0] is None, kv[0])))

print("(f) coalescence above 2^44 is common and is NOT an identity in e: pairs (3^e, 3^(e+1)), e = 30..399")
THR = 1 << 44
def high_orbit(x):
    s = set()
    while x >= THR:
        s.add(x); x = T(x)
    return s
prev = high_orbit(3**30); cnt = 0
for ee in range(30, 400):
    cur = high_orbit(3**(ee + 1))
    cnt += bool(prev & cur)
    prev = cur
print(f"  {cnt}/370 consecutive pairs share an orbit value >= 2^44")

print("(g) first tail class without a certificate (Lean: pow_three_pair_closure_form): N = 4u, q = (3^N-1)/16, w = 3q, 8x = 3w+1")
print("    u = 3 mod 16 gives x odd (closure pair (m, 3m-1), m = 3x+1); u = 11 mod 16 gives x even")
for N in (12, 76, 140, 204, 44, 108):
    q = (3**N - 1) >> 4; w = 3*q; x = (3*w + 1) >> 3
    a, b = 3**N, 3**(N-1)
    for _ in range(7): a = T(a); b = T(b)
    print(f"  N={N:<3} u={N//4:<2} (u mod 16 = {N//4 % 16:>2}): w mod 16 = {w % 16:>2}, 3w+1 == 8x: {3*w + 1 == 8*x}, x odd: {x % 2 == 1}, "
          f"T^7(3^N) == x: {a == x}, T^7(3^(N-1)) == 9x+2 == 3(3x+1)-1: {b == 9*x + 2}")
