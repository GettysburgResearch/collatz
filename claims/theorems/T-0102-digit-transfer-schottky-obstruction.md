# T-0102 — Schottky/IFS obstructions for digit-transfer charts

Claim ID: `T-0102`  
Title: Compact positive IFS and periodic digit itineraries fail for supercritical digit-transfer maps  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`, `T-0101`, `L-0101`, `L-0107`  
Scope: maps \(H(MB+d)=NB+d\) with \(N>M\ge2\), finite digit set \(D\)  
Related counterexample candidates: none (obstruction bridging to collision fibers)

## Statement

Let \(M,N\) be integers with \(N>M\ge2\), and let \(D\subset\{0,1,\ldots,M-1\}\)
be a nonempty finite digit set. Define the partial map

\[
H(MB+d)=NB+d\qquad(d\in D)
\]

on the disjoint union of progressions \(MB+d\) (\(d\in D\)).

This is the **digit-transfer** / induced collision-fiber format (externally:
`T-0002` on the collision-fiber branch; used here only as a definition).

### 1. Inverse branches

On the reals, each digit \(d\in D\) has inverse branch

\[
g_d(y)=\frac{y-d}{N}\cdot M+d=\frac{M}{N}y+d\Bigl(1-\frac MN\Bigr).
\]

Each \(g_d\) has slope \(M/N<1\) and fixed point \(d\).

### 2. Compact positive IFS

If \(0\notin D\) or more generally if one seeks an IFS on a compact interval
\(I\subset(0,\infty)\) with \(g_d(I)\subseteq I\) for all \(d\in D\) and pairwise
disjoint images: such a system, when it exists as a classical IFS, produces a
Cantor set of real (typically non-integral) survivors. **No claim** is made
that this Cantor set is empty — digit-transfer survivor sets may be nonempty
in \(\mathbb R\) or \(\mathbb Z_2\). The Collatz obstruction is integrality.

However: if \(D=\{d\}\) is a singleton, the unique fixed point is \(d\), and
the only constant itinerary survivor is \(d\) itself (often not a divergent
Collatz lift).

### 3. Periodic digit itineraries

An eventually periodic infinite digit itinerary for \(H\) corresponds to an
eventually periodic schedule of accelerated Collatz blocks in any lift of \(H\)
to shortcut words of common length \(L=\mathrm v_2(M)\) and weight
\(a=\log_3 N\) (when \(M,N\) are pure powers). By `T-0101`(D) /
`L-0107`, any supercritical such periodic lift that is realized in
\(\mathbb Z_2\) is a negative rational fixed point, not a positive ordinary
integer.

### 4. Fixed finite geometry vs growing boundary

Suppose a certificate uses a **fixed** finite digit set \(D\) and a fixed
radix pair \((M,N)\) forever. Then the finite-state digit choice is a finite
CRT/digraph certificate. By `T-0101`(E) and `L-0108`, forward dynamics on the
digit state have no new 2-adic branching beyond the prepaid modulus \(\log_2 M\).
An infinite ordinary positive survivor in \(V_\infty(M,N,D)\) is exactly a
nontrivial digit-transfer survivor — the central open object of the
collision-fiber packet — **not** something classical Schottky creates for free.

### 5. Bridge corollary (packet-external target)

Any Schottky-style attempt to certify a Collatz counterexample through a
digit-transfer chart must either:

- exhibit a nontrivial ordinary survivor for some fixed \((M,N,D)\) (open;
  rigidity in the symbolic-rewrite packet suggests this is hard for small
  charts), or
- allow **growing geometry**: digit sets / charts that change with scale so
  that the effective prepaid modulus or difference geometry grows
  (collision-fiber `Q-0010`), or
- leave the digit-transfer format.

Classical fixed-\(D\) Schottky does not bypass the survivor problem.

## Motivation

Connects the ping-pong packet’s negative surface to the collision-fiber
program’s positive open problem without merging ledgers or treating unmerged
`T-0002` as proved dependency — only the abstract \(H\)-format is used.

## Proof

(1) Solve \(NB+d=y\) for \(B=(y-d)/N\), then \(x=MB+d\).

(2) Standard IFS remarks; singleton case by unique fixed point of \(g_d\).

(3) Periodic digit stream \(\Rightarrow\) periodic block schedule in a pure-power
realization \(\Rightarrow\) `T-0101`(D).

(4) Digit state in a finite set \(D\) with fixed \(M\) is finite prepaid
state; apply `T-0101`(E). Forward digit choice at a fixed residue is
deterministic once the integer is chosen.

(5) Logical corollary of (3)–(4).

## Dependency audit

- Affine/shortcut encoding for pure-power lifts: `D-0101`.
- Accounting: `T-0101`.
- Periodic negative fixed points: `L-0107`.
- External collision-fiber naming is motivational only.

## Gap audit

- Does not prove emptiness of \(V_\infty\cap\mathbb Z_{>0}\) for any chart.
- Mixed / multi-chart transitions (variable \((M,N)\)) are the remaining
  Schottky-adjacent constructive surface — same as multi-chart groupoid ideas
  externally labeled `Q-0004`.
- Real Cantor survivors vs integer survivors must not be conflated.

## Adversarial tests

- Singleton \(D=\{0\}\) on \(H(64B)=81B\): survivor \(0\) only among constants.
- `X-0114` / `X-0115`: periodic digit streams on small charts lift only to
  negative fixed points when supercritical.

## Remaining uncertainty

Medium on the informal “does not bypass” language in (5); the precise claim is
the trichotomy listed there.

## Suggested next attack

Formalize multi-chart transitions as schedules with variable \((M_i,N_i)\) and
apply `T-0101` tax across chart changes (`L-0111`).
