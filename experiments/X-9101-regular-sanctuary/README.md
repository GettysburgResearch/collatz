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
  `U(odd_part(n))`, an exact lift from an odd DFA `O` to `0* O`, and the raw
  one-state suffix lift used for exact-floor state accounting.
- `search.py` — labeled-skeleton enumeration and guarded-core search.
- `spine_cegis.py` — optional Z3 proposal engine for the conditional exact-
  floor spine/gate normal form, including portable exact implication banks.
  The standard checker remains the arbiter.
- `odd_suffix_cegis.py` — optional Z3 proposal engine for L-9111's structured
  71-state suffix normal form. It checks `U` exactly and then requires the
  unchanged shortcut verifier to accept the one-state lift.
- `paired_gate_census.py` — durable generation-barrier coordinator for the 69
  structured suffix/raw gate pairs, with Z3-free exact artifact replay.
- `reset_spine.py` — standard-library-only reset-pattern construction and
  concrete-clause coverage audit for L-9113.
- `symbolic_minimum.py` — Boolean ripple-carry and local distance-budget model
  for the 1-preferred minimum-length word used by L-9114.
- `check_certificate.py` — Python-standard-library-only JSON certificate verifier.
- `run.py` — deterministic baseline driver.
- `test_regular_sanctuary.py`, `test_independent_check.py`,
  `test_odd_core.py`, `test_spine_cegis.py`, `test_odd_suffix_cegis.py`,
  `test_paired_gate_census.py`, `test_reset_spine.py`, and
  `test_symbolic_minimum.py` — adversarial regression suites.
- `results/control-3n-minus-1.json` — known-cycle positive-control certificate.
- `results/summary.json` — frozen original baseline.
- `results/spine-cegis-diagnostic.json` — five-state solver-engine diagnostic.
- `results/spine-q72-gate0-scout.json` — checkpoint after two bounded gate-0
  exact-floor scout sessions.
- `results/spine-q72-gate0-bank.json` — portable bank of the 213 exact
  implications learned by that frozen scout; source status is retained only
  as non-authoritative provenance and is not target accounting or evidence.
- `results/spine-q72-gate3-seeded-scout.json` — bounded raw gate-3 scout seeded
  by the portable bank.
- `results/odd-suffix-cegis-diagnostic.json` — five-state suffix-engine
  diagnostic.
- `results/odd-suffix-q71-gate2-scout.json` — bounded unseeded suffix gate-2
  scout.
- `results/odd-suffix-q71-gate2-seeded-scout.json` — separate bounded suffix
  gate-2 scout seeded by the normalized shortcut bank.
- `results/paired-gate-census-generation0.json` — complete 138-partition
  one-model census with every model exactly replayable.
- `results/reset-spine-q71-bank-blind-spot.json` — exact q=71 concrete-factor
  coverage and 69-gate reset-spine audit.
- `results/symbolic-minimum-q71-gates2-70.json` — local carry/distance models
  for all structured suffix gates.

## Software environment

- Python 3.12.10
- Windows 11 (`Windows-11-10.0.26200-SP0`)
- trusted checker and baseline: Python standard library only
- optional synthesis: `z3-solver==4.16.0.0`, pinned in
  `requirements-search.txt`
- deterministic solver seed `0`; soft-deadline model counts remain machine-
  and solver-version-dependent because exact verification and witness batching
  finish atomically after each solver call
- `.gitattributes` pins committed result JSON to LF so documented formatted-
  file hashes do not depend on checkout line-ending conversion

## Replay commands

From this directory, the trusted checker and test discovery run as:

~~~text
python -B -m py_compile automata.py transducer.py verify.py independent_check.py odd_core.py search.py run.py check_certificate.py spine_cegis.py odd_suffix_cegis.py paired_gate_census.py reset_spine.py symbolic_minimum.py test_regular_sanctuary.py test_independent_check.py test_odd_core.py test_spine_cegis.py test_odd_suffix_cegis.py test_paired_gate_census.py test_reset_spine.py test_symbolic_minimum.py
python -B -m unittest -v
python -B check_certificate.py results/control-3n-minus-1.json --allow-nonstandard-control
python -S -B reset_spine.py --validate results/reset-spine-q71-bank-blind-spot.json
python -S -B symbolic_minimum.py --validate results/symbolic-minimum-q71-gates2-70.json
python -S -B paired_gate_census.py --validate results/paired-gate-census-generation0.json
python -B run.py --exhaustive-states 4 --approximation-depth 20
~~~

