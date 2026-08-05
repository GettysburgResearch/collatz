# L-9608 — Equal-summary libraries below the sharp carry threshold collapse to one block constant

**Claim ID:** `L-9608`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-26  
**Dependencies:** elementary accelerated affine-word algebra; `L-8402` or `L-9607` only for comparison  
**Scope:** arbitrary finite libraries of accelerated blocks with one common length and total valuation  
**Related counterexample candidates:** none

## 1. Equal-summary library

Let

\[
\mathcal B=\{B_s:s\in\Sigma\}
\]

be a finite library of nonempty accelerated valuation blocks. Assume every block has the same odd-state length `k`, total valuation `A`, and affine form

\[
S_{B_s}(x)=\frac{P x+C_s}{Q},
\qquad
P=3^k,
\qquad
Q=2^A,
\qquad
Q>P.
\tag{1}
\]

Put

\[
C_*=\min_{s\in\Sigma}C_s,
\qquad
W=\max_{s\in\Sigma}C_s-C_*.
\tag{2}
\]

The load-bearing hypothesis is the sharp carry-width inequality

\[
\boxed{W<Q+P.}
\tag{3}
\]

For an arbitrary block word

\[
\mathbf s=(s_0,\ldots,s_{R-1})\in\Sigma^R,
\qquad R\ge1,
\]

write the chronological concatenation as

\[
B_{\mathbf s}=B_{s_0}\cdots B_{s_{R-1}}.
\]

Its affine constant is

\[
\boxed{
C_{\mathbf s}
=\sum_{j=0}^{R-1}P^{R-1-j}Q^j C_{s_j}.}
\tag{4}
\]

Define

\[
G_R=\frac{Q^R-P^R}{Q-P}
=\sum_{j=0}^{R-1}P^{R-1-j}Q^j.
\tag{5}
\]

## 2. Rigidity theorem

If the complete cycle denominator divides the composite numerator,

\[
\boxed{Q^R-P^R\mid C_{\mathbf s},}
\tag{6}
\]

then every selected block has the same affine constant:

\[
\boxed{
C_{s_0}=C_{s_1}=\cdots=C_{s_{R-1}}.}
\tag{7}
\]

Moreover, for that common value `C`, condition `(6)` is equivalent to

\[
\boxed{Q-P\mid C.}
\tag{8}
\]

Consequently an equal-summary library whose numerator diameter is below `Q+P` cannot synthesize a new full-denominator cycle by changing block types, ordering them, or increasing the repetition length. Every possible affine divisor hit is already the fixed point of one constant class in the original library.

If the constants in the library are pairwise distinct, `(7)` says that the block word itself is constant. If no single library block satisfies `Q-P|C_s`, then no word over the library, at any length, satisfies the full cycle divisibility condition.

## 3. Reduction to a zero carry word

Put

\[
\delta_s=C_s-C_*,
\qquad 0\le\delta_s\le W.
\tag{9}
\]

Equation `(4)` becomes

\[
C_{\mathbf s}=C_*G_R+H,
\tag{10}
\]

where

\[
H=\sum_{j=0}^{R-1}P^{R-1-j}Q^j\delta_{s_j}.
\tag{11}
\]

Since

\[
Q^R-P^R=(Q-P)G_R,
\]

condition `(6)` implies `G_R|C_(mathbf s)`. The first term in `(10)` is already divisible by `G_R`, hence

\[
G_R\mid H.
\tag{12}
\]

All weights in `(11)` are positive, so

\[
0\le H\le WG_R.
\]

Therefore

\[
H=tG_R
\tag{13}
\]

for one integer `t` with `0\le t\le W`.

Set

\[
\varepsilon_j=\delta_{s_j}-t.
\tag{14}
\]

Subtracting `(13)` from `(11)` gives

\[
\boxed{
\sum_{j=0}^{R-1}P^{R-1-j}Q^j\varepsilon_j=0.}
\tag{15}
\]

Equivalently define the integral carry recursion

\[
\boxed{
c_0=0,
\qquad
Qc_{j+1}=Pc_j+\varepsilon_j.}
\tag{16}
\]

Then `(15)` is equivalent to

\[
\boxed{c_R=0.}
\tag{17}
\]

Indeed, iteration of `(16)` gives

\[
Q^R c_R=
\sum_{j=0}^{R-1}P^{R-1-j}Q^j\varepsilon_j.
\]

## 4. The first nonzero carry cannot return

Assume for contradiction that some `\varepsilon_j` is nonzero, and let `m` be the first such index. Then `c_m=0`. Reducing the remaining identity `(15)` modulo `Q` gives

