# Pass 2 self-audit, source pins and execution boundary

**This is a same-author audit, not independent mathematical review.** Four
parallel computational workers were executed; no callable independent-agent
launcher was available. All mathematical statements remain PROPOSED.

## Frozen inputs and provenance

- Parent PR #140, `92981cd32bc3b0d05d28cd98f330246be8b54bc0`:
  `research/novel-swarm-20261030/OCCUPATION.md`, O1--O3;
  `CONCENTRATION.md`, E1--E5; `ADELIC_SHADOWS.md`, A1--A5.
  The fixed-source collision upper bound E5 remains OPEN. No old claim is
  upgraded, and the unavailable original swarm is not used as evidence.
- PR #132, `7687eec1ac364009d644cb8d015f1fe3b28730cc`:
  `research/astra-exit-merging/affine-completeness/PROOF.md`, ACS-002/003.
  The finite-family construction is credited, re-derived and independently
  replayed at the level of complete affine progressions. Its other claims are
  not dependencies of the new rigidity theorem.
- PR #142, `d0f48c472d45a336e9083b37b45e1a8d39a2cf16`:
  `research/beeping-density-swarm-20261030/NEGATIVE_SPIKE_BARRIER.md`, DSP-005.
  The prior fixed-depth positive-source injection is extended to first hits,
  all depths and exact cycle repetitions. No global clipping bound is imported.
- PR #137, `2911b53930cbd31f623d3e0586ca3613854f0143`:
  component-rigidity/inverse-ladder programme, read through current metadata as
  context. R2 is proved independently in full; no uninspected later claim is
  adopted as a premise. PR #141's current metadata was surveyed but its rewrite
  order is not a mathematical dependency.
- Main/parent reading surfaces: README, AGENTS, research map and scoped ERRATA
  at the parent commit. No corrected six-branch/algebraic-section statement is
  reused. In particular the source-indexed invariant theorem is different from
  an automatic controller for a single parity itinerary.
- External dependency only for R6: Christol--Kamae--Mendes France--Rauzy,
  *Suites algebriques, automates et substitutions*, Bull. SMF 108 (1980),
  Theorem 1, Section 5, p.406, DOI 10.24033/bsmf.1926. Primary PDF parsed text
  was checked. The screenshot call failed; no visual check is claimed.

## Mathematical attack checks

**R1--R2.** The compiler does not choose the next bit of one fixed integer.
It produces an actual whole arithmetic progression for each finite family.
That is enough to make a finite monochromatic interval, not to solve Collatz.
The inverse ladder stays positive, odd and a unit modulo three. Its bounded
choice of exponents gives a convergent logarithmic correction, so cone access
uses an irrational rotation with vanishing error rather than an assumed
random distribution of a forward orbit.

**R3--R6.** Canonical digit conventions are explicit. Short suffixes are
obtained from a zero block by *right* zero padding and doubling invariance.
Column observability stabilizes by dimension minus one. Subtracting the block
color adds at most one dimension. For other bases, periodicity is that of the
finite subset automaton, not an assertion that arbitrary automatic sequences
are periodic. The power-of-two bases are handled separately. The characteristic
of the finite field is retained in the external algebraicity theorem. No
finite-complexity hypothesis is asserted for the actual convergence indicator.

**P1--P5.** A fixed-depth injection alone cannot sum all depths when a target
is periodic. First hits and the exact cycle factor repair that issue. The
known cycle 1 contributes factor 16/7 for square pressure; omitting that factor
is rejected by the control. Hypothetical positive cycles are retained using
lambda<1, not removed. The source tail covers infinitely many unexamined
sources even if some never hit the target. Absence for the enumerated finite
sources is certified by their actual arrival at 1. The critical resolvent
bound is an upper growth estimate, not an analytic continuation or a value at
z=1. The 5x+1 cycle 13,33,83,13 prevents claiming summability implies Collatz.

**D1--D2.** Every exponent congruence class is summed to infinity. The cyclic
geometric recurrence is compared with a direct rational kernel at low depth;
all higher-depth laws are checked for exact mass, projectivity, nonnegativity
and closure. The denominator formula is proved, not inferred merely from the
finite output. Arithmetic-operation counts are not called bit-complexity
bounds. Density limits of a fixed forward source are never inferred.

## Actual execution

The compact receipt records source and output hashes. Runs used Python 3.11+
standard-library code with explicit exceptions, not disableable assertions.
Normal four-worker, normal serial and optimized four-worker executions returned
zero and had byte-identical JSON. Results include:

- 903 chart cases with 1,806 literal positive lifts; 128 whole-progression
  families, 8,256 arms; four targeted corruptions rejected.
- 128 inverse ladders visiting each of 64 leading-digit cones, using 6,214
  checked inverse edges; maximum search length 54 steps in this bounded set.
- 7,178 labeled binary-output DFAOs in five stated (base,state-count) classes.
  Every nonconstant candidate had an explicit invariant-equation violation;
  the largest first violating source in these classes was 11. This does not
  establish the theorem for unbounded state counts by enumeration.
- 1,024 exhaustive 2x2 observability cases over F2, plus 680 sharpness
  length/ones-count checks. The latter are not 680 independent matrix models.
- 18 full exact ternary laws through depth 9, covering 59,046 entries, with
  240 entries independently compared against direct congruence aggregation.
- 32,768 odd sources through 65,535: 1,195,565 accelerated transitions,
  followed by 2,379,157 raw shortcut steps in the separate replay. Eight
  all-depth source-tail enclosures and eight exact cross-track upper checks.

These are bounded computations and implementation-diverse checks, not an
independent proof review. The all-depth conclusions use the displayed proofs,
not a finite search extrapolation. No complete-checkout repository validator,
remote CI execution or external formal proof build was performed. The parent
API reads and additive packet execution do not substitute for those events.

## First unsupported inference / priority

The exact missing inference is still either fixed-source forward regularity
strong enough for parent E5, or a finite-complexity theorem for an actual
nonconstant candidate invariant. Inverse pressure does not currently imply
either. A claim that these results are new to the external literature has not
been established. Independent review should prioritize the all-base R5 proof,
the first-hit/cycle decomposition P2, and the critical summation bound P4.
