# L-6603 — harmonic-mean ceiling for a no-descent first crossing

**Claim ID:** `L-6603`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** elementary shortcut-Collatz product identity and AM--GM  
**Literature comparison:** independently reconstructs the relevant Rozier--Terracol Theorem 4.1 / Corollaries 4.2--4.3 interface  
**Scope:** positive ordinary first-coefficient-crossing segments whose endpoint does not descend  

## 1. Statement

Let

\[
x_t=T^t(n),\qquad0\le t\le j,
\]

be a positive ordinary shortcut-Collatz segment. Let `q` be the number of odd sources among

\[
x_0,\ldots,x_{j-1}.
\]

Assume

\[
3^{q_t}\ge2^t
\qquad(0\le t<j),
\tag{1}
\]

while

\[
3^q<2^j,
\tag{2}
\]

and assume the endpoint does not descend:

\[
x_j\ge n.
\tag{3}
\]

Let

\[
m_1,\ldots,m_q
\]

be the odd source values among `x_0,...,x_(j-1)`, and let

\[
h={q\over\sum_{i=1}^{q}1/m_i}
\]

be their harmonic mean.

Then

\[
\boxed{
n\le h\le {1\over2^{j/q}-3}.}
\tag{4}
\]

If

\[
\lambda=j\log2-q\log3>0,
\]

then

\[
\boxed{
n<{q\over3\lambda}<{\alpha j\over3\lambda},
\qquad
\alpha={\log2\over\log3}.}
\tag{5}
\]

## 2. Every odd source is at least the initial value

For every proper time `t<j`, the exact affine formula has nonnegative remainder and coefficient at least one by `(1)`. Hence

\[
x_t\ge n.
\]

Every odd source `m_i` is one of these values, so

\[
m_i\ge n
\qquad(1\le i\le q).
\]

Therefore

\[
\boxed{h\ge n.}
\tag{6}
\]

## 3. Product identity

At an even source, the one-step ratio is `1/2`. At an odd source `m`, it is

\[
{3m+1\over2m}
={3\over2}\left(1+{1\over3m}\right).
\]

Multiplying all `j` step ratios gives

\[
\boxed{
{x_j\over n}
={3^q\over2^j}
\prod_{i=1}^{q}
\left(1+{1\over3m_i}\right).}
\tag{7}
\]

By `(3)`,

\[
{2^j\over3^q}
\le
\prod_{i=1}^{q}
\left(1+{1\over3m_i}\right).
\tag{8}
\]

The geometric mean on the right is at most its arithmetic mean:

\[
\left[
\prod_{i=1}^{q}
\left(1+{1\over3m_i}\right)
\right]^{1/q}
\le
1+{1\over3q}\sum_{i=1}^{q}{1\over m_i}
=
1+{1\over3h}.
\tag{9}
\]

Combining `(8)--(9)` gives

\[
2^{j/q}
\le
3+{1\over h},
\]

or

\[
h\le{1\over2^{j/q}-3}.
\]

Together with `(6)`, this proves `(4)`.

## 4. Logarithmic-gap form

Because

\[
2^{j/q}
=3e^{\lambda/q},
\]

one has

\[
{1\over2^{j/q}-3}
={1\over3(e^{\lambda/q}-1)}.
\]

The elementary strict inequality `e^x-1>x` for `x>0` gives

\[
{1\over3(e^{\lambda/q}-1)}
<{q\over3\lambda},
\]

proving `(5)`. ∎

## 5. Canonical first-crossing consequence

If the Box-2 target fails for a first-crossing word `w`, take

\[
n=r^+(w).
\]

Every proper prefix is automatically at least `n`, and the endpoint is at least `n` by the failure assumption. Thus

\[
\boxed{
r^+(w)\le H_{j,q}:={1\over2^{j/q}-3}.}
\tag{10}
\]

This is a deterministic height ceiling depending only on `(j,q)`, not on the internal order of the parity word.

## 6. Sharpened return gate

Whenever `T-6604` supplies a repeated factor of length `L` at two distinct physical states, equation `(11)` of that theorem gives

\[
2^L+1
\le3^B\left(n+{j\over2}\right).
\]

Using `(4)` yields the stronger exact necessary condition

\[
\boxed{
2^L+1
\le
3^B\left({1\over2^{j/q}-3}+{j\over2}\right).}
\tag{11}
\]

Thus a recurrence certificate may be checked without any generic Baker bound and without replacing the exact `(j,q)` geometry by `j/lambda`.

## 7. Gap audit

- The height ceiling becomes large when `q/j` is exceptionally close to `alpha`.
- It does not by itself control the canonical residue from below.
- The theorem assumes a first crossing and no descent at that crossing; it does not apply to later paradoxical resurfacings after an earlier descent.
- No CST or Collatz proof is claimed.
