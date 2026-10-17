# L-0023 — Quadratic Hensel recurrence for the moving stage bulk

Claim ID: `L-0023`  
Title: Exact rational-frontier plus quadratic-defect decomposition of the dyadic tower stack  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Dependencies: `L-0021`, `L-0022`, `O-0009`  
Scope: stage-boundary connector prefixes on the negative eleven-cycle  
Related counterexample candidates: none

## Statement

Fix one phase-34 self-return tower type. Retain its constants

\[
r,
\qquad
g_0,
\qquad\mu_*,
\]

and define

\[
\omega_m=\omega_{2^m}
=
\frac{\mu_*+3^{-g_0-7\,2^m}}{2^{r+1}}
\in\mathbb Z_2
\tag{1}
\]

for all sufficiently large \(m\).

Let the rational frontier be

\[
\boxed{
\omega_\infty
=
\frac{\mu_*+3^{-g_0}}{2^{r+1}}.
}
\tag{2}

Define

\[
\boxed{
y_m=3^{-7\,2^m}}
\tag{3}
\]

and the normalized moving defect

\[
\boxed{
u_m=
\frac{y_m-1}{2^{m+2}}.
}
\tag{4}

Then:

### 1. Integral odd defect

\[
\boxed{u_m\in\mathbb Z_2^\times.}
\tag{5}

That is, \(u_m\) is a 2-adic odd unit.

### 2. Exact quadratic stage recurrence

\[
\boxed{
u_{m+1}
=
u_m+2^{m+1}u_m^2.
}
\tag{6}

Equivalently, the stage update is one Hensel-squaring operation.

### 3. Exact connector-frontier decomposition

Put

\[
J_m=m-r+1.
\tag{7}

Then

\[
\boxed{
\omega_m
=
\omega_\infty
+2^{J_m}3^{-g_0}u_m.
}
\tag{8}

Thus every full stage-boundary connector prefix decomposes into:

1. an eventually periodic rational frontier \(\omega_\infty\);
2. a dyadic shift by \(J_m\) positions;
3. one odd moving bulk word \(u_m\).

### 4. The defect converges by forward Hensel lifting

The sequence \((u_m)\) is Cauchy in \(\mathbb Z_2\), because

\[
\boxed{
\nu_2(u_{m+1}-u_m)=m+1.
}
\tag{9}

It therefore converges to one odd 2-adic unit

\[
\boxed{
u_\infty=\lim_{m\to\infty}u_m.}
\tag{10}

Moreover

\[
\boxed{
u_{m+1}\equiv u_m\pmod{2^{m+1}},}
\tag{11}

and the congruence is exact: it fails modulo \(2^{m+2}\).

### 5. Finite-prefix update rule

Let \(N\ge m+2\). If a finite LSD-first word represents

\[
U_m\equiv u_m\pmod{2^N},
\]

then the next prefix is determined exactly by

\[
\boxed{
U_{m+1}
\equiv
U_m+2^{m+1}U_m^2
\pmod{2^N}.
}
\tag{12}

No additional 2-adic oracle is needed to compute the next prefix at the **same** precision.

The unresolved problem is precision growth: producing \(u_{m+1}\) at a longer precision than was already known for \(u_m\).

## Proof

For the valuation, use 2-adic LTE:

\[
\nu_2(3^{7\,2^m}-1)=m+2.
\]

Multiplication by the odd unit \(3^{-7\,2^m}\) does not change valuation, so

\[
\nu_2(y_m-1)=m+2.
\]

Equation (4) therefore defines an odd 2-adic integer, proving (5).

Since

\[
y_{m+1}
=3^{-7\,2^{m+1}}
=y_m^2,
\]

write

\[
y_m=1+2^{m+2}u_m.
\]

Then

\[
\begin{aligned}
y_{m+1}
&=(1+2^{m+2}u_m)^2\\
&=1+2^{m+3}u_m+2^{2m+4}u_m^2\\
&=1+2^{m+3}
\left(u_m+2^{m+1}u_m^2\right).
\end{aligned}
\]

Comparing with

\[
y_{m+1}=1+2^{m+3}u_{m+1}
\]

proves (6).

For the frontier decomposition,

\[
\begin{aligned}
\omega_m-\omega_\infty
&=
\frac{3^{-g_0}(y_m-1)}{2^{r+1}}\\
&=
3^{-g_0}2^{m-r+1}u_m\\
&=
2^{J_m}3^{-g_0}u_m,
\end{aligned}
\]

which proves (8).

Because \(u_m\) is odd, equation (6) gives

\[
\nu_2(u_{m+1}-u_m)=m+1,
\]

proving (9), exact congruence (11), and the Cauchy property. Completeness of \(\mathbb Z_2\) gives the limit. Reducing (6) modulo \(2^N\) proves (12). ∎

## Interpretation

The stage stack has now split into three mathematically distinct tracks:

### 1. Rational frontier

The low stabilized bits come from one explicit periodic rational, recorded in `O-0009`.

### 2. Seven-bit odometer

The 128 substeps of one stage have the exact carry profile in `L-0021`.

### 3. Quadratic moving bulk

Every nonperiodic high correction is contained in one odd word \(u_m\) updated by

\[
u\longmapsto u+2^{m+1}u^2.
\]

This is a far smaller target than an arbitrary connector language. A string-rewrite construction need only implement one shifted square-and-add operation per scale stage, plus finite frontier and target control.

## The remaining precision gap

Equation (12) computes the next bulk word at any precision already present. It does not manufacture higher bits that were absent from the current finite word.

A forward ordinary stack grammar must therefore couple the quadratic update to the positive free-tail budget of `T-0022`. The extra archimedean data created by the 128 tail-expanding connectors must fund the additional binary precision required at the next stage.

This is now the sharpest form of the construction problem:

> turn real free-tail growth into Hensel precision growth for the quadratic defect word, while transporting one marked ordinary Collatz particle.

## Dependency audit

- `L-0022` supplies the rational frontier.
- `L-0021` supplies the exact stage valuation.
- The quadratic recurrence is elementary squaring and LTE.

## Gap audit

- The limit \(u_\infty\) is a 2-adic completion object and must not be preloaded.
- Same-precision computability is weaker than forward precision generation.
- No local finite rewrite implementation of squaring has yet been integrated with the marked trajectory.

## Adversarial tests

`X-0012` verifies (5)--(12) modulo increasing powers of two over several stages and all four phase-34 tower types.

## Suggested next attack

Construct a stage-level string transducer with tracks

```text
frontier-state | odometer-state | bulk-word | marked-tail
```

and prove a net 128-step rewrite that:

1. performs the quadratic bulk update;
2. appends at least one new correct bulk bit;
3. returns finite control to the next stage;
4. maps the marked ordinary state through the exact 128 Collatz tower blocks.