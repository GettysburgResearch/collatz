# Session report: H frontier iteration 06

**Agent:** `gpt56-h-01`  
**Issue:** #17  
**Branch:** `agent/gpt56-h-01/17-h-exact-frontier`  
**Date:** 2026-07-22

## Requested inputs read

This session read the live literature branch's `LITERATURE.md`,
`literature/LIVE_REPO_REVIEW_WAVE5.md`, and the latest `gpt56-pro-03` comments
on PR #19. The most useful recommendation was to move a centered H room to its
first nonzero section and write the smallest simultaneous exponential equation
before invoking logarithmic forms or S-unit finiteness.

The session also inspected the directly relevant completion-height and
cross-direction packets, especially the finite-trap theorem in PR #33 and the
H renewal/core compatibility claims in PR #34. No external branch claim is
silently promoted; the renewal identities used here are rederived in
`ITERATION_06.md`.

## New results

### 1. Complete closure-boundary audit (`L-9517`)

The earlier centered-room packet listed only the outer boundary sequence
`phi_0^q(0)`. The full ghost closure also contains deeper finite-code boundaries
`Phi_w(0)`. They are now classified exactly:

```text
G = genuine infinite ghosts
    disjoint union
    finite-code points Phi_w(0).
```

Every nonempty finite-code point is negative in the real embedding. Hence no
positive ordinary integer can be a closure boundary. This repairs the compactness
step in the monotone ordinary-section theorem `T-9510`.

### 2. Dual renewal bridge (`L-9518`)

At consecutive nonzero letters, with nonzero height `R`, intervening zero-room
length `L`, and endpoint odd cores, there is one bridge core `W=5 mod 6`:

\[
9^RU-1=4^LW,
\qquad
2^{3R'}U'-1=3^LW.
\]

The integral renewal height

\[
Z=(p-4)/4=2^{3R}U-1
\]

obeys

\[
Z'=A Z+(A-c),
\qquad
A=(9/8)^{R-\kappa L},
\quad c=(3/4)^L.
\]

On a nonperiodic orbit, the sign of `Z'-Z` is exactly the sign of the renewal
capital `R-kappa L`. This is the first integral transformed height found for the
centered subcritical program, although it is not yet uniformly contracting.

The centered-room normal form requested by the literature audit is now explicit:

\[
3^aX+1=8^RU,
\qquad
4^bY+1=9^RU,
\]

\[
8^R4^bY-9^R3^aX=9^R-8^R.
\]

### 3. Exact subcritical future demand (`T-9511`)

After the critical mode is removed, put

\[
c=\log_8 9,
\qquad h_n=\log_8u_n.
\]

The sole subcritical regime has an exact future-mean identity:

\[
\overline h_n-h_n
=c(r_n-\kappa+B_n),
\qquad B_n>0,
\]

where `bar(h)_n` is the exponentially weighted geometric future mean. Thus a
large present valuation forces a later odd-core spike exponential in `r_n`.

The equivalent rounded-deficit representation proves

\[
\sup_{m\ge n}d_m\ge(c-1)r_n.
\]

Therefore the last surviving regime cannot have bounded deficit/carry blocks.
Every large valuation must eventually be paid by an unbounded below-critical
deficit and an exponentially large multiplicative core reset.

### 4. Least-survivor toll rigidity (`T-9512`)

If a nonperiodic survivor exists and `P` is the least such starting state, the
plastic survivor count gives

\[
\log(Q_\infty/P)=O(P^{\log_2\rho-1}),
\qquad
Q_\infty-P=O(P^{\log_2\rho}).
\]

Thus the real affine toll is sublinear in the least ordinary start and is tiny
in relative terms.

## Exact experiment X-9505

The standard-library audit checked:

- 55,986 finite-code boundary signs;
- 20,000 exact random words;
- 269,845 dual renewal bridges;
- 269,845 renewal-height sign laws;
- the exact central plateau equation in the box `1 <= R,a <= 300`.

No identity failed. Ninety-four plateau tuples entered the necessary narrow
real window, but none produced an exact positive integral plateau. The latter
is finite evidence only.

Digest:

```text
f5c6aaab56111fd2a3167dd44896473d421d51e17635b08fd41775f71c295777
```

## Current frontier

The direct scalar target remains

\[
\nu_K\to\infty.
\]

Subject to the independent Yu-specialization audit, a hypothetical nonperiodic
ordinary ghost is now forced into one regime only:

```text
eventual zero carry
+ subcritical capital
+ unbounded rounded deficits
+ exponential future core resets.
```

`Q-9507` asks for an integral finite-state refinement of the renewal height that
turns this regime into a finite-trap contradiction. The real future-demand
identity is exact, but it is not itself an integer and therefore does not yet
close the ordinary section.

## Suggested next attack

1. Work directly with the simultaneous star
   `3^a X+1=8^R U`, `4^b Y+1=9^R U`.
2. Search for an integer quotient/remainder whose zero-carry update contracts
   after each unbounded deficit reset.
3. Keep proper-subsum audits explicit before using S-unit finiteness.
4. In parallel, formulate a Fourier/cusp estimate for the ordinary-section
   minimum `nu_K`; the exact plastic recurrence supplies the correct branch
   pressure, while finite-code boundary negativity supplies the cusp boundary.
