"""Exact big-integer evaluation of the binding value of the T-6243 closed form.

T-6243:   Bmax(j) = ( sum_{m=0}^{k-1} 3^(k-1-m) 2^(a_m) ) / (2^j - 3^k),
          k = floor(j*log2/log3),  a_m = floor(m*log2 3).

chi_floor.c evaluates this in long double.  The certified floor turns entirely on ONE number --
Bmax(301994), which must lie below the scan bound -- so that one is recomputed here in exact
integer arithmetic, with nothing decided in floating point:

  * k is fixed by the exact comparison  3^k < 2^j < 3^(k+1);
  * a_m is fixed by the exact comparison  2^(a_m) <= 3^m < 2^(a_m + 1), marched incrementally;
  * the numerator is accumulated by Horner, N <- 3N + 2^(a_m), in exact integers;
  * the quotient is reported as a float only at the very end, from exact leading bits.

Also cross-checks the closed form against maxbound.py's exact rational at j = 65.
"""
import math

def bmax_exact(J):
    """returns (numerator, denominator, k) with Bmax(J) = numerator/denominator, exact."""
    p2 = 1 << J
    k, p3 = 0, 1
    while p3 * 3 < p2:
        p3 *= 3
        k += 1
    assert p3 < p2 < p3 * 3, "k is not floor(j*log2/log3)"
    D = p2 - p3
    # Horner over m = 0..k-1 with a_m marched exactly
    N = 0
    pw2, a, q = 1, 0, 1          # pw2 = 2^a, q = 3^m
    for m in range(k):
        while pw2 * 2 <= q:
            pw2 *= 2
            a += 1
        N = 3 * N + pw2          # a = a_m = floor(m log2 3) exactly
        q *= 3
    return N, D, k

# --- cross-check the closed form against maxbound.py's exact rational -----------------------
from fractions import Fraction
N, D, k = bmax_exact(65)
print("j = 65 : Bmax =", Fraction(N, D))
print("maxbound.py  :  364625035073295549935/420491770248316829")
print("match        :", Fraction(N, D) == Fraction(364625035073295549935, 420491770248316829))
print()

# --- the binding value --------------------------------------------------------------------
J = 301994
N, D, k = bmax_exact(J)
print("j =", J, " k =", k, " (3^k < 2^j < 3^(k+1) verified exactly)")
print("numerator has %d bits, denominator has %d bits" % (N.bit_length(), D.bit_length()))
val = N / D                  # Python's int/int is correctly rounded even at this size
print("Bmax(%d) = %.10e   (exact integers, float taken only at the last step)" % (J, val))
print("long double chi_floor.c value : 7.102205e+11")
print("float DP chi_bound_fast.c     : 7.101490e+11")
print()
print("scan bound needed to clear j = %d : %.6e" % (J, val))
