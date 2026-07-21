"""P2 deep-dive III (issue #4): the 81-adic Cantor refinement of the
room recursion.

Claims under test (EQ-INTERCHANGE.md ###11-12):

  (C_j)  The set of j-step-admissible seeds
         C_j = {A mod 81^j : the deterministic child chain
                A_{i+1} = (64A_i + 17 eps_i)/81, eps_i = A_i mod 81,
                keeps A_i mod 81 in {0,1} for i < j}
         satisfies the exact lifting recursion
             C_j = {(81c - 17 eps) * 64^{-1} mod 81^j :
                    c in C_{j-1}, eps in {0,1}},
         and |C_j| = 2^j exactly.

  (refined identity)  For Y in the one-room regime iterated j times:
         {A in R_K : 0 < A <= Y}  <-->
         {A* in R_{K-j} : A* mod 81^j in C_j, 0 < desc_j(A*) <= Y},
         desc_j = j-fold deterministic child map; and
         desc_j(A*) = (64/81)^j A* + O(1) (drift < 4).

  (mask 6 at depth j)  law <=> R_n cap interval occupies the 2^j
         Cantor classes with total frequency (2/81)^j + o(1).
"""
import math
from eq_ladder import coded

M, N = 64, 81


def build_C(jmax):
    C = {1: [0, 1]}
    for j in range(2, jmax + 1):
        inv = pow(64, -1, 81 ** j)
        C[j] = sorted({(81 * c - 17 * e) * inv % 81 ** j
                       for c in C[j - 1] for e in (0, 1)})
    return C


def admissible_direct(A, j):
    """Check the chain condition directly on the integer A."""
    x = A
    for _ in range(j):
        e = x % 81
        if e not in (0, 1):
            return False
        x = (64 * x + 17 * e) // 81
        assert (64 * (x * 0 + 0) + 0) == 0  # no-op
    return True


def desc(A, j):
    x = A
    for _ in range(j):
        e = x % 81
        assert e in (0, 1)
        x = (64 * x + 17 * e) // 81
    return x


def enumerate_RK(K):
    words = [[0], [1]]
    for _ in range(K - 1):
        words = [w + [d] for w in words for d in (0, 1)]
    return sorted(coded(w, M, N, K) for w in words)


if __name__ == "__main__":
    JMAX = 4
    C = build_C(JMAX)
    print("== C_j construction ==")
    ok = True
    for j in range(1, JMAX + 1):
        ok &= len(C[j]) == 2 ** j
        # cross-check lifting vs direct chain condition on a sample
        import random
        random.seed(6)
        for _ in range(300):
            A = random.randrange(81 ** j * 50)
            lhs = (A % 81 ** j) in set(C[j])
            rhs = admissible_direct(A, j)
            if lhs != rhs:
                ok = False
                print(f"  chain/class mismatch j={j} A={A}")
        print(f"  j={j}: |C_j| = {len(C[j])} = 2^{j} "
              f"{'OK' if len(C[j]) == 2 ** j else 'FAIL'}")
    print(f"  [{'PASS' if ok else 'FAIL'}] lifting recursion == direct "
          f"chain condition (300 samples/level)")

    print("\n== refined identity: count(K,Y) via Cantor classes ==")
    R = {n: enumerate_RK(n) for n in range(6, 15)}
    bad = tested = 0
    for K in (10, 12, 14):
        for j in (1, 2, 3):
            for Y in (10 ** 3, int(64 ** (0.6 * K)), int(64 ** (0.8 * K))):
                if 81 ** (j + 1) * Y >= 64 ** K:
                    pass  # regime generous; identity checked via desc anyway
                lhs = sum(1 for A in R[K] if 0 < A <= Y)
                Cs = set(C[j])
                rhs = sum(1 for A2 in R[K - j]
                          if A2 % 81 ** j in Cs and A2 > 0
                          and 0 < desc(A2, j) <= Y)
                tested += 1
                if lhs != rhs:
                    bad += 1
                    print(f"  MISMATCH K={K} j={j} Y={Y}: {lhs} vs {rhs}")
    print(f"  [{'PASS' if bad == 0 else 'FAIL'}] {tested} cells")

    print("\n== drift bound |desc_j(A) - (64/81)^j A| ==")
    import random
    random.seed(8)
    mx = 0.0
    for _ in range(2000):
        j = random.randrange(1, JMAX + 1)
        A = random.choice(C[j]) + 81 ** j * random.randrange(10 ** 6)
        mx = max(mx, abs(desc(A, j) - (64 / 81) ** j * A))
    print(f"  max drift over 2000 samples: {mx:.3f} (< 4 claimed)")

    print("\n== Mask 6 at depth j: Cantor-class share of R_n cap (0,Z] ==")
    print("  n   j   Z=64^(bn)   |set|    share      (2/81)^j")
    for n in (12, 14):
        for j in (1, 2):
            for b10 in (9, 10):
                b = b10 / 10
                Z = int(64 ** (b * n))
                sel = [A for A in R[n] if 0 < A <= Z]
                if len(sel) < 30:
                    continue
                Cs = set(C[j])
                sh = sum(1 for A in sel if A % 81 ** j in Cs) / len(sel)
                print(f" {n:3d} {j:3d}   b={b:.1f}    {len(sel):6d}"
                      f"   {sh:.5f}    {(2 / 81) ** j:.5f}")
    print("MEASUREMENT COMPLETE")
