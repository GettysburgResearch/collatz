# KTHM-0009 — Everett's density-one finite descent theorem

**Source:** Everett, Theorem 2 and its preceding parity-count estimate. [@Everett1976]  
**Proof status:** original theorem imported as a black box; source proof inspected  
**Maps to:** contextualizes all “free fuel” and stopping-time observations; no direct proof of an individual orbit

## Statement

For the shortcut map

\[
T(2n)=n,\qquad T(2n+1)=3n+2,
\]

the set of positive integers `n` for which some iterate satisfies

\[
T^k(n)<n
\]

has natural density one.

## Source proof architecture

Everett uses the exact parity-word/residue bijection to count length-`L` cylinders by odd-step weight. A binomial large-deviation estimate shows that almost all cylinders have odd-step density below the growth threshold `log_3 2`, so the affine multiplier `3^a/2^L` is contracting; the additive term is then controlled to obtain descent for all sufficiently large members of those cylinders.

## Scope limitations

- Density one does not mean every integer.
- The theorem only guarantees one descent below the start, not convergence to `1`.
- It cannot exclude a sparse exceptional family or validate an explicitly proposed infinite orbit.
