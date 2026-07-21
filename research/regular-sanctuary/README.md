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

## Current results

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
8. 104 regression tests in the current extended suite, including a known
   `3n-1` nontrivial cycle;
9. exact bounded searches over all labeled one- through four-state skeletons;
10. an initial structured search behind a 72-bit length guard;
11. a seven-state fully accelerated odd-core transducer and exact `0* O` lift;
12. a second preimage/inclusion closure route, exhaustively differential-tested
    against the primary verifier on all 5,898 labeled DFAs through three states;
13. a checkpointable exact-floor CEGIS driver whose every proposed automaton
    is adjudicated by the unchanged exact verifier;
14. a portable, individually revalidated bank of exact closure implications
    with source and target accounting kept separate;
15. a conditional 71-state odd-suffix CEGIS lane with exact `U` checking and
    mandatory final verification of its raw shortcut lift;
16. prefix-trie batching that shares common LSD-prefix solver expressions while
    preserving exact implication semantics;
17. a durable paired census over all 69 structured suffix/raw gate pairs, with
    every proposed transition table replayable without Z3;
18. a reset-pattern audit quantifying the concrete-clause bank's exponential
    fixed-gate blind spot;
19. a local ripple-carry circuit for 1-preferred minimum-length spine words.

All one- through four-state standard-Collatz skeletons had empty maximal safe
kernels.  Every one- and two-state transition core behind the fixed 72-bit
guard also had an empty kernel.  These are bounded negative computations only.
They are not evidence for Collatz convergence.

The first exact-floor scout covered only accepting gate `0`: two sessions with
configured 60-second soft solver budgets checked and exactly rejected 22
proposed 72-state machines, learning 213 concrete closure implications.  Its
status is `time_limit`, not UNSAT.  Exact verification may finish after a
solver deadline; the frozen checkpoint makes subsequent work cumulative.

Those 213 clauses now form a portable logical bank. A bounded raw gate-3 scout
imported the bank, checked two models, and learned three further clauses before
its 20.016-second soft boundary. A separate structured suffix-gate-2 scout
normalized all 213 clauses through the exact odd map, checked five models, and
learned 11 more before its 20.125-second soft boundary. Both statuses are
`time_limit`; neither is an UNSAT result or evidence for convergence.

The paired generation-zero census completed all 138 partitions with a one-
model quota.  Every model was exactly rejected, 1,855 local implication
instances were recorded, and no partition stalled.  No partition is eliminated
by this bounded evidence.

The reset-pattern audit proves that concrete antecedent accumulation is badly
mismatched to the fixed-gate family: the frozen 224-clause corpus has 1,692
distinct length-71 factors, and 69 targeted additions raise this only to 1,760,
versus `2^68 = 295147905179352825856` factors needed for complete coverage at
one gate.  All distinguished spines are exact countermodels, not sanctuaries.

The minimum-word circuit is solver-UNSAT at suffix gate 2 and satisfiable at
gates 3 through 70, where all 68 frozen models are exactly rejected.  The
solver result alone is not promoted.  L-9114's separate carry induction proves
that gate 2 is impossible in the exact-distance suffix normal form.

## Structural constraints added after adversarial review

Nine further proposed lemmas sharply narrow the target without claiming that
arbitrary regular sanctuaries are impossible:

- `L-9106` gives an existence equivalence with regular odd languages invariant
  under `U(n)=(3n+1)/2^nu_2(3n+1)`; dyadic saturation is the regular language
  `0* O`.
- `L-9107` proves that every fixed low-bit residue cylinder contains
  infinitely many values in the trivial basin.  Full cylinders and eventual
  fixed-modulus tails are therefore dead search templates.
- `L-9108` proves that a forward-invariant finite union of affine-geometric
  binary rays has only eventually periodic orbits.  Via the classical
  slender-regular decomposition, a safe slender sanctuary would already
  certify a nontrivial positive cycle.
- `L-9109` shows conditionally that a candidate exactly at the 72-state floor
  has no structural slack: its least accepted word begins `11`, a 71-edge
  prefix spine exhausts all states, the last `1` is an accepting gate, and the
  start-state `0` transition is forced to loop.
