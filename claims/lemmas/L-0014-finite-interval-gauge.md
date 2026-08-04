# L-0014 — Collatz as finite-interval renormalization

Claim ID: `L-0014`  
Title: Exact finite-interval lift, gauge freedom, and canonical fixed and diagonal gauges  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0001`, `L-0013`  
Scope: exact ordinary-integer interval representation of every shortcut-Collatz step  
Related counterexample candidates: none

## Statement

Let

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Fix integers

\[
n>0,
\qquad
v\ge1,
\qquad
q=v+n,
\]

and represent the physical state \(n\) by the finite half-open integer interval

\[
I=[v,q),
\qquad |I|=q-v=n.
\]

Put

\[
e=n\bmod2.
\]

Define two interval renormalizations:

\[
\boxed{
\mathcal R_0([v,q))
=
\left[
\left\lceil\frac v2\right\rceil,
\left\lceil\frac q2\right\rceil
\right),
}
\tag{1}
\]

and

\[
\boxed{
\mathcal R_1([v,q))
=
\left[
\left\lfloor\frac{3v}{2}\right\rfloor,
\left\lceil\frac{3q}{2}\right\rceil
\right).
}
\tag{2}
\]

Then:

### 1. Exact length dynamics

For \(e=n\bmod2\),

\[
\boxed{
|\mathcal R_e(I)|=T(n).
}
\tag{3}
\]

Thus shortcut Collatz is exactly the evolution of the cardinality of a finite integer interval under parity-selected contraction or outward-rounded dilation.

### 2. Exact endpoint coupling

Write

\[
\mathcal R_e([v,q))=[v',q').
\]

Then \(v'\) and \(q'\) are precisely the lower-phase and quotient endpoints of `L-0013`, and

\[
\boxed{
T(q-v)=q'-v'.
}
\tag{4}
\]

Iterating the physical parity sequence of \(n_0\) produces finite intervals

\[
I_t=[v_t,q_t)
\]

with

\[
\boxed{
|I_t|=T^t(n_0)
}
\tag{5}
\]

for every \(t\ge0\).

### 3. Gauge freedom

The initial lower endpoint \(v_0\ge1\) is arbitrary. Different choices give different finite endpoint lifts of the same physical Collatz orbit.

Two gauges are canonical.

#### Fixed gauge

If

\[
v_0=1,
\qquad q_0=n_0+1,
\]

then

\[
\boxed{
v_t=1,\qquad q_t=T^t(n_0)+1.}
\tag{6}
\]

#### Diagonal gauge

If

\[
v_0=n_0+1,
\qquad q_0=2n_0+1,
\]

then

\[
\boxed{
v_t=T^t(n_0)+1,\qquad q_t=2T^t(n_0)+1.}
\tag{7}
\]

In the diagonal gauge, the phase height \(v_t-1\) is exactly the physical Collatz state.

### 4. Ordinary-boundary criterion

Any infinite rewrite proof that begins from one finite interval \([v_0,q_0)\), applies only the exact rules (1)--(2), and proves that the interval lengths are unbounded gives a positive-integer Collatz counterexample

\[
n_0=q_0-v_0.
\]

No inverse limit, left-infinite word, or adic starting object is involved.

## Proof

### Even length

Assume \(n=q-v\) is even. Then \(q\) and \(v\) have the same parity. Therefore

\[
\left\lceil\frac q2\right\rceil
-
\left\lceil\frac v2\right\rceil
=
\frac{q-v}{2}
=
\frac n2
=T(n).
\]

This proves (3) for \(e=0\).

### Odd length

Assume \(n=q-v\) is odd. Then \(q\) and \(v\) have opposite parity. Checking the two possible parities of \(v\) gives

\[
\left\lceil\frac{3q}{2}\right\rceil
-
\left\lfloor\frac{3v}{2}\right\rfloor
=
\frac{3(q-v)+1}{2}
=
\frac{3n+1}{2}
=T(n).
\]

This proves (3) for \(e=1\).

The lower endpoints in (1)--(2) are exactly

\[
S_0(v)=\left\lceil\frac v2\right\rceil,
\qquad
S_1(v)=\left\lfloor\frac{3v}{2}\right\rfloor
\]

from `L-0013`. The upper endpoints equal the corresponding quotient updates because the parity relation \(q-v\equiv e\pmod2\) supplies the required rounding. Hence (4) holds, and induction proves (5).

For the fixed gauge, both lower branches fix \(v=1\):

\[
\left\lceil\frac12\right\rceil
=
\left\lfloor\frac32\right\rfloor
=1.
\]

Equation (5) then gives (6).

For the diagonal gauge, suppose \(v=n+1\) and \(q=2n+1\). If \(n\) is even,

\[
\left\lceil\frac{n+1}{2}\right\rceil
=
\frac n2+1
=T(n)+1,
\]

while if \(n\) is odd,

\[
\left\lfloor\frac{3(n+1)}{2}\right\rfloor
=
\frac{3n+3}{2}
=T(n)+1.
\]

The upper endpoint is then twice the new length plus one, proving (7). The ordinary-boundary criterion follows directly from (5). ∎

## Interpretation

The moving negative phase is a **gauge choice for the lower endpoint of a finite interval**. The physical Collatz value is the interval length.

This clarifies both the power and the limitation of phase methods:

- a negative-cycle gauge may expose finite return structure;
- the fixed gauge removes the phase entirely;
- the diagonal gauge makes phase escape identical to physical Collatz escape;
- phase growth by itself is not gauge invariant.

The useful object is therefore not an unqualified growing phase, but a finite endpoint grammar whose interval length follows deterministic Collatz dynamics.

## Gap audit

- The lemma is an exact reformulation, not a counterexample construction.
- A phase-escape statement in one gauge need not imply physical growth unless the interval length is also controlled.
- A successful interval grammar must keep both endpoints finite and prove the parity-selected rule indefinitely.

## Adversarial tests

`X-0010` checks (1)--(7) for a large finite range of interval lengths and gauges and verifies direct agreement with the shortcut map.

## Suggested next attack

Design string rewrites on **decorated finite intervals**, carrying both endpoint words and a finite boundary marker. Negative-cycle gauges can simplify the lower endpoint, while the upper endpoint and interval length certify that the starting object is one ordinary positive integer.