# Block q-Gaussian program for all fixed periods

## Exact starting point

For a positive period-`r` word, the combined moments are

```text
u_N=R^[N(N-1)/2]Z^N P_W(Xlambda^N),
R=lambda^r.
```

PR #34 proves nonzero Hankel minors and the exact quadratic `2`-adic Padé error. The only missing ingredient for irrationality is a reduced global-height bound.

## Fine moment lift

Choose `q_0,b` with

```text
q_0^r=lambda,
b^r=Zq_0^[-r(r-1)/2],
```

and put

```text
m_k=q_0^[k(k-1)/2]b^k.
```

Then

```text
nu_N=sum_(h=0)^(r-1)D_hm_(rN+h)
    =L(D_W(x)x^(rN)).
```

The fine base Hankel determinant is one explicit Vandermonde product. This is the formal q-Gaussian or Stieltjes–Wigert bulk.

## Why ordinary Christoffel theory is close but not enough

For ordinary moments, multiplying the measure or functional by a fixed polynomial replaces a growing Hankel determinant by:

```text
base Hankel determinant
 x fixed-size orthogonal-polynomial determinant.
```

The stack system is `r`-decimated. In the coarse variable `y=x^r`, the word polynomial has fractional exponents. The residue classes `h mod r` must therefore remain as separate components.

## Correct target object

Use the `r` functionals

```text
L_h(y^N)=L(x^(rN+h)).
```

Develop their mixed multiple-orthogonal or biorthogonal system. The desired identity is a block Christoffel formula for every Cramer minor appearing in the combined Padé system.

## Required arithmetic output

After factoring the universal bulk, prove

```text
log_2 H(A_n:B_n)
 <=(81Sr-eta_r)n^2+o(n^2)
```

for some `eta_r>0` and infinitely many `n`. The exact finite-place error then gives irrationality by the product formula.

## Literature to mine

- Christoffel–Uvarov determinant identities for polynomial and rational moment modifications;
- biorthogonal Stieltjes–Wigert systems with unequal monomial lattices;
- mixed multiple orthogonality from block moment-matrix Gauss–Borel factorization;
- multiple-orthogonal Christoffel and Geronimus transformations.

No located theorem currently supplies the exact block formula or arithmetic height estimate.
