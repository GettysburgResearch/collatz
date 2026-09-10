# L-7701 — Exact repair of the Claude frequency-block mean

**Claim ID:** `L-7701`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-crossmodel-audit-01`  
**Created:** 2026-07-27  
**Dependencies:** branch-qualified Claude `L-0011/L-0012` at `407a788972a72da2fde59c19e9446e02647cc4f4`; branch-qualified exact reciprocity identity PR #16 `L-9304` at `87478352e65c7b816dfc8b3b30894b71fb50f662`  
**Scope:** the `64 -> 81` Fourier product and frequency blocks used by Claude `L-0020`  
**Related counterexample candidates:** none

## Statement

Let `S_K(theta)` be the exact Fourier product of the Claude `64 -> 81` survivor set. Let `r>=1` and assume

\[
81^r\le 2^K.
\]

For every interval `I` of exactly `81^r` consecutive positive frequencies contained in `[1,2^K]`,

\[
\boxed{
\frac1{81^r}\sum_{\theta\in I}
\frac{|S_K(\theta)|}{2^K}
\le \left(\frac7{10}\right)^r.}
\]

Thus the frequency-block hypothesis sought by Claude `L-0020` holds with the exact constant `a=7/10`, which lies in `(1/81,1)`.

## Why the submitted proof needs repair

Claude `L-0020` replaces each true phase by its reciprocal residue and then applies the exact Markov-chain average. PR #16 `L-9304` proves that the replacement has an explicit nonzero error:

\[
\frac{z_{K,t}(\theta)}{64^{K-t}}
=
\frac{q_{K,t}(\theta)}{81^{t+1}}
+
\frac{17\theta}{81^{t+1}64^{K-t}}.
\]

The submitted proof never pays this term. The claimed constant

\[
2/\pi+1/81
\]

therefore does not follow from the displayed argument.

## Proof

Keep only the first `r` factors of the exact product; all omitted factors have absolute value at most one. Put

\[
x_t(\theta)=z_{K,t}(\theta)/64^{K-t},
\qquad
y_t(\theta)=q_{K,t}(\theta)/81^{t+1}.
\]

As `theta` runs through any complete residue system modulo `81^r`, multiplication by the unit `-17*64^{-K}` makes the initial reciprocal state uniform modulo `81^r`. The nested recurrence

\[
q_{t+1}\equiv64q_t\pmod{81^{t+1}}
\]

adds one fresh uniform base-81 digit at each level. Conditional averaging and Claude `L-0012` therefore give the exact reciprocal-product bound

\[
\frac1{81^r}\sum_{\theta\in I}
\prod_{t<r}|\cos(\pi y_t(\theta))|
\le a^r,
\qquad a:=2/\pi+1/81.
\]

For products of numbers in `[0,1]`, telescoping and the `pi`-Lipschitz bound for `|cos(pi x)|` give

\[
\left|
\prod_{t<r}|\cos(\pi x_t)|-
\prod_{t<r}|\cos(\pi y_t)|
\right|
\le \pi\sum_{t<r}|x_t-y_t|.
\]

The exact errors form a geometric sum:

\[
\sum_{t<r}|x_t-y_t|
=
\frac{17\theta}{64^K}
\sum_{t<r}\frac{64^t}{81^{t+1}}
<\frac{\theta}{64^K}
\le\frac1{32^K}.
\]

Using `pi<4`, the true block mean is at most

\[
a^r+4/32^K.
\]

Now `pi>3` gives

\[
a<2/3+1/81=55/81<7/10.
\]

Since `a>1/2`,

\[
(7/10)^r-a^r
\ge
\left(7/10-55/81\right)2^{-(r-1)}
=
\frac{17}{810}2^{-(r-1)}.
\]

The condition `81^r<=2^K` with `r>=1` forces `K>=7` and `r<=K`. Hence

\[
(7/10)^r-a^r
\ge\frac{17}{810}2^{-(K-1)}
>4/32^K.
\]

Combining the inequalities proves the claim.

## Consequence and boundary

This repairs the local frequency-block input. It does not independently verify Claude `T-0030` or any fair-window/minimal-survivor consequence. Those require a separate reconstruction of the density-one shell assembly and its downstream counting interface.

## Adversarial checks

`X-7701` checks the smallest feasible `K=7` comparison exactly:

```text
reciprocity-error upper bound = 1/8589934592
gap lower bound               = 17/51840.
```
