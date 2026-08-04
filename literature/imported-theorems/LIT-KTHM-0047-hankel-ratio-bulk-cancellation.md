# LIT-KTHM-0047 — Orthogonal-polynomial ratios cancel the universal Hankel bulk

**Type:** standard moment-theory identities with complete proofs and a native height interpretation.  
**Maps to:** `SYN/T-9821`, `SYN/T-9824`, `LIT-KTHM-0045`, and `LIT-KTHM-0046`.

## Setup

Let `L` be a linear functional with moments

```text
mu_k=L(x^k),
```

and put

```text
Delta_n=det(mu_(i+j))_(0<=i,j<n),
Delta_0=1.                                             (1)
```

Assume `Delta_n!=0` for all required `n`.

## Theorem 1 — determinant formula for the monic orthogonal polynomial

The unique monic polynomial `p_n(x)` of degree `n` orthogonal to

```text
1,x,...,x^(n-1)
```

is

```text
p_n(x)
 = 1/Delta_n
   det [
     mu_0       mu_1       ... mu_n
     mu_1       mu_2       ... mu_(n+1)
     ...
     mu_(n-1)   mu_n       ... mu_(2n-1)
     1          x          ... x^n
   ].                                                  (2)
```

### Proof

Expansion along the last row shows that `(2)` is monic: the coefficient of `x^n` is `Delta_n/Delta_n=1`.

For `0<=k<n`, apply `L(x^k * )` to `(2)`. The last row becomes

```text
mu_k,mu_(k+1),...,mu_(k+n),
```

which duplicates the `(k+1)`st moment row. The determinant is zero. Hence `p_n` has the required orthogonality. Uniqueness follows because the difference of two such monic polynomials has degree below `n` and is orthogonal to itself. QED.

## Theorem 2 — norm and recurrence-coefficient ratios

Put

```text
h_n=L(p_n^2).
```

Then

```text
boxed:
h_n=Delta_(n+1)/Delta_n.                              (3)
```

If the monic orthogonal polynomials obey

```text
p_(n+1)(x)=(x-alpha_n)p_n(x)-beta_n p_(n-1)(x),       (4)
```

then

```text
boxed:
beta_n
 =h_n/h_(n-1)
 =Delta_(n+1)Delta_(n-1)/Delta_n^2.                   (5)
```

### Proof

The Gram determinant of `1,x,...,x^n` is `Delta_(n+1)`. Replacing this basis by the monic triangular basis

```text
p_0,p_1,...,p_n
```

does not change the determinant. Orthogonality makes the new Gram matrix diagonal with entries `h_0,...,h_n`. Therefore

```text
Delta_(n+1)=product_(j=0)^n h_j,
Delta_n=product_(j=0)^(n-1)h_j,
```

which proves `(3)`.

Taking the inner product of `(4)` with `p_(n-1)` gives

```text
L(xp_np_(n-1))=beta_n h_(n-1).
```

Taking the recurrence for `p_n`, multiplying by `p_n`, and using symmetry of `L(fg)` shows that the left side is `h_n`. Thus `beta_n=h_n/h_(n-1)`, and `(5)` follows from `(3)`. QED.

## Bulk-cancellation interpretation

Suppose

```text
log H(Delta_n)=c_3 n^3+c_2 n^2+O(n).                  (6)
```

The second-difference expression in `(5)` cancels the cubic bulk formally:

```text
log H(Delta_(n+1)Delta_(n-1)/Delta_n^2)=O(n)         (7)
```

at the level of an ideal multiplicative height model.

For exact rational determinants, one must still control:

- cancellation of common integer content;
- other-prime unit parts;
- and the difference between a real-valued size estimate and reduced rational height.

Nevertheless, `(2)`–`(5)` show why raw cubic determinant heights are not the correct final objects. Orthogonal-polynomial coefficients, norms, recurrence coefficients, and Cramer ratios are the quantities in which the universal bulk can cancel.

## Application to the period-ten combined moments

`SYN/T-9821` proves that all combined-moment Hankel and bordered minors are nonzero and gives exact quadratic differences of their `2`- and `3`-adic endpoint orders. `SYN/T-9824` proves that removing only the visible ordinary Vandermonde leaves a cubic Schur quotient.

The correct continuation is therefore not another bound on one raw determinant. It is to identify the orthogonal or biorthogonal polynomials of the decimated functional in `LIT-KTHM-0045` and estimate directly:

```text
- the coefficients of p_n;
- the norms h_n;
- the recurrence coefficients beta_n;
- the evaluated Padé numerator/denominator pair.
```

A block Christoffel factorization of the kind targeted in `LIT-KTHM-0046` would make the common bulk explicit before rational specialization.

## Scope boundary

These identities do not prove that the required reduced heights are quadratic. They explain the exact algebraic location where a cubic bulk may cancel and provide a better set of target quantities for the all-period proof.
