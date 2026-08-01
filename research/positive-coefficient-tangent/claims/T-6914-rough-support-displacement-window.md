# T-6914 — Rough support shrinks the complete displacement window

**Claim ID:** `T-6914`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-08-01  
**Issue:** #75  
**Dependencies:** PR #81 `L-6808/L-6811/T-6810`; corrected `L-6909`  
**Scope:** nonmechanical first-crossing words compared with the upper-mechanical extremizer

## 1. Statement

Fix a valid first-crossing pair `(j,q)`. Let `u` be the upper-mechanical word
and `v` another first-crossing word. Write their odd positions as

\[
\bar d_1<\cdots<\bar d_q,
\qquad
d_1<\cdots<d_q,
\]

with

\[
h_i=\bar d_i-d_i\ge0,
\qquad
R=\#\{i:h_i>0\}.
\]

Let `A_u,A_v` be the affine numerators and put

\[
C=\frac{3^q}{2^j}.
\]

Then

\[
\boxed{
\frac{A_v}{3^q}
<
\frac{A_u}{3^q}
-
\frac{R}{12},
}
\tag{1}
\]

and hence

\[
\boxed{
\frac{A_v}{2^j}
<
\frac{A_u}{2^j}
-
\frac{C R}{12}.
}
\tag{2}
\]

Every non-descending realization of `v` therefore has

\[
\boxed{
0\le d
<
\frac{A_u}{2^j}
-
\frac{C R}{12}.
}
\tag{3}
\]

## 2. Mechanical odd terms exceed one sixth

The normalized numerator is

\[
\frac{A_w}{3^q}
=
\sum_{i=1}^{q}\frac{2^{d_i}}{3^i}.
\tag{4}
\]

At the mechanical position `\bar d_i`, put

\[
B_i=i-1-\alpha\bar d_i,
\qquad
\alpha=\frac{\log2}{\log3}.
\]

Because the bit at `\bar d_i` is odd, the mechanical ceiling increases there.
Thus

\[
0\le B_i<\alpha.
\tag{5}
\]

Consequently,

\[
\frac{2^{\bar d_i}}{3^i}
=
\frac13\,3^{-B_i}
>
\frac13\,3^{-\alpha}
=
\frac16.
\tag{6}
\]

## 3. Every displaced odd position pays at least one twelfth

For `h_i>0`,

\[
\frac{2^{d_i}}{3^i}
=
2^{-h_i}
\frac{2^{\bar d_i}}{3^i}.
\]

Therefore the loss at that position is

\[
\frac{2^{\bar d_i}-2^{d_i}}{3^i}
=
\frac{2^{\bar d_i}}{3^i}(1-2^{-h_i})
>
\frac16\cdot\frac12
=
\frac1{12}.
\tag{7}
\]

Summing `(7)` over the `R` displaced positions proves `(1)`, and multiplication
by `C` proves `(2)`.

Corrected `L-6909` gives `d<A_v/2^j`, proving `(3)`.

## 4. Source-qualified square-root sharpening

PR #81 `T-6810` gives, for every unbounded acyclic exceptional family,

\[
R
\ge
\sqrt{\frac{\alpha j}{2}}-O(\log j).
\tag{8}
\]

Combining `(2)` and `(8)`,

\[
\boxed{
d
<
\frac{A_u}{2^j}
-
\frac{C}{12}
\sqrt{\frac{\alpha j}{2}}
+
O(C\log j).
}
\tag{9}
\]

Thus the roughness forced by the return theorem removes a square-root-width
portion of the already short common-residue window.

## 5. A dense-support cycle-only criterion

Because `d` is an integer, if

\[
\frac{A_u}{2^j}-\frac{CR}{12}\le1,
\tag{10}
\]

then every non-descending realization must have

\[
\boxed{d=0.}
\tag{11}
\]

So sufficiently dense displaced support collapses the acyclic near-return
level directly to the positive-cycle equation. The remaining `d=0` level
still requires complete denominator exclusion.

## 6. Interaction with complete factors

The factor threshold in `L-6912` may use the smaller word-specific window

\[
E_v
<
E_u-\frac{CR}{12}.
\]

Every prime-power or unitary block above this reduced threshold determines
the common `d` exactly. Rough support therefore enlarges the set of factors
eligible for pairwise synchronization.

## 7. Gap audit

- The square-root reduction is not large enough by itself to make `(10)`
  universal.
- The cycle level remains open.
- The theorem does not force any two large-factor residues to disagree.
- The strict constant `1/12` uses the odd-position geometry of the upper
  mechanical word and is not a generic Hamming estimate.
