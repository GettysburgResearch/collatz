# Session report: H frontier iteration 05

**Agent:** `gpt56-h-01`  
**Issue:** #17  
**Branch:** `agent/gpt56-h-01/17-h-exact-frontier`  
**Date:** 2026-07-22

## Objective

Transfer the fixed-room/minimum viewpoint from adjacent repository work to the
H ghost attractor, while preserving the distinction between the compact ghost
closure and actual itinerary ghosts.

## New proposed results

### L-9516 — centered rooms around the fixed ghost 4

The all-zero itinerary has fixed ghost `4`. Every nontrivial actual ghost has a
unique finite number `q` of leading zero letters and satisfies

\[
v_2(P-4)=2q+2.
\]

The compact closure additionally contains boundary points

\[
b_q=\phi_0^q(0)=4-4(4/3)^q.
\]

These boundary points share the same centered valuation rooms but are not
ordinary integers for `q>=1`; `b_0=0`. This boundary correction was made before
using the room decomposition in the ordinary-section theorem.

For an ordinary positive ghost in room `q`,

\[
P=4+4^{q+1}z,
\qquad
T_0^q(P)=4(1+3^qz),
\]

with positive odd `z`. This supplies a natural integral coordinate for the
remaining transformed-height problem.

### T-9510 — monotone ordinary-section minimum

At binary precision `K`, let `G_K` be the ghost closure modulo `2^K` and define

\[
\nu_K=\min\{P\ge16:P=1\pmod3,\ P\bmod2^K\in G_K\}.
\]

The sequence is nondecreasing, and

\[
\boxed{
H\text{ terminates on every positive integer}
\iff
\nu_K\to\infty.
}
\]

This is a stronger finite extremal target than the prefix-expanding minimum:
it addresses the entire ordinary section and does not require a prior descent
theorem.

## X-9504 exact finite checkpoint

The standard-library computation enumerated the complete ghost residue sets
through precision 50. At `K=50` there are

```text
922111
```

residue classes and

```text
nu_50 = 10205790208.
```

One decoded visible prefix for the minimizing residue is

```text
(6,1,0,1,0,0,1,0).
```

The finite minimum has plateaus; the result is not an asymptotic proof.

Frozen digest:

```text
2e6a51a8c9707d876ef35200baaa9554bfce619abf416fb27946638a52820280
```

## Combined frontier after iterations 04--05

Iteration 04 excludes the critical real-escape branch, subject to independent
verification of the imported Yu specialization. Iteration 05 packages the sole
remaining all-orbit obstruction into

```text
nu_K -> infinity.
```

The remaining proof task can now be attacked room by room in the integral
coordinate `z`, or globally by proving nonstabilization of the monotone minimum.
The finite mixed-sign zero-carry displacement problem remains useful for the
alternative descent-plus-LX architecture, but it is no longer logically
necessary if `Q-9506` is solved directly.
