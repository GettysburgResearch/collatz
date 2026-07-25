# L-9608 — Narrow equal-summary libraries collapse to one block constant

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

The load-bearing hypothesis is

\[
\boxed{W<Q.}
\tag{3}
\]

For an arbitrary block word

\[
\mathbf s=(s_0,\ldots,s_{R-1})\in\Sigma^R,
\qquad R\ge1,
\]

write `B_mathbf{s}=B_(s_0)\cdots B_(s_(R-1))`. Its affine constant is

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

Consequently a narrow equal-summary library cannot synthesize a new full-denominator cycle by changing block types, ordering them, or increasing the repetition length. Every possible affine divisor hit is already the fixed point of one constant class in the original library.

If the constants in the library are pairwise distinct, `(7)` says that the block word itself is constant. If no single library block satisfies `Q-P|C_s`, then no word over the library, at any length, satisfies the full cycle divisibility condition.

## 3. Proof

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

condition `(6)` implies `G_R|C_{\mathbf s}`. The first term in `(10)` is already divisible by `G_R`, hence

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

Subtract `(13)` from `(11)` and set

\[
\varepsilon_j=\delta_{s_j}-t.
\]

Then

\[
\sum_{j=0}^{R-1}P^{R-1-j}Q^j\varepsilon_j=0.
\tag{14}
\]

Reduce `(14)` modulo `Q`. Every term except the first vanishes, so

\[
P^{R-1}\varepsilon_0\equiv0\pmod Q.
\]

Because `P` is odd, it is invertible modulo the power of two `Q`. Thus `Q|\varepsilon_0`. But

\[
|\varepsilon_0|\le W<Q,
\]

so `\varepsilon_0=0`.

After the first `m` coefficients have been proved zero, divide `(14)` by `Q^m` and reduce the remaining identity modulo `Q`. This gives

\[
P^{R-1-m}\varepsilon_m\equiv0\pmod Q,
\]

and the same width bound forces `\varepsilon_m=0`. Induction yields

\[
\delta_{s_j}=t
\qquad(0\le j<R),
\]

which is `(7)`.

If the common block constant is `C`, then `(4)` gives

\[
C_{\mathbf s}=CG_R.
\]

Since the denominator is `(Q-P)G_R`, exact divisibility is equivalent to `(8)`. ∎

## 4. Carry interpretation beyond the narrow regime

The proof exposes the exact carry machine hidden in an arbitrary equal-summary library. Whenever `H=tG_R`, define

\[
c_0=0,
\qquad
Qc_{j+1}=Pc_j+\delta_{s_j}-t.
\tag{15}
\]

The polynomial identity is equivalent to an integral carry path satisfying

\[
c_R=0.
\tag{16}
\]

Under `(3)`, the first congruence in `(15)` forces `c_1=0`, and induction forces every carry and every digit difference to vanish. If `W\ge Q`, nonzero carries become possible. Thus

\[
\boxed{
\text{numerator diameter at least }2^A
}
\]

is a necessary condition for a genuinely mixed equal-summary repair circuit.

This is the sharp architectural escape boundary: adding a third, fourth, or thousandth block type does not help unless the library spans at least one complete dyadic block radix or otherwise changes the summary from position to position.

## 5. Corollary for disjoint replacement libraries

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
\sum_j|\Delta_j|<2^A
}
\tag{17}
\]

places the entire `2^m`-block alphabet under the rigidity theorem. Arbitrary words over that alphabet, at arbitrary repetition length, reduce to pure powers of one replacement combination.

For Christoffel/Farey swaps, `L-9606` gives each `\Delta_j` as one explicit signed `{2,3}`-unit, so `(17)` is an exact integer check rather than an asymptotic estimate.

## 6. Relationship to earlier work

`T-9607` handles a binary library of the two standard Christoffel conjugates by proving a coprimality-based all-or-none geometric-subsum theorem. `L-9608` is different and strictly broader in alphabet size:

- it permits any finite number of block types;
- it uses no pairwise coprimality of constant differences;
- it permits arbitrary ordering and repetition length;
- it gives the exact escape threshold `W>=Q`.

The price is the explicit numerator-diameter hypothesis `(3)`.

## 7. Gap audit

- The theorem is an affine full-denominator obstruction. Exact valuation replay remains required for a surviving single-block fixed point.
- Libraries with diameter at least `Q` may support nonzero carry paths and are not excluded.
- Scale-varying summaries, overlapping replacements, and genuinely nonaligned hierarchical circuits may leave the theorem's scope.
- Equal constants can arise from different chronological words; they share the same affine map but their local replay domains must still be audited.
- No positive cycle or divergent orbit is constructed.