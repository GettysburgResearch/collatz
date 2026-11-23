# Density-free arithmetic-germ proof and finite execution boundary

23 November 2026. **Full Collatz and the original residue-512 implication
remain OPEN.**

[Written theorem](../../../../research/lean-exact-witness-global-20261121/construction-attacks-20261123/germ/DENSITY_FREE_DEFLATED_GERM.md)
· [Actual executions](REPLAY.json)
· [Independent review](../reviews/REVIEW_DENSITY_FREE_GERM.md)
· [Source ledger](SOURCES.json)

The new theorem characterizes reaching one by a condition on the complete
actual binary germ `K_n(t)=(1+4t+t^2)B_n(2+t)`: coefficients in Z[1/3],
complex convergence radius greater than 1/2, and ternary convergence
radius at least one. It does not require a parity-density limit. It pays
explicit analytic bounds in place of that earlier premise; it does not
infer those bounds from the old qualitative arithmetic-germ hypothesis.

The written proof uses the full integral-model and local-realization
hypotheses of Chambert-Loir--Nous, Theorem4.3, and the actual-cycle
obstruction R6-SEL-4 at the frozen PR182 head. Both were read directly;
the independent reviewer also opened both primary objects. The full
actual germ is not constructed for an unrestricted positive source.

## Six finite Lean declarations

`GermCapacity.lean` checks two explicit positive logarithmic column
payoffs and their lower bound against every mixed column. The selected
row strategy is (2/5,3/5). The three remaining declarations check the
constant, linear and general convolution coefficients for the integer
inverse of `1+4t+t^2`.

The module uses Lean4.34.1 and Mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Strict compilation uses
`-j 1 -DwarningAsError=true`. All six axiom audits are preserved in
`lean-strict-audit.log`; only standard Lean/Mathlib axioms occur.

The multipoint rationality theorem, analytic domains, infinite Taylor
translation, variable-radius calculus, rationality-to-periodicity
consumer and universal germ construction are not formalized by this file.
The analytic source theorem has not been inserted as a Lean axiom.

## Exact finite controls

The checker uses rational interval arithmetic, with 96 terms of the
atanh logarithm series, to certify strict capacity margins. It checks
four radius choices above one half and a failed below-threshold control.
It verifies 64 integer inverse coefficients.

For 153 known convergent sources, it computes the deflated actual germ
by two independent finite constructions: backward substitution from the
terminal cycle, and the complete chronological prefix carry followed by
translation. These give 4,260 matching coefficients across 4,107 actual
ordinary steps, with maximum polynomial degree 219. The earlier derivative-
zero fixture is retained, and a constant polynomial fitted only at the
source value is rejected.

The normal and optimized checker outputs are byte-identical. These are
finite controls on actual known witnesses. They are not an empirical
claim that the complete germ of an unknown ordinary source has rational
coefficients or the specified radii.

The saved `REPLAY.json` records actual fresh root executions, full command
arguments, working directory, timestamps, exit codes, stdout and stderr,
with all three source hashes. The coordinating `ROOT_REPLAY.json` includes
these same three executions as part of its twelve-execution receipt.
