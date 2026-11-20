# Source refresh and dependency boundaries

The branch starts from main
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, tree
`1c25c17df24491de6187445f1a1d355d5a7660c3`.
The current README, research map, results catalog, errata and contribution
instructions were read before the new work. Results below remain proposed
research; this branch does not extend the accepted baseline by declaration.

## Exact repository sources

| Source | Full inspected head | Specific material and use |
|---|---|---|
| [PR146](https://github.com/GettysburgResearch/collatz/pull/146) | `e238c63a5d57f96bb063b7472498d1977df51951` | `research/upper-bit-mergers/DEEP_REVERSE_BASIN.md`, `REVERSE_BASIN.md`, `STABILIZED_CORE_DESCENT.md`, `ONE_CELL_SIXTY_FOUR.md`, `SHORTER_ANCESTORS.md`, `BOUNDED_RANK_TRANSFER.md`, `MERSENNE_EXPONENT_DESCENT.md`, `BASIN_PHASE.md`: latest directed certificate criterion, actual inverse-word construction, stabilized labels, and the signed-offset boundary. The head was queried again before integration and remained unchanged. |
| [PR157](https://github.com/GettysburgResearch/collatz/pull/157) | `64361ecca770092d6c8242dc6211e38818af2e50` | `research/global-closure-20261120/merger.md`, `closing-attempts.md`: full Collatz reduction to forward five on convergent odd ternary units, and the rank-one shifted-power obstruction. The reduction is used as a source-pinned theorem; this packet does not rerun its complete cover. |
| [PR158](https://github.com/GettysburgResearch/collatz/pull/158) | `cf49a68bf93e98c97a18dc3d1a4186faf534e422` | `research/ordinary-basin-closure-20261120/README.md`, `CERTIFICATE_CARRY.md`, `EXPANDING_RETURNS.md`, `TWO_MACRO_NORMALIZATION.md`: why augmented movement and local carry normalization do not supply ordinary all-source closure. Context and overlap audit, not a new full verification of that packet. |
| [PR159](https://github.com/GettysburgResearch/collatz/pull/159) | `0e7d2841b1591073c6399f91f3b6944ebcdbdbd5` | `research/allhands-global-closure-20261120/PRIME_SUPPORT_PEAKS.md`, `DIRECTED_BOUNDARY_CIRCULATION.md`, `UNIFORM_J_ATTEMPT.md`: previous peak/circulation progress and the unresolved high-exponent label problem. No claim that GRH provides an orbitwise prime bound or finite boundary moment. |
| [PR160](https://github.com/GettysburgResearch/collatz/pull/160) | `6d877e718f5ef9d57fe1830912c444359718747a` | `research/closure-attacks-20261120/README.md`, `merger/PHYSICAL_CERTIFICATE_BOUNDARY.md`, `critical/SINGLE_SLICE_ENERGY.md`: physical certificate and energy obligations. Its five-energy propagation question is subsequently answered by PR163; this packet does not repeat it as open. |
| [PR161](https://github.com/GettysburgResearch/collatz/pull/161) | `4a0536b587fc91ee0c7bb1b160c06dda16ddbf23` | `research/source-rigidity-20261120/README.md`, `CLOSURE_ATTEMPTS.md`, `CARRY_DEBT_RESET.md`, `SINGLE_LAYER_FIVE.md`: shifted-power and carry limitations. The later shifted-smooth classification in PR163 is acknowledged rather than claimed anew. |
| [PR162](https://github.com/GettysburgResearch/collatz/pull/162) | `2279da37ac612dbe049777354cdedb3c0aa03282` | `research/creative-closure-20261120/five_closure.md`, `occupation.md`: the r=1 physical block and family are prior work. FL1 generalizes the block to every r; FL2 compiles a full restricted language. The original-source occupation problem is not replaced by a prime distribution. |
| [PR163](https://github.com/GettysburgResearch/collatz/pull/163) | `051237135a34ae7d4b973ee5fcf5da04ded6f0fc` | Newly available during this pass. Directly read `research/deep-reverse-closure-20261120/README.md` and `CLOSING_ATTEMPTS.md`, including section D's exact single-cylinder renewal `64/441`. The new `LADDER_RENEWAL.md` extends that deduction to the whole disjoint ladder union and contracts at both s=1 and s=.84. Other reported PR163 results are acknowledged at their source scope, not independently reverified here. |

The most recent seven updated PRs were re-queried during integration,
revealing PR163. This was a current targeted refresh of the relevant
sources, not a claim to have independently audited every open PR. Full
source SHA pins are used because PR numbers and branch descriptions can
change.

## External mathematical inputs

1. Eric Bach and Jonathan Sorenson, *Explicit bounds for primes in residue
   classes*, Mathematics of Computation 65 (1996), 1717--1735,
   [DOI](https://doi.org/10.1090/S0025-5718-96-00763-6).
   The least-prime bound under ERH/GRH and the Chebotarev scale are quoted
   with their hypotheses. No proof of either theorem is claimed here.
2. Youness Lamzouri, Xiannan Li and Kannan Soundararajan, *Conditional
   bounds for the least quadratic non-residue and related problems*,
   [corrected arXiv v3](https://arxiv.org/abs/1309.3595v3).
   The sharper least-prime statement is corroborated in section 1.2 of
   Carneiro--Milinovich--Quesada-Herrera--Ramos,
   [arXiv:2404.08380v2](https://arxiv.org/html/2404.08380v2).
   Only the coarser bound is needed for G1. A source review is not a
   reconstruction of the external analytic proof.
3. J.-H. Evertse, H. P. Schlickewei and W. M. Schmidt, *Linear equations
   in variables which lie in a multiplicative group*, Annals of
   Mathematics 155 (2002), 807--836,
   [journal](https://annals.math.princeton.edu/2002/155-3/p04),
   [author manuscript](https://arxiv.org/abs/math/0409604).
   Its finite-rank nondegenerate solution theorem is the explicit
   SOURCE-QUALIFIED input to the bounded-depth ancestor finiteness
   deduction. Positivity establishes nondegeneracy in the application.

GRH was explicitly authorized as a hypothesis. No claim about a recent
announcement, its author, institutional attribution or acceptance is
required or made. Allowing the relevant stronger GRH formulations does
not license a zero assertion for an arbitrary component Dirichlet series.

## New work versus credited work

The unbounded ladder, restricted whole-certificate compiler, complete
cylinder description and expanded energy renewal are the proposed
extensions relative to the inspected sources. The r=1 block, forward-five
global reduction, rank-one residual obstruction and single-cylinder energy
renewal have prior source pins above. The eventual-periodic label lemma
and standard GRH consequences carry no priority claim.

The exact remaining gaps are not renamed as results: arbitrary certificate
transport, finite uncovered five energy, uniform-J rigidity and actual
finite-exception closure remain unresolved.
