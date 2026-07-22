# L-9708 verification: exact arithmetic, stdlib only, deterministic. (Numerics are sanity checks, not proof.)
from fractions import Fraction

def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2   # shortcut Collatz
def U(n): return n // 2 if n % 2 == 0 else (3 * n - 1) // 2   # 3n-1 control

# (a) Preimage structure of T (used in Lemma 1(a) and Remark 8): T^{-1}(0)={0};
#     for n>=1, T^{-1}(n) = {2n} plus (2n-1)/3 iff n = 2 (mod 3).
for n in range(0, 2000):
    pre = {m for m in range(0, 6 * n + 10) if T(m) == n}
    expect = {0} if n == 0 else ({2 * n} | ({(2 * n - 1) // 3} if n % 3 == 2 else set()))
    assert pre == expect, (n, pre, expect)

# (b) T(n) >= 1 for n >= 1 (Lemma 1(a)/(c)): component of 0 is {0}; T preserves N.
assert all(T(n) >= 1 for n in range(1, 200000))

# (c) Components = grand orbits (Lemma 0): membership decided by which cycle the forward orbit enters.
def cycle_of(f, n, cap=10**6):
    seen = set(); x = n
    for _ in range(cap):
        if x in seen:
            cyc = [x]; y = f(x)
            while y != x:
                cyc.append(y); y = f(y)
            return frozenset(cyc)
        seen.add(x); x = f(x)
    raise RuntimeError("iteration cap exceeded at n=%d" % n)

N = 5000
labT = {n: cycle_of(T, n) for n in range(0, N)}
assert set(labT.values()) == {frozenset({0}), frozenset({1, 2})}
labU = {n: cycle_of(U, n) for n in range(1, N)}
assert set(labU.values()) == {frozenset({1}), frozenset({5, 7, 10}),
                              frozenset({17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34})}

# (d) Component labels give F-fixed sequences (Lemma 2, easy direction, finite window):
for n in range(0, N):
    m = T(n); assert labT[n] == labT.get(m, cycle_of(T, m))
for n in range(1, N):
    m = U(n); assert labU[n] == labU.get(m, cycle_of(U, m))

# (e) Corollary 5/7 sanity: {0}-component has exactly one element <= N (the finite component);
#     C1 contains everything else here; summable weight w_n=(n+1)^{-2} keeps C1-mass below zeta(2).
assert sum(1 for n in range(0, N) if labT[n] == frozenset({0})) == 1
c1 = [n for n in range(0, N) if labT[n] == frozenset({1, 2})]
assert len(c1) == N - 1
mass = sum(Fraction(1, (n + 1) ** 2) for n in c1)
assert mass < Fraction(16449, 10000)  # zeta(2) = 1.6449...

# (f) 3n-1 control (Remark 9): U has >= 3 distinct components among 1..N — a faithful summable-
#     weight space gives dim >= 3 for U, while the unweighted l2(N) kernel is 0 for BOTH maps.
assert len(set(labU.values())) == 3

print("all checks passed:",
      "T-components<=%d:" % N, len(set(labT.values())),
      "| U-components<=%d:" % N, len(set(labU.values())),
      "| C1 mass (w=(n+1)^-2) =", float(mass))
