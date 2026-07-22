# L-9705 verification: stdlib only, deterministic, exact arithmetic where possible.
from fractions import Fraction

def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2          # shortcut Collatz
def U(n): return n // 2 if n % 2 == 0 else (3 * n - 1) // 2          # 3n-1 control (n >= 1)

# 1. Preimage formula (Lemma 1)
M = 200000
pre = {}
for m in range(M):
    pre.setdefault(T(m), []).append(m)
for n in range((M - 1) // 2):
    expected = [2 * n] + ([(2 * n - 1) // 3] if n % 3 == 2 else [])
    assert sorted(pre.get(n, [])) == sorted(expected), n

# 2. kappa(s) = (3/5)^s + (3/2)^s, unique argmax n = 2
def d(n, s):
    return ((n + 1) / (2 * n + 1)) ** s + ((1.5) ** s if n % 3 == 2 else 0.0)
N = 100000
for s in (1.1, 1.5, 2.0, 3.0):
    kappa = (3 / 5) ** s + (3 / 2) ** s
    assert abs(d(2, s) - kappa) < 1e-12
    assert all(d(n, s) < kappa for n in range(N) if n != 2), s
    print(f"s={s}: kappa={kappa:.12f}  ||F||={kappa**0.5:.12f}  (max at n=2 over n<{N})")
# exact rational checks
for s in (2, 3):
    w = lambda n: Fraction(1, (n + 1) ** s)
    assert (w(4) + w(1)) / w(2) == Fraction(3, 5) ** s + Fraction(3, 2) ** s   # T^{-1}(2)={4,1}
    assert w(0) / w(0) == 1                                                    # T^{-1}(0)={0}

# 3. F*F diagonality, exact (s=2), truncation n,k <= K with all preimage rows included
s, K = 2, 60
rows = 2 * K + 2
w = [Fraction(1, (n + 1) ** s) for n in range(rows)]
Fmat = [[1 if T(m) == n else 0 for n in range(K + 1)] for m in range(rows)]
for n in range(K + 1):
    for k in range(K + 1):
        g = sum(Fmat[m][n] * Fmat[m][k] * w[m] for m in range(rows))  # <F e_n, F e_k>
        if n != k:
            assert g == 0
        else:
            dn = Fraction(n + 1, 2 * n + 1) ** s + (Fraction(3, 2) ** s if n % 3 == 2 else 0)
            assert g == dn * w[n]
print(f"F*F diagonal verified exactly (s=2) for n,k <= {K}")

# 4. 3n-1 control: known cycles, preimage formula, and sup NOT attained
for cyc in ([1], [5, 7, 10], [17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34]):
    for i, x in enumerate(cyc):
        assert U(x) == cyc[(i + 1) % len(cyc)], cyc
preU = {}
for m in range(1, M):
    preU.setdefault(U(m), []).append(m)
for n in range(1, (M - 1) // 2):
    expected = sorted(set([2 * n] + ([(2 * n + 1) // 3] if n % 3 == 1 else [])))
    assert sorted(preU.get(n, [])) == expected, n
for s in (1.1, 2.0):
    dU = lambda n: ((n + 1) / (2 * n + 1)) ** s + \
                   ((3 * (n + 1) / (2 * n + 4)) ** s if n % 3 == 1 else 0.0)
    sup_seen = max(dU(n) for n in range(1, N))
    limit = 0.5 ** s + 1.5 ** s
    assert sup_seen < limit
    print(f"U control s={s}: max d^U (n<{N}) = {sup_seen:.9f} < limit {limit:.9f} (not attained)")
print("ALL CHECKS PASSED")