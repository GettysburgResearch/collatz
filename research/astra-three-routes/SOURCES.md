# Frozen sources and overlap boundary

This is a focused research pass, not a complete independent review of all source
branches or of the external literature. The packet makes no broad priority claim.

## Repository snapshot

* Canonical main: `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`, re-queried in this pass.
  [Agent protocol](https://github.com/GettysburgResearch/collatz/blob/9704bcf1ff33cc9e2b729e0c40137a1e55b95397/AGENTS.md)
  and the research map / integrated coefficient-stopping packet give the ordinary,
  all-depth, and source-status boundaries.
* PR #87: `e9adc409031a61f3801c4ee1e1e6deeb34188eb7`.
  [Fixed-height attack](https://github.com/GettysburgResearch/collatz/blob/e9adc409031a61f3801c4ee1e1e6deeb34188eb7/research/external/mazur-2026/fixed-height-power-saving-attack.md).
  Prior: exponent-race and eternal endpoint-one target. Not a native proof of
  fixed-height power saving.
* PR #88: `c28922fb6d1c070bf86a76192f40bc9ea3edd67c`.
  [Committed fixed-height note](https://github.com/GettysburgResearch/collatz/blob/c28922fb6d1c070bf86a76192f40bc9ea3edd67c/research/external/mazur-2026/fixed-height-forward-power-saving.md).
  Prior: one-horizon entropy wall, exponent collapse, and all-subset
  mass-conservation obstruction. The PR description lists older paths; the
  committed file, not those path names, controls this cross-reference.
* PR #90: `aeb69ce631370be36fd1f80b472ab448e7df2a73`, frozen by current PR metadata.
  [Proof packet](https://github.com/GettysburgResearch/collatz/blob/aeb69ce631370be36fd1f80b472ab448e7df2a73/research/astra-critical-mass/PROOF.md).
  Prior: critical weighted-mass bridge; positive summable inverse criterion;
  power-like weight obstruction; a particular infinite even-ray repair and its
  all-block obstruction; finite-time all-source Green bounds. Our work does not
  relabel those results as new. The new route-1 certificate uses full finite
  inverse cones and aggregate fractional Mellin weights; the new rank theorem
  treats arbitrary finite affine-valuation features.
* PR #81: `09d6f9086d4ead63a5102f05458441939c29f4f5`.
  [Support-corrected envelope](https://github.com/GettysburgResearch/collatz/blob/09d6f9086d4ead63a5102f05458441939c29f4f5/research/positive-coefficient-entropy/claims/T-6812-support-corrected-cofinal-envelope.md).
  Prior: source/end displacement convention and the cofinal source-height target.
  The echo packet reproves the elementary interfaces it uses and does not assume
  that cofinal inequality or the mechanical all-length sector has been solved.
* PR #6: `4810a0771da61a1cb609ef8707dfcf7f0f6e666f`.
  [Termination frontier](https://github.com/GettysburgResearch/collatz/blob/4810a0771da61a1cb609ef8707dfcf7f0f6e666f/research/termination-frontier/README.md).
  Prior: six carry rules and the distinction between standard match height and
  semantic termination. Legacy leads in that source are not proof dependencies.

Main, #88, and #90 were re-queried in this pass. The other listed exact snapshots
were the frozen sources already inspected in the preceding route-assessment
pass; no later head is claimed reviewed. No source branch is merged or modified.

## External primary sources checked

1. Lech Mazur, *Certified x^0.90 Lower Bounds for Collatz Predecessor Sets*,
   version 2 / source 1.0.0, 2026-07-17.
   [Primary theorem page](https://www.proofatlas.ai/collatz-predecessor-090/)
   and [source overview](https://www.proofatlas.ai/sources/collatz-predecessor-090/).
   The page states that every fixed positive target not divisible by three has
   eventually at least c_target X^(901/1000) predecessors, for some positive
   target-dependent constant. Its pinned source is
   `5f76a170e74ea5b0c37c56683bd4c1e9d72e5e3f`.
   The page discloses native finite-check trust dependencies. We did not build
   Lean or replay its large payload. Only the final conditional application of
   T-A3-102 uses this imported hypothesis. All main native results are independent
   of it. No PDF is redistributed or presented as newly inspected in this pass.
2. Emre Yolcu, Scott Aaronson, Marijn J. H. Heule,
   *An Automated Approach to the Collatz Conjecture*, arXiv:2105.14697v3,
   revised 2022-12-31.
   [Primary abstract and metadata](https://arxiv.org/abs/2105.14697).
   This supplies the broader rewriting-program context, including its
   termination/Collatz equivalence and nontrivial weakenings. The elementary
   carry-normalization and valuation-rank proofs here do not invoke that
   equivalence as a black box.

Both external pages were checked during this pass. The focused search did not
establish priority or exhaust the literature on arithmetic Lyapunov functions.
The same finite parity and p-adic congruence facts occur widely in the Collatz
literature; the claims here should be judged by their precise scope and proof.
