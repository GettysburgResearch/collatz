# T-6905 — every first-crossing threshold lies below one explicit scalar envelope

**Claim ID:** `T-6905`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #75  
**Dependencies:** `L-6904`, `L-6905`; elementary affine remainder algebra  
**Scope:** every valid first-coefficient-crossing length

## Statement

Put

\[
\alpha=\frac{\log2}{\log3}.
\]

For a length `j` admitting a first coefficient crossing, let

\[
q=q(j)=\lfloor\alpha j\rfloor=\lceil\alpha(j-1)\rceil,
\]

and put

\[
D_j=2^j-3^q>0.
\]

Define the explicit rational envelope

\[
\boxed{
G_j=\frac{q\,2^{j-1}}{D_j}.}
\tag{1}
\]

Then every first-crossing word `w` of length `j` satisfies

\[
\boxed{
\frac{A_w}{D_j}<G_j.}
\tag{2}
\]

Consequently,

\[
\boxed{m_{j-1}^{\rm sup}>G_j}
\tag{3}
\]

forces canonical descent for every first-crossing word of length `j`.

If `(3)` holds for every sufficiently late valid crossing length, then after a finite small-length audit both final coefficient obligations are closed:

```text
m_N^sup -> infinity;
every finite first coefficient crossing descends.
```

## Proof of the scalar envelope

Let

\[
T_w(x)=\frac{3^q x+A_w}{2^j}
      =C_jx+E_w,
\qquad
C_j=\frac{3^q}{2^j}.
\]

Write

\[
D_{w,m}=q_m(w)-\alpha m.
\]

The exact normalized affine remainder is

\[
\boxed{
E_w
=\frac12\sum_{m=1}^j
v_{m-1}\,3^{D_{w,j}-D_{w,m}}.}
\tag{4}
\]

Indeed, the odd contribution born at shortcut time `m-1` is

\[
\frac{3^{q-q_m}2^{m-1}}{2^j}
=\frac12\,3^{q-q_m+\alpha(m-j)}
=\frac12\,3^{D_{w,j}-D_{w,m}}.
\]

At a first crossing,

\[
D_{w,j}<0,
\qquad
D_{w,m}\ge0\quad(m<j),
\]

and the final bit is even. Hence every nonzero term in `(4)` is strictly below `1/2`. There are exactly `q` such terms, so

\[
\boxed{E_w<\frac q2.}
\tag{5}
\]

Since

\[
1-C_j=\frac{D_j}{2^j},
\]

we obtain

\[
\frac{A_w}{D_j}
=\frac{E_w}{1-C_j}
<\frac{q/2}{D_j/2^j}
=G_j,
\]

proving `(2)`.

If a canonical word fails descent, `L-6905` gives

\[
m_{j-1}^{\rm sup}\le r^+(w)\le\frac{A_w}{D_j}<G_j.
\]

This contradicts `(3)`, so every canonical root descends. `L-6904` then makes every positive lift descend as well. ∎

## The envelope is cofinally unbounded

Along the infinitely many lower continued-fraction convergents `q/j` to `alpha` that are valid first-crossing pairs,

\[
\lambda_j=j\log2-q\log3\longrightarrow0^+.
\]

Because

\[
\frac{D_j}{2^j}=1-e^{-\lambda_j},
\]

formula `(1)` becomes

\[
G_j=\frac{q}{2(1-e^{-\lambda_j})}
\longrightarrow\infty.
\tag{6}
\]

Thus `(3)` on all sufficiently late valid lengths forces an unbounded subsequence of the monotone sequence `m_N^sup`, and hence

\[
m_N^{\rm sup}\to\infty.
\]

## Polynomial reduction from logarithmic forms

Suppose an effective two-logarithm theorem gives

\[
\lambda_j\ge c_0j^{-\mu}
\tag{7}
\]

for every valid pair, with fixed effective constants `c_0,mu>0`.

First crossing gives `0<lambda_j<log2`, and therefore

\[
1-e^{-\lambda_j}\ge\frac{\lambda_j}{2}.
\]

Using `q<j`,

\[
\boxed{
G_j
\le\frac q{\lambda_j}
<c_0^{-1}j^{\mu+1}.}
\tag{8}
\]

Hence the explicit source-dependent theorem

\[
\boxed{
 m_N^{\rm sup}
 >c_0^{-1}(N+1)^{\mu+1}
 \quad\text{for all sufficiently large }N}
\tag{9}
\]

would imply Collatz after the finite small-length and no-cycle checks inherited by the coefficient program.

Equivalently, any effective irrationality measure `nu` for `alpha=log2/log3` converts the final ordinary-extraction target into escape beyond a concrete polynomial of degree `nu`.

## Strategic meaning

`L-6905` reduced the two final boxes to `m_(j-1)^sup>F_j`, where `F_j` was a maximum over all first-crossing words. `T-6905` removes that maximization:

```text
prove the least supercritical root exceeds G_j,
where G_j is one explicit rational number determined only by j.
```

This is not yet a proof, but it turns the global blocker into a direct comparison between two exact scalar sequences.

## Gap audit

- The current repository has no polynomial lower bound for `m_N^sup`.
- The Baker/Matveev constants and exponent must be fixed from a reviewed source before using `(8)--(9)` quantitatively.
- The scalar envelope is intentionally coarse; the mechanical extremizer and ballot constraints can lower it.
- A fixed verification floor cannot dominate `G_j` because `(6)` is unbounded.
