# Attempt to close the primitive-source moment

**OPEN.** This is a record of the attempted global estimate, not an
additional convergence assumption attached to the Lean equivalence.

Use the notation of `PRIMITIVE_SURVIVAL.md`: A_q is the actual
fourth-power mass of positive odd sources not yet at 1; B_q is its
primitive-source part; R_q is the complete higher-lift remainder.

## Exact absorption and source-birth balance

Let

\[
F_q=\sum_{\substack{n>0\text{ odd}\\
 U^q(n)\ne1,\ U^{q+1}(n)=1}}n^{-4}.
\]

Since U(1)=1, disjoint positive summation gives

\[
A_{q+1}=A_q-F_q,\qquad
B_{q+1}=B_q-F_q+(R_q-R_{q+1}).\tag{F1}
\]

A source becomes primitive when n<2^(A_q(n)+1), where A_q(n) is its
cumulative division exponent. Once primitive it remains primitive,
because every later valuation is positive. Therefore R_q is decreasing.
The total new primitive-source mass after stage q is R_q, bounded by
zeta(4)*15^(-q)/16. Thus the source-birth term is already summable. The
missing estimate is a sufficient loss from already present ordinary
sources. Bounding new births alone cannot remove a persistent source.

## A concrete fixed-loss proposal fails

The tempting uniform inequality F_q>=A_q/1000 is false even on the
actual arithmetic sequence. At q=20, exact finite iteration of all
positive odd n<=512 finds that only n=377 first reaches 1 at step 21.
Moreover

\[
U^{20}(27)=377,\quad U^{21}(27)=283,\qquad
U^{20}(31)=425,\quad U^{21}(31)=319.
\]

The uncomputed sources have the unconditional envelope

\[
\sum_{n>512\text{ odd}}n^{-4}
\le\sum_{n>512}n^{-4}
\le\int_{512}^{\infty}x^{-4}\,dx
=\frac1{3\cdot512^3}.
\]

Hence

\[
F_{20}\le377^{-4}+(3\cdot512^3)^{-1},\qquad
A_{20}\ge27^{-4}+31^{-4}.
\]

Exact rational arithmetic gives

\[
27^{-4}+31^{-4}
-1000\bigl(377^{-4}+(3\cdot512^3)^{-1}\bigr)
=\frac{71767245110956876777297}
 {166336335222330752861277782016}>0.\tag{F2}
\]

The finite computation determines the whole part below 512; the
analytic tail handles every omitted source. This refutes the specified
coefficient. It does not refute every smaller uniform coefficient or
an estimate on adaptive blocks. F2 is a written exact calculation with
finite integer replay, and is not among the theorems compiled in the
companion Lean module.

It also refutes the direct primitive-moment proposal

\[
B_{q+1}\le\frac{999}{1000}B_q+\frac18\,15^{-q}.
\]

At q=20, its left side minus its right side is bounded below by
the F2 margin divided by 1000, minus
(1/8)*(15^(-20)+15^(-21)). The former exceeds 10^(-10); the latter
is below 10^(-20). Thus a correct exponentially small source-birth
allowance does not repair that particular contraction inequality.

## Why the new mixing interface does not supply the missing loss

The new PR173 interface at
`cccf14d13250d3f98ef9b01ddbd304d11294e603` proves exact mixing of a
finite dyadic residue square and converts a small ordinary
table-mismatch count into label rigidity. Its five-block criterion
still needs a passing bound on actual missed mergers. It gives no such
bound merely from the residue square.

To use that interface here one would need to control the periodic
approximation error of the actual surviving component labels, or
directly prove sufficiently many absorptions in F1. The source-word
partition does not supply either estimate: a hypothetical fixed
nonconvergent source contributes the same n^-4 forever, even while its
valuation word occupies an exponentially small residue cylinder.
Endpoint mixing under a residue distribution does not erase that
ordinary atom.

Adaptive-block renewal remains a possible target, but no bound has been
proved that forces each fixed surviving source to lose its mass. A
positive residual in A_q is compatible with the established birth
bound, orbit sparsity, long failed blocks, and the presently conditional
merger-count interface. The first unsupported step is therefore an
actual absorption estimate, not the finite-word partition or its tail.
