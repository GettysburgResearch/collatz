# T-6903 — divergence forces a tau-infinite integer or infinitely many deep CST violations

**Claim ID:** `T-6903`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** `T-6902`  
**Scope:** positive divergent shortcut-Collatz trajectories  

## Statement

If a positive shortcut-Collatz orbit tends to `+infinity`, then exactly one of the following alternatives occurs along its tail-minimum sequence `h_i`.

### Alternative A — coefficient-supercritical ordinary failure

For some `i`,

\[
\boxed{t(h_i)=\tau(h_i)=\infty.}
\]

Thus one positive ordinary integer has all-time coefficient supercriticality. Branch-qualified PR #77 then gives

\[
T^k(h_i)\to+\infty.
\]

### Alternative B — an infinite staircase of CST counterexamples

Every `tau(h_i)` is finite, and

\[
\boxed{
 h_i\to\infty,
 \qquad
 \tau(h_i)\to\infty,
 \qquad
 t(h_i)=\infty>\tau(h_i).}
\tag{1}
\]

Hence the integers `h_i` are infinitely many distinct counterexamples to Terras's coefficient-stopping equality, with both their starting values and coefficient stopping depths escaping to infinity.

## Proof

`T-6902` gives distinct tail minima `h_i` with

\[
t(h_i)=\infty,
\qquad
h_i\to\infty,
\qquad
\tau(h_i)\to\infty.
\]

If any `tau(h_i)` is infinite, Alternative A holds. Otherwise every `tau(h_i)` is finite, so each strict inequality

\[
t(h_i)=\infty>\tau(h_i)
\]

is a CST violation, and Alternative B follows. ∎

## Sufficient positive proof package

The following three statements together imply the Collatz conjecture.

1. There is no nontrivial positive cycle.
2. Every positive integer has finite coefficient stopping time.
3. Terras's equality `t(n)=tau(n)` holds for all sufficiently large positive integers.

Indeed, if Collatz were false and there were no cycle, a nonconvergent positive orbit could not revisit a bounded set infinitely often and therefore would tend to infinity. Alternative A contradicts statement 2. Alternative B supplies arbitrarily large CST violations, contradicting statement 3.

This package is deliberately weaker than requiring full CST equality at every positive integer. It is nevertheless open and should not be presented as a resolution.

## Comparison with Rozier--Terracol

Rozier--Terracol prove that one infinite-stopping integer generates infinitely many paradoxical finite sequences, sometimes after multiplying its start by powers of two. `T-6903` is complementary:

- its starts are actual tail minima on one divergent orbit;
- the starts are pairwise distinct and tend to infinity;
- their coefficient stopping depths tend to infinity;
- when finite, they directly violate `t=tau`.

No global novelty claim is made without a broader literature comparison.

## Gap audit

- Alternative A is a possible Collatz failure mode, not a contradiction.
- Alternative B is compatible with the present literature, which supplies only bounded computations and heuristics about CST violations.
- Eventual CST and universal coefficient-stopping finiteness remain separate unproved statements.
