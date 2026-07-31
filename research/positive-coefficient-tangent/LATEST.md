# Latest coefficient-envelope stack

**Updated:** 2026-08-01  
**Active draft PR:** #83  
**Namespace:** `69xx`

No proof of Collatz is claimed.

## Synced collaborator state

This pass reads PR #81 at

```text
086ac39d93d7c1aad9d05732f5fc11c9ce349530
```

and retains all corrections concerning:

```text
source versus endpoint labels;
the one-third displacement window;
complete-prime-power compatibility;
square-root displaced support;
two-thirds integrated displacement;
logarithmic early departure and self-shadowing;
zero family entropy versus internal factor complexity.
```

## Current FC* equation

For source `r`, endpoint `s=r+d`, and

```text
P=2^j,
Q=3^q,
D=P-Q,
```

one has

\[
\boxed{A_w=Dr+Pd=Ds+Qd,}
\]

with

\[
\boxed{0\le d<A_w/P<q/3.}
\]

The endpoint-labelled form is

\[
A_w=sD+dQ;
\]

the source-labelled form is

\[
A_w=rD+dP.
\]

`d=0` is the positive-cycle level and `d>0` is an acyclic near-return.

## New complete-factor theorem

Factor

\[
D=\prod M_\nu
\]

into complete prime powers and put

\[
\delta_\nu=[A_wQ^{-1}]_{M_\nu}.
\]

Every factor larger than `A_w/P` must satisfy

\[
\boxed{\delta_\nu=d.}
\]

Hence any two large factors with unequal local residues exclude the word.
The exact gcd profile is

\[
\boxed{\gcd(D,A_w)=\gcd(D,d).}
\]

For a large unitary factor `U|D`, a second quotient jet recovers the exact
endpoint and source. Cofinally, the complete factorization has one of two
forms:

```text
balanced:
  D=UV with both U,V larger than the ordinary endpoint bound;
  both blocks must return the same d and quotient jet;

dominant:
  D=Wc with W a giant prime power and c a small cofactor;
  W determines d,r,s and c must complete the divisibility.
```

These are the two irreducible FC* objects.

## Resultant-root normal form

When `gcd(j,q)=1`, choose `a,b` with `aq+bj=1` and put

\[
z=2^a3^b\pmod D.
\]

Then

\[
z^q=2,\qquad z^j=3,\qquad
|\operatorname{Res}(X^q-2,X^j-3)|=D.
\]

For odd positions `d_i`, define

\[
\gamma_i=j(i-1)-qd_i\ge0.
\]

The common displacement is exactly

\[
\boxed{
3d\equiv\sum_i z^{-\gamma_i}\pmod D.}
\]

Relative to the mechanical word, this is

\[
3d\equiv
\sum_i z^{-\bar\gamma_i}2^{-h_i}\pmod D.
\]

Thus FC* is a least-residue theorem for one rough lacunary polynomial at a
universal resultant root, simultaneously over every complete denominator
factor.

## Roughness shrinks the bad interval

If `R` odd positions are displaced from the upper-mechanical word, then

\[
\boxed{
A_v/2^j
<
A_{\rm mech}/2^j
-
(3^q/2^j)R/12.}
\]

Therefore the possible `d` interval loses at least that amount. PR #81 gives

\[
R\ge\sqrt{(\log2/(2\log3))j}-O(\log j)
\]

for every unbounded acyclic exceptional family.

This is a genuine square-root improvement but does not yet force the local
jets to disagree.

## X-6912 method boundary

Exact finite regression through length `27`:

```text
first-crossing words:             502,523
nontrivial canonical failures:         0
single-prime-power strategy failures:  3
```

The first local-strategy failure is

```text
j=27,
q=17,
D=5*71*14303.
```

Three descending words have every individual prime-power residue inside the
bad interval. A proper two-factor CRT block rejects each one.

Therefore one-factor size arguments cannot prove FC*. Cross-factor
synchronization is a mathematically necessary layer, not merely an
implementation detail.

## Current exact frontier

FC* is not proved.

The final complete objects are:

```text
Object B:
  balanced large-factor blocks with identical d and identical endpoint jet;

Object G:
  one giant prime-power block returning small d,r,s
  plus one completing small cofactor.
```

Equivalently, prove that the resultant-root sum cannot have a least residue
below `A_w/2^j`, including residue zero.

SC* remains separate:

```text
min_{w in W_N^sup} r_w -> infinity.
```

## New claims and artifact

```text
L-6912  complete-factor synchronization and quotient jets
L-6913  resultant-root lacunary normal form
T-6914  rough-support displacement-window shrinkage
R-6915  exact cross-factor method boundary
X-6912  independent factor-synchronization regression
```