With the pinned optional Z3 dependency installed, all 104 tests pass. In a
standard-library-only environment, 77 pass and the 27 synthesis tests skip.

The optional search dependency and engine diagnostic are:

~~~text
python -m pip install -r requirements-search.txt
python -B spine_cegis.py --dry-diagnostic --seed 0 --result results/spine-cegis-diagnostic-replay.json
python -B odd_suffix_cegis.py --dry-diagnostic --seed 0 --result results/odd-suffix-cegis-diagnostic-replay.json
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

Exporting the exact implications is deterministic. Models, batches, elapsed
time, and candidates are omitted; source status remains only as
non-authoritative provenance and is never a target conclusion:

~~~text
python -B spine_cegis.py --export-bank results/spine-q72-gate0-scout.json results/spine-q72-gate0-bank-replay.json
~~~

The two seeded scouts were produced with the same logical bank but cover
different search spaces: raw gate 3 permits transitions back to its start
state, whereas the suffix lift keeps work transitions inside its 71-state
copy. Their configured soft-budget commands were:

~~~text
python -B spine_cegis.py --states 72 --gate 3 --seed 0 --max-models 100 --time-limit 20 --import-bank results/spine-q72-gate0-bank.json --result results/spine-q72-gate3-seeded-scout-replay.json
python -B odd_suffix_cegis.py --states 71 --gate 2 --seed 0 --max-models 100 --time-limit 20 --import-shortcut-bank results/spine-q72-gate0-bank.json --result results/odd-suffix-q71-gate2-seeded-scout-replay.json
~~~

The historical unseeded suffix scout used:

~~~text
python -B odd_suffix_cegis.py --states 71 --gate 2 --seed 0 --max-models 100 --time-limit 10 --result results/odd-suffix-q71-gate2-scout-replay.json
~~~

The paired generation-zero wave used four workers, a 30-second watchdog, a
one-model quota per partition, and no local-clause sharing across partitions.
The other two scientific audits use deterministic q=71 parameters:

~~~text
python -B paired_gate_census.py --output results/paired-gate-census-generation0-replay.json --watchdog 30 --workers 4
python -B reset_spine.py --output results/reset-spine-q71-bank-blind-spot-replay.json
python -B symbolic_minimum.py --states 71 --gate-min 2 --gate-max 70 --seed 0 --timeout 10 --result results/symbolic-minimum-q71-gates2-70-replay.json
~~~

All replay outputs use ignored `*-replay.json` names so the committed artifact
hashes remain stable.

The original baseline's platform-independent mathematical-result digest is:

~~~text
a06327fe24dd611b9fd2d70e24bedaa3ed2bf38242063354b7a7ede803d4cc16
~~~

Its full environment-bound summary digest is
`0e7e23e4712600b501eb2083030e149e4b92dda35cadb87c1276acc7c988dab7`.

## Frozen original baseline

- Direct standard-transducer comparison: every `1 <= n < 100000`.
- Original regression suite: 29 tests; current extended suite: 104 tests.
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
- the raw suffix lift agrees with odd-part membership below 10,000, exposes an
  accepting empty suffix as the forbidden powers of two, and preserves the
  known `3n-1` suffix cycle as a positive control;
- every portable bank clause is rechecked as an exact canonical `w -> T(w)`
  image, with integrity, provenance, cross-gate accounting, and source-free
  resume covered adversarially;
- all 213 frozen shortcut clauses normalize to exact nontrivial suffix
  `x -> U(1x)[1:]` clauses; tests specifically catch the invalid shortcut of
  dropping only one zero from an even output;
- CEGIS tests exercise batched exact implications, mandatory final
  verification, strict checkpoint validation, resume accounting, and explicit
  timeout/model-limit result boundaries;
- prefix-trie batching is formula-equivalent to asserting each implication
  separately in both raw and suffix encodings;
