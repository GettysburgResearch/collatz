# Three-hour proof pass: the median collision threshold and semiprimes

**Collatz remains unresolved. The pass is active.** The requested interval is November 28, 2026, 08:52:20–11:52:20 UTC. This packet continues PR #214 at `504d29d399efa941a62006d1ea4635385ce6bb5f` and keeps its analytic and formal dependencies explicit.

The goals are to force the actual median synchronous collision probability to its maximal value \(1/8\), and to identify whether the semiprime work in `gfreund123/factoring-in-p` supplies a missing arithmetic step. Arguments, failed routes, source pins and reviews are kept here rather than in long chat updates.

## First result: an unconditional number-theoretic bridge to full convergence

[Semiprime sufficiency](SEMIPRIME_SUFFICIENCY.md) proves a proposed, source-qualified reduction to
\[
\mathcal S=\{pq:p<q\text{ prime},\ \log(pq)<p\le(\log(pq))^2\}.
\]
Every positive-density Collatz component union contains \(\gg X/\log X\) such semiprimes through \(X\). With the imported positive-predecessor theorem, convergence on this family, or upper relative density one of convergence within it, is equivalent to full Collatz convergence.

The arithmetic step combines the unconditional Matomäki–Teräväinen short-interval semiprime lower bound with actual pair-fusion cylinders and a Brun–Titchmarsh upper bound in each failing residue. This retains the sparse population's normalization. It does not remove RH from the distinct ordered-prime-product independence theorem in recent Paper 233.

The factors of every member of this sufficient family are already findable in polynomial time by trial division. The outstanding task is a dynamical convergence or descent theorem on the family. Factor recovery itself does not discharge it.

## The collision endpoint and its exact open estimate

[The collision threshold](COLLISION_THRESHOLD.md) proves the full countable-series
deficit bound \(1/8-L\ge b(1-b)/4\), including arbitrary nonperiodic mass.
Eight freshly checked Lean roots give the exact maximal-mass equivalence and
its quantitative approximation. This formalizes the endpoint reduction; it
does not prove the missing lower bound.

The new [boundary zero-one theorem](collision/DYADIC_BOUNDARY_ZERO_ONE.md)
gives a different sufficient condition: the reciprocal sum of the exact
asynchronous component boundary is finite if and only if Collatz holds,
using the positive-predecessor input. It uses both exact branches and avoids
the Gaussian law. An [explicit construction](collision/SHARP_HALVING_BOUNDARY.md)
shows why exact halving and an \(O(X/\log X)\) boundary count alone cannot close it.

## What the factoring work supplies, and what its import needs

The [source audit](factoring/FACTORING_BRIDGE.md) and
[pointwise import audit](factoring/POINTWISE_IMPORT_AUDIT.md) inspect twenty
complete files at immutable factoring PR heads. The reversible sampler in PR 296 is
a real arithmetic coverage theorem, but its positions are not actual
Collatz merger certificates. PR 359's \(1/8\) is a total-variation tolerance
for a factoring-equivalent sampler, unrelated to the Collatz collision endpoint.

The [actual multiplier theorem](factoring/MULTIPLIER_CERTIFICATE_RIGIDITY.md)
proves that a multiplier with a prime factor other than two and three has
at most one genuine source per pair of affine word cells. The full bounded-clock
census is at most \((2h+1)2^h\); the unbounded two-adic Haar merger event is
countable and null. These restrictions are compatible with universal
ordinary convergence. Three Lean roots certify the algebra and its actual-path
interface.

The [high-state spectral obstruction](arithmetic/HIGH_STATE_AND_PROFILE_OBSTRUCTIONS.md)
shows that a doubly stochastic sampler certified by actual Collatz paths of
length at most \(L\), staying above \(M\), has Poincaré gap at most
\(C(\eta+L^2/M)\), where \(\eta\) is the remaining transition weight.
Long-range endpoints alone do not create the required expansion. The same note
rules out global inverse supersolutions comparable to a sublinear power by
an explicit positive-integer all-one chain.

A separate [finite-residue spectral theorem](factoring/FINITE_AFFINE_GAP.md)
tracks the exponent, denominator and translation budgets of native affine
charts. It gives an explicit vanishing-gap regime even after granting extra
sign operations. The factoring sources' pointwise quaternionic estimate,
ordered-product algorithms and analytic integer-zero method still need a
representation of the full ordered Collatz carry together with its real window.

## Work in progress

- `collision/`: direct attack on the \(1/8\) lower bound, exact boundary amplification and the distinction between a positive lower bound and the maximal one.
- `factoring/`: source-level audit of the relevant factoring PRs, their reversible coverage constructions, and whether they can be implemented by actual Collatz mergers.
- `arithmetic/`: independent audit and a separate attack on integer inverse profiles and escape.

The separate PR #216, at `1917b07ae5cc8f5d27c79f34cc43a4bcf25efff8`, already supplies near-quadratic widely separated median-clock first meetings and positive conditional density bounds. Its result does not establish \(1/8\); this pass does not claim those counts as new.

## Checkpoints

| Checkpoint | Scientific content | Evidence |
|---|---|---|
| 1 | Uniform sparse semiprime transfer and the resulting sufficient-family theorem | Original input clauses read; independent reconstruction of the weighted failure bound and all quantifiers; complete repository integrity gate before publication |
| 2 | Full collision-series endpoint, summable-boundary equivalence and sharp halving control; cross-repository factoring audit and actual multiplier obstruction; high-state spectral and inverse-envelope obstructions | 24 new Lean roots across four modules, each freshly compiled and separately audited; exact binary controls through 262,144 in normal and optimized Python; three independent written semiprime audits |

[Intake pins](INTAKE_PINS.json) record source versions and the exact starting heads. The [checkpoint 1 review](../../reports/astra-collision-factor-bridge-20261128/checkpoint01/REVIEW.md) states the review boundary. Repository integrity and finite Lean kernels do not certify imported analytic inputs or a full Collatz proof.
