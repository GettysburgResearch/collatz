# Ordinary sources, inverse equilibrium, and same-depth comparison

This packet continues the full-problem investigation from the [previous six-hour proposal](../astra-six-hour-20261127/FINAL_PROPOSAL.md). The present session began on 27 November 2026 at 11:36:06 UTC and is allocated six hours. **The second checkpoint does not prove Collatz.** It supplies new exact structures and written arguments aimed at the missing ordinary-source estimate, with finite Lean kernels and explicit distinctions between those kernels and the infinite arguments. Research continues during checkpoint publication.

## Second checkpoint: the current closing proposal

For one hypothetical escaping ordinary ray `a_j=U^j(a)`, the [critical sibling identity](global/CRITICAL_SIBLING_SCENERY.md) proves summability of the same-depth side/trunk ratios

\[
 \sum_j \frac{\rho_j(s(a_j))}{\rho_j(a_j)}<\infty,
\]

where `rho_j` is the original mean-one ternary density and `s(y)` is the ternary unit among the true siblings `4y+1` and `16y+5`. This retains one fixed positive integer source, both physical clocks, and the exact original measure. A lower bound as weak as `c_a/(j log(j+2))` would contradict this identity. The [nonlinear proposal](operator/SIBLING_COMPARISON_PROPOSAL.md) instead asks for the stronger uniform estimate

\[
                \rho_j(s(y))\ge c\,\rho_j(y)^2/y.
\]

The estimate is **unproved**. Its conditional finite-duration consequence is a reciprocal/Riccati bound checked in Lean. The cycle consequence additionally retains effective constants and a finite remaining-range obligation. The exploratory floating-point probe through depth 16 limits a possible constant but does not establish one.

The [first-power transfer theorem](escape/FIRST_POWER_HAAR.md) uses the cited fixed-total localization input to prove uniqueness of positive product-Haar entrance laws. The [ordinary ancestor theorem](escape/ORDINARY_ANCESTOR_EQUILIBRIUM.md) then gives individual-depth local equilibrium for the actual positive ancestors of each fixed integer, and at moving targets for any depth overshoot tending to infinity. The [marked theorem](escape/CORRECTED_PHASE.md) keeps the corrected real-height distribution, independent of the two local Haar coordinates. At zero overshoot the source measure is atomic; these results do not supply the proposed same-depth lower comparison.

The arithmetic attack adds exact [pinned rivals](arithmetic/PINNED_RIVALS.md) and a proposed [all-horizon ordinary rival-density theorem](arithmetic/ALL_HORIZON_RIVAL_DENSITY.md). Its power-saving shell estimate covers arbitrarily late smaller ancestors at a specified endpoint. It also shows that both inverse floors can hold for a positive density of ordinary sources in every fixed binary class. This is a constraint on a finite-word exclusion strategy, not a class of counterexamples: it does not impose the same floors at every future phase.

## The full-problem target

Let `U` be the actual accelerated map on positive odd integers. Put

\[
 \rho_1(x)=\begin{cases}0&x\equiv0\pmod3,\\1&x\equiv1\pmod3,\\2&x\equiv2\pmod3,
 \end{cases}\qquad
 R_j=\frac1j\sum_{x>0\ \mathrm{odd}}
             \frac{\rho_1(x)}{x(3U^j(x)+1)}.
\]

The [compensated occupation argument](escape/COMPENSATED_OCCUPATION.md) identifies the limit of this positive, original-source observable:

\[
 \lim_j R_j=\frac{\log(4/3)}2
       \sum_{C\ \mathrm{cyclic}}\frac{d_C}{|C|}
                         \sum_{y\in C}\frac1{3y+1}
       \le\frac{\log(4/3)}8.
\]

Here `d_C` is the relative odd natural density of the full ordinary basin of the cycle. The proof retains the known ordinary-depth trace theorem and positive predecessor-density inputs, cited in the note. Equality at the displayed upper endpoint is equivalent to universal convergence. Establishing the matching lower bound is an open obligation, not a conclusion of this checkpoint.

The note also proves an exact source law: the main term occupies the original logarithmic source window `0 < log(x)/j < log(4/3)`. Nonprincipal same-word residue aliases contribute only `O(3^(-j))` before division by `j`. Thus averaging those aliases cannot supply the missing main term. This identifies a concrete source distribution for the next attack.

## Independent structures under investigation

