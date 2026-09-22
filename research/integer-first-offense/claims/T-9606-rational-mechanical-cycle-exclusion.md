# T-9606 — Rational mechanical valuation words cannot be nontrivial positive cycles

**Claim ID:** `T-9606`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** `L-9606`; elementary cyclic-rotation and power identities  
**Scope:** lower and upper rational mechanical accelerated valuation words over `{1,2}`

## 1. Statement

For integers

\[
0\le p\le q,
\qquad q\ge1,
\]

let

\[
w^-_{p,q}
=\left(
1+\left\lfloor{(j+1)p\over q}\right\rfloor
 -\left\lfloor{jp\over q}\right\rfloor
\right)_{0\le j<q}
\tag{1}
\]

be the lower rational mechanical valuation word, and let `w^+_(p,q)` be the corresponding upper mechanical word obtained by replacing both floors with ceilings.

Then neither `w^-_(p,q)` nor `w^+_(p,q)` is the accelerated itinerary of a nontrivial positive Collatz cycle.

The only positive exact cycle in this complete rational-mechanical class is the trivial fixed point

\[
\boxed{w=(2),\qquad n_0=1.}
\tag{2}
\]

## 2. Primitive standard factorization

Assume first that

\[
0<p<q,
\qquad \gcd(p,q)=1.
\tag{3}
\]

Let `b` be the inverse of `p` modulo `q`, chosen in `1,...,q-1`, and put

\[
a={pb-1\over q},
\qquad
c=p-a,
\qquad
d=q-b.
\tag{4}
\]

Then

\[
{a\over b}<{c\over d},
\qquad
cb-ad=1,
\qquad
{p\over q}={a+c\over b+d}.
\tag{5}
\]

The elementary standard factorization of the lower Christoffel word is

\[
\boxed{
w^-_{p,q}=w^-_{a,b}\,w^-_{c,d}.}
\tag{6}
\]

For completeness, `(6)` follows directly from the lattice path under the line from `(0,0)` to `(q,p)`: the unique visible lattice point selected by `(4)` divides the path into the two Farey-parent paths. Equivalently, substituting `(4)` into the floor increments in `(1)` gives the first `b` increments of slope `a/b` followed by the `d` increments of slope `c/d`.

Put

\[
u=w^-_{a,b},
\qquad
v=w^-_{c,d},
\qquad
w=uv.
\]

Let

\[
C_w=\sum_{j=0}^{q-1}3^{q-1-j}2^{A_j},
\qquad
D_w=2^{p+q}-3^q.
\tag{7}
\]

## 3. Full-denominator coprimality

The word `vu` is a cyclic rotation of `uv`. The exact rotation identity gives

\[
2^{A_u}C_{vu}-3^{k_u}C_{uv}=D_w C_u.
\tag{8}
\]

Because `D_w` is coprime to both two and three, `(8)` implies

\[
\gcd(C_{uv},|D_w|)=\gcd(C_{vu},|D_w|).
\tag{9}
\]

By `L-9606`, the Farey-parent determinant in `(5)` gives

\[
\boxed{
C_{uv}-C_{vu}
=-2^{c+d-1}3^{b-1}.}
\tag{10}
\]

Any common divisor in `(9)` therefore divides one signed `{2,3}`-unit. On the other hand,

\[
D_w=2^{p+q}-3^q
\]

is odd and is not divisible by three. Hence

\[
\boxed{
\gcd(C_w,|D_w|)=1.}
\tag{11}
\]

This is a statement about the **entire** cycle denominator, not a selected factor.

## 4. Exclusion of the primitive word

A positive exact accelerated cycle requires

\[
D_w>0,
\qquad
D_w\mid C_w.
\tag{12}
\]

Together with `(11)`, this forces

\[
D_w=1.
\tag{13}
\]

But

\[
2^{p+q}-3^q=1
\tag{14}
\]

has no solution with `0<p<q`. Indeed, if `p+q>=3`, then the left power of two is zero modulo eight, while `3^q+1` is congruent to either `4` or `2` modulo eight. Thus `p+q` would have to equal two, impossible under `0<p<q`.

Therefore no primitive nonconstant lower mechanical word is a positive cycle.

## 5. Endpoints, powers, and upper words

### All-one endpoint

If `p=0`, the valuation word is all `1`, and

\[
D=2^q-3^q<0.
\]

It cannot be a positive cycle.

### All-two endpoint

If `p=q`, the word is all `2`. Its primitive root is `(2)`, which replays the trivial fixed point `1`. No nontrivial cycle occurs.

### Nonprimitive rational slopes

If

\[
g=\gcd(p,q)>1,
\]

then the lower mechanical word is exactly the `g`th power of the primitive word for

\[
{p/g\over q/g}.
\]

The numerator and denominator of a powered word acquire the same positive geometric factor. Hence the powered word is a positive cycle certificate exactly when its primitive root is, and it has the same reduced fixed point. The primitive cases above complete the lower-word proof.

### Upper mechanical words

For a rational slope, the upper and lower mechanical words are cyclic rotations of one another, including the powered case. Cycle divisibility is rotation invariant, so the upper words are excluded as well.

This proves the theorem. ∎

## 6. Consequence for the critical mechanical compiler

The unmodified balanced base word in the smooth-denominator cycle program cannot itself be a cycle, regardless of its length, continued-fraction quality, local-minimum count, or denominator factorization. Every viable mechanical construction must introduce a genuine fixed-boundary repair.

`L-9606/(14)` gives the exact repair atom:

\[
\Delta C=\pm2^x3^y
\]

for every contextual swap of Farey-neighbor standard factors. Thus the constructive problem is sharpened to

```text
primitive mechanical SLP
  + a finite hierarchical signed-S-unit repair circuit
  -> complete identity C=nD.
```

The theorem eliminates the unrepaired family but does not exclude such repaired circuits.

## Gap audit

- The theorem covers rational lower/upper mechanical words, not arbitrary balanced aperiodic words or arbitrary local repairs.
- A repaired word need not retain mechanical factor complexity.
- The pure-unit atoms do not automatically span the full denominator.
- No positive cycle, divergent seed, or unconditional Collatz counterexample is claimed.

## Verification

`X-9610` checks the standard factorization, full-denominator gcd, upper/lower rotation, power decomposition, and absence of nontrivial cycle hits for every rational slope of denominator at most `100`.