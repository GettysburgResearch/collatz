# L-0003 — Exact binary recursion for collision fibers

Claim ID: `L-0003`  
Title: Linear-time recursion for the affine data of every residue class  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0001`, `D-0001`  
Scope: exact construction and enumeration of all finite collision fibers  
Related counterexample candidates: none

## Statement

For \(L\ge0\) and \(0\le r<2^L\), define

\[
a_L(r)=\#\{0\le t<L:T^t(r)\text{ is odd}\},
\]

and

\[
s_L(r)=T^L(r).
\]

Then for every integer \(q\ge0\),

\[
\boxed{
T^L(2^Lq+r)=3^{a_L(r)}q+s_L(r).
}
\tag{1}
\]

The complete tables at level \(L+1\) are obtained from those at level \(L\)
as follows. For \(0\le k<2^L\),

\[
a_{L+1}(2k)=a_L(k),
\qquad
s_{L+1}(2k)=s_L(k).
\tag{2}
\]

For the odd residue \(2k+1\), write

\[
3k+2=2^Lq+u,
\qquad q\in\{0,1,2\},\quad0\le u<2^L.
\tag{3}
\]

Then

\[
\boxed{
a_{L+1}(2k+1)=1+a_L(u)
}
\tag{4}
\]

and

\[
\boxed{
s_{L+1}(2k+1)=3^{a_L(u)}q+s_L(u).
}
\tag{5}
\]

Consequently, the collision fibers at depth \(L\) are exactly the level sets
of the pair

\[
r\longmapsto\bigl(a_L(r),s_L(r)\bigr).
\tag{6}
\]

All affine data through depth \(L\) can therefore be generated using
\(O(2^L)\) arithmetic operations in total, rather than tracing every residue
for \(L\) separate steps.

## Definitions

A collision fiber with odd-step count \(a\) and common output \(s\) is

\[
F_L(a,s)=
\{0\le r<2^L:(a_L(r),s_L(r))=(a,s)\}.
\tag{7}
\]

It is **supercritical** when \(3^a>2^L\).

## Motivation

The recursion changes the object of study from isolated parity words to an
exact coalescence forest. A wider fiber appears when even and odd predecessor
families enter the same level set in (6). This exposes sparse fibers that a
search for consecutive runs misses and supplies a scalable exact experiment.

## Proof

Equation (1) is the residue-class form of `L-0001`: the first \(L\) parities
of \(2^Lq+r\) are those of \(r\), and the coefficient of \(q\) after the
block is \(3^{a_L(r)}\).

For an even residue,

\[
T(2k)=k.
\]

The remaining \(L\) steps therefore give (2).

For an odd residue,

\[
T(2k+1)=3k+2.
\]

Write this value as in (3). Applying (1) at level \(L\) gives

\[
T^L(3k+2)
=T^L(2^Lq+u)
=3^{a_L(u)}q+s_L(u).
\]

The first step was odd and the remaining block contains \(a_L(u)\) odd
steps, proving (4) and (5).

Two residues have the same affine image on every lift \(2^Lq+r\) exactly when
both the coefficient \(3^{a_L(r)}\) and constant \(s_L(r)\) agree. Since
powers of three are distinct, this is equivalent to equality of the pair in
(6). The recurrence creates two level-\(L+1\) entries for every level-\(L\)
index, so the total work over all preceding levels is a geometric sum
\(O(2^L)\). ∎

## Dependency audit

- `L-0001` supplies the affine residue-class identity (1).
- The remaining recursion is a direct decomposition by the first parity.
- No statistical or asymptotic claim is used.

## Gap audit

- The recursion enumerates finite fibers; it does not prove their maximum
  cardinality is unbounded.
- A large fiber is only a richer local alphabet, not an infinite orbit.
- Machine implementations must use exact integers; output values grow beyond
  fixed-width ranges at larger depths.

## Adversarial tests

`X-0002` compares the recursively generated tables with direct shortcut-map
traces for all residues through depth 12, then uses the recursion to enumerate
all supercritical nontrivial fibers through depth 22.

## Remaining uncertainty

The recursion appears complete and elementary but has not been independently
reviewed.

## Suggested next attack

Study repeated even/odd coalescence events in (2)--(5) as a branching algebra.
An explicit recursive family of coalescences with controlled odd-step density
would prove unbounded collision alphabets and could yield structured digit sets
rather than accidental large fibers.
