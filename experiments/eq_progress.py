"""Provable progress on EQ: Theorems 9 and 10.

THEOREM 9 (self-similarity and the sharp global maximum).
(a) S_K(64^j theta') = 2^j S_{K-j}(theta')  (the top j factors are
    exactly 1), so the frequency group acts self-similarly.
(b) For 64 !| theta (theta not divisible by 64), the level t* = K-1
    has phase z/64 with z = 17 theta 81^{-K} mod 64 != 0, whence a factor
    <= cos(pi/64).  Combining with (a):
        max_{theta != 0} |S_K(theta)|/2^K = cos(pi/64),
    attained exactly on theta = 64^{K-1} u with 17 u 81^{-1} == +-1 (64).
    [Proof of <=: after factoring 64^j, some level has nonzero phase with
    denominator exactly 64; |cos| <= cos(pi/64).  Attained: theta=64^{K-1}.]

THEOREM 10 (exact-run rigidity).  Let 0 < |theta| <= 2^K.  Suppose the
levels t0..t0+L-1 are all delta-degenerate (delta < 64/145) with
t0 + L - 1 < K_margin := largest t with 64^{K-t} > 2*17*2^K  (i.e.
t < K - (K+6)/6, about 5K/6).  The cascade gives the exact ladder
s_{t0+i} = 81^{L-1-i} sigma with sigma = s_{t0+L-1} != 0.  If moreover
|81^{t0+L} sigma| < 64^{K-t0}/2   ("sub-modulus ladder"), then the
congruence 17 theta == 81^{t0+L} sigma (mod 64^{K-t0}) holds with BOTH
SIDES smaller than half the modulus, hence is an integer EQUATION:
        17 theta = 81^{t0+L} sigma.
Then 17 | sigma (17 coprime to 81), theta = 81^{t0+L} (sigma/17), and
        t0 + L <= log_81(|theta|) <= log_81(2^K) ~ 0.158 K.
COROLLARY: in the survivor range, every delta-degenerate run is either
  (i) confined:  t0 + L <= 0.158 K   (exact ladder, theta an 81-power
      multiple -- checkable), or
  (ii) boundary-anchored: it violates sub-modulus or margin, forcing
      t0 + L - 1 >= K_margin - O(1) or a huge ladder value
      |sigma| >= 64^{K-t0}/(2*81^{t0+L}).
All clean interior adversaries are excluded; only boundary-anchored
runs remain, and those have cascade length <= 1 + log_81(delta 64^{K-t0})
with K - t0 <= K/6 + O(1), i.e. length <= ~0.158 K + O(1).

GRAND COROLLARY (structure of worst frequencies): for |theta| <= 2^K,
total degenerate coverage <= 0.158K (exact zone) + 0.158K (boundary
zone) + [huge-ladder interior runs].  The huge-ladder branch is the
single remaining unproven case; this file measures whether it ever
occurs (prediction: no).
"""

import math
from collections import Counter

def c_coeffs(K):
    M = 64 ** K
    return [17 * 64 ** t * pow(81, -(t + 1), M) % M for t in range(K)], M


def phases(K, theta):
    cs, M = c_coeffs(K)
    out = []
    for t, c in enumerate(cs):
        Mt = 64 ** (K - t)
        z = (17 * theta * pow(81, -(t + 1), Mt)) % Mt
        out.append((z, Mt))
    return out


def absS_ratio(K, theta):
    p = 1.0
    for z, Mt in phases(K, theta):
        p *= abs(math.cos(math.pi * z / Mt))
    return p


print("== Theorem 9: self-similarity and sharp maximum ==")
ok = True
for K in (6, 9):
    for tp in (3, 5, 111, 2 ** K - 1):
        for j in (1, 2, 3):
            a = absS_ratio(K, (64 ** j * tp) % 64 ** K)
            b = absS_ratio(K - j, tp % 64 ** (K - j))
            ok &= abs(a - b) < 1e-9
