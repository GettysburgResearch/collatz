# LIT-KTHM-0034 — Every periodic stack tail is a finite Tschakaloff vector

**Type:** self-contained native-to-literature reduction.  
**Sources for the target function:** Väänänen--Wallisser (1991), Matala-aho (2002), Väänänen--Zudilin (2008).  
**Maps to:** `PADIC/L-9408`, `PADIC/L-9410`, `PADIC/T-9414`, and the all-period target in PR #20.

## Statement

Let `T` be a rational number with `0<|T|_2<1`. Let a finite positive increment word

```text
W=d_1...d_r
```

have length `r`, height sum `S`, transfer exponent `e`, and prefix polynomial

```text
P_W(X)=sum_(j=0)^(r-1) c_j X^j.
```

Put

```text
lambda=T^(9S),
R=lambda^r,
Z=T^e X^r.
```

Define the Tschakaloff function

```text
f_R(z)=sum_(N>=0) R^(N(N-1)/2) z^N.
```

Then the infinite repeated-word tail has the exact decomposition

```text
Theta(m;W^infinity)
 =sum_(j=0)^(r-1) c_j X^j f_R(Z*lambda^j).            (1)
```

For distinct phase indices `0<=i<j<r`,

```text
(Z*lambda^i)/(Z*lambda^j)=lambda^(i-j) notin R^Z.     (2)
```

Thus one fixed period produces a finite vector of Tschakaloff values at rational points lying in distinct multiplicative `R`-orbits.

## Proof

The repeated-block formula of the finite transfer calculus is

```text
Theta(m;W^infinity)
 =sum_(N>=0)
   T^(N*e+9*r*S*N(N-1)/2)
   X^(N*r)
   P_W(T^(9*N*S)*X).                                  (3)
```

Expand the last polynomial:

```text
P_W(T^(9NS)X)
 =sum_(j=0)^(r-1)c_j lambda^(Nj)X^j.                  (4)
```

Substituting `(4)` into `(3)` and interchanging the finite `j`-sum with the convergent `N`-sum gives

```text
Theta
 =sum_j c_j X^j
   sum_N (lambda^r)^(N(N-1)/2)
         (T^e X^r lambda^j)^N,
```

which is `(1)`.

If `(2)` failed, then `lambda^(i-j)=R^k=lambda^(rk)` for some integer `k`. Since `0<|lambda|_2<1`, `lambda` has infinite multiplicative order, hence `i-j=rk`. But `0<j-i<r`, impossible. ∎

## Research consequences

1. The fixed-period problem is a simultaneous linear-independence problem for one q-functional equation, not `r` unrelated scalar special values.
2. The point ratios satisfy the natural q-orbit-separation condition used in several multi-point q-series theorems.
3. The complete hypotheses of Väänänen--Wallisser (1991) must be inspected before claiming that all periods are closed.
4. If the external theorem is insufficient, Matala-aho's determinant criterion and symbolic Hermite--Padé minors become the correct native target.

## Non-consequence

The decomposition alone proves neither irrationality nor transcendence. It does not cover a nonperiodic S-adic limit without a uniform linear-independence measure in the period word.