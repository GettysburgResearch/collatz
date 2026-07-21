# Regular Sanctuary Program

- **Agent:** `gpt56-regular-01`
- **Issue:** [#10](https://github.com/gfreund123/collatz/issues/10)
- **Branch:** `agent/gpt56-regular-01/10-regular-sanctuary`
- **Program status:** active
- **Counterexample status:** none

## Objective

Find a nonempty regular language `L` of canonical finite binary encodings such
that the shortcut Collatz map satisfies

$$
T(L)\subseteq L,
\qquad
L\cap\{1,2\}=\varnothing.
$$

Any accepted positive integer would then avoid the trivial shortcut cycle for
all time.  The language and its finite closure certificate would constitute an
exact counterexample construction.

No such language is claimed here.  This contribution establishes an exact
laboratory for stating, checking, synthesizing, and refuting bounded regular
sanctuary candidates.

## First-session results

The experiment under
[`experiments/X-9101-regular-sanctuary`](../../experiments/X-9101-regular-sanctuary/)
provides:

1. canonical least-significant-digit-first finite-word semantics;
2. a five-state subsequential transducer for the shortcut `3n+1` map;
3. an exact product-graph decision procedure for `T(L) subset L`;
4. concrete closure-violation witnesses whenever inclusion fails;
5. the maximal safe accepting set for any fixed DFA transition skeleton;
6. exact finite-horizon safety approximants;
7. a Python-standard-library-only JSON certificate checker;
8. 29 regression tests, including a known `3n-1` nontrivial cycle;
9. exact bounded searches over all labeled one- through four-state skeletons;
10. an initial structured search behind a 72-bit length guard.

All one- through four-state standard-Collatz skeletons had empty maximal safe
kernels.  Every one- and two-state transition core behind the fixed 72-bit
guard also had an empty kernel.  These are bounded negative computations only.
They are not evidence for Collatz convergence.

## Conditional 72-state floor for standard-map searches

The original idea suggested synthesizing raw DFAs with 2--12 states.  That is
impossible for a genuine standard-Collatz sanctuary given the currently
published verified range.

Every nonempty `q`-state candidate DFA, under this program's semantic
canonicalization, accepts a canonical word of length at most `q`.  Published
computation verifies convergence for every positive integer below `2^71`.
Consequently, a genuine sanctuary DFA must have at least 72 states.

Small DFAs remain valuable for testing the verifier and generalized maps.  The
serious search space is therefore structured rather than blindly random:

- a hard length spine followed by a small recurrent core;
- residue-cylinder automata selecting low binary digits;
- unions of a small number of cylinders with a shared tail machine;
- phase covers `T(L_i) subset L_(i+1)` using the base transducer;
- finite-horizon safety automata followed by automata-learning or PDR-style
  widening and exact inductiveness checks.

The 72-bit guard is search pruning only.  A future candidate's soundness must
come entirely from exact nonemptiness, safety, and closure verification.

## Why this direction is not covered by active no-go results

PR #6 records obstructions for particular additive carry processors and notes
that automatic descriptions in general remain open.  Issue #4's automaticity
obstruction concerns regeneration schedules for one `81/64` chart.  Neither is
a theorem excluding arbitrary regular forward-invariant sets for the full
shortcut map.

A regular sanctuary is nevertheless a strong target.  It would generally
describe a whole structured family of counterexample seeds, not merely one
aperiodic divergent orbit.  Failure of every bounded template considered here
would refute only those templates.

## Live overlap with PR #11

Draft PR #11 appeared during this session.  Its `C-0101` proposes a finite
automaton whose edges are Collatz parity blocks and whose accepted infinite run
must be realized by one ordinary seed with growing height.  This program uses a
different certificate: a regular language of **finite canonical integer
encodings**, every accepted member of which is closed under the full shortcut
map.  Neither checker verifies the other's seed-existence or closure obligation.

PR #11's `L-0105`/`L-0106` power-of-two port-thinning and bit-budget results are
relevant warnings for future residue-cylinder templates, but they are not used
as dependencies here and their status remains branch-qualified.  They concern
one arithmetic-progression parameter line, not arbitrary regular languages of
finite integers.  PR #11's cycle-hunt direction also overlaps issue #9; that
handoff has been cross-linked for reconciliation rather than silently
duplicated.

See https://github.com/gfreund123/collatz/pull/11.

## Read order

1. [`SEMANTICS.md`](SEMANTICS.md) for definitions, proofs, and algorithms.
2. [`CLAIMS.md`](CLAIMS.md) for exact statuses and dependency boundaries.
3. The [experiment README](../../experiments/X-9101-regular-sanctuary/README.md).
4. `verify.py` for the standard-library-only checker core.
5. `test_regular_sanctuary.py` for adversarial controls.
6. `results/summary.json` for the frozen first run.

## Next attacks

1. Generate deeper safety approximants and minimize them; mine recurring
   strongly connected quotients as candidate inductive widenings.
2. Search three- and four-state cores behind the 72-bit guard using symmetry
   reduction, CEGIS, or SAT rather than labeled brute force.
3. Add residue-cylinder templates that retain selected low bits after the
   length spine.
4. Extend maximal-safe-kernel synthesis to cyclic phase covers without
   composing a large transducer for `T^B`.
5. Request independent reconstruction of `L-9101` through `L-9104` before any
   status promotion.

## Literature boundary

Relevant primary sources include Caucal--Rispal's synchronized transducer
construction, Shallit--Wilson's finite-automata treatment of `3x+1`, and
Barina's verification below `2^71`.  Exact attribution and novelty positioning
remain provisional pending the repository-wide audit in issue #7.

- https://doi.org/10.1007/978-3-031-81202-6_8
- https://cs.uwaterloo.ca/~shallit/Papers/wilson.pdf
- https://doi.org/10.1007/s11227-025-07337-0
