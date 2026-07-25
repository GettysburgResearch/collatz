# T-7301 — No fixed two-point linear descent can carry an infinite positive orbit

**Claim ID:** `T-7301`  
**Title:** Every contracting two-point linear image has a finite or impossible type tail  
**Status:** `PROPOSED / EXACT GLOBAL CLASS EXCLUSION`  
**Authoring agent:** `gpt56-cycle-01`  
**Created:** 2026-07-26  
**Dependencies:** `L-7301`  
**Scope:** fixed integer combinations of two consecutive states on one all-time six-branch orbit  
**Related counterexample candidates:** none

## 1. Theorem

Let

\[
Qx_{n+1}=Px_n+a_{i_n}
\]

be a positive ordinary six-branch orbit defined for every `n>=0`.  Fix integers
`u,v` satisfying

\[
0<u+v{P\over Q}<1,
\]

and put

\[
z_n=ux_n+vx_{n+1}.
\]

Then the sequence `(z_n)` cannot be a positive six-branch orbit for every
sufficiently large `n`.

Equivalently:

\[
\boxed{
\text{no positive all-time six-branch orbit admits a fixed contracting
integer two-point linear self-descent.}}
\]

## 2. Proof

By `L-7301`, if the induced digit

\[
u a_{i_n}+v a_{i_{n+1}}
\]

belongs to the allowed alphabet at every sufficiently large time, then one of
two type-tail geometries is forced.

### Case 1: diagonal family

For some `1<=t<=73`,

\[
(u,v)=(t+1,-t),
\]

and every sufficiently late edge satisfies

\[
i_{n+1}=i_n.
\]

Thus the type is eventually one constant value `i`.

Put

\[
Y_n=(P-Q)x_n+a_i.
\]

On a constant-type tail,

\[
Qx_{n+1}=Px_n+a_i
\]

implies

\[
\boxed{QY_{n+1}=PY_n.}
\tag{1}
\]

Because `gcd(P,Q)=1`, equation `(1)` implies that `Q^m` divides `Y_N` for every
`m>=1`. Hence `Y_N=0`. But

\[
Y_N=(P-Q)x_N+a_i>0
\]

for a positive state, a contradiction.

This is a self-contained exclusion of every eventually constant type tail; no
periodicity theorem is needed.

### Case 2: adjacent-ascent family

The pair is `(-8,8)` or `(-9,9)`, and every sufficiently late edge satisfies

\[
i_{n+1}=i_n+1.
\]

No infinite sequence in the finite set `{0,1,2,3,4,5}` can obey this relation.
Contradiction.

These are all cases in `L-7301`, proving the theorem. ∎

## 3. Why the contraction is genuine

The exact identity

\[
z_n=\left(u+v{P\over Q}\right)x_n+{v a_{i_n}\over Q}
\]

and the strict growth `x_n->infinity` imply

\[
0<z_n<x_n
\]

for every sufficiently large `n`.  Thus this theorem does not reject a merely
formal coordinate: it closes every fixed two-state integer linear mechanism
that could eventually turn one hypothetical orbit into a genuinely smaller
positive legal orbit.

## 4. Relationship to the least-root objective

If `m_n` stabilized, the resulting least all-time root could not be reduced by:

- the increment `x_(n+1)-x_n`;
- the `74/73` Euclidean remainder;
- any later continued-fraction remainder;
- or any other fixed integer two-point contraction whatsoever.

The positive target must therefore be genuinely nonlinear or carry unbounded
section information.  This theorem does not prove that the least roots diverge.

## 5. Gap audit

- Time-dependent coefficients are outside the theorem.
- A nonlinear function of the current integer may still provide an invariant.
- A finite-control full-subtree polynomial version is treated separately by
  `T-7303`.
- No all-time root or Collatz counterexample is claimed.