| Route | New content | Remaining full-problem obligation |
|---|---|---|
| Original stopped trace | [Mellin dissipation](escape/STOPPED_MELLIN_DISSIPATION.md), [critical signed transport](escape/CRITICAL_DEFECT_LAW.md), and the positive occupation limit above | An independent endpoint lower bound or the earlier exponential original-law upper bound |
| Inverse potential | [Riesz transfer](global/RIESZ_TRANSFER.md): an exact critical singular correction, finite at every ordinary positive target | Control of its ordinary boundary contribution along an escaping source |
| Permutation and compression | [First gate columns](arithmetic/PERMUTATION_COLUMNS.md), [fixed gate clocks](arithmetic/FIXED_GATE_CLOCKS.md), and [moving gate clocks](arithmetic/MOVING_GATE_CLOCKS.md) | Every fixed ordinary source must encounter enough gates and reach the absorbing basin |
| Actual cycle arithmetic | [Run cofactor transport](arithmetic/RUN_COFACTORS.md), retaining both native valuations and all factors outside 2 and 3 | A contradiction for an actual integer cycle, rather than independent one-place estimates |
| Ordinary coefficient rigidity | [Mixed Hardy equation](global/ORDINARY_HARDY.md) and [fixed tripling defects](global/TRIPLING_DEFECTS.md) | A rigidity statement using the exact `+1` edges and the ordinary support |

The [density and square-mass comparison](escape/DENSITY_AND_SQUARE_MASS.md) gives a source-qualified lower estimate toward saturation from the actual unproved-source mass. It retains its ineffective constants and does not reach the self-consistency threshold needed for a contradiction.

Two controls prevent inappropriate use of deep machinery: [compression alone](global/COMPRESSION_CONTROL.md) does not force compact rescaled profiles, and [critical adelic capacity with boundary summability](global/CRITICAL_ADELIC_CONTROL.md) still admits bounded-coefficient variants. The [integer-fibre note](escape/LOCALIZED_INTEGER_FIBRES.md) keeps the complete maximal-in-height condition and gives a scaled `3x+5` calibration of the marginal-law estimates. These controls are not counterexamples to Collatz.

## Current sources and relation to other branches

The complete intake inventory is [INTAKE.json](../../reports/astra-diagonal-20261127/INTAKE.json). The new pass started from this PR's exact head `aa6868996f6f30b12d91c367f7c6edcfd93784b2`. It read the current research map and the changes on the other active research branches, including:

- PR200 at `eb91086951b66923787f696801f0c3ca52a0077d`: joint gated fractional pressure, first-power boundary layer, first-arrival currents, and the actual inverse-gain criterion.
- PR201 initially at `d21bac748e705a64b6b57a7996a8ad6282f0bcbf`, then at `dac732467c6ed5307d1b78eaa8534653aeeb7a4c`: fixed ordinary source restrictions, canonical localization, and the noncancelling transport test; followed by denominator-aware Pell/rank restrictions, actual critical paired translations, and the support-energy criterion. [Second intake and scope](SECOND_INTAKE.md).
- PR192 at `ae48a04cca29abe5fc8273bcda45e7eee0874896`, PR195 at `3fa7ef4a0011b35447a70f587b400878d5ea8ebe`, and the source-pinned prior inputs identified inside the notes.

No branch-history merge is needed to use a written theorem with its exact source and hypotheses. New literature leads include Weaver's bounded-real ternary localization, translated-interval compression and first-landing estimates; the branch-separation papers; the permutation literature; and Nashida's uniform fixed-barrier power-saving theorem. A bibliographic lookup is not a fresh validation of a paper or its Lean dependency closure.

## Lean and verification scope

The finite kernels use Lean 4.34.1 and Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`. The [driver](check_lean.py) builds the listed modules in a fresh temporary project-object directory, records exact source hashes, and runs `#print axioms` on every public theorem. It does not rebuild the old packet.

`AmusicalReturn.lean` connects the standard positive Collatz map directly to the permutation-with-compression map and proves its finite first-gate identities. `CompensatedOccupation.lean` proves the exact finite Duhamel identity while retaining the original endpoint. `OrdinaryHardy.lean` proves that the compressed coefficient rows recover every actual exponent. `RunCofactors.lean` proves the finite arithmetic transport. `ScaledSource.lean` verifies the separate scaling calibration.

The second checkpoint adds six freshly compiled modules and 30 audited public theorems: `PinnedRivals`, `OrdinaryCurrent`, `CriticalSibling`, `MovingScenery`, `InvariantCone`, and `ReciprocalGrowth`. They cover exact affine rival certificates, the finite ordinary residue current, the authentic sibling budget, centered inverse-word sections, uniqueness in a positive cone under explicit uniform minorization, and the conditional quadratic-growth horizon. Together with the first checkpoint this packet contains 11 checked modules and 67 audited public theorems. Receipts: [checkpoint 1](../../reports/astra-diagonal-20261127/LEAN_CHECKPOINT1.json), [checkpoint 2](../../reports/astra-diagonal-20261127/LEAN_CHECKPOINT2.json). The second build did not rebuild the earlier modules.

The analytic limits, density statements, infinite-column tightness and ordinary Riesz arguments remain written proofs or proposals with the external inputs shown in their notes. Neither a successful Lean kernel build nor the repository integrity validator establishes those infinite arguments or proves the conjecture.

Publication uses the existing draft [PR193](https://github.com/GettysburgResearch/collatz/pull/193). The other agents continue their attacks during checkpoint publication.
