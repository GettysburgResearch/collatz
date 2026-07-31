# L-6813 — The two coefficient blockers lie under one sharpened scalar envelope

**Claim ID:** `L-6813`  
**Status:** **PROPOSED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Dependencies:** `L-6803`, `L-6812`; the upper-mechanical numerator extremizer  
**Scope:** the exact Box-1 / Box-2 coefficient-stopping program

## 1. Definitions

Put

\[
\alpha={\log2\over\log3}.
\]

For `N>=1`, let

\[
\mathcal S_N^{\rm sup}
=
\{m>0:3^{q_k(m)}\ge2^k\text{ for every }1\le k\le N\}
\]

and

\[
m_N^{\rm sup}=\min\mathcal S_N^{\rm sup}.
\]

At a valid first-crossing length `j`, the last bit is even and the weight is
the unique integer

\[
q(j)=\lfloor\alpha j\rfloor
=\lceil\alpha(j-1)\rceil.
\tag{1}
\]

Put

\[
D_j=2^j-3^{q(j)}>0.
\]

For one first-crossing word `w`, define its real no-descent threshold

\[
\Theta(w)={A_w\over D_j}.
\]

Let

\[
F_j=\max_w\Theta(w),
\tag{2}
\]

where the maximum ranges over all first-crossing words of length `j`.

## 2. Exact box coupling

Suppose a first-crossing word `w` fails canonical descent.  Its canonical
root `r^+(w)` is supercritical through every proper prefix, so

\[
m_{j-1}^{\rm sup}\le r^+(w).
\tag{3}
\]

Canonical failure is exactly

\[
r^+(w)\le{A_w\over D_j}
\]

by `L-6803`.  Therefore

\[
\boxed{
m_{j-1}^{\rm sup}
\le r^+(w)
\le{A_w\over D_j}
\le F_j.}
\tag{4}
\]

Consequently

\[
\boxed{
m_{j-1}^{\rm sup}>F_j}
\tag{5}
\]

forces canonical descent for every first-crossing word of length `j`.

This is the exact relative envelope coupling: the ordinary source-extraction
sequence and the finite-crossing threshold sequence are not independent
proof obligations.

## 3. Exact mechanical envelope

Adjacent moves

```text
10 -> 01
```

preserve length and weight and strictly increase the affine numerator.  The
proper-prefix supercritical constraints make the upper-mechanical word the
unique maximal element under these moves.  Hence

\[
\boxed{
F_j
={A_{\rm mech}(j)\over D_j}.}
\tag{6}
\]

Equivalently, with

\[
C_j={3^{q(j)}\over2^j},
\]

one may write

\[
F_j
={E_{\rm mech}(j)\over1-C_j}.
\]

Thus the exact cofinal comparison is between one least-root sequence and one
explicit mechanical scalar sequence.

## 4. One-third scalar envelope

`L-6812` proves for every first-crossing word

\[
{A_w\over2^j}<{q(j)\over3}.
\]

Therefore

\[
\boxed{
F_j
<
G_j^{(1/3)}
:=
{q(j)\,2^j
 \over
 3\bigl(2^j-3^{q(j)}\bigr)}.}
\tag{7}
\]

The explicit sufficient inequality

\[
\boxed{
m_{j-1}^{\rm sup}>G_j^{(1/3)}}
\tag{8}
\]

therefore forces descent for every first crossing of length `j`.

This improves the earlier `q/2` scalar envelope by the factor `2/3`.

## 5. Cofinal implication for both boxes

The exact mechanical envelope `F_j` is unbounded along lower continued-
fraction convergents `q/j<alpha`, because

\[
j\log2-q\log3\to0^+
\]

and the first odd contribution alone makes `F_j` diverge.

Suppose there is `J` such that for every valid first-crossing length `j>=J`,

\[
\boxed{m_{j-1}^{\rm sup}>F_j.}
\tag{9}
\]

Then:

1. `(5)` forces canonical descent at every sufficiently late finite first
   crossing;
2. the unbounded subsequence `F_j` and `(9)` force the monotone sequence
   `m_N^sup` to be unbounded, hence
   \[
   m_N^{\rm sup}\to\infty.
   \]

After a finite small-length audit, `(9)` closes both coefficient-stopping
boxes.

The coarser condition `(8)` has the same implication.

## 6. Effective polynomial version

Suppose an effective two-logarithm theorem gives

\[
\lambda_j=j\log2-q(j)\log3
\ge c_0j^{-\mu}.
\]

Since

\[
1-C_j=1-e^{-\lambda_j}\ge\lambda_j/2
\]

at a first crossing, equation `(7)` gives

\[
\boxed{
G_j^{(1/3)}
< {2\over3c_0}j^{\mu+1}.}
\tag{10}
\]

Thus the source-qualified theorem

\[
\boxed{
m_N^{\rm sup}
>{2\over3c_0}(N+1)^{\mu+1}
\quad\text{eventually}}
\tag{11}
\]

would close both boxes after the finite and positive-cycle checks.

The repository currently has no such polynomial lower bound on the least
canonical supercritical roots.

## 7. What this does and does not reduce

`L-6813` replaces the pair

```text
prove source escape;
prove every first crossing descends;
```

by the one cofinal relative-growth target

\[
\boxed{
m_{j-1}^{\rm sup}>F_j.}
\]

This is a useful exact fusion, but it is not itself weaker than the missing
positive conclusion: proving it cofinally would settle both lanes.

## 8. Gap audit

- Neither `(9)` nor `(11)` is proved.
- `F_j` is unbounded, so a fixed verification floor cannot dominate it.
- Real numerator extremality does not order canonical roots modulo `2^j`;
  wrapped nonmechanical words remain the finite-place obstruction.
- The effective constants in `(10)--(11)` require primary-source review.
- No proof of Collatz is claimed.
