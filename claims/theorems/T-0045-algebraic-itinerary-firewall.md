# T-0045 — Algebraic-itinerary firewall for the supercritical six-branch chart

Claim ID: `T-0045`  
Title: Every positive ordinary six-branch survivor has a transcendental digit generating function  
Status: `PROPOSED / SOURCE-QUALIFIED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-26  
Dependencies: Fatou's bounded-integral-coefficient theorem as audited by the literature program; elementary periodic affine coding  
Scope: the stationary six-branch chart with multiplier `3^12/2^19`  
Related counterexample candidates: none

## Setup

Use

\[
P=3^{12},
\qquad
Q=2^{19},
\qquad
P>Q,
\tag{1}
\]

and the six positive digits

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\}.
\tag{2}
\]

An all-time legal ordinary orbit obeys

\[
\boxed{Qx_{n+1}=Px_n+a_n,}
\qquad
x_n\in\mathbb Z_{>0},
\quad
 a_n\in\mathcal A.
\tag{3}
\]

Define the digit generating function

\[
\boxed{A(z)=\sum_{n\ge0}a_nz^n.}
\tag{4}
\]

Equivalently, label the six digits by indices \(i_n\in\{0,\ldots,5\}\) and define

\[
I(z)=\sum_{n\ge0}i_nz^n.
\tag{5}
\]

## Theorem

If a positive ordinary orbit (3) is legal for every \(n\), then both \(A(z)\) and \(I(z)\) are transcendental over \(\mathbb Q(z)\).

Consequently no eventually algebraic, context-free-algebraic, or finite-algebraic generating-function directive can produce a positive six-branch survivor.

## 1. Algebraic bounded-coefficient series are rational

Fatou's theorem in the bounded integral-coefficient form states:

> A power series with coefficients in a finite subset of \(\mathbb Z\), algebraic over \(\mathbb Q(z)\), is rational.

Both coefficient sequences in (4)--(5) take values in finite integer sets. Hence algebraicity of either generating function would imply rationality.

A rational generating function gives an eventual linear recurrence. Since the coefficients themselves range over a finite set, the finite recurrence state eventually repeats. Therefore the coefficient sequence is eventually periodic.

Thus it remains only to exclude every eventually periodic legal digit itinerary.

## 2. Purely periodic tails have a unique negative completion

Suppose that from some time onward the digits repeat a word

\[
w=(b_0,\ldots,b_{L-1})
\in\mathcal A^L.
\]

One complete period has the affine form

\[
\boxed{
Q^L y^+
=P^L y+C_w,}
\tag{6}
\]

where

\[
\boxed{
C_w=
\sum_{j=0}^{L-1}
P^{L-1-j}Q^j b_j>0.}
\tag{7}
\]

The periodic coding point is

\[
\boxed{
y_*={C_w\over Q^L-P^L}<0,}
\tag{8}
\]

because \(P>Q\).

We now prove that it is the only \(2\)-adic point realizing the periodic tail. The denominator \(P^L-Q^L\) is odd, so \(y_*\in\mathbb Z_2\). If another \(y\in\mathbb Z_2\) realizes every repetition of the same period, subtracting (6) at the fixed point gives

\[
y_m-y_*
=
\left({P^L\over Q^L}\right)^m(y-y_*).
\tag{9}
\]

Every \(y_m-y_*\) lies in \(\mathbb Z_2\). But the right side has valuation

\[
\nu_2(y-y_*)-19Lm.
\tag{10}
\]

This remains nonnegative for every \(m\) only when

\[
\boxed{y=y_*.}
\tag{11}
\]

Hence a periodic tail has one completion and it is negative.

## 3. A finite preperiod cannot restore positivity

An inverse branch of (3) is

\[
\boxed{x={Qx^+-a\over P}.}
\tag{12}
\]

If \(x^+<0\) and \(a>0\), then the numerator in (12) is negative and therefore \(x<0\).

Starting from the negative periodic point (8), every finite preperiod pulls back to a negative rational number. Consequently no positive ordinary integer can realize an eventually periodic digit itinerary.

Combining this with Section 1 proves the theorem. ∎

## Why this is stronger than the finite-state firewall

A deterministic finite-state schedule is eventually periodic and is already excluded by the periodic/full-denominator theorem. The present result excludes every digit sequence whose ordinary generating function is algebraic, even when it is not presented by a finite-state generator.

Thus two broad finite descriptions are now closed independently:

```text
finite algebraic state-section nucleus:  T-0044;
algebraic digit generating function:     T-0045.
```

Any positive survivor must have both genuinely unbounded arithmetic state and a transcendental itinerary series.

## Relationship to full-denominator divisibility

If \(P<Q\), equation (8) is positive and is an ordinary integer exactly when the full denominator \(Q^L-P^L\) divides \(C_w\); this is the positive-cycle funnel.

Here \(P>Q\), so every periodic schedule has negative realization before divisibility is even considered. This is the supercritical schedule firewall.

## Source qualification

The only external input is Fatou's bounded-integral-coefficient algebraic-series theorem. The literature branch has audited the surrounding Fatou--Pólya framework, but this exact application should be checked against the preferred primary-source normalization before promotion.

The periodic-tail uniqueness and sign argument are proved completely here.

## Gap audit

- Transcendence of the itinerary generating function does not imply existence or nonexistence of a survivor.
- Highly aperiodic, transcendental, unbounded-state directives remain possible.
- The theorem concerns one strict six-branch chart, not all Collatz trajectories.
- No ordinary survivor or counterexample is claimed.
