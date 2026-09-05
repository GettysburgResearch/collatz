# Exceptional mass, coefficient counts, and fixed-height descent

**Resident reference assembly of independently reviewed components.** This page supplies orientation, not a new accepted synthesis. Exact proof bodies are local and unaltered; use the claim-level verdicts in [A's matrix](../../../reports/prepublic-2026-09-05/reviewer-a/CLAIM_MATRIX.md) and [B's matrix](../../../reports/prepublic-2026-09-05/reviewer-b/CLAIM_MATRIX.md). Review A is pinned at `0137620b92afb714c19272017dbbc626d12af1ac`; B at `ea5faf5bcdd49a693e450dc0eeda83ace807f2f3`. [Conventions](../CONVENTIONS.md) fix maps, clocks and evidence boundaries.

## What survives review

A sufficiently strong upper bound for **actual eternal survivors at one certified floor**, combined with the explicitly assumed predecessor lower bound, gives a Collatz contradiction. The local exponent-race and critical-endpoint implications are reviewed; the needed survivor upper bound is not supplied. The external predecessor theorem remains **EXTERNAL SOURCE-QUALIFIED**: its stronger endpoint is `c_b X^0.901` with a positive target-dependent constant and cutoff; the unit-coefficient endpoint is 0.90. No local Lean build or large external payload replay is asserted.

Coefficient-supercritical starts, native-horizon no-descent roots, global forward minima, and all eternal survivor starts are four different populations. The reviewed entropy/no-descent estimates concern the first three, not an uncontrolled predecessor basin. In particular the native no-descent bound is `6499+2 X^(19/20)` in its stated range, while the entropy exponent is `h_2(log(2)/log(3))`. Thinness is not emptiness.

| Read the exact proof | Reviewed components and boundary |
|---|---|
| [External dossier](../../external/mazur-2026/README.md) | Faithful source-qualified statements, source/release pins and attribution; imported density does not imply fixed-floor convergence. |
| [Endpoint-one and entropy attack](../../external/mazur-2026/fixed-height-power-saving-attack.md) | A: RA-010–015. Counts, entropy and conditional recurrence algebra; the actual contraction is OPEN. |
| [Native no-descent and fiber barrier](../../external/mazur-2026/fixed-height-forward-power-saving.md) | A: RA-017–023, RA-076. MZ-FH-001–004 survive; the unrestricted timed endpoint in MZ-FH-005 is not accepted. See [errata](../ERRATA.md). |
| [Critical mass and killed Green criteria](../../astra-critical-mass/PROOF.md) | A: RA-024–030. The critical count/weighted-mass criteria retain P(gamma); the local killed-weight criterion does not need the external theorem. |
| [Complete first-passage fibers](../../astra-critical-mass/FIRST_PASSAGE.md) | A: RA-031. Exact AP integrality, all survival prefixes, endpoint interval `(Y/2,Y]` and unresolved-source mass; no extra mixing follows. |
| [Mellin transfer and finite inverse cones](../../astra-three-routes/ROUTE1_MELLIN.md) | B: T-A3-101–103. Exact killed identities and analytic infinite-source tails at finite times. The all-time survivor bias is OPEN. |
| [Signed ordinary boundary charge](../../astra-three-routes/pass3/BOUNDARY_CHARGE.md) | B: T-A3-601–603. Actual ordinary roots and signed terms are essential. A floor growing with time is not one fixed floor. |

## Proof-bearing limits and preserved failures

The local criterion `Lw<w` needs a strictly positive summable weight on the killed state space; such a global weight is not constructed. The finite all-source enclosure `8.6140<G_256<8.9619` is independently supported by A's narrower reconstruction, but it is not a uniform bound over K. Its source-tail estimate cannot be held fixed as K grows.

The all-subset positive fiber-saving premise is refuted by mass conservation; a dynamically surviving subset may still admit a saving. B separately refutes the uniform one-third Mellin ceiling using a complete finite cone and certified tails. Neither failure is a proof of a divergent ordinary orbit.

## Evidence and next missing lemma

A's complete PR90 encoded corpora remain source-reported unless separately replayed; the narrower independent checks are recorded individually. B did not rerun the large first-pass cone. The PR88 finite checker has a [nonmutating replay](../../external/mazur-2026/check_fixed_height_forward.py), with its own report name. [Replay policy](../../../docs/REPLAY_POLICY.md) distinguishes every evidence tier.

The next obligation is a survivor-specific pullback gain or an actual fixed-floor mass estimate that survives repeated transport. See [open obligations](../../open-obligations/README.md). No SC*, FC*, cycle exclusion, or full Collatz status is promoted.