\[
Q\mid\varepsilon_m.
\tag{18}
\]

Because

\[
|\varepsilon_m|\le W<Q+P<2Q,
\]

one has

\[
\varepsilon_m=Q
\qquad\hbox{or}\qquad
\varepsilon_m=-Q.
\tag{19}
\]

### Positive first carry

If `\varepsilon_m=Q`, then

\[
\delta_{s_m}=t+Q\le W,
\]

so

\[
t\le W-Q<P.
\tag{20}
\]

The next carry is `c_(m+1)=1`. For every later digit,

\[
\varepsilon_j=\delta_{s_j}-t\ge-t>-P.
\]

Hence if `c_j>=1`, then

\[
Pc_j+\varepsilon_j>P-P=0,
\]

and the integral recursion `(16)` gives `c_(j+1)>=1`. The carry can never return to zero, contradicting `(17)`.

### Negative first carry

If `\varepsilon_m=-Q`, then

\[
t=\delta_{s_m}+Q\ge Q.
\]

For every later digit,

\[
\varepsilon_j\le W-t\le W-Q<P.
\tag{21}
\]

The next carry is `c_(m+1)=-1`. If `c_j<=-1`, then

\[
Pc_j+\varepsilon_j<-P+P=0,
\]

so the integral recursion gives `c_(j+1)<=-1`. Again the carry cannot return to zero.

Both alternatives are impossible. Therefore every `\varepsilon_j=0`, which proves `(7)`.

If the common block constant is `C`, then `(4)` gives

\[
C_{\mathbf s}=CG_R.
\]

Since the denominator is `(Q-P)G_R`, exact divisibility is equivalent to `(8)`. ∎

## 5. Sharpness of the threshold

The strict threshold `W<Q+P` is best possible for the abstract carry problem.

At

\[
W=Q+P,
\]

consider two allowed offset digits

\[
\delta_0=0,
\qquad
\delta_1=Q+P,
\]

at repetition length `R=2`, and put `t=Q`. Then

\[
\varepsilon_0=-Q,
\qquad
\varepsilon_1=P,
\]

and

\[
P\varepsilon_0+Q\varepsilon_1=0.
\]

The carry path is

\[
0\longmapsto-1\longmapsto0.
\]

Thus a nonconstant two-block solution exists exactly at the boundary. This is an algebraic sharpness example; it is not asserted that an accelerated Collatz library realizes these two constants.

Accordingly,

\[
\boxed{
\text{numerator diameter at least }2^A+3^k
}
\tag{22}
\]

is a necessary condition for a genuinely mixed equal-summary repair circuit.

## 6. Corollary for disjoint replacement libraries

Fix one block and a collection of disjoint same-summary local replacements whose signed numerator changes are

\[
\Delta_1,\ldots,\Delta_m.
\]

Every one of the `2^m` replacement combinations has the same `(k,A)`, and its constant lies in an interval of width at most

\[
\sum_{j=1}^m|\Delta_j|.
\]

Hence

\[
\boxed{
\sum_j|\Delta_j|<2^A+3^k
}
\tag{23}
\]

places the entire `2^m`-block alphabet under the rigidity theorem. Arbitrary words over that alphabet, at arbitrary repetition length, reduce to pure powers of one replacement combination.

For Christoffel/Farey swaps, `L-9606` gives each `\Delta_j` as one explicit signed `{2,3}`-unit, so `(23)` is an exact integer check rather than an asymptotic estimate.

## 7. Relationship to earlier work

`T-9607` handles a binary library of the two standard Christoffel conjugates by proving a coprimality-based all-or-none geometric-subsum theorem. `L-9608` is different and strictly broader in alphabet size:

- it permits any finite number of block types;
- it uses no pairwise coprimality of constant differences;
- it permits arbitrary ordering and repetition length;
- it gives the exact sharp escape threshold `W>=Q+P`.

The price is the explicit numerator-diameter hypothesis `(3)`.

## 8. Gap audit

- The theorem is an affine full-denominator obstruction. Exact valuation replay remains required for a surviving single-block fixed point.
- Libraries with diameter at least `Q+P` may support nonzero carry paths and are not excluded.
- Scale-varying summaries, overlapping replacements, and genuinely nonaligned hierarchical circuits may leave the theorem's scope.
- Equal constants can arise from different chronological words; they share the same affine map but their local replay domains must still be audited.
- The sharpness example is an abstract equal-summary digit library, not a positive Collatz cycle.
- No positive cycle or divergent orbit is constructed.