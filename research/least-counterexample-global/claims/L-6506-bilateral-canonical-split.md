# L-6506 — Bilateral zero-lift structure across a Lane-A cusp

**Claim ID:** `L-6506`  
**Title:** A zero-rate Lane-A cusp makes a linear interval of internal orbit states simultaneously canonical from the source and endpoint directions  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-08-01  
**Dependencies:** `L-6504`; canonical start/end ray `L-6803` on PR #81; branch-qualified PR #77 divergence  
**Scope:** an actual positive ordinary all-prefix-supercritical orbit at a cusp prefix  
**Related candidates:** none

## 1. Setup

Let

\[
x_t=T^t(n)
\]

be a positive ordinary all-prefix-supercritical orbit. Fix a cusp prefix length `K` from `L-6504`, and put

\[
q_t=\#\{0\le i<t:x_i\text{ is odd}\},
\qquad
s=x_K,
\qquad
q=q_K.
\]

Thus

\[
\log s=o(K),
\qquad
q=\alpha K+o(K),
\qquad
\alpha=\frac{\log2}{\log3}.
\tag{1}
\]

For a cut `0<t<K`, let the suffix have

\[
L=K-t,
\qquad
R=q-q_t
\tag{2}
\]

steps and odd steps respectively.

## 2. Prefix canonicality

For all sufficiently large `t`, the actual prefix source and endpoint are the canonical pair:

\[
\boxed{r_{[0,t)}=n,
\qquad
s_{[0,t)}=x_t.}
\tag{3}
\]

Indeed, `2^t>n` eventually. Also the all-supercritical numerator estimate gives

\[
\frac{x_t}{3^{q_t}}
\le
\frac{n+t/2}{2^t}<1
\tag{4}
\]

for all sufficiently large `t`. Hence both actual values lie in their canonical source/end rectangles.

In particular,

\[
\boxed{x_t\le3^{q_t}.}
\tag{5}
\]

## 3. Suffix zero lift

Let `(r_{t,K},s_{t,K})` be the canonical source/end pair of the suffix word from time `t` to time `K`. Every ordinary realization of that suffix has the exact form

\[
x_t=r_{t,K}+2^L z,
\qquad
s=s_{t,K}+3^R z,
\qquad
z\in\mathbf Z_{\ge0}.
\tag{6}
\]

If

\[
\boxed{s<3^R,}
\tag{7}
\]

then the actual endpoint already belongs to the canonical endpoint interval, so uniqueness forces

\[
s=s_{t,K},
\qquad
z=0.
\]

Consequently

\[
\boxed{x_t=r_{t,K}\le2^{K-t}.}
\tag{8}
\]

Combining `(5)` and `(8)`, every cut satisfying `(7)` obeys the bilateral tent bound

\[
\boxed{
x_t\le
\min\{3^{q_t},\,2^{K-t}\}.}
\tag{9}
\]

The same ordinary state `x_t` is simultaneously the canonical endpoint of the prefix and the canonical source of the suffix.

## 4. A linear interval of bilateral cuts

Fix

\[
0<\varepsilon<\alpha.
\]

For every cut

\[
t\le(\alpha-\varepsilon)K,
\]

all-prefix supercriticality and the trivial bound `q_t<=t` give

\[
R=q-q_t
\ge\alpha K-t
\ge\varepsilon K.
\tag{10}
\]

By `(1)`,

\[
\log_3s=o(K).
\]

Therefore, for all sufficiently large cusp lengths `K`, condition `(7)` holds simultaneously for every

\[
\boxed{t_0\le t\le\lfloor(\alpha-\varepsilon)K\rfloor,}
\tag{11}
\]

where `t_0` is one fixed source-dependent prefix threshold from `(3)--(4)`.

Thus a linear number of cuts have exact zero lift in both canonical directions.

## 5. Ordinary distinctness and capacity

Branch-qualified PR #77 makes an all-prefix-supercritical positive orbit tend to `+infinity`. A deterministic orbit tending to infinity cannot repeat a state; a repetition would make it eventually periodic. Also all-prefix supercriticality gives

\[
x_t=3^{D_t}n+E_t\ge n.
\tag{12}
\]

Let

\[
I_K(\varepsilon)
=
\{t_0,\ldots,\lfloor(\alpha-\varepsilon)K\rfloor\}
\tag{13}
\]

and define the cut capacity

\[
B_t=\min\{3^{q_t},2^{K-t}\}.
\tag{14}
\]

The `x_t`, `t in I_K(epsilon)`, are distinct integers satisfying

\[
n\le x_t\le B_t.
\]

Hence, for every real `Y>=n`,

\[
\boxed{
\#\{t\in I_K(\varepsilon):B_t\le Y\}
\le\lfloor Y\rfloor-n+1.}
\tag{15}
\]

In particular,

\[
\boxed{
\max_{t\in I_K(\varepsilon)}B_t
\ge n+|I_K(\varepsilon)|-1.}
\tag{16}
\]

Equation `(15)` is a fixed-integer, two-boundary Hall-type capacity condition. It is not available for a generic inverse-limit path.

## 6. Why this is stronger than two endpoint rates

The raw cusp statement gives only

\[
r_K=n,
\qquad
s_K=\exp(o(K)).
\]

The present lemma propagates those two boundary conditions through a linear interval of internal cuts. At every such cut:

```text
prefix source lift       = 0;
prefix endpoint lift     = 0;
suffix source lift       = 0;
suffix endpoint lift     = 0.
```

The internal state is constrained by both expanding moduli at once, as in `(9)`.

## 7. Exact missing inequality

The current estimates do not make `(15)` fail: the capacities `B_t` may still be exponentially large.

A sufficient Lane-A closure is now the following single inequality. Prove that every sufficiently long all-prefix-supercritical prefix with fixed canonical source `n` and subexponential canonical endpoint has some `Y=exp(o(K))` for which

\[
\boxed{
\#\{t\in I_K(\varepsilon):
\min(3^{q_t},2^{K-t})\le Y\}
>Y-n+1.}
\tag{17}
\]

Then `(15)` gives an immediate contradiction.

Equivalently, one may prove any stronger boundary uncertainty estimate that forces too many internal canonical states into too short an ordinary interval.

## 8. Gap audit

- The suffix criterion uses the endpoint modulus `3^R`, not the full-prefix modulus `3^q`.
- The lift parameter in `(6)` is the same on the source and endpoint sides; condition `(7)` forces it to be exactly zero.
- The linear cut interval follows from `q>=alpha K`, `q_t<=t`, and `log s=o(K)`; no mixing heuristic is used.
- Distinctness is an ordinary dynamical fact, not a symbolic cylinder count.
- Equation `(15)` is exact but currently compatible with exponential capacities.
- This lemma does not exclude Lane A by itself.
