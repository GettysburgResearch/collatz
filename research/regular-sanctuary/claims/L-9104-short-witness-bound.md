# L-9104 — Short canonical witness bound

- **Claim ID:** L-9104
- **Title:** A nonempty q-state semantic DFA has a witness of length at most q
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101
- **Scope:** complete q-state raw DFAs under semantic canonicalization
- **Related counterexample candidates:** none

## Statement

If a complete `q`-state DFA `D` has nonempty semantic language `L_D`, then it
accepts a canonical word of length at most `q`.

Conditional consequence: if every positive integer below `2^71` is known to
reach the trivial cycle, then a regular sanctuary under D-9101 semantics needs
at least 72 raw DFA states.

## Definitions

Word length is binary bit length in the LSD-first representation.  The
conditional premise refers to the published computational bound, not to a
locally admitted theorem.

## Motivation

The bound prevents a structurally impossible tiny-DFA search and redirects
computation toward deep-spine or residue templates whose expanded state count
can reach the necessary scale.

## Proof or construction

Choose an accepted canonical word `v1`, where the displayed final one is its
highest bit.  Let `p` be the state reached after `v`.  Since `p` is reachable
in a graph with `q` vertices, a shortest word `u` reaching `p` has length at
most `q-1`.  Then

$$
\delta(q_0,u1)=\delta(p,1)=\delta(q_0,v1),
$$

so `u1` is accepted, canonical, and has length at most `q`.

If `q <= 71`, its value is below `2^71`.  Under the published verified-range
premise it eventually reaches 1 or 2.  Exact forward invariance would then put
a forbidden cycle state in the sanctuary, a contradiction.

## Dependency audit

- The first paragraph uses only D-9101 and finite graph reachability.
- The 72-state corollary additionally cites Barina's published verification:
  https://doi.org/10.1007/s11227-025-07337-0
- Citation admission remains pending issue #7.

## Gap audit

- The unconditional theorem is the length-at-most-`q` statement.
- The 72-state number is conditional on an external computational result.
- A small synthesized core behind a fixed guard may expand to far more raw DFA
  states and is not excluded by the lemma.

## Adversarial tests

The suite exhausts every acceptance mask for every labeled transition skeleton
through three states and checks the claimed length bound whenever the semantic
language is nonempty.

## Remaining uncertainty

The elementary proof appears complete.  The external verified range is not yet
an admitted repository dependency.

## Suggested next attack

Have issue #7 verify the exact theorem statement and bound in the cited source;
then promote only the conditional corollary justified by that audit.
