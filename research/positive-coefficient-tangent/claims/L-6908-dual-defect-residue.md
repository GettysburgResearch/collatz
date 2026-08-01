# L-6908 — late first crossings have one canonical candidate and one tiny dual bad interval

**Claim ID:** `L-6908`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** `L-6904`; elementary modular arithmetic  
**Scope:** first-coefficient-crossing parity cylinders satisfying `2^j-3^q>A_w/2^j`

## Setup

Let `w` be a first-crossing word of length `j`, weight `q`, affine numerator `A`, canonical positive root `r`, and canonical endpoint

\[
y=T_w(r).
\]

Put

\[
M=2^j,
\qquad
p=3^q,
\qquad
D=M-p>0,
\qquad
E=\frac{A}{M}.
\]

Let the integer descent defect be

\[
\boxed{c=r-y.}
\tag{1}
\]

`L-6904` gives

\[
\boxed{Dr-A=Mc.}
\tag{2}
\]

Define the dual canonical residue

\[
\boxed{
\zeta=[-A M^{-1}]_D=[-A p^{-1}]_D
\in\{0,1,\ldots,D-1\}.}
\tag{3}
\]

The two expressions agree because `M congruent p mod D`.

## Universal defect bounds

One always has

\[
\boxed{-E<c<D.}
\tag{4}
\]

Indeed, `r>0` in `(2)` gives `c>-A/M=-E`, while `r<M` gives

\[
c=\frac{Dr-A}{M}<D.
\]

Moreover

\[
\boxed{c\equiv\zeta\pmod D.}
\tag{5}
\]

## Dual-residue trichotomy when `D>E`

Assume

\[
\boxed{D>E.}
\tag{6}
\]

Then `(4)--(5)` leave exactly the following possibilities.

### Descent

\[
\boxed{c>0}
\]

if and only if

\[
\boxed{1\le\zeta\le D-E.}
\tag{7}
\]

The inequality in `(7)` is interpreted over the integers; equivalently `zeta` does not lie in the open top interval below.

### Positive cycle

\[
\boxed{c=0}
\]

if and only if

\[
\boxed{\zeta=0.}
\tag{8}
\]

Then `r=y`, so full-denominator divisibility and exact replay give a positive cycle with period dividing `w`.

### Canonical CST failure

\[
\boxed{c<0}
\]

if and only if

\[
\boxed{D-E<\zeta<D.}
\tag{9}
\]

In this case

\[
\boxed{c=\zeta-D,}
\tag{10}
\]

and therefore

\[
\boxed{0<y-r=D-\zeta<E.}
\tag{11}
\]

### Proof

Condition `(6)` makes the interval `(-E,D)` shorter than `2D`. For one residue class modulo `D`, at most two representatives can lie there: `zeta` and `zeta-D`.

If `zeta=0`, the negative candidate `-D` lies below `-E`, so `c=0` and `(8)` follows.

If `zeta>0`, then:

- `zeta` is the positive representative;
- `zeta-D` lies in `(-E,0)` exactly when `zeta>D-E`.

This proves `(7)--(10)`, and `(11)` follows from `-c=D-zeta`. ∎

## Every lift except the canonical one descends

Every positive integer in the cylinder has the form

\[
x=r+Mt,
\qquad t\ge0,
\]

and `L-6904` gives

\[
x-T_w(x)=c+Dt.
\tag{12}
\]

Under `(6)`, even in the failure case `(11)` one has

\[
-D<c<0.
\]

Therefore

\[
\boxed{
 t\ge1
 \quad\Longrightarrow\quad
 x-T_w(x)>0.}
\tag{13}
\]

Thus each cylinder has at most one non-descending positive integer: its canonical root `r`.

This eliminates every noncanonical lift from the late finite-crossing blocker.

## First crossings automatically have small remainder

For every first-crossing word,

\[
\boxed{E<q/2<j/2.}
\tag{14}
\]

This is the termwise estimate proved in `T-6905`: every odd contribution to the normalized final remainder is below `1/2`.

Consequently, the hypothesis `(6)` is implied by the purely scalar condition

\[
\boxed{D>j/2.}
\tag{15}
\]

Under `(15)`, the bad interval `(9)` contains fewer than `j/2` integers inside the modulus `D`.

## Source-dependent eventual form

Suppose an effective logarithmic-form theorem gives

\[
\lambda=j\log2-q\log3\ge c_0j^{-\mu}.
\]

Since

\[
D=2^j(1-e^{-\lambda})
\]

and first crossing gives `0<lambda<log2`,

\[
D\ge\frac{c_0}{2}\,2^j j^{-\mu}.
\]

The right side exceeds `j/2` for all sufficiently large `j`. Hence every sufficiently late first-crossing cylinder satisfies `(6)` and has the exact classification:

```text
zeta=0:
  positive cycle;

D-E < zeta < D:
  the canonical root alone is a CST failure;

all other zeta:
  every positive integer in the cylinder descends.
```

## Strategic meaning

The finite-crossing lane is no longer an uncontrolled union of ordinary lifts. At late lengths it reduces to one dual residue per parity word:

\[
\boxed{\zeta_w=[-A_w3^{-q}]_{2^j-3^q}.}
\]

A noncyclic failure requires this residue to land in the top interval

\[
(D-E_w,D),
\]

whose width is exactly the canonical rise `y-r` and is always less than `j/2`, while the modulus is exponentially large up to a polynomial Diophantine loss.

The remaining theorem is therefore a deterministic residue-avoidance statement, not an ordinary-lift search.

## Gap audit

- The lemma does not prove that `zeta` avoids the top interval.
- The source-dependent eventual assertion requires a reviewed effective logarithmic-form theorem.
- Positive cycles correspond to `zeta=0` and remain a separate full-denominator lane.
- A tiny bad interval is not empty merely because it has small relative density.
