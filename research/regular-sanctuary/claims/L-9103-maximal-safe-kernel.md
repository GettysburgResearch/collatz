# L-9103 — Maximal safe acceptance kernel

- **Claim ID:** L-9103
- **Title:** Largest safe accepting set for a transition skeleton
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** L-9102
- **Scope:** a fixed complete DFA transition skeleton
- **Related counterexample candidates:** none

## Statement

Let `R_D` be the exact endpoint relation for a fixed transition skeleton and
let

$$
B=\{\delta(q_0,\texttt{1}),\delta(q_0,\texttt{01})\}.
$$

Then

$$
F_{max}=Q\setminus\operatorname{Pre}_{R_D}^{*}(B)
$$

is the unique largest accepting-state set whose semantic language rejects 1
and 2 and is forward invariant under the shortcut map.

## Definitions

`Pre*` is reflexive transitive reverse reachability in the directed relation
`R_D`.  Extra states may be added to `B` to impose a search restriction such as
a minimum input length.

## Motivation

For a `q`-state transition skeleton, naively searching every acceptance mask
costs another factor `2^q`.  The theorem solves the acceptance choice exactly
and supplies an emptiness fitness measure for structured skeleton search.

## Proof or construction

Every state in `B` must be rejected.  If `p R_D q` and `q` is forced rejected,
then accepting `p` would violate closure, so `p` is also forced rejected.
Induction along reverse paths shows every valid accepting set is disjoint from
`Pre*_(R_D)(B)` and hence contained in `F_max`.

Conversely, the rejected set is reverse closed.  Therefore, if `p` is in
`F_max` and `p R_D q`, then `q` cannot be rejected; otherwise reverse closure
would reject `p`.  Thus `F_max` is forward closed and rejects `B`.

## Dependency audit

L-9102 supplies the exact finite relation; no arithmetic sampling enters the
kernel computation.

## Gap audit

- `F_max` may contain no canonically reachable state; semantic nonemptiness is
  a separate exact check.
- Extra forbidden states narrow the language and must be reported as a search
  template, not a universal obstruction.
- State-label enumeration is not enumeration up to isomorphism.

## Adversarial tests

The committed test suite compares `F_max` with every acceptance mask on every
labeled two-state skeleton.  A broader in-session audit was reported but is not
admitted as a replayable repository artifact.

## Remaining uncertainty

No known algorithmic uncertainty remains for a fixed skeleton, but repository
independent-review status has not been granted.

## Suggested next attack

Encode transition-skeleton search with symmetry breaking or CEGIS while
keeping this standard-library implementation as the final acceptance checker.
