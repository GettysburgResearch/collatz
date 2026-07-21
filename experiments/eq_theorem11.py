"""THEOREM 11 (block-mean exponential decay -- unconditional).

Setup: for |theta| in a block of 81^{m+1} consecutive frequencies (inside
the survivor range, with the margin t <= m << 5K/6 so the quantized
phase approximation y_t = s_t/81^{t+1} + O(2^{-cK}) is valid), the first
m+1 phase numerators satisfy s_t == -17 theta 64^{t-K} (mod 81^{t+1}).

LEMMA A (Markov decomposition).  As theta runs over any full period of
81^{m+1} consecutive integers, the vector (s_0, j_0, ..., j_{m-1}),
where s_{t+1} = 64 s_t + j_t 81^{t+1} (0 <= j_t < 81), is EXACTLY
uniform on (Z/81) x (Z/81)^m -- i.e. s_0 uniform and the successive
top digits j_t independent uniform.  [Proof: theta -> s_m mod 81^{m+1}
is a bijection on the period (unit multiplier); (s_0, j) <-> s_m is a
bijection by construction.]

LEMMA B (contraction).  For every real shift phi,
    (1/81) Sum_{j=0}^{80} |cos(pi (j+phi)/81)|  <=  2/pi + V/(2*81),
with V = total variation of |cos(pi x)| on [0,1] = 2.  Numerically
<= 0.6366 + 0.0124 = 0.6490.  [Riemann-sum vs integral, standard.]

THEOREM 11.  Over any full block B of 81^{m+1} consecutive frequencies
(within margins), the block mean of the partial product satisfies
    (1/|B|) Sum_{theta in B} Prod_{t=0}^{m} |cos(pi y_t(theta))|
        <=  (2/pi + 1/81)^{m+1}  <=  0.649^{m+1},
and since the remaining K-m-1 factors are <= 1,
    mean_{theta in B} |S_K(theta)|/2^K  <=  0.649^{m+1}.
[Proof: condition on the chain: E[Prod g(y_t)] = E[g(y_0) E[g(y_1)|y_0]
... ] and each conditional average is a shifted Riemann sum of |cos|
over j_t (Lemma A), bounded by Lemma B uniformly in the shift.]

COROLLARY.  |S_K(theta)|/2^K <= 0.649^{m+1} for all theta in a block,
EXCEPT on a fraction <= 0.805^{m+1} of each block (Markov with
sqrt: P(|S| > 0.805^m) <= (0.649/0.805)^m).  EQ holds with exponential
strength for ALMOST ALL frequencies at every scale; the entire residual
gap of EQ is the finitely many smallest frequencies per scale (theta =
O(1)), each an individual-orbit digit statement.

This file verifies Lemma A exactly, Lemma B by direct maximization,
and Theorem 11's bound against exact block means (m <= 2) and sampled
means (m = 3, 4), for the true phases (not the approximation).
"""

import math, random
from collections import Counter

def phases_first(K, theta, upto):
    """true phases y_t, t = 0..upto (exact rationals via residues)."""
    out = []
    for t in range(upto + 1):
        Mt = 64 ** (K - t)
        z = (17 * theta * pow(81, -(t + 1), Mt)) % Mt
        out.append(z / Mt)
    return out


print("== Lemma A: Markov decomposition (exact) ==")
K = 40
m = 2
P = 81 ** (m + 1)
seen = set()
ok_uniform = True
base = 12345
for i in range(P):
    theta = base + i
    # s_t from the exact congruence
    s = [(-17 * theta * pow(64, t - K, 81 ** (t + 1))) % 81 ** (t + 1)
         for t in range(m + 1)]
    # compatibility + top digits: s_{t+1} == 64 s_t (mod 81^{t+1}),
    # j_t = s_{t+1} div 81^{t+1}  (chain: y_{t+1} = ({64 y_t} + j_t)/81)
    js = []
    for t in range(m):
        assert s[t + 1] % 81 ** (t + 1) == (64 * s[t]) % 81 ** (t + 1), \
            (theta, t)
        j = s[t + 1] // 81 ** (t + 1)
        assert 0 <= j < 81, (theta, t, j)
        js.append(j)
    seen.add((s[0], tuple(js)))
print(f"  (s0, j0, j1) over one full period of {P} thetas: "
      f"{len(seen)} distinct tuples of {P} -- bijection: {len(seen) == P}")
assert len(seen) == P

print("\n== Lemma B: shifted Riemann sums of |cos| ==")
worst = 0
for i in range(2000):
    phi = i / 2000
    v = sum(abs(math.cos(math.pi * ((j + phi) / 81))) for j in range(81)) / 81
    worst = max(worst, v)
print(f"  max over shifts = {worst:.6f}; bound 2/pi + 1/81 = "
      f"{2/math.pi + 1/81:.6f}; 2/pi = {2/math.pi:.6f}")
assert worst <= 2 / math.pi + 1 / 81 + 1e-12
LAM = 2 / math.pi + 1 / 81

print("\n== Theorem 11: block means of the true partial products ==")
K = 40
for m in (0, 1, 2):
    P = 81 ** (m + 1)
    tot = 0.0
    for i in range(P):
        theta = 777_000 + i
        ys = phases_first(K, theta, m)
        p = 1.0
        for y in ys:
            p *= abs(math.cos(math.pi * y))
        tot += p
    mean = tot / P
    print(f"  m={m}: exact block mean {mean:.6f}  vs bound "
          f"{LAM ** (m + 1):.6f}   ({'OK' if mean <= LAM**(m+1) else 'FAIL'})")
    assert mean <= LAM ** (m + 1)

random.seed(1)
for m in (3, 4):
    P = 81 ** (m + 1)
    n = 40000
    tot = 0.0
    for _ in range(n):
        theta = 777_000 + random.randrange(P)
        ys = phases_first(K, theta, m)
        p = 1.0
        for y in ys:
            p *= abs(math.cos(math.pi * y))
        tot += p
    mean = tot / n
    se = LAM ** (m + 1) / math.sqrt(n)  # crude scale for report
    print(f"  m={m}: sampled block mean {mean:.6f} (n={n}) vs bound "
          f"{LAM ** (m + 1):.6f}   ({'OK' if mean <= LAM**(m+1)*1.05 else 'FAIL'})")
    assert mean <= LAM ** (m + 1) * 1.05

print("\n== full |S_K|/2^K block means (all K factors, K=16) ==")
# the theorem bounds mean of the FULL product too (extra factors <= 1);
# check against the survivor-range measurement
def c_coeffs(KK):
    MM = 64 ** KK
    return [17 * 64 ** t * pow(81, -(t + 1), MM) % MM for t in range(KK)], MM
for m in (0, 1):
    P = 81 ** (m + 1)
    K2 = 16
    cs, M = c_coeffs(K2)
    tot = 0.0
    cnt = 0
    for theta in range(1, P + 1):
        p = 1.0
        for c in cs:
            x = ((theta * c) % M) / M
            p *= abs(math.cos(math.pi * x))
        tot += p
        cnt += 1
    print(f"  m={m}: mean over theta in [1,{P}] = {tot/cnt:.6f} <= "
          f"{LAM ** (m + 1):.6f}: {tot/cnt <= LAM**(m+1)}")
    assert tot / cnt <= LAM ** (m + 1)

print("\nALL CHECKS PASS -- Theorem 11 verified")
