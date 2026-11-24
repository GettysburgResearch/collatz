# Focused internal semantic reviews

These reviews are independent collaborating-agent reconstructions, not
external peer review. The root separately inspected the proofs and ran the
fresh combined compiler/audit replay. The exact mathematical scopes below
are narrower than any whole-repository acceptance claim.

## Coefficient counting and finite strip exit

Reviewer: `band_route`. Verdict: **PASS** at the following exact bytes.

| File | SHA-256 |
|---|---|
| CoefficientCounting.lean | `070d4f0f0da69130b04033b8aac169fd1e9f763c3435ff78448ba1dbe232e51e` |
| CoefficientPeaks.lean | `34c522620ab742bd728db2d2ebf958b131a981fb5edd9d7c9ad160ee28d50db9` |
| COEFFICIENT_PEAKS.md | `f0a70650278bf52fba5ecc94ee102ab710b9faef69ec08187d27683c75a1cd41` |

The review checked the exact parity flip under addition of `2^k`, the
weighted residue moment, both integer threshold constants and the final
partial-period term in the quotient--residue packing bound. No independence
assumption on a fixed ordinary orbit appears.

It reconstructed both affine-correction inequalities. A finite strip
`1<=C_t<=B` gives `x_t<=B(n+t)` and `t<=6B*x_t`. A repeated pair among the
first `N=n+M+1` states would bound all future states by `B(n+N)`, contradicting
the second inequality at `H=6B^2(n+N)+1`; hence the needed injectivity is
derived. Every shifted counting block fits before `H`. Packing contradicts
the choice of `N`, and the polynomial clock estimate is algebraically
correct.

The note correctly credits the stronger qualitative coefficient-escape
results in the earlier orbit-Mellin program. The finite upper-exit
alternative is still possible, and a coefficient crossing is never equated
with ordinary descent. Neither universal coefficient stopping nor Collatz
is concluded.

`lean_architecture` also separately reviewed the counting module before
using its API in the dynamics module and found its exact residue and
inclusive-interval interpretation sound.

## Complete-certificate source reset

Reviewer: `lean_architecture`. Verdict: **PASS** at the following exact bytes.

| File | SHA-256 |
|---|---|
| CertificateBoundary.lean | `3cdedfd465939cf48528b8ee199d528a7d6d9f795b332470757ac0d96944d3c9` |
| CERTIFICATE_BOUNDARY.md | `d5ad56134c36d2adc586b10227e9e4a336e0548b7a764002be49b9a81230c0b5` |

The reviewer directly read PR177's `Witness.lean`, `GapMultiset.lean`, and
`RetainedEvenReset.lean` at
`a0a0d76f91b4e3846c1b1f0706cad56cb6098317`. The local certificate recurrence
and grade comparison match the pinned definitions mathematically, including
allowed gap-two padding at one. The new module proves its own ordinary
orbit semantics; it does not claim a Lean theorem importing both predicate
definitions.

Complete child certificates force odd endpoints, so every supplied gap is
an exact valuation. The four predecessor constructions preserve the literal
suffix. Oddness strengthens `z>=2p` to `z>=2p+1`, giving `S'=8z>=S+4` and
preserving every original target unchanged. At grade eight, the count drops
exactly once and every higher suffix count agrees. The explicit guards
concern the sibling `p`: it must be a ternary unit, nonterminal, and outside
the two displayed dead residue classes.

The separate physical boundary identities and their positivity conditions
were checked as well. They are not needed for the final source-growing
reset. The local interval theorem keeps the lower-rank hypothesis explicit
and leaves the global dispatcher open. No review concern remained at the
frozen files above.

## Written periodic-approximation rigidity and marginal population input

Reviewer: `lean_architecture`. Verdict: **PASS as a source-qualified written
proof**, outside the Lean count, at the following exact bytes.

| File | SHA-256 |
|---|---|
| PROFINITE_LABEL_RIGIDITY.md | `ec502a0e26562badfbfb615420ce80036917e1b39d6ec28be32c1a658b6cffa6` |
| PREDECESSOR_POPULATION_AUDIT.md | `07cd8744f5ddd29016f976faa2fa9bb8becef3ff42e5ec7f5cba7b4fad9ec07d` |

The reviewer directly checked Tao's version-seven Proposition 1.14 and
the consistency identities, and reconstructed the pinned selected-block
atom floor and marginal logarithmic-population proof. The final rigidity
argument does not use the separate joint-clock natural-density claim.
The odd-part and unitization losses give a valid lower logarithmic unit
mass with factor 20.

The review checked Haar parity independence, the same-symbol ternary
coupling and compact mixing, coherent weak limits of the actual ordinary
empirical measures, the finite-level stationarity defect with its exact
factor one-half, and total-variation passage to an invariant dominated
measure. It then checked the positive scalar bounds for a separating pair
of ordinary labels, one fixed finite density truncation independent of the
periodic approximant, and the arbitrary lower-limit subsequence argument.
The almost-everywhere density is never evaluated at ordinary integers.

The theorem gives a positive logarithmic lower-mean error and a natural
upper-mean error against every fixed periodic approximant of the displayed
modulus class. It does not construct ordinary component approximations,
erase retained source atoms, or prove convergence. The companion audit's
added LOG section was independently checked; this review is not a second
full audit of its separate joint-clock PD derivation.

The root also reconstructed the compact invariance, finite-density limit,
unit-source conversion and conductor-independent error argument before
publication. External analytic inputs remain source-qualified and are not
added to Lean as axioms.

## Cross-program guard comparison

The root separately checked
`GUARD_COMPOSITION_AUDIT.md` at SHA-256
`3dae66743d99a7ede57d6fd0fb2d20d11223e5d5681093842ada6e393587039a`.
The unbounded family `768r+295` is discharged by the already checked
eight-step identity. Its nearby family `768r+287` only demonstrates the
limits of the specifically listed short guards. The root independently
replayed the supplied source word for 133 and the first strict descent
of 1055 at clock 80 to 628; a further exact replay reached one at clock
107. These are bounded arithmetic checks, not additional Lean declarations
or evidence of any nonconvergent source.

## Evidence boundaries

The compiler receipt supplies mathematical kernel checking for the three
new source modules; this review addresses their interpretation and relation
to prior work. The population audit and any further measure-theoretic
deductions are written arguments with external inputs and are not included
in the 38-theorem Lean count. Earlier failed development compiles are not
counted as successful checks; the archived replay rebuilds every local proof
input successfully in a fresh output directory.
