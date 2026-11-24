# Coefficient stopping: literature and overlap audit

## Outcome

This investigation did **not** close the passage from coefficient escape to
ordinary descent. No additional Lean theorem is claimed here. Several
initially promising bounds are already present in the repository or in the
classical stopping-time literature; the current continuation therefore
prioritizes the genuinely broader rigidity and inverse-prefix results.

For the shortcut map, write

\[
 T^k(n)=\frac{3^{q_k}}{2^k}(n+M_k),\qquad M_k\ge0.
\]

The distinction remains exact: `3^q_k < 2^k` is coefficient contraction,
whereas ordinary descent requires

\[
 n\left(\frac{2^k}{3^{q_k}}-1\right)>M_k.
\]

The positive affine correction cannot be discarded when applying a
parity-counting or Diophantine estimate to one prescribed ordinary source.

## Primary literature checked

**Korec, 1994.** The primary paper proves that, for each
`c > log_4(3)`, the sources whose orbit reaches below `n^c` have natural
density one. Its proof permits a witnessing clock bounded by `log_2 n`
on the density-one family it constructs. It uses the exact parity-class
correspondence and binomial counting, while controlling the affine
correction by the source scale. This is not a bound for every source.
The paper itself separates increasing-time density estimates from stronger
source-dependent height conclusions and gives examples illustrating that
the quantifiers matter.

Source: Ivan Korec, *A density estimate for the 3x + 1 problem*,
Mathematica Slovaca 44 (1994), 85–89, Theorem 1 and its proof;
[primary scan](https://dml.cz/bitstream/handle/10338.dmlcz/133225/MathSlov_44-1994-1_8.pdf).

**First-crossing refinements, November 2026.** The primary preprint of
Elias De Jesús states an at-most-81-odd-runs descent theorem and stronger
necessary conditions for a first-crossing failure. Its inputs include a
verified coefficient/ordinary stopping-time equality range, rational
approximations, and Rhin's logarithmic lower bound. It explicitly credits
the classical affine comparator and the asymptotic least-residue
exception to Lagarias's Theorem E. Thus a polynomial source bound obtained
merely by combining the correction estimate with a linear-form bound
would not be a new route. The preprint does not claim full Collatz or full
coefficient/ordinary stopping-time equality. Its external numerical and
Diophantine inputs have not been imported into this Lean packet.

Source: Elias De Jesús, *Realizer Bounds and Repetition Constraints at the
First Coefficient Crossing in the 3x + 1 Problem*, version 2,
14 November 2026, Proposition 1, Remark 3, Theorem 8, Corollary 9;
[primary PDF](https://hexagonmath.org/pdf/2611.00459v2).

The publisher's metadata for Terras's 1976 paper was checked, but its
primary full text could not be retrieved in this session. This audit does
not present a new verification of that paper or of Rhin's original
logarithmic estimate.

## Repository overlap that changes the implementation decision

The source survey found the following overlap:

- [ORBIT_MELLIN.md](https://github.com/GettysburgResearch/collatz/blob/7bb6d36d3bc37dd09b52aa9a23c8e33973032359/research/astra-three-routes/pass2/ORBIT_MELLIN.md)
  at PR92 commit `7bb6d36d3bc37dd09b52aa9a23c8e33973032359` already
  states the ordinary-orbit count `4 X^(39/40)`, the reciprocal
  budget `160 m^(-1/40)`, the resulting product bound, full coefficient
  divergence on a nonperiodic orbit, a quantitative coefficient occupation
  bound, and a cycle discrepancy bound independent of the period.
- [FINITE_RECORDS.md](https://github.com/GettysburgResearch/collatz/blob/7bb6d36d3bc37dd09b52aa9a23c8e33973032359/research/astra-three-routes/pass3/FINITE_RECORDS.md)
  at the same PR92 pin transfers the counting argument to finite injective path segments and
  gives finite descent-or-repetition consequences under explicitly supplied
  local coefficient-window hypotheses.
- [ROUTE2_RETURN_ECHO.md](https://github.com/GettysburgResearch/collatz/blob/2d478a6588f33a72fc3a5bdc085a928b5cf78737/research/astra-three-routes/ROUTE2_RETURN_ECHO.md)
  as retained in the published checkpoint `2d478a6` already keeps the
  first-crossing correction, bounds a non-descent
  displacement by `q/3`, and studies the forced continuation through the
  two-adic agreement of the source and endpoint.

These are written repository results with their stated hypotheses. They
are not being relabeled as new kernel-checked outputs of this continuation.
The existing [COEFFICIENT_PEAKS.md](COEFFICIENT_PEAKS.md) identifies the
narrower, explicit finite alternative that this packet actually formalized.

A further elementary candidate was investigated: if `k=blockClock(P)`,
`2^k <= n`, `B+1 <= P`, and a simple ordinary orbit segment stays in
`[n,Bn]` long enough to contain every required `k`-step block, then

\[
 4PN\le Bn+2^k\le(B+1)n.
\]

Indeed the unconditional affine estimate
`2^k T^k(x) <= 3^q (x+2^k)` makes each block resistant at parameter `P`,
and the already checked `CoefficientCounting.packing` supplies the count.
Choosing `P` to grow with `n` gives a sublinear residence bound. This is
useful intuition about retaining the affine correction, but weaker in
substance than the repository's existing finite-path sparsity program.
It was not added as a nominally new theorem.

## The unresolved pointwise obligation

Neither a density-one descent theorem nor an occupation bound forces a
particular ordinary path to leave the exceptional set. Likewise, an
upper coefficient exit is not a contradiction, and a coefficient drop
does not by itself pay the affine correction. The remaining source-level
obligation must rule out the all-supercritical alternative or prove an
appropriate ordinary descent at a crossing (or its retained continuation).
This audit supplies no uniformization of an almost-all theorem, no assumed
bound on exceptional ordinary sources, and no new global stopping-time
claim.
