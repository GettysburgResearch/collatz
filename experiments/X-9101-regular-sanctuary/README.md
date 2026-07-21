# X-9101 — Exact Regular-Sanctuary Laboratory

- **Experiment ID:** X-9101
- **Issue:** [#10](https://github.com/gfreund123/collatz/issues/10)
- **Agent:** `gpt56-regular-01`
- **Classification:** `EMPIRICAL` bounded computation plus exact finite-state algorithms
- **Candidate counterexamples:** none

## Research question

Can a regular language of canonical finite LSD-first binary integers be made
nonempty, disjoint from `{1,2}`, and exactly forward invariant under the
shortcut Collatz map?

The experiment separates a small trusted checking layer from optional search
machinery. It never infers infinite behavior from samples: a proposed language
must pass exact finite-product closure before it can become a candidate.

## Files

- `automata.py` — complete DFAs, canonical encodings, minimization, finite
  languages, threshold/core templates.
- `transducer.py` — exact five-state subsequential `3n+1` and `3n-1` shortcut
  machines.
- `verify.py` — endpoint relation, exact closure witness, maximal safe kernel,
  preimages, and finite-horizon safety approximants.
- `independent_check.py` — a second closure route using regular preimage,
  complement, and inclusion. It does not call the primary endpoint-relation
  verifier, but it deliberately shares `preimage_dfa`, data types, and author;
  it is differential validation, not an independent review artifact.
- `odd_core.py` — seven-state totalized transducer for
  `U(odd_part(n))` and an exact lift from an odd DFA `O` to `0* O`.
- `search.py` — labeled-skeleton enumeration and guarded-core search.
- `spine_cegis.py` — optional Z3 proposal engine for the conditional exact-
  floor spine/gate normal form. The standard checker remains the arbiter.
- `check_certificate.py` — Python-standard-library-only JSON certificate verifier.
- `run.py` — deterministic baseline driver.
- `test_regular_sanctuary.py`, `test_independent_check.py`,
  `test_odd_core.py`, `test_spine_cegis.py` — adversarial regression suites.
- `results/control-3n-minus-1.json` — known-cycle positive-control certificate.
- `results/summary.json` — frozen original baseline.
- `results/spine-cegis-diagnostic.json` — five-state solver-engine diagnostic.
- `results/spine-q72-gate0-scout.json` — checkpoint after two bounded gate-0
  exact-floor scout sessions.

## Software environment

- Python 3.12.10
- Windows 11 (`Windows-11-10.0.26200-SP0`)
- trusted checker and baseline: Python standard library only
- optional synthesis: `z3-solver==4.16.0.0`, pinned in
  `requirements-search.txt`
- deterministic solver seed `0`; soft-deadline model counts remain machine-
  and solver-version-dependent because exact verification and witness batching
  finish atomically after each solver call

## Replay commands

From this directory, the trusted checker and test discovery run as:

~~~text
python -B -m py_compile automata.py transducer.py verify.py independent_check.py odd_core.py search.py run.py check_certificate.py spine_cegis.py test_regular_sanctuary.py test_independent_check.py test_odd_core.py test_spine_cegis.py
python -B -m unittest -v
python -B check_certificate.py results/control-3n-minus-1.json --allow-nonstandard-control
python -B run.py --exhaustive-states 4 --approximation-depth 20
~~~

With the pinned optional Z3 dependency installed, all 57 tests pass.  In a
standard-library-only environment, 51 pass and the six synthesis tests skip.

The optional search dependency and engine diagnostic are:

~~~text
python -m pip install -r requirements-search.txt
python -B spine_cegis.py --dry-diagnostic --seed 0 --result results/spine-cegis-diagnostic-replay.json
~~~

The committed 72-state gate-0 checkpoint was produced by two consecutive
configured 60-second solver-budget sessions.  The budget is soft because an
exact verification/batching pass is never interrupted:

~~~text
python -B spine_cegis.py --states 72 --gate 0 --seed 0 --max-models 100 --time-limit 60 --checkpoint results/spine-q72-gate0-scout.json --result results/spine-q72-gate0-scout.json
python -B spine_cegis.py --states 72 --gate 0 --seed 0 --max-models 100 --time-limit 60 --resume results/spine-q72-gate0-scout.json --checkpoint results/spine-q72-gate0-scout.json --result results/spine-q72-gate0-scout.json
~~~

Those historical commands intentionally show how the frozen file was made;
rerunning them would overwrite it and invalidate its integrity hash.  Continue
from the immutable snapshot through an ignored working copy instead:

~~~text
Copy-Item results/spine-q72-gate0-scout.json results/spine-q72-gate0-working.json
python -B spine_cegis.py --states 72 --gate 0 --seed 0 --max-models 100 --time-limit 60 --resume results/spine-q72-gate0-working.json --checkpoint results/spine-q72-gate0-working.json --result results/spine-q72-gate0-working.json
~~~

Likewise, direct diagnostic replays should use an ignored
`results/spine-cegis-diagnostic-replay.json` output if the committed diagnostic
hash is to remain stable.

The original baseline's platform-independent mathematical-result digest is:

~~~text
a06327fe24dd611b9fd2d70e24bedaa3ed2bf38242063354b7a7ede803d4cc16
~~~

Its full environment-bound summary digest is
`0e7e23e4712600b501eb2083030e149e4b92dda35cadb87c1276acc7c988dab7`.

## Frozen original baseline

- Direct standard-transducer comparison: every `1 <= n < 100000`.
- Original regression suite: 29 tests; current extended suite: 57 tests.
- Finite safety approximants: depths 0 through 20.
- Labeled raw transition skeletons:
  - 1 state: 1;
  - 2 states: 16;
  - 3 states: 729;
  - 4 states: 65,536.
- Guarded template: saturating minimum length 72, with every labeled one-state
  and two-state transition core (1 and 16 cores; 73 and 146 expanded states).

The baseline checker agreed with direct arithmetic, accepted the `3n-1`
sanctuary `{5,7,10}`, found empty maximal safe kernels on all 66,282 raw
standard skeletons through four states, and found empty kernels in both
guarded-core classes. Minimized safety-approximant state counts at depths
0--20 were:

~~~text
4, 5, 6, 8, 9, 12, 15, 18, 21, 30, 36,
42, 46, 54, 63, 75, 92, 116, 143, 179, 217
~~~

## Extended exact validation

The additional tests establish finite, replayable agreement boundaries:

- the odd-core `3n+1` transducer agrees with direct arithmetic for every odd
  value below 100,000 and its totalization for every positive value below
  20,000;
- the odd-core `3n-1` control agrees for every odd value below 20,000, and the
  lifted language `{2^k 5, 2^k 7 : k >= 0}` passes the unchanged shortcut
  verifier;
- odd-core closure and lifted shortcut closure agree exactly for every
  two-state DFA skeleton and accepting mask;
- the preimage/inclusion route and primary endpoint-relation route agree on
  every labeled DFA through three states and every accepting mask: 5,898
  complete candidates in total, including exact failure reasons and witnesses;
- malformed terminal behavior and noncanonical transducer output are rejected
  even when the defect lies outside a candidate's accepted language;
- CEGIS tests exercise batched exact implications, mandatory final
  verification, strict checkpoint validation, resume accounting, and explicit
  timeout/model-limit result boundaries.

## Exact-floor CEGIS observations

The five-state diagnostic checked six models, learned 18 exact implications,
and received `solver_unsat` for that tiny encoded normal-form space. This is an
engine diagnostic only. The artifact explicitly records that no independently
checkable UNSAT proof was emitted. Its SHA-256 is
`72c04543b6b2a061adf5c00b5a0560796dc7d4d47dead6094e5907f6119fdd75`.

The conditional 72-state gate-0 scout checked 22 models in two bounded
sessions, rejected every one with an exact closure witness, and accumulated
213 distinct exact implications across 22 batches. The final status is
`time_limit`; cumulative elapsed wall time is 120.062 seconds. Its SHA-256 is
`b6a58a043c734bd755963e3abe7083d4404886b94cf0c087dbc11e5c8cd9499b`.

This scout covers only gate `0`, one seed, one normal-form partition, and a
machine-dependent amount of search. It is not UNSAT, not a convergence result,
and not evidence against other gates, larger automata, or template-external
regular languages. Its value is operational: every failed proposal becomes a
sound constraint that can be checkpointed and resumed.

## What is rigorous versus empirical

The source implements finite graph algorithms. Given a certificate, the
checker exhausts its finite product graph and either accepts it or returns a
concrete closure-violation witness. The accompanying proofs are in
`research/regular-sanctuary/SEMANTICS.md` and remain `PROPOSED` until an
independent reviewer reconstructs them.

Arithmetic ranges, enumeration totals, model counts, and elapsed times are
computational observations. They are exact within the declared artifacts and
parameters but make no claim about larger automata or unbounded search.

## Limitations

- No standard-Collatz sanctuary was found.
- Four-state brute force is an engine regression; the conditional published
  verification premise forces a genuine raw candidate to at least 72 states.
- The original one-/two-state guarded cores are extremely narrow templates.
- The preimage route shares the project's `preimage_dfa` constructor and is
  not a separately authored checker.
- The optional solver emits no independently checkable UNSAT proof artifact.
- The committed 72-state search is a two-minute gate-0 scout, not an exhaustive
  partition result.
- A bounded empty kernel or a long sequence of rejected models does not support
  Collatz convergence.
- Safety approximants certify only finite orbit windows.
- The external `2^71` premise is used for search pruning and normal-form
  necessity, never for candidate-certificate soundness.
- LSD-first BFS order is not numerical order.

## Next experiment

Resume the exact-floor checkpoint and run the gate partitions `0,3,...,71`
with a common solver version, seeds, and limits, publishing a separate integrity
hash for each artifact; gates 1 and 2 are already inconsistent with the forced
`11` prefix. In parallel, synthesize nonslender odd-core DFAs
through the seven-state `U` transducer, lift every proposal to `0* O`, and make
the unchanged shortcut checker the final arbiter. A proof-producing solver or
separately authored verifier is required before promoting any negative solver
claim.
