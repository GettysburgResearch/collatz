# Exact formalization boundary

**The two new modules contain 24 public theorems with explicit axiom
audits. They do not declare the Collatz conjecture.** Both are independent
of local Collatz modules and import only Mathlib. Runtime pins and source
hashes are in `DEPENDENCIES.json`; actual executions are recorded separately.

## OriginalSourceEntropy.lean: 21 declarations

The main theorem `finite_original_source_entropy_of_mean` takes a finite
index type, arbitrary nonnegative sample weights summing to one, and exact
integer path equations

\[
3q+1=2^gq'.
\]

Each sample has a word of length \(m\). Symbols \(v_i\) encode positive
gaps \(g_i=v_i+1\), so `excess` is \(\sum_i(g_i-1)\). If \(a>1\) and the
weighted mean excess is at most \(m(a-1)\), the entropy of the **actual
endpoint residue distribution modulo \(3^m\)** is at most \(m\Phi(a)\).

There is no independence, stationarity or stochastic-gap assumption on
the samples. The product geometric law appears only as a reference
subprobability in a cross-entropy comparison. The finite cap `M` bounds a
given finite sample, with no uniform cap asserted for an infinite orbit.

| Declarations | Verified content |
|---|---|
| `entropy_le_crossEntropy` | Logarithmic comparison against a strictly positive finite subprobability |
| `push_nonneg`, `le_push`, `push_sum`, `sum_push_mul`, `push_comp` | Exact finite pushforward bookkeeping |
| `entropy_push_le` | Entropy decreases under a deterministic finite projection |
| `geometric_mass`, `codeProb_pos`, `codeProb_sum_le`, `log_codeProb` | Truncated geometric product and its log-cost identity |
| `finite_word_entropy_bound` | Arbitrary joint word law bounded by geometric cross-entropy |
| `gapPath_affine`, `same_word_same_ternary_endpoint`, `endpoint_eq_code`, `physical_endpoint_code` | Affine path identity and the source-independent residue decoder |
| `finite_original_source_entropy` | The preceding inequality transferred to actual endpoint residues |
| `finite_original_source_entropy_of_mean` | Optimized \(a>1\) bound \(m\Phi(a)\) |
| `sliding_window_cost_le` | Every nonnegative gap cost occurs at most \(m\) times in all windows |
| `single_gap_log_identity`, `finite_gap_log_budget` | Exact positive-real logarithmic recurrence and finite telescope |

`GapPath` deliberately stores algebraic equations only. It is broader than
the accelerated Collatz path type; all actual positive odd trajectories
satisfy those equations. Thus the finite theorem includes all actual
samples but does not assert that every algebraic path is an exact
valuation itinerary. No such converse is needed.

The combined finite formula E1 in `ACTUAL_ORBIT_ENTROPY.md` still uses a
written construction of the uniform sliding-window family and its cost
estimate from these formal ingredients. The special mean-one case,
nonperiodicity-to-escape deduction, Cesaro limit of the correction, weak
empirical limits, entropy dimension, collision bound and speed refinement
also remain written mathematics. Independent reviews verify those
arguments at that scope; they are not Lean declarations in this packet.

## CycleWordEntropy.lean: three declarations

For natural numbers \(0<p\le A\) in the cone \(4A\le7p\), the module
proves the weighted binomial bound, the associated cone-weight inequality,
and, for \(A>0\),

\[
\binom Ap^7<120^A.
\]

The theorem declarations are `weighted_binomial_bound`, `cone_weight_bound`
and `cycle_word_count_bound`. The first two also cover the degenerate
parameters stated in their source. These are exact arithmetic theorems.

The written deductions that a nontrivial positive cycle lies in the cone,
that a small support prevents uniformity modulo the full denominator, and
that a primitive cycle supplies \(A\) zero-residue rotations are separately
reviewed. The asymptotic denominator estimate uses the explicitly stated
existing Matveev specialization as a SOURCE-QUALIFIED analytic input. It
is not a Lean axiom. GRH is neither assumed nor proved in either module.

## Trust and replay

The checker compares source and review hashes, compiles with warnings as
errors, and accepts only `propext`, `Classical.choice`, and `Quot.sound`
in the transitive theorem audits. It rejects unfinished or native-evaluated
proof mechanisms and requires the audit set to equal the public theorem
set. Compiler artifacts and logs are written outside the tested checkout.

This establishes the stated finite theorems. The repository integrity gate
establishes repository consistency. Neither is evidence for an unproved
lower entropy bound, zero-atom exclusion, source selector, or full Collatz.
