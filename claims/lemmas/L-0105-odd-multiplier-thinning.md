# L-0105 — Odd-multiplier thinning for power-of-two image ports

Claim ID: `L-0105`  
Title: Every power-of-two image-port constraint thins the parameter lattice by the full modulus  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`  
Scope: accelerated blocks with destination constraints modulo powers of two  
Related counterexample candidates: none (obstruction)

## Statement

Let \(w\) be a chronological parity word of length \(L\) and odd-weight \(a\ge0\),
with

\[
T^L(2^L q+r)=3^a q+s
\]

for all integers \(q\) in the native domain. Fix \(L'\ge1\) and a residue
\(r'\pmod{2^{L'}}\). Then the set of parameters \(q\) for which the image lies
in the port \(2^{L'}\mathbb Z+r'\) is either empty or a single residue class
modulo \(2^{L'}\). In particular it is never a cofinite subset of the native
parameter line, and never the full native parameter line.

Equivalently: there is no accelerated Collatz block whose image arithmetic
progression is contained, for all native \(q\), in a single residue class
modulo \(2^{L'}\) with \(L'\ge1\).

Moreover, if an ordinary integer realizes a walk containing \(N\) successive
successful transitions each imposing some image-port constraint of modulus
\(2^{L_i'}\) with \(L_i'\ge1\), then that integer satisfies a congruence
modulo \(2^{\sum_i L_i'}\) (relative to the evolving parameter lattices).
Hence infinitely many such transitions require unbounded 2-adic precision and
cannot occur for a fixed ordinary integer without a mechanism that
**regenerates** precision (leaves the pure power-of-two image-port transition
class).

## Definitions

Native domain: \(n=2^Lq+r\) with \(r=r(w)\). Image port: the condition
\(T^L(n)\equiv r'\pmod{2^{L'}}\).

## Motivation

This is the general precision-drain theorem conjectured as `C-0102`, now
proved for the pure power-of-two port calculus that `D-0102` initially
suggested. It explains `L-0104` and the deaths in `O-0101`.

## Proof

The image-port condition is

\[
3^a q+s\equiv r'\pmod{2^{L'}}
\iff
3^a q\equiv r'-s\pmod{2^{L'}}.
\]

The multiplier \(3^a\) is odd, hence a unit in \(\mathbb Z/2^{L'}\mathbb Z\).
Therefore the congruence has either no solution or exactly one solution class
modulo \(2^{L'}\). It cannot hold for two distinct residues of \(q\) modulo
\(2^{L'}\), and in particular cannot hold for all \(q\).

The iterative precision claim follows by induction along the walk: each
successful transition replaces the current parameter line by a sublattice of
index \(2^{L_i'}\) (or aborts). An ordinary integer determines only finitely
many bits of any such nested residue tower; an infinite nested sequence of
proper thinnings is therefore impossible unless at some steps the walk uses
constraints outside this class (general moduli that create free 2-adic digits,
collision-fiber style gadgets, etc.).

## Dependency audit

- Affine block formula: `D-0101`.
- Units modulo \(2^{L'}\): elementary number theory.

## Gap audit

- Does not forbid destination ports of odd modulus (e.g. modulo \(3^b\)).
- Does not forbid variable moduli that grow in the 3-adic direction while
  regenerating 2-adic freedom.
- Does not forbid real/Möbius complementary-domain ping-pong (still open).
- “Precision regeneration” is named but not classified; that is the residual
  constructive problem.

## Adversarial tests

- Special case `L-0104`: \(L'=7\), multiplier \(243\equiv115\pmod{128}\) unit,
  unique thinning \(q\equiv0\pmod{128}\).
- Random check: for many words and random \(r'\), the solution count mod
  \(2^{L'}\) is 0 or 1 (`X-0105` edge builder).

## Remaining uncertainty

Low for the pure power-of-two statement. The residual uncertainty is entirely
in whether precision-regenerating edge types exist.

## Suggested next attack

Classify transitions with odd destination moduli: when do they create free
binary digits while preserving a height Lyapunov function? Connect to
collision-fiber growing-geometry questions without merging ledgers.
