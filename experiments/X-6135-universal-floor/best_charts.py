"""Optimal fixed macro-block charts under the T-6131 criterion.

For block length q, the highest-dimension expanding chart uses the smallest k with 3^k > 2^q
(a larger k pushes k/q further from 1/2 and shrinks C(q-1,k-1)).

    dim(q) = log2 C(q-1, k-1) / q ,      least roots grow like 2^((1-dim) L) per Collatz step,
    ceiling = H_2(log2/log3) = 0.949956  (T-6131c).

Also tests, and REFUTES, the natural guess that continued-fraction convergents of log3/log2
are the best block lengths.
"""
import math
from math import comb, log2, ceil

ALPHA = math.log(2)/math.log(3)
CEIL = -ALPHA*log2(ALPHA) - (1-ALPHA)*log2(1-ALPHA)


def best_k(q):
    k = ceil(q*ALPHA)
    while 3**k <= 2**q:
        k += 1
    return k


def dim(q):
    return log2(comb(q-1, best_k(q)-1))/q


def main():
    print(f"universal ceiling  H_2(log2/log3) = {CEIL:.6f}   codim {1-CEIL:.6f}")
    print(f"\n{'q':>5} {'k':>5} {'k/q':>9} {'D = C(q-1,k-1)':>16} {'dim':>8} {'codim':>8}"
          f" {'gap':>8} {'depth L below 2^64':>19}")
    for q in [6, 19, 24, 41, 65, 84, 106, 200, 400, 1000, 2000]:
        k = best_k(q)
        D = comb(q-1, k-1)
        d = dim(q)
        Ds = str(D) if D < 10**12 else f"~2^{log2(D):.1f}"
        print(f"{q:>5} {k:>5} {k/q:>9.5f} {Ds:>16} {d:>8.5f} {1-d:>8.5f}"
              f" {CEIL-d:>8.5f} {64/(1-d):>19.0f}")

    d6 = log2(6)/19
    print(f"\nsix-branch chart (q=19 but D=6, not C(18,11)=31824):"
          f"  dim={d6:.5f}  codim={1-d6:.5f}  depth below 2^64 = {64/(1-d6):.0f}")
    print(f"universal floor (codim {1-CEIL:.5f}):"
          f"                              depth below 2^64 = {64/(1-CEIL):.0f}")

    print("\n--- refuted guess: are convergents of log3/log2 the best block lengths? ---")
    print("(numerators of the convergents are block lengths q, denominators are odd-step counts)")
    print(f"{'q':>6} {'dim(q)':>9} {'max dim over q+-5':>19} {'local max?':>11} {'k/q - alpha':>14}")
    for q in [8, 19, 65, 84, 485, 1054]:
        nb = max(dim(r) for r in range(max(2, q-5), q+6))
        print(f"{q:>6} {dim(q):>9.6f} {nb:>19.6f} {str(abs(dim(q)-nb) < 1e-12):>11}"
              f" {best_k(q)/q - ALPHA:>+14.8f}")
    print("""
REFUTED.  Convergents are where k/q is closest to alpha (the last column confirms it: q=84
gives +2.3e-5, q=1054 gives +4e-8), but that is a different objective from maximising dim.
dim(q) = log2 C(q-1,k-1)/q is largest when k/q is closest to 1/2, i.e. when the smallest
expanding k is as small as possible relative to q; it grows with q toward the ceiling almost
regardless of arithmetic quality.  Convergents matter for the CYCLE lane, where 2^q - 3^k must
be small (T-6140A), not for the dimension of a divergence chart.

Design criterion that survives: take q large.  dim -> H_2(alpha) = 0.949956 as q -> infinity.""")


if __name__ == "__main__":
    main()
