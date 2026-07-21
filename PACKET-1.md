# Packet 1: the EQ extreme-value estimate

**Status:** open. **Prerequisite reading:** `EQ.md`, `MINIMAL.md`.
**Claim in ledger:** EQ (archimedean form).

## Context

EQ is the program's isolated attackable problem: the valid sets `R_K`
(2^K coded residues mod 64^K) are equidistributed at survivor scale
32^K. Proved so far: exact Fourier product formula (T7), cascade lemma
(T8, threshold δ < 1/145), self-similarity + sharp global maximum
cos(π/64) (T9), exact-run rigidity confining all sub-modulus
adversarial frequencies to the first ~0.158K levels via the integer
equation 17θ = ±81^{t₀+L}σ (T10, zero violations over the full
survivor range at K = 16). Remaining: excluding chance-level clustering
— measured at exactly the generic Poisson rate (138 multi-level deep
interior runs vs 160 expected, max length 3 at K = 16).

## Target

Prove:  Σ_{0<θ≤2^K} |S_K(θ)|/θ ≤ 2^K · K^{−ε}  for some ε > 0
(or any bound sufficing for Erdős–Turán at scale 32^K).

Consequence: quantitative near-emptiness of survivors — the program's
flagship theorem, converting every null measurement into mathematics.

## Sub-packets (parallelizable)

- **1a (analysis).** L^{2s} moment bounds for Π_t|cos(πθc_t/64^K)|
  over θ ≤ 2^K, using T7's product structure and T10 to control
  inter-level correlations. Even s = 2 with the exact-run input may
  close the ET sum. Deliverable: proof or a precise identification of
  the obstruction.
- **1b (adversarial).** Construct survivor-range frequencies with
  |S_K(θ)|/2^K ≥ K^{−o(1)}, or show the observed ≈0.30 plateau decays:
  extend scans to K = 20–24 with branch-and-bound pruning on the
  product. Deliverable: the max-decay curve and the structure of
  argmax frequencies.
- **1c (literature).** Do Li–Sahlsten / Solomyak Fourier-decay results
  or Bourgain-type sum-product apply to the twisted affine system
  `R_K = 81^{−1}(64·R_{K−1} + 17ε)`? Deliverable: a mapping of
  hypotheses of the nearest applicable theorem onto this system, with
  the gaps listed.
- **1d (verification).** Independent re-implementation of T7–T10 from
  their statements alone (no reference to existing code). Deliverable:
  a second verification suite; any discrepancy is a finding.

## Success criteria (falsifiable)

Either (i) a proof of the ET bound — then EQ closes and the survivor
theorem gets written; or (ii) an explicit adversarial family — then EQ
as stated is false, and `MINIMAL.md` gets a corrected formulation.
Both outcomes advance the program; only silence does not.
