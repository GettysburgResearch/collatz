# Review of the direct closing attempts

Base checkout: `9b02334f27ff59694a91fe7f018e0aaabad7620b` (PR182).
Research packet: `research/central-closure-20261124/`.

## Outcome

The universal Collatz obligation is still open. No cycle-exclusion theorem,
universal return selector, or successful fixed-source contradiction is
claimed. This checkpoint preserves direct attempts to construct those
objects and the first exact inferences that failed.

Three GPT-6.2 Astra agents were assigned the ordinary minimum, global rank,
and integrality routes. The coordinating agent continued each past its
initial failure: source-dependent inverse budgets, infinite and nonlinear
rank corrections, and moving dimension/positive integer summands. Agents
then cross-reviewed the written calculations. These are model-assisted
mathematical reviews, not independent human referee acceptance.

## Reconstructed claims

1. **Original floor and level minima — VERIFIED as written.** The finite
   hull uses the strong-induction hypothesis only for smaller starts. A hit
   of a target at least q occurs before their first visit to one. Acyclic
   levels are well-defined; cyclic levels are only modulo the period. The
   positive quarter predecessor has the same next odd value and preserves
   the mark. It therefore excludes high valuations at an ordinary level
   minimum, rather than forcing criticality. The argument does not force
   the original source to meet the finite hull.
2. **Rank attempt — VERIFIED WITH SCOPE CORRECTIONS.** The coordinating
   agent derived the entire family y=512t+91, z=576t+103, and its seven
   literal shortcut transitions. The source valuation is exactly five;
   the destination is 6+v2(11t+2). The CRT/majorant proof of atomic weight
   propagation is valid under the explicit finite logarithmic moment.
   The nonlinear envelope identity requires positive odd inputs. The
   root-center example disproves a uniform inequality at every center,
   not an inequality limited to actual maximizers or the entire restricted
   supremum. Both restrictions were incorporated before publication.
3. **Moving cuts — VERIFIED WITH SCOPE CORRECTIONS.** The exact raw
   product, normalized product, primitive gcd and source-height bound
   were reconstructed. The actual vector's stencil indices are 1 through
   m-2. The unit-gap count uses q_m>=1, avoiding an unjustified all-time
   comparison with q_0. The cited large-height quantitative theorem is
   outside the dimension/height range. The exceptional hyperplanes are
   explicit and independent; their existence yields no contradiction.
4. **Integer summands — VERIFIED, SOURCE-QUALIFIED.** The generating
   congruence gives exact gap-one rising blocks and a two-summand start.
   Parity rules out every vanishing subsum in the fixed-rank equation.
   The external unit-equation finiteness theorem then leaves only finitely
   many exponents for each fixed j,t. The source varies with block length
   and summand threshold. Fixed-source asymptotic tightness remains open.

The rank author cross-checked the integrality arguments against the primary
papers; the integrality author checked the rank's CRT, dominated convergence,
gcd and height formulas. The ordinary-minimum author independently checked
the odd-input domain and the restricted-tree limitation. All three then
read the revised relevant packet files. Their final reviews requested only
the explicit wording that the log-height difference **divided by m** tends
to zero, which was corrected.

## Lean boundary

The initial draft compile exposed an unexpanded conditional and a missing
decidability reduction in two finite proofs. Both were repaired. The final
source was compiled successfully and then replayed from a fresh private
directory with the pinned Lean 4.34.1 and Mathlib listed in `SOURCES.json`.
`LEAN_REPLAY.json` contains the actual command, outputs, source hash, compiled
object hash and audits of all ten named declarations, with warnings treated
as errors. Only standard Lean axioms are permitted by the replay script.

Lean checks the finite algebra and ordinary diagnostic family. It does not
check the infinite atomic-weight argument, the rational supremum theorem,
the level-minimum argument, or either Diophantine argument. None of the
audited declarations states the Collatz conjecture.

## Publication evidence

`SOURCE_MANIFEST.json` binds the reviewed research sources and this report
to hashes. The complete-checkout default validator is run on the exact
commit after creating its Git object and before advancing the remote branch.
Its exact-head receipt is recorded in the PR body, avoiding a self-referential
commit-hash receipt. GitHub's branch ref and the published packet source
are read back after the update. These checks are publication/integrity
evidence, distinct from the mathematical reviews and Lean scope above.
