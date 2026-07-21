# Candidate counterexamples

Last updated: 2026-07-21

There is currently **no candidate positive integer**, no regular sanctuary, and
no finite symbolic construction proved to define an infinite positive-integer
Collatz trajectory.

## Literature-informed boundary

The literature-review branch and PR #12 establish a sharp expressiveness
boundary.

`L-0015` proves that regular finite endpoint or population languages have
regular ordinary marker projections. `T-0020` proves that finitely many regular
phase domains with fixed finite Collatz blocks compile to a one-step regular
sanctuary.

Therefore:

> A finite-state regular marked interval, marked-particle, carry-phase, or
> negative-target grammar is not a new existential class. It belongs to the
> exact regular-sanctuary program already implemented in PR #12.

A genuinely new route needs unbounded memory, variable block lengths, a
nonregular ordinary survivor, or non-rational marker coupling.

## What the negative-cycle tower now supplies

For each padded self-return type at phase \(-34\), `L-0016` gives exact finite
blocks

\[
A_t+2^{K_t}h
\longmapsto
B_t+3^{G_t}h
\qquad(h\ge0).
\]

The arbitrary ordinary high tail \(h\) survives unchanged.

For every adjacent pair of tower instances, `L-0017` gives one canonical
connector

\[
B+3^G\eta=\bar A+2^{\bar K}\theta,
\]

and hence the ordinary family

\[
\eta+2^{\bar K}z
\longmapsto
\theta+3^Gz
\qquad(z\ge0).
\]

Thus every finite tower schedule has infinitely many ordinary finite
realizations. Finite-depth compatibility is not candidate evidence by itself.

## Corrected stage architecture

The earlier 128-transition lane is retained only as a one-connector precursor.
True residual regeneration must pay the next two cylinder depths. The corrected
stage from `T-0023` and `L-0024` is

\[
t_{m,j}=2^m+j2^{m-8},
\qquad 0\le j\le256,
\]

with

\[
t_{m,256}=t_{m+1,0}.
\]

One scale stage therefore has exactly 256 transitions and an eight-bit finite
odometer.

For a tower type with recovery depth \(r\), put

\[
H_m=m-r-7.
\]

The normalized connector prefixes satisfy

\[
\nu_2(\omega_{m,j}-\omega_{m,0})
=H_m+\nu_2(j).
\]

The stage-boundary stack splits into three tracks.

### 1. Periodic rational frontier

The low stabilized bits are supplied by one explicit rational
\(\omega_\infty\), with a finite binary period depending only on the tower type.

### 2. Eight-bit odometer

The 256 substeps have exactly the carry profile of the binary counter
\(0,1,\ldots,256\).

### 3. Quadratic moving bulk

Put

\[
y_m=3^{-7\cdot2^m},
\qquad
u_m=\frac{y_m-1}{2^{m+2}}.
\]

Then \(u_m\) is odd and obeys

\[
\boxed{u_{m+1}=u_m+2^{m+1}u_m^2.}
\]

The full stage-boundary prefix is

\[
\omega_m
=
\omega_\infty+2^{m-r+1}3^{-g_0}u_m.
\]

This reduces the nonperiodic stack update to one shifted square-and-add
operation per scale.

## Exact information budget

The negative eleven-cycle has bit margin

\[
\frac5{53}<7\log_2 3-11<\frac4{41}.
\]

`T-0024` proves that one corrected 256-transition stage has exponential residual
capacity after paying the full next-stage connector-precision increase. The
remaining surplus is rigorously greater than

\[
\frac{20985}{6784}2^m>3\cdot2^m
\]

bits, apart from a fixed type-dependent constant.

This is important but not sufficient. Bit-length surplus must be converted into
the **specific** required low bits.

## Current preferred candidate state

A future candidate should carry

\[
\boxed{(i,m,j,W,z,n),}
\]

where:

- \(i\) is one of finitely many tower/phase types;
- \(m\) is the unbounded dyadic scale;
- \(j\in\{0,\ldots,255\}\) is the finite stage odometer;
- \(W\) is a finite word carrying the rational frontier and quadratic bulk;
- \(z\) is the ordinary residual high tail;
- \(n\) is one explicitly marked ordinary positive integer.

A substep must replay one exact Collatz tower block and connector. A full stage
must have the form

\[
(i,m,0,W_m,z_m,n_m)
\longmapsto
(i',m+1,0,W_{m+1},z_{m+1},n_{m+1})
\]

with

\[
W_{m+1}
\text{ implementing }
 u_{m+1}=u_m+2^{m+1}u_m^2,
\]

and

\[
n_{m+1}=T^{L_m}(n_m)
\]

for the exact concatenated deterministic block.

## The load-bearing missing theorem

The remaining candidate theorem is an exact **surplus-routing stage
substitution**. It must prove, uniformly for every sufficiently large scale:

1. all 256 connector cylinders are selected exactly;
2. the periodic frontier and odometer are updated by finite control;
3. the quadratic bulk update is performed on a finite forward-generated word;
4. newly available residual bits are routed into the exact next bulk and
   connector prefix;
5. the residual recurrence
   \[
   z_{k+1}
   =
   \frac{3^{G_k}z_k+\theta_k-\eta_{k+1}}{2^{K_{k+2}}}
   \]
   stays integral, nonnegative, and above a stated threshold;
6. the marked ordinary integer is transported through every deterministic
   Collatz step;
7. the stage returns to the same finite syntactic track types at scale \(m+1\);
8. one explicit finite initial configuration exists.

Without item 4, nested Hensel prefixes define only a 2-adic limit. Without item
6, the construction remains an unmarked auxiliary population.

## Routes now excluded as complete candidates

The following do not suffice:

- a fixed periodic residue table (`L-0018`);
- a finite high-tail library with affine counter rules (`T-0021`);
- arbitrary finite connector depth (`L-0017`);
- the 128-step one-connector budget (`T-0022` precursor);
- positive residual bit-length surplus without exact routing (`T-0024`);
- a finite-state regular marked grammar (`T-0020`);
- a compact graph-directed or 2-adic attractor without an ordinary marker.

## Regular controls

Every bounded scale/counter truncation and every finite-state approximation
should be compiled through `L-0015`/`T-0020` and submitted to PR #12's exact
sanctuary verifier. Such controls are useful for producing concrete failure
words and safe kernels, but only an all-scale symbolic rule advances the present
route.

## Non-negotiable candidate checks

A future `K-####` file must prove:

- one finite positive starting integer exists explicitly;
- every tower and connector word agrees with the unique Collatz trajectory;
- the marker is transported exactly forever;
- the scale and odometer updates are total on the accepted state set;
- the quadratic bulk is generated forward rather than read from a 2-adic oracle;
- every residual division is exact and leaves a nonnegative ordinary integer;
- all next prefix/carry obligations are satisfied;
- positivity holds at every physical boundary;
- the full corrected stage, including repairs, has justified net growth;
- the stage grammar regenerates indefinitely from the finite initialization;
- the marked trajectory is unbounded or permanently avoids the terminal cycle.