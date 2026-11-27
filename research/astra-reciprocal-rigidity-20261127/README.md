# Ordinary merger costs, cycle mismatches, and analytic rigidity

**PROPOSED research. The Collatz conjecture remains OPEN.** This packet uses
the positive shortcut map `T(2x)=x`, `T(2x+1)=3x+2`, with odd acceleration
only where explicitly stated. Its first checkpoint combines independently
read arithmetic proofs, fresh Lean builds, exact finite controls, and
clearly identified external analytic inputs. None of those evidence levels
is silently promoted to a proof of universal convergence.

## Results worth carrying forward

| Result | Exact scope | Evidence |
|---|---|---|
| Kernel formalization of the prior ternary merger barrier | If `3^K | n−s`, `s=0` or `1`, and the first `j` departures of `n` are odd, every positive `m<n` reaching that endpoint at any clock uses more than `K+j` odd steps. | Unified Lean proof and deterministic readout of the written PR146 barriers; exact prior paths are credited below. |
| A finite ordinary certificate increases that bill at all future clocks | For all `K≥84`, the same family needs more than `K+j+12` odd steps. The lower native clock is unbounded. | Lean evaluates 648 finite ordinary trajectories and proves their all-time consumer. |
| A single halving can collapse the optimal merger cost | On the stated second-halving family, the optimal smaller visitor uses exactly `H−1` odd steps, after an immediately preceding endpoint can require arbitrarily more than `H+K`. | Exact ordinary witness and all-clock lower bound, Lean kernel proof; antecedent merger families credited. |
| Every cyclic shift is constrained by the complete reduced denominator | A primitive rational cycle of length `n`, minimum `m`, denominator `d`, and shift mismatch count `s` satisfies `n < H_s(1+log₂(d(m+1))+(log₂3)s/2)`. No restriction on the order of the shift. | Elementary written proof; finite physical pair, mismatch-mask, and arithmetic kernels in Lean. |
| Few-mismatch shifts have short rational approximations | If `n≥4s(1+log₂(d(m+1)))`, some `1≤q≤8s` has cyclic distance `|qh|_n≤2s²`. At most `32k³+32k²+4k` shifts have at most `k` mismatches under the corresponding hypothesis. | Written finite proof and exact bounded rational-cycle controls. |
| An ordinary bad component forces a full natural boundary at every positive exponent | Canonically normalized squared-slope masses are either zero or have `n²a_n` uniformly bounded above and away from zero. Every nonempty bad support gives a natural boundary for `Σ a_n^(s/2) z^n`, for every real `s>0`. | Written proof using deterministic ordinary basin blocks, finite reciprocal packing, and a right-limit argument. |
| The mixed equations admit an explicit analytic obstruction inside the known component | The actual predecessor tree of 5 supplies the same natural boundary with one monomial of forcing, while preserving the exact dyadic section relation. | Ordinary construction and exact coefficient identities; no hypothetical bad orbit required. |
| Finite recurrence complexity has an explicit lower bound | A nonzero rational prefix obeying `4a(2n)=a(n)` and a constant-coefficient recurrence of order `d` through index `N` must satisfy `N+2<4d`. | Lean kernel proof, including the primitive-annihilator and denominator arguments. |

Here `H_s=1+α+⋯+α^s` and `α=log₂3`. The cycle corollaries “42
mismatches at every proper shift” and “134 when `n≥2^100`” additionally
use the explicitly cited effective height and verified period inputs.
Those external proofs and large computations have not been rebuilt here.

## Reading paths

- [Descent and postpeak coverage](descent/README.md) states the physical
  barriers, exact inverse prices, successful families, and remaining
  residual sources. It also proves that asking for the finite-prefix
  oracles at every size would itself be equivalent to full Collatz.
- [The instantiated finite anchor](root/ANCHOR_BUDGET.md) explains why 648
  kernel checks give an all-time theorem, and separates arrival defects
  from larger intermediate prefix excesses.
- [Cycle arithmetic](cycles/README.md) includes the all-shift denominator
  bound, its lag spectrum, genuine ordinary obstructions to translated
  prime potentials, and a source-qualified first-exit theorem.
- [Ordinary analytic rigidity](rigidity/README.md) builds one physical
  coefficient array, proves finite recurrence obstructions, and uses
  ordinary blocks to remove the exceptional exponents from a more general
  right-limit result.
- [Review boundary and remaining gaps](REVIEW_BOUNDARY.md) explains how
  these results relate to the current frontier and why their combination
  still stops short of universal convergence.

## Second checkpoint

