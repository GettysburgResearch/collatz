# Equal-shape block-mixture execution scope

23 November 2026. The scientific note is
[BLOCK_CARRY_CAPACITY.md](../../../../research/lean-exact-witness-global-20261121/universal-step-20261123/cycles/BLOCK_CARRY_CAPACITY.md).

The written theorem keeps the complete denominator
\(D_N=2^{AN}-3^{pN}\). For a nonconstant integer boundary cycle made
from equal-shape blocks, a common carry-difference divisor G and carry
span Delta satisfy

\[
\Delta\gcd(G,D_N)\ge G(2^A+3^p).
\]

For two blocks, their carry difference delta must satisfy
\(\gcd(\delta,D_N)\ge2^A+3^p\). Thus a 6-free carry difference below
that threshold excludes every mixed concatenation, with no block-length,
period, frequency, or switch bound. Constant boundary cycles remain
separate. The theorem does not cover arbitrary Collatz words by itself.

## Executed checks

[execution.json](execution.json) binds the exact scientific source hashes
and records the actual commands, return codes, and output hashes.

- `BlockMixture.lean` compiled with Lean 4.34.1, `-j 1`, and
  `-DwarningAsError=true`.
- Eight public declarations were audited. They use only subsets of
  `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx` or custom
  research axiom occurs. See [lean-audit.log](lean-audit.log).
- The formalized scope is arbitrary-length affine composition and the
  full no-mixed-cycle/closed-path exclusion for a 6-smooth carry
  difference. The larger nonsmooth capacity theorem is written
  mathematics, not an additional Lean claim.
- The exact Python checker passed normally and under `python -O`, with
  byte-identical output: [normal.json](normal.json),
  [optimized.json](optimized.json).
- Its bounded controls include 8,166 mixed U/V schedules through 12
  blocks, 114 schedules for the nonsmooth example through six blocks,
  six common contexts, ten unbounded-family parameter controls, 36
  nonvacuous general affine cycles, a sharp equality example, and three
  rejected damaged inputs. The general affine cycles are explicitly
  not claimed to be Collatz cycles.

No historical cycle census was rerun. No repository-wide validation,
commit, push, remote CI execution, or external review is claimed by this
lane; the coordinating agent handles publication and its separate gates.

## Primary-source inspection

- Halbeisen--Hungerbuehler, *Optimal bounds for the length of rational
  Collatz cycles*, primary author PDF: Section 2's carry, concatenation,
  and rational-cycle identities were read. No external finite
  verification threshold is used.
- The primary manuscript *Collatz cycles whose parity word has two
  periodic stretches*, rStation paper 57, v1, was read at Sections 2
  and 5 to compare the junction/gcd route and arbitrary-switch boundary.
  Its claims about bounded numerical cycle exclusion are not imported
  or independently reviewed here.
- The related single-transposition manuscript, rStation paper 4, v1,
  was inspected for overlap. The present proof is self-contained and
  does not claim historical priority for the basic swap identity or
  balanced-word exclusion.

The source URLs and exact inspection boundary are in the scientific note.
