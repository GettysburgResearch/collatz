# Sources, claim scope, and review boundary for pass two

All new theorem-level claims are **PROPOSED pending independent review**.
This file is a provenance record, not a canonical status promotion.

## Exact repository state

- Repository: GettysburgResearch/collatz.
- Parent PR #92: `879343c33a7dca29128891cf6e10d9c7be1ba482`.
- Branch extended: `agent/astra-three-routes-01/three-route-offense`.
- Main underlying that parent: `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`.
- AGENTS.md and the published PR body were read from the actual connection.
- The 14-file publication receipt and local supplied ZIP agree on the parent
  packet. Old proof and experiment bodies remain unchanged; its README receives
  an appended continuation pointer only.

## Claim matrix

| Claim | Exact scope | Proof dependency | Not supplied |
|---|---|---|---|
| T-A3-401 | N_S(X)<=4X^(39/40) for every equal-depth-U-injective odd set | Elementary exact cylinders, affine remainder, Chernoff certificate | An inverse-basin bound |
| T-A3-402 | O(X^(19/20)) when S is also forward invariant | T-A3-401's splitting argument; separate fiber-free recurrence | A sub-0.901 basin exponent |
| T-A3-403 | Uniform Mellin/reciprocal budget above m | T-A3-401 and nonnegative integration | Uniform weighted mass over all exceptional sources |
| T-A3-451 | Actual SC-infinite tail; SC* iff eventual periodicity | T-A3-403, exact product formula, cycle coefficient | SC* or positive-cycle exclusion |
| L-A3-452 | Extracted source within O(n^(39/40)) of a value minimum | T-A3-451 and explicit product bound | An extraction-time bound |
| T-A3-453 | Complete finite continuation as an interval and one CRT class | Exact affine identities and parity cylinders | All-length rejection of ordinary tuples |
| T-A3-501 | No fixed-block scalar rank with arbitrary separate profiles | Ordinary CRT tests, finite root support, all-odd paths | No-go for interacting profiles or general ranks |
| T-A3-502 | Same rank class fails the specified adaptive whole-run macro | Separate branch/root transport and one ordinary macro family | No-go for all adaptive grouping schemes |

The finite countermodel at source 61/295 has exact preperiod/period replay.
It refutes a rational-only strengthening, not an ordinary-integer theorem.
The cofinal-time mass criterion is an additional conditional corollary of the
parent's exact inverse identity, with the core [1,64] rechecked in this pass.

## Prior literature: do not claim novelty for orbit summability

M. V. P. Garcia and F. A. Tal, **A note on the generalized 3n+1 problem**,
Acta Arithmetica 90(3) (1999), 245–250.

Primary bibliographic record:
https://eudml.org/doc/207326

Primary indexed full-text route:
https://repositorio.usp.br/bitstreams/a02b7ba9-c8be-42d8-bbae-4d836520ec13

The search establishes the bibliographic record and the closely related
orbit-sparsity literature. Direct full-text retrieval timed out in this
session; the paper's detailed proof was not reconstructed from that PDF.
No theorem in this pass depends on an uninspected equation from it. The local
proof starts from exact ordinary cylinders and supplies all estimates used.
We make no priority claim for reciprocal summability or the qualitative
coefficient-discrepancy escape.

Discovery provenance, not a black-box proof dependency: a public reference
request dated July 24, 2026 already explicitly derives summable reciprocals
and q_k log 3-k log 2 -> infinity from Garcia–Tal-style interval bounds:
https://mathoverflow.net/questions/513539/is-it-known-that-a-divergent-collatz-trajectory-must-have-summable-reciprocals

Its existence was checked during this pass. The proposed local quantitative
constants and the source-extraction crosswalk still require review; a full
literature-priority comparison was not completed. The original elementary
proof here makes that literature-access limit harmless to the stated logical
dependency chain, not a license to imply novelty.

## Exact cross-PR comparisons

**PR #80**, reviewed slice `5ca112a783fc269acdadadc6e2e86e2cdadb4298`:

    research/least-counterexample-global/claims/L-6503-tail-minimum-syndetic-ladder.md
    research/least-counterexample-global/LITERATURE_AUDIT.md

The first gives value-minimum ladders and coefficient-stopping depths tending
to infinity; it explicitly does not establish one infinite coefficient-stopping
source. The second records the older scalar/adelic boundaries. Our new local
bridge obtains an actual SC-infinite tail from bounded real correction mass.
It does not purport to invalidate the earlier carefully stated limitation.

**PR #90**, current snapshot `345168de8732f6240e5c926420cee3db3b0fa137`:

    research/astra-critical-mass/RUN_RENEWAL.md

Its PR summary and the kernel/ordinary-drift portion of the note were read.
It supplies an unbounded-run ordinary shell drift, and explicitly isolates
transported-distribution discrepancy; it is not imported or promoted here.
The new orbitwise counting argument uses equal-depth injectivity, not a
fresh-shell independence assumption, and does not solve that discrepancy.

**PR #91**, snapshot `b8c88843726ee7ac11cf91323c69bf911ca50706`:

    research/astra-three-routes/ROUTE_3_RANK_CERTIFICATES.md

Its common-rank upward progression and unbounded repayment families were read.
They use different adaptive multi-return grouping, so the new profile obstruction
for one F-macro does not refute them. Complete coverage remains open there.
No file or result from #91 is silently incorporated into #92. The shared
research/astra-three-routes/README.md integration collision remains explicit.

**Parent PR #92** supplies the mass and echo notation, exact ordinary core,
and the prior linear-profile obstruction. The new claims have new identifiers
and separate proof files. An author-derived generalization is not an independent
review of the parent.

## Validation and limits

The standard-library generator and a separate verifier were executed locally.
The verifier obtains cylinders by exhaustive ordinary residues rather than
modular inversion, obtains first-crossing words breadth-first rather than by
the generator's recursive traversal, evaluates continuation by rational
physical stepping and bitwise source lifting, and checks macro endpoints by
literal odd/even runs. Six resealed corruptions are rejected.

The elementary all-set, all-time conditional, and all-profile proofs are
written mathematical arguments; the finite JSON does not certify those proofs.
Both programs have the same author. No external Lean build, large external
certificate replay, full-repository structural validator, or workflow was run.
A preliminary floating-point survivor-bias extension gave no all-time argument;
it is not part of the certified evidence and supports no theorem claim.

No source status, canonical registry, main file, repository setting, workflow,
or other contributor's PR is changed. No route is dropped from the portfolio.
