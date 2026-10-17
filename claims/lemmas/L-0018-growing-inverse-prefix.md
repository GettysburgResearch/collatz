# L-0018 — Growing inverse-power prefixes require unbounded memory

Claim ID: `L-0018`  
Title: Exact order obstruction to fixed-period control of all-height tower connector prefixes  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Dependencies: `L-0017`  
External infrastructure: 2-adic lifting-the-exponent; PR #13 `LIT-KTHM-0003` is a nearby recorded instance  
Scope: inverse odd multipliers modulo growing powers of two  
Related counterexample candidates: none

## Statement

Fix integers

\[
K_0\ge3,
\qquad
\ell\ge1,
\qquad
G_0\ge0,
\]

and an odd positive integer \(a\). Put

\[
K_t=K_0+\ell t,
\qquad
G_t=G_0+at.
\tag{1}
\]

Let \(\xi_t\) be the least nonnegative residue modulo \(2^{K_t}\) satisfying

\[
\boxed{
3^{G_t}\xi_t\equiv1\pmod{2^{K_t}}.
}
\tag{2}
\]

Then:

### 1. Exact order

For every \(K\ge3\),

\[
\boxed{
\operatorname{ord}_{2^K}(3^a)=2^{K-2}.
}
\tag{3}
\]

### 2. No fixed counter period at growing precision

For every fixed integer \(P\ge1\), there is a threshold \(t_P\) such that, for all \(t\ge t_P\),

\[
\boxed{
\xi_{t+P}\not\equiv\xi_t\pmod{2^{K_t}}.
}
\tag{4}
\]

More explicitly, equality in (4) could hold only when

\[
2^{K_t-2}\mid P.
\tag{5}
\]

Since \(K_t\to\infty\), no fixed \(P\) satisfies this at all heights.

### 3. Consequence for tower connectors

The connector seed in `L-0017` is obtained by multiplying a required residue difference by an inverse power

\[
3^{-G_t}\pmod{2^{\bar K}}.
\]

When the next tower depth \(\bar K\) grows with the padding counter, its exact low binary prefix cannot in general be supplied by a table depending only on \(t\) modulo one fixed period.

The local recovery residue \(\mu_t\) of `L-0016` is periodic because its precision \(r+1\) is fixed. The all-height connector is qualitatively different because its required precision grows without bound.

This is an obstruction only to **fixed-period finite residue control**. A stack, an explicit growing word, or another unbounded arithmetic register can still carry the prefixes.

## Proof

Because \(a\) is odd,

\[
3^a\equiv3\pmod8.
\]

If \(n\) is odd, then

\[
3^{an}\equiv3\pmod4,
\]

so

\[
\nu_2(3^{an}-1)=1.
\]

If \(n\) is even, the 2-adic lifting-the-exponent formula gives

\[
\begin{aligned}
\nu_2(3^{an}-1)
&=\nu_2(3^a-1)+\nu_2(3^a+1)+\nu_2(n)-1\\
&=1+2+\nu_2(n)-1\\
&=2+\nu_2(n).
\end{aligned}
\tag{6}
\]

Therefore

\[
3^{an}\equiv1\pmod{2^K}
\]

holds exactly when

\[
\nu_2(n)\ge K-2.
\]

The least positive such \(n\) is \(2^{K-2}\), proving (3).

Now suppose

\[
\xi_{t+P}\equiv\xi_t\pmod{2^{K_t}}.
\]

By definition,

\[
\xi_t\equiv3^{-G_t}\pmod{2^{K_t}}
\]

and

\[
\xi_{t+P}\equiv3^{-G_t-aP}\pmod{2^{K_t}}.
\]

Equality implies

\[
3^{aP}\equiv1\pmod{2^{K_t}}.
\]

By (3),

\[
2^{K_t-2}\mid P.
\]

For fixed \(P\), this is impossible once

\[
K_t>\nu_2(P)+2.
\]

This proves (4)--(5). ∎

## Interpretation

One padded mismatch edge has a small periodic finite core because it asks for only \(r+1\) recovery bits. Chaining into a next tower of height proportional to \(t\) asks for an inverse odd multiplier at proportional precision. The period of that inverse obligation is exponential in the requested precision.

Hence the state proposal

\[
(i,t,\rho,n)
\]

must not treat \(\rho\) as a fixed finite residue label if it is intended to encode the entire next connector. The construction needs an actual growing prefix word, stack, or equivalent arithmetic register.

## Dependency audit

- The proof is elementary LTE and does not depend on a conjectural Collatz claim.
- `L-0017` explains where the inverse powers enter the connector seed.
- PR #13 records the same order-lifting mechanism for the special base \(81\) modulo powers of two.

## Gap audit

- Nonperiodicity does not rule out a pushdown or counter transducer that computes the prefixes.
- The lemma does not prove that every connector seed has maximal order; extra even factors in its residue difference can lower the required precision.
- It is not a nonexistence theorem for counter-stack grammars.

## Adversarial tests

`X-0012` verifies

\[
\operatorname{ord}_{2^K}(3)=2^{K-2}
\]

through \(K=63\), and checks that no period below \(2^{12}\) survives a suitably larger requested precision.

## Suggested next attack

Represent the inverse-prefix obligation itself as a growing LSD-first stack word. Division by the fixed odd number \(3^a\) is a finite carry transduction; the missing theorem is a self-regenerating coupling between that word and the ordinary marked Collatz tail.