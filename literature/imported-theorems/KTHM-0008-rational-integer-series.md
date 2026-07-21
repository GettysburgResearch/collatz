# KTHM-0008 — Reciprocal poles of a rational integer power series are algebraic integers

**Source context:** Fatou/Pólya–Carlson literature; a modern discussion appears in Borwein–Coons. [@BorweinCoons2009]  
**Proof status:** complete independent proof  
**Maps to:** the external rational-series step in `CLAUDE/T-0020`

## Statement

Let

\[
F(z)=\sum_{n\ge0}a_nz^n\in\mathbb Z[[z]]
\]

be a rational function. Write `F=P/Q` in lowest terms with `P,Q∈Q[z]` and `Q(0)≠0`. If `α` is a pole of `F`, then `α^{-1}` is an algebraic integer.

Equivalently, every characteristic ratio that actually occurs in the coefficient sequence is an algebraic integer.

## Proof

First justify `P,Q∈Q[z]`. Since the integer sequence `(a_n)` is rational-recursive over `C`, its infinite Hankel matrix has finite rank. Choose a minimal recurrence order and a nonsingular finite Hankel minor. Solving the corresponding recurrence equations by Cramer's rule uses only integer entries, so the recurrence coefficients are rational. Multiplying the recurrence by the generating series gives a representation over `Q(z)`.

Let `K` contain a pole `α`. For any finite nonarchimedean place `v` of `K`, suppose `|α|_v<1`. Because every `a_n` is an integer, `|a_n|_v≤1`; hence the series `Σa_nα^n` converges in `K_v`. The formal identity

\[
Q(z)F(z)=P(z)
\]

may therefore be evaluated at `z=α`, giving `P(α)=0` because `Q(α)=0`. This contradicts the coprimality of `P` and `Q`. Thus `|α|_v≥1` at every finite place.

Consequently `|α^{-1}|_v≤1` at every finite place. The standard valuation characterization of algebraic integers now shows that `α^{-1}` is an algebraic integer. ∎

## Repository corollary

A rational noninteger such as `(N/M)^U` in lowest terms with `M>1` is not an algebraic integer. It therefore cannot be an actual characteristic ratio of an integer sequence with rational generating function.

## Scope limitation

The theorem does not show that an arbitrary integer sequence has a rational generating function. That hypothesis must be supplied by the repository's finite exp-polynomial schema definition.
