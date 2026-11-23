# Formal scope of checkpoint 17

The new Lean module is `lean/TriadicCertificateRigidity.lean`. It imports
the unchanged checkpoint-16 `TriadicAmortizedBudget.lean`, which imports
the unchanged PR178 paired-state module `TriadicDualClosure.lean`.
Dependency hashes and origins are recorded in `SOURCES.json` and enforced
by `verify_candidate_rigidity.py`.

## New formal conclusions

For one fixed positive ordinary n and one signed triadic representation
`a/3^r`, the same finite compatibility premise as checkpoint 16 proves:

1. A literal paired-state hit with original coordinate one and represented
   candidate value two by `8*binaryBudget n a r`.
2. Compatibility at every subsequent natural clock for that same
   deterministic paired trajectory.
3. Equivalence between the first `9*binaryBudget n a r+1` tests and all
   tests.

The budget, denominator bounds, initial two-test estimate for n=1,
zero-numerator exclusion, terminal-defect divisibility, defect size bound,
and exact-cycle invariant are all discharged in Lean. There is no
all-time compatibility hypothesis in the forward implications, and no
universal construction supplied as an axiom.

`RIGIDITY_THEOREMS.json` enumerates every declaration: 15 theorems and two
definitions. `TriadicCertificateRigidityAudit.lean` prints the axioms of
all 17. The allowed union is `propext`, `Classical.choice`, and
`Quot.sound`; no admission, custom axiom, or native proof shortcut occurs.

## Written statements, not new formal declarations

The following are proved or discussed in the written notes only:

- Identifying the accepted rational with the 2-adic autoconjugacy value,
  and uniqueness across different accepted representations.
- The reduced denominator count `r_*=b_tau-1`, its logarithmic first-hit
  bound, and the exact negative-to-positive crossing classification.
- The prior complete-carry congruence implication to finite compatibility.
- The all-target finite lifting and positive-sector reset normalization.
- The fixed-source simultaneous linear-form product, conditional Haar
  joint-limit theorem, mixed-phase collision identity, and universal
  rational-cycle Sidon construction.

Those statements are not certified merely by compiling the new module.
Their separate reconstructed proofs and exact finite controls are linked
from the report. The numerical controls do not prove universal convergence.
