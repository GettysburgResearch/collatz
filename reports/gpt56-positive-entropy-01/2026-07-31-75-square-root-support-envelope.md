# Session report — square-root support, one-third near-returns, and the fused coefficient envelope

**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Date:** 2026-07-31  
**Issue:** #75  
**Branch:** `agent/gpt56-positive-entropy-01/75-supercritical-entropy`  
**PR:** #81  
**Status:** draft mathematical research

## 1. Objective of this pass

The pass did not reopen finite-prefix amplification, a free symbolic
completion, or another conditional growth theorem. It attacked the exact
residual objects from `Q-6802`:

```text
SC*:
  least canonical roots of supercritical prefixes escape;

FC*:
  no wrapped first-crossing excess path satisfies the complete shifted
  denominator equations with one common small displacement.
```

The newest parallel work on PR #83 supplied a valuable fusion: one cofinal
comparison between the least-root sequence and the largest first-crossing
threshold would close both coefficient lanes.

## 2. Exact box coupling

For a first-crossing failure of length `j`,

\[
m_{j-1}^{\rm sup}
\le r^+(w)
\le {A_w\over2^j-3^q}
\le F_j,
\]

where `F_j` is the upper-mechanical threshold. Therefore

\[
m_{j-1}^{\rm sup}>F_j
\]

forces every first crossing of that length to descend.

Since `F_j` is unbounded along lower convergents, the same cofinal inequality
would force `m_N^sup` to infinity. `L-6813` records this as one exact relative
envelope.

The reduction is genuine, but the missing lower bound on `m_N^sup` is still
not proved.

## 3. Bilateral shifted equation and coordinate correction

Let

\[
P=2^j,
\qquad Q=3^q,
\qquad D=P-Q,
\]

and suppose the canonical near-return is

\[
T^j(r)=s=r+d.
\]

`L-6812` proves the bilateral identities

\[
\boxed{A=Dr+Pd=Ds+Qd.}
\]

Thus

```text
source  r=(A-Pd)/D;
endpoint s=(A-Qd)/D.
```

The congruences modulo `D` are equivalent, but the integer quotients differ
by `d`.

This exposed a coordinate error in the first version of PR #83 `L-6909`:
`A=nD+dQ` uses the endpoint as `n`, while the same paragraph reconstructed
`n=(A-Pd)/D` as the source. The correction was posted directly to PR #83
before further use.

## 4. One-third displacement window

The exact normalized affine remainder is

\[
{A\over2^j}
=
{1\over2}
\sum_{m=1}^{j}
 v_{m-1}3^{D_j-D_m}.
\]

Every nonzero term comes from an odd step ending at a proper time. Hence

\[
D_m\ge1-\alpha,
\qquad
D_j<0,
\qquad
\alpha={\log2\over\log3},
\]

so every term is strictly below

\[
{1\over2}3^{-(1-\alpha)}={1\over3}.
\]

Therefore

\[
\boxed{
{A\over2^j}<{q\over3},
\qquad
0\le d<{q\over3}<{j\over3}.}
\]

This sharpens:

- the finite displacement list;
- the dual bad interval;
- the scalar crossing envelope;
- the self-shadowing depth;
- the complete prime-power compiler.

The new scalar sufficient envelope is

\[
F_j
<
{q(j)2^j
 \over
 3(2^j-3^{q(j)})}.
\]

## 5. Support-sensitive factor complexity

Let `R` be the number of odd positions displaced from the upper-mechanical
word. The two binary words differ at at most `2R` positions. Therefore

\[
\boxed{p_v(L)\le L+1+2RL.}
\]

Taking

\[
L_R=\left\lfloor{j-2\over2(R+1)}\right\rfloor
\]

forces a repeated proper factor whenever `L_R>=1`.

In an acyclic physical realization, the two starts are distinct, so their
state difference is a nonzero multiple of `2^(L_R)`. This feeds directly into
the exact return/gap inequality.

## 6. Square-root support theorem

The prefix-excess height satisfies

\[
B<H+1\le R+1.
\]

Combining the support-forced return with the quoted Rhin lower bound gives

\[
2^{L_R}+1
<
{3\over2}3^{R+1}j^{14.3}.
\]

Solving the resulting quadratic gives the explicit source-qualified floor

\[
\boxed{
R
\ge
\left\lfloor
{-A_j+\sqrt{A_j^2+2(\log_2 3)(j-2)}
 \over2\log_2 3}
\right\rfloor,}
\]

where

\[
A_j=14.3\log_2j+1+\log_2(3/2).
\]

Hence

\[
\boxed{
\liminf{R_j\over\sqrt j}
\ge
\sqrt{{\log2\over2\log3}}
=0.5615\ldots.}
\]

This improves the previous cube-root support theorem. The total integrated
displacement still satisfies the independent two-thirds-scale floor.

A surviving acyclic obstruction must now be:

```text
nonmechanical;
a genuine dyadic wrap;
O(log j)-early relative to the mechanical word;
O(log j)-early relative to its own post-return tail;
Omega(j^(2/3)) in total displacement;
Omega(sqrt(j)) in distinct displaced odd positions;
accepted by every complete prime-power equation;
and governed by one common 0<d<q/3.
```

## 7. Lossless compiler update

`L-6809` was updated so that a complete local-path tuple certifies an exact
ordinary near-return if and only if it passes all of:

```text
generalized CRT compatibility;
unique monotone physical excess lift;
all proper first-crossing coefficient inequalities;
one common 0<=d<q/3;
every complete prime-power congruence A == 3^q d;
canonical source r=(A-2^j d)/D in the positive rectangle.
```

A selected order-cover may decode the word but does not certify omitted prime
powers. The first-crossing test remains mandatory after reconstruction.

## 8. What remains

The pass did not prove either unrestricted theorem.

### SC*

\[
\min_{w\in\mathcal W_N^{\rm sup}}r_w\to\infty.
\]

The fused envelope suggests the quantitative target

\[
m_{j-1}^{\rm sup}>F_j,
\]

but no cofinal lower bound on the least roots is currently available.

### FC*

Exclude every square-root-supported wrapped excess path from the complete
prime-power target interval

\[
0<d<q/3.
\]

The cycle level `d=0` remains separate.

## 9. Claims added or materially sharpened

```text
L-6811  displaced support controls factor complexity          PROPOSED
T-6810  square-root displaced-support floor                   PROPOSED / SOURCE-DEPENDENT
L-6812  bilateral shifted equation and one-third window       PROPOSED
L-6813  sharpened box-coupling envelope                       PROPOSED
L-6807  displacement range sharpened from j/2 to q/3          PROPOSED
L-6809  complete compiler tightened and coordinate-safe        PROPOSED / SOURCE-QUALIFIED
L-6810  self-shadowing window sharpened to log_2(q/3)          PROPOSED
Q-6802  residual theorem pair updated                          OPEN
```

## 10. Review priorities

1. reconstruct the `2R` Hamming-support bound and factor count in `L-6811`;
2. check the `L_R=0` case and quadratic extraction in `T-6810`;
3. verify the termwise `1/3` bound in `L-6812`;
4. audit source-versus-endpoint quotients;
5. check all `q/3` substitutions in `L-6807/L-6809/L-6810`;
6. audit the quoted Rhin normalization;
7. preserve the positive-cycle level and every omitted-factor warning.

No proof of Collatz, counterexample, nontrivial cycle, or `K-####` object is
claimed.