- `L-9110` proves that maximal semantic kernels are monotone under
  right-congruence refinement.  An empty kernel on a fine skeleton cannot be
  repaired by literally quotienting or transition-stably merging its states.
- `L-9111` removes the forced dyadic state at the conditional exact floor: a
  safe `U`-invariant suffix language needs at least 71 states, and equality
  forces a complete suffix spine with gate `2,...,70`.
- `L-9112` replaces noncanonical comparisons between independently minimized
  Boolean safety DFAs by a strict chain of first-hit-colored Moore refinements.
  Bare colored skeletons are only finite/cofinite; their useful role is as
  exact features in products with a genuinely recurrent skeleton.
- `L-9113` constructs `2^(q-3)` reset-pattern models at every fixed suffix gate
  and proves an exponential coverage lower bound for concrete antecedent
  clauses.  Symbolic transition cubes and arithmetic proofs lie outside it.
- `L-9114` uses the exact output-length budget and ripple-carry arithmetic to
  eliminate suffix gate 2.  It does not eliminate generic raw gate 3.

Thus a genuinely new counterexample family must be sought in a nonslender,
branching language with unbounded high-bit dependence, unless the computation
is directly hunting a nontrivial cycle.

## Conditional 72-state floor for standard-map searches

The original idea suggested synthesizing raw DFAs with 2--12 states.  That is
impossible for a genuine standard-Collatz sanctuary given the currently
published verified range.

Every nonempty `q`-state candidate DFA, under this program's semantic
canonicalization, accepts a canonical word of length at most `q`.  Barina's
2025 article states that the project verified every positive integer strictly
below `2^71` and reports that limit in Section 6.  This is exactly the strict
range used here: a word of length at most 71 has value `<2^71`.  Consequently,
a genuine sanctuary DFA must have at least 72 states.

Small DFAs remain valuable for testing the verifier and generalized maps.  The
serious search space is therefore structured rather than blindly random:

- a hard length spine followed by a small recurrent core;
- odd-core automata with an explicit dyadic-saturation zero loop;
- low-residue filters followed by a genuinely branching high-bit tail machine,
  never a full or eventually full residue cylinder;
- phase covers `T(L_i) subset L_(i+1)` using the base transducer;
- finite-horizon safety automata followed by automata-learning or PDR-style
  refinement/augmentation and exact inductiveness checks.

The 72-bit guard is search pruning only.  A future candidate's soundness must
come entirely from exact nonemptiness, safety, and closure verification.

At exactly 72 states, L-9109 supplies stronger symmetry breaking than a
generic guard: exact BFS spine distances, upper-Hessenberg transitions, a
semantically singleton accepting gate, and forced low transitions.  Above 72
states, spine exhaustion and the zero-loop conclusion no longer follow.

L-9111 exploits L-9109's forced zero loop by splitting off the dyadic state.
Every odd word is uniquely `1x`; a 71-state DFA reads only `x`, and adjoining
one zero-loop state produces a raw 72-state shortcut DFA. This covers suffix
gates `2,...,70`, corresponding to raw gates `3,...,71`, but it is a structured
subspace: raw gate 0 and work-state transitions back to the added state remain
outside it.

L-9114 removes suffix gate 2, leaving active structured suffix gates
`3,...,70`, corresponding to structured raw gates `4,...,71`.  Generic raw
gate 3 remains open.

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

## Live overlaps

### PR #11 — affine parity-block construction

Draft PR #11 appeared during this session.  Its `C-0101` proposes a finite
automaton whose edges are Collatz parity blocks and whose accepted infinite run
must be realized by one ordinary seed with growing height.  This program uses a
different certificate: a regular language of **finite canonical integer
encodings**, every accepted member of which is closed under the full shortcut
map.  Neither checker verifies the other's seed-existence or closure obligation.

An audit of PR #11's later margin-persistence statement found a cancellation
counterexample: for `L>=2`, taking `D_0={0,2^L-1}` and adding the next digit
block `{0,2^L}` creates differences `+/-1` even though the old radius is zero.
The posted repair is the stronger sufficient condition
`diam(D_0)+R(D_0)+1<2^L`, plus a still-needed persistence argument across all
stages.  This program does not use the affected statement as a dependency.
PR #11's cycle-hunt direction also overlaps issue #9; that handoff remains
cross-linked for reconciliation rather than silently duplicated.

