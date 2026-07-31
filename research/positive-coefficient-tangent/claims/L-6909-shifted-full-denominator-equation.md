# L-6909 — universal shifted full-denominator classification

**Claim ID:** `L-6909`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Corrected:** 2026-07-31  
**Issue:** #75  
**Dependencies:** elementary shortcut-Collatz affine composition and the finite parity-cylinder bijection  
**Scope:** every finite first-coefficient-crossing word; no bank, entropy, periodicity, aperiodicity, or lateness hypothesis

## Correction notice

An earlier draft wrote

\[
A_w=n(2^j-3^q)+d3^q
\]

while simultaneously calling `n` the **starting** value. That notation was inconsistent.

The coefficient `3^q` is correct when `n` denotes the **endpoint**. If `n` denotes the start, the coefficient of `d` is `2^j`.

The corrected dual identities are

\[
\boxed{
A_w=x(2^j-3^q)+d2^j
}
\tag{1}
\]

for the starting value `x`, and

\[
\boxed{
A_w=y(2^j-3^q)+d3^q
}
\tag{2}
\]

for the endpoint `y=x+d`.

The correction strengthens the theorem: the shifted classification below holds for **every** first-crossing word and every non-descending positive realization. The previous auxiliary hypothesis `2^j-3^q>A_w/2^j` is not needed.

## Setup

Let `w=(v_0,...,v_(j-1))` be a shortcut-Collatz parity word of length `j` and weight

\[
q=\sum_{i=0}^{j-1}v_i.
\]

Write

\[
T_w(x)=\frac{3^q x+A_w}{2^j}.
\]

Put

\[
M=2^j,
\qquad
p=3^q,
\qquad
D=M-p.
\]

Assume `w` is a first coefficient crossing:

\[
3^{q_k}\ge2^k
\quad(0\le k<j),
\qquad
p<M.
\tag{3}
\]

Let `x>0` be an ordinary integer following `w`, let

\[
y=T_w(x),
\]

and put

\[
d=y-x.
\tag{4}
\]

## Universal start/endpoint identity

For every such realization,

\[
\boxed{
A_w=xD+dM=yD+dp.
}
\tag{5}
\]

### Proof

The affine identity is

\[
My=px+A_w.
\]

Using `y=x+d` gives

\[
A_w=M(x+d)-px=x(M-p)+dM=xD+dM.
\]

Using `x=y-d` gives

\[
A_w=My-p(y-d)=y(M-p)+dp=yD+dp.
\]

This proves `(5)`. ∎

## Exact classification of every non-descending realization

A positive integer in the parity cylinder of `w` fails to descend at time `j` if and only if there is an integer

\[
\boxed{d\ge0}
\tag{6}
\]

such that

\[
\boxed{D\mid A_w-dp}
\tag{7}
\]

and

\[
\boxed{d<\frac{A_w}{M}.}
\tag{8}
\]

For such a `d`, the endpoint and start are respectively

\[
\boxed{
y=\frac{A_w-dp}{D},
\qquad
x=y-d=\frac{A_w-dM}{D}.
}
\tag{9}
\]

Conversely, every integer `d` satisfying `(6)--(8)` produces one positive ordinary realization following `w` and obeying

\[
T_w(x)=y=x+d.
\]

### Forward implication

If `y>=x`, then `d=y-x>=0`. Identity `(5)` gives `(7)` and `(9)`. Since `x>0`, the start form in `(5)` gives

\[
A_w=xD+dM>dM,
\]

which is `(8)`.

### Converse implication

Suppose `(6)--(8)` hold. Because `M congruent p (mod D)`, divisibility `(7)` also gives

\[
D\mid A_w-dM.
\]

Define `x,y` by `(9)`. Condition `(8)` gives `x>0`, and `y=x+d>=x`.

Moreover,

\[
px+A_w
=p(y-d)+yD+dp
=y(p+D)
=yM.
\]

Thus the affine endpoint is the integer `y`.

For a fixed parity word `w`, the integers following `w` form the unique residue class modulo `M` satisfying

\[
px+A_w\equiv0\pmod M.
\]

The displayed equality places `x` in that class, so its actual first `j` parity bits are exactly `w`. ∎

