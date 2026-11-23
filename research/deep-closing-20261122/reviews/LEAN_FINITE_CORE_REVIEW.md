# Independent mathematical review of the finite entropy core

Date: 2026-11-22.
Reviewer: the independent `deep_escape` lane, author of the written
entropy deduction but not author of the Lean implementation.

**Verdict: VERIFIED at the mathematical statement/implementation-interface
level.** Compiler execution and axiom auditing are separate evidence to
be supplied by the root task. This review did not execute Lean and makes
no claim about a later source revision.

Reviewed source:
`collatz_work/deep_root/OriginalSourceEntropy.lean`, SHA256
`4b40c2c433751eeb72c3ceceb1c32df149d70dc7e99cf60ca7a066642be492ea`.
The publication may change the containing path; the hash identifies the
reviewed bytes.

## Scope reconstructed

1. `entropy_le_crossEntropy` uses a nonnegative probability `p` and a
   strictly positive subprobability reference `q`. The termwise inequality
   from `log t <= t-1` gives the correct direction; summing the unused
   reference mass gives a nonpositive remainder. Zero masses use the
   continuous convention `0 log 0 = 0`.

2. `push` retains all weights on each complete finite fibre. `push_sum`,
   `sum_push_mul`, and `push_comp` retain normalization and every collision.
   `entropy_push_le` is valid for any nonnegative finite weight, even
   without a normalization hypothesis, because the common total-mass
   contribution cancels under deterministic pushforward.

3. The geometric product is only a reference distribution. The actual
   word law `p` has no independence assumption. Its values encode
   `gap-1`; consequently `excess` is the total gap cost minus the word
   length. Summing the truncated geometric product gives a subprobability,
   so no missing long-gap mass is renormalized.

4. The exact `GapPath` equations imply
   `3^length*n + offset(word) = 2^sum*endpoint`. Since powers of two and
   three are coprime, two such paths with the same word have the same
   endpoint modulo `3^length`, regardless of their initial sources.
   Allowing zero or nonexact valuations in the general affine relation
   weakens its hypotheses; genuine positive odd trajectories are included.

5. `ternaryCode` uses one chosen endpoint only to define the common
   residue for an observed word; the preceding uniqueness theorem makes
   that choice immaterial. Its arbitrary fallback on unrealized words
   causes no loss: those words receive no mass in the actual sample law.

6. `finite_original_source_entropy` applies the deterministic code to
   an arbitrary finite weighted family of physical affine paths. Pushing
   the source weights through words and then endpoints is exactly the
   same as pushing directly through endpoints. Thus its final entropy
   includes all actual source collisions, and its mean excess remains
   attached to the original weighted family.

7. `finite_original_source_entropy_of_mean` takes an explicit upper
   bound on the actual mean excess, with reference mean `a>1`, and
   chooses `rho=(a-1)/a`. Since `-log rho` is positive, the excess-cost
   upper bound has the correct direction. Its final expression is
   exactly `m*Phi(a)`, not an independent-gaps assumption.

8. `sliding_window_cost_le` uses every original sample with its actual
   multiplicity, at most `m`. For fixed window coordinate `j<m`, the
   injective map `k -> k+j` sends the `N-m+1` window positions into
   `0,...,N-1`. Nonnegative extra entries give the inequality. Empty
   windows and zero-length endpoint cases are harmless. Taking its
   sequence at index `i` to be the written gap `g_(i+1)` matches the
   indexing of E7 exactly.

9. `single_gap_log_identity` and `finite_gap_log_budget` retain the
   positive correction `log(1+1/(3q))` with the correct sign. They use
   positive real values satisfying the actual finite recurrence, and
   the latter sums by telescoping. No boundedness of that correction,
   orbit divergence, or asymptotic passage is assumed inside the finite
   theorem.

### All 21 public declarations in scope

| Declarations | Count | Reviewed mathematical role |
|---|---:|---|
| `entropy_le_crossEntropy` | 1 | Finite Gibbs inequality against a positive subprobability |
| `push_nonneg`, `le_push`, `push_sum`, `sum_push_mul`, `push_comp` | 5 | Complete finite source fibres, mass and test-function preservation |
| `entropy_push_le` | 1 | Entropy decreases under the actual deterministic projection |
| `geometric_mass`, `codeProb_pos`, `codeProb_sum_le`, `log_codeProb` | 4 | Positive truncated product reference and exact logarithmic cost |
| `finite_word_entropy_bound` | 1 | Arbitrarily dependent finite word distribution |
| `gapPath_affine`, `same_word_same_ternary_endpoint`, `endpoint_eq_code`, `physical_endpoint_code` | 4 | Exact ordinary affine paths and deterministic ternary endpoint code |
| `finite_original_source_entropy`, `finite_original_source_entropy_of_mean` | 2 | Composition with the unchanged original weighted source family |
| `sliding_window_cost_le` | 1 | Each physical gap is counted at most once per window coordinate |
| `single_gap_log_identity`, `finite_gap_log_budget` | 2 | Finite real logarithmic identity and complete telescope |
| **Total** | **21** | **Finite mathematical core only** |

## Relation to the full written theorem

For the sliding-window sample in `ACTUAL_ORBIT_ENTROPY.md`, take the
sample index to be `k=m,...,N`, weights `1/(N-m+1)`, and a finite cap at
least the largest of the finitely many observed gaps. Code each gap as
`gap-1`. Every actual window is then one of the exact paths assumed by
the Lean theorem.

The formalized sliding multiplicity inequality bounds the mean excess
by `m*(A_N/(N-m+1)-1)`. The optimized geometric theorem gives the written
finite bound E1 when that reference mean exceeds one; its mean-one
endpoint is handled in the written proof. The formal logarithmic
telescope supplies the exact identity E8 after conversion of logarithm
bases. The written proof then uses escape from bounded ordinary sets,
the vanishing average correction, fixed-precision continuity of finite
entropy, and weak empirical limits.

This source does **not** formalize those later asymptotic passages, the
entropy-dimension value, collision-energy consequence, or full escape
exclusion. The observed-window construction and its composition into
E1 are explained in writing, using the three finite interfaces just
listed; no monolithic theorem named E1 is claimed. The proved finite
input is substantive, and does not assume an entropy bound as an opaque
hypothesis. Axiom/compile evidence cannot extend its mathematical claim
beyond its stated finite domain.
