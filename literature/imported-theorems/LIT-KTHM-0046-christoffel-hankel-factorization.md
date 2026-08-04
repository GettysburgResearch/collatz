# LIT-KTHM-0046 — Polynomial moment deformations factor through a fixed orthogonal-polynomial determinant

**Type:** imported theorem with an exact nonapplication and a native block-generalization target.  
**Source:** C. Krattenthaler, *Hankel determinants of linear combinations of moments of orthogonal polynomials, II*, Ramanujan Journal 61 (2023), 597–627, Theorem 1.  
**Maps to:** `SYN/T-9821`, `SYN/T-9824`, and `LIT-KTHM-0045`.

## External theorem

Let `L` be a linear functional over a characteristic-zero field with moments

```text
mu_n=L(x^n),
```

and let `p_n(x)` be its monic orthogonal polynomials. Assume the relevant base Hankel determinants are nonzero.

For variables `x_1,...,x_d`, put

```text
D(x)=product_(ell=1)^d(x_ell+x).
```

Then, for every `n>=0`,

```text
 det_(0<=i,j<n) L(x^(i+j)D(x))
 -------------------------------------------------
 det_(0<=i,j<n) L(x^(i+j))

 = (-1)^(nd)
   det_(1<=i,j<=d)(p_(n+i-1)(-x_j))
   / product_(1<=i<j<=d)(x_i-x_j).                  (1)
```

The source also treats confluent/singular specializations. Its statement and proofs are formal: positivity of a real measure is not required once the moment functional and nonzero Hankel determinants are available.

The proof is imported as a black box.

## Meaning of the theorem

A fixed degree-`d` polynomial deformation does not require a new determinant of size growing with `n` after the universal base Hankel determinant is removed. All deformation data are carried by one `d x d` determinant of orthogonal-polynomial values.

Consequently, a cubic bulk in the logarithm of the base Hankel determinant may cancel exactly in determinant ratios, leaving a fixed-rank boundary object.

## Exact applicability boundary for the periodic stack moments

`LIT-KTHM-0045` writes the periodic stack moments as

```text
u_N^W = L(D_W(x)x^(rN)),                              (2)
```

where `D_W` has degree `r-1` in the fine variable `x`.

For `r=1`, `(2)` is an ordinary scalar moment deformation and the standard theorem is in the correct object class.

For `r>1`, the coarse moment index is `N`, while the functional is sampled at powers `x^(rN)`. If one writes `y=x^r`, then

```text
D_W(x)=sum_(h=0)^(r-1)D_h y^(h/r),                   (3)
```

which is not a polynomial or rational function of `y` in general.

Therefore `(1)` cannot be applied directly to the current periodic-stack Hankel determinants. Doing so would silently discard the residue classes modulo `r`.

## Correct block target

Define residue-class functionals

```text
L_h(y^N)=L(x^(rN+h)),
0<=h<r.                                               (4)
```

Then

```text
nu_N^W=sum_h D_h L_h(y^N).                            (5)
```

The required extension is a block or multiple-orthogonal Christoffel formula for the `r`-component functional `(L_0,...,L_(r-1))`.

A successful theorem should factor every base and bordered Cramer minor in `SYN/T-9821` as

```text
universal quadratic-exponential bulk determinant
 x fixed-rank or block boundary determinant.          (6)
```

The boundary determinant must then be estimated at both the Archimedean and `2`-adic places.

## Relevant neighboring literature

The following sources confirm that the target object class is established mathematical territory, but none has yet been checked as a verbatim solution of `(4)`–`(6)`:

1. Dolivet and Tierz construct biorthogonal Stieltjes–Wigert polynomials for log-normal ensembles with unequal monomial lattices.
2. Mixed multiple orthogonal polynomials are built by Gauss–Borel factorization of block moment matrices and admit determinant and Christoffel–Darboux formulas.
3. Multiple-orthogonal Christoffel and Geronimus transformations treat separate polynomial or rational modifications of component weights.

These are methodological neighbors, not imported conclusions for the repository moments.

## Native proof program

The all-fixed-period route is now sharply stated:

1. use `LIT-KTHM-0045` to form the `r` residue-class moment matrix;
2. identify its fine quadratic-exponential orthogonal or biorthogonal polynomials explicitly;
3. prove the block analogue of `(1)` for every Cramer minor used by `SYN/T-9821`;
4. factor the common cubic bulk before specializing the rational parameters;
5. prove that the remaining block determinant has global reduced height at most
   ```text
   (81Sr-eta_r)n^2+o(n^2)
   ```
   for some `eta_r>0`;
6. combine that bound with the exact `2`-adic error order already proved in `SYN/T-9821`.

This would establish irrationality for each fixed positive period.

## Nonconsequences

The imported theorem does not by itself prove:

- the required block formula;
- cancellation of the primitive integer unit parts;
- a positive `eta_r`;
- estimates uniform in growing period `r`;
- irrationality of the balanced nonperiodic directive;
- or any Collatz conclusion.
