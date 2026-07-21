# Classical parity vectors and `2`-adic Collatz coding

## Located foundations

Everett and Terras independently developed the finite parity-vector viewpoint for the shortcut map

\[
T(n)=\begin{cases}n/2,&n\equiv0\pmod2,\\(3n+1)/2,&n\equiv1\pmod2.\end{cases}
\]

For each length `L`, the initial parity word is determined exactly by `n mod 2^L`, and every binary word occurs. On one such cylinder, `T^L` is affine with multiplier `3^a/2^L`. [@Everett1976; @Terras1976]

Bernstein and Lagarias extend the parity-vector map to `Z_2` and study its conjugacy properties. [@BernsteinLagarias1996]

## Direct repository consequences

- `PR3/L-0001` is classical after normalization.
- `CLAUDE/L-0004` is the exact valuation form of the same cylinder rigidity.
- `CLAUDE/T-0021`'s exact uniformity of parity words on an odd affine lattice is a short corollary.
- Infinite parity strings naturally define `2`-adic points; this does **not** establish that the point is a positive ordinary integer.

## Boundary of the literature match

The papers do not supply the repository's sparse collision-fiber conjugacies, carry grammars, finite-boundary regeneration, or signature-tail amplification. Those statements begin from classical cylinders but add new finite algebraic packaging.

See KTHM-0001 through KTHM-0003.
