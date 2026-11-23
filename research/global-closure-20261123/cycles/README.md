# Unrestricted cycle closure: simultaneous scaling and the exact integral lattice

**Status, 23 November 2026: the full positive integer-cycle exclusion remains
OPEN.** This lane attacked the complete word condition after reading the new
residual-denominator, identity-atom and invariant-polynomial work. It does
not add a fixed word family, a prime census or another rational-cycle
construction.

The [closing attempt](INTEGRAL_MAHLER_CLOSURE_ATTEMPT.md) develops two routes:

1. Apply independent-base Mahler rigidity to the *entire* positive cycle
   polynomial. The exact dyadic elimination is already in PR175 and is
   credited there. The additional primary-source check proves that the
   natural nonzero dyadic series cannot satisfy any independent 3-Mahler
   equation: it is nonrational. This is true even for the genuine trivial
   cycle. Thus the independent-base theorem does not provide the proposed
   rigidity conclusion from the identities currently available.
2. Keep every word and every denominator factor in a two-dimensional torus
   map. Its minimal triangular diagonalizing isogeny has degree exactly
   `D/gcd(C,D)`, the **actual reduced denominator**, not the polynomial
   denominator `D_pol`. Integer cycle closure is precisely the degree-one
   case. The common Mahler direction exists at every degree, so this
   normalization preserves the remaining arithmetic question.

The elementary derivations are supplied in full. The Mahler corollary imports
Adamczewski--Bell, Theorem 1.3, with the exact field and independent-base
hypotheses checked against the primary journal PDF. These are written
arguments and a qualified application of an external theorem; there is no
new Lean closure theorem, and no imported theorem has been declared as a Lean
axiom.

The attempt also records why the existing residual polynomial growth,
primitive-divisor ideas and fixed-support gcd theorems have not yielded a
word-uniform estimate for simultaneous numerical cancellation. The exact
remaining target is

$$
2^A-3^p \nmid \sum_{i=0}^{p-1}2^{d_i}3^{p-1-i}
$$

for every nontrivial primitive positive candidate. Neither the torus change
of coordinates nor the sparse-series lemma proves this statement.

[Source and evidence record](../../../reports/2026-11-23-global-closure/cycles-sources.md)
records the exact repository heads and the primary literature inspected.
