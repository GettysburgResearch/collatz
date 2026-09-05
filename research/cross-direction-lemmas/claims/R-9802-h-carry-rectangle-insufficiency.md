# R-9802 — Coarse H carry rectangles do not control displacement

Claim ID: `R-9802`  
Title: Canonical endpoint ranges and interface carries do not imply the H first-crossing sign  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-h`, integrated by `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: none  
Scope: refutation of a coarse-data proof strategy for `PR19/C-9501`  
Related counterexample candidates: none

## Statement

The following proof strategy is invalid:

> Use only the canonical endpoint ranges, the correct signed-displacement
> inequalities for both pieces, and the canonical interface-carry rectangle
> to deduce the correct sign after a mixed-sign concatenation.

There are integral affine data satisfying every one of those coarse
conditions for which the concatenated displacement has the wrong sign.

## Definitions

An abstract normalized affine datum consists of positive integers `U,V`, an
integer offset `B>0`, and endpoints `A,Y` satisfying

\[
0\le A<U,
\qquad 0\le Y<V,
\qquad UY-VA=B.
\]

Its multiplier gap and signed displacement are

\[
D=U-V,
\qquad \Delta=A-Y.
\]

For a following one-letter datum `(P,Q,A_r,Y_r)`, canonical interface carries
`h,j` satisfy

\[
Y+hV=A_r+jP,
\qquad 0\le h<P,
\qquad 0\le j<V.
\]

## Proof

Take an abstract expanding prefix with

\[
U=2^{19}=524288,
\qquad
V=3^{12}=531441,
\]

\[
A=1,
\qquad
Y=13.
\]

Its affine offset is the positive integer

\[
B=UY-VA=6{,}284{,}303.
\tag{1}
\]

The canonical endpoint and signed-displacement conditions hold:

\[
0\le A<U,\qquad0\le Y<V,
\]

\[
D=U-V=-7153,
\qquad
D<\Delta=A-Y=-12<0.
\tag{2}
\]

Append the genuine contracting one-letter data for `r=0`:

\[
P=4,\qquad Q=3,\qquad A_r=Y_r=1,
\qquad d=1,\qquad\delta=0.
\]

The interface equation holds with canonical carries

\[
Y+hV=A_r+jP,
\qquad h=0,\quad j=3,
\tag{3}
\]

because `13=1+3*4`. In particular, `0<=h<P` and `0<=j<V`.

Nevertheless, the concatenated data are contracting while their displacement
is negative:

\[
D_{ur}=P(-7153)+V(1)=502{,}829>0,
\tag{4}
\]

\[
\Delta_{ur}=-12+0+3=-9<0.
\tag{5}
\]

Equivalently, the sharp inequality of `L-9807` fails:

\[
c+he=12>3=\delta+jd.
\]

This proves that the coarse-data implication is false. ∎

### Actual-word exclusion

The prefix data above do not come from an actual H word. Indeed, the scales
`U=2^19` and `V=3^12` force a length-two word whose two letters sum to `5`.
For the six possible orders, the constrained word sum

\[
B_w=\frac14\sum_k2^{E_k}3^{S_w-S_k}.
\]

takes respectively the values

```text
308219, 288536, 271040, 255488, 241664, 229376,
```

none of which equals `6,284,303`.

Therefore (4)--(5) are not a counterexample to `PR19/C-9501`. They refute only
proofs that forget the word-specific offset or equivalent ghost-digit
structure.

## Adversarial tests

- Both components satisfy their correct signed-displacement inequalities:
  `-7153<-12<0` for the expanding prefix and `0<=0<1` for the `r=0` letter.
- The endpoint and carry ranges all hold, including `h=0<P` and `j=3<V`.
- The aggregate H scales and endpoint congruence alone do not rescue the
  inference: `U=2^19`, `V=3^12`, and `Y=13=1 mod 3` have the expected coarse
  form.
- The explicit six-offset enumeration is the word-specific check excluding
  this datum from the actual H system.

## Remaining uncertainty

Whether every actual H offset forces `L-9807/(6)` remains open. This
countermodel narrows the admissible proof strategy but does not lower the
empirical status of `PR19/C-9501`.

## Motivation

Negative information is useful here: it prevents further effort on a broad
carry-rectangle lemma that is algebraically false and focuses the H program on
the one source of rigidity not present in arbitrary affine tuples.

## Dependency audit

Every displayed equality is direct integer arithmetic. No H conjecture or
source-branch theorem is assumed.

## Gap audit

- The example is an abstract affine tuple, not an H word.
- It says nothing about whether actual offsets satisfy `L-9807/(6)`.
- It does not lower the empirical status of `PR19/C-9501`; it narrows the
  admissible proof strategy.

## Suggested next attack

Classify the residues or interval restrictions on `B_w` that follow from its
ordered word sum, then test which one excludes (1). A useful lemma must fail on
this countermodel for an explicitly word-specific reason.
