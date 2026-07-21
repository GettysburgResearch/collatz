# KTHM-0007 — Skolem–Mahler–Lech and the nondegenerate power-sum corollary

**Source:** Bell's theorem exposition and historical review. [@Bell2019]  
**Proof status:** SML used as a black box; corollary proved  
**Maps to:** intended external input of `CLAUDE/T-0006`; possible future schema audits

## Black-box theorem

Let `(u_n)` be a linear recurrence sequence over a field of characteristic zero. Then

\[
\{n\ge0:u_n=0\}
\]

is the union of a finite set and finitely many full arithmetic progressions.

## Nondegenerate power-sum corollary

Let

\[
u_n=\sum_{i=1}^r c_i\alpha_i^n
\]

with nonzero `c_i,α_i` in a characteristic-zero field. Assume `α_i/α_j` is not a root of unity whenever `i≠j`. Then `u_n=0` for only finitely many `n`.

## Proof of the corollary

The power sum is a linear recurrence sequence. If it had infinitely many zeros, SML would give an infinite arithmetic progression of zeros, say

\[
u_{n_0+qm}=0\qquad(m\ge0).
\]

Put `d_i=c_iα_i^{n_0}` and `β_i=α_i^q`. Nondegeneracy makes the `β_i` distinct. For `m=0,…,r-1`,

\[
\sum_i d_i\beta_i^m=0.
\]

The coefficient matrix is Vandermonde and invertible, so every `d_i=0`, contradicting `c_iα_i^{n_0}≠0`. ∎

## Application checklist

A repository claim must expose the fixed sequence, field, coefficients, bases, and root-of-unity ratios. SML is qualitative; it ordinarily supplies no usable last-zero bound.
