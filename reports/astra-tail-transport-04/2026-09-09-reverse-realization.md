# Research continuation: reverse realization and the unresolved progress step

Parent: PR105 at `912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe`.
All new results are PROPOSED pending independent mathematical review.
This is a research contribution, not an extension of Reviewer D's verdicts.

The requested end-to-end attempt focused on the parent's illegal-minimizer
obstruction. A useful connection emerged: any expanding-word component at
most n^2 already certifies a smaller positive ancestor, whether or not the
word is legal from n. The correct common induction order is ordinary value.
The source rank of the witness can increase.

This gives an exact positive-ancestor formula for the SAME rho, a batch algorithm
using O(N log N) physical shortcut states for ranks through N, and a sharper
square-root spectrum after retaining the affine progression moduli. The complete
infinite dictionary satisfies N_rho(X)<350sqrt(X), reciprocal sum <14, and
ordinary-height inverse-square source tail <77/N^2.

The construction resolves an infinite odd family in 19 mod36 whose unique
minimizing 111010 word is physically illegal. Its smaller ordinary ancestor
is physically valid, but has 4096/81 times the old source's rho. The finite
example 1351 --111010--> 1711 also shows why considering nonminimal components
below n^2 is more useful than testing minima alone.

The resulting normalizer terminates, produces a finite physical merging diagram,
and may return an explicit residual. The attempted universal next-step progress
claim fails: for any finite K, sources 0 mod3 and -1 mod2^(K+2) have all K forward
prefixes normalized back to the original source. Their total signed clock is
zero, so these are administrative cancellations, not nontrivial Collatz cycles.

The exact remaining all-source progress condition is Q-ATT-301 in the proof.
It has not been proved. The new manuscript is not a completed Collatz proof
with only routine independent checking left.

## Deliverables and exact checks

Eight new files only: three research files, four experiment files, and this
report. No parent file, main branch, canonical registry, reviewer record,
workflow or setting is changed.

The formal-word generator and independently structured positive-orbit verifier
agree on 4095 exact ranks, all 1688 qualifying source/word pairs in that range,
four complete rank balls, physical normalization composition and explicit
adversarial families. The normalizer produces 569 initial residual labels;
184 tested sources reach 1 under its rules. These are partial-algorithm outputs,
not a convergence classification of the tested range.

The payload also checks eleven large inverse-family substitutions (large rank
values via explicit parent-theorem hypotheses, not exhaustive word search),
21 echo sources spanning 381 physical forward positions, and the near-critical
counterexample demonstrating necessity of the spacing guard. Twelve resealed
corruptions are rejected. No source/generator/repository imports occur in the
verifier; all checks remain active under optimization.

Semantic digest:
`a6f7d63e6c6f54f0d0078d02768ebc56226880f436f3365bbaef0e738d7cf75f`.

Both programs have one author. Their agreement is implementation cross-checking,
not independent mathematical peer review. A complete authenticated checkout
was unavailable; no repository-wide structural validator execution is claimed.
The publication receipt records the actual GitHub head and byte identities.
