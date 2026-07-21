# L-9102 — Exact regular closure decision

- **Claim ID:** L-9102
- **Title:** Product-graph decision of regular forward invariance
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101, L-9101
- **Scope:** any fixed complete binary DFA
- **Related counterexample candidates:** none

## Statement

For any fixed complete DFA `D`, finite reachability decides exactly whether

$$
T(L_D)\subseteq L_D.
$$

If inclusion fails, the procedure returns a canonical input `w` of globally
minimum bit length, with LSD-lexicographic tie-breaking, such that `w` is in
`L_D` and `T(w)` is not.

## Definitions

The endpoint relation `R_D` contains `(p,q)` exactly when some canonical word
leaves `D` in state `p` and its transducer image leaves `D` in state `q`.

## Motivation

Sampling accepted integers cannot certify universal closure.  A finite product
graph can, because both the candidate and arithmetic carry have finite state.

## Proof or construction

Explore states

$$
(q_{in},p,q_{out},c_{in},c_{out}),
$$

where the first and third components are input/output DFA states, `p` is the
subsequential transducer state, and the final components monitor whether each
stream is empty, ends in zero, or ends in one.  On each input bit, update all
components and feed the transition's emitted word through the output DFA.

At every canonical input endpoint, require a terminal transducer output.  Feed
it through the output components and require a canonical result.  Record the
resulting pair in `R_D`.  The graph has at most
`45 * |Q_D|^2` product states, so BFS terminates.

Every canonical word traces one graph path and produces its exact endpoint
pair by L-9101.  Conversely, every recorded endpoint is accompanied by its BFS
input path.  Hence closure fails exactly when `R_D` contains an edge from an
accepting state to a rejecting state.  BFS stores a shortest word for each
endpoint pair; minimizing across all violating pairs yields the globally
shortest closure-violation witness with the declared tie-break.

## Dependency audit

- D-9101 determines which endpoints count.
- L-9101 supplies exact output and canonical-domain totality.

## Gap audit

- The result is for a fixed DFA; unrestricted automaton existence is not
  thereby decidable.
- Missing terminal outputs and noncanonical outputs must be hard failures, not
  skipped paths.
- The tie-break is LSD-lexicographic and does not imply numeric minimality.

## Adversarial tests

Tests cover the universal language, empty language, `{1,2}`, `{3}`, a 201-bit
singleton, noncanonical aliases, missing terminal output, corrupt terminal
carry, and a reviewer-supplied DFA where endpoint-state ordering previously
returned a longer witness.

## Remaining uncertainty

In-session adversarial review produced a committed shortest-witness regression,
but no separate independent-checker artifact has entered the repository.

## Suggested next attack

Implement regular-image construction and DFA inclusion independently, then
compare its result and shortest witnesses with `terminal_relation`.
