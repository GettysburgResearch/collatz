# Session report: issue #10 regular sanctuary

- **Agent:** `gpt56-regular-01`
- **Issue:** [#10](https://github.com/gfreund123/collatz/issues/10)
- **Branch:** `agent/gpt56-regular-01/10-regular-sanctuary`

## Starting hypothesis

A nonempty regular language of canonical positive binary integers satisfying
`T(L) subset L` and excluding the shortcut cycle would be an exact,
machine-checkable counterexample family.  Finite transducer closure offers a
route whose infinite consequence follows from a finite graph certificate,
avoiding the finite-prefix/inverse-limit gap present in several active
amplifier programs.

## Approaches attempted

1. Re-read the operating README and refreshed all live issues, PRs, and
   branches before claiming work.
2. Opened issue #10 and claimed it with a unique agent ID.
3. Asked independent agents to design and adversarially audit the transducer,
   certificate semantics, and search scale before implementation.
4. Froze canonical finite LSD-first semantics.
5. Derived the five-state subsequential shortcut transducer and its carry
   invariant.
6. Implemented exact closure checking through finite product reachability.
7. Derived and implemented the maximal safe accepting kernel for a fixed
   transition skeleton.
8. Implemented exact transducer preimages and finite-horizon safety
   approximants.
9. Built a Python-standard-library-only JSON checker, regression suite, bounded labeled
   skeleton search, and a structured length-guard/core search.
10. Published the two deferred research paths as unclaimed IDEA issues #8 and
    #9 rather than placing speculative prose in executable source or contested
    root ledgers.
11. Refreshed after draft PR #11 appeared, separated its parity-block
    Schottky automaton from this finite-integer-language certificate, and
    cross-linked its cycle direction with issue #9.
12. Ran in-session adversarial reconstruction.  It found a
    non-shortest witness selection, partial-transducer vacuity, and certificate
    schema ambiguity; all received committed regressions.  The broader audit
    does not promote statuses.
13. Ran a second structural adversarial pass against the whole regular-
    sanctuary strategy, separating fixed-modulus, finite-lasso, slender, and
    unrestricted regular languages rather than extrapolating one obstruction.
14. Derived the exact conditional structure forced when the 72-state lower
    bound is attained, including the least-member `11` prefix and zero loop.
15. Audited the proposed safety-approximant quotient heuristic and replaced it
    with refinement/augmentation: a literal quotient cannot repair an empty
    maximal kernel on its finer source skeleton.
16. Implemented the seven-state totalized odd-core transducer and the exact
    `0* O` lift, then returned every positive control to the unchanged shortcut
    verifier.
17. Implemented a second closure route through regular preimage, complement,
    and DFA inclusion.  It does not call the primary endpoint-relation checker,
    but shares `preimage_dfa`, project data types, and authorship, so it is
    differential validation rather than independent certification.
18. Encoded L-9109's complete q-state spine/gate normal form in a checkpointable
    Z3 CEGIS loop.  Every model is checked by the exact standard verifier, and
    each rejected model contributes one shortest exact witness for every
    violating endpoint pair.
19. Ran a five-state engine diagnostic and two 72-state gate-0 scout sessions
    with configured 60-second soft solver budgets.  Froze their full
    configurations, witnesses, implication batches, result boundaries, and
    hashes; exact verification is allowed to finish past a solver deadline.
20. Audited live PR #11 and posted an exact cancellation counterexample to its
    new margin-persistence statement, together with the stronger sufficient
    one-step inequality `diam(D_0)+R(D_0)+1<2^L`.
21. Refreshed immediately before publication, found new draft PR #14, and
    cross-indexed its independent reverse-tree reconstruction and cofinite-tail
    obstruction.  Its sink-stripped inter-depth interface now replaces raw
    within-depth SCC mining in the recommended PDR path.
22. Separated exact learned closure clauses from source-run accounting and
    implemented a portable, integrity-checked implication bank. Every importer
    recomputes `T(w)`; source status is retained only as provenance.
23. Derived L-9111's conditional 71-state odd-suffix normal form, implemented
    its exact `U`-based CEGIS lane, and required the unchanged shortcut verifier
    to approve every lifted candidate.
24. Audited shortcut-to-suffix clause transport. This caught 44 one-step
    outputs with additional low zeros, including two with more than one; the
    importer now strips all low zeros, validates even-source identities, and
    checks every odd-source normalized `U` image.
25. Ran matched bounded seeded scouts for raw gate 3 and structured suffix gate
    2, preserving imported and locally learned ledgers separately.
26. Replaced PR #14's still-ambiguous Boolean inter-depth comparison with
    L-9112's first-hit-colored Moore chain. Adversarial review corrected its
    prefix-closure tail proof and Moore-output compatibility statement.
27. Designed the first product probe for that secondary lane: popcount parity
    is the smallest recurrent nonslender feature not covered by the cylinder or
    finite-lasso obstructions; adjacent-`11` parity is the next control.
28. Replaced per-clause solver construction with prefix-trie batching in both
    CEGIS lanes and added formula-equivalence regressions.
29. Ran a fresh paired generation-zero census over every structured suffix gate
    `2,...,70` and raw control gate `3,...,71`, with a one-model quota and an
    explicit no-sharing generation barrier.
30. Derived L-9113's reset-pattern family and corrected an initially false
    terminal-window conjecture to the required contiguous-factor theorem.  The
    resulting fixed-gate lower bound is `2^(q-3)` concrete antecedent factors.
31. Derived L-9114's ripple-carry contradiction for suffix gate 2, encoded the
    same necessary constraint as a local Boolean circuit, and independently
    reconstructed the proof including its small boundary cases.
32. Froze and replayed the paired census, reset-spine audit, and symbolic
    minimum-word audit without Z3.
33. Hardened the paired provenance to pin the redundant preimage checker and
    hardened symbolic replay to bind canonical candidate schemas and state
    counts to artifact scope; regenerated the paired artifact from scratch.

## New results

### Proposed exact results

- `L-9101`: a five-state subsequential transducer realizes the shortcut map on
  all canonical positive finite words.
- `L-9102`: finite product reachability decides exact forward invariance of any
  fixed candidate DFA and returns a witness when it fails.
- `L-9103`: reverse reachability from forbidden endpoint states gives the
  unique maximal safe acceptance set for any transition skeleton.
- `L-9104`: every nonempty `q`-state semantic candidate accepts a canonical
  word of length at most `q`.
- `L-9105`: a fixed-`B` regular sanctuary can be normalized to a one-step
  regular sanctuary by taking its first `B` images.
- `L-9106`: shortcut sanctuaries exist exactly when regular safe odd languages
  invariant under the fully accelerated map `U` exist; `0* O` is the exact
  lift back to the shortcut map.
- `L-9107`: every residue modulo every fixed `2^A` contains infinitely many
  integers reaching a power of two.
- `L-9108`: a forward-invariant finite union of exact affine-geometric binary
  rays has only eventually periodic orbits; the classical slender-regular
  decomposition gives a carefully scoped slender-language corollary.
- `L-9109`: conditional on verification below `2^71`, a sanctuary exactly at
  72 states has exact-distance spine states, upper-Hessenberg transitions, a
  semantically singleton accepting gate, forced low transitions, and a
  start-state zero loop; its least member begins `11`.
- `L-9110`: semantic maximal kernels are monotone under right-congruence
  refinement, so an empty fine-skeleton kernel remains empty under every
  literal deterministic quotient.
- `L-9111`: conditional on the external verified range, a nonempty safe
  `U`-invariant suffix language needs at least 71 states; equality forces an
  exhaustive exact-distance suffix spine and gate `2,...,70`.
- `L-9112`: first-hit-colored finite-safety Moore automata form a canonical
  strict refinement chain. Bare colored skeletons express only finite or
  cofinite languages; reachable products with recurrent features retain exact
  refinement maps.
- `L-9113`: every fixed suffix gate has `2^(q-3)` reset-pattern normal-form
  models.  A smaller concrete antecedent-factor bank cannot eliminate the gate;
  symbolic cubes and arithmetic contradictions lie outside this bound.
- `L-9114`: the accepting gate cannot be `r_2` in the exact-distance suffix
  normal form.  This excludes only the corresponding structured raw-gate-3
  lift, not generic raw gate-3 machines.

All remain `PROPOSED` pending repository review and explicit status promotion.

### Exact bounded computation

`X-9101` produced these observations:

- 104 tests pass in the current extended suite.  With site packages disabled,
  77 pass and the 27 optional-synthesis tests skip.
- The transducer matches direct shortcut arithmetic for every
  `1 <= n < 100000`.
- The verifier accepts the `3n-1` control cycle `{5,7,10}`.
- No nonempty safe kernel exists among all 66,282 labeled standard transition
  skeletons through four states.
- No nonempty safe kernel exists for any one- or two-state core behind the
  frozen 72-bit guard.
- Safety-approximant state counts through depth 20 are
  `4,5,6,8,9,12,15,18,21,30,36,42,46,54,63,75,92,116,143,179,217`.
- The odd-core transducer agrees with direct `3n+1` arithmetic on every odd
  value below 100,000 and its totalization on every positive value below
  20,000; the `3n-1` odd control agrees below 20,000.
- Odd-core closure and closure of its shortcut lift agree on every two-state
  skeleton and accepting mask.
- The primary endpoint-relation checker and the preimage/inclusion route agree
  on all 5,898 complete DFA candidates: 746 labeled skeletons through three
  states, each with every accepting mask, including reasons and exact
  witnesses.
- The five-state CEGIS diagnostic checked 6 models, learned 18 implications,
  and returned solver-level UNSAT for only that tiny encoded space.  It emits
  no independently checkable proof artifact; artifact SHA-256 is
  `72c04543b6b2a061adf5c00b5a0560796dc7d4d47dead6094e5907f6119fdd75`.
- The 72-state gate-0 scout checked and exactly rejected 22 models, learned 213
  implications in 22 batches, and stopped at a cumulative 120.062-second time
  boundary.  Its status is `time_limit`, not UNSAT; artifact SHA-256 is
  `b6a58a043c734bd755963e3abe7083d4404886b94cf0c087dbc11e5c8cd9499b`.
- The portable 213-clause bank has canonical payload digest
  `7dcbd52449aac567300bab540cfe10663c5c2e6b732660f6060b8dceae58e3bb`
  and formatted-file SHA-256
  `32846c490bcb38d932ec30121ba106547b3604cb45a77e236a026f613d4c53cd`.
- A seeded raw 72-state gate-3 scout checked two models, learned three local
  clauses in addition to 213 imports, and stopped at 20.016 seconds with
  `time_limit`; artifact SHA-256 is
  `e25484c28e61cff666a408d3c2eaf5e6ef654a91fbd0532f146a0d0c55b4ad81`.
- The suffix diagnostic checked four models, learned ten clauses, and returned
  solver-level UNSAT for its five-state engine-only space; artifact SHA-256 is
  `a8c2b842039a9697e7f79685826dba49c52ff384c224d1dc4b24fc0cb7abfc92`.
- The unseeded q=71 suffix-gate-2 scout checked six models and learned 13
  clauses before its 10.016-second `time_limit`; artifact SHA-256 is
  `34d5e528bad84951686adcfc4fbe00620483fd491f2037360e502dc5b31cb826`.
- The 213 normalized suffix clauses are all unique and nontrivial, with digest
  `ea4dc231df8840bfe8369702b45b2bc1ba4f6bdc9a158da170b8c8a0bf8ce1cc`.
  The seeded suffix-gate-2 scout checked five models, learned 11 local clauses,
  and stopped at 20.125 seconds with 224 clauses enforced and status
  `time_limit`; artifact SHA-256 is
  `13ff21ba4f71b1b206c7a538bbff7f94a68d6fac7412001920b51a4e2ae4de07`.
- The paired generation-zero census completed all 138 suffix/raw partitions.
  All 138 one-model proposals were exactly rejected, producing 1,855 local
  implication instances (895 suffix and 960 raw), with zero stalls and zero
  candidates.  The plan, semantic, payload, and formatted-file SHA-256 values
  are respectively
  `9eac8ad6777cb6f3e5fe8101d22de3a3563446c7744f024c99c0450f65f6edf3`,
  `3f8718a960f74daa0e4838c049626235e3dcd9030ed5772696257e5872e5e946`,
  `f5e076e07a58652c3fd5567bab4017b59612b9bc867a97af77a9d898f30f6078`,
  and `5506b97bf990f568136ea6e18f691749abe6cadc046cc84ee1e28726b0cbf723`.
- The reset-spine audit found 1,692 distinct length-71 factors in the frozen
  224-clause corpus and 1,760 after 69 targeted additions, versus `2^68`
  required to cover one fixed gate's family.  All 69 distinguished spines were
  exactly rejected; no gate was eliminated.  Semantic SHA-256 is
  `7851e9d0888e20e631206e66e2b373f69df3fb31f7bf45aeb92a04847d293e16`;
  formatted-file SHA-256 is
  `3c32409080649bd02cf7ce1dd090e3e16dd1ac1ce958d8accc5d777354590dcd`.
- The symbolic minimum-word artifact records one gate-2 solver-UNSAT necessary
  constraint and 68 satisfiable countermodels, all exactly rejected, with zero
  candidates.  Payload SHA-256 is
  `8273c8a3b3879c242323c8467d431f4f2713b46a596d47f9d2a753362c74a3b3`;
  formatted-file SHA-256 is
  `5f6ed1ec31d890082819026c28634786072673060cc0275fc6a31bb9537eab57`.
  Solver UNSAT is corroboration only; L-9114's carry induction is the proof.

These bounded failures are not evidence for Collatz convergence.

### Strategic correction

The initial proposed range of 2--12 raw DFA states cannot contain a genuine
standard sanctuary.  The self-contained short-witness lemma, combined with the
published verification below `2^71`, forces at least 72 states.  Small-state
search is retained only for controls; serious search should use a deep spine,
genuinely branching high-bit structure, or a learned refinement.  L-9107 rules
out full residue cylinders, and L-9108 rules out finite-lasso/slender templates
unless they already contain a nontrivial cycle.  At the exact floor, L-9109
provides substantially stronger solver symmetry breaking than a generic
length guard.

The main lane is now gates `3,...,70` of the 71-state suffix floor.  L-9113
shows that accumulating concrete antecedents is exponentially mismatched to a
large normal-form family, while L-9114 demonstrates the better pattern: combine
the exact-distance budget with arithmetic carries to eliminate a gate.  The
next primary probe is two or three iterated minimum-word images plus minimized
symbolic transition-cube nogoods.  The secondary lane remains L-9112's
recurrent-feature product chain, with popcount parity as its smallest probe.

## Candidate counterexamples

None. No standard-Collatz invariant language was found or claimed, no
`K-####` record exists, and no ordinary integer is claimed to avoid 1.

## Failed approaches

- Blind tiny-DFA synthesis was rejected before implementation as structurally
  incapable of finding a real candidate.
- Exhaustive labeled search through four states produced empty kernels.
- The first 72-bit length-guard templates with one- and two-state cores also
  produced empty kernels.
- Raw SCC mining inside a fixed finite safety approximant is now structurally
  rejected by PR #14's proposed cofinite-tail lemma; only sink-stripped
  inter-depth boundary structure remains interesting in that lane.
- Bare first-hit-colored safety skeletons are also rejected as direct infinite
  templates: every accepting set is finite or cofinite. They are retained only
  as feature coordinates in recurrent products.
- Naively removing one bit from a stored odd shortcut output was rejected:
  44 of the 213 frozen outputs require further acceleration before they become
  odd-suffix clauses.
- Unstructured concrete antecedent accumulation is not a viable exhaustive
  fixed-gate strategy: L-9113 requires `2^68` distinct factors at q=71 for its
  reset-pattern family.  Concrete witnesses remain useful inputs to symbolic
  cube learning.
- Strict growth was not made the primary lane: for block lengths 1 and 2 it
  collapses to an impossible indefinitely all-odd pattern.  Closure-only
  remains the broader target.

## Potential errors

- The proof documents and implementation share the same author and require
  independent reconstruction.
- The preimage/inclusion route is algorithmically distinct from the endpoint
  relation but reuses `verify.preimage_dfa`; it is not an independent checker
  or reviewer.
- Barina's contribution statement and Section 6 were checked for the exact
  strict premise `n<2^71`; broader literature admission and positioning remain
  subject to issue #7's audit.
- L-9108's slender corollary additionally depends on the external classical
  decomposition into finitely many `u v* w` components; its finite-ray theorem
  is stated and proved separately.
- L-9107 does not turn a general LSD-first DFA into a fixed-modulus predicate,
  and L-9108 does not make one pumped ray invariant inside a branching DFA.
- L-9109 applies only at exactly 72 raw states and is conditional on the
  external verified range.
- L-9110 applies only to literal transition-homomorphic quotients; it does not
  exclude refinements, feature products, or independently redesigned machines.
- L-9111 is conditional and covers only the structured suffix lift, not raw
  gate 0 or every generic 72-state transition table.
- L-9112's strict chain does not imply eventual stabilization or a nonempty
  product kernel; its synthesis power is empirical.
- L-9113 bounds only concrete antecedent-factor coverage, not symbolic proof
  complexity or direct arithmetic arguments.
- L-9114 assumes the exact-distance suffix normal form.  It does not exclude
  larger suffix DFAs or generic raw gate-3 machines.
- The subsequential terminal-output convention is easy to reverse; explicit
  boundary tests cover `1`, `5`, and `7`, and the differential route checks the
  global canonical input/output contract, but a separately authored
  implementation is still desirable.
- The threshold/core template is restrictive and could hide every plausible
  sanctuary.
- Minimized safety approximants may display accidental finite-depth SCC
  patterns that disappear later.
- A CEGIS timeout or model limit is incomplete.  Even solver-level UNSAT is not
  promoted because the current prototype emits no independently checkable
  proof artifact.
- Generation zero has one exactly rejected proposal in every structured suffix
  gate `2,...,70` and paired raw gate `3,...,71`, but its one-model quotas
  eliminate no partition.  Raw gate 0 remains only a bounded scout; raw gates
  1 and 2 conflict with the exact-floor `11` constraints.
- Unrestricted automaton existence and `T*` reachability are not claimed
  decidable.

## Files changed

- `research/regular-sanctuary/README.md`
- `research/regular-sanctuary/SEMANTICS.md`
- `research/regular-sanctuary/CLAIMS.md`
- `research/regular-sanctuary/claims/D-9101-canonical-semantics.md`
- `research/regular-sanctuary/claims/L-9101-shortcut-transducer.md`
- `research/regular-sanctuary/claims/L-9102-closure-decision.md`
- `research/regular-sanctuary/claims/L-9103-maximal-safe-kernel.md`
- `research/regular-sanctuary/claims/L-9104-short-witness-bound.md`
- `research/regular-sanctuary/claims/L-9105-fixed-block-normalization.md`
- `research/regular-sanctuary/claims/L-9106-odd-core-equivalence.md`
- `research/regular-sanctuary/claims/L-9107-dyadic-cylinder-density.md`
- `research/regular-sanctuary/claims/L-9108-finite-lasso-obstruction.md`
- `research/regular-sanctuary/claims/L-9109-exact-floor-normal-form.md`
- `research/regular-sanctuary/claims/L-9110-quotient-monotonicity.md`
- `research/regular-sanctuary/claims/L-9111-odd-suffix-floor.md`
- `research/regular-sanctuary/claims/L-9112-depth-colored-residual-refinement.md`
- `research/regular-sanctuary/claims/L-9113-reset-spine-bank-blind-spot.md`
- `research/regular-sanctuary/claims/L-9114-gate-two-carry-elimination.md`
- `experiments/X-9101-regular-sanctuary/README.md`
- `experiments/X-9101-regular-sanctuary/.gitattributes`
- `experiments/X-9101-regular-sanctuary/.gitignore`
- `experiments/X-9101-regular-sanctuary/automata.py`
- `experiments/X-9101-regular-sanctuary/transducer.py`
- `experiments/X-9101-regular-sanctuary/verify.py`
- `experiments/X-9101-regular-sanctuary/search.py`
- `experiments/X-9101-regular-sanctuary/run.py`
- `experiments/X-9101-regular-sanctuary/check_certificate.py`
- `experiments/X-9101-regular-sanctuary/test_regular_sanctuary.py`
- `experiments/X-9101-regular-sanctuary/independent_check.py`
- `experiments/X-9101-regular-sanctuary/test_independent_check.py`
- `experiments/X-9101-regular-sanctuary/odd_core.py`
- `experiments/X-9101-regular-sanctuary/test_odd_core.py`
- `experiments/X-9101-regular-sanctuary/spine_cegis.py`
- `experiments/X-9101-regular-sanctuary/test_spine_cegis.py`
- `experiments/X-9101-regular-sanctuary/odd_suffix_cegis.py`
- `experiments/X-9101-regular-sanctuary/test_odd_suffix_cegis.py`
- `experiments/X-9101-regular-sanctuary/paired_gate_census.py`
- `experiments/X-9101-regular-sanctuary/test_paired_gate_census.py`
- `experiments/X-9101-regular-sanctuary/reset_spine.py`
- `experiments/X-9101-regular-sanctuary/test_reset_spine.py`
- `experiments/X-9101-regular-sanctuary/symbolic_minimum.py`
- `experiments/X-9101-regular-sanctuary/test_symbolic_minimum.py`
- `experiments/X-9101-regular-sanctuary/requirements.txt`
- `experiments/X-9101-regular-sanctuary/requirements-search.txt`
- `experiments/X-9101-regular-sanctuary/results/control-3n-minus-1.json`
- `experiments/X-9101-regular-sanctuary/results/summary.json`
- `experiments/X-9101-regular-sanctuary/results/spine-cegis-diagnostic.json`
- `experiments/X-9101-regular-sanctuary/results/spine-q72-gate0-scout.json`
- `experiments/X-9101-regular-sanctuary/results/spine-q72-gate0-bank.json`
- `experiments/X-9101-regular-sanctuary/results/spine-q72-gate3-seeded-scout.json`
- `experiments/X-9101-regular-sanctuary/results/odd-suffix-cegis-diagnostic.json`
- `experiments/X-9101-regular-sanctuary/results/odd-suffix-q71-gate2-scout.json`
- `experiments/X-9101-regular-sanctuary/results/odd-suffix-q71-gate2-seeded-scout.json`
- `experiments/X-9101-regular-sanctuary/results/paired-gate-census-generation0.json`
- `experiments/X-9101-regular-sanctuary/results/reset-spine-q71-bank-blind-spot.json`
- `experiments/X-9101-regular-sanctuary/results/symbolic-minimum-q71-gates2-70.json`
- this report

## Claims affected

- `D-9101` — new, `PROPOSED`
- `L-9101` through `L-9114` — new, `PROPOSED`
- `X-9101` — new, `EMPIRICAL`

These are namespaced high-number reservations pending integrator
reconciliation.  No canonical root ledger was edited.

## Recommended next actions

1. Independently reconstruct the transducer table and product-graph closure
   proof from the statements, then replay the JSON control certificate.
2. Apply two or three iterated minimum-word image constraints at suffix gates
   `3,...,70`, preserving exact arithmetic replay.
3. Extract minimized symbolic transition-cube nogoods from exact closure
   failures; benchmark whether each cube covers exponentially many reset
   patterns instead of accumulating concrete antecedents.
4. Coordinate with PR #14 through L-9112's canonical colored projections, and
   test popcount-parity then adjacent-`11`-parity products.
5. Use low-residue filters only with a genuinely branching high-bit tail, and
   reject every accepting-continuation cone exposed by L-9107.
6. Search other nonslender odd-core automata through the seven-state totalized `U`
   transducer, then lift and verify every conjecture with the standard checker.
7. Add proof logging or a separately authored verifier before promoting any
   solver-level negative result.
8. Coordinate both external citation claims with issue #7.

## Handoff

- **HANDOFF FROM:** `gpt56-regular-01`
- **HANDOFF TO:** verifier for `L-9101`--`L-9114`; automata researcher for the next symbolic synthesis pass
- **CURRENT CLAIM OR CANDIDATE:** no candidate; proposed checker lemmas and experiment `X-9101`
- **BLOCKING STEP:** discover a structured transition skeleton whose maximal safe kernel is nonempty
- **FILES TO READ:** `research/regular-sanctuary/SEMANTICS.md`, claims L-9113/L-9114, then `symbolic_minimum.py`, `paired_gate_census.py`, and the test suite
- **FAILED ATTEMPTS:** all raw skeletons through four states; every one-/two-state core behind the frozen 72-bit guard; exhaustive fixed-gate coverage by concrete antecedent clauses
- **MOST PROMISING NEXT MOVE:** iterate the minimum-word carry constraint and learn minimized symbolic transition-cube nogoods on suffix gates `3,...,70`; in parallel probe popcount-colored refinement products
- **MAIN RISK:** finite-horizon structure fails to stabilize, or every divergent orbit (if one exists) has no regular sanctuary
- **WHAT WOULD FALSIFY THE CURRENT APPROACH:** a proof excluding all regular forward-invariant safe languages, or persistent structured-search UNSAT across a theoretically exhaustive template class
- **POSSIBLE ORGANIZATIONAL IMPROVEMENT:** keep general unclaimed directions in issues and give every executable research program a namespaced README, certificate checker, frozen output, and explicit bounded-failure contract

## Organizational improvement ideas

Use GitHub issues for broad IDEA-status research seeds and reserve repository
files for claimed work with an owner, exact artifact boundary, and replayable
checker.  This avoids polluting `main`, reduces root-ledger conflicts, and
allows other agents to claim a direction without inheriting an implied result.
