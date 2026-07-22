# D-8701 — Centered forced-tail transition system

**Claim ID:** `D-8701`  
**Type:** definition / exact construction  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-pdr-01`  
**Issue:** #40  
**Created:** 2026-07-22  
**Dependencies:** independently verified `ADEL/L-9313`, `ADEL/L-9314` from draft review PR #37  
**Scope:** eventual-zero appended-block tails in the ordinary `64 -> 81` centered system

## State and exact transition

A state is a pair

\[
(B,e)\in\mathbb Z_{\ge0}\times\{0,1\}.
\]

It represents a nearest integer `B` and the current binary centered-error sign digit `e`. Once the appended nearest-integer cylinder block is zero, one further zero block requires an integer `B'` and a digit `e'` satisfying

\[
\boxed{64B'=81B+e-e'.}
\tag{1}
\]

For a fixed state, at most one choice of `e'` is possible. Reducing `(1)` modulo `64` gives the complete table

| `e` | `B mod 64` | `e'` | legal update |
|---:|---:|---:|---|
| 0 | 0 | 0 | `B'=81(B/64)` |
| 0 | 49 | 1 | `B'=81((B-49)/64)+62` |
| 1 | 0 | 1 | `B'=81(B/64)` |
| 1 | 15 | 0 | `B'=81((B-15)/64)+19` |

Every other state fails immediately.

Writing `B=r+64Q`, the partial deterministic map is therefore

```text
r=0  : (B,e) -> (81Q,e)
r=15 : (B,1) -> (81Q+19,0)
r=49 : (B,0) -> (81Q+62,1).
```

## Base-64 bounded-carry transducer

Let

\[
Q=\sum_{j\ge0}a_j64^j,
\qquad 0\le a_j<64,
\]

with only finitely many nonzero digits. For an offset

\[
c\in\{0,19,62\},
\]

the update computes

\[
81Q+c=(64+17)Q+c.
\]

Put `a_{-1}=0` and initialize `k_0=c`. The output digit and next carry are

\[
\boxed{
\begin{aligned}
w_j&=17a_j+a_{j-1}+k_j,\\
b_j&=w_j\bmod64,\\
k_{j+1}&=\lfloor w_j/64\rfloor.
\end{aligned}}
\tag{2}
\]

After the first column,

\[
0\le k_j\le17.
\]

Thus the exact word update is a finite sequential transducer with bounded carry and one previous-input-digit register. Canonical finiteness of the ordinary integer is a separate top-boundary condition; an infinite base-64 stream is only a `2`-adic object.

## Ordinary witness obligation

A genuine positive witness in this system must provide one explicit finite `B_0>0`, one initial digit `e_0`, and a proof that `(1)` is legal for every time. Then

\[
A_n=64B_n+e_n
\]

is a positive ordinary orbit of the induced `64 -> 81` chart. Translation into a Collatz counterexample additionally requires the chart-class and physical-replay interface from umbrella issue #4 to be independently checked.

## Boundary

- A finite modular path is not an ordinary infinite orbit.
- A cycle in a residue abstraction is not an integer lasso.
- A compatible infinite low-digit stream may define only a nonordinary element of `Z_2`.
- No counterexample is asserted by this definition.
