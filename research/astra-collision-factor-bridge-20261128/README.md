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

## Work in progress

- `collision/`: direct attack on the \(1/8\) lower bound, exact boundary amplification and the distinction between a positive lower bound and the maximal one.
- `factoring/`: source-level audit of the relevant factoring PRs, their reversible coverage constructions, and whether they can be implemented by actual Collatz mergers.
- `arithmetic/`: independent audit and a separate attack on integer inverse profiles and escape.

The separate PR #216, at `1917b07ae5cc8f5d27c79f34cc43a4bcf25efff8`, already supplies near-quadratic widely separated median-clock first meetings and positive conditional density bounds. Its result does not establish \(1/8\); this pass does not claim those counts as new.

## Checkpoints

| Checkpoint | Scientific content | Evidence |
|---|---|---|
| 1 | Uniform sparse semiprime transfer and the resulting sufficient-family theorem | Original input clauses read; independent reconstruction of the weighted failure bound and all quantifiers; complete repository integrity gate before publication |

[Intake pins](INTAKE_PINS.json) record source versions and the exact starting heads. The [checkpoint 1 review](../../reports/astra-collision-factor-bridge-20261128/checkpoint01/REVIEW.md) states the review boundary. Repository integrity and finite Lean kernels do not certify imported analytic inputs or a full Collatz proof.
