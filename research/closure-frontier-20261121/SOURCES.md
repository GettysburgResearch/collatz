# Frozen source snapshot and dependency scope

This pass began by querying all-state pull requests sorted by update time,
including older PRs with newer commits, and reading the current main ref.
The newest 30 updated PRs were inspected as metadata; the proof-relevant
files below were selected for direct reading. A second latest-head query
found the same scientific heads. This is a selected source audit, not a
claim that every historical file or every open PR was independently proved.

Base main: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
Date of this research pass: 21 November 2026, Jerusalem. GitHub and
execution timestamps in raw receipts remain UTC.

| PR | Frozen head | Directly inspected material and use |
|---|---|---|
| 146 | `fd991063721e9c157d318e40bb20131762f7d750` | `research/upper-bit-mergers/LEAST_FAILURE_SIEVE.md`, `FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`, `TWO_SCALE_TRIPLING.md`, `TRIPLING_VARIATION.md`; current localization, sparse-sieve limitations, and the reconstructed antichain amplification. No Lean build from this PR is claimed. |
| 164 | `6fa6b429870a9cd53cde0fc77ad64a3c3956199f` | `research/witness-closure-512-2026-11-20/continuation-negative.md` and `continuation-descent.md`; two inherited signed-reference descents and the distinct positive-base construction. The new grammar credits both old templates. |
| 165 | `78bdb31ccba608de3d089b751a0ab59a52007408` | PR metadata and `research/certificate-transfer-intake-20261120/EXCEPTIONAL_FAMILY.md`; its affine-coalescence exclusion is distinguished from actual ordinary meetings and from least-failure exclusions. Uploaded archives and the entire intake audit were not independently replayed. No new proof here depends on that manuscript's density-one theorem. |
| 166 | `5996b9f525ca50978bc34f423192c36a87765bf3` | `research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`, `LADDER_RENEWAL.md`, `GRH_INTERFACES.md`; inherited ladder language and its coarse renewal estimate, and exact eventual-periodic rigidity G5. No GRH assumption is used in the new elementary theorems. |
| 163 | `051237135a34ae7d4b973ee5fcf5da04ded6f0fc` | `research/deep-reverse-closure-20261120/FIVE_SLICE_ENERGY.md`, `LEAST_FAILURE_HEIGHT.md`, `REVERSE_CERTIFICATE_KERNEL.md`; comparison of five energy to tripling energy, conditional least-failure height, and the rank-five singular reference. External dependencies remain as named in that source. |
| 162 | `2279da37ac612dbe049777354cdedb3c0aa03282` | `research/creative-closure-20261120/five_closure.md` and the preceding pass's reviewed scope; the original paired two-odd-input block is credited, and fixed-rank carry bounds are not assumed. |

Each row can be opened with the immutable URL form
`https://github.com/GettysburgResearch/collatz/blob/<full-head>/<path>`.
The principal notes include their load-bearing immutable links and claim IDs.
New conclusions depend on the displayed proofs and exact finite certificates,
not on agreement between PR summaries.

## Primary external inputs

1. Ilia Krasikov and Jeffrey C. Lagarias, *Bounds for the 3x+1 Problem
   using Difference Inequalities*, [arXiv:math/0205002](https://arxiv.org/abs/math/0205002),
   Theorem6.1, printed page16. The fixed-target exponent `.84` is used
   only in FC5 and in the named consequences of the older energy
   comparison. Both author and reviewer inspected the source. Its large
   linear program was not rerun in this pass.
2. Terence Tao, *Almost all orbits of the Collatz map attain almost
   bounded values*, Forum of Mathematics, Pi10 (2022), e12,
   [DOI10.1017/fmp.2022.8](https://doi.org/10.1017/fmp.2022.8),
   equations1.23,1.25,1.27 and Proposition1.14. These identify the
   stationary Syracuse projections and their fine-scale `L^1` estimate.
   TM6--TM7 retain this published input; TM1--TM5 do not require its
   Fourier proof. The density conversion in TM7 is proved here.

A search also surfaced more recent claimed predecessor improvements and
a proposed automatic-set result at rStation. None is imported as a new
verified premise. Using the published `.84` input keeps the current
closing threshold explicit and independently source-checkable. This is
not a claim that `.84` is the latest proposed exponent.
