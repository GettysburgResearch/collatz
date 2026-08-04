# Tao--surplus rigidity breakthrough

## Objective

This pass attacked the all-time coefficient-supercritical lane left open by the
positive coefficient-gate program.  It did not add a longer finite prefix, a
new itinerary encoding, or another downstream growth theorem.

## New theorem

For the shortcut Collatz orbit, put

\[
D_k=q_k-k\log_3 2,
\]

where `q_k` is the number of odd shortcut branches before time `k`.

If `D_k>=0` for every `k`, the exact affine identity is

\[
x_k=3^{D_k}x_0+
\frac12\sum_{m=1}^k v_{m-1}3^{D_k-D_m}.
\]

When `0<=D_k<=B`, this gives the two-sided linear bound

\[
\frac{\log_3 2}{2\,3^B}k
\le x_k\le
3^B\left(x_0+\frac k2\right).
\]

The orbit states are therefore distinct, tend to infinity, and have positive
upper logarithmic density as a subset of the positive integers.

For one divergent orbit, let `m_k=min_(j>=k) x_j` and define

\[
f(N)=\frac12\min\{m_k:x_k\ge N\}.
\]

Then `f(N)->infinity`, while every orbit state satisfies

\[
\operatorname{Col}_{\min}(x_k)=m_k>f(x_k).
\]

Tao's theorem says the set of positive integers violating
`Col_min(N)<f(N)` has logarithmic density zero.  The linear orbit has positive
upper logarithmic density, a contradiction.

Hence no positive ordinary orbit can be all-time coefficient-supercritical with
bounded surplus.

A low-band refinement proves that on any all-time supercritical ordinary orbit,
for each fixed `B`,

\[
\sum_{\substack{k\le N\\D_k\le B}}\frac1{k+1}=o(\log N).
\]

Thus

\[
D_k\to+\infty
\quad\text{in logarithmic density.}
\]

## Effect on the least-counterexample program

Combined with the proposed coefficient-stopping gate in PR #76, a least
counterexample must now lie in one of two sharply separated classes:

1. a finite first coefficient crossing no earlier than
   `217,976,794,617` steps; or
2. an ordinary divergent no-crossing orbit whose coefficient surplus is
   unbounded and escapes every fixed band in logarithmic time density.

This closes the bounded-bank critical/mechanical regime without assumptions on
periodicity, automaticity, substitution structure, or finite-state generation.

## Remaining gap

The theorem does not eliminate sparse high-surplus returns.  The remaining
no-crossing target is to rule out an ordinary orbit satisfying both

```text
D_k >= 0 for every k
```

and

```text
D_k -> infinity in logarithmic density.
```

A closing theorem must either force positive logarithmic-density returns to a
bounded surplus band, prove least-root escape in the high-surplus tree, or
manufacture a derived finite-place approximation beyond the exponent-one
product-formula threshold.

## Repository artifact

The complete proof, dependency audit, shortcut/unshortened minimum comparison,
and sharpened least-counterexample dichotomy are in

`research/h-frontier/claims/ITERATION_14.md`.

No proof of Collatz is claimed.  The result eliminates one exhaustive dynamical
subregime of the uniform-supercritical lane.