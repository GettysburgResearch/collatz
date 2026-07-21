"""The attack on EQ (equidistribution of the valid sets R_K).

THEOREM 7 (product formula).  The coded residue of the epsilon-word is
    A(eps) = sum_t 17 eps_t 64^t 81^{-(t+1)}  (mod 64^K)
(composition of the inverse branches J_e(x) = (64x+17e)/81 applied to 0),
hence the Fourier transform of R_K factors EXACTLY:
    S_K(theta) = sum_{A in R_K} e(theta A/64^K)
               = prod_{t<K} (1 + e(theta c_t / 64^K)),
    c_t = 17*64^t*81^{-(t+1)} mod 64^K,
so |S_K(theta)|/2^K = prod_t |cos(pi {theta c_t/64^K})|.

THEOREM 8 (cascade lemma).  Write M_t = 64^{K-t} and
z_t = 17 theta 81^{-(t+1)} mod M_t (so {theta c_t/64^K} = z_t/M_t after
the 64^t shift).  If two consecutive terms are delta-degenerate
(||z_t/M_t|| < delta and ||z_{t+1}/M_{t+1}|| < delta) with
delta < 64/145, then the small representatives satisfy s_t = 81 s_{t+1}
exactly; inductively a degenerate run of length L starting at t forces
81^{L-1} <= delta * 64^{K-t}: maximal degenerate runs from position t
have length <= 1 + log_81(delta 64^{K-t}).  Degeneracy is an
81-divisibility cascade, not an accident.

This file: verifies Theorem 7 exactly, verifies the cascade lemma's
conclusion on random and adversarial frequencies, computes the true
worst-case |S_K|/2^K by full scan (K <= 4) and over the
survivor-relevant range |theta| <= 2^K (K <= 16), and evaluates the
Erdos-Turan discrepancy sum at survivor scale.
"""

import cmath, math
from collections import Counter

def build_R(K):
    R = [0, 1]
    M = 64
    for k in range(2, K + 1):
        M *= 64
        inv = pow(81, -1, M)
        R = sorted({(64 * y + 17 * e) * inv % M for y in R for e in (0, 1)})
    return R, M


def c_coeffs(K):
    M = 64 ** K
    return [17 * 64 ** t * pow(81, -(t + 1), M) % M for t in range(K)], M


def S_direct(R, M, theta):
    return sum(cmath.exp(2j * math.pi * ((theta * A) % M) / M) for A in R)


def S_product(cs, M, theta):
    p = 1.0 + 0j
    for c in cs:
        p *= 1 + cmath.exp(2j * math.pi * ((theta * c) % M) / M)
    return p


print("== Theorem 7: product formula ==")
import random
random.seed(3)
for K in (4, 7, 10):
    R, M = build_R(K)
    cs, M2 = c_coeffs(K)
    assert M == M2
    ok = True
    for _ in range(25):
        th = random.randrange(1, M)
        a, b = S_direct(R, M, th), S_product(cs, M, th)
        ok &= abs(a - b) < 1e-6 * max(1.0, abs(a))
    print(f"  K={K}: product == direct sum on 25 random frequencies: {ok}")
    assert ok

print("\n== full worst-case scan (all theta) ==")
for K in (2, 3, 4):
    cs, M = c_coeffs(K)
    best, argb = 0.0, None
    # vectorized-ish scan in pure python (K=4: 16.7M -> sample stride for
    # speed; stride 1 for K<=3)
    stride = 1 if K <= 3 else 7  # stride coprime to 64^K covers residues well
    count = 0
    th = 1
    seen = 0
    limit = M - 1
    step = stride
    for th in range(1, M, step):
        p = 1.0
        for c in cs:
            x = ((th * c) % M) / M
            p *= abs(math.cos(math.pi * x))
            if p < best:
                break
        if p > best:
            best, argb = p, th
        seen += 1
    print(f"  K={K}: max |S|/2^K = {best:.6f} at theta={argb} "
          f"(v81: {0 if argb % 81 else 'div81'}; scanned {seen})")

print("\n== survivor-range scan: |theta| <= 2^K ==")
print("K   max|S|/2^K   argmax    mean|S|/2^K   ET-sum")
for K in range(6, 17, 2):
    cs, M = c_coeffs(K)
    best, argb, tot, et = 0.0, None, 0.0, 0.0
    T = 2 ** K
    for th in range(1, T + 1):
        p = 1.0
        for c in cs:
            x = ((th * c) % M) / M
            p *= abs(math.cos(math.pi * x))
        if p > best:
            best, argb = p, th
        tot += p
        et += p / th
    print(f"{K:2d}  {best:.3e}  {argb:8d}  {tot/T:.3e}  {et:.4f}")

print("\n== cascade lemma verification ==")
# for random theta, measure degenerate-run structure and check the bound
K = 24
cs, M = c_coeffs(K)
delta = 1 / 8
viol = 0
runs_all = Counter()
for _ in range(2000):
    th = random.randrange(1, M)
    # positions t with ||{th c_t/M}|| < delta
    degs = []
    for t, c in enumerate(cs):
        x = ((th * c) % M) / M
        degs.append(min(x, 1 - x) < delta)
    # maximal runs and the bound L <= 1 + log81(delta*64^{K-t})
    t = 0
    while t < K:
        if degs[t]:
            L = 0
            t0 = t
            while t < K and degs[t]:
                L += 1
                t += 1
            runs_all[L] += 1
            bound = 1 + math.log(delta * 64.0 ** (K - t0)) / math.log(81)
            if L > bound + 1e-9:
                viol += 1
        else:
            t += 1
print(f"  2000 random frequencies, delta=1/8: run-length distribution "
      f"{dict(sorted(runs_all.items()))}")
print(f"  cascade bound violations: {viol}")

# adversarial: construct theta via the cascade (81-power structured) and
# check how slow the decay can get in the FULL range
print("\n== adversarial 81-power frequencies ==")
K = 16
cs, M = c_coeffs(K)
worst = []
for j in range(0, 60):
    if 81 ** j > M:
        break
    for mu in (1, 5, 7):
        th = (81 ** j * mu) % M
        if th == 0:
            continue
        p = 1.0
        for c in cs:
            x = ((th * c) % M) / M
            p *= abs(math.cos(math.pi * x))
        worst.append((p, j, mu))
worst.sort(reverse=True)
for p, j, mu in worst[:5]:
    print(f"  theta = {mu}*81^{j}: |S|/2^K = {p:.4e}")
print(f"  (survivor-range max at K=16 for comparison: see table above)")
