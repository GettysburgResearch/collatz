# L-6913 — Resultant-root normal form for the complete displacement residue

**Claim ID:** `L-6913`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-08-01  
**Issue:** #75  
**Dependencies:** corrected `L-6909`; elementary resultants and Bézout  
**Scope:** first-crossing lengths with `gcd(j,q)=1`; componentwise extension recorded for general gcd

## 1. Universal resultant root

Put

\[
P=2^j,\qquad Q=3^q,\qquad D=P-Q,
\]

and first assume

\[
\gcd(j,q)=1.
\tag{1}
\]

Choose integers `a,b` with

\[
aq+bj=1.
\tag{2}
\]

Because `2` and `3` are units modulo the odd integer `D`, define

\[
z=2^a3^b\in(\mathbf Z/D\mathbf Z)^\times.
\tag{3}
\]

Using `2^j≡3^q (mod D)`,

\[
\boxed{z^q=2,\qquad z^j=3\pmod D.}
\tag{4}
\]

Moreover,

\[
\boxed{
\left|\operatorname{Res}(X^q-2,X^j-3)\right|
=
2^j-3^q
=
D.}
\tag{5}
\]

Thus every complete prime-power factor of `D` sees the reduction of one
universal common root of the two binomials.

## 2. First-crossing excess exponents

Write the odd positions as

\[
0=d_1<d_2<\cdots<d_q\le j-2.
\tag{6}
\]

Define

\[
\boxed{\gamma_i=j(i-1)-q d_i.}
\tag{7}
\]

The proper first-crossing inequalities imply `gamma_i>=0`. Indeed, before
the `i`th odd bit,

\[
3^{i-1}\ge2^{d_i},
\]

while `q/j<log 2/log 3`, so

\[
q d_i\le j(i-1).
\]

The affine numerator satisfies

\[
\frac{A_w}{Q}
=
\sum_{i=1}^{q}2^{d_i}3^{-i}.
\tag{8}
\]

Using `(4)` and `(7)` gives the exact modular collapse

\[
2^{d_i}3^{-i}
=
z^{q d_i-j i}
=
\frac13z^{-\gamma_i}.
\]

Therefore the common displacement residue is

\[
\boxed{
3d
\equiv
\sum_{i=1}^{q}z^{-\gamma_i}
\pmod D.}
\tag{9}
\]

Equation `(9)` holds simultaneously modulo every complete prime-power factor
of `D`. It is equivalent to `A_w≡Qd (mod D)`.

## 3. Excess-path form

Writing

\[
d_i=i-1+e_i,
\qquad
0=e_1\le\cdots\le e_q\le j-q-1,
\]

one has

\[
\boxed{\gamma_i=(j-q)(i-1)-q e_i.}
\tag{10}
\]

Thus the complete denominator tests one monotone path through one lacunary
Laurent sum at the resultant root.

The strict order window in PR #81 `L-6809` makes the physical `e_i` path
recoverable from compatible local exponent residues. Equation `(9)` adds the
missing common small-value condition.

## 4. Displacement from the upper mechanical word

Let `\bar d_i` and `\bar\gamma_i` denote the upper-mechanical positions and
exponents. For any other first-crossing word, put

\[
h_i=\bar d_i-d_i\ge0.
\tag{11}
\]

Then

\[
\gamma_i=\bar\gamma_i+q h_i.
\tag{12}
\]

Since `z^q=2`,

\[
\boxed{
3d
\equiv
\sum_{i=1}^{q}
z^{-\bar\gamma_i}2^{-h_i}
\pmod D.}
\tag{13}
\]

Subtracting the mechanical value gives one support-sensitive lacunary
displacement polynomial:

\[
\boxed{
3(d-d_{\rm mech})
\equiv
\sum_{h_i>0}
z^{-\bar\gamma_i}(2^{-h_i}-1)
\pmod D.}
\tag{14}
\]

The right side has exactly the displaced support from PR #81. Every surviving
acyclic family has at least square-root many nonzero terms and
two-thirds-scale total displacement, but remains polynomially sparse across
words.

## 5. Prime-power interpretation

For every `M_\nu|D`, let `z_\nu` be the reduction of `z`. Then

\[
z_\nu^q=2,\qquad z_\nu^j=3\pmod {M_\nu},
\]

and

\[
\boxed{
3d
\equiv
\sum_i z_\nu^{-\gamma_i}
\pmod {M_\nu}.}
\tag{15}
\]

The full-factor synchronization theorem `L-6912` says that every factor larger
than the real displacement window must return the same ordinary integer `d`,
not merely a local residue.

Thus FC* asks for a lower bound on the least nonnegative value of the
lacunary sum `(15)` that is uniform over every resultant factor and compatible
with the same monotone path.

## 6. General gcd

For

\[
g=\gcd(j,q)>1,
\]

the binomial resultant is

\[
\left|\operatorname{Res}(X^q-2,X^j-3)\right|
=
\left|2^{j/g}-3^{q/g}\right|^g.
\tag{16}
\]

Meanwhile

\[
2^j-3^q
=
\prod_{\ell\mid g}
\Phi_\ell(2^{j/g},3^{q/g}),
\tag{17}
\]

with `Phi_\ell(X,Y)` the homogeneous cyclotomic polynomial. On each
coprime component one obtains the corresponding twisted common-root form.
The clean scalar root `(3)` is therefore the primitive `g=1` model; the
complete all-`j` proof must retain every homogeneous component.

## 7. What a product-formula proof must establish

The structural data now reduce the unrestricted residue problem to:

\[
\boxed{
\left[
\frac13
\sum_i z^{-\gamma_i}
\right]_D
\ge
\frac{A_w}{2^j},
}
\tag{18}
\]

apart from the trivial cycle, for a monotone path whose departures are early,
square-root-supported, and two-thirds-scale.

A successful resultant or product-formula argument must therefore control a
growing-support lacunary polynomial at all reductions of one resultant root.
Bounds depending only on degree, coefficient height, or number of candidate
words do not presently imply `(18)`.

## 8. Gap audit

- The resultant normal form is exact but is not a residue lower bound.
- Square-root support grows with `j`; fixed-sparsity resultant theorems do not
  directly apply.
- The cycle case is the zero value of `(9)` and remains included.
- For `g>1`, every homogeneous cyclotomic component must be retained.
- The smallest missing theorem is a uniform least-residue/product-formula
  bound for `(13)` or a contradiction between two complete factor blocks.