## Exact displacement residue

Since `gcd(p,D)=1`, every possible displacement lies in one residue class:

\[
\boxed{
d\equiv A_w p^{-1}\pmod D.}
\tag{10}
\]

Hence all non-descending starts are classified by the finite set

\[
\boxed{
\mathcal D_w
=
\left\{
 d\in\mathbf Z_{≥0}:
 d<\frac{A_w}{M},
 \ d\equiv A_wp^{-1}\pmod D
\right\}.}
\tag{11}
\]

Their number satisfies

\[
\boxed{
|\mathcal D_w|
\le
\left\lceil\frac{A_w/M}{D}\right\rceil.}
\tag{12}
\]

In particular, if `D>=A_w/M`, there is at most one non-descending realization, necessarily the canonical positive cylinder representative.

## First-crossing harmonic identity

Let

\[
\alpha=\frac{\log2}{\log3},
\qquad
S_i=\sum_{h=0}^{i-1}v_h,
\qquad
B_i=S_i-\alpha i.
\]

The affine numerator is

\[
A_w
=
\sum_{i=0}^{j-1}
 v_i\,2^i3^{q-S_{i+1}}.
\tag{13}
\]

Dividing by `p=3^q` and using `S_(i+1)=S_i+1` at every odd position gives

\[
\boxed{
\frac{A_w}{p}
=
\frac13
\sum_{i:v_i=1}3^{-B_i}.}
\tag{14}
\]

Since first crossing gives `B_i>=0` for every `i<j`,

\[
\frac{A_w}{p}\le\frac q3.
\]

Because `p/M<1`,

\[
\boxed{
\frac{A_w}{M}
=
\frac{p}{M}\,rac13
\sum_{i:v_i=1}3^{-B_i}
<
\frac q3
<
\frac j3.}
\tag{15}
\]

Therefore every non-descending first-crossing realization, with no further hypothesis, satisfies

\[
\boxed{
0\le d<\frac{A_w}{2^j}<\frac q3<\frac j3.}
\tag{16}
\]

This improves the former `j/2` displacement bound.

The bound is sensitive to the entire bank profile, not merely its maximum:

\[
\boxed{
 d
<
\frac{3^q}{2^j}\,rac13
\sum_{i:v_i=1}3^{-B_i}.}
\tag{17}
\]

Thus a high-bank path can support a positive displacement only through sufficiently many odd times returning to low surplus.

## Cycle and near-return cases

The exact alternatives are now:

```text
d=0:
  x=y and D|A_w;
  the word closes to a positive cycle point.

d>=1:
  x -> x+d is a positive first-crossing near-return;
  d is the short full-denominator residue in (10).
```

Using the endpoint notation `n=y`, the user-facing equation is exactly

\[
\boxed{
A_w
=
n(2^j-3^q)+d3^q,
\qquad
0\le d<\frac j3,
}
\tag{18}
\]

and the starting value is

\[
\boxed{x=n-d.}
\tag{19}
\]

Using `n` for the starting value instead gives the equally exact form

\[
\boxed{
A_w
=
n(2^j-3^q)+d2^j,
\qquad
T_w(n)=n+d.}
\tag{20}
\]

## Applicability to the surviving regime

Nothing in the proof assumes:

- bounded or logarithmic coefficient bank;
- low factor complexity;
- zero entropy;
- periodicity or eventual periodicity;
- a pulse decomposition;
- closeness to the mechanical extremizer;
- a prescribed infinite directive.

Therefore `(18)` applies verbatim to arbitrary high-bank, internally high-factor-complexity, genuinely nonperiodic first-crossing words whenever they possess a positive non-descending realization.

The equation is an exact reduction, not yet a universal exclusion of those realizations.

## Gap audit

- The earlier start/endpoint notation error is corrected explicitly rather than hidden.
- Equation `(18)` uses `n` for the endpoint; equation `(20)` uses `n` for the start.
- Aperiodicity and high internal factor complexity do not by themselves exclude the short residue `(10)`.
- Existing cycle theorems treat `d=0`; arbitrary growing-support exclusion for `d>0` remains open.
- The source-free advance is the universal equivalence and the sharper displacement interval `(16)`.