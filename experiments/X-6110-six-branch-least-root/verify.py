"""Self-contained re-verification of every value published in X-6110.

Re-derives nothing from the search: each m_N below is re-run through the forward chart map
and its digit word recomputed.  Exit status is nonzero if any check fails.
"""
import math
import sys

P = 3**12
Q = 2**19
A = [7 * 3**(2*i) * 2**(15-3*i) for i in range(6)]
ASET = set(A)
IDX = {a: i for i, a in enumerate(A)}

# published table: N -> (m_N, digit word)
TABLE = {
    1:  (6472, "4"),
    2:  (1908874353, "50"),
    3:  (44906374791168, "041"),
    4:  (275202518480529950784, "3222"),
    5:  (735266885070322294097984, "31552"),
    6:  (49927377479016341945330731072, "345415"),
    7:  (31262847560142629190894965371116657, "5500454"),
    8:  (181625992579115023082252809688279976000, "34150040"),
    9:  (274731072270742333628800865325991165013963264, "252541135"),
    10: (1986427850123090115679978949016973174519765670216, "4032154251"),
    11: (597061551299008579089934000992013372324288526534606848, "03512524310"),
    12: (83301137368103499460139839972641009013711852735287572369408, "134324152111"),
    13: (30699375960653180905548356146446826616831594299893600882131999048,
         "4515040532345"),
    14: (5507203783350029278298158112206428933561267597997030606259626621304832,
         "01123340100302"),
    15: (148637017271338238565064267618715766778481872048601196567971011267386061312,
         "205431351450115"),
}


def legal_steps(x, cap):
    """Number of consecutive legal chart steps from x (capped), plus the digit word."""
    w = []
    for _ in range(cap):
        d = (-P * x) % Q
        if d not in ASET:
            break
        w.append(IDX[d])
        x = (P * x + d) // Q
    return w


def main():
    ok = True
    prev = 0
    for N in sorted(TABLE):
        m, word = TABLE[N]
        w = legal_steps(m, N + 1)
        got = "".join(map(str, w))
        checks = {
            "legal for exactly N steps": len(w) == N,
            "digit word matches":        got[:N] == word,
            "strictly greater than m_{N-1}": m > prev,
        }
        for name, val in checks.items():
            if not val:
                print(f"FAIL N={N}: {name}  (got word {got})")
                ok = False
        prev = m
    if ok:
        print(f"all {len(TABLE)} published least roots verified "
              f"(legal for exactly N steps, correct digit word, strictly increasing)")
        ks = sorted(TABLE)
        ls = [math.log(TABLE[k][0]) for k in ks]
        n = len(ks)
        sx, sy = sum(ks), sum(ls)
        sxx = sum(k*k for k in ks)
        sxy = sum(k*l for k, l in zip(ks, ls))
        slope = (n*sxy - sx*sy) / (n*sxx - sx*sx)
        print(f"growth fit: exp(slope) = {math.exp(slope):,.0f}   "
              f"density prediction Q/|A| = {Q/len(A):,.1f}   "
              f"log-exponent error {abs(slope - math.log(Q/len(A)))/math.log(Q/len(A))*100:.2f}%")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
