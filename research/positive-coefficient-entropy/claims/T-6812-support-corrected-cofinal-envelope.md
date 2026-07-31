# T-6812 — A support-corrected cofinal envelope still closes both coefficient lanes

**Claim ID:** `T-6812`  
**Status:** **PROPOSED / SOURCE-QUALIFIED ONLY AT THE MECHANICAL ALL-LENGTH INPUT**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-08-01  
**Dependencies:** `L-6808`, `L-6811`, `L-6815`, `L-6816`, `L-6817`; `T-6806` for the all-length mechanical sector; cross-branch `T-6710` only for the inverse formulation  
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
\left\lfloor{j-2\over2(R+1)}\right\rfloor.
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
\left({q\over3\lambda_j}+{q\over3}\right).}
\tag{4}
\]

The set is nonempty, because `(3)` holds once `R>(j-4)/2`.  In particular,

\[
\boxed{
rho_j\le\left\lfloor{j-2\over2}\right\rfloor.}
\tag{5}
\]

The definition is exact and source-free.  The left side of `(4)` is
nonincreasing in `R`, while the right side is increasing, so the admissible
set is an upper interval.  For one concrete `j`, a directed lower bound for
`lambda_j` evaluates `rho_j` proof-gradely.

## 2. Every internally injective failure has support at least `rho_j`

Let `v` be a nonmechanical canonical first-crossing failure of length `j` and
let

\[
R=R(v)
\]

be its displaced support relative to the upper-mechanical word.  Assume the
proper physical states

\[
r_v,T(r_v),\ldots,T^{j-1}(r_v)
\]

are pairwise distinct.

If `L_j(R)=0`, then `R` satisfies `(3)`.  Otherwise `L-6811` supplies a
repeated parity factor of length `L_j(R)`.  Its physical starts are distinct,
so `L-6815` gives

\[
2^{L_j(R)}+1
<
3^{B(v)}
\left({q\over3\lambda_j}+{q\over3}\right).
\tag{6}
\]

`L-6808` gives `B(v)<R+1`, and therefore `(4)` holds.  Thus

\[
\boxed{R(v)\ge rho_j.}
\tag{7}
\]

No generic Rhin or Baker exponent enters this section.

## 3. Pointwise support-corrected envelope

Let

\[
F_j
={A_{\rm mech}(j)\over2^j-3^q}
={E_{\rm mech}(j)\over1-C_j}
\tag{8}
\]

be the exact mechanical threshold and define

\[
\boxed{
H_j^{\rm supp}
=
F_j-{C_jrho_j\over12(1-C_j)}.}
\tag{9}
\]

`L-6816` proves for every nonmechanical canonical non-descent

\[
r_v
<
F_j-{C_jR(v)\over12(1-C_j)}.
\tag{10}
\]

Combining `(7)` and `(10)`,

\[
\boxed{r_v<H_j^{\rm supp}.}
\tag{11}
\]

Consequently

\[
\boxed{m_{j-1}^{\rm sup}\ge H_j^{\rm supp}}
\tag{12}
\]

excludes every internally injective nonmechanical canonical failure at length
`j`.

This is strictly weaker than the preceding target

\[
m_{j-1}^{\rm sup}>F_j.
\]

## 4. Explicit scalar version

The one-third remainder theorem gives

\[
E_{\rm mech}(j)<{q\over3}.
\]

Define

\[
\boxed{
G_j^{\rm supp}
={q/3-C_jrho_j/12\over1-C_j}.}
\tag{13}
\]

Every internally injective nonmechanical failure satisfies

\[
r_v<G_j^{\rm supp}.
\tag{14}
\]

Hence the explicit condition

\[
\boxed{m_{j-1}^{\rm sup}\ge G_j^{\rm supp}}
\tag{15}
\]

is sufficient at length `j`.  It improves

\[
{q\over3(1-C_j)}
={q2^j\over3(2^j-3^q)}
\]

by the forced-support correction.

## 5. Why the cycle branch is included

`L-6817` proves that any canonical FC obstruction with a repeated proper
physical state yields a nontrivial positive cycle, and that a least-period
cycle, rotated to its minimum and stopped at its first coefficient crossing,
has pairwise distinct proper states and is itself a canonical FC obstruction.

Thus every nontrivial FC obstruction reduces to an internally injective one,
possibly at a shorter first-crossing length.  For such an injective witness,
the equal-state alternative in the proof of `T-6806` is unavailable.  Subject
to `T-6806`'s finite and logarithmic-form inputs, an injective mechanical
witness descends.

Therefore every surviving nontrivial FC obstruction may be chosen

```text
internally injective;
nonmechanical;
and subject to (7)--(12).
```

The cycle level `d=0` is retained, not assumed away.

## 6. Cofinal closure theorem

Assume there is `J` such that:

1. every nontrivial first-crossing failure below `J` is excluded by
   proof-grade finite or symbolic certificates;
2. the all-length mechanical input `T-6806` holds; and
3. for every valid first-crossing length `j>=J`, `(12)` holds—or the stronger
   explicit condition `(15)` holds.

Then FC* is empty apart from the trivial word `10`: any nontrivial witness
reduces by Section 5 to an internally injective nonmechanical one, while
`m_(j-1)^sup<=r_v` contradicts `(11)--(12)`.

The same cofinal hypothesis proves SC*.  Every mechanical odd contribution is
greater than `C_j/6`, so

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

Hence

\[
\boxed{H_j^{\rm supp}\to+\infty}
\tag{18}
\]

along that subsequence.  Condition `(12)` makes the monotone sequence
`m_N^sup` unbounded and therefore forces

\[
\boxed{m_N^{\rm sup}\to+\infty.}
\]

Thus the support-corrected cofinal inequality closes both exhaustive
coefficient lanes and proves Collatz, subject to the listed finite and source
inputs.

**The cofinal inequality itself is not proved here.**

## 7. Exact finite inverse form

Cross-branch `T-6710` proves

\[
m_N>B
\iff
\tau_c(n)\le N
\quad(1\le n\le B).
\]

Put

\[
\boxed{
B_j^{\rm supp}
=
\max\left\{0,
\left\lceil H_j^{\rm supp}\right\rceil-1
\right\}.}
\tag{19}
\]

For the cofinal range where `H_j^supp>1`, condition `(12)` is equivalent to

\[
\boxed{
\tau_c(n)\le j-1
\quad
\text{for every }1\le n\le B_j^{\rm supp}.}
\tag{20}
\]

Equivalently, one needs a source-dependent finite upper bound on

\[
v_2(3^{q(w)}n+A_w)
\]

as `w` ranges over all-supercritical words realized from one fixed source
`n`.

The moving box `(20)` is the smallest exact source obligation reached by this
pass.

## 8. What changed and what remains

The theorem replaces the requested envelope by a strictly lower one:

\[
F_j
\quad\rightsquigarrow\quad
F_j-{C_jrho_j\over12(1-C_j)}.
\]

The subtraction comes from the same internal support forced by exact ordinary
returns; it is not a new encoding, average-case estimate, or finite-prefix
amplifier.

Existing endpoint growth, family sparsity, and complete-prime-power
reconstruction do not prove `(20)`.  The unresolved fixed-source valuation
bound is therefore retained explicitly.

## 9. Audit targets

1. Verify `1/6 < 2^(e_i)/3^i <= 1/3` and the strict `C_jR/12` loss.
2. Reconstruct `rho_j` from `L-6811/L-6815` without a generic logarithmic
   exponent.
3. Verify the least-period cycle reduction and proper-state injectivity.
4. Preserve source `(A-2^jd)/D` versus endpoint `(A-3^qd)/D`.
5. Verify `(17)--(18)` along lower convergents.
6. Do not promote `(12)`, `(15)`, or `(20)` without the fixed-source bound.
