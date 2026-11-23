# Independent review: the general-density two-center consumer

23 November 2026. Reviewer: `/root/actual_collision`.

**Verdict: VERIFIED, for the stated conditional written theorem at the
frozen file hash below.** This is not a proof of Jet hypothesis J, of a
limiting parity density for every ordinary source, or of Collatz.

## Frozen target and inspected source

- Target: `research/literature-push-20261123/rigidity/GENERAL_DENSITY_JET.md`.
- SHA256: `400e3c6cdccea71b71224fc2ee5cfb1379b334e5422cd64b81a87bd239403890`.
- Base worktree commit: `a9b23dcee61a4b65a63aa4e7ca653d875a405037`.
- Supporting definitions and critical consumer were read in
  `rigidity/SCALAR_BOUNDARY_AND_SECOND_CENTER.md`, SHA256
  `e5b8ac874505bbecfd2ae889cfe81eb9586b68e4ad19fb3a0ee6dbe61a493c73`.
- The primary PDF of Chambert-Loir--Nous,
  [*Potentiel et rationalite*](https://arxiv.org/pdf/2305.17210),
  Sections 2.3 and 4.1--4.3, was directly opened during this review.
  Section 2.3 permits disconnected local analytic domains; Section 4.1
  requires the compatible local meromorphic realizations and an integral
  model; Theorem 4.3 uses strictly positive game value to obtain one
  rational function with the specified germs. A separate request to the
  version-suffixed URL failed; this review does not label that failed
  request as a successful independent download of a fixed-version PDF.

This is a review of the target's new capacity estimate and its application,
not an independent audit of the surrounding repository or every earlier
rational-series theorem.

## Reconstructed small-hole estimate

Fix `S>2+h`, `0<h<2`, and let
`Omega=D(0,S)\setminus closure(D(2,h))`. The two displayed disc Green
functions have the correct logarithmic singularities and vanish on the
outer circle. On the hole boundary,

\[
g_S(z,0)\le \log\frac S{2-h}=M_h,
\qquad
g_S(z,2)\ge
\log\frac{S^2-4-2h}{Sh}=m_h>0.
\]

The second inequality uses
`S^2-2z=S^2-4-2h exp(it)` on that boundary. In fact `S>2+h`
already implies positivity of `m_h`.

Let `H` be one on the inner boundary and zero on the outer boundary.
The difference `g_S(z,0)-g_Omega(z,0)` extends harmonically across zero;
its logarithmic singularities cancel. The maximum principle bounds it
between zero and `M_h H`. A second application to
`g_S(z,2)/m_h-H` gives

\[
H(0)\le \frac{g_S(0,2)}{m_h}
=\frac{\log(S/2)}{m_h}.
\]

Thus the loss `delta` of the zero-center Green constant satisfies
exactly the target's inequality (5). No unproved asymptotic capacity
formula is needed for this step.

For a **fixed** `R>2`, take `S=R exp(-epsilon)` and `h=2 epsilon`.
The admissibility inequalities hold for sufficiently small epsilon.
The numerator in (5) tends to `log(R/2)^2`, while its denominator is
`|log epsilon|+O_R(1)`. Therefore

\[
0\le\limsup_{\varepsilon\downarrow0}
\delta_\varepsilon|\log\varepsilon|
\le \log(R/2)^2.
\]

The bound is pointwise in the fixed density; no uniform choice of
epsilon across all germs or all values of `R` is asserted.

## Global matrix and arithmetic hypotheses

The ternary interval in the target gives

\[
\log S+\log r_3=-d_\varepsilon\varepsilon,
\qquad 2<d_\varepsilon<3.
\]

Hence `a=-delta-d_epsilon epsilon` and
`b=log epsilon+C`, with `C` fixed independently of epsilon. Both are
negative for small epsilon, and

\[
\limsup ab\le\log(R/2)^2
\le\log(3/2)^2<\log2^2.
\]

All error terms in this product vanish: `epsilon |log epsilon|` tends
to zero and the small-hole bound implies `delta=O(1/|log epsilon|)`.
The strict margin follows from `R<=3`; the proof does not mistake an
equality-case capacity criterion for a strict one. The two-row mixed
strategy displayed in the target has positive weights and equal
positive payoff against both columns when `ab<log2^2`.

The local realizations also retain the relevant distinctions:

- At two, the original binary unit disc contains both centers. The
  second germ is required to be the **entire actual translated germ**,
  so one binary analytic function realizes both. Its off-diagonal
  Green value is `-log|2|_2=log2`.
- At infinity when `R>2`, the hole separates the original complex
  branch from the second germ. They are realized on disjoint
  components. No false equality between the binary value `-n` and
  the real value at two is used.
- At three and the remaining finite primes the indicated discs are
  disjoint. The small second-center radii can be fixed while epsilon
  shrinks. The common coefficient ring in J gives an integral model
  outside the finite set of primes dividing `6M`, with exactly the
  reduction-tube domains required by the primary theorem.
- The cases `R<2` and `R=2` have first-diagonal loss `O(epsilon)` and
  hence product tending to zero, as the target states. The small-hole
  argument is only used for `R>2`.

These checks justify the cited rationality conclusion under J and the
assumed limiting density. The previously credited rational-series
consumer then yields eventual ordinary periodicity.

## Converse and scope

For the converse, a rational function matching the actual binary series
is regular at two, because two lies inside the binary convergence disc.
Its rational Taylor coefficients at two have denominators in one fixed
finite prime set and have positive convergence radii at every completion.
This verifies J for an eventually periodic source.

The result is therefore a valid equivalence on the stated class of
sources with a limiting parity density. It does not construct even the
first unknown derivative at two, and it does not imply that the
limiting-density hypothesis holds on an arbitrary hypothetical escape.
It also leaves exclusion of other positive cycles separate. No Lean
formalization of the Green functions or the primary multipoint theorem
was run or claimed in this review.
