# Exact two-channel value descent at a peeled cyclotomic order

Date: 2026-07-22

Status: **all-order theorem**, scratch-only.  The shared repository was not
edited.  This theorem completely reduces the *value* of `Q_u^(5)` modulo a
residual cyclotomic polynomial to one or two smaller residual values and a
central-binomial carry scalar.  It does not yet bound the higher
`Phi_m`-multiplicity required by prime-power peeling.

## 1. Statement

Let `m>=2`, let `zeta` be a primitive `m`-th root, and write

\[
 u=Am+r,\qquad 0\le r<m,\qquad
 \delta=\left\lfloor\frac{2r+1}{m}\right\rfloor\in\{0,1\}.
\]

Put `C_A=binom(2A,A)`.  Then the positive period-four quotient satisfies the
following exact identities in `Q(zeta)`.

If `delta=1`, then

\[
 \boxed{
 Q_{Am+r}^{(5)}(\zeta)
 =2^A(2A+1)C_A\,Q_r^{(5)}(\zeta).}                 \tag{1}
\]

If `delta=0`, then

\[
 \boxed{
 4Q_{Am+r}^{(5)}(\zeta)
 =2^AC_A\{A Q_{m+r}^{(5)}(\zeta)
             +4(1-A)Q_r^{(5)}(\zeta)\}.}           \tag{2}
\]

Equivalently, (1)--(2) are congruences in `Z[q]/(Phi_m(q))`.  Consequently
they may be reduced modulo every odd prime `p` not dividing `m`.  Since
`Phi_m` is squarefree in that characteristic, they give the exact full-factor
tests

\[
\begin{aligned}
 \delta=1:\quad
 \Phi_m\mid Q_{Am+r}^{(5)}\pmod p
 &\Longleftrightarrow
 p\mid (2A+1)C_A\quad\hbox{or}\quad
 \Phi_m\mid Q_r^{(5)}\pmod p,                         \tag{3}\\
 \delta=0:\quad
 \Phi_m\mid Q_{Am+r}^{(5)}\pmod p
 &\Longleftrightarrow
 p\mid C_A\quad\hbox{or}\quad
 \Phi_m\mid
   \{A Q_{m+r}^{(5)}+4(1-A)Q_r^{(5)}\}\pmod p.       \tag{4}
\end{aligned}
\]

Thus this is a descent in the precise sense needed after peeling: the
unbounded index `u` disappears from the residual polynomial state.  What
remains is `r`, one lower/upper channel bit `delta`, and `A mod p`, together
with a base-`p` carry flag.

By Kummer's theorem,

* `p|C_A` exactly when the base-`p` addition `A+A` has a carry;
* `p|(2A+1)C_A` exactly when the three-summand addition `A+A+1`
  has a carry.

The second assertion is the multinomial form of Kummer, since
`(2A+1)C_A=(2A+1)!/(A!A!1!)`.

## 2. The zero-order blocks

Use the exact two-level decomposition

\[
 Q_u^{(5)}=\sum_{b=0}^uD_{u,b}F_{u-b,b},             \tag{5}
\]

\[
 D_{u,b}=\frac{(q;q)_{2u+1}(q;q)_b^2}
 {(q;q)_u(q;q)_{u-b}(q;q)_{2b+1}},
\quad
 F_{N,b}=\sum_{c=0}^Nq^{(b+c)(b+c+1)+b(b+1)}
 {N\brack c}_q.                                      \tag{6}
\]

Write `b=Bm+t`, `0<=t<m`, and put

\[
 e={\bf1}_{t>r},\qquad
 f=\left\lfloor\frac{2t+1}{m}\right\rfloor.
\]

The ordinary `Phi_m`-order of the factorial block is

\[
 v_m(D_{u,b})=B+\delta+e-f.                         \tag{7}
\]

Although (7) appears to allow `B=1`, equality to zero there would require
simultaneously `delta=e=0` and `f=1`.  This is impossible: `delta=0` and
`e=0` give `t<=r<(m-1)/2`, whereas `f=1` requires
`t>=(m-1)/2`.  Hence every nonzero block value has `B=0`, and its residual
index satisfies exactly

\[
 \delta+e=f.                                         \tag{8}
\]

This observation is what collapses an arbitrarily long sum to two finite
channels.

## 3. Exact evaluation of a surviving block

For `0<=s<m`, abbreviate

\[
 P_s=(\zeta;\zeta)_s.
\]

For `n=am+s`, remove the `a` factors whose exponents are multiples of `m`.
The remaining factors have value