See https://github.com/gfreund123/collatz/pull/11.

### PR #14 — sink-stripped safety boundaries

PR #14 appeared during the final integration pass and independently rebuilt
the finite safety languages from integer reverse trees.  Its proposed L-9201
proves that every fixed-depth approximant is cofinite, that its only cyclic
minimal-DFA component is the inevitable two-state canonical tail, and that
stripping this tail leaves a DAG.  Its depth-0-through-20 state counts exactly
reproduce X-9101's frozen sequence without importing this branch's transducer.

This complements rather than duplicates L-9110. L-9201 removes a specific
finite-horizon false signal; L-9110 says a literal quotient cannot repair an
empty fine-skeleton maximal kernel. L-9112 now supplies the missing inter-depth
map: retain exact first-hit colors, and `H_(d+1)` projects canonically and
strictly onto `H_d`. The bare colored machines still express only finite or
cofinite semantic languages, so their boundary fibers must be paired with a
genuinely recurrent feature. Popcount parity is the smallest first control.
Every resulting product returns immediately to X-9101's exact closure
verifier. None of the proposed lemmas is promoted by these cross-checks.

See https://github.com/gfreund123/collatz/pull/14.

## Read order

1. [`SEMANTICS.md`](SEMANTICS.md) for definitions, proofs, and algorithms.
2. [`CLAIMS.md`](CLAIMS.md) for exact statuses and dependency boundaries.
3. The [experiment README](../../experiments/X-9101-regular-sanctuary/README.md).
4. `verify.py` for the standard-library-only checker core.
5. `independent_check.py`, `odd_core.py`, `spine_cegis.py`,
   `odd_suffix_cegis.py`, `paired_gate_census.py`, `reset_spine.py`, and
   `symbolic_minimum.py` for the differential, accelerated, synthesis, census,
   and symbolic-proof layers.
6. The eight `test_*.py` modules for adversarial controls.
7. `results/summary.json`, `results/spine-q72-gate0-bank.json`, and the census,
   reset-spine, symbolic-minimum, and scout artifacts listed in the experiment
   README for frozen empirical boundaries.

## Next attacks

1. Iterate the 1-preferred minimum-word image constraint at suffix gates
   `3,...,70`, and learn minimized symbolic transition-cube nogoods whose exact
   arithmetic witnesses cover many reset patterns at once.
2. Deepen raw partitions `0,3,...,71` only as the broader control. Gates 1 and
   2 conflict with the forced initial `11` spine. Share only revalidated exact
   clauses across generations, never solver conclusions.
3. Implement the L-9112 colored refinement chain and test popcount parity
   products at depths `8,12,16,20,24`, followed by adjacent-`11` parity. A
   proper nonempty canonical-tail fiber is the first interesting signal; any
   proposal still needs the base shortcut verifier.
4. Search other nonslender odd-core automata through the seven-state `U`
   transducer; lift every proposal to `0* O` and recheck it under the base map.
5. Add low-residue filters after the length spine only when a branching
   high-bit machine prevents acceptance of a whole cylinder.
6. Extend maximal-safe-kernel synthesis to cyclic phase covers without
   composing a large transducer for `T^B`.
7. Add proof logging or a separately authored checker before treating any
   solver-level UNSAT report as more than a bounded computational observation.
8. Request independent reconstruction of `L-9101` through `L-9114` before any
   status promotion, including the external slender-language decomposition.

## Literature boundary

Relevant primary sources include Caucal--Rispal's synchronized transducer
construction, Shallit--Wilson's finite-automata treatment of `3x+1`, and
Barina's verification below `2^71`.  Păun--Salomaa supplies one primary source
for the slender-regular decomposition used only in L-9108's corollary.  Exact
attribution and novelty positioning remain provisional pending the repository-
wide audit in issue #7.

- https://doi.org/10.1007/978-3-031-81202-6_8
- https://cs.uwaterloo.ca/~shallit/Papers/wilson.pdf
- https://doi.org/10.1007/s11227-025-07337-0
- https://doi.org/10.1016/0166-218X(94)00014-5
