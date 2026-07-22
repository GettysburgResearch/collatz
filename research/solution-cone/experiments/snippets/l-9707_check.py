# L-9707 verification: exact arithmetic (Fractions), deterministic, stdlib only.
# Numerics are sanity checks of finitely many instances, never proof.
from fractions import Fraction as F
import math

# ---------- Parts (1)&(2) on S = perfect squares (beta = 1/2) ----------
# A(x) = floor(sqrt(x)) >= (1/2) x^{1/2} for x >= 4 (c=1/2, x0=4) and <= x^{1/2} for x >= 1 (C=1, x1=1).
# Thm 1 => f_S(r) >= (1/2)e^{-3}(1-r)^{-1/2} > (1/42)(1-r)^{-1/2} for r >= 3/4.
# Thm 2 => f_S(r) <= (Gamma(3/2)+2)(1-r)^{-1/2} < 3(1-r)^{-1/2} for all r in (0,1).
for k in [3, 4, 5, 6, 7]:
    q = 2 ** k
    r = F(q - 1, q)             # r = 1 - 1/2^k >= 7/8 >= 3/4
    eps = F(1, q)               # 1 - r
    N = 60 * q                  # truncation point
    fs_lo = sum((r ** (n * n) for n in range(1, math.isqrt(N) + 1)), F(0))
    rq = r ** q
    assert rq < F(1, 2)         # exact: (1-1/q)^q < 1/2
    tail = q * rq ** 60         # sum_{n>N} r^n <= r^N/(1-r) <= q*2^{-60}, exact majorant
    fs_hi = fs_lo + tail
    # compare squares to stay rational: ((1-r)^{-1/2})^2 = 1/eps
    assert fs_lo ** 2 * eps >= F(1, 42) ** 2, ("thm1 fail", k)
    assert fs_hi ** 2 * eps <= F(3, 1) ** 2, ("thm2 fail", k)

# ---------- Part (3): dyadic-block set, M_1=2, M_{k+1}=M_k^4 ----------
def inS(n):
    M = 2
    while M <= n:
        if M < n <= 2 * M:
            return True
        M = M ** 4
    return False

def A(x):
    return sum(1 for n in range(1, x + 1) if inS(n))

M1, M2, M3 = 2, 16, 65536
assert A(2 * M1) >= M1 and A(2 * M2) >= M2          # (ii): A(2M_k) >= M_k
assert A(M2) <= 2 * 2 and A(M3) <= 2 * 16           # (iii): A(M_{k+1}) <= 2 M_{k+1}^{1/4}
# (i) at k = 2: r_2 = 255/256, (1-r_2)^{-1/2} = 16
r = F(255, 256)
blocks12 = sum((r ** n for n in range(3, 5)), F(0)) + sum((r ** n for n in range(17, 33)), F(0))
r256 = r ** 256
assert r256 < F(1, 2)                                # exact, so r^{65536} = (r^256)^{256} < 2^{-256}
tail3 = 256 * r256 ** 256                            # exact majorant of sum_{n > M3} r^n
assert blocks12 >= F(7, 8) * 16                      # f_{S*}(r_2) >= (7/8)(1-r_2)^{-1/2}
assert blocks12 + tail3 <= 2 * 16                    # f_{S*}(r_2) <= 2 (1-r_2)^{-1/2}

# ---------- Part (4): partition identity for T, plus 3n-1 control ----------
def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2
def U(n): return n // 2 if n % 2 == 0 else (3 * n - 1) // 2

N4 = 2000
r = F(9, 10)
comp = {}
for n in range(0, N4 + 1):
    m, steps = n, 0
    while m not in (0, 1, 2):
        m = T(m); steps += 1
        assert steps < 10 ** 5
    comp[n] = 0 if m == 0 else 1
f0 = sum((r ** n for n in range(N4 + 1) if comp[n] == 0), F(0))
f1 = sum((r ** n for n in range(N4 + 1) if comp[n] == 1), F(0))
geo = sum((r ** n for n in range(N4 + 1)), F(0))
assert f0 == 1 and f0 + f1 == geo                    # truncated partition identity, T map

# 3n-1 control: the three known U-cycles' components partition [1, N4]
cycA, cycB = {1}, {5, 7, 10}
cycC = {17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34}
lab = {}
for n in range(1, N4 + 1):
    m, steps = n, 0
    while m not in cycA and m not in cycB and m not in cycC:
        m = U(m); steps += 1
        assert steps < 10 ** 5
    lab[n] = 'A' if m in cycA else ('B' if m in cycB else 'C')
s = {L: sum((r ** n for n in range(1, N4 + 1) if lab[n] == L), F(0)) for L in 'ABC'}
assert s['A'] + s['B'] + s['C'] == sum((r ** n for n in range(1, N4 + 1)), F(0))
assert all(s[L] > 0 for L in 'ABC')
print("ALL CHECKS PASSED")
# Output when run (Python 3, ~0.6 s): ALL CHECKS PASSED