# KTHM-0013 — Classical preimage-tree and density lower bounds

**Sources:** Applegate–Lagarias I and II; Krasikov–Lagarias. [@ApplegateLagarias1995a; @ApplegateLagarias1995b; @KrasikovLagarias2003]  
**Proof status:** black-box imports; computer-assisted proofs not reproduced  
**Maps to:** methodological interface for `CLAUDE/Q-0004`, `CLAUDE/Q-0006`, and collision-fiber growth; non-equivalence warning for `PR3/T-0005`

## Statements

Let `a` be an integer not divisible by `3`, and let `n_k(a)` count integers `n` with `T^k(n)=a` for the shortcut map.

Applegate and Lagarias prove, for all sufficiently large `k`,

\[
1.302^k\le n_k(a)\le1.359^k.
\]

If `π_a(x)` counts integers `n` with `|n|≤x` that eventually reach `a`, their tree-search method gives

\[
\pi_a(x)\ge x^{0.65}
\]

for all sufficiently large `x`. Their Krasikov-inequality method improves the density exponent to `0.81`. Krasikov and Lagarias later use improved difference-inequality systems and a computer-aided proof to obtain exponent `0.84`.

## Non-equivalence to collision-fiber width

The quantity `n_k(a)` counts all depth-`k` preimages of one target, across parity weights and residues. A repository collision fiber usually fixes a same-depth affine output **and** an odd-step count so that one common multiplier produces a digit-preserving induced map. Therefore the tree bounds neither prove nor disprove exponential same-stratum fiber width.

## Strategic use

The exact recursive inequalities and computer-assisted linear-program method are plausible templates for an upper bound on within-stratum multiplicity. A new state system adapted to `(odd count, affine output)` is required first.