- paired-census tests cover outside-in scheduling, process isolation, atomic
  checkpoints, implementation provenance, strict replay, and resealed
  tampering without instantiating Z3;
- reset-spine tests exhaust the required-factor lemma through `q=7` and replay
  all 69 exact countermodels and explicit bank evaders;
- symbolic-minimum tests cover small gate-2 UNSAT instances, satisfiable path
  replay, canonical nested schemas, state-count binding, and digest tampering.

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

### Portable obstruction bank

The portable gate-0 bank contains exactly the same 213 mathematical
implications but deliberately omits the source model tables, batches, elapsed
time, and candidate. Source status is retained only as non-authoritative
provenance; it is never credited as target accounting, evidence, or a solver
conclusion. Every importer recomputes each exact `T` image before using it.
The bank's canonical payload digest is
`7dcbd52449aac567300bab540cfe10663c5c2e6b732660f6060b8dceae58e3bb`;
its formatted-file SHA-256 is
`32846c490bcb38d932ec30121ba106547b3604cb45a77e236a026f613d4c53cd`.

The matched raw 72-state gate-3 scout imported all 213 clauses, checked two
models, learned three further clauses in two batches, and stopped at its
20.016-second soft boundary with 216 clauses enforced. Its status is
`time_limit`, not UNSAT, and its SHA-256 is
`e25484c28e61cff666a408d3c2eaf5e6ef654a91fbd0532f146a0d0c55b4ad81`.

### Conditional odd-suffix lane

L-9111 removes the forced dyadic-saturation state before synthesis. A
71-state suffix DFA at the conditional floor lifts to exactly 72 raw states;
suffix gates `2,...,70` map to raw gates `3,...,71`. This is a structured
subspace: it excludes raw gate 0 and generic machines whose work transitions
return to the saturation state.

The five-state suffix diagnostic checked four models, learned ten clauses,
and returned solver-level `solver_unsat` for that engine-only space. It emits
no independent UNSAT proof. Its SHA-256 is
`a8c2b842039a9697e7f79685826dba49c52ff384c224d1dc4b24fc0cb7abfc92`.

The unseeded q=71, suffix-gate-2 scout checked six models and learned 13 exact
clauses in 10.016 seconds. Its status is `time_limit`, and its SHA-256 is
`34d5e528bad84951686adcfc4fbe00620483fd491f2037360e502dc5b31cb826`.

For a dyadically saturated candidate, each full shortcut clause can be
normalized by stripping **all** initial LSD zeros from both sides and then
removing the forced odd marker. In the frozen bank, all 213 inputs are odd;
44 one-step outputs contain low zeros and two contain more than one. The 213
unique nontrivial suffix clauses have canonical digest
`ea4dc231df8840bfe8369702b45b2bc1ba4f6bdc9a158da170b8c8a0bf8ce1cc`.
Every pair is independently checked against the exact `U` transducer.

The separately seeded q=71 gate-2 scout imported all 213 normalized clauses,
checked five models, learned 11 further clauses in five batches, and stopped
at its 20.125-second soft boundary with 224 clauses enforced. It found no
candidate; `time_limit` remains incomplete. Its SHA-256 is
`13ff21ba4f71b1b206c7a538bbff7f94a68d6fac7412001920b51a4e2ae4de07`.

The raw gate-3 and suffix gate-2 scouts share a gate correspondence but are
not equivalent search spaces or a controlled speed benchmark. Their value is
that the same exact obstruction knowledge now crosses both representations.

### Paired generation-zero census

The durable coordinator paired suffix `(q=71,h)` with raw `(q=72,h+1)` for
every `h=2,...,70`, scheduled outside-in.  Generation zero used four workers,
a 30-second per-partition watchdog, solver seed 0, and a one-model quota.  Each
partition began from the same 213-clause bank; no locally learned clause crossed
the generation barrier.

All 138 partitions produced one model.  The unchanged primary verifier and the
preimage route exactly rejected all 138, reconstructing 1,855 local implication
instances: 895 in suffix partitions and 960 in raw partitions.  There were no
zero-model stalls and no candidates.  Every status is still
`bounded_model_quota`; the artifact eliminates no partition.

