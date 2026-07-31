# T-6812 — A support-corrected cofinal envelope still closes both coefficient lanes

**Claim ID:** `T-6812`  
**Status:** **PROPOSED / SOURCE-QUALIFIED ONLY AT THE MECHANICAL ALL-LENGTH INPUT**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-08-01  
**Dependencies:** `L-6811`, `L-6814`, `L-6815`, `L-6816`; `T-6806` for the all-length mechanical sector  
**Scope:** the unified SC* / FC* coefficient program  
**Counterexample status:** none

## 1. Exact return-forced support threshold

Fix a valid first-crossing length `j`, with unique weight `q`, and put

\[
C_j={3^q\over2^j},
\qquad
\lambda_j=j\log2-q\log3>0.
\tag{1}
\]

For an integer `R>=0`, define

\[
L_j(R)
=
\left\lfloor
{j-2\over2(R+1)}
\right\rfloor.
\tag{2}
\]

Let `rho_j` be the least nonnegative integer `R` satisfying at least one of

\[
L_j(R)=0,
\tag{3}
\]

or

\[
\boxed{
2^{L_j(R)}+1
<
3^{R+1}
\left(
{q\over3\lambda_j}+{q\over3}
\right).}
\tag{4}
\]

The set is nonempty because `(3)` holds once

\[
R>{j-4\over2}.
\]

In particular,

\[
\boxed{
rho_j\le\left\lfloor{j-2\over2}\right\rfloor.}
\tag{5}
\]

The definition is exact and source-free.  For a concrete `j`, a directed
lower bound on `lambda_j` gives a proof-producing integer value of `rho_j`.
The left side of `(4)` is nonincreasing in `R`, while the right side is
increasing, so the admissible set is an upper interval.

## 2. Every internally injective failure has support at least `rho_j`

Let `v` be a nonmechanical canonical first-crossing failure of length `j` and
let

\[
R=R(v)
\]

be its displaced support relative to the upper-mechanical word.
Assume its proper physical states

\[
r_v,T(r_v),\ldots,T^{j-1}(r_v)
\]

are pairwise distinct.

If `L_j(R)=0`, then `R` satisfies `(3)`.  Otherwise `L-6811` forces a repeated
parity factor of length `L_j(R)`.  The two physical starts are distinct by
hypothesis.  `L-6815` therefore gives

\[
2^{L_j(R)}+1
<
3^{B(v)}
\left(
{q\over3\lambda_j}+{q\over3}
\right).
\tag{6}
\]

`L-6808` gives

\[
B(v)<R+1.
\]

Substitution in `(6)` proves `(4)`.  Hence every internally injective failure
satisfies

\[
\boxed{R(v)\ge rho_j.}
\tag{7}
\]

This section imports no generic Rhin or Baker exponent.  The logarithmic gap
appears in its exact word-specific value.

## 3. The support-corrected exact envelope

Let

\[
F_j
={A_{\rm mech}(j)\over2^j-3^q}
={E_{\rm mech}(j)\over1-C_j}
\tag{8}
\]

be the exact upper-mechanical threshold and define

\[
\boxed{
H_j^{\rm supp}
=
F_j
-
{C_j\,rho_j\over12(1-C_j)}.}
\tag{9}
\]

`L-6816` and `(7)` prove that every internally injective nonmechanical
canonical failure has source

\[
\boxed{r_v<H_j^{\rm supp}.}
\tag{10}
\]

Consequently the strictly weaker source inequality

\[
\boxed{
m_{j-1}^{\rm sup}\ge H_j^{\rm supp}}
\tag{11}
\]

excludes every internally injective nonmechanical canonical failure at length
`j`.

Compare `(11)` with the previous target

\[
m_{j-1}^{\rm sup}>F_j.
\]

The new threshold is lower by the explicit positive amount

\[
{C_j\,rho_j\over12(1-C_j)}.
\]

## 4. Fully explicit scalar version

The one-third remainder theorem gives

\[
E_{\rm mech}(j)<{q\over3}.
\]

Define

\[
\boxed{
G_j^{\rm supp}
=
{q/3-C_jrho_j/12\over1-C_j}.}
\tag{12}
\]

Every internally injective nonmechanical canonical failure satisfies

\[
r_v<G_j^{\rm supp}.
\tag{13}
\]

Thus the scalar condition

\[
\boxed{
m_{j-1}^{\rm sup}\ge G_j^{\rm supp}}
\tag{14}
\]

is sufficient at length `j`.  It improves the previous scalar target

\[
{q\over3(1-C_j)}
=
{q2^j\over3(2^j-3^q)}
\]

by the same forced-support correction.

## 5. Positive cycles reduce to the internally injective case

Suppose any nontrivial positive cycle exists.  Choose one of least period,
rotate it to its minimum state, and stop at its first coefficient crossing.
`L-6814` gives a canonical first-crossing failure.

