# L-0034 — Exact defect-digit expansion

Claim ID: `L-0034`  
Title: The fixed-room fractional defect is a rapidly convergent positive digit expansion whose leading digit is the current tower type  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-22  
Dependencies: `L-0031`, `T-0033`, `T-0036`  
Scope: every sufficiently late local boundary of an assumed infinite positive ordinary corrected-stage path  
Related counterexample candidates: none

## Local notation

Concatenate all tower transitions of all corrected stages into one chronological
sequence.  At local boundary `n`, let

\[
t_n\in\mathbb Z_{\ge0}
\]

be its padding height, let `i_n in {0,1,2,3}` be its tower type, and put

\[
N_n=3^{7(t_n+1)},
\qquad
T_n=2^{11(t_n+1)}.
\tag{1}
\]

The scaled ordinary boundary satisfies

\[
\boxed{
T_{n+1}W_{n+1}=N_nW_n+b_{i_n},}
\tag{2}
\]

where

\[
(b_0,b_1,b_2,b_3)=(9,54,36,24).
\tag{3}
\]

Let `H_n` be the local homogeneous scale from `T-0036`, so

\[
{H_{n+1}\over H_n}={N_n\over T_{n+1}},
\tag{4}
\]

and let

\[
\varepsilon_n=C_\infty H_n-W_n>0
\tag{5}
\]

be the fixed-room defect.

## Statement 1 — one-step defect recursion

Define

\[
\boxed{Z_n=N_n\varepsilon_n.}
\tag{6}
\]

Then

\[
\boxed{
Z_n=b_{i_n}+q_{n+1}Z_{n+1},}
\tag{7}
\]

where

\[
\boxed{
q_{n+1}={T_{n+1}\over N_{n+1}}
=\left({2048\over2187}\right)^{t_{n+1}+1}.}
\tag{8}
\]

### Proof

Insert `W_n=C_infinity H_n-epsilon_n` and the analogous expression at the next
boundary into (2).  Equation (4) cancels the homogeneous terms and leaves

\[
N_n\varepsilon_n=b_{i_n}+T_{n+1}\varepsilon_{n+1}.
\]

Substitution of (6) gives (7)--(8). ∎

## Statement 2 — exact infinite digit series

For every sufficiently late boundary,

\[
\boxed{
Z_n
=
\sum_{k=0}^{\infty}
 b_{i_{n+k}}
 \prod_{r=1}^{k}q_{n+r},}
\tag{9}
\]

with the empty product equal to one.

Every term is positive.  The series converges in the ordinary real topology.

### Proof

Iterating (7) for `K` steps gives the first `K` terms plus

\[
\left(\prod_{r=1}^{K}q_{n+r}\right)Z_{n+K}.
\]

The heights strictly increase, every `q` belongs to `(0,1)`, and `Z_(n+K)` is
bounded by `108` from the local form of the estimate in `T-0036`.  The product
tends to zero, proving (9). ∎

## Statement 3 — the leading digit is isolated by a fixed real gap

At every stabilized boundary beginning at scale `m >= 12`,

\[
\boxed{
 b_{i_n}<Z_n<b_{i_n}+{1\over16}.}
\tag{10}
\]

Consequently the current type is recovered from the real defect alone:

\[
\boxed{
 i_n=b^{-1}\bigl(\lfloor Z_n\rfloor\bigr).}
\tag{11}
\]

### Proof

In the stabilized region, `t_(n+1)+1 >= 128`.  Direct integer comparison gives

\[
\left({2048\over2187}\right)^{128}<2^{-10}.
\tag{12}
\]

The heights increase, so every future `q` is below `2^(-10)`.  Since every toll
digit is at most `54`, (9) yields

\[
0<Z_n-b_{i_n}
<54\sum_{k\ge1}2^{-10k}
={54\over1023}
<{1\over16}.
\]

This proves (10).  The four toll values are distinct integers, so (11) follows.
∎

## Consequences

The tower type has three simultaneous exact descriptions:

```text
binary description:   v_2(W_n) in {0,1,2,3};
ternary description:  v_3(W_(n+1)) in {1,2,3};
real description:     floor(N_n * {C_infinity H_n}) in {9,54,36,24}.
```

Thus the symbolic stage word is not an independent control tape.  It is read
simultaneously from:

1. the low binary bits of an ordinary boundary;
2. the low ternary valuation of the next boundary;
3. the leading real digit of one fixed room's shrinking defect.

This is the exact three-place synchronization object for the next
product-formula or seam-carry argument.

## Gap audit

- The digit expansion is compatible with transcendental rooms and does not by
  itself prove nonexistence.
- The very small tail in (10) does not determine the growing Hensel carry of
  `L-0033`.
- No cap stitch or finite marked initialization is constructed.