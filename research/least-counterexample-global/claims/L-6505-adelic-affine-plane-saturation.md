# L-6505 — Exact adelic saturation of the Lane-A affine orbit plane

**Claim ID:** `L-6505`  
**Title:** The two-place product gain at a zero-rate Lane-A cusp is exactly consumed by the known affine orbit plane  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-08-01  
**Dependencies:** `L-6504`; elementary product-formula normalization  
**Scope:** an actual positive ordinary all-prefix-supercritical orbit at the cusp subsequence of `L-6504`  
**Related candidates:** none

## 1. Exact affine point

Let `n` be a fixed positive ordinary integer and let a length-`k` prefix of its shortcut-Collatz orbit have `q` odd steps, affine numerator `A`, and endpoint

\[
s=T^k(n).
\]

Thus

\[
\boxed{A+n3^q=s2^k.}
\tag{1}
\]

Assume the prefix is coefficient-supercritical at every proper stage. In particular the first parity bit is odd. The usual numerator expansion is

\[
A=
\sum_{m=1}^{k}
 v_{m-1}2^{m-1}3^{q-q_m}.
\tag{2}
\]

Then

\[
\boxed{\gcd(A,6)=1.}
\tag{3}
\]

Indeed, the first summand in `(2)` is odd and every later summand is even, so `A` is odd. Modulo three, only the summand belonging to the final odd step survives, and it is a nonzero power of two.

Put

\[
X=(X_0,X_1,X_2)=(A,3^q,2^k)
\in\mathbf Z^3,
\tag{4}
\]

and

\[
H(X)=\max(A,3^q,2^k).
\tag{5}
\]

Equation `(3)` makes `X` primitive.

## 2. Three exact systems of linear forms

Use the standard absolute values

\[
|2|_2=\frac12,
\qquad
|3|_3=\frac13.
\]

At the three places `infinity,2,3`, take respectively

\[
\begin{array}{lll}
L_{0,\infty}=X_0,&L_{1,\infty}=X_1,&L_{2,\infty}=X_2,\\[1mm]
L_{0,2}=X_0+nX_1,&L_{1,2}=X_1,&L_{2,2}=X_2,\\[1mm]
L_{0,3}=X_0-sX_2,&L_{1,3}=X_1,&L_{2,3}=X_2.
\end{array}
\tag{6}
\]

Each coefficient matrix has determinant one. By `(1)`,

\[
L_{0,2}(X)=s2^k,
\qquad
L_{0,3}(X)=-n3^q.
\tag{7}
\]

Therefore the unnormalized three-place product is exactly

\[
\boxed{
\prod_{v\in\{\infty,2,3\}}
\prod_{i=0}^{2}|L_{i,v}(X)|_v
=
\frac{A}{2^k3^q}\,|s|_2|n|_3.}
\tag{8}
\]

In particular,

\[
\prod_{v,i}|L_{i,v}(X)|_v
\le\frac{A}{2^k3^q}.
\tag{9}
\]

## 3. Cusp exponent

For every odd step ending at time `m`, all-prefix supercriticality gives

\[
D_m=q_m-\frac{\log2}{\log3}m
\ge1-\frac{\log2}{\log3}.
\]

Hence

\[
\frac{2^{m-1}}{3^{q_m}}
=\frac12\,3^{-D_m}
\le\frac13.
\]

Using `(2)`,

\[
\boxed{
0<A\le\frac q3\,3^q\le\frac k3\,3^q.}
\tag{10}
\]

Now take the zero-rate cusp sequence of `L-6504`, so

\[
D_k=o(k),
\qquad
\log s=o(k).
\tag{11}
\]

Since

\[
3^q=2^k3^{D_k}\ge2^k,
\]

relations `(5)` and `(10)` give

\[
\log H(X)=k\log2+o(k).
\tag{12}
\]

Consequently `(9)` implies

\[
\boxed{
\prod_{v,i}|L_{i,v}(X)|_v
\le H(X)^{-1+o(1)}.}
\tag{13}
\]

Because `A` is a unit at both finite places, the local sup norms of `X` at `2` and `3` are one. Dividing by the three powers of the projective height at the Archimedean place therefore gives

\[
\boxed{
\prod_{v\in\{\infty,2,3\}}
\prod_{i=0}^{2}
\frac{|L_{i,v}(X)|_v}{\|X\|_v}
\le H(X)^{-4+o(1)}.}
\tag{14}
\]

This is one full power beyond the ordinary three-variable Subspace-Theorem exponent.

## 4. Why the gain gives no contradiction

The point satisfies the exact slowly moving linear relation

\[
\boxed{X_0+nX_1-sX_2=0.}
\tag{15}
\]

At the cusp,

\[
h(1,n,-s)=\log\max(1,n,s)=o(\log H(X)).
\tag{16}
\]

Thus the exceptional hyperplane predicted by a moving-target argument is already present explicitly: it is the physical affine orbit equation itself.

This is not a merely verbal degeneracy. Quotient the plane `(15)` by using

\[
Y=(Y_1,Y_2)=(3^q,2^k).
\tag{17}
\]

The coordinate product over the same places is exactly

\[
\boxed{
|Y_1Y_2|_\infty
|Y_1Y_2|_2
|Y_1Y_2|_3
=(3^q2^k)(2^{-k})(3^{-q})=1.}
\tag{18}
\]

Since `3^q>=2^k`, the normalized projective-line product is exactly

\[
\boxed{H(Y)^{-2}.}
\tag{19}
\]

There is no residual power saving after the known affine plane has been removed.

## 5. Exact implication

The standard two-place product-formula attack does not exclude Lane A. Its complete extra smallness is equivalent to one known codimension-one relation.

A valid Subspace/Ridout closure must supply a **second independent small form**. Concretely, it is enough to find forms on the quotient coordinate `Y=(3^q,2^k)` whose coefficient height is `o(k)`, whose restriction is not a coordinate or a multiple of `(15)`, and for which the normalized product gains one fixed power beyond `(19)`.

No such second form follows from the source/end height assumptions alone.

## 6. Ridout normalization audit

The fixed-source congruence can also be written

\[
n+\frac{A}{3^q}=\frac{s2^k}{3^q}.
\tag{20}
\]

At the `2`-adic place,

\[
\left|n+\frac{A}{3^q}\right|_2
=2^{-k}|s|_2.
\tag{21}
\]

The rational approximant `-A/3^q` has height `3^{q+o(q)}` by `(10)`, while `2^{-k}=3^{-q+o(q)}` at the cusp. Thus `(21)` has approximation exponent only `1+o(1)`, not a Roth/Ridout exponent exceeding two. The one-place route also does not cross its theorem threshold.

## 7. Gap audit

- Equation `(14)` is genuine, but `(15)` explains it completely.
- The moving coefficient `s` is small enough for a moving-target framework; that does not help because the sequence is identically degenerate in the moving plane.
- Quotienting by `(15)` leaves exact product-formula equality `(18)`.
- The argument supplies no lower bound for either raw canonical boundary rate.
- Any claimed Lane-A proof using only `(14)` without classifying `(15)` repeats a standard Subspace-Theorem degeneracy error.

## 8. Handoff

Attack one of the following exact objects:

1. a second independent quotient form with a strict product power saving;
2. finite multiplicative rank of the normalized two-term split, which is addressed negatively in `T-6507`;
3. an internal-word theorem controlling the prime support or height of `A` strongly enough that `(15)` cannot absorb every smallness gain.