Its proper states are pairwise distinct: a repeated state before the end of
the minimal period would produce a shorter positive period.  Hence the
resulting canonical failure is internally injective and is subject to
Sections 2--4.

If a general canonical failure contains a repeated proper physical state,
it contains a nontrivial positive cycle.  Replacing it by a least-period cycle
therefore again produces an internally injective canonical failure, possibly
at a shorter first-crossing length.

Thus, after a finite initial-length audit, it suffices globally to exclude the
internally injective failures controlled by `(11)` or `(14)`.  The cycle level
`d=0` is not discarded; it is reduced to the same support-corrected language.

## 6. Cofinal closure theorem

Assume there is `J` such that:

1. every nontrivial first-crossing failure of length below `J` has been
   excluded by proof-grade finite or symbolic certificates;
2. the source-qualified all-length mechanical closure `T-6806` holds; and
3. for every valid first-crossing length `j>=J`,
   \[
   \boxed{m_{j-1}^{\rm sup}\ge H_j^{\rm supp}}
   \tag{15}
   \]
   or, more strongly but more explicitly, `(14)` holds.

Then FC* is empty apart from the trivial word `10`.

Indeed, any nontrivial failure reduces by Section 5 to an internally injective
one.  `T-6806` removes the mechanical case, and `(10)` contradicts `(15)` in
the nonmechanical case.

The same cofinal hypothesis also proves SC*.  To see this, first note that
every mechanical odd contribution is greater than `C_j/6`, so

\[
F_j>{C_jq\over6(1-C_j)}.
\tag{16}
\]

Using `(5)`,

\[
H_j^{\rm supp}
>
{C_j(2q-rho_j)\over12(1-C_j)}
\ge
{C_j\left(2q-\lfloor(j-2)/2\rfloor\right)
 \over12(1-C_j)}.
\tag{17}
\]

At valid crossings,

\[
q>\alpha(j-1),
\qquad
\alpha={\log2\over\log3},
\]

and `2alpha-1/2>0`.  Along the infinitely many valid lower convergents,

\[
C_j\to1^-,
\qquad
1-C_j\to0^+.
\]

Equation `(17)` therefore gives

\[
\boxed{H_j^{\rm supp}\to+\infty}
\tag{18}
\]

along that subsequence.  Condition `(15)` makes the monotone least-source
sequence unbounded, hence

\[
\boxed{m_N^{\rm sup}\to+\infty.}
\]

Therefore the cofinal support-corrected inequality closes both exhaustive
coefficient lanes and proves Collatz, subject to the explicitly listed source
and finite inputs.

No such cofinal source lower bound is proved in this file.

## 7. Exact finite inverse form

`T-6710` on the updated base branch proves

\[
m_N>B
\iff
\tau_c(n)\le N
\quad\text{for every }1\le n\le B.
\]

Put

\[
B_j^{\rm supp}
=
\left\lceil H_j^{\rm supp}\right\rceil-1.
\tag{19}
\]

Then `(15)` is equivalent to the moving finite statement

\[
\boxed{
\tau_c(n)\le j-1
\quad
\text{for every }1\le n\le B_j^{\rm supp}.}
\tag{20}
\]

Thus the smallest exact remaining source obligation after the support loss is
not the old full mechanical envelope.  It is the moving coefficient-stopping
box `(20)`, or its fixed-source valuation equivalent

\[
v_2(3^{q(w)}n+A_w)<|w|
\]

for every `n` in that box and every sufficiently long all-supercritical word
realized from `n`.

## 8. What has and has not been achieved

The theorem gives a strictly weaker sufficient condition than the requested
cofinal inequality:

\[
F_j
\quad\rightsquigarrow\quad
F_j-{C_jrho_j\over12(1-C_j)}.
\]

The reduction uses the complete ordinary support/return geometry; it is not a
new encoding or a finite-prefix amplifier.

It does **not** prove the new inequality.  Existing endpoint-growth, family-
sparsity, and complete-prime-power constraints do not yet yield the fixed-
source valuation bound `(20)`.

## 9. Audit targets

1. Verify the mechanical contribution corridor `1/6 < 2^(e_i)/3^i <= 1/3`.
2. Check the strict support loss `C R/12`.
3. Reconstruct `rho_j` directly from `L-6811/L-6815` without importing a
   generic logarithmic-form exponent.
4. Check primitive-cycle reduction and the distinction between proper-state
   repetition and endpoint return.
5. Preserve the source quotient `(A-2^j d)/D` and endpoint quotient
   `(A-3^q d)/D`.
6. Verify unboundedness of the corrected envelope along lower convergents.
7. Do not promote `(15)` or `(20)` to a theorem until the fixed-source
   coefficient-stopping bound is supplied.
