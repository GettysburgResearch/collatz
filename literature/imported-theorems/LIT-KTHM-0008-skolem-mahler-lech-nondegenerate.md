# LIT-KTHM-0008 — nondegenerate power sums have finitely many zeros

**Source:** [@Bell2019]
**Inspection:** full text
**Proof status:** Skolem–Mahler–Lech BLACK BOX; nondegenerate corollary proved completely

## Black-box theorem

Let `(u_n)` be a linear recurrence sequence over a characteristic-zero field. Its zero set is a finite set together with finitely many infinite arithmetic progressions.

## Corollary

Let

```text
u_n = c_1 alpha_1^n + ... + c_r alpha_r^n
```

in a characteristic-zero field, where every `c_i` is nonzero and no quotient `alpha_i/alpha_j` for `i≠j` is a root of unity. Then `u_n=0` for only finitely many `n≥0`.

## Proof

The power sum is a linear recurrence sequence, so Skolem–Mahler–Lech makes its zero set a finite set plus finitely many arithmetic progressions. Suppose an infinite progression `n=n_0+qt` were contained in the zero set. Then for every `t≥0`,

```text
0 = sum_i c_i alpha_i^n_0 (alpha_i^q)^t.
```

The numbers `alpha_i^q` are pairwise distinct because no quotient `alpha_i/alpha_j` is a root of unity. Evaluating at `t=0,...,r-1` gives a Vandermonde linear system with nonzero determinant, so every coefficient `c_i alpha_i^n_0` is zero, contradicting the hypotheses. Thus no infinite arithmetic progression occurs, and the zero set is finite. ∎

## Native application

For bases

```text
alpha_1=81^18,  alpha_2=81^9,  alpha_3=1,
```

every pairwise quotient is a nontrivial positive power of `81` or its reciprocal, hence not a root of unity. Therefore an exact three-term coincidence sequence with all nonzero coefficients has finitely many zeros.

## Audit requirements for `CLAUDE/T-0006`

The branch must still:

- display the exact coefficients;
- handle vanished coefficients and rule out the identically zero case;
- prove the target is equality in a characteristic-zero field, not merely a family of deeper congruences;
- distinguish exact zeros from high 2-adic valuation;
- state that the theorem is ineffective here and supplies no computable last zero.
