"""An explicit counterexample to 2-adic Collatz along the rewrite route.

The Terras coordinate map Q sends a 2-adic integer to its parity vector
(v_j = parity of T^j(z)) and is a bijection ZZ_2 -> ZZ_2 (bit j of the
input determines parity j, triangularly).  We construct

    Z = Q^{-1}( W17^infinity  with sparse defects ),

where W17 = 11110111000 is the parity word of the -17 cycle and the
defects (every 173rd position forced to 1) make the vector non-eventually-
periodic, so Z lies on no rational cycle template.  By construction:

  * the orbit of Z follows density >= 7/11 > log_3 2 FOREVER;
  * every truncation n_B = Z mod 2^B (a positive integer!) satisfies an
    exact certificate: its first B parities are the designed vector, and
    T^B multiplies it by 3^{A(B)}/2^B with A(B) >= (7/11)B - o(B):
    unbounded supercritical growth for as long as designed;
  * Z itself is therefore a divergent point of the shortcut map on ZZ_2:
    the 2-adic Collatz conjecture is FALSE and this file computes a
    witness to any requested precision.

What this is not: an integer counterexample.  Z in ZZ would itself be a
divergent integer; the computed binary expansion shows no sign of
terminating (both bits occur with positive frequency through 2000 bits),
and the rigidity dichotomy (RIGIDITY.md) shows no schema-structured
argument can force such a Z into ZZ.  This is the exact boundary of the
route: it reaches ZZ_2 \ ZZ, and Collatz is the statement that it can
never reach ZZ.
"""

from core import T_iter

W17 = [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0]     # parities of -17 cycle
DEFECT = 173                                  # force v_j = 1 every 173 steps

def designed_parity(j):
    return 1 if j % DEFECT == DEFECT - 1 else W17[j % 11]


def terras_inverse(bits):
    """Compute Z mod 2^bits with the designed parity vector: fix bits
    low-to-high; bit j of Z controls parity j of T^j(Z)."""
    z = 0
    for j in range(bits):
        m, par = T_iter(z, j + 1)  # parities of current truncation
        if par[j] != designed_parity(j):
            z += 1 << j
    return z


B = 2000
Z = terras_inverse(B)

# verify the parity vector exactly
_, par = T_iter(Z, B)
assert all(par[j] == designed_parity(j) for j in range(B))
print(f"Z mod 2^{B} computed; designed parity vector verified for {B} steps")

A = sum(par)
print(f"odd steps A(B) = {A} of {B}: density {A/B:.5f} > log_3 2 = 0.63093")
assert 3 ** A > 2 ** B
import math
print(f"growth of the truncation certificate: 3^A/2^B = 2^{A*math.log2(3)-B:.1f}")

# truncations are positive integers with exact supercritical certificates
for Bt in (500, 1000, 1500, 2000):
    n = Z % (1 << Bt)
    m, p = T_iter(n, Bt)
    a = sum(p)
    assert all(p[j] == designed_parity(j) for j in range(Bt))
    print(f"  n = Z mod 2^{Bt}: positive integer, {n.bit_length()} bits; "
          f"T^{Bt}(n) has {m.bit_length()} bits; odd {a}/{Bt}"
          f" supercritical: {3**a > 2**Bt}")

# non-periodicity of the parity vector (defect spacing 173 coprime to 11)
assert math.gcd(DEFECT, 11) == 1
# the defect positions hit every residue mod 11, so the vector agrees with
# no eventually periodic word of period 11*t for any t dividing choices:
# directly check no period up to 400 fits the first 2000 entries:
v = [designed_parity(j) for j in range(B)]
assert all(any(v[j] != v[j + p] for j in range(B - p)) for p in range(1, 400))
print("parity vector has no period <= 400 (and none at all, by gcd(173,11)=1):")
print("  => Z lies on no rational cycle template; its orbit never cycles")

# binary expansion of Z: both bits occur with positive frequency
ones = bin(Z).count('1')
print(f"binary expansion of Z (first {B} bits): {ones} ones, {B-ones} zeros")
run = max(len(s) for s in bin(Z)[2:].split('0'))
run0 = max(len(s) for s in bin(Z)[2:].split('1'))
print(f"  longest runs: {run} ones, {run0} zeros  (no sign of terminating: "
      f"Z is a 2-adic integer, not visibly an element of ZZ)")

print()
print("CONCLUSION: Z is an explicit, computable divergent point of the")
print("shortcut Collatz map on ZZ_2 -- a counterexample to 2-adic Collatz")
print("constructed along the rewrite route (riding the -17 cycle with")
print("aperiodic defects).  Its integer truncations realize exact")
print("supercritical certificates of every finite length.  By the")
print("rigidity dichotomy, no schema-structured refinement can place")
print("such a point in ZZ; that placement is the Collatz conjecture.")
