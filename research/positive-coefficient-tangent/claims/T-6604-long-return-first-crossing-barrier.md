# T-6604 — long returns force a large coefficient bank at first crossing

**Claim ID:** `T-6604`  
**Status:** **PROPOSED**; Section 6 is **SOURCE-DEPENDENT**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** elementary shortcut-Collatz affine algebra; only the polynomial corollary in Section 6 uses an effective Baker lower bound  
**Scope:** finite positive ordinary first-coefficient-crossing segments whose endpoint does not descend  

## 1. Statement

Let

\[
x_t=T^t(n),\qquad 0\le t\le j,
\]

be a positive ordinary shortcut-Collatz segment. Write

\[
q_t=\#\{0\le r<t:x_r\text{ is odd}\},
\qquad
\alpha={\log2\over\log3},
\qquad
D_t=q_t-\alpha t.
\]

Assume that `j` is the first coefficient crossing:

\[
D_t\ge0\quad(0\le t<j),
\qquad
D_j<0,
\tag{1}
\]

and that the endpoint does not descend:

\[
x_j\ge n.
\tag{2}
\]

Put

\[
B=\max_{0\le t<j}D_t,
\qquad
q=q_j,
\qquad
\lambda=j\log2-q\log3>0.
\tag{3}
\]

Suppose the same parity factor of length `L>=1` occurs beginning at two distinct times

\[
0\le a<b\le j-L,
\tag{4}
\]

and suppose the two physical starting states are distinct:

\[
x_a\ne x_b.
\tag{5}
\]

Then the following exact return-gap inequality holds:

\[
\boxed{
2^L+1
<
3^B\left({j\over\lambda}+{j\over2}\right).}
\tag{6}
\]

Equivalently, whenever

\[
3^{-B}(2^L+1)>{j\over2},
\]

one necessarily has

\[
\boxed{
\lambda
<
{j\over 3^{-B}(2^L+1)-j/2}.}
\tag{7}
\]

Thus a long repeated factor forces the first coefficient gap itself to be exponentially small unless it is paid for by a large coefficient bank `B`.

## 2. Dyadic separation of the repeated factor

Let the common length-`L` factor have weight `s` and affine numerator `A`. Starting from either occurrence,

\[
2^Lx_{a+L}=3^sx_a+A,
\qquad
2^Lx_{b+L}=3^sx_b+A.
\]

Subtracting gives

\[
2^L(x_{a+L}-x_{b+L})=3^s(x_a-x_b).
\]

Since `gcd(2^L,3^s)=1`,

\[
2^L\mid x_a-x_b.
\]

By `(5)`,

\[
|x_a-x_b|\ge2^L.
\tag{8}
\]

## 3. Upper height inside the coefficient corridor

For every `t<j`, the exact affine identity can be written

\[
x_t
=3^{D_t}n
 +{1\over2}\sum_{m=1}^{t}
 v_{m-1}3^{D_t-D_m},
\tag{9}
\]

where `v_r=x_r mod 2`.

By `(1)` and `(3)`, every exponent occurring in `(9)` is at most `B`. Therefore

\[
x_t\le3^B\left(n+{t\over2}\right)
\le3^B\left(n+{j\over2}\right)
\qquad(t<j).
\tag{10}
\]

The two positive integers in `(8)` both lie below the right side of `(10)`. Their difference is at least `2^L`, so their maximum is at least `2^L+1`. Hence

\[
\boxed{
2^L+1
\le3^B\left(n+{j\over2}\right).}
\tag{11}
\]

This lower bound is placed on the same ordinary start `n` that appears in the no-descent inequality.

## 4. First crossing gives an exact gap-dependent upper bound

The final crossing step must be even. Therefore the exact affine endpoint is

\[
x_j=e^{-\lambda}n+E_j,
\]

with

\[
0<E_j<{q\over2}<{j\over2}.
\tag{12}
\]

Indeed, each odd-source contribution is

\[
{1\over2}3^{D_j-D_m}<{1\over2}
\]

because `D_j<0<=D_m` at every preceding odd endpoint.

From `(2)` and `(12)`,

\[
n(1-e^{-\lambda})<{j\over2}.
\tag{13}
\]

First crossing gives `0<lambda<=log 2`. On this interval,

\[
1-e^{-\lambda}\ge{\lambda\over2}.
\]

Thus

\[
\boxed{n<{j\over\lambda}.}
\tag{14}
\]

Combining `(11)` and `(14)` proves `(6)`, and rearrangement proves `(7)`. No external theorem enters this core implication.

## 5. Farey/Ostrowski decision interface

