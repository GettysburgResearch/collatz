# L-9601 — Negative-cycle single-pulse reduction

**Claim ID:** `L-9601`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-22  
**Scope:** exact accelerated positive-cycle candidates obtained by perturbing one valuation in a repeated negative cycle

## 1. Accelerated word notation

For a positive valuation word

\[
w=(a_0,\ldots,a_{k-1}),
\qquad
A=\sum_{j=0}^{k-1}a_j,
\]

write

\[
2^A S_w(x)=3^k x+C_w,
\]

where

\[
C_w=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j},
\qquad
A_j=\sum_{i<j}a_i.
\]

Suppose a cyclic rotation of `w` has a negative odd integer fixed point `z`:

\[
S_w(z)=z<0.
\]

Then

\[
C_w=z(2^A-3^k).
\tag{1}
\]

## 2. One pulse in a repeated negative cycle

Fix `r>=1` and `delta>=1`. Repeat the rotated word `r` times, but increase the **first** valuation by `delta`:

\[
w_{r,\delta}
=(a_0+\delta,a_1,\ldots,a_{k-1},w,\ldots,w).
\]

Its total exponent and odd-step count are

\[
Ar+\delta,
\qquad kr.
\]

Put

\[
D_{r,\delta}=2^{Ar+\delta}-3^{kr}.
\tag{2}
\]

The first numerator term of the unperturbed repeated word is `3^(kr-1)`. Increasing the first valuation leaves that term unchanged and multiplies every later term by `2^delta`. If `C_r` is the numerator of `w^r`, then

\[
C_r=z(2^{Ar}-3^{kr})
\]

and

\[
\begin{aligned}
C_{r,\delta}
&=3^{kr-1}+2^\delta(C_r-3^{kr-1})\\
&=zD_{r,\delta}
 -(2^\delta-1)(3z+1)3^{kr-1}.
\end{aligned}
\tag{3}
\]

Therefore the unique rational fixed point of the perturbed affine word is

\[
\boxed{
 n_{r,\delta,z}
 =z-
 \frac{(2^\delta-1)(3z+1)3^{kr-1}}
      {D_{r,\delta}}.
}
\tag{4}
\]

## 3. Exact divisibility filter

Assume `D_(r,delta)>0`, as required for a positive cycle. Since

\[
\gcd(D_{r,\delta},3)=1,
\]

integrality of `(4)` implies the much smaller divisibility condition

\[
\boxed{
D_{r,\delta}
\mid
(2^\delta-1)(3z+1).
}
\tag{5}
\]

Equation `(5)` is necessary, not by itself sufficient. Any divisibility hit must still replay every intermediate valuation exactly and return to its positive start.

## 4. Why this covers every single pulse position

A cycle word is defined only up to cyclic rotation. Given a repeated negative-cycle word with one pulsed valuation anywhere, rotate the word so that the pulsed valuation is first. The underlying negative state becomes the corresponding rotated cycle state `z`, and `(2)`--`(5)` apply.

Thus one does not need to scan every raw position independently. It is enough to scan:

1. the finitely many negative states on the primitive cycle;
2. the repetition count `r`;
3. the pulse size `delta`.

## 5. Two native specializations

### Negative three-cycle

The primitive accelerated word is

\[
(1,2),
\qquad
(k,A)=(2,3),
\]

with rotated negative states

\[
z\in\{-5,-7\}.
\]

The reduced coefficients `-(3z+1)` are

\[
14,\ 20,
\]

and

\[
D_{r,\delta}=2^{3r+\delta}-3^{2r}.
\]

### Negative eleven-cycle

The primitive accelerated word is

\[
(1,1,1,2,1,1,4),
\qquad
(k,A)=(7,11),
\]

with rotated odd states

\[
-17,-25,-37,-55,-41,-61,-91.
\]

The reduced coefficients are

\[
50,74,110,164,122,182,272,
\]

and

\[
D_{r,\delta}=2^{11r+\delta}-3^{7r}.
\]

## 6. Exact finite consequence

`X-9601` checks every state above, every `1<=r<=20000`, and the smallest pulse crossing `D>0` together with the next three pulse sizes.

The only integral replay is

\[
(1,2)\longmapsto(2,2),
\qquad n=1,
\]

the trivial Collatz cycle. No nontrivial positive cycle occurs in the frozen scan.

## 7. Interpretation

This closes the simplest perturbative hope:

> repeat a known negative cycle and insert one unusually large division to move the total multiplier just below one.

A viable negative-cycle-derived positive cycle must instead use at least one of:

- pulses at several positions;
- more than one primitive block type;
- a nonperiodic compressed word;
- or a construction not organized as a perturbation of one negative cycle.

## 8. Gap audit

- The lemma does not exclude distributed pulses.
- It does not exclude two-block or substitutional compressed words.
- The finite scan is not an all-`r` theorem.
- Integrality of the affine fixed point is weaker than exact valuation replay; the experiment checks both for every hit.
- No nontrivial cycle, divergent seed, or Collatz counterexample is claimed.
