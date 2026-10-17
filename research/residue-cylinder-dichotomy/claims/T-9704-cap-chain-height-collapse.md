# T-9704 — Global height collapse on every cap-correction chain

**Claim ID:** `T-9704`  
**Title:** A surviving 256-stage cap chain uses asymptotically less than one part in 275 of its cylinder precision  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `L-9703`; frozen PR #3 stage exponent formulas  
**Scope:** every eventual cap-correction chain of corrected phase-`-34` 256-transition stages  
**Related counterexample candidates:** none

## Statement

Suppose an admissible sequence of corrected stage words has a cap-correction
tail beginning at scale `M >= 8`:

\[
\boxed{R_{m+1}=S_m
\qquad(m\ge M).}
\tag{1}
\]

Use the exact PR #3 stage notation

\[
R_{m+1}=\Lambda_mR_m+\beta_m,
\tag{2}
\]

where

\[
\Lambda_m=\frac{3^{A_m}}{2^{D_m}},
\tag{3}
\]

\[
A_m=\frac{5369}{2}2^m+1792,
\qquad
D_m=\frac{1085579}{256}2^m+2816.
\tag{4}
\]

Then:

### 1. One-step shifted height contraction

For every `m >= M`,

\[
\boxed{
R_{m+1}+257
<
\Lambda_m(R_m+257).}
\tag{5}
\]

### 2. Exact product height bound

For every `m > M`,

\[
\boxed{
R_m+257
<
(R_M+257)
\prod_{k=M}^{m-1}\Lambda_k.}
\tag{6}
\]

### 3. Explicit elementary exponent bound

Put

\[
\gamma=\frac{161341}{10496},
\qquad
c_0=\frac{1024}{41}.
\tag{7}
\]

Then

\[
\boxed{
\log_2(R_m+257)
<
\log_2(R_M+257)
+\gamma(2^m-2^M)
+c_0(m-M).}
\tag{8}
\]

No decimal approximation is used in the proof.

### 4. Cylinder-height collapse

Let

\[
q_m=2^{D_m}
\]

be the complete stage modulus. Then

\[
\boxed{
\limsup_{m\to\infty}
\frac{\log_2(R_m+257)}{D_m}
\le
\frac{161341}{44508739}
<
\frac1{275}.}
\tag{9}
\]

Thus every hypothetical cap-correction chain uses asymptotically less than
`0.363%` of the available binary completion height.

Equivalently,

\[
\boxed{
\log_2\frac{R_m+257}{q_m}
<
-\frac{22173699}{5248}2^m+O_M(m).}
\tag{10}
\]

The completion precision exceeds the ordinary representative height by more
than `99.6%` of its leading exponent.

## Definitions

A **cap-correction chain** is the zero-quotient tail isolated in `T-9703`:

\[
z_m=R_m,
\qquad
z_{m+1}=S_m=R_{m+1}.
\]

The constant `257` is a fixed archimedean shift chosen to absorb all 256 local
offset contributions. It is not a radix digit and is not part of the physical
state.

## Motivation

`T-9703` removes the arbitrary ordinary quotient from every hypothetical
infinite trajectory but leaves open whether the exact cap-correction equality
can persist. `L-9703` shows that the complete inhomogeneous stage offset is only
256 copies of the stage surplus scale. Consequently the surviving correction
height grows at the **surplus** rate, about `15.4*2^m` bits, while the complete
stage cylinder has about `4240.5*2^m` bits.

This converts the final ordinary-integer question into a very strong
completion-height or p-adic approximation problem. A future exclusion theorem
must still display the relevant nonzero numerator or logarithmic form; the
small ratio alone is not a contradiction.

## Proof

`L-9703` gives

\[
|\beta_m|<256\Lambda_m.
\tag{11}
\]

The exact lower bound

\[
\log_2 3>\frac{84}{53}
\]

implies

\[
\log_2\Lambda_m
>
\frac{191801}{13568}2^m+rac{1280}{53}>9
\qquad(m\ge8).
\tag{12}
\]

Hence

\[
\Lambda_m>512>257.
\tag{13}
\]

Using (2), nonnegativity of `R_(m+1)`, and (11),

\[
\begin{aligned}
R_{m+1}+257
&\le \Lambda_mR_m+|\beta_m|+257\\
&<\Lambda_m(R_m+256)+257\\
&<\Lambda_m(R_m+257),
\end{aligned}
\]

where the last inequality uses `Lambda_m>257`. This proves (5). Iteration gives
(6).

For the upper exponent, the exact inequality

\[
\log_2 3<\frac{65}{41}
\]

gives

\[
\begin{aligned}
\log_2\Lambda_m
&=A_m\log_2 3-D_m\\
&<
\left(
\frac{5369}{2}\frac{65}{41}
-rac{1085579}{256}
\right)2^m
+\left(1792\frac{65}{41}-2816\right)\\
&=
\frac{161341}{10496}2^m+rac{1024}{41}\\
&=\gamma2^m+c_0.
\end{aligned}
\tag{14}
\]

Taking logarithms in (6), applying (14), and summing the geometric series

\[
\sum_{k=M}^{m-1}2^k=2^m-2^M
\]

proves (8).

Finally,

\[
D_m=\frac{1085579}{256}2^m+2816.
\]

Divide (8) by `D_m` and pass to the limsup. The fixed initial term and the linear
term `c_0m` vanish relative to `2^m`, giving

\[
\limsup
\frac{\log_2(R_m+257)}{D_m}
\le
\frac{161341/10496}{1085579/256}
=
\frac{161341}{44508739}.
\]

The exact comparison

\[
161341\cdot275=44368775<44508739
\]

proves the strict bound by `1/275` in (9).

Subtracting `D_m` from (8) gives (10), because

\[
\frac{1085579}{256}-\frac{161341}{10496}
=
\frac{22173699}{5248}.
\]

This completes the proof. ∎

## Dependency audit

- `L-9703` supplies the type-uniform bound on the normalized affine offset.
- The exact PR #3 formulas (4) are used as a frozen `PROPOSED` interface.
- The integer comparisons `3^53>2^84` and `3^41<2^65` supply the lower and
  upper logarithmic bounds.
- No equidistribution, entropy, transcendence, or finite experiment is a proof
  dependency.

## Gap audit

- The theorem is conditional on a cap-correction chain existing. It does not
  construct or exclude one.
- A representative shorter than `q_m^(1/275)` can still be a valid residue.
  Product-formula or logarithmic-form work must identify the structured target.
- The estimate concerns the stage residual, not an initialized marked Collatz
  integer.
- The additive constant 257 is an archimedean proof device only.
- The theorem does not imply eventual periodicity of stage words.

## Adversarial tests

`X-9703` independently checks the exact coefficient identities, composes 82,082
small expanding odd-affine systems satisfying the local offset hypotheses, and
constructs 32 exact artificial cap chains. A separate checker uses a different
family of 11,403 expanding composites and 27 cap chains.

## Remaining uncertainty

The highest-value review points are the uniform inequality `|beta_m|<256
Lambda_m`, the use of `Lambda_m>257`, and the passage from the exact finite
bound (8) to the asymptotic cylinder ratio (9).

## Suggested next attack

For each fixed normalized stage-word pair, express the correction congruence in
a finite p-adic exponential/logarithmic form. The height budget (9) leaves a
factor greater than 275 between ordinary height and completion precision, far
above the direct rational threshold. A uniform lower bound over the finite
stage-word alphabet would exclude every cap-correction chain.