Inequality `(7)` is designed to consume an exact lower bound for the particular gap

\[
\lambda=j\log2-q\log3.
\]

For example, if a Farey cell, continued-fraction row, or Ostrowski decomposition proves

\[
\lambda\ge\lambda_0>0,
\]

then the word is excluded as soon as

\[
\boxed{
2^L+1
\ge
3^B\left({j\over\lambda_0}+{j\over2}\right).}
\tag{15}
\]

This couples the two newest positive mechanisms directly:

```text
Diophantine distance of the first crossing
        versus
ordinary dyadic height forced by symbolic recurrence.
```

Unlike a global Baker estimate, `(15)` can be sharp on one exact continued-fraction block and can be checked with rational logarithm intervals.

## 6. Source-dependent uniform polynomial corollary

A standard effective Baker theorem for the multiplicatively independent numbers `2` and `3` supplies effective constants

\[
c_0>0,\qquad \mu>0,
\]

such that every nonzero form with `0<=q<=j` satisfies

\[
\lambda=j\log2-q\log3\ge c_0j^{-\mu}.
\tag{16}
\]

Substitution into `(6)` yields

\[
\boxed{
2^L+1
\le
3^B\left(c_0^{-1}j^{\mu+1}+{j\over2}\right),}
\tag{17}
\]

and hence

\[
\boxed{
L
\le
B\log_2 3
 +(\mu+1)\log_2j
 +\log_2(c_0^{-1}+1/2).}
\tag{18}
\]

Only `(16)--(18)` are source-dependent.

## 7. Asymptotic return barrier

Consider any family of such acyclic no-descent first crossings with lengths `j_r->infinity`, maximum proper-prefix banks `B_r`, and repeated-factor lengths `L_r`.

If

\[
L_r\log2
 -B_r\log3
 -(\mu+1)\log j_r
\longrightarrow+\infty,
\tag{19}
\]

then `(17)` is eventually impossible. Hence no such family exists.

A particularly useful consequence is:

\[
\boxed{
B_r=o(j_r)
\quad\Longrightarrow\quad
L_r=o(j_r)
}
\tag{20}
\]

for the longest repeated parity factor of every surviving family.

Thus a late first crossing with sublinear coefficient bank must become asymptotically recurrence-poor: it cannot contain two copies of any factor occupying a fixed positive fraction of its total length.

## 8. Canonical first-crossing consequence

For a first-crossing word `w` of length `j`, let `r^+(w)` be its least positive parity-cylinder representative and put

\[
y^+(w)=T^j(r^+(w)).
\]

Its affine identity gives

\[
(2^j-3^q)r^+(w)-A_w
=2^j\bigl(r^+(w)-y^+(w)\bigr).
\tag{21}
\]

Therefore the exact target

\[
r^+(w)>{A_w\over2^j-3^q}
\]

is equivalent to

\[
r^+(w)>y^+(w).
\]

If this target fails, the canonical representative itself satisfies the no-descent hypothesis `(2)`. Therefore every non-cycle counterexample to the target must obey `(6)--(7)`, and source-conditionally `(17)--(18)`.

Consequently, any unbounded family of target failures must choose at least one of the following escape mechanisms:

```text
coefficient bank B comparable to the repeated-factor scale;
longest repeated factor o(j);
a repeated physical state, hence a positive cycle;
or an exceptionally small first-crossing logarithmic gap satisfying (7).
```

This is a direct narrowing of the delayed-crossing blocker, not a finite prefix census.

## 9. Families eliminated

The source-dependent corollary excludes every unbounded no-descent first-crossing family for which

- the proper-prefix bank is sublinear in `j`; and
- a repeated factor has length at least `delta*j` for some fixed `delta>0`.

The exact core `(15)` can eliminate much broader finite or cofinal families whenever their Diophantine gaps are certified explicitly.

The asymptotic conclusion includes, after their return constants are checked, bounded-bank families generated by primitive substitutions, linearly recurrent systems, Sturmian/mechanical systems, and bounded-distortion finite-state codings with linear-size repeated supertiles.

No blanket claim about every substitution or transducer is made without verifying the stated return hypothesis.

## 10. Gap audit

- The theorem does not exclude high-bank, recurrence-poor first-crossing words.
- The Baker constants in Section 6 are not instantiated numerically; source reconstruction is required before promoting that corollary.
- If `x_a=x_b`, the segment contains a positive cycle and must be handled by the full-denominator cycle lane.
- The theorem does not prove the universal canonical descent inequality.
- It nevertheless closes a complete asymptotic class with growing lengths and supplies an exact Farey-compatible gate for further exclusions.
