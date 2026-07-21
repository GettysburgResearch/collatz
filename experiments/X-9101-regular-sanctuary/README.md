# X-9101 — Exact Regular-Sanctuary Laboratory

- **Experiment ID:** X-9101
- **Issue:** [#10](https://github.com/gfreund123/collatz/issues/10)
- **Agent:** `gpt56-regular-01`
- **Classification:** `EMPIRICAL` bounded computation plus independently readable exact algorithms
- **Candidate counterexamples:** none

## Research question

Can a regular language of canonical finite LSD-first binary integers be made
nonempty, disjoint from `{1,2}`, and exactly forward invariant under the
shortcut Collatz map?

This first experiment builds the trusted checking layer and runs deliberately
small bounded searches.  It does not infer infinite behavior from samples.

## Files

- `automata.py` — complete DFAs, canonical encodings, minimization, finite
  languages, threshold/core templates.
- `transducer.py` — exact five-state subsequential `3n+1` and `3n-1` shortcut
  machines.
- `verify.py` — endpoint relation, exact closure witness, maximal safe kernel,
  preimages, and finite-horizon safety approximants.
- `search.py` — labeled-skeleton enumeration and guarded-core search.
- `check_certificate.py` — Python-standard-library-only JSON certificate verifier.
- `run.py` — deterministic baseline driver.
- `test_regular_sanctuary.py` — adversarial regression suite.
- `results/control-3n-minus-1.json` — known-cycle positive-control certificate.
- `results/summary.json` — frozen output of the full baseline below.

## Software environment

- Python 3.12.10
- Windows 11 (`Windows-11-10.0.26200-SP0`)
- Python standard library only
- no randomness and therefore no random seed

## Commands

From this directory:

~~~text
python -m py_compile automata.py transducer.py verify.py search.py run.py check_certificate.py test_regular_sanctuary.py
python -m unittest -v test_regular_sanctuary.py
python check_certificate.py results/control-3n-minus-1.json --allow-nonstandard-control
python run.py --exhaustive-states 4 --approximation-depth 20
~~~

The final command's platform-independent mathematical-result digest is:

~~~text
a06327fe24dd611b9fd2d70e24bedaa3ed2bf38242063354b7a7ede803d4cc16
~~~

The full environment-bound summary digest is
`0e7e23e4712600b501eb2083030e149e4b92dda35cadb87c1276acc7c988dab7`.

## Frozen parameters

- Direct standard-transducer comparison: every `1 <= n < 100000`.
- Regression suite: 29 tests.
- Finite safety approximants: depths 0 through 20.
- Labeled raw transition skeletons:
  - 1 state: 1;
  - 2 states: 16;
  - 3 states: 729;
  - 4 states: 65,536.
- Guarded template: saturating minimum length 72, with every labeled one-state
  and two-state transition core (1 and 16 cores; 73 and 146 expanded states).

## Exact output summary

- The standard transducer agreed with direct integer arithmetic throughout the
  frozen range.
- The checker accepted the `3n-1` sanctuary `{5,7,10}`.
- All 66,282 standard raw skeletons through four states had empty maximal safe
  kernels.
- Both guarded-core classes had zero nonempty kernels.
- Minimized safety-approximant state counts at depths 0--20 were:

~~~text
4, 5, 6, 8, 9, 12, 15, 18, 21, 30, 36,
42, 46, 54, 63, 75, 92, 116, 143, 179, 217
~~~

## What is rigorous versus empirical

The source implements finite graph algorithms.  Given a certificate, the
checker exhausts its finite product graph and either accepts it or returns a
concrete closure-violation witness.  The accompanying proofs are in
`research/regular-sanctuary/SEMANTICS.md` and remain `PROPOSED` until an
independent reviewer reconstructs them.

The enumeration totals and direct arithmetic comparisons are computational
observations.  They are reproducible and exact within the frozen parameters,
but they are not claims about larger automata.

## Adversarial controls

The tests include:

- the entire canonical positive language, which is closed but unsafe;
- `{1,2}`, which is closed but unsafe;
- the empty language, which fails nonemptiness;
- `{3}`, which yields the exact witness `3 -> 5`;
- the `3n-1` cycle `{5,7,10}`, which passes;
- a singleton containing a 201-bit integer, showing there is no sampling
  cutoff in closure checking;
- malformed canonical encodings and orientation metadata;
- an intentionally reversed terminal carry, which is rejected;
- comparison of the maximal kernel with every acceptance mask on every
  two-state skeleton;
- comparison of safety approximants with direct iteration.

## Limitations

- No standard-Collatz sanctuary was found.
- Four-state brute force is only an engine regression; published verification
  already forces a genuine raw candidate to at least 72 states.
- The one-/two-state guarded cores are a very narrow 72+-state template.
- A bounded empty kernel does not support Collatz convergence.
- Safety approximants certify only finite orbit windows.
- The published 72-bit pruning premise is not used in certificate soundness.
- LSD-first BFS order is not numerical order.
- The certificate checker and experiment generator share project modules;
  independent reimplementation is still required for status promotion.

## Next experiment

Use the minimized `S_d` safety automata as exact positive examples for
automata-learning/PDR-style widening.  Conjectured SCC quotients should be fed
back into `verify_candidate`; only exact one-step closure may promote a result
to a candidate.
