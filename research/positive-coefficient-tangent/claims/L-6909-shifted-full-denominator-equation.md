# L-6909 — a late first-crossing failure is a shifted full-denominator solution

**Claim ID:** `L-6909`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** `L-6904`, `L-6908`  
**Scope:** first-crossing parity cylinders satisfying `D=2^j-3^q>E=A/2^j`

## Setup

Let `w` be a first-crossing word of length `j`, weight `q`, and affine numerator `A`:

\[
T_w(x)=\frac{3^q x+A}{2^j}.
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

Assume

\[
\boxed{D>E.}
\tag{1}
\]

As shown in `L-6908`, `(1)` holds for all sufficiently late first crossings under any effective Baker lower bound, because `E<j/2` while `D` is exponential up to a polynomial Diophantine loss.

## Shifted full-denominator theorem

A positive integer in the parity cylinder of `w` fails to descend at time `j` if and only if there is an integer

\[
\boxed{d\in\mathbf Z,\qquad 0\le d<E,}
\tag{2}
\]

such that

\[
\boxed{D\mid A-dp.}
\tag{3}
\]

For such a `d`, the unique non-descending positive integer is the canonical root

\[
\boxed{
 r=\frac{A-dM}{D}}
\tag{4}
\]

and its endpoint is

\[
\boxed{T_w(r)=r+d.}
\tag{5}
\]

The cases are:

```text
d=0:
  r is a positive cycle point and D|A;

d>=1:
  r is a canonical CST failure with a positive near-return r -> r+d.
```

Every noncanonical lift descends.

## Proof

### Failure implies the shifted equation

Let `r` be the canonical root and suppose it does not descend. Under `(1)`, `L-6908` shows it is the only possible non-descending lift. Put

\[
d=T_w(r)-r\ge0.
\]

The dual-residue theorem gives

\[
0\le d<E<D.
\]

The affine identity is

\[
M(r+d)=pr+A.
\]

Rearranging,

\[
Dr=A-dM.
\tag{6}
\]

Since `M congruent p mod D`, equation `(6)` gives

\[
A-dp\equiv0\pmod D,
\]

which is `(3)`, while `(4)--(5)` follow directly.

### The shifted equation gives a failure

Conversely, suppose `(2)--(3)` hold. Since `M congruent p mod D`, divisibility `(3)` implies

\[
D\mid A-dM.
\]

Define `r` by `(4)`. Condition `d<E=A/M` gives `r>0`. Condition `(1)` gives

\[
A-dM<M E<M D,
\]

so

\[
0<r<M.
\]

Thus `r` is the canonical positive solution of the parity-cylinder congruence.

Using `D=M-p`,

\[
M(r+d)-pr
=Dr+Md
=A,
\]

which proves `(5)`. Therefore `r` follows `w` exactly and does not descend. ∎

## Small-displacement bound

Every first-crossing word satisfies

\[
E<q/2<j/2.
\]

Hence every noncyclic late failure has

\[
\boxed{1\le d<j/2.}
\tag{7}
\]

So an orbit segment of potentially enormous height and length must return to within fewer than `j/2` ordinary units of its start.

## Dual-residue form

Because `p` is invertible modulo `D`, equation `(3)` is equivalent to

\[
\boxed{
 d=[A p^{-1}]_D.}
\tag{8}
\]

Under `(1)`, failure occurs exactly when this canonical residue is smaller than `E<j/2`. The complementary residue in `L-6908` is

\[
\zeta=D-d.
\]

Thus the late bad set is a bottom interval of width `E` for the displacement residue, equivalently a top interval of width `E` for the descent-defect residue.

## Unified cycle/CST compiler target

The cycle and finite-crossing funnels now share one exact finite equation:

\[
\boxed{
 A_w=n(2^j-3^q)+d3^q,
 \qquad
 0\le d<j/2.}
\tag{9}
\]

Here:

- `d=0` is the usual positive-cycle equation;
- `d>0` is a delayed first-crossing CST failure;
- `n=(A_w-d2^j)/(2^j-3^q)` is the canonical positive start.

A proof-producing compiler may therefore search or exclude the two lanes together by retaining the small displacement `d` as one additional ordinary parameter.

## Why this advances the blocker

Previous cycle machinery targeted

\[
D\mid A.
\]

Previous coefficient machinery targeted the inequality

\[
r^+(w)>A/D.
\]

`L-6909` proves that, at every sufficiently late crossing, failure of the inequality is **exactly** a full-denominator divisibility hit after subtracting one term `d3^q` with `d<j/2`.

This creates a direct handoff to:

- sparse resultants and pulse-cone eliminants;
- prime-power excess-path compilers;
- mixed-place height forcing;
- S-unit and logarithmic-form methods;
- exact physical replay.

The remaining theorem is to exclude `(9)` for every `d` in the declared short interval, not to control an infinite family of ordinary lifts.

## Gap audit

- The shifted equation is a reduction, not a universal exclusion.
- Existing cycle theorems for `d=0` do not automatically cover `d>0`.
- The displacement range grows linearly with `j`, though it is tiny relative to `D`.
- Source-dependent eventual use of `(1)` requires a reviewed effective logarithmic-form bound.
