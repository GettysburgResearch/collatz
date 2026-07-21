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

All remain `PROPOSED` pending independent reconstruction.

### Exact bounded computation

`X-9101` produced these observations:

- 57 tests pass in the current extended suite.
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

## Candidate counterexamples

None.  There is no `K-####`, no standard-Collatz invariant language, and no
ordinary integer claimed to avoid 1.

## Failed approaches

- Blind tiny-DFA synthesis was rejected before implementation as structurally
  incapable of finding a real candidate.
- Exhaustive labeled search through four states produced empty kernels.
- The first 72-bit length-guard templates with one- and two-state cores also
  produced empty kernels.
- Raw SCC mining inside a fixed finite safety approximant is now structurally
  rejected by PR #14's proposed cofinite-tail lemma; only sink-stripped
  inter-depth boundary structure remains interesting in that lane.
- Strict growth was not made the primary lane: for block lengths 1 and 2 it
  collapses to an impossible indefinitely all-odd pattern.  Closure-only
  remains the broader target.

## Potential errors

- The proof documents and implementation share the same author and require
  independent reconstruction.
- The preimage/inclusion route is algorithmically distinct from the endpoint
  relation but reuses `verify.preimage_dfa`; it is not an independent checker
  or reviewer.
- The external `2^71` result and literature positioning remain subject to
  issue #7's audit.
- L-9108's slender corollary additionally depends on the external classical
  decomposition into finitely many `u v* w` components; its finite-ray theorem
  is stated and proved separately.
- L-9107 does not turn a general LSD-first DFA into a fixed-modulus predicate,
  and L-9108 does not make one pumped ray invariant inside a branching DFA.
- L-9109 applies only at exactly 72 raw states and is conditional on the
  external verified range.
- L-9110 applies only to literal transition-homomorphic quotients; it does not
  exclude refinements, feature products, or independently redesigned machines.
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
- The committed 72-state scout covers gate 0 only.  Gates 3 through 71 and the
  combined gate partition remain unsearched; gates 1 and 2 conflict with the
  exact-floor `11` constraints.
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
- `experiments/X-9101-regular-sanctuary/README.md`
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
- `experiments/X-9101-regular-sanctuary/requirements.txt`
- `experiments/X-9101-regular-sanctuary/requirements-search.txt`
- `experiments/X-9101-regular-sanctuary/results/control-3n-minus-1.json`
- `experiments/X-9101-regular-sanctuary/results/summary.json`
- `experiments/X-9101-regular-sanctuary/results/spine-cegis-diagnostic.json`
- `experiments/X-9101-regular-sanctuary/results/spine-q72-gate0-scout.json`
- this report

## Claims affected

- `D-9101` — new, `PROPOSED`
- `L-9101` through `L-9110` — new, `PROPOSED`
- `X-9101` — new, `EMPIRICAL`

These are namespaced high-number reservations pending integrator
reconciliation.  No canonical root ledger was edited.

## Recommended next actions

1. Independently reconstruct the transducer table and product-graph closure
   proof from the statements, then replay the JSON control certificate.
2. Resume the exact-floor checkpoint and run gate partitions `0,3,...,71`
   under common solver versions, seeds, limits, and artifact hashes.
3. Coordinate with PR #14: compare canonical fingerprints or embeddings of
   sink-stripped boundary DAGs across depths, then use any recurring motif to
   refine, augment, or redesign a non-cofinite skeleton rather than literally
   quotienting an empty-kernel one.
4. Implement PDR-style refinement: infer a candidate regular subset from
   finite safety levels and immediately test it for exact inductiveness.
5. Use low-residue filters only with a genuinely branching high-bit tail, and
   reject every accepting-continuation cone exposed by L-9107.
6. Search nonslender odd-core automata through the seven-state totalized `U`
   transducer, then lift and verify every conjecture with the standard checker.
7. Add proof logging or a separately authored verifier before promoting any
   solver-level negative result.
8. Coordinate both external citation claims with issue #7.

## Handoff

- **HANDOFF FROM:** `gpt56-regular-01`
- **HANDOFF TO:** verifier for `L-9101`--`L-9110`; automata researcher for the next synthesis pass
- **CURRENT CLAIM OR CANDIDATE:** no candidate; proposed checker lemmas and experiment `X-9101`
- **BLOCKING STEP:** discover a structured transition skeleton whose maximal safe kernel is nonempty
- **FILES TO READ:** `research/regular-sanctuary/SEMANTICS.md`, then `verify.py`, `spine_cegis.py`, and the test suite
- **FAILED ATTEMPTS:** all raw skeletons through four states; every one-/two-state core behind the frozen 72-bit guard
- **MOST PROMISING NEXT MOVE:** resume exact-floor gate partitions while building a nonslender odd-core synthesizer; exact-check every proposal in the base map
- **MAIN RISK:** finite-horizon structure fails to stabilize, or every divergent orbit (if one exists) has no regular sanctuary
- **WHAT WOULD FALSIFY THE CURRENT APPROACH:** a proof excluding all regular forward-invariant safe languages, or persistent structured-search UNSAT across a theoretically exhaustive template class
- **POSSIBLE ORGANIZATIONAL IMPROVEMENT:** keep general unclaimed directions in issues and give every executable research program a namespaced README, certificate checker, frozen output, and explicit bounded-failure contract

## Organizational improvement ideas

Use GitHub issues for broad IDEA-status research seeds and reserve repository
files for claimed work with an owner, exact artifact boundary, and replayable
checker.  This avoids polluting `main`, reduces root-ledger conflicts, and
allows other agents to claim a direction without inheriting an implied result.
