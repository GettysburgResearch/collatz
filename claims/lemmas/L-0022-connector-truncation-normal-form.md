# L-0022 — Connector seeds have one inverse-prefix stream and a bounded top digit

Claim ID: `L-0022`  
Title: Truncation normal form for every cycle-tower connector seed  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Dependencies: `L-0016`, `L-0017`, `L-0019`  
Scope: connectors among cycle-padded mismatch towers  
Related counterexample candidates: none

## Statement

Let a source tower instance have data

\[
(B,G,g,r,b,\mu)
\]

from `L-0016`. Define its normalized 2-adic prefix

\[
\boxed{
\omega=
\frac{\mu+3^{-g}}{2^{r+1}}
\in\mathbb Z_2.
}
\tag{1}

Let a target tower instance have binary anchor

\[
\bar A=2^{\bar k}\bar\mu
\]

and total binary depth

\[
\bar K=\bar k+\bar r+1,
\]

where

\[
0\le\bar\mu<2^{\bar r+1}.
\]

Let \(\eta\) be the canonical connector seed from source to target:

\[
B+3^G\eta
\equiv
\bar A
\pmod{2^{\bar K}},
\qquad
0\le\eta<2^{\bar K}.
\tag{2}

For every \(k\ge0\), write

\[
[\!-\omega\!]_k
\]

for the least nonnegative residue of \(-\omega\) modulo \(2^k\).

Then:

### 1. Exact long-prefix identity

\[
\boxed{
\eta
\equiv
-\omega
\pmod{2^{\bar k}}.
}
\tag{3}

Thus the first \(\bar k\) LSD-first bits of the connector seed depend only on the source tower instance and on the requested truncation length. They are independent of the target tower type.

### 2. Bounded target digit

There is a unique digit

\[
0\le d<2^{\bar r+1}
\]

such that

\[
\boxed{
\eta
=
[\!-\omega\!]_{\bar k}
+2^{\bar k}d.
}
\tag{4}

The target dependence is confined to the final \(\bar r+1\) high bits of the connector block.

For the four phase-34 self-return tower types of the negative eleven-cycle,

\[
\bar r+1\in\{6,5,4,3\}.
\]

Hence every connector seed, however deep, consists of:

1. one source inverse-prefix word of length \(\bar k\); and
2. at most six target-control bits.

### 3. Exact source rational

The normalized prefix is the rational 2-adic number

\[
\boxed{
\omega
=
\frac{c}{3^g},
}
\tag{5}

where

\[
c=rac{3^g\mu+1}{2^{r+1}}
\]

is the finite integer from `L-0016`.

Equivalently,

\[
\boxed{
[\!-\omega\!]_{\bar k}
=
\left[-c\,3^{-g}\right]_{\bar k}.
}
\tag{6}

The unbounded connector language is therefore one family of truncated inverse powers of three, with a bounded target cap.

### 4. Stage-boundary rational limit

For one fixed tower type, take source heights

\[
t=2^m.
\]

For all sufficiently large \(m\), the finite recovery residue \(\mu_t\) is constant; call it \(\mu_*\). Put

\[
g_t=g_0+7\,2^m.
\]

Then in \(\mathbb Z_2\),

\[
\boxed{
\omega_{2^m}
\longrightarrow
\omega_\infty
=
\frac{\mu_*+3^{-g_0}}{2^{r+1}}.
}
\tag{7}

Moreover

\[
\nu_2(\omega_{2^{m+1}}-\omega_{2^m})=m-r+1
\]

by `L-0021`. Thus the stage-boundary inverse-prefix stream converges to an explicit rational 2-adic number at exactly one new certified bit per stage.

Its binary digits are eventually periodic because its denominator is odd.

## Proof

The connector congruence (2), reduced modulo \(2^{\bar k}\), loses the target anchor:

\[
\bar A=2^{\bar k}\bar\mu
\equiv0
\pmod{2^{\bar k}}.
\]

Therefore

\[
3^G\eta\equiv-B\pmod{2^{\bar k}}.
\]

Since

\[
B
=
3^b\frac{3^g\mu+1}{2^{r+1}}
\]

and

\[
G=g+b,
\]

we have in \(\mathbb Z_2\)

\[
\begin{aligned}
B3^{-G}
&=
3^b\frac{3^g\mu+1}{2^{r+1}}3^{-g-b}\\
&=
\frac{\mu+3^{-g}}{2^{r+1}}\\
&=\omega.
\end{aligned}
\]

Multiplying the connector congruence by \(3^{-G}\) proves (3).

Because

\[
0\le\eta<2^{\bar k+\bar r+1},
\]

Euclidean division by \(2^{\bar k}\) gives one digit

\[
0\le d<2^{\bar r+1}
\]

and one remainder below \(2^{\bar k}\). Equation (3) identifies that remainder with

\[
[\!-\omega\!]_{\bar k},
\]

proving (4).

Equation (5) is the same algebra:

\[
\omega
=
\frac{\mu+3^{-g}}{2^{r+1}}
=
\frac{3^g\mu+1}{2^{r+1}3^g}
=
\frac c{3^g}.
\]

For the limit, powers \(2^m\) are eventually divisible by the finite period of \(\mu_t\), so \(\mu_{2^m}=\mu_*\). Also

\[
3^{-7\,2^m}\longrightarrow1
\]

in \(\mathbb Z_2\), since

\[
\nu_2(3^{7\,2^m}-1)=m+2\longrightarrow\infty.
\]

Therefore

\[
3^{-g_t}
=3^{-g_0}3^{-7\,2^m}
\longrightarrow3^{-g_0},
\]

which proves (7). A rational number with odd denominator has an eventually periodic base-two expansion by the finite remainder algorithm. ∎

## Interpretation

The target graph does not create an unbounded collection of unrelated connector words. Once a source tower instance is fixed, every possible deep target reads a longer prefix of the same inverse-power stream. Only a bounded high digit identifies the target type.

This isolates the true stack object:

\[
\boxed{
W_{t,k}
=
[\!-c_t3^{-g_t}\!]_k.
}
\]

A future grammar should manipulate this word directly. Finite target-phase control supplies at most six additional bits and is no longer the main obstacle.

## Caution about the rational limit

The stage-boundary limit \(\omega_\infty\) is a completion object. Its eventual periodicity does not supply a positive-integer counterexample.

However a forward rule that starts with a finite prefix and appends its periodic digits one stage at a time would remain an ordinary finite stack at every time. The missing burden is to prove that the actual Collatz connector output performs that append operation.

## Dependency audit

- `L-0016` supplies the exact block parameters.
- `L-0017` supplies the connector equation.
- `L-0019` introduced \(\omega\).
- The stage limit uses only LTE.

## Gap audit

- The target cap is bounded, but the source inverse-power prefix still has length linear in the tower height.
- Eventual periodicity of the stage-boundary limit controls only the slowly stabilizing low end, not the entire current connector word.
- No forward self-regeneration is proved.

## Adversarial tests

`X-0012` verifies (3)--(6) for all 1,024 connector families in its census and verifies the stage-boundary valuation law from `L-0021`.

## Suggested next attack

Build an LSD-first transducer for the truncated inverse stream

\[
-c_t3^{-g_t}\pmod{2^k}
\]

under one stage update. The finite phase state supplies the bounded top digit; the stack must carry the inverse prefix and the distinguished ordinary marker.