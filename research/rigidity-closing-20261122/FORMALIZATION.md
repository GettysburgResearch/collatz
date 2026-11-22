# Formalization and dependency boundary

## New Lean theorems

`lean/CanonicalRetracing.lean` contains eight new public theorems. Its
inputs are a real sequence `v`, monotonicity, a positive initial value,
and the indicated finite or uniform upper bound `C`.

| Theorems | Kernel-checked statement |
|---|---|
| `sum_increments`, `window_capacity_sum_le` | Finite telescoping and the multiplicity bound for overlapping windows. |
| `capacity_ratio_failure_le`, `retracing_failure_sum_le`, `retracing_failure_mean_le` | The exact scalar upper bound on the sum/mean of `1-v_k/v_(k+r)`. |
| `tail_retracing_failure_le`, `linear_window_failure_le` | The lower capacity floor controls the failure ratio at every stated clock. |
| `uniform_shift_failure_mean_le` | The average failure is at most `1-sum(v_j)/(C(M+1))`, uniformly for every shift `r`. |

The one local theorem dependency is the existing
`CollatzOriginalEntropy.sliding_window_cost_le`, imported from the
byte-pinned `OriginalSourceEntropy` module in the preceding packet. Its
complete module has 21 audited public theorems. Recompilation of that
module is dependency validation, not 21 additional new results.

`lean/CyclotomicBlockExclusion.lean` contains ten new public theorems:

| Theorems | Kernel-checked statement |
|---|---|
| `complete_denominator_factorization`, `integer_bezout_805` | Exact integer polynomial identities, including signs and the constant 805. |
| `residual_coprime`, `reduced_divisibility` | Coprimality cancels the factor `s^14` in the Bezout consequence. |
| `residual_lower_bound`, `residual_exceeds_805` | For integer `s>t>=3`, the residual denominator exceeds `805t`. |
| `residual_nondivisibility`, `common_factor_pos`, `complete_nondivisibility` | The complete factorized numerator cannot be divisible by the complete denominator for coprime `s,t`, `0<u<t`. |
| `twelve_block_power_nondivisibility` | Specialization to `s=2^a`, `t=3^b`, `u=2^b`, for `b>0` and `2^a>3^b`. |

The cycle specialization assumes **no** general Collatz theorem or cycle
exclusion. Its algebraic assumptions are slightly weaker than the
conditions needed to construct the actual twelve-block words. The
word-to-polynomial identity, legality, and primitivity for `a-b>=2` are
proved in the written note and independently reviewed; they are not
claimed as Lean declarations.

## Written mathematical deductions

The full-path probability, exact ordinary endpoint total variation,
`sup_r` identity, Cesaro limit, finite-alphabet entropy continuity, and
all-shifts entropy ceiling are written probability arguments. The
finite scalar ratios underneath them are formalized, but the Lean file
does not construct the Markov kernel or prove those measure-theoretic
interpretations.

The ordinary harmonic flow and its boundedness are explicit imported
analytic inputs, preserving the source qualifications of the preceding
packet. The actual-orbit finite entropy inequality comes from that
packet's separate elementary proof. No unproved entropy lower bound,
independent-gap model, Feller property, or root-uniform onset is imported.

The full-denominator algebraic lift, polynomial-gcd family with
subexponential residual size, wrong-conjugate resultant example, and
rotation identities are written mathematical arguments with exact finite
controls. Only the twelve-block divisibility exclusion's integer algebra
is formalized in the new cycle module.

## Executed evidence

`check.py` demands a clean complete checkout, exact Lean and Mathlib
revisions, byte-pinned module inputs, a complete expected theorem/audit
set, and immutable source copies. It rebuilds the one real inherited
module and the two new modules outside the checkout. The 18 new theorem
audits and 21 inherited audits are reported separately.

The allowlist of kernel axioms is `propext`, `Classical.choice`, and
`Quot.sound`. The checker rejects admitted proofs, added custom axioms,
native proof shortcuts, unlisted local imports, and incomplete audit
sets. This establishes only the statements actually compiled.

The two small certificate scripts test exact polynomial arithmetic,
ordinary-source realization, the targeted norm obstruction, and damaged
controls. Both run normally and with `python -O`; no assertion is used
as a required validation gate. There is no broad cycle census. The
all-parameter arguments do not follow by extrapolating finite outputs.

The default repository gate is also run. Repository integrity does not
certify the written mathematics or the external literature. The actual
published-checkout command logs and receipt are stored in the accompanying
report after execution; no successful run is inferred merely from this
workflow description.
