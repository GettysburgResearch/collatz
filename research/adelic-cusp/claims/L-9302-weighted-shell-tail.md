# L-9302 — Weighted shell tail from block means

**Claim ID:** L-9302  
**Title:** Exponentially decaying block means force an exponentially small weighted high-frequency tail  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** elementary interval decomposition; no Collatz theorem  
**Scope:** abstract Fourier-weighted estimate, intended for the EQ block means  
**Related counterexample candidates:** none

## Statement

Let `H >= 1`, let

\[
\frac1{81}<a<1,
\]

and let

\[
F:\{1,2,\ldots,H\}\longrightarrow[0,1].
\]

Assume the following block-mean property:

> For every integer `r >= 0` with `81^r <= H`, and every interval `I` of exactly `81^r` consecutive integers contained in `{1,...,H}`,
> \[
> \sum_{n\in I}F(n)\le81^r a^r. \tag{BM_r}
> \]

Then, for every `M >= 0` with `81^M <= H`,

\[
\boxed{
\sum_{n=81^M}^{H}\frac{F(n)}{n}
\le C_a a^M,
}
\]

where one valid explicit constant is

\[
\boxed{
C_a=
\frac{80}{1-a}
+
\frac{80}{1-(81a)^{-1}}.
}
\]

In particular, with

\[
a_*=\frac2\pi+\frac1{81},
\]

the high-frequency contribution is `O(a_*^M)` uniformly in `H`.

## Definitions

An *interval of consecutive integers* is a set

\[
\{u,u+1,\ldots,u+81^r-1\}.
\]

The interval need not begin at a multiple of `81^r`. This uniformity is important in the final incomplete shell.

The weight `1/n` is the harmonic weight occurring in the Erdős--Turán discrepancy sum used by the issue-#4 EQ program.

## Motivation

A pointwise bound for every frequency up to `2^K` is much stronger than the weighted discrepancy target requires. The proposed issue-#4 block-mean theorem controls complete blocks of `81^r` consecutive frequencies. This lemma converts that average information into a uniform tail estimate and leaves only a slowly growing low-frequency window for pointwise work.

## Proof

Let

\[
R=\lfloor\log_{81}H\rfloor,
\]

so

\[
81^R\le H<81^{R+1}.
\]

Because `81^M <= H`, one has `M <= R`.

### Complete shells

For each `r` with `M <= r < R`, the shell

\[
[81^r,81^{r+1})\cap\mathbb Z
\]

has length

\[
81^{r+1}-81^r=80\cdot81^r
\]

and is the disjoint union of exactly `80` consecutive blocks of length `81^r`. On each block, `(BM_r)` gives total mass at most `81^r a^r`. Since every denominator in the shell is at least `81^r`,

\[
\sum_{81^r\le n<81^{r+1}}
\frac{F(n)}n
\le
\frac{80\cdot81^r a^r}{81^r}
=80a^r.
\]

Summing the complete shells gives

\[
\sum_{r=M}^{R-1}80a^r
\le\frac{80}{1-a}a^M. \tag{1}
\]

### Final incomplete shell

It remains to control

\[
I_R=[81^R,H]\cap\mathbb Z.
\]

Write its cardinality in base `81`:

\[
|I_R|=\sum_{j=0}^{R}b_j81^j,
\qquad 0\le b_j\le80.
\]

Reading this expansion from the largest place to the smallest partitions the consecutive interval `I_R` into `b_j` consecutive blocks of length `81^j` for each `j`. The block hypothesis therefore gives

\[
\sum_{n\in I_R}F(n)
\le
\sum_{j=0}^{R}b_j81^j a^j
\le
80\sum_{j=0}^{R}81^j a^j.
\]

Every `n in I_R` satisfies `n >= 81^R`, hence

\[
\begin{aligned}
\sum_{n\in I_R}\frac{F(n)}n
&\le
80\sum_{j=0}^{R}81^{j-R}a^j\\
&=80a^R\sum_{\ell=0}^{R}(81a)^{-\ell}\\
&\le
\frac{80}{1-(81a)^{-1}}a^R\\
&\le
\frac{80}{1-(81a)^{-1}}a^M. \tag{2}
\end{aligned}
\]

The geometric series is valid because `81a>1`.

Adding `(1)` and `(2)` proves the stated bound. QED.

## Dependency audit

The proof uses only:

- the block-mean hypothesis `(BM_r)`;
- the exact shell identity `81^(r+1)-81^r=80*81^r`;
- base-`81` expansion of a finite interval length;
- two elementary geometric-series bounds.

No independence, equidistribution, Collatz dynamics, or unproved asymptotic statement is used.

To apply the lemma to issue #4, a reviewer must verify that its proposed Theorem 11 supplies `(BM_r)` for **every consecutive full block** in the required frequency range, not merely for blocks with one preferred alignment.

## Gap audit

- A global average over `{1,...,H}` would not suffice; the proof uses uniform block control at every scale and location.
- The lemma controls the harmonic weighted tail, not the maximum Fourier coefficient in that tail.
- The explicit constant is intentionally crude. Improving it is irrelevant unless a later argument needs finite-depth numerics.
- The base `81` is essential only because it matches the available block periods. The proof generalizes to any integer base `B >= 2` with `B-1` in place of `80`.
- This result does not prove the block-mean hypothesis.

## Adversarial tests

1. At `M=R`, there are no complete shells. The base-`81` decomposition of the final interval still proves the estimate.
2. If `H=81^R-1`, then the final shell belongs to the previous value of `R`, and the complete-shell calculation is exact.
3. If `F` is supported at one point, `(BM_r)` holds whenever the point mass is at most `81^r a^r` at each containing scale; the conclusion reduces to the evident `1/n` bound.
4. If `F` is identically `1`, `(BM_1)` fails for every `a<1`, showing that the hypothesis carries real content.

## Remaining uncertainty

The abstract proof is complete-looking. The application risk is entirely in the exact quantifiers of the branch-qualified frequency block-mean input.

## Suggested next attack

Use this lemma in `T-9301` to choose a growing cutoff `81^M`. Then seek the weakest possible uniform estimate below the cutoff rather than attacking all `2^K` frequencies.
