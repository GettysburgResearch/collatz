"""P2 (issue #4): the L1/L2 mass profile of S_K over the survivor range.

Everything the interchange analysis (EQ-INTERCHANGE.md) needs measured:

  (a) L1 block means  mean_{theta in (0, 81^{m+1}]} |S_K|/2^K  vs the
      T11 bound (2/pi + 1/81)^{m+1} and the lower envelope
      (2/pi - 1/81)^{m+1} -- both sides of the shifted-Riemann-sum
      variation bound;
  (b) L2 block means  mean cos^2-products vs (1/2 + 1/81)^{m+1};
  (c) the range masses  Sigma_{0<theta<=2^K} (|S_K|/2^K)^p, p = 1, 2,
      and the L2 exponent lambda_K = log2(L2 mass)/K;
  (d) |S_K(1)|/2^K (the core frequency) per K.

Exact product formula (T-0007): |S_K(theta)|/2^K =
prod_{t<K} |cos(pi * frac(theta c_t / 64^K))|,
c_t = 17*64^t*81^{-(t+1)} mod 64^K.  Floats suffice here (measurement,
not proof); phases are computed from exact integers before the single
float division.
"""
import math

TWO_OVER_PI = 2 / math.pi


def phases(K):
    Q = 64 ** K
    inv81 = pow(81, -1, Q)
    cs = []
    p = inv81
    for t in range(K):
        cs.append(17 * pow(64, t, Q) * p % Q)
        p = p * inv81 % Q
    return Q, cs


def profile(K):
    Q, cs = phases(K)
    B = 1 << K
    l1 = l2 = 0.0
    block_l1 = {}
    block_l2 = {}
    s1 = None
    vals_needed = max(B, 81 ** int(math.log(B, 81)) )
    for theta in range(1, B + 1):
        prod = 1.0
        prod2 = 1.0
        for c in cs:
            x = (theta * c) % Q
            ph = x / Q
            co = abs(math.cos(math.pi * ph))
            prod *= co
        prod2 = prod * prod
        l1 += prod
        l2 += prod2
        if theta == 1:
            s1 = prod
        for m in range(0, 4):
            if theta <= 81 ** (m + 1):
                block_l1[m] = block_l1.get(m, 0.0) + prod
                block_l2[m] = block_l2.get(m, 0.0) + prod2
    print(f"K={K:2d}: |S_K(1)|/2^K = {s1:.3e}")
    for m in sorted(block_l1):
        n = 81 ** (m + 1)
        if n > B:
            break
        bm1 = block_l1[m] / n
        bm2 = block_l2[m] / n
        up1 = (TWO_OVER_PI + 1 / 81) ** (m + 1)
        lo1 = (TWO_OVER_PI - 1 / 81) ** (m + 1)
        up2 = (0.5 + 1 / 81) ** (m + 1)
        print(f"   block m={m}: L1 mean {bm1:.5f} in "
              f"[{lo1:.5f}, {up1:.5f}]? {'Y' if lo1 <= bm1 <= up1 else 'N'}"
              f";  L2 mean {bm2:.5f} <= {up2:.5f}? "
              f"{'Y' if bm2 <= up2 else 'N'}")
    lam = math.log2(l2) / K
    print(f"   range (theta <= 2^{K}): L1 mass {l1:.4f}  "
          f"L2 mass {l2:.4e}  lambda_K = log2(L2)/K = {lam:+.4f}",
          flush=True)
    return l1, l2, lam, s1


if __name__ == "__main__":
    lams = []
    s1s = []
    for K in range(8, 17):
        l1, l2, lam, s1 = profile(K)
        lams.append((K, lam))
        s1s.append((K, s1))
    print("\nlambda_K sequence:", ", ".join(f"K={k}:{v:+.4f}"
                                            for k, v in lams))
    if len(s1s) > 1:
        rates = [ (s1s[i][1] / s1s[i-1][1]) for i in range(1, len(s1s))
                  if s1s[i-1][1] > 0 ]
        gm = math.exp(sum(math.log(r) for r in rates) / len(rates))
        print(f"|S_K(1)| geometric mean per-level rate over K=8..16: "
              f"{gm:.4f}")
    print("MEASUREMENT COMPLETE")
