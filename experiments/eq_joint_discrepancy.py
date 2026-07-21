"""P2 deep-dive IV (issue #4): the C-hat product formula (mirror of
T-0007) and the S x C-hat pairing tested by joint discrepancy.

  (product)  C_j-hat(psi) = prod_{i=1..j} (1 + e(-17 * 64^{-i} psi /
             81^{j-i+1}))  -- the exact 81-adic mirror of T-0007.

  (pairing)  Near-window counting error is governed by the CRT-joint
             set J = {CRT(A, x): A in R_n, x in C_j} in
             Z/(64^n 81^j).  Measure its star discrepancy D* vs the
             1D discrepancies and a random baseline: cancellation in
             the S–C-hat pairing <=> D*(joint) tracks the max of the
             1D discrepancies rather than degrading.

  (decay)    Enhancement profile: share of C_1 classes in
             R_n cap (0, 64^{beta n}] across n -- the o(1) of Mask 6.
"""
import cmath
import math
from eq_ladder import coded
from eq_cantor_classes import build_C, enumerate_RK


def chat_direct(C, j, psi):
    Q = 81 ** j
    return sum(cmath.exp(2 * math.pi * 1j * psi * x / Q) for x in C[j])


def chat_product(j, psi):
    val = 1 + 0j
    for i in range(1, j + 1):
        Qi = 81 ** (j - i + 1)
        inv = pow(pow(64, i, Qi), -1, Qi)
        ph = (-17 * inv * psi) % Qi
        val *= 1 + cmath.exp(2 * math.pi * 1j * ph / Qi)
    return val


def star_discrepancy(points, Q):
    """Exact star discrepancy of a sorted point set in [0, Q)."""
    N = len(points)
    d = 0.0
    for i, x in enumerate(points):
        u = x / Q
        d = max(d, abs((i + 1) / N - u), abs(i / N - u))
    return d


if __name__ == "__main__":
    C = build_C(4)

    print("== C-hat product formula vs direct sum ==")
    import random
    random.seed(9)
    worst = 0.0
    for j in (1, 2, 3, 4):
        for _ in range(40):
            psi = random.randrange(1, 81 ** j)
            a = chat_direct(C, j, psi)
            b = chat_product(j, psi)
            worst = max(worst, abs(a - b))
    print(f"  max |direct - product| over 160 samples: {worst:.2e} "
          f"({'PASS' if worst < 1e-6 else 'FAIL'})")

    print("\n== joint discrepancy: D*(R_n x C_j) via CRT ==")
    print("   n  j      N        D*(joint)   D*(R_n)    rand~sqrt")
    for n in (10, 12, 13):
        Rn = enumerate_RK(n)
        Qn = 64 ** n
        d1 = star_discrepancy(Rn, Qn)
        for j in (0, 1, 2, 3):
            Qj = 81 ** j
            Q = Qn * Qj
            if j == 0:
                J = Rn
                Qq = Qn
            else:
                # CRT(A mod 64^n, x mod 81^j)
                u = Qj * pow(Qj, -1, Qn)   # == 1 mod 64^n, 0 mod 81^j
                v = Qn * pow(Qn, -1, Qj)   # == 0 mod 64^n, 1 mod 81^j
                J = sorted((A * u + x * v) % Q for A in Rn for x in C[j])
                Qq = Q
            N = len(J)
            dj = star_discrepancy(J, Qq)
            rnd = math.sqrt(math.log(max(N, 3)) / N)
            print(f"  {n:3d} {j:2d} {N:8d}   {dj:.6f}   {d1:.6f}   "
                  f"{rnd:.6f}", flush=True)

    print("\n== Mask-6 enhancement decay: share of C_1 in R_n ∩ (0,64^(bn)] ==")
    print("   n    b=0.85          b=0.90          b=0.95          b=1.00")
    for n in range(10, 17):
        Rn = enumerate_RK(n)
        row = [f"{n:4d}"]
        for b100 in (85, 90, 95, 100):
            Z = int(round(64 ** (b100 / 100 * n)))
            sel = [A for A in Rn if 0 < A <= Z]
            if len(sel) < 20:
                row.append("   (few)      ")
                continue
            sh = sum(1 for A in sel if A % 81 in (0, 1)) / len(sel)
            row.append(f" {sh:.4f}/{len(sel):<6d}")
        print("  " + "".join(row), flush=True)
    print(f"  (uniform share 2/81 = {2/81:.4f})")
    print("MEASUREMENT COMPLETE")
