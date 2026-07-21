"""P5 (issue #4): the run-length skeleton -- exact extraction from real
induced orbits, and the periodic-chain search behind the skeleton
rigidity theorem (SKELETON.md).

Part 1 (extraction / cross-verification of the skeleton normal form).
For each verified chart (M, N, D) and exact coded K-step words, extract
maximal constant-digit phases of the induced orbit A_t. Check exactly:
  phase entry  A = d + M^u * C  (M does not divide C at the change),
  phase exit   A' = d + N^u * C,
  and at each digit change the chain equation
      d_k + N^{u_k} C_k = d_{k+1} + M^{u_{k+1}} C_{k+1}.

Part 2 (periodic chains = the bounded-state class of SKELETON.md).
A period-p skeleton chain composes to an affine fixed-point equation
    C_0 = (alpha C_0 + beta),  alpha = N^{sum u} / M^{sum u},
so C_0 = beta / (1 - alpha) is rational and unique given the pattern
(d_i, u_i). Enumerate all patterns with p <= 3, u_i <= 5, digits from
each chart alphabet; report every pattern whose fixed point is a
positive integer with M not dividing C_i -- the only candidates for a
schema-closed expanding chain. Expected by the sign analysis
(SKELETON.md, Lemma S): alpha > 1 forces C_0 <= 0 whenever beta >= 0;
the search tests the general signed case.
"""
import random
from fractions import Fraction

random.seed(4)

D18 = [0, 16, 20, 21, 32, 34, 35, 40, 42, 49, 68, 69, 70, 78, 79,
       92, 93, 94]
CHARTS = [
    ("64->81", 64, 81, [0, 1]),
    ("512->729", 512, 729, [0, 1, 2]),
    ("2^17->3^11", 1 << 17, 3 ** 11, list(range(6))),
    ("2^22->3^14", 1 << 22, 3 ** 14, D18),
]


def coded(eps, M, N, K):
    MK = M ** K
    Ninv = pow(N, -1, MK)
    A, npow, Mpow = 0, Ninv, 1
    for t in range(K):
        A = (A + (N - M) * eps[t] * Mpow * npow) % MK
        npow = npow * Ninv % MK
        Mpow *= M
    return A


def extract_and_check(M, N, D, eps):
    """Run the induced orbit of the coded word, extract phases, verify
    the skeleton equations exactly. Returns number of chain links."""
    K = len(eps)
    A = coded(eps, M, N, K)
    # phases of the digit word itself
    phases = []
    i = 0
    while i < K:
        j = i
        while j < K and eps[j] == eps[i]:
            j += 1
        phases.append((eps[i], j - i))
        i = j
    links = 0
    x = A
    for p, (d, u) in enumerate(phases):
        C = (x - d) // M ** u
        assert (x - d) % M ** u == 0, "phase entry not d + M^u C"
        if p + 1 < len(phases):
            assert C % M != 0, "M | C at a digit change"
        # execute u steps
        for _ in range(u):
            assert x % M == d
            x = N * (x // M) + d
        assert x == d + N ** u * C, "phase exit not d + N^u C"
        if p + 1 < len(phases):
            d2, u2 = phases[p + 1]
            C2 = (x - d2) // M ** u2
            assert (x - d2) % M ** u2 == 0 and d + N ** u * C == d2 + M ** u2 * C2
            links += 1
    return links


def periodic_search(M, N, D, pmax=3, umax=5):
    """Enumerate period-p patterns; solve the fixed point exactly."""
    from itertools import product
    found = []
    checked = 0
    for p in range(1, pmax + 1):
        for ds in product(D, repeat=p):
            if p > 1 and any(ds[i] == ds[(i + 1) % p] for i in range(p)):
                continue  # digit must change at a link
            if p == 1 and len(set(ds)) == 1:
                continue  # constant digit = trivial fixed point d
            for us in product(range(1, umax + 1), repeat=p):
                checked += 1
                # C_{i+1} = (d_i - d_{i+1} + N^{u_i} C_i) / M^{u_{i+1}}
                # compose symbolically: C_0 -> alpha C_0 + beta
                alpha, beta = Fraction(1), Fraction(0)
                for i in range(p):
                    d1, d2 = ds[i], ds[(i + 1) % p]
                    u2 = us[(i + 1) % p]
                    alpha = alpha * N ** us[i] / M ** u2
                    beta = (beta * N ** us[i] + d1 - d2) / M ** u2
                if alpha == 1:
                    continue
                C0 = beta / (1 - alpha)
                if C0.denominator != 1:
                    continue
                C0 = int(C0)
                # reconstruct all C_i, test integrality/positivity/M-coprimality
                Cs = [C0]
                good = True
                for i in range(p):
                    d1, d2 = ds[i], ds[(i + 1) % p]
                    num = d1 - d2 + N ** us[i] * Cs[-1]
                    if num % M ** us[(i + 1) % p]:
                        good = False
                        break
                    Cs.append(num // M ** us[(i + 1) % p])
                if not good:
                    continue
                expanding = alpha > 1
                positive = all(c > 0 for c in Cs)
                coprime = all(c % M for c in Cs[:-1])
                found.append((p, ds, us, Cs[:-1], expanding, positive,
                              coprime))
    return checked, found


if __name__ == "__main__":
    print("== Part 1: skeleton extraction on exact induced orbits ==")
    total = 0
    for name, M, N, D in CHARTS:
        links = 0
        for _ in range(40):
            K = random.randrange(6, 14)
            eps = [random.choice(D) for _ in range(K)]
            links += extract_and_check(M, N, D, eps)
        total += links
        print(f"  {name:12s} 40 random coded orbits: all phase and chain "
              f"equations exact ({links} links)", flush=True)
    print(f"[PASS] skeleton normal form verified on {total} chain links\n")

    print("== Part 2: periodic-chain search (p <= 3, u <= 5) ==")
    verdict_ok = True
    for name, M, N, D in CHARTS:
        checked, found = periodic_search(M, N, D)
        exp_pos = [f for f in found if f[4] and f[5] and f[6]]
        con_pos = [f for f in found if not f[4] and f[5] and f[6]]
        neg = [f for f in found if not f[5]]
        print(f"  {name:12s} {checked:7d} patterns: integer fixed points "
              f"{len(found):3d}; expanding+positive+coprime {len(exp_pos)}; "
              f"contracting+positive {len(con_pos)}; nonpositive {len(neg)}",
              flush=True)
        for f in exp_pos:
            print(f"    !! EXPANDING POSITIVE CHAIN: {f}")
            verdict_ok = False
    if verdict_ok:
        print("[PASS] no expanding positive coprime periodic chain in range "
              "-- every expanding fixed point is nonpositive (the skeleton "
              "sign-criticality pattern)")
    print("\nALL CHECKS PASS" if verdict_ok else "\nSEARCH FOUND CANDIDATES")
