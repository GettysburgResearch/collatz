# T-0010 — Rational-base orbits force a fixed fractional-part window

Claim ID: `T-0010`  
Title: Real rounding law, normalized displacement width, and fractional-part confinement  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `T-0008`  
Scope: infinite signed rational-base return chains  
Related counterexample candidates: none

## Statement

Let \(M,N\) be coprime positive integers with \(N>M\), and put

\[
\beta=\frac NM,
\qquad
\rho=\frac MN,
\qquad
c=N-M.
\]

Let \(A\subset\mathbb Z\) be a finite nonempty signed digit set. Suppose an infinite integer chain satisfies

\[
Nq_t=Mq_{t+1}+a_t,
\qquad a_t\in A,
\qquad t\ge0.
\tag{1}
\]

Write

\[
a_-=\min A,
\qquad
a_+=\max A,
\qquad
\Delta(A)=\frac{a_+-a_-}{c}.
\tag{2}
\]

Then:

### 1. Exact real decomposition

The limit

\[
\boxed{
C=\lim_{t\to\infty}\rho^tq_t
}
\tag{3}
\]

exists. Define

\[
\boxed{
x_t=
\frac1N
\sum_{j=0}^{\infty}a_{t+j}\rho^j.
}
\tag{4}
\]

Then

\[
\boxed{
q_t=C\beta^t+x_t
}
\tag{5}
\]

for every \(t\ge0\), and

\[
\boxed{
\frac{a_-}{c}
\le x_t\le
\frac{a_+}{c}.
}
\tag{6}
\]

### 2. Fractional-part confinement

Because \(q_t\) is an integer,

\[
\boxed{
\{C\beta^t\}=\{-x_t\}
}
\tag{7}
\]

on the circle \(\mathbb R/\mathbb Z\). Consequently the full multiplicative orbit

\[
\{C\beta^t\}
\qquad(t\ge0)
\]

is confined to the image modulo one of the interval

\[
\left[-\frac{a_+}{c},-\frac{a_-}{c}\right],
\tag{8}
\]

whose circular length is at most

\[
\boxed{
\min\{1,\Delta(A)\}.
}
\tag{9}
\]

For a collision chart, \(a_+-a_-\) equals the diameter of its ordinary branch-residue or offset alphabet. Thus

\[
\boxed{
\Delta
=
\frac{\operatorname{diam}D}{N-M}
}
\tag{10}
\]

is an intrinsic **aspect ratio** measuring the real control window of the chart.

### 3. Balanced nearest-integer form

Translating the quotient coordinate by an integer \(z\),

\[
q_t=\widetilde q_t+z,
\]

replaces the digit alphabet by

\[
\widetilde A=A-cz
\tag{11}
\]

without changing \(\Delta(A)\). If a gauge can be chosen with

\[
\widetilde A\subseteq[-c/2,c/2],
\tag{12}
\]

then

\[
|\widetilde x_t|\le\frac12
\]

and every quotient is a nearest integer to one exponential orbit:

\[
\boxed{
\widetilde q_t
=\operatorname{nint}(\widetilde C\beta^t),
}
\tag{13}
\]

with ties handled by the actual signed digit.

## Proof

From (1),

\[
q_{t+1}=\beta q_t-\frac{a_t}{M}.
\tag{14}
\]

Multiplying by \(\rho^{t+1}\) gives

\[
\rho^{t+1}q_{t+1}
=
\rho^tq_t-rac{a_t}{N}\rho^t.
\tag{15}
\]

Since the digits are bounded and \(0<\rho<1\), the correction series converges absolutely. Hence \(\rho^tq_t\) converges, proving (3), and summing (15) from \(t\) to infinity gives

\[
\rho^tq_t-C
=
\frac1N
\sum_{j=t}^{\infty}a_j\rho^j.
\]

Multiplication by \(\beta^t\) yields (5) and (4).

The nonnegative weights

\[
\frac cN\rho^j
\]

sum to one because

\[
\frac cN\sum_{j=0}^{\infty}\rho^j
=
\frac{c/N}{1-M/N}
=1.
\]

Therefore

\[
x_t
=
\sum_{j=0}^{\infty}
\left(\frac cN\rho^j\right)
\frac{a_{t+j}}c
\]

is a convex combination of the normalized digits \(a/c\). This proves (6).

Equation (7) follows immediately from (5) and integrality of \(q_t\). Reducing an interval of length \(\Delta(A)\) modulo one produces a circular arc, possibly wrapping through zero, of circular length at most \(\min\{1,\Delta(A)\}\). This proves (8) and (9).

For a collision chart in `T-0008`,

\[
A=\{v-u_i\},
\qquad
u_i=M-r_i.
\]

Thus

\[
\operatorname{diam}A
=
\operatorname{diam}\{u_i\}
=
\operatorname{diam}\{r_i\}
=
\operatorname{diam}D,
\]

which proves (10).

Finally, substituting \(q_t=\widetilde q_t+z\) into (1) gives

\[
N\widetilde q_t
=M\widetilde q_{t+1}+(a_t-cz).
\]

The corresponding real error is translated by \(-z\), and (12) puts it in \([-1/2,1/2]\). Equation (13) follows. ∎

## Motivation

The earlier collision program measured branch count, finite difference intervals, and small-modulus projection. This theorem identifies a separate global quantity:

\[
\Delta=\frac{\text{alphabet diameter}}{\text{radix gap}}.
\]

An infinite ordinary return orbit in a chart with \(\Delta\ll1\) would force all fractional parts of one real exponential sequence \(C(N/M)^t\) into an extremely short fixed arc. This is a severe global synchronization demand that is invisible in raw branch cardinality.

The theorem also shows that the signed rational-base quotient is a controlled-rounding process. Negative-template alphabets should therefore be evaluated simultaneously by:

- symbolic branching;
- 2-adic correction power;
- normalized real aspect ratio;
- and compatibility with renewal or multi-target return grammars.

## Dependency audit

- `T-0008` supplies the signed return equation and identifies alphabet diameter with the collision offset diameter.
- The proof otherwise uses only a convergent geometric series and convexity.

## Gap audit

- Fractional-window confinement is necessary, not sufficient.
- A tiny window does not prove nonexistence; special real numbers can have exceptional multiplicative orbits.
- A wide window does not prove an ordinary 2-adic starting value exists.
- Multi-chart systems have a nonstationary sequence of ratios and require a graph-directed extension of this theorem.

## Adversarial tests

`X-0006` checks the finite recurrence and error decomposition numerically with exact rational truncations for recorded charts, and reports their exact aspect ratios.

## Remaining uncertainty

The finite theorem appears complete. The next challenge is to derive construction or obstruction criteria for graph-directed windows rather than one stationary chart.

## Suggested next attack

Search for collision or return systems with macroscopic aspect ratio, or for multi-chart cycles whose graph-directed real windows overlap enough to support a finite-state rounding controller while the 2-adic boundary remains ordinary and finite.
