# Execution and independent review record

This record accompanies the [AYH research packet](../../research/ayh-resource-reset-20261124/README.md). The packet is a proposed research contribution. Collatz remains open. The verification events below concern the stated narrow theorems and finite controls, not universal termination.

## Lean build actually executed

The publishing agent ran the packet's `check_lean.sh` with Lean **4.34.1** (compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`) and a built Mathlib checkout at **`d13f23b723b8a846827a245b89c10fc7d3f11612`**. The command exited **0**. Each module was compiled into fresh temporary storage, with one worker and `-DwarningAsError=true`.

The ten compiled modules were `SelfEmbedding`, `MixedBaseRigidity`, `PolynomialPump`, `PositivePolynomialBarrier`, `CarryTrace`, the three byte-identical upstream modules `ShellCover`, `ForwardSection`, `OffsetDescent`, and the two new modules `MarkedCylinders`, `InversePowerRows`. The temporary output directory was removed after the run. No pre-existing compiled copy of a new module was used.

The final audit explicitly queried **29 new public theorem declarations**. Every printed dependency was among `propext`, `Classical.choice`, and `Quot.sound`; some certificates used no axioms. There was no `sorryAx` or project-specific axiom in those reports. The [complete compiler output](lean-build.log) also includes audit messages emitted while compiling supporting sources. Its repeated names are not additional theorems.

The main theorem boundaries are:

| Declaration or family | Checked scope |
|---|---|
| `PositivePolynomialBarrier.no_strict_rule` | All eleven forward AYH rules, positive integer triples, distinguished-coordinate order, arbitrary nonnegative polynomial binary-zero map; other symbols preserve both comparisons. |
| `AYHSelfEmbedding` | Literal 29- and 32-step all-rule traces, a generic extensive-algebra obstruction, and the contextual zero-stutter implication. |
| `MixedBaseRigidity` | Strictly increasing scalar maps, both word orientations, collapse of the five digit maps. |
| `CarryTrace` | Natural-matrix carry aggregation, trace vanishing, and zero carry defects on returning digit paths. |
| `cofinal_marked_power_predecessors` | For every fixed positive target not divisible by three and every bound, an actual marked predecessor above that bound, with the checked power estimate and a physical continuation to the same target. |
| `universal_iff_marked_power` | Closed equivalence between universal ordinary convergence and convergence on the specified marked power-descent section. |
| Other `MarkedCylinders` declarations | Arithmetic cylinder gluing, section closure from inverse rows, and the inverse power-cost inequality. |

The [source manifest](source-hashes.json) authenticates the delivered research files. The vendored upstream file identities and exact source commits are also recorded in the positive-section README and `SOURCES.json`.

## Independent internal reviews

The agent who developed the scalar approach independently reconstructed the other agents' main arguments. These are internal mathematical reviews, with exact source hashes, rather than external peer-review acceptance:

- [Polynomial and trace review](POLYNOMIAL_TRACE_REVIEW.md): positive-coordinate dependence argument, literal rule uses, ordered-algebra linkage, and compilation of the exact reviewed sources.
- [Positive ordinary-section review](POSITIVE_SECTION_REVIEW.md): rotation estimates, same-target arithmetic realization, physical clocks, cofinal quantifiers, and the missing smaller-source step.
- [Zero-coordinate extension review](ZERO_FACE_REVIEW.md): support-mask dynamics, eventual two-step comparison, and independent replay of the 308-step all-rule witness. This extension is a written proof, **not** part of the positive-orthant Lean theorem.

The final publication review corrected two prose overstatements: the prefix-length guarantee is in shortcut clocks, with up to two bits of numerator overhead; and the two-base rank obstruction requires weak decrease at every step in addition to strict decrease on one parity.

## Exact finite controls actually executed

[Finite command receipts](finite-checks.json) record six successful executions: each of `check_rewrite_certificates.py`, `monomial_transfer.py`, and `check_zero_faces.py` ran under both normal Python and `python -O`. Each normal/optimized pair produced identical stdout. The checkers use explicit failure conditions for their acceptance checks.

The first checker replays the 27-to-107 and 41-to-161 traces, all eleven rule occurrences, physical values, administrative value preservation, reversed literal traces, and the required endpoint comparisons. Its JSON is also retained as [rewrite-replay.json](rewrite-replay.json). The monomial compiler checks exact prime-charge transfer, nonlinear exponents, a constant reset, multiplicative equality, round-trip orientation, a rejected false orientation, and the boundary-reset matrix counterexample.

The zero-face checker verifies the three larger witnesses, including their decoded integer value after every rewrite: 515 to 2051 in 308 rewrites and 52 shortcut steps; 259 to 2051 in 306 rewrites and 51 shortcut steps; 1042601 to 8906921 in 150 rewrites and 8 shortcut steps. Each uses all eleven rules. It also enumerates the 36 monotone maps on the Boolean square, with maximum transient length two. The written proof uses the weaker bound three.

The ordinary-section checker was separately run in normal Python and exited 0. Its retained [marked-replay.json](marked-replay.json) covers eight targets and three rational-rotation denominators, giving **24 rows, 8,216 entries and 728 marked predecessors**. Each marked predecessor was checked against its original supplied target and the fifth-power inequality. These finite checks supplement the all-quantified Lean proof; they do not establish it by enumeration.

## Written and external results

The whole-nonnegative-orthant dimension-three extension, the positive-orthant extension through dimension five, reversed polynomial presentation, general monomial-to-affine equivalence, digit-defect nilpotence consequences, octave counting bound, and full arbitrary-fixed-suffix extension remain written results. Some have exact finite controls or separately formalized ingredients. They are not advertised as completed Lean theorems.

The source-qualified two-base rank argument invokes Bell's published regular-sequence theorem. Nashida's pinned natural/arctic barrier development was inspected at its primary source but **was not rebuilt**. Neither external result is a dependency of the new polynomial or sparse-section Lean theorem.

The wider repository's earlier proof corpus was not replayed by this pass. A repository-integrity validation checks preservation and structure, not the mathematics in every branch. The exact complete-checkout receipt is recorded separately after the content commit.
