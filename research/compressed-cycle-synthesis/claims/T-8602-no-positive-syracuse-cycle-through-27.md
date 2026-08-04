# T-8602 — Exact exclusion of positive Syracuse cycles through 27 odd terms

**Claim ID:** `T-8602`  
**Title:** No nontrivial positive Syracuse cycle has at most 27 odd terms  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cycle-01`  
**Reviewing agents:** none  
**Created:** 2026-07-22  
**Dependencies:** the exact cycle equation and product formula of `L-9905`; exact computation `X-8601`  
**Scope:** positive cycles of the accelerated odd Syracuse map, counted by odd terms `m`  
**Related counterexample candidates:** none

## Statement

For the accelerated odd map

\[
S(x)=\frac{3x+1}{2^{\nu_2(3x+1)}}
\qquad(x\text{ positive and odd}),
\]

there is no nontrivial positive cycle with

\[
2\le m\le27
\]

odd terms.

The finite computation checks exactly 24 admissible `(m,K)` windows and

\[
\boxed{802,459,998,516}
\]

positive exponent compositions. No composition even satisfies the necessary cycle divisibility congruence.

## Definitions

For a putative cycle, write its exact valuation word as

\[
a=(a_1,\ldots,a_m),
\qquad a_i\ge1,
\qquad K=\sum_i a_i,
\]

and partial sums `A_0=0`, `A_i=a_1+...+a_i`. Put

\[
C(a)=\sum_{i=1}^{m}3^{m-i}2^{A_{i-1}},
\qquad
D_{m,K}=2^K-3^m.
\]

The cycle equation is

\[
x_1D_{m,K}=C(a).
\]

Thus a necessary condition is

\[
C(a)\equiv0\pmod{D_{m,K}}.
\]

## Proof

### 1. Exact finite `(m,K)` windows

In a nontrivial positive cycle the least odd element satisfies `x_min>=7`:

- `x_min=1` puts the orbit in the trivial cycle;
- `S(3)=5` and `S(5)=1`, so neither `3` nor `5` can be the least element of a nontrivial cycle.

The cycle product formula gives

\[
3^m<2^K\le\left(3+\frac1{x_{\min}}\right)^m
\le\left(\frac{22}{7}\right)^m.
\]

Therefore every candidate pair is selected by the two exact integer inequalities

\[
3^m<2^K,
\qquad
2^K7^m\le22^m.
\]

`X-8601` evaluates these inequalities with ordinary integer arithmetic. It does not choose windows with floating-point logarithms.

### 2. Exact affine monoid

For a finite valuation word `w`, store

\[
M(w)=(m_w,K_w,C_w)
\]

with

\[
2^{K_w}S^{m_w}(x)=3^{m_w}x+C_w.
\]

Concatenation satisfies

\[
\boxed{
C(uv)=3^{m_v}C(u)+2^{K_u}C(v).
}
\]

This follows by substituting the affine formula for `u` into the formula for `v`.

### 3. Meet-in-the-middle equivalence

For one fixed pair `(m,K)`, split a composition uniquely as `a=uv` with lengths

\[
h=\lfloor m/2\rfloor,
\qquad
\ell=m-h.
\]

Since `D_{m,K}` is odd, `2^{K_u}` is invertible modulo `D_{m,K}`. The cycle congruence is equivalent to

\[
C(v)
\equiv
-3^\ell C(u)\,2^{-K_u}
\pmod{D_{m,K}}.
\]

The program enumerates every positive left composition, stores the required right residue grouped by `K_u`, sorts those residues, and enumerates every positive right composition. Every full positive composition appears in exactly one left/right pair, and a match occurs exactly when its `C(a)` is divisible by `D_{m,K}`.

### 4. Frozen exhaustive result

The canonical output records 24 nonempty windows through `m=27`. Their total number of compositions is

\[
\sum_{(m,K)}\binom{K-1}{m-1}
=802,459,998,516.
\]

The number of modular matches is exactly zero. Therefore no candidate produces an integer `x_1`, and a fortiori none can replay the requested exact valuations or close to a positive cycle. ∎

## Verification

Run

```bash
g++ -O3 -std=c++17 -Wall -Wextra run.cpp -o run
./run 27
python3 verify.py
```

under `experiments/X-8601-cycle-window-exhaustion/`.

The independent Python verifier directly enumerates the trivial positive control `(m,K)=(1,2)` and the forced windows through `m=14`; it recovers only `x=1` in the control and agrees that every nontrivial window is empty.

## Dependency audit

- The only mathematical cycle input is the exact affine cycle equation and product formula.
- The finite upper window uses the elementary `x_min>=7` argument written above.
- The exclusion itself is the zero-match exhaustive certificate in `X-8601`.

## Gap audit

- The parameter `m` is the number of accelerated odd terms, not the number of local minima used in some external cycle bounds.
- The theorem says nothing about `m>=28`.
- A zero divisibility count is stronger than a failed trajectory search but remains a bounded theorem.
- No conclusion about divergent orbits follows.

## Remaining uncertainty

The code and proof of exhaustive coverage have not yet received an independent repository review.
