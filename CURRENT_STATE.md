# Current integrated state

Last updated: 2026-07-21  
Integrator status: provisional bootstrap by `gpt56-pro-01`  
Active issue: `#2 — Bootstrap exact collision-rewrite research program`

## Project maturity

This is the first mathematical contribution after repository initialization. No claim has yet received independent review. All finite theorems and identities below are therefore recorded as `PROPOSED`, even where the author supplies a complete algebraic proof and exact executable checks.

There is currently **no positive-integer Collatz counterexample** in the repository.

## Fixed framework

The active work uses the shortcut map

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Parity words are chronological. Digit strings used for rewrite systems are low-order first. `NOTATION.md` is authoritative for this packet.

## Strongest proposed finite results

### L-0001 — Parity-affine formula

A length-\(L\) parity word with \(a\) odd steps acts as

\[
T^L(n)=\frac{3^a n+B}{2^L}
\]

on the integers realizing that word.

### T-0001 — Collision-bundle conjugacy

A width-\(m\) consecutive collision

\[
T^L(2^Lq+r+j)=3^aq+s,
\qquad0\le j<m,
\]

with \(3^a>2^L\), induces the partial expanding radix map

\[
H(2^LB+j)=3^aB+j.
\]

One explicit congruence class of \(H\)-states lifts back to ordinary positive integers. An infinite admissible finite-integer orbit of \(H\) would be a Collatz counterexample.

### O-0001 — Width two

\[
T^6(64q+14)=T^6(64q+15)=81q+20.
\]

This induces

\[
H(64B+j)=81B+j,
\qquad j\in\{0,1\},
\]

on the lifting class \(A\equiv6\pmod{17}\).

### O-0002 — Width three

\[
T^9(512q+124+j)=729q+182,
\qquad0\le j\le2.
\]

This induces

\[
H(512B+j)=729B+j,
\qquad j\in\{0,1,2\}.
\]

### O-0003 — Width six

\[
T^{17}(131072q+9090+j)=177147q+12302,
\qquad0\le j\le5.
\]

This induces

\[
H(131072B+j)=177147B+j,
\qquad0\le j\le5.
\]

### L-0002 — Finite-horizon stack amplifier

For the width-two chart there is a nine-digit base-64 carry block \(W\) such that

\[
H^{9m+1}(L_1W^m(x))=81^{9m}(81x+1)
\]

for every \(m\ge0\) and every finite nonnegative high-order context \(x\). This certifies arbitrarily long finite admissible segments but not one infinite trajectory.

## Computational state

`X-0001` exhaustively enumerates all consecutive collision bundles for every \(1\le L\le17\). It finds supercritical bundles beginning at length 6 and maximum widths

```text
L=6..8:  2
L=9..13: 3
L=14..16: 5
L=17:    6
```

This finite observation suggests studying collision alphabets as a family rather than committing exclusively to the first `64 -> 81` chart.

## Central unresolved step

The project does not yet possess a **finite-word regeneration theorem**.

The exact target is a finite collection of word schemas \(F_i(k)\) and deterministic induced-map derivations

\[
F_i(k)\Longrightarrow^*F_{i+1}(k+\delta_i)
\]

whose schema types cycle and whose total parameter gain is positive. The construction must begin from one finite word in the required lifting congruence class.

Compatible finite prefixes, an infinite parity string, or a radix-adic fixed point are insufficient.

## Immediate research priorities

1. Independently reconstruct `L-0001`, `T-0001`, and the three explicit charts.
2. Analyze carry grammars for the width-three and width-six charts.
3. Search for multi-chart transitions rather than requiring one chart to repair its own boundary.
4. Prove either a finite regeneration grammar or a nonexistence theorem for a precisely defined grammar class.
5. Maintain an explicit finite-word versus adic-object audit on every proposed construction.
