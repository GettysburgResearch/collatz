# Session report — support-corrected cofinal envelope attack

**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Draft PR:** #81  
**Date:** 2026-08-01

## Requested objective

Attack the full sufficient theorem

\[
m_{j-1}^{\rm sup}
>
F_j
=
{A_{\rm mech}(j)\over2^j-3^{q(j)}}
\]

or the scalar envelope

\[
m_{j-1}^{\rm sup}
>
{q(j)2^j\over3(2^j-3^{q(j)})},
\]

using the corrected current state of PR #81, PR #83, the coefficient-stopping
base branch, and the complete-denominator compiler.  Computation was permitted
only to discover or falsify lemmas; every promoted statement had to be
symbolic.

## Synchronization audit

The pass synchronized against:

```text
PR #81 LATEST.md;
PR #81 Q-6802;
PR #81 head and comments;
PR #83 LATEST.md, head, and correction comments;
issue #75 collaborator comments;
updated PR #77-base claims T-6710 and L-6711.
```

No `CURRENT_STATE.md` existed at the searched root or active research paths.
This pass creates

```text
research/positive-coefficient-entropy/CURRENT_STATE.md
```

as the durable corrected snapshot.

The source/endpoint convention was kept fixed throughout:

\[
A=Dr+2^jd=Ds+3^qd,
\qquad s=r+d.
\]

Thus `(A-2^j d)/D` is the source and `(A-3^q d)/D` is the endpoint.

## Updated base-branch boundary

The base branch advanced after PR #81 forked.

`T-6710` proves the exact inverse theorem

\[
m_N>B
\iff
\tau_c(n)\le N
\quad(1\le n\le B),
\]

and therefore identifies SC* exactly with universal finite coefficient
stopping.  It also gives the fixed-source valuation form

\[
v_2(3^{q(w)}n+A_w)\ge|w|
\]

for an all-supercritical word realized from source `n`.

`L-6711` proves endpoint accumulation for a fixed source but explicitly does
not move that source.  This prevents the present attack from confusing
physical or endpoint growth with canonical source escape.

## New lemma — uniform support loss

Fix one valid first-crossing pair `(j,q)`.  Let `u` be the upper-mechanical
word and `v` another admissible word.  If their odd positions are

\[
e_i,\qquad d_i=e_i-h_i,
\]

then

\[
E_u-E_v
=C\sum_i{2^{e_i}\over3^i}(1-2^{-h_i}),
\qquad C={3^q\over2^j}.
\]

For every mechanical odd position,

\[
{1\over6}<{2^{e_i}\over3^i}\le{1\over3}.
\]

Each displaced position has `h_i>=1`, hence pays at least one half of its
mechanical contribution.  If `R(v)` is the displaced support,

\[
\boxed{
E_u-E_v>{C\over12}R(v)>{R(v)\over24}.}
\]

For a canonical non-descent

\[
E_v=(1-C)r_v+d,
\qquad d\ge0,
\]

so

\[
\boxed{
 r_v
 <
 F_j-{C R(v)\over12(1-C)}.}
\]

This is a direct source-coordinate inequality.  It does not average over
words or replace the full denominator by a proper factor.

## Exact source-free support threshold

Put

\[
L_j(R)=\left\lfloor{j-2\over2(R+1)}\right\rfloor.
\]

Define `rho_j` as the least nonnegative `R` such that either `L_j(R)=0` or

\[
2^{L_j(R)}+1
<
3^{R+1}
\left({q\over3\lambda_j}+{q\over3}\right),
\qquad
\lambda_j=j\log2-q\log3.
\]

`L-6811`, `L-6808`, and `L-6815` imply that every internally injective
nonmechanical canonical failure has

\[
R(v)\ge rho_j.
\]

No generic logarithmic-form exponent is used in the definition.  A directed
candidate-specific lower bound for `lambda_j` evaluates it exactly.

## Strictly weaker closure theorem

Define

\[
\boxed{
H_j^{\rm supp}
=
F_j-{C_jrho_j\over12(1-C_j)}.}
\]

Then every internally injective nonmechanical failure has source below
`H_j^supp`.

Repeated proper states reduce to a positive cycle.  Choosing a least-period
cycle, rotating to its minimum, and taking its first coefficient crossing
produces an internally injective canonical failure.  Thus, after a finite
initial audit and the source-qualified all-length mechanical theorem, the
cofinal inequality

\[
\boxed{m_{j-1}^{\rm sup}\ge H_j^{\rm supp}}
\]

closes FC* in full, including the cycle level.

The corrected envelope remains unbounded along lower convergents.  Indeed,
mechanical contributions give

\[
F_j>{C_jq\over6(1-C_j)},
\]

while

\[
rho_j\le\lfloor(j-2)/2\rfloor.
\]

Hence

\[
H_j^{\rm supp}
>
{C_j(2q-rho_j)\over12(1-C_j)}
\to+\infty
\]

along the lower-convergent subsequence.  The same cofinal hypothesis therefore
forces SC*.

The fully explicit scalar sufficient condition is

\[
\boxed{
 m_{j-1}^{\rm sup}
 \ge
 {q/3-C_jrho_j/12\over1-C_j}.}
\]

This is strictly weaker than the requested scalar envelope.

## Smallest exact blocker

The cofinal support-corrected inequality was **not proved**.

Using `T-6710`, define

\[
B_j^{\rm supp}
=
\lceil H_j^{\rm supp}\rceil-1.
\]

The remaining source obligation is exactly

\[
\boxed{
\tau_c(n)\le j-1
\quad
\text{for every }1\le n\le B_j^{\rm supp}}
\]

cofinally over valid first-crossing lengths.

Equivalently, for each fixed source `n`, one needs a finite upper bound on the
length of an all-supercritical word satisfying

\[
v_2(3^{q(w)}n+A_w)\ge|w|.
\]

This is now the smallest fixed-source blocker reached by the unified envelope
route.  Existing endpoint divergence, mean-surplus, family-sparsity, and
prime-power reconstruction theorems do not provide that valuation bound.

## Computation boundary

A local exact scan was used only as an adversarial check against an invalid
all-length strengthening of the cofinal envelope.  No numerical observation
enters `L-6816` or `T-6812`, and no finite scan is extrapolated.

## Files added

```text
research/positive-coefficient-entropy/claims/L-6816-uniform-support-remainder-loss.md
research/positive-coefficient-entropy/claims/T-6812-support-corrected-cofinal-envelope.md
research/positive-coefficient-entropy/CURRENT_STATE.md
reports/gpt56-positive-entropy-01/2026-08-01-75-support-corrected-envelope.md
```

## Honest outcome

The full Collatz theorem is not closed.  The pass does, however, improve the
single sufficient cofinal inequality by a rigorously forced amount tied to
the same internal support that every complete first-crossing obstruction must
carry.

The next proof must now establish the support-corrected moving coefficient-
stopping box or the equivalent fixed-source valuation bound.  Another
physical-growth theorem, family count, or proper-factor sieve does not cross
that boundary.
