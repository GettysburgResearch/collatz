# R-8802 — Autonomous finite-state certificates cannot produce a positive survivor

Claim ID: R-8802  
Title: Autonomous bounded-state directive generation cannot close the exact `4 -> 5` chart  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-8802, T-8812  
Scope: autonomous deterministic finite-state directive generators  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

No autonomous deterministic finite-state directive generator in the sense of
`D-8802` can emit the phase directive of a positive ordinary infinite orbit in
the exact `4 -> 5` chart.

Equivalently, no counterexample certificate whose complete infinite directive
is produced by iterating one fixed deterministic map on a finite state set can
construct a positive survivor of this chart.

## Proof

By `D-8802`, every directive emitted by an autonomous deterministic finite-state
generator is eventually periodic. By `T-8812`, the chart completion of every
eventually periodic directive lies in the rational interval `[-2,-1]` after the
physical shift and therefore is not a positive ordinary integer. Hence no such
generator produces a positive infinite chart orbit. **QED**

## What is refuted

The theorem rules out:

- periodic schedules;
- finite-prefix-plus-periodic schedules;
- autonomous finite automata with any fixed number of states;
- finite directed control graphs with one deterministic successor per state;
- attempts to hide periodicity by relabeling the finite states.

## What is not refuted

The theorem does not cover:

- finite-state transducers driven by an external aperiodic input;
- counters, stacks, queues, tapes, or growing residue data;
- arithmetic state containing an unbounded integer quotient or carry;
- nondeterministic trees unless a bounded-state autonomous selector is fixed;
- proof-producing negative invariants;
- infinite directives defined by non-eventually-periodic mathematics.

## Dependency audit

- `D-8802`: finite autonomous state implies eventual periodicity.
- `T-8812`: eventual periodicity implies no positive ordinary completion.

## Gap audit

The word **autonomous** is load-bearing. A finite transducer with an infinite
aperiodic input can emit aperiodic output and is outside the theorem. Likewise,
a finite control program operating on unbounded integer registers does not have
a finite total state space.

## Adversarial tests

Any claimed finite-state counterexample certificate should expose its total
state. If the total state set is genuinely finite and the update is autonomous
and deterministic, cycle detection produces the eventual period explicitly.

## Remaining uncertainty

None known within the stated certificate class.

## Suggested next attack

A constructive successor must identify the unbounded arithmetic state that
preserves one ordinary root across all cylinder depths. A negative successor
must prove that every such state forces the least positive root to escape.