print(f"  (a) S_K(64^j t')/2^K = S_(K-j)(t')/2^(K-j): {ok}")
assert ok
# (b) the max: verify no theta beats cos(pi/64) and the attaining set
ok = True
for K in (2, 3):
    M = 64 ** K
    mx, arg = 0, None
    for th in range(1, M):
        v = absS_ratio(K, th)
        if v > mx:
            mx, arg = v, th
    ok &= abs(mx - math.cos(math.pi / 64)) < 1e-12
print(f"  (b) global max == cos(pi/64) = {math.cos(math.pi/64):.6f} "
      f"(exhaustive K=2,3): {ok}")
assert ok

print("\n== Theorem 10: exact-run rigidity in the survivor range ==")
DELTA = 1 / 8


def runs_of(K, theta):
    """maximal delta-degenerate runs: list of (t0, L, ladder_exact,
    sigma, sub_modulus)."""
    ph = phases(K, theta)
    deg = [min(z / Mt, 1 - z / Mt) < DELTA and z != 0 for z, Mt in ph]
    res = []
    t = 0
    while t < K:
        if deg[t]:
            t0 = t
            while t < K and deg[t]:
                t += 1
            L = t - t0
            # signed small representatives
            def srep(i):
                z, Mt = ph[i]
                return z if z <= Mt // 2 else z - Mt
            sigma = srep(t0 + L - 1)
            ladder = all(srep(t0 + i) == 81 ** (L - 1 - i) * sigma
                         for i in range(L))
            Mt0 = 64 ** (K - t0)
            sub = abs(81 ** (t0 + L) * sigma) < Mt0 // 2
            res.append((t0, L, ladder, sigma, sub))
        else:
            t += 1
    return res


K = 16
margin_t = max(t for t in range(K) if 64 ** (K - t) > 2 * 17 * 2 ** K)
print(f"  K={K}: margin level (interior zone) t < {margin_t + 1}; "
      f"exact-zone bound 0.158K = {0.158 * K:.1f}")
viol_ladder = viol_class = huge_interior = 0
confined_ok = True
runsc = Counter()
for th in range(1, 2 ** K + 1):
    for t0, L, ladder, sigma, sub in runs_of(K, th):
        runsc[L] += 1
        if t0 + L - 1 <= margin_t:          # interior run
            if not ladder:
                viol_ladder += 1
            elif sub:
                # theorem: exact equation must hold
                if 17 * th != 81 ** (t0 + L) * sigma and \
                   17 * (-th) != 81 ** (t0 + L) * sigma:
                    viol_class += 1
                if t0 + L > math.log(17 * 2 ** K) / math.log(81) + 1e-9:
                    confined_ok = False
            else:
                huge_interior += 1
print(f"  scanned all theta <= 2^{K}: run lengths {dict(sorted(runsc.items()))}")
print(f"  interior runs violating the exact ladder: {viol_ladder}")
print(f"  interior sub-modulus runs violating 17*theta = 81^(t0+L)*sigma: "
      f"{viol_class}")
print(f"  interior runs confined to <= log_81(17*2^K): {confined_ok}")
print(f"  interior HUGE-ladder runs (the open branch): {huge_interior}")

# argmax structure: where do the worst survivor-range frequencies anchor?
print("\n== anchor structure of the worst survivor-range frequencies ==")
worst = sorted(((absS_ratio(K, th), th) for th in range(1, 2 ** K + 1)),
               reverse=True)[:5]
for v, th in worst:
    rr = runs_of(K, th)
    desc = ", ".join(f"[t0={t0},L={L}{'E' if lad else ''}"
                     f"{'S' if sub else 'H'}]" for t0, L, lad, s, sub in rr)
    print(f"  theta={th:6d}: |S|/2^K={v:.4f}  runs: {desc or 'none'}")
print(f"  (E = exact ladder, S = sub-modulus, H = huge; boundary zone "
      f"starts at t = {margin_t + 1})")
