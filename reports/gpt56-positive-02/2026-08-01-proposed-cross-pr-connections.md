# PROPOSED cross-PR connections from the pre-public review

**Status:** **PROPOSED / STRATEGIC CONNECTIONS ONLY**  
**Author:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Date:** 2026-08-01  
**Reviewed frozen sources:** PR #6 `4810a077`, PR #11 `7950713c`, PR #12 `7ea63c56`, PR #13 `de739355`

Nothing in this note changes a reviewed claim status. These connections require separate proofs before use as theorem dependencies.

## 1. Exact safety kernels should replace weak-component inequalities

PR #6 `R-9001` shows that weak connectivity to a cycle does not imply a lower bound by the cycle minimum. PR #12 `L-9103` gives the correct finite-state substitute whenever the relevant dynamics have been represented by a finite relation:

\[
F_{\max}=Q\setminus\operatorname{Pre}_R^*(B).
\]

**Proposed use:** any finite cycle/inverse-tree argument that currently reasons from SCC or weak-component membership should instead encode the actual bad set and compute its complete predecessor closure. This will either produce a genuine safe kernel or a concrete finite counterexample path.

This does not solve infinite-state or arithmetic value-space problems.

## 2. A restricted salvage route for tensor-radius freeze

PR #11 `T-0104/T-0105` fail because a new difference of size `2^L` can almost cancel an old difference. PR #13 `LIT-KTHM-0024` proves the corrected sufficient condition

\[
\operatorname{diam}(D_0)+R(D_0)+1<2^L.
\]

PR #12 `L-9112/L-9114` show that exact carry/refinement constraints can sharply restrict the reachable residual set in a finite control slice.

**Proposed theorem target:** for a concrete carry slice, prove an inductive diameter bound strong enough to imply the corrected separation inequality at every tensor stage. If established, this would recover radius freeze for that restricted family without reviving the false unconditional theorem.

No such inductive diameter estimate is proved here.

## 3. Fixed-support pulse tools should feed the complete-denominator compiler

PR #13 source-audits Matveev and finite-place two-logarithm tools and proves proposed fixed-support pulse closures below the positive largest-gap rate. The repository’s first-crossing work reduces the remaining cycle/near-return problem to divisibility by the complete denominator

\[
2^j-3^q.
\]

**Proposed unification:** eliminate the pulse-baseline restriction by deriving, from a general complete first-crossing word, a finite family of shifted resultants whose product captures the full denominator. Then combine:

1. Archimedean logarithmic separation;
2. fixed-prime valuation bounds;
3. a fresh-prime theorem for the denominator; and
4. exact replay of the surviving finite exceptional families.

The load-bearing missing statement is a uniform theorem that at least one fresh denominator prime avoids every shifted numerator/resultant for growing support. Current source theorems only show that fresh denominator primes must exist, not that the numerator cannot share them.

## 4. Why this is a serious but incomplete full-resolution path

If the proposed full-denominator bridge closes `FC*`, the separate `SC*` fixed-source problem remains. A complete Collatz proof still requires a source-dependent upper bound on

\[
v_2(3^{q(w)}n+A_w)
\]

for all all-prefix-supercritical words from each fixed positive integer `n`.

Thus the serious repository-wide route is two-front, not a single repaired PR:

```text
fixed-source valuation closure (SC*)
+
complete-denominator fresh-prime/resultant closure (FC*)
=
least-counterexample contradiction.
```

Both missing theorems remain **PROPOSED targets**, not results.
