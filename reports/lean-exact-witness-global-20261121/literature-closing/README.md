# Checkpoint thirteen: S-unit returns and canonical run weights

Date: 22 November 2026. Owned parent:
`431d858d1ac92e88f4a58f6610c0d67733dc7242`, PR177.

## Mathematical result and proof boundary

The main written result is in the scientific packet's
`LITERATURE_ARITHMETIC_RETURN.md`. The published Evertse--Schlickewei--Schmidt
Theorem 1.1 supplies a finite set of projective ratios in each fixed arity.
It is applied twice with different quantifiers: endpoint-only arity at most
`4S` gives one fixed finite exceptional separation set; full arity at most
`4S+h` gives a correction-ratio floor for each fixed separation. This proves
an actual finite-core return and then upper Banach density zero of bounded
binary-run times on every escaping odd orbit.

This deep theorem and the density proof are written mathematics. They are
not Lean declarations. No external S-unit assumption is installed as a Lean
axiom. The ordinary-orbit result uses the published theorem directly; its
separate application to the canonical energy retains the imported analytic
construction's predecessor-population and envelope qualifications.

The new core-Lean modules prove:

- `ArithmeticPrecision`: eight public theorems retaining every ordinary
  clock, the complete affine correction, and the actual later odd core.
- `AffineBlockPrecision`: thirteen public theorems for arbitrary actual
  blocks and exact dyadic valuation loss under repetition. The possible
  fixed-point exception is explicit.
- `SegmentFloor`: eleven public theorems. The sharp finite bound is
  `M*C + 3^h*n <= 4^h*n`. The final theorem converts
  `3^h*n <= Q*C` into an actual return below `Q*2^h` before the supplied
  ordinary segment ends, without a gap-size restriction.

`LITERATURE_CANONICAL_ENERGY.md` additionally proves a finite absolute edge
variation bound for the actual canonical potential. The S-unit result makes
every exponential run weight detect escape; an interval of those weights
has finite canonical forcing. Equations (45)--(49) keep the remaining
multiplication/transport commutator and weighted boundary drift explicitly.
No sufficient uniform upper bound is established. Nontrivial positive
cycles and `FloorIntervalStep` remain unresolved.

## Mathematical review performed in this pass

The main agent checked the exact signed-endpoint representation, minimal
zero-subset argument, rank `2*(arity-1)`, and the two different finiteness
quantifiers against the primary ESS paper. The analytic and termination
agents independently checked the same argument and the uniform sliding-window
packing step. This is internal mathematical review, not external peer review.
The arithmetic agent reviewed the separate finite-return Lean module and
the distinction between its ordinary-clock witness and the written odd-input
return theorem. The main agent also checked the one-charge side-current
telescope, killed-edge contribution, explicit sector test, fixed-anchor
energy lower bound, finite subcritical forcing, and the finite-Green
commutator identity.

The cited termination and recurrence machinery was tested against its actual
hypotheses. The packet does not replace failure of one proposed application
with a claim that the full theorem is impossible.

## Execution scope

`checkpoint-thirteen.json` records the exact runtime, commands, source
hashes, axiom audit, and written-artifact hashes. It uses checkpoint twelve's
receipt as the baseline and hash-checks every unchanged preexisting Lean
source except the two intentionally extended aggregate files.

The aggregate build is incremental. Each of the three new modules is also
strictly recompiled with warnings treated as errors. The expanded aggregate
axiom audit is executed anew. This does not claim a fresh rebuild of all
unchanged mathematical dependencies.

A separate complete clean-checkout integrity/regression gate is run after
the local commit and before publication. The checked commit/tree, receipt
digest, remote commit, and exact remote tree comparison are recorded in the
PR. That gate checks repository integrity; it does not independently verify
the written S-unit or infinite analytic proofs.

`SOURCES.json` pins the newly inspected source files and primary literature.
No existing external branch is merged, and no default-branch update is made.