The plan SHA-256 is
`9eac8ad6777cb6f3e5fe8101d22de3a3563446c7744f024c99c0450f65f6edf3`,
the semantic SHA-256 is
`3f8718a960f74daa0e4838c049626235e3dcd9030ed5772696257e5872e5e946`,
the payload SHA-256 is
`f5e076e07a58652c3fd5567bab4017b59612b9bc867a97af77a9d898f30f6078`,
and the formatted-file SHA-256 is
`5506b97bf990f568136ea6e18f691749abe6cadc046cc84ee1e28726b0cbf723`.
The no-Z3 validator replays every table, verification, relation batch, and
implementation hash.

### Reset-pattern concrete-clause audit

The frozen corpus contains 213 imported and 11 local implications, with 2,170
length-71 factor occurrences and 1,692 distinct factors.  L-9113 proves that a
concrete antecedent bank needs `2^68 = 295147905179352825856` distinct factors
to cover one fixed gate's reset-pattern family.  Adding all 69 distinguished
targeted implications raises the corpus only to 1,760 factors, and an explicit
factor-avoiding normal-form model remains at every gate.  Separately, all 69
distinguished spines are exactly rejected by both odd-core and shortcut-lift
verification.  No sanctuary is reported and no gate is eliminated.

The semantic SHA-256 is
`7851e9d0888e20e631206e66e2b373f69df3fb31f7bf45aeb92a04847d293e16`;
the formatted-file SHA-256 is
`3c32409080649bd02cf7ce1dd090e3e16dd1ac1ce958d8accc5d777354590dcd`.

### Symbolic minimum-word audit

The local ripple-carry/distance constraint is solver-UNSAT at gate 2 and
satisfiable at all 68 gates from 3 through 70.  Every satisfiable model is
reconstructed and exactly rejected by both odd-core and shortcut-lift
verification; no candidate is reported.  Solver UNSAT remains corroboration,
not a proof artifact.  L-9114's separate carry induction eliminates gate 2.

The payload SHA-256 is
`8273c8a3b3879c242323c8467d431f4f2713b46a596d47f9d2a753362c74a3b3`;
the formatted-file SHA-256 is
`5f6ed1ec31d890082819026c28634786072673060cc0275fc6a31bb9537eab57`.

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
- Generation zero touches suffix gates `2,...,70` and raw gates `3,...,71`, but
  only at a one-model quota.  These bounded statuses eliminate no partition.
  Raw gate 0 remains represented only by the earlier bounded scout.
- The 71-state suffix lane is conditional on the external verified range and
  covers only a structured subset of raw exact-floor machines.
- L-9113 constrains concrete antecedent-factor coverage only; symbolic clauses
  and arithmetic arguments are outside its lower bound.
- L-9114 excludes only gate 2 inside the exact-distance suffix normal form, not
  larger suffix automata or generic raw gate-3 machines.
- SHA-256 makes bank provenance tamper-evident, not cryptographically signed;
  logical safety instead comes from recomputing every imported exact image.
- A bounded empty kernel or a long sequence of rejected models does not support
  Collatz convergence.
- Safety approximants certify only finite orbit windows.
- The external `2^71` premise is used for search pruning and normal-form
  necessity, never for candidate-certificate soundness.
- LSD-first BFS order is not numerical order.

## Next experiment

Apply the distance-budget construction to the first two or three `U` images of
the 1-preferred minimum-length word at suffix gates `3,...,70`.  In parallel,
extract and minimize symbolic transition-cube nogoods from exact closure
failures so that one independently checkable arithmetic witness blocks many
reset patterns at once.  Keep raw gates `0,3,...,71` as the broader control,
and share revalidated clauses only across explicit generation barriers.

The primary mathematical objective is to extend L-9114's carry contradiction,
not accumulate concrete clauses whose exponential blind spot is quantified by
L-9113.  The secondary lane remains L-9112's colored refinement products with
popcount parity as the first genuinely recurrent nonslender feature.  Every
positive proposal still returns to the unchanged shortcut checker.  A proof-
producing solver or separately authored verifier is required before promoting
any negative solver claim.
