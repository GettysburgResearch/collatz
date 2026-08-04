# LIT-KTHM-0045 — Periodic stack moments are a finite decimation of one quadratic-exponential moment functional

**Type:** exact native algebraic reduction with a complete proof.  
**Maps to:** `SYN/T-9821`, `SYN/T-9824`, `PADIC/L-9408`, `PADIC/L-9415`, and the all-fixed-period Padé frontier.

## Setup

Fix a positive periodic increment word `W` of length `r>=1`. Retain the notation

```text
T = 64/81,
lambda = T^(9S),
R = lambda^r,
Z = T^zeta,
P_W(X) = sum_(h=0)^(r-1) p_h X^h,
C_h = p_h X^h.
```

The combined moments used in `SYN/T-9821` are

```text
u_N^W
 = R^[N(N-1)/2] Z^N P_W(X lambda^N)
 = sum_(h=0)^(r-1)
   C_h R^[N(N-1)/2](Z lambda^h)^N.                 (1)
```

Work in an algebraic extension containing elements `q_0` and `b` satisfying

```text
q_0^r = lambda,
b^r = Z q_0^[-r(r-1)/2].                            (2)
```

Define one quadratic-exponential moment sequence

```text
m_k = q_0^[k(k-1)/2] b^k,                            (3)
```

and fixed coefficients

```text
D_h = C_h q_0^[-h(h-1)/2] b^(-h).                   (4)
```

## Theorem 1 — exact decimation identity

For every `N>=0`,

```text
boxed:
nu_N^W = sum_(h=0)^(r-1) D_h m_(rN+h).              (5)
```

### Proof

For `k=rN+h`, expand

```text
k(k-1)/2
 = r^2 N(N-1)/2
   + rhN
   + r(r-1)N/2
   + h(h-1)/2.                                      (6)
```

Using `(2)`,

```text
m_(rN+h)
 = q_0^[r^2N(N-1)/2+rhN]
   Z^N
   q_0^[h(h-1)/2] b^h.                              (7)
```

Since `q_0^r=lambda` and `R=lambda^r=q_0^(r^2)`, the first two factors in `(7)` are

```text
R^[N(N-1)/2] (lambda^h)^N Z^N.
```

Multiplication by `(4)` gives the `h`th summand of `(1)`. Summing proves `(5)`. QED.

## Theorem 2 — moment-functional form

Let `L` be the formal linear functional defined by

```text
L(x^k)=m_k,
```

and put

```text
D_W(x)=sum_(h=0)^(r-1)D_h x^h.                      (8)
```

Then

```text
boxed:
nu_N^W = L(D_W(x) x^(rN)).                           (9)
```

Thus the scalar periodic-stack moment sequence is obtained from one quadratic-exponential moment functional by:

1. a fixed degree-`r-1` polynomial modification in the fine variable `x`;
2. restriction to the sublattice of exponents divisible by `r`.

Equation `(9)` is exact; it is not an asymptotic analogy.

## Theorem 3 — the underlying fine moment functional is explicit

For every `n>=1`,

```text
Delta_n^(0)
 = det(m_(i+j))_(0<=i,j<n)
```

satisfies

```text
boxed:
Delta_n^(0)
 = b^[n(n-1)]
   q_0^[n(n-1)(n-2)/3]
   product_(0<=i<j<n)(q_0^j-q_0^i).                 (10)
```

In particular, it is nonzero whenever `q_0` is nonzero and not a root of unity.

### Proof

One has

```text
m_(i+j)
 = [q_0^[i(i-1)/2]b^i]
   [q_0^[j(j-1)/2]b^j]
   q_0^(ij).                                         (11)
```

Factor the first bracket from row `i` and the second from column `j`. Their total contribution is

```text
b^[n(n-1)]q_0^[n(n-1)(n-2)/3].                      (12)
```

The remaining determinant is

```text
det((q_0^i)^j)_(0<=i,j<n)
 = product_(i<j)(q_0^j-q_0^i),                      (13)
```

which proves `(10)`. QED.

## Interpretation

The fine moment sequence `(3)` is a formal Stieltjes–Wigert or log-normal-type quadratic-exponential moment sequence. The word-dependent object is not an arbitrary ten-phase vector: it is a fixed finite deformation of one such functional followed by an `r`-fold decimation.

This identifies a new all-period target:

```text
construct the orthogonal/biorthogonal theory of
N -> L(D_W(x)x^(rN))
with global coefficient heights tracked at R and Q_2.
```

The relevant external neighbors are:

- Christoffel–Uvarov determinant identities for polynomial/rational modifications of moments;
- biorthogonal Stieltjes–Wigert systems with unequal monomial lattices;
- multiple orthogonal polynomials and block moment-matrix Gauss–Borel factorization.

## Critical nonapplication

Ordinary scalar Christoffel theory does **not** apply directly to `(9)` in the coarse variable `y=x^r`, because

```text
D_W(x)=sum_h D_h y^(h/r)
```

contains fractional powers of `y` when `r>1`. The missing theorem is a block or multiple-orthogonal extension which retains the residue classes `h mod r`.

## Strategic consequence

`SYN/T-9821` already proves:

- every combined Hankel minor is nonzero;
- the exact `2`-adic error has quadratic gain;
- the unresolved issue is the primitive global height of Cramer ratios.

The reduction `(5)`–`(10)` suggests that the cubic bulk belongs to the universal fine quadratic-exponential moment determinant, while the word-specific information should live in a fixed `r`-component boundary determinant. Proving such a factorization, with an `O_r(n^2)` height bound for the residual component, is a plausible route to irrationality for every fixed period.

No such block factorization is asserted here.
