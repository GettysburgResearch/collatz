# Session report: H frontier iteration 03

**Agent:** `gpt56-h-01`  
**Issue:** #17  
**Branch:** `agent/gpt56-h-01/17-h-exact-frontier`  
**Date:** 2026-07-22

## Objective

Review adjacent repository programs for reusable mechanisms, then use those
interfaces to narrow both the mixed-sign descent gap and the one-sided ordinary
ghost obstruction.

## Repository interfaces inspected

- PR #3: ordinary marked-spine versus unmarked pressure;
- PR #16: fixed-room minima, carry rigidity, and ordinary-section divergence;
- PR #20: repetition/completion-height and direct approximation barriers;
- PR #33: finite-trap nonstabilization for contracting cylinder systems;
- PR #13: the H ghost as a separated countable `2`-adic IFS.

No theorem status was imported from those branches. The H-specific results were
rederived inside this packet.

## New proposed results

### L-9513 — exact first-crossing threshold

For an expanding prefix `u` followed by a final contracting letter
`r in {0,1,2}`, the canonical displacement is

\[
\Delta_{ur}
=\left(1/M_u-a_r\right)N-(1+\Sigma_u)/4.
\]

This identifies one exact intermediate-state threshold. Positive carry helps;
zero carry is the sharp remaining finite interface.

### L-9514 / T-9506 — plastic ghost pressure

The ghost inverse maps

\[
\phi_r(x)=2^{3r+2}3^{-(2r+1)}(x-1)
\]

have pairwise disjoint exact-valuation images. Their residue counts obey

\[
N(K)=N(K-2)+N(K-3).
\]

If `rho^3=rho+1`, then `N(K)=Theta(rho^K)` and the ghost dimension is
`log_2(rho)`. Hence the positive ordinary survivor count is

\[
O(X^{\log_2\rho}),
\]

which strengthens and supersedes the earlier stretched-exponential-density
proposal.

### T-9507 — critical harmonic kernel

For the survivor branch with `v_2(p)=3r+2`,

\[
\sum 1/p=O(2^{-(3r+2)}).
\]

Thus every weight with `sum g_r2^(-(3r+2))<infinity` has finite weighted
harmonic mass. Along any nonperiodic survivor, each valuation scale has a
uniform odd-core reciprocal budget:

\[
\sup_r\sum_{i:r_i=r}1/u_i<infinity.
\]

This permits critical weights `8^r c_r` for arbitrary summable kernels `c_r`.

### L-9515 — completion-height repetition

If the same length-`ell` itinerary factor occurs at two positions, then

\[
2^{E_w}\mid p_j-p_i.
\]

A nonperiodic ordinary orbit therefore pays exponential ordinary height for
symbolic repetition. In a sublinear-capital regime the itinerary must have
superlinear factor complexity along a subsequence.

### T-9508 — critical/subcritical split

The normalized capital `K_i/c_*^i` has a limit. If it is positive, the orbit
would be a critical near-Pillai chain with

\[
r_{i+1}/r_i\to c_*=\log9/\log8,
\qquad
\sum_i\log(u_i)/r_i<infinity.
\]

Direct ghost truncations have limiting approximation exponent exactly one. If
the normalized limit is zero, capital growth is strictly subcritical.

## New open interfaces

- `Q-9504`: audit a sufficiently strong uniform two-term `2`-adic logarithmic
  form bound. The desired shape would contradict the critical core budget.
- `Q-9505`: find a transformed integer height to apply a finite-trap theorem to
  the subcritical zero-carry regime.

## Exact experiment X-9503

The standard-library audit checked:

- ghost residues through precision 24;
- 21 plastic recurrence identities;
- 92 exact branch partitions;
- 22,244 first-contracting crossings over prefix letters `0,...,8` and prefix
  length at most six;
- 3,511 zero-carry and 18,733 positive-carry crossings;
- no threshold failure.

The minimum observed threshold ratio was

```text
31922527 / 36067 = 885.0896...
```

at word `(4,0)`.

Digest:

```text
ab52939e289eb2489f3a9c032d89aed07a649e36c7c1fc0870b76ef54134b578
```

## Corrections and supersessions

- `T-9501` is superseded by the plastic power bound `T-9506`.
- `T-9504` is superseded by the branchwise critical theorem `T-9507`.
- No measure, entropy, pressure, or dimension estimate is treated as excluding
  an individual ordinary integer.
- Direct rational truncations in the critical regime are exactly at exponent
  one, so a generic supercritical approximation shortcut is unavailable.

## Remaining frontier

Finite side:

```text
actual-word zero-carry mixed-sign inequality
```

Infinite side:

```text
critical near-Pillai exclusion
or
subcritical transformed-height finite trap
```

The next highest-leverage task is the exact theorem audit behind `Q-9504`,
followed by a search for an integral completion height in `Q-9505`.
