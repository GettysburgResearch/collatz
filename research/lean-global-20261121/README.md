# Lean global attack: ordinary certificates and complete closing obligations

**Checkpoint 1. Full Collatz convergence is OPEN.** This is an active attempt
to complete a proof, using Lean 4.34.1 with no Mathlib dependency. Existing
reductions are reused with exact attribution; new proof work begins at
`CollatzGlobal/OrbitLift.lean`. No open conjecture is introduced as an axiom.

The shortcut map is `n/2` on even naturals and `(3*n+1)/2` on odd naturals.
`CollatzReverseBasin.Basin n` means that an actual finite shortcut orbit
from `n` reaches one. The global goal is `forall n, 0 < n -> Basin n`.

## New kernel-checked ordinary bridge

Let `s_t(n)` count the odd inputs in the first `t` shortcut steps. For all
natural `n,t,q`, the new module proves simultaneously

\[
 T^t(n+2^tq)=T^t(n)+3^{s_t(n)}q,
 \qquad s_t(n+2^tq)=s_t(n).
\]

It then proves exact basin equivalence on every ordinary lift. For a
balanced five-return (equal odd counts on both arms and an endpoint ratio
of five), the return and the actual failure label
`Basin n and not Basin (5*n)` transport across the whole cylinder. The
statements concern actual natural-number trajectories for every parameter,
with no almost-everywhere or completed-source substitution.

Principal new names in namespace `CollatzGlobal`:

- `high_bit_lift` and `basin_high_bit_lift`;
- `balanced_five_lift`;
- `five_failure_return` and `five_failure_cylinder`.

This supplies a reusable formal bridge for whole-source certificate
construction. It does not assert that an arbitrary ordinary input has a
balanced return.

## Full-proof work in progress

The active attacks are a total normalization of supplied source
certificates by their first-hit clock; an unbounded, fully formal return
family; and a separate attempt to force the residual ordinary inputs by
the latest interval and affine-section results. They are targets here,
not claims already proved in this checkpoint.

The imported PR174 project proves the equivalence between full Collatz
and one precisely named psi-closure statement. That statement remains a
hypothesis of its conditional theorem. The current work does not mistake
that equivalence for a proof of the hypothesis.

## Build and audit

From the `lean` subdirectory, with Lean 4.34.1 installed:

```sh
lake build
lake env lean -DwarningAsError=true CheckpointAudit.lean
```

The audit prints the logical dependencies of the new results and the
inherited global reduction. No new axiom, `sorry`, `admit`, or native
decision shortcut is part of the proof source. Actual checkpoint build
receipts and exact heads are recorded in the publishing PR.

See [SOURCES.md](SOURCES.md) for the latest source snapshot and the precise
reuse boundary. This packet is exploratory; kernel checking establishes
the formal statements as written, not every informal claim in a source PR.
