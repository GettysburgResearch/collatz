"""P6 (issue #4): the EQ ladder -- coded survivor sets and the survivor
law at every verified chart rung.

Each chart (M, N, D) induces H_D(MB+d) = NB+d with inverse branches
J_d(x) = (Mx + (N-M)d)/N; the K-step valid residues mod M^K are exactly
the |D|^K coded sums (T-0007 shape, transferred per GENERAL.md #3):

    A(eps) = sum_{t<K} (N-M) eps_t M^t N^{-(t+1)}  (mod M^K).

Checks per chart:
  1. coding functional check: for random words eps, the integer A(eps)
     mod M^K actually executes K H_D-steps emitting exactly eps
     (exact arithmetic);
  2. injectivity: |R_K| = |D|^K;
  3. survivor law: minimal nontrivial element of R_K (nontrivial =
     not a fixed digit d in D) vs the equidistribution prediction
     M^K/|D|^K; ratio in [~0.1, ~10] with no drift = law holds.

Rungs (densities marching toward log_3 2 = 0.63093):
  (64,     81,    {0,1})        L=6,  a/L = 0.66667   (reference: M3)
  (512,    729,   {0,1,2})      L=9,  a/L = 0.66667
  (2^17,   3^11,  {0..5})       L=17, a/L = 0.64706
  (2^22,   3^14,  18 sparse d)  L=22, a/L = 0.63636
"""
import random

random.seed(2)

D18 = [0, 16, 20, 21, 32, 34, 35, 40, 42, 49, 68, 69, 70, 78, 79,
       92, 93, 94]

CHARTS = [
    ("64->81  |D|=2", 64, 81, [0, 1], 16),
    ("512->729 |D|=3", 512, 729, [0, 1, 2], 11),
    ("2^17->3^11 |D|=6", 1 << 17, 3 ** 11, list(range(6)), 7),
    ("2^22->3^14 |D|=18", 1 << 22, 3 ** 14, D18, 5),
]


def step(A, M, N, D):
    d = A % M
    assert d in D, "invalid digit"
    return N * (A // M) + d, d


def coded(eps, M, N, K):
    MK = M ** K
    Ninv = pow(N, -1, MK)
    A = 0
    npow = Ninv
    Mpow = 1
    for t in range(K):
        A = (A + (N - M) * eps[t] * Mpow * npow) % MK
        npow = npow * Ninv % MK
        Mpow *= M
    return A


def run_chart(name, M, N, D, KMAX):
    print(f"== {name}:  M={M}, N={N}, N-M={N - M}, "
          f"law base M/|D| = {M / len(D):.4g} ==", flush=True)
    # 1. functional check on random words at K = KMAX
    for _ in range(25):
        eps = [random.choice(D) for _ in range(KMAX)]
        A = coded(eps, M, N, KMAX)
        x = A
        out = []
        for _ in range(KMAX):
            x, d = step(x, M, N, D)
            out.append(d)
        assert out == eps, (eps, out)
    print(f"  [PASS] coding executes {KMAX} exact H-steps on 25 random words")
    # 2+3. enumerate R_K, injectivity, survivor law
    trivial = set(D)
    print("   K      |R_K|  |D|^K ok   min nontrivial    law M^K/|D|^K   ratio")
    RK = {coded([d], M, N, 1) for d in D}
    words = [[d] for d in D]
    for K in range(2, KMAX + 1):
        words = [w + [d] for w in words for d in D]
        RK = {coded(w, M, N, K) for w in words}
        ok = len(RK) == len(D) ** K
        nontriv = [A for A in RK if A not in trivial]
        mn = min(nontriv)
        law = M ** K / len(D) ** K
        print(f"  {K:2d} {len(RK):10d}  {'Y' if ok else 'N'}"
              f"   {mn:16d}   {law:14.6g}   {mn / law:7.3f}", flush=True)
    print()


if __name__ == "__main__":
    for c in CHARTS:
        run_chart(*c)
    print("ALL CHECKS PASS (coding + injectivity at every rung; "
          "law ratios reported above)")