\[
 \prod_{\substack{1\le j\le n\\m\nmid j}}(1-\zeta^j)
 =m^aP_s,                                            \tag{9}
\]

because `prod_(i=1)^(m-1)(1-zeta^i)=m`.  In a ratio of zero total
`Phi_m`-order, the powers of `m` cancel, while

\[
 \lim_{X\to1}\frac{(X;X)_a}{(1-X)^a}=a!.           \tag{10}
\]

Let

\[
 s=2r+1-\delta m,\quad R=r-t+em,\quad h=2t+1-fm,
\]

and

\[
 K_{r,t}=\frac{P_sP_t^2}{P_rP_RP_h}.                \tag{11}
\]

Equations (9)--(10) give, whenever (8) holds,

\[
 D_{u,t}(\zeta)=K_{r,t}
 \frac{(2A+\delta)!}{A!(A-e)!f!}.                  \tag{12}
\]

Exact root-of-unity q-Lucas gives

\[
 F_{u-t,t}(\zeta)=2^{A-e}F_{R,t}(\zeta).           \tag{13}
\]

All denominators in (11) are nonzero.  Equations (12)--(13) therefore hold
algebraically, not merely analytically.

## 4. Summing the two channels

If `delta=1`, condition (8) forces `e=0,f=1` and

\[
 \left\lceil\frac{m-1}{2}\right\rceil\le t\le r.
\]

The factorial ratio in (12) is `(2A+1)C_A`, and (13) contributes `2^A`.
The residual sum is exactly the block decomposition of `Q_r(\zeta)`; all
other blocks in that decomposition vanish at `zeta`.  This proves (1).

If `delta=0`, (8) gives two channels:

* `0<=t<=r`, where `e=f=0`; its total is `2^AC_A Q_r(\zeta)`;
* `ceil((m-1)/2)<=t<m`, where `e=f=1`; its total is
  `2^(A-1) A C_A E_(m,r)(\zeta)` for a residual sum independent of `A`.

At `A=1` the same identity reads

\[
 Q_{m+r}(\zeta)=4Q_r(\zeta)+2E_{m,r}(\zeta).        \tag{14}
\]

Eliminating `E_(m,r)` proves (2).  The formulas at `A=0` are interpreted
directly; the high channel is absent and its displayed factor `A` is zero.

## 5. Consequence for a putative composite cyclotomic zero

Let `L=mp^k`, where `p` is odd and `p` does not divide `m`.  If
`Phi_L|Q_u^(5)` in `Z[q]`, prime-power peeling gives

\[
 \operatorname{mult}_{\Phi_m}(Q_u^{(5)}\bmod p)
 \ge\varphi(p^k).                                    \tag{15}
\]

In particular the multiplicity is positive, so (3)--(4) give an explicit
necessary alternative:

* a quotient-digit carry (`A+A+delta`), or
* one finite residual full-factor relation.

This is substantially sharper than merely evaluating at one primitive
component over an algebraic closure: (3)--(4) concern divisibility by the
entire polynomial `Phi_m` over `F_p`.

The generalized distinguished-block lemma supplies, under
`mp^k>2u+1`, a carry-only block order `V_*` with

\[
 2V_*+1<\varphi(p^k).                               \tag{16}
\]

Together, (3)--(4) and (16) isolate the still-open step exactly: control
cancellation of the first `2V_*+1` local jets after one of the value
alternatives occurs.  A value descent alone cannot claim the multiplicity
deficit in (15).

The known complementary residual zeros occur in the distinguished channel
only at

\[
 m\equiv0\pmod4,\qquad r=m/2-1\ \hbox{or}\ r=m-1.  \tag{17}
\]

These are precisely the two residues aligned with the proved dyadic boundary
families.  Finite-field reduction can increase their local multiplicity, so
the characteristic-zero simplicity theorem must not be substituted for the
missing jet bound.

## 6. Exact audit

`experiments/X-9876-period-four-quotient-audits/check_composite_value_descent.js`
verifies with exact `BigInt`
polynomial arithmetic:

1. (1)--(2) modulo `Phi_m` for all `2<=m<=10`, all residuals, and
   `0<=A<=3` (216 identities);
2. independent reductions for `p=3,5,7,11`, `p` not dividing `m`
   (704 identities); and
3. the multinomial carry test through `A=1000` for five odd primes.

In the separate exact peeling census through `u<=18`, `L<=500`, the
zero-order test alone excludes 4,960 of 5,147 cutoff candidates.  Full
multiplicity peeling excludes 5,134; the remaining 13 are all pure dyadic
and have separate folded-residue certificates.  This census is supporting
evidence only; formulas (1)--(4) are proved for every index.


