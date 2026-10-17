# LIT-KTHM-0006 — primitive-substitution letter frequencies are algebraic

**Source:** Perron–Frobenius theory for integer incidence matrices; standard substitution-dynamics corollary
**Proof status:** complete proof of the algebraicity statement

## Statement

Let `sigma` be a primitive substitution on a finite alphabet, and let an infinite fixed point of `sigma` have letter frequencies. Then every letter frequency is an algebraic number.

## Proof

Let `M` be the incidence matrix of the substitution: `M_{ij}` counts occurrences of letter `i` in `sigma(j)`. The matrix is nonnegative integral and primitive. Perron–Frobenius theory gives a simple dominant eigenvalue `lambda>0` and a strictly positive right eigenvector `v`; normalized coordinates of `v` are the letter frequencies of the primitive fixed point.

Because `M` has integer entries, `lambda` is a root of the monic characteristic polynomial of `M`, hence an algebraic integer. The nullspace of `M-lambda I` can be solved over the number field `Q(lambda)`, so `v` may be chosen with all coordinates in `Q(lambda)`. Dividing by the nonzero algebraic number `sum_i v_i` preserves algebraicity. Therefore every normalized coordinate, and hence every letter frequency, is algebraic. ∎

## Native application

The transcendental frequency in `LIT-KTHM-0004` cannot be the letter frequency of a fixed primitive substitution. This supports the limited claim that one stationary primitive-substitution grammar cannot track the exact `64→81` boundary slope.

## Non-applications

The theorem does not exclude:

- nonprimitive substitutions with more delicate coding;
- nonstationary S-adic directive sequences;
- fusion systems;
- grammars whose relevant asymptotic parameter is not a letter frequency;
- finite substitutions used only as local components of a nonstationary construction.
