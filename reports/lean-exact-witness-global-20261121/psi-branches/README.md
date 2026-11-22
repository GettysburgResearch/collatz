# Checkpoint nine: complete psi valuation branches

This continuation follows published checkpoint eight at
`2efabba9a341839b67ed011d6b878b23730ee51d`. Its scientific statements are
in the [research packet](../../../research/lean-exact-witness-global-20261121/README.md).
Full Collatz and the original residue implication remain OPEN.

The three new modules prove all odd-initial-exponent psi steps and the
complete initial-exponent-two cases with first odd gap two or four. Every
step uses the original lower-rank interval induction hypothesis. The
remaining normalized psi head is three at initial exponent two. This does
not supply complete coverage for arbitrary non-psi interval targets.

`checkpoint-nine.json` pins all 34 Lean source files by SHA-256. Their bytes
exactly match the source inputs of a new build directory with no previous
`.lake` outputs. The recorded build passed 34 jobs. The expanded audit
checks 141 declarations with warnings treated as errors. All dependencies
are subsets of `propext`, `Classical.choice`, and `Quot.sound`, or empty;
there is no `sorryAx` or conjectural axiom.

The actual logs are `checkpoint-nine-build.txt` and
`checkpoint-nine-axioms.txt`. The three modules add eleven public proved
declarations; the existing analytic paper deductions retain their previous
evidence boundaries.

`head-three-rank-witness.json` records a separate exact finite identity
check: complete odd source paths for 205, 77, and 173, the ordinary merger
of 1639 and 1383 at clocks ten and five, and the increase in the highest
changed source grade. Its general ternary-class context is proved
algebraically in `PSI_HEAD_THREE_FRONTIER.md`. This witness is not a search
cutoff or a counterexample to Collatz.

The complete clean-checkout integrity/regression gate is run separately on
the final committed tree. PR177 records the actual checked commit and tree,
the non-forced remote publication, and the matching remote tree. No new
finite verification cutoff is used as mathematical evidence for these
unbounded theorems.
