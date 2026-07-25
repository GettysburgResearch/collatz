# T-7302 — Fixed finite-order affine sliding filters are trivial

**Claim ID:** `T-7302`  
**Title:** A fixed integer-affine sliding filter carrying the complete six-branch language is only a time shift  
**Status:** `PROPOSED / EXACT ALGEBRAIC THEOREM`  
**Authoring agent:** `gpt56-cycle-01`  
**Created:** 2026-07-26  
**Dependencies:** PR #64 `D-7401` for the digit alphabet  
**Scope:** fixed finite-order integer-affine filters required to work on every finite type block  
**Related counterexample candidates:** none

## 1. Statement

Let `d>=0`, let

\[
b_0,\ldots,b_d,s\in\mathbf Z,
\]

and, for every legal six-branch trajectory, define

\[
\boxed{Y_n=s+\sum_{r=0}^{d}b_r x_{n+r}.}
\tag{1}
\]

Assume that for **every** type block

\[
(i_0,\ldots,i_d)\in\{0,\ldots,5\}^{d+1},
\]

the induced digit belongs to the original six-digit alphabet.  Then there is
one index `r_0` such that

\[
\boxed{b_{r_0}=1,
\qquad b_r=0\ (r\ne r_0),
\qquad s=0.}
\tag{2}
\]

Hence

\[
\boxed{Y_n=x_{n+r_0}.}
\]

No fixed finite-order affine sliding filter gives a contracting or
seed-preserving full-language self-section.

## 2. Induced digit

Using

\[
Qx_{n+r+1}=Px_{n+r}+a_{i_r},
\]

one obtains

\[
\boxed{
QY_{n+1}=PY_n+(Q-P)s+\sum_{r=0}^{d}b_r a_{i_r}.}
\tag{3}
\]

Thus the hypothesis is the set inclusion

\[
\boxed{
(Q-P)s+b_0\mathcal A+\cdots+b_d\mathcal A
\subseteq\mathcal A.}
\tag{4}
\]

Here `b A={ba:a in A}` and sums are Minkowski sums in the integers.

## 3. Sumset rigidity

For nonempty finite subsets `X,Y` of the integers,

\[
\boxed{|X+Y|\ge |X|+|Y|-1.}
\tag{5}
\]

Indeed, if

\[
x_1<\cdots<x_m,
\qquad y_1<\cdots<y_n,
\]

then

\[
x_1+y_1<\cdots<x_m+y_1<x_m+y_2<\cdots<x_m+y_n
\]

exhibits `m+n-1` distinct sums.

If two coefficients `b_r,b_t` are nonzero, both scaled alphabets have six
elements, so `(5)` gives at least

\[
6+6-1=11
\]

distinct induced digits before any further summands are added.  This contradicts
`(4)`, whose right side has six elements.  Therefore at most one coefficient is
nonzero.

No coefficient can be nonzero only through cancellation by later variables:
the type entries are independently free because every finite type word has
positive ordinary representatives.

## 4. One-coefficient case

Suppose `b=b_(r_0)` is the unique nonzero coefficient.  Then `(4)` is an
inclusion between two six-element sets and hence an equality:

\[
\boxed{c+b\mathcal A=\mathcal A,
\qquad c=(Q-P)s.}
\tag{6}
\]

If `b>0`, equality of diameters gives `b=1`, and equality of minima gives
`c=0`.

If `b<0`, equality of diameters gives `b=-1`; then reflection symmetry would
force

\[
a_0+a_5=a_1+a_4=a_2+a_3.
\]

But

\[
642719,\qquad625464,\qquad616896
\]

are distinct.  Thus reflection is impossible.

Therefore `b=1`, `c=0`, and since `P-Q=7153` is nonzero, `s=0`.  This proves
`(2)`.

If all coefficients were zero, `(3)` would require `(Q-P)s` to be an allowed
positive digit.  This is impossible because `P-Q=23*311`, while every allowed
digit has prime support contained in `{2,3,7}`.

## 5. Strategic meaning

`L-7301/T-7301` close path-specific two-point contractions.  This theorem is the
full-language counterpart at arbitrary finite order: increasing the fixed
linear observation window cannot manufacture a contracting ordinary section.

A successful boundedness proof must therefore be nonlinear, unbounded-state, or
seed-specific in a way not expressible by one fixed finite convolution of orbit
states.

## 6. Gap audit

- The theorem requires the filter to carry the complete six-branch language.
  A proper sublanguage may have additional relations.
- Coefficients depending on an unbounded arithmetic state are outside scope.
- The theorem does not decide boundedness or divergence of the least roots.
- No counterexample is claimed.