[The second checkpoint](SECOND_CHECKPOINT.md) adds an exact finite-word
criterion for discounted postpeak mergers at all lower clocks, the scaled
and postpeak consumers of the twelve-extra-odds certificate, and the
complete cyclic assembly of the all-shift kernel proof. It also develops
collective lag and edit-distance restrictions with explicit predecessor
credit, and proves that a broad algebra of local arithmetic and log-height
operators has the same essential norms on every ordinary component.
The latter identifies a limitation of those tests; it does not identify
all components with the known basin or settle the exact kernel at 1.

## Third checkpoint

[The third checkpoint](THIRD_CHECKPOINT.md) gives a finite executable
decision for bounded odd-step smaller visitors at every lower clock,
including the exact scale-sensitive postpeak consumer. It proves the
sharp six-even residual threshold, full-denominator restrictions for
two-swap rotations and boundedly many odd runs, and an exact cyclotomic
formula for symbol-dilation denominator exponents. Its ordinary clock
bound sums the largest fibers across every component. A separate
small-anchor theorem forces a physical return under a bounded-piece
decomposition, with the corresponding rational denominator cost retained.
The new decision procedure, structural hypotheses, and averaged clock
estimate do not themselves supply universal convergence.

## Fourth checkpoint

[The fourth checkpoint](FOURTH_CHECKPOINT.md) proves an all-modulus
numerator estimate and a total-variation law for the complete reduced
denominator, with the fixed-dictionary congruence obstruction retained.
A corrected signed quadratic energy strengthens the kernel-checked
postpeak height from `21q+9K+3` to `6q+3K+3`. The wider-band theorem
forces a smaller ordinary merger or a matching physical exit through
ratio `2^(51/20)`. Elementary inverse banks give uniform moving-target
families and a two-term count near the fastest first-hit clocks. The
rare integer denominator atom, upward exits, and future of an arbitrary
target remain explicit gaps.

## Fifth checkpoint

[The fifth checkpoint](FIFTH_CHECKPOINT.md) gives explicit simultaneous
cycle-defect budgets for the four open mod-eight avoidance classes,
uniform interval counts for two precisely defined survivor families,
and canonical-cut lists for each large complete divisor. The common
all-scales protection set now exceeds one third of ternary space, with
more than one quarter protected inside its zero residue alone. The
ordinary first-hit exponent near the fastest clock agrees with the
ternary-filtered entropy expression to all algebraic orders in the
small excess. The order of limits and the possible exceptional single
source or cycle remain explicit.

## Source intake and credit

The branch starts from main at
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
[INTAKE.json](INTAKE.json) freezes the complete 146-open-PR metadata
inventory at the recorded observation time, including full head SHAs.
That inventory is a source map, not a claim to have independently checked
all proofs in those pull requests. The integrated research map, cumulative
catalog, scoped errata, and recent frontier packets were read before
choosing these directions. Each subpacket supplies exact source paths and
head pins for its substantive comparisons.

Several attractive initial directions were already covered in the recent
work: fixed-clock modular routing, polynomial-height entropy, and the
basic neighboring postpeak mergers. The present claims retain those
credits. A new kernel proof or synthesis is not labeled as historical
priority over its written antecedents.

The second source pass found the exact antecedents of the basic `K+j`
merger barrier in PR146's `THREE_RAY_SMALLER.md` and `ADJACENT_DESCENT.md`,
and its prepaid-origin architecture in `NEGATIVE_FIVE_CHECKPOINT.md` and
`EXCESS_DENSITY.md`, all at `f431078244e868dc699fad011044f0d5e7f76437`.
The [descent note](descent/README.md) now records the correction explicitly.
The basic barrier is a formalization, not a newly discovered theorem.

## Replay

Lean requires version 4.34.1 and mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`, with its built dependencies.
The [packet replay driver](replay_lean.py) topologically orders local
imports, uses a fresh local output directory, turns warnings into errors,
records source hashes, and rejects printed nonstandard axioms.

```bash
python -B replay_lean.py --lean /path/to/lean --mathlib /path/to/mathlib4 --receipt /outside/checkout/lean-replay.json
```

Each subpacket has its own finite arithmetic replay commands. Retained
Python data are bounded calculations. Their normal and optimized replays
are recorded separately from Lean compilation. The repository validator
checks repository integrity, preservation, and its enumerated old
regressions; it does not validate the mathematical conclusions here.

## First unsupported steps

For descent, we still need a smaller physical merger for every fixed
residual source. For cycles, a word with many mismatches at every lag can
still pass the new restrictions. For analytic rigidity, no argument
forces the homogeneous ordinary mass series to continue through an arc;
the forced ordinary example shows why broad regularity claims fail.
The same-source first-moment extinction target in PR200/201 remains
unproved. Each of these is an explicit mathematical obligation, not an
assumption inserted into a purported final proof.
