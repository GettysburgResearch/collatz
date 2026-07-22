"""T-9702 finite sanity checks (exact arithmetic, deterministic, stdlib only).
Checks the FINITE content of the claim on a window [0, N]:
  (a) component-class function is T-invariant: class(n) == class(T(n))  [F-fixedness of indicators]
  (b) a = sum_C c_C 1_C coefficientwise for a sample fixed nonnegative vector a
  (c) a vector carrying mass on >= 2 components admits a two-term split in K
      into NON-proportional parts (non-extremality witness)
  (d) 3n-1 control map U: same checks with its 3 known cycles, grand-orbit
      merges (5 ~ 7 ~ 10, 17 ~ 25) and separations (1 vs 5 vs 17).
NOTE: verifies finite instances only; it is NOT a proof.
"""
from fractions import Fraction

def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2   # Collatz shortcut on N_0
def U(n): return n // 2 if n % 2 == 0 else (3 * n - 1) // 2   # 3n-1 shortcut on N_>0 (control)

def classify(n, step, cycle_reps, cap=10**6):
    x = n
    for _ in range(cap):
        if x in cycle_reps:
            return cycle_reps[x]
        x = step(x)
    raise RuntimeError(f"cap exceeded at {n}")

T_cycles = {0: 0, 1: 1, 2: 1}                                  # {0} and {1,2}
U_cyc_lists = [[1], [5, 7, 10], [17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34]]
U_cycles = {x: min(c) for c in U_cyc_lists for x in c}

N = 5000

clsT = {n: classify(n, T, T_cycles) for n in range(N + 1)}
for n in range(N + 1):
    assert clsT[n] == classify(T(n), T, T_cycles)              # (a) class is T-invariant
assert sorted(set(clsT.values())) == [0, 1]
assert clsT[0] == 0 and clsT[1] == 1 and clsT[2] == 1

c = {0: Fraction(3, 7), 1: Fraction(2, 5)}
a = {n: c[clsT[n]] for n in range(N + 1)}
for n in range(N + 1):
    assert a[n] == c[classify(T(n), T, T_cycles)]              # (Fa)_n = a_n on window
    assert a[n] == c[clsT[n]]                                  # (b) a_n = c_{C(n)}

u = {n: (c[0] if clsT[n] == 0 else Fraction(0)) for n in range(N + 1)}
v = {n: a[n] - u[n] for n in range(N + 1)}
assert all(u[n] >= 0 and v[n] >= 0 and u[n] + v[n] == a[n] for n in range(N + 1))
assert all(u[n] == u[T(n)] if T(n) <= N else True for n in range(N + 1))
assert u[0] * a[1] != u[1] * a[0]                              # (c) split is non-proportional

clsU = {n: classify(n, U, U_cycles) for n in range(1, N + 1)}
for n in range(1, N + 1):
    assert clsU[n] == classify(U(n), U, U_cycles)
assert sorted(set(clsU.values())) == [1, 5, 17]                # (d) exactly 3 components observed
assert clsU[5] == clsU[7] == clsU[10]
assert clsU[17] == clsU[25]
assert clsU[1] != clsU[5] != clsU[17] and clsU[1] != clsU[17]
cu = {1: Fraction(1, 2), 5: Fraction(1, 3), 17: Fraction(1, 11)}
au = {n: cu[clsU[n]] for n in range(1, N + 1)}
for n in range(1, N + 1):
    assert au[n] == cu[classify(U(n), U, U_cycles)]
    assert au[n] == cu[clsU[n]]
ind5 = {n: (Fraction(1) if clsU[n] == 5 else Fraction(0)) for n in range(1, N + 1)}
for rep in (1, 17):
    assert all(ind5[n] == 0 for n in range(1, N + 1) if clsU[n] == rep)

print("all T-9702 finite sanity checks passed (N =", N, ")")