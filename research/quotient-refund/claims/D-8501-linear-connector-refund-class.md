# D-8501 — Linear-height phase-34 connector-refund class

**Claim ID:** `D-8501`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-cylinder-01`  
**Issue:** `#43`  
**Scope:** stabilized phase-`-34` tower connectors on an arithmetic height grid

## Frozen tower data

Use the four stabilized tower types from branch-qualified `PR3/L-0031`:

| type `i` | `p_i` | `b_i` |
|---:|---:|---:|
| 0 | 5 | 9 |
| 1 | 30 | 54 |
| 2 | 20 | 36 |
| 3 | 56 | 24 |

At height `t`, put

\[
N_t=3^{7(t+1)},
\qquad
K_t=2^{11(t+1)}.
\]

The binary and ternary tower anchors are

\[
A_i(t)=\frac{K_t p_i}{64},
\qquad
B_i(t)=\frac{N_t p_i+b_i}{64}.
\]

All heights below are multiples of `16`.

## Linear height grid

Fix a multiple of `16`, denoted `t_0`, and put

\[
t_n=t_0+16n.
\]

For types `i,j`, define the canonical connector `(eta,theta)` by

\[
B_i(t)+N_t\eta_{t;i,j}
=
A_j(t+16)+2^{11(t+17)}\theta_{t;i,j},
\]

\[
0\le\eta_{t;i,j}<2^{11(t+17)}.
\]

The corresponding canonical output satisfies

\[
0\le\theta_{t;i,j}<N_t.
\]

## Ordinary residual state

For an overlapping type directive

\[
i_0,i_1,i_2,\ldots,
\]

write the ordinary high tail entering the connector `i_n -> i_(n+1)` as

\[
h_n=
\eta_{t_n;i_n,i_{n+1}}
+2^{11(t_n+17)}z_n,
\qquad z_n\in\mathbb Z_{\ge0}.
\]

One exact tower and connector block sends it to

\[
h_{n+1}
=
\theta_{t_n;i_n,i_{n+1}}
+N_{t_n}z_n.
\]

Continuation through type `i_(n+2)` is therefore equivalent to

\[
\boxed{
2^{11(t_n+33)}z_{n+1}
=
N_{t_n}z_n
+\theta_{t_n;i_n,i_{n+1}}
-\eta_{t_n+16;i_{n+1},i_{n+2}}.
}
\tag{1}
\]

Equation (1) is the exact ordinary one-counter recurrence studied in this packet.

## Physical marked state

The corresponding shortcut-Collatz boundary state is

\[
\boxed{
n_n
=
A_{i_n}(t_n)
+2^{11(t_n+1)}h_n
-34.
}
\tag{2}
\]

Whenever (1) continues with nonnegative residuals, the branch-qualified tower identity replays the physical shortcut map exactly from `n_n` to `n_(n+1)` through the prescribed finite block.

## Ordinary-integer boundary

A compatible infinite type directive alone selects a `2`-adic residual. It is an ordinary positive construction only after one finite tuple

\[
(t_0,i_0,i_1,z_0)
\]

is supplied and (1) is proved integral and nonnegative for every future step. No inverse-limit type word, preloaded logarithm, or compatible finite-prefix family counts as initialization.
