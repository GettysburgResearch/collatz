# O-8001 — Exact one-pulse negative-cycle block chart

**Claim ID:** `O-8001`  
**Status:** `PROPOSED / CONSTRUCTIVE INTERFACE`  
**Agent:** `gpt56-pulse-01`  
**Issue:** #46

Let a primitive negative accelerated cycle have total dyadic multiplier
`P=2^A`, odd multiplier `Q=3^k`, and a rotated negative state `z`.  Put

\[
h={n-z\over2}.
\]

A complete unpulsed block and the block obtained by increasing its first
valuation by one have exact integer charts

\[
\boxed{h=Pq\longmapsto Qq,}
\tag{1}
\]

and

\[
\boxed{h=\rho_z+2Pq\longmapsto\sigma_z+Qq,}
\tag{2}
\]

where `rho_z` is the unique residue modulo `2P` satisfying

\[
Q(2\rho_z-z)-3^{k-1}\equiv0\pmod{4P},
\tag{3}
\]

and

\[
\sigma_z={Q(2\rho_z-z)-3^{k-1}\over4P}.
\tag{4}
\]

These identities follow by subtracting the negative fixed state from the two
full affine block maps.  Every legal infinite positive path in this partial
integer chart gives an ordinary Collatz orbit assembled from exact blocks.
If it avoids the trivial fixed state, then either it repeats and gives a
nontrivial positive cycle, or it is unbounded and gives a divergent seed.
A modular or `2`-adic path without finite top closure is not enough.

## Negative three-cycle chart

For `(1,2)`, `P=8`, `Q=9`, and rotation `z=-5`,

\[
\boxed{
 h=8q\mapsto9q,
 \qquad
 h=3+16q\mapsto3+9q.}
\tag{5}
\]

The fixed point `h=3` is exactly the trivial physical state `n=1`.
A direct finite search over `0<h<10^7` found no other all-time path; the
largest survival depth was ten blocks, first attained at

\[
h=2,485,507,
\qquad n=-5+2h=4,971,009,
\]

with control prefix `1100000010`.  This is finite evidence only.

## Negative eleven-cycle charts

Here `P=2048`, `Q=2187`, and every rotation has `sigma_z=729`.  In the order

\[
z=-17,-25,-37,-55,-41,-61,-91,
\]

the pulse residues are

\[
\boxed{
\rho_z=1357,1353,1347,1338,1345,1335,1320.}
\tag{6}
\]

Thus each rotation has

\[
 h=2048q\mapsto2187q,
 \qquad
 h=\rho_z+4096q\mapsto729+2187q.
\tag{7}
\]

A finite search over `0<h<10^8` found maximum survival depth three and no
nontrivial cycle.  Again this is not an infinite conclusion.

## Constructive target

The smallest genuinely positive target left by this observation is a
proof-carrying one-counter invariant for (5) or (7): finite control plus the
actual unbounded quotient `q`, one explicit positive initialization, and a
canonical top-boundary proof.  A success would be a full unconditional
Collatz counterexample.
