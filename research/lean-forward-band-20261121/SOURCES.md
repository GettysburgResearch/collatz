# Source pins and evidence boundaries

## Ordinary forward section

- Repository: `GettysburgResearch/collatz`, PR173.
- Frozen head: `fa0c9e2a2851e6324391e39c17afcb5913185aec`.
- Original path: `research/lean-shell-cover/`.
- Verbatim imported modules: `ShellCover.lean`, `ForwardSection.lean`,
  `SectionDynamics.lean`, `RisingReturns.lean`.
- Exact interfaces used: ordinary `step`, `orbit`, `Hits`, `Basin`,
  `basin_at_hit`; the `Marked` predicate, bounded visit, and actual positive
  return definitions.
- Scope: these sources prove band visitation, density-zero counting, and
  arbitrarily expanding first returns. They do not supply global return
  descent.

The new modules retain the same namespace and exact map, so their adapters
use the imported definitions directly. Source hashes are recorded in the
replay report; `upstream-pins.json` records comparison with the frozen commit.

## Selected-density interface

- Repository: `GettysburgResearch/collatz`, PR180.
- Frozen preceding head: `f87cb69b3dd86257731ddfbab58c87bf3b5f63d6`.
- Path: `research/lean-ordinary-closure-20261121/LINEAR_BLOCK_ATOM_FLOOR.md`.
- Invoked results: weighted residue counting (WC); retained-prefix bounds;
  a positive cylinder for the smoothed selected densities; exact affine
  word normalization and concatenation.
- [Pinned parent proof](https://github.com/GettysburgResearch/collatz/blob/f87cb69b3dd86257731ddfbab58c87bf3b5f63d6/research/lean-ordinary-closure-20261121/LINEAR_BLOCK_ATOM_FLOOR.md).

The parent note attributes the selected-density strategy and weighted
counting device to Naoufal El Jaouhari, DOI `10.5281/zenodo.23377671`, located
in the attributed exposition at rStation paper 10, version 2. That attribution
is retained. The present extension develops controlled floors at all large
depths and their placement in the actual shrinking forward section. It does
not claim priority for the parent strategy or import its neighboring
joint-mixing claims.

## Published analytic input

Terence Tao, *Almost all orbits of the Collatz map attain almost bounded
values*, Forum of Mathematics, Pi 10 (2022), e12,
[DOI 10.1017/fmp.2022.8](https://doi.org/10.1017/fmp.2022.8),
Proposition 1.14, equations (1.26)--(1.27).

Under the parent note's full-Haar normalization this supplies

\[
\|D_n-\operatorname{lift}D_m\|_1\le C_A m^{-A}
\qquad(1\le m\le n).
\]

The root checked the published statement and its oscillation normalization
for this packet. The input concerns the offset law, not a joint law
conditioned on the total exponent. The new proof uses unconditioned
subdensity truncation and an operator bound, then a finite pigeonhole step.

## Formalization boundary

The population theorem and its unit-source refinement are written analytic
proofs with a separate independent review. They have not been translated to
Lean. `BandPopulationCriterion.lean` therefore takes `DenseBandFans` as a
named hypothesis; no axiom states that predicate.

The exact clock-compression, marked-family component descent, restoration,
and carry identities are unconditional Lean theorems. Their scope is their
stated identities and implications, not universal Collatz convergence.

The first missing global estimate is the unconditional cubic survivor
bound in the README. The alternative universal clock-saving selector and
the carry-reset repayment bound are also open.
