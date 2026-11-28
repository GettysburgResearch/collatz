# Persistent pass brief

## Authorization, clock, and working agreement

- New pass start: **2026-11-28 12:33:06 UTC**.
- Full nine-hour target: **2026-11-28 21:33:06 UTC**.
- The user explicitly requests Astra 6.2 Ultra agents with broad context and
  substantial mathematical freedom. Continue and reignite lanes through the
  full interval. Favor load-bearing attacks, including directions absent from
  the repository, over auxiliary bounds or cosmetic formalization.
- Keep chat and inter-agent summaries short; put full arguments, computations,
  and evidence in tracked files. This is an output-volume preference, not an
  instruction to omit material problems or evade safeguards.
- Outside theorems and outsider-reported Lean are permitted. Clearly mark what
  was actually replayed here. No proof assertion is licensed merely by ambition.
- Publish reviewed checkpoints periodically to a dedicated branch/PR. Do not
  merge main, rewrite other contributors' branches, or alter repository settings.

## Workspaces

- Coordinator: `/workspace/scratch/921bae088f07/collatz-nine-hour`;
  branch `research/astra-nine-hour-resolution-20261128`.
- Arithmetic/structural energy: `/workspace/scratch/921bae088f07/collatz-nine-arithmetic`.
- Analytic/probabilistic energy: `/workspace/scratch/921bae088f07/collatz-nine-analysis`.
- Independent synthesis/new directions: `/workspace/scratch/921bae088f07/collatz-nine-wild`.
- Shared Git object store and fetched PR refs:
  `/workspace/scratch/921bae088f07/collatz-audit`.
- All worktrees initially contain exact PR218 head
  `960b4252f9a787ab8d25e9e5894cb007d1b08977`. Each lane owns only its new
  `research/astra-nine-hour-resolution-20261128/{arithmetic,analysis,wild}/`
  directory and corresponding report subdirectory unless coordinated otherwise.
  Commit local milestones; root handles remote publication. No lane should
  reset another worktree or use another lane's index.

## Broad starting context

Read the repository's `AGENTS.md`, `README.md`, `docs/RESEARCH_MAP.md`, relevant
catalog/packet, and `research/integrated/ERRATA.md`. The previous pass's compact
scientific map is `research/astra-full-proof-20261128/FINAL_ASSESSMENT.md`, with
the coordinator's reconstruction in
`reports/astra-full-proof-20261128/FINAL_REVIEW.md`. They are not a mandate to
continue those exact directions.

Previous work made several full-proof consumers explicit but supplied no
ordinary-source upper estimate. The direct signed suffix mean after the critical
clock would settle both escape and additional cycles. A whole real/ternary
stationary selector exactly reconstructs ordinary sources with O(log N/N)
replacement error, but conditioning is rare and the selected suffix has low
entropy. An elementary rational floor-survival bound vanishes after the critical
clock while ordinary floor-one survival is identically one. A repeat-stopped
correction product has a uniform positive lower bound on every bad ordinary
source and vanishing rational reference mean; its ordinary upper mean remains
open. Future-minimum flux is localized to intermediate widths. Upper-certificate
padding preserves a negative chart carrying the original lower trajectory.
These are useful constraints, not evidence that one selected route must win.

Other live work at initial intake:

| PR | Frozen full head | Useful context |
|---|---|---|
| 217 | `3d700eaf6aac6617cab81b59cbeb8f75c5d38aaf` | Critical negative quantile consumer; median collisions; stationary selector; semiprime reduction; finite Cartier systems with growing-conductor gap |
| 219 | `b1f2276c45218b0a05a6c4c0e413fec1e4e4dd46` | Native affine rectangles from Subspace Theorem; sharp Mersenne anchor rigidity; entropy-critical inverse decoding; rational-source sieve |
| 220 | `330dc8f7f1f7e970ad52b2835bf151cc71e44030` | Semiprime factor passage; actual source first-passage, still no universal convergence |
| 215 | `4f33ecc2de6f0ccf605a68c28da5abea0348e47b` | Earlier long pass, signed endpoint transfer and native minimum/clock programs |

Read their actual source paths with `git ls-tree` and `git show origin/pr-N:path`
from the shared clone. Freeze later heads separately. A PR's summary is not
automatic validation of its individual claims. The shared clone is a no-checkout
clone: apparent deletions there are not user work to reset.

## Outside inputs worth exploring freely

- `https://rstation.ai/problems/collatz/papers/191/v2`: Weaver actual first-passage
  scale; when B is logarithmic the error is sqrt(k log k), not sqrt(k).
- Weaver papers 12 (positive fixed-target predecessor mass), 19 (joint real/ternary
  stationary laws), 42/95 (Fourier limitations/profiles), 175–177 (orbit packing
  and harmonic clocks), and Wren 55 (uniform future-floor sparsity).
- Valbuena repository `x1xhlol/collatz-two-coordinate-obstruction`, last inspected
  `a7275d5a73814d3d9a400c6fe6577de9542b03a3`: extensive outsider-reported Lean on
  densities, Lp stationary laws, cylinder energy, and occupation. Not locally
  rebuilt. New work may be available. The full integer trace remains a boundary.
- Mazur and Lau positive-predecessor-density results have outsider formalization
  evidence and were not rebuilt in the last pass. They allow density-zero bad
  sources to imply no bad source, with eligible targets handled correctly.
- Classical number theory, dynamics, probability, combinatorics, computer algebra,
  proof assistants, and entirely different architectures are all available.

No requirement to stick to this source list. Search primary material for niche
or uncertain claims. Do not spend the whole pass rechecking already scoped inputs
unless a genuine dependency problem appears.

## Checkpoint discipline

Save derivations early. For an intermediate result, state the exact theorem,
proof, first unsupported inference, and what would turn it into full closure.
Finite computations should discriminate a concrete proposed statement, not just
extend a census. Formalize genuinely useful identities or new arguments when
feasible, but do not substitute a Lean wrapper around an open hypothesis for a
proof advance.

Root reconstructs claims before publication and runs `python -X utf8 -B
tools/validate.py` on a clean complete checkout; receipts stay outside the
checkout while validation runs. Repository integrity is separate from mathematical
validation. Record remote head/tree and verify each pushed checkpoint.

## Continuation record

- 12:33 UTC: new pass authorized and begun; previous pass's scope recovered.
- 12:38 UTC: fresh worktrees created from PR218; current PR217/219/220 refs fetched.
- Next: broad agent exploration, root-wide frontier/source review, first substantive
  reconstruction and checkpoint. This pass must remain active until 21:33:06 UTC.
