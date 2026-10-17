# L-0021 — Binary-odometer law inside one Hensel stage

Claim ID: `L-0021`  
Title: Exact valuation profile of the 128 connector prefixes in a dyadic Hensel stage  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Dependencies: `L-0019`, `L-0020`  
Scope: each phase-34 self-return tower type of the negative eleven-cycle  
Related counterexample candidates: none

## Statement

Fix one of the four phase-34 self-return tower types, with recovery depth \(r\). For \(m\) sufficiently large, use the stage heights

\[
t_{m,j}=2^m+j2^{m-7},
\qquad
0\le j\le128,
\tag{1}
\]

from `L-0020`. Put

\[
H_m=m-r-6
\tag{2}
\]

and let

\[
\omega_{m,j}=\omega_{t_{m,j}}
\]

be the normalized 2-adic connector prefix of `L-0019`.

Then:

### 1. Exact within-stage valuation law

For every

\[
1\le j\le128,
\]

\[
\boxed{
\nu_2(\omega_{m,j}-\omega_{m,0})
=H_m+\nu_2(j).
}
\tag{3}

Thus the first \(H_m\) low bits remain fixed throughout the stage, while the next seven bits evolve with the exact carry profile of the binary counter

\[
0,1,2,\ldots,128.
\]

### 2. Stage-overflow precision

At the stage boundary,

\[
t_{m,128}=t_{m+1,0},
\]

and

\[
\boxed{
\nu_2(\omega_{m+1,0}-\omega_{m,0})
=m-r+1.
}
\tag{4}

Define

\[
J_m=m-r+1.
\tag{5}
\]

Then

\[
\boxed{
\omega_{m+1,0}
\equiv
\omega_{m,0}
\pmod{2^{J_m}},
}
\tag{6}

but the congruence fails modulo \(2^{J_m+1}\).

Since

\[
J_{m+1}=J_m+1,
\]

the stage-boundary sequence certifies exactly one additional limit bit at each scale doubling.

### 3. Actual connector-seed odometer

Let \(\eta_{m,j}\) denote the canonical connector seed from tower instance \(t_{m,j}\) to \(t_{m,j+1}\) for \(0\le j<128\). Let \(\eta_{m+1,0}\) be the first seed of the next stage.

For all precisions occurring below, the target anchors are divisible by the required powers of two, so

\[
\eta_{m,j}
\equiv
-\omega_{m,j}
\]

at that precision. Consequently,

\[
\boxed{
\nu_2(\eta_{m,j}-\eta_{m,0})
=H_m+\nu_2(j)
}
\tag{7}

for \(1\le j<128\), and

\[
\boxed{
\nu_2(\eta_{m+1,0}-\eta_{m,0})
=J_m.
}
\tag{8}

The connector seeds themselves therefore implement a finite seven-bit carry automaton over a slowly growing immutable LSD prefix.

## Proof

The finite recovery core \(\mu_t\) has period at most 16 by `L-0016`. For sufficiently large \(m\), the stage jump

\[
\Delta_m=2^{m-7}
\]

is divisible by that period. Hence

\[
\mu_{t_{m,j}}=\mu_{t_{m,0}}
\]

for every \(j\).

Write

\[
\zeta_t=3^{-g_t},
\qquad
\omega_t=
\frac{\mu_t+\zeta_t}{2^{r+1}}.
\]

Since

\[
g_{t_{m,j}}-g_{t_{m,0}}
=7j2^{m-7},
\]

we have

\[
\omega_{m,j}-\omega_{m,0}
=
\frac{\zeta_{t_{m,0}}
\left(3^{-7j2^{m-7}}-1\right)}{2^{r+1}}.
\tag{9}
\]

The leading factor \(\zeta_{t_{m,0}}\) is a 2-adic unit. Also

\[
\nu_2(3^{-N}-1)=\nu_2(3^N-1)
\]

for every positive \(N\), because multiplication by the odd unit \(3^{-N}\) does not change valuation.

Here

\[
N=7j2^{m-7}
\]

is even. The 2-adic lifting-the-exponent formula gives

\[
\begin{aligned}
\nu_2(3^N-1)
&=\nu_2(3-1)+\nu_2(3+1)+\nu_2(N)-1\\
&=1+2+(m-7+\nu_2(j))-1\\
&=m-5+\nu_2(j).
\end{aligned}
\]

Subtracting the denominator valuation \(r+1\) in (9) proves

\[
\nu_2(\omega_{m,j}-\omega_{m,0})
=m-r-6+\nu_2(j)
=H_m+\nu_2(j),
\]

which is (3).

For \(j=128=2^7\), equation (3) gives

\[
H_m+7
=m-r+1
=J_m.
\]

This proves (4)--(6), including exact failure at the next bit.

For the connector seeds, reduce the identity of `L-0019`

\[
\eta\equiv-\omega_t
\]

modulo one bit beyond each displayed valuation. The tower input anchors contain a factor \(2^{k_t}\) with \(k_t\) much larger than \(J_m\), so no target-anchor term enters those low bits. The exact omega valuations therefore transfer unchanged to the eta differences, proving (7)--(8). ∎

## Interpretation

The finite stage control \(j\in\{0,\ldots,127\}\) is not merely a convenient enumeration. Its trailing-zero function

\[
\nu_2(j)
\]

is exactly the depth of the connector-prefix carry.

This is a literal string-rewrite architecture:

- a stable low stack prefix;
- a seven-bit finite odometer above it;
- one carry overflow per 128 steps;
- one newly certified limit bit per overflow.

The origin of the number 128 is structural:

\[
128=2^7,
\]

where seven is the number of odd phases in one circuit of the negative eleven-cycle.

## What remains

The odometer describes the required connector seeds; it does not yet prove that the forward output tail emits them from one finite marked stack. The current system still risks specifying a 2-adic limit by increasingly long prefixes.

A valid next lemma must couple the odometer carry to the canonical ternary cap

\[
0\le\theta<3^{G_t}
\]

and prove a forward substitution that produces the newly required binary bit while preserving an ordinary finite high tail.

## Dependency audit

- `L-0019` supplies the normalized prefix and connector identity.
- `L-0020` supplies the stage schedule.
- The proof uses only exact LTE.

## Gap audit

- Seven-bit finite control plus one growing prefix is still not a closed pushdown grammar.
- The stage-boundary limit remains 2-adic until generated forward from a finite stack.
- The result does not show marked-rank growth.

## Adversarial tests

`X-0012` verifies (3)--(8) for all four self-return tower types over several dyadic stages.

## Suggested next attack

Build a 128-transition stage macro that carries the seven finite odometer bits explicitly and treats the stable prefix below them as a stack. Search for a net stage rewrite of the form

\[
W\#
\longmapsto
Wb\#
\]

on a forward-generated finite stack word, with the distinguished ordinary marker transported through all 128 exact Collatz blocks.