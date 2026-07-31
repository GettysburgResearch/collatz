# Q-6802 — Canonical-displacement closure after the support correction

**Claim ID:** `Q-6802`  
**Status:** **OPEN**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Last updated:** 2026-08-01

## 1. Canonical variables

For a parity word `w` of length `j` and weight `q`, let

\[
2^j s_w=3^q r_w+A_w
\]

be its canonical source--endpoint pair.  If `2^j>3^q`, then

\[
A_w=(2^j-3^q)r_w+2^j(s_w-r_w)
\]

and therefore

\[
\boxed{
r_w>{A_w\over2^j-3^q}
\iff
s_w-r_w<0.}
\]

The source residue and the real no-descent threshold differ by one exact
integer displacement.

## 2. The two exhaustive targets

### SC*

\[
\boxed{
m_N^{\rm sup}
=
\min_{w\in\mathcal W_N^{\rm sup}}r_w
\longrightarrow\infty.}
\]

### FC*

Apart from the trivial word `10`, prove that no complete first-crossing tuple
has

\[
\boxed{d=s_w-r_w\ge0.}
\]

`L-6814` proves that every nontrivial positive cycle, rotated to its minimum
and stopped at its first coefficient crossing, produces a canonical FC
failure. Thus FC* includes the cycle level and

\[
\boxed{\mathrm{SC}^*+\mathrm{FC}^*\Longrightarrow\text{Collatz}.}
\]

No third cycle premise is required.

## 3. Coordinate-safe full-denominator equation

For a canonical near-return

\[
T^j(r)=s=r+d,
\qquad
D=2^j-3^q,
\]

`L-6812` gives

\[
\boxed{
A_w=Dr+2^jd=Ds+3^qd,}
\]

with

\[
\boxed{0\le d<A_w/2^j<q/3<j/3.}
\]

Hence

```text
source   = (A_w-2^j d)/D;
endpoint = (A_w-3^q d)/D.
```

The complete local congruence may be written `A_w == 3^q d`, but the source
quotient must use `2^j d`.

## 4. Previous unified envelope

Let

\[
F_j
={A_{\rm mech}(j)\over2^j-3^{q(j)}}
\]

be the exact upper-mechanical first-crossing threshold.  `L-6813` proves that
any canonical failure satisfies

\[
\boxed{
m_{j-1}^{\rm sup}
\le r^+(w)
\le{A_w\over2^j-3^q}
\le F_j.}
\]

Thus the cofinal inequality

\[
m_{j-1}^{\rm sup}>F_j
\]

would close both SC* and FC*.

## 5. New support-corrected envelope

For a nonmechanical word `v`, let `R(v)` be the number of odd positions
displaced from the upper-mechanical word and put

\[
C_j={3^q\over2^j}.
\]

`L-6816` proves the uniform normalized-remainder loss

\[
\boxed{
E_{\rm mech}-E_v>{C_j\over12}R(v).}
\]

Therefore every canonical non-descent satisfies

\[
\boxed{
 r_v
 <
 F_j-{C_jR(v)\over12(1-C_j)}.}
\tag{1}
\]

Define

\[
L_j(R)=\left\lfloor{j-2\over2(R+1)}\right\rfloor
\]

and let `rho_j` be the least nonnegative integer `R` such that either
`L_j(R)=0` or

\[
2^{L_j(R)}+1
<
3^{R+1}
\left({q\over3\lambda_j}+{q\over3}\right),
\qquad
\lambda_j=j\log2-q\log3.
\]

`T-6812` proves that every internally injective nonmechanical failure has

\[
R(v)\ge rho_j.
\]

Put

\[
\boxed{
H_j^{\rm supp}
=
F_j-{C_jrho_j\over12(1-C_j)}.}
\tag{2}
\]

Then every internally injective nonmechanical failure has source below
`H_j^supp`.

Repeated proper states reduce to a nontrivial positive cycle.  A least-period
cycle, rotated to its minimum and stopped at its first coefficient crossing,
is internally injective on its proper states.  Thus, after a finite initial
audit and the source-qualified mechanical theorem, the cofinal inequality

\[
\boxed{m_{j-1}^{\rm sup}\ge H_j^{\rm supp}}
\tag{E_supp}
\]

closes FC* in full.

The explicit scalar form is

\[
\boxed{
m_{j-1}^{\rm sup}
\ge
{q/3-C_jrho_j/12\over1-C_j}.}
\tag{G_supp}
\]

Both are strictly weaker than the prior envelope targets.

## 6. Why the corrected envelope still closes SC*

Every upper-mechanical odd contribution is greater than `C_j/6`, so

\[
F_j>{C_jq\over6(1-C_j)}.
\]

Also

\[
rho_j\le\lfloor(j-2)/2\rfloor.
\]

Hence

\[
H_j^{\rm supp}
>
{C_j(2q-rho_j)\over12(1-C_j)}.
\]

At valid crossings, `q>alpha(j-1)` with `alpha=log2/log3`, and
`2alpha-1/2>0`. Along the lower convergents,

\[
C_j\to1^-,
\qquad
1-C_j\to0^+.
\]

Therefore

\[
H_j^{\rm supp}\to+\infty
\]

along that subsequence.  A cofinal proof of `(E_supp)` makes the monotone
least-source sequence unbounded and proves SC*.

## 7. Updated fixed-source equivalence

The updated base branch contains `T-6710`:

\[
\boxed{
m_N>B
\iff
\tau_c(n)\le N
\text{ for every }1\le n\le B.}
\]

Thus SC* is exactly universal finite coefficient stopping.

Define

\[
B_j^{\rm supp}
=
\lceil H_j^{\rm supp}\rceil-1.
\]

Then `(E_supp)` is equivalent to the moving finite box

\[
\boxed{
\tau_c(n)\le j-1
\quad
\text{for every }1\le n\le B_j^{\rm supp}.}
\tag{M_supp}
\]

In fixed-source valuation form, source `n` realizes an all-supercritical word
`w` of length `N` only if

\[
v_2(3^{q(w)}n+A_w)\ge N.
\]

The exact source theorem still missing is a source-dependent finite upper
bound on this valuation.

## 8. Complete-prime-power target

Factor

\[
D=2^j-3^q=\prod_sQ_s,
\qquad
h_s=\operatorname{ord}_{Q_s}(2).
\]

`L-6809` proves that one exact first-crossing non-descent is equivalent to:

```text
compatible local excess paths modulo every h_s;
the unique monotone physical lift in the full-order window;
every proper first-crossing coefficient inequality;
one common 0<=d<q/3;
every complete prime-power equation A == 3^q d;
the canonical source (A-2^j d)/D.
```

An order-cover may decode a word but does not certify omitted prime powers.
A proper-factor hit is not an FC tuple.

## 9. What is already closed in the acyclic FC sector

Subject to the stated source dependencies:

```text
upper-mechanical words;
no-wrap nonmechanical words;
bounded-bank / low-complexity families;
sub-sqrt(j)-support repair families;
one-pulse near-return families in PR #83's scope.
```

The remaining acyclic language is polynomially sparse across candidate words,
but every member is square-root-supported, two-thirds-scale displaced,
wrapped, and early-departing at both boundaries.

## 10. Smallest exact blocker

Neither `(E_supp)`, `(G_supp)`, `(M_supp)`, SC*, nor FC* is proved.

The present smallest exact blocker is the cofinal moving source box

\[
\boxed{
\tau_c(n)\le j-1
\quad
(1\le n\le\lceil H_j^{\rm supp}\rceil-1),}
\]

or equivalently the fixed-source valuation bound, or the complete-denominator
emptiness theorem with one common `d<q/3`.

Endpoint divergence, family sparsity, high internal factor complexity,
proper-factor divisibility, and compatible free completion do not prove this
source-coordinate statement.

## 11. Review boundary

This file records a strictly improved sufficient theorem, not a completed
proof.  The support loss is elementary; the all-length mechanical theorem and
full-order compiler retain their declared source qualifications.
