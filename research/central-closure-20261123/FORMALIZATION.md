# What the new Lean files prove

The runtime pins are Lean **4.34.1**, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`.
Both new modules import only Mathlib. Their 21 public declarations are
audited individually; no inherited theorem is counted as new.

## ResidualWord.lean: 12 public declarations

| Declarations | Exact formal scope |
|---|---|
| `numerator_coefficient`, `alternating_coefficient` | Extract each coefficient of the actual descending-power numerator and geometric quotient, with the index range explicit. |
| `alternating_factorization` | The full geometric polynomial identity `S_p(X)(X-4)=X^p-4^p`. |
| `numerator_of_quotient_divides` | Divisibility by the degree-`p-1` geometric quotient forces the quotient to be the constant `2^(d 0)`; degree and nonzero facts are proved. |
| `exponents_of_alternating_quotient`, `phase_of_alternating_quotient` | Coefficient equality forces `d i=d 0+2*i`; the last-position bound forces `d 0<=1`. |
| `numerator_positive`, `principal_factor_survives` | The actual numerator is positive at a positive real number. An irreducible factor with a positive real root survives in `F_0` under the exact factor/divisibility hypotheses. **Irreducibility is an explicit premise of this generic theorem.** |
| `quotient_of_linear_residual`, `alternating_profile_of_linear_residual` | The exact linear residual identity forces the geometric quotient and hence the whole alternating profile, including both phases. |
| `alternating_evaluation`, `ordinary_realizer_of_linear_residual` | Evaluate at three; the actual affine fixed-point equation then forces the natural source to be 1 or 2. |

The finite numerator is

\[
Q(X)=\sum_{i<p}2^{d_i}X^{p-1-i}\in\mathbb Q[X].
\]

The integer factor normalization, irreducibility of `X^b-2^a`, and the
complex-root equality argument taking `|F_0(3)|=1` to `F_0=X-4` are
written proofs in `RESIDUAL_UNIT_EXCLUSION.md`. They have independent
mathematical reviews, but are not claimed as Lean theorems. The written
primitive residual-degree result is also outside the formal module.

The final formal theorem assumes the necessary actual cycle equation
`(4^p-3^p)n=Q(3)`. It proves `n=1 or n=2`; it does not assume or prove
an unrestricted Collatz convergence assertion. The direct shortcut
transitions identify those two values with the trivial cycle.

## DistinctWordBudget.lean: nine public declarations

| Declarations | Exact formal scope |
|---|---|
| `choose_prefix_sum`, `weighted_choose_sum`, `squared_weighted_choose_sum` | The ordinary and two weighted hockey-stick identities for all natural parameters, including empty ranges. |
| `histogram_deficit_le`, `histogram_squared_deficit_le` | A finite distinct-word histogram satisfying the explicit binomial capacity bound obeys the first and second deficit budgets. |
| `histogram_cost_budget`, `mean_cost_budget`, `count_le_choose_of_mean` | Convert a finite histogram's mean-cost bound to the stated binomial upper count. |
| `finite_collision_budget` | For the **given** finite probability law, its mean cost and squared-deficit capacity imply the Cauchy collision inequality. The masses, normalization, capacity and nonnegative margin are all explicit. |

The proof does not formalize the stars-and-bars identification of the
histogram with all positive words, the Collatz affine word-to-residue
map, Stirling's asymptotic, or the ordinary harmonic-flow construction.
Those applications are written out in `COLLISION_LOGARITHMIC_GAIN.md`.
The old window-count lemma is a pinned written dependency; its entire
module is neither imported nor recompiled here.

The collision theorem is about order-two collision entropy. It does not
claim the same logarithmic improvement for Shannon entropy. The
all-clock inverse-law conclusion retains the original qualified
harmonic-flow input; the actual-orbit finite collision bound and the
bounded-height duration theorem do not need that input.

## Evidence levels

`check.py` copies the exact two sources to an external empty directory,
compiles them with warnings treated as errors, checks the complete set of
21 public axiom reports, and rejects unfinished proofs, custom axioms and
native proof mechanisms. The permitted foundational axiom names are
`propext`, `Classical.choice`, and `Quot.sound`.

The three Python certificates use exact integer/rational arithmetic and
explicit checks that remain active under `python -O`. They support the
factor-growth logarithmic-form certificate, the rational control family's
finite replay, and the finite orbit/word indexing. They are not finite
search evidence for the full theorem. The infinite factor-growth root-gap
coverage retains its explicitly cited Matveev and continued-fraction
inputs; it is not a Lean proof.

The clean-checkout repository gate checks integrity, not mathematical
truth. Exact source hashes, compiler outputs and replay results are
recorded separately in the published report.
