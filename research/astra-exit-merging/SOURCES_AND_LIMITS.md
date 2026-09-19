# Sources, credit, exact scope, and remaining work

## Repository references

This is additive exploration based on main
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, read live during this pass. It does
not import unmerged packets or modify their status. The strategy is
[issue #121](https://github.com/GettysburgResearch/collatz/issues/121).

The direct research context is:

- PR105, `423a0180a0f6a89da7adc1ab4bad950a6dc79ef6`,
  `research/astra-tail-transport/reverse-realization/PROOF.md`, especially
  ATT-304–306: ordinary-value partial normalization, residual n=3 mod12, and
  administrative echoes. This later continuation remains proposed; the prior
  review only covered the earlier head `912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe`.
- PR106, `7b7471ea0e7b359a2ac46fb1e6aff269331509c3`,
  `research/astra-linear-frontier/prefix-rank/PROOF.md`,
  `PERIODIC_SWITCHING.md`, and `SPIKES.md`: actual-prefix ranks and their exact
  selection/spike boundaries. No rank theorem is a premise of our identities.
- PR117, `d414cffc3a4119767df30f5ee0d5ee5856c5050f`,
  `research/astra-suffix-rotation/PROOF.md`, ASR-005–007: the specific Psi
  normalizer's Mersenne obstruction and the mixed-rank 11/17 cycle. Our
  ordinary-value selector is different, so its success on a family does not
  refute the original algorithm-specific obstruction.

The current packet does not independently review every claim in those
branches, run their full native protocols, or extend their inherited reviews.
It supplies separate proofs and evidence for the statements in PROOF.md.

## External credit found during the pass

An external repository was inspected through the connected GitHub reader:
`Sodelin/Collatz-Conjecture-Work`, exact main observed
`026aa4ad4be6453a005ab950b160a9f2204c5271` (publication commit dated 2026-09-07).

1. [L6_Minimal_Counterexample_Exit_Constraint.md](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/026aa4ad4be6453a005ab950b160a9f2204c5271/proof-search/lemmas/L6_Minimal_Counterexample_Exit_Constraint.md),
   blob `2400b0ca03fc0fff8af1ce385e8b46e8f3132a56`, dated 2026-08-23 in the note.
   It records the good first odd-exit congruence and smaller-source mergers.
   The even-run half-source identity is the same as AEM-002; the source uses
   another smaller witness for odd run lengths. Our uniform half-source
   version is proved here and is not claimed novel. This external note was
   found after the elementary identity was rederived, before publication.
2. [Root_Relative_Burst_Descent.md](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/026aa4ad4be6453a005ab950b160a9f2204c5271/proof-search/lemmas/Root_Relative_Burst_Descent.md),
   blob `894ef5fe2313add6bd7d412a69f4d678664c1b8c`.
   This is useful related work on n=8^k u-5. Its stated mechanism requires
   `2^k | (9^k u-5)` and yields an actual forward descent after 4k steps.
   Our guards use `9^k u+1`, a source-halving seed bridge, and a second odd
   phase; the k>=23 specialization has no forward descent on its certified
   arm. That comparison is a mechanism distinction, not an exhaustive
   priority/novelty audit of the external repository or the literature.

No external manuscript or code was copied into this packet, and no external
formalization or acceptance claim is adopted. The external source's stated
Lean status was not rebuilt or independently certified. The words, affine
identities, positivity, and source-order consequences used here are proved
locally and checked by new standalone programs.

## New claim identities and review tasks

| Claim | Scope | Priority for independent review |
|---|---|---|
| AEM-001a/b | Composition clocks and lifting seed pairs through repeated physical words | Preserve positivity, parity-cylinder semantics, and the original source comparator. |
| AEM-002 | Known good odd-exit merger, including r=1 and uniform half-source target | Check the empty-prefix case and external credit; do not score as a new conjecture reduction. |
| AEM-003 | The guarded two-exit half-source theorem, all k,u satisfying actual-input guards | Check both seven-bit seed paths on v=7 mod32, X=2Y+1, and the second phase's valuation and mod4 condition. |
| AEM-004 | Equal-clock one-third certificate when 3|n | Check the prefixed inverse step and the actual output class x=7 mod32. |
| AEM-005 | No forward descent on the displayed arm for k>=23; no smaller pure ancestor when 3|n; unbounded CRT specialization | Check the +617 comparison, all intermediate states, exact CRT valuations, and the restricted nature of the no-descent conclusion. |

All are **PROPOSED pending independent mathematical review**. The two programs
have one author, despite independent implementations. Agreement is not peer
review. A review of this packet must state its exact file hashes/commit, not
silently promote neighboring research.

## Research boundary and a targeted next investigation

The result has genuine two-stage composability and an additional uniform
inverse reduction. It does not close the transition system. Specifically,
`h<1`, the final hard-exit congruence, inputs outside exact 110 shadow-depth
classes, and the reduced x=7 mod32 population remain outside a universal
successful-cover theorem. UNRESOLVED means just that.

The next useful investigation is to derive source-relative seed bridges for
these complementary actual exits, allowing variable tails but retaining
literal physical endpoints and one original-source order. A fixed additional
horizon that happens to work on a finite set is not sufficient. Do not replace
this open coverage problem with another renamed closing equivalence.

No complete Collatz proof, divergent orbit, or nontrivial positive cycle was
obtained in this pass. The exact affirmative result is the guarded theorem
and its unbounded, strongly two-sided specialization.
