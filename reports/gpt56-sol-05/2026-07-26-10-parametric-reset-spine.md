# Session report: exact parametric reset-spine closure

- **Agent:** `gpt56-sol-05`
- **Issue:** [#10](https://github.com/gfreund123/collatz/issues/10)
- **Branch:** `cursor/parametric-reset-spine-8f0f`
- **Date:** 2026-07-26

## Starting hypothesis

The `2^68` reset patterns at each active q=71 suffix gate should be treated as
one finite symbolic transition system, not with plain concrete CEGIS. A
guarded product reachability computation could either find a closure-safe
assignment, prove all assignments bad, or preserve an honest `UNKNOWN`
boundary.

The main logical risk was quantifier handling: a SAT encoding with
reachability variables must not permit a model to hide concretely reachable
bad states.

## Approaches attempted

1. Read the repository operating rules, X-9101 transducer and both closure
   verifiers, the odd-core lift, L-9113, L-9114, their tests and artifacts, the
   issue history, and the only prior issue-10 report.
2. Searched the branch, issue comments, and pull requests for X-9102,
   O-9102, parametric reset-spine classification, SAT proof logging, and
   overlapping work. No duplicate implementation or claim existed.
3. Detected local solver support. No `kissat`, `cadical`, `minisat`,
   `glucose`, `cryptominisat`, `z3`, `drat-trim`, `gratgen`, `lrat-check`, or
   `cake_lpr` executable was present; Python modules `z3`, `pysat`, and
   `pycosat` were absent.
4. Implemented a standard-library ROBDD manager and exact least guarded
   product fixed point over input DFA state, X-9101 transducer state, output
   DFA state, and canonical endpoint monitors.
5. Exhaustively compared symbolic classification with every materialized
   reset-pattern DFA for `q=3,...,8` through X-9101's unchanged
   `verify_candidate`.
6. Attempted to expand the full symbolic output-state partition directly at
   q=71. One gate showed exponential intermediate ROBDD growth and reached
   about 8.4 GB RSS before completion; the process was stopped. This route was
   retained only as the small-q differential engine and complete fallback.
7. Derived a compact universal parametric witness. For each assignment,
   `1 c[0]...c[q-2]1` is accepted. Its exact shortcut image can contain the
   required reset pattern in only four alignments, and elementary shortcut
   equations exclude all four.
8. Replaced the q=71 expansion with a linear guarded input/transducer trace
   plus the exact factor-alignment terminal decision. This proves all
   assignments bad without enumerating them or relying on a solver.
9. Wrote a separate standard-library checker that imports neither the
   generator nor X-9101. It reconstructs the five-state carry identities,
   terminal flush, canonical lift, guarded trace, four arithmetic cases, and
   any materialized SAT candidate.
10. Generated and independently replayed the deterministic q=71 artifact.

## New results

### Proposed exact observation

O-9102 states that every L-9113 reset-pattern suffix spine fails closure.
This holds for every `q>=3` and every legal gate, not only q=71.

For the accepted word `w(c)`, write `m=[w(c)]`. Since `c[0]=1`, `m=3 mod 4`,
so `T(m)=(3m+1)/2` is odd. The output suffix has length `q` or `q+1`. If it
were accepted, L-9113 requires the q-bit reset pattern as a factor. The four
alignments imply respectively

```text
T(m)=m,
T(m)=m+2^(q+1),
T(m)=2m-1,
T(m)=2m+1.
```

The shortcut equation gives `m=-1`, `m=2^(q+2)-1`, `m=3`, and `m=-1`.
All contradict `2^q<=m<2^(q+1)`.

### Exact q=71 computation

X-9102 classified gates `3,...,70`:

```text
SAT       0
UNSAT    68
UNKNOWN   0
```

Each gate covers exactly
`2^68 = 295147905179352825856` parameter assignments. Across the 68 active
gates, the certificates cover
`20070057552195992158208` `(gate,c)` pairs.

Artifact:

```text
experiments/X-9102-parametric-reset-spine/results/
  parametric-reset-spine-q71-gates3-70.json
```

Semantic-result SHA-256:

```text
2116fb81d40b6de21c6df8306fa135d9d0ca5ec4a7583fa558a33930bfe9b680
```

Formatted-file SHA-256:

```text
aad5b12ab1249d83adde64c0e9790b160a6d7ecd5212c818cc277bc138f9b876
```

No CNF was emitted, so the artifact records `cnf_sha256: null`. This is not a
missing proof: every UNSAT record has the guarded parametric witness and a
separately replayed algebraic certificate. No SAT answer occurred. The code
would materialize a fixed-point SAT assignment and require both X-9101 and
the separate checker to accept its DFA.

### Quantifier correction

An existential inductive-set encoding does **not** need to force `R` to be
the least reachable set. It is exact when it includes:

```text
R(start),
R(v) and edge_guard(v,w,c) => R(w),
R contains no bad endpoint.
```

For a fixed assignment `c`, induction on path length forces every reachable
state into any such `R`, so arbitrary omission is impossible. Conversely,
the least reachable set supplies `R` whenever the bad endpoint is
unreachable. The encoding becomes unsound only if start inclusion or guarded
closure is omitted. X-9102 uses forward least reachability directly.

## Validation

- Every one of 321 candidates for `q=3,...,8`, all legal gates, and every
  parameter assignment was materialized and rejected by X-9101's existing
  verifier.
- The explicit ROBDD guarded trace agrees with the compact certificate on all
  321 candidates.
- The full guarded least fixed point agrees through `q=6`.
- One q=71 assignment at each active gate was materialized and rejected by
  X-9101 as an integration check.
- The separate checker validates all 68 q=71 UNSAT proofs.
- Adversarial tests reject result-digest tampering, resealed guarded-coverage
  tampering, resealed arithmetic-proof tampering, false CNF metadata,
  duplicate JSON keys, and nonfinite JSON.

## Candidate counterexamples

None. No reset-pattern DFA is a sanctuary, and no ordinary Collatz
counterexample is claimed.

## Failed approaches

The literal q=71 ROBDD expansion of all symbolic output-DFA state guards is a
poor representation. Although the number of product configurations stayed
moderate at small q, the guard functions accumulated exponentially many BDD
nodes; one q=71 gate consumed about 8.4 GB before being stopped. This failure
is preserved in the design: explicit ROBDD expansion remains a small-q
differential check and general fallback, while the q=71 proof uses the
arithmetic factor abstraction.

Plain CEGIS bound extension was not attempted. L-9113 already proves why
concrete antecedent accumulation is mismatched to this family.

## Potential errors

- The required-factor step imports L-9113. Its backward-run argument should be
  reconstructed by another agent together with the four output alignments.
- The separate checker and generator have different implementations but the
  same author. This is not independent review.
- O-9102 concerns nonadvancing transitions that all reset to `r0`. It must not
  be generalized to arbitrary upper-Hessenberg exact-distance suffix DFAs.
- Gate 2 is covered here only for the reset subfamily; L-9114 remains the
  broader gate-2 result.
- `UNSAT` eliminates a finite automaton family. It is not evidence for Collatz
  convergence.

## Files changed

- `experiments/X-9102-parametric-reset-spine/README.md`
- `experiments/X-9102-parametric-reset-spine/symbolic_closure.py`
- `experiments/X-9102-parametric-reset-spine/check_result.py`
- `experiments/X-9102-parametric-reset-spine/test_symbolic_closure.py`
- `experiments/X-9102-parametric-reset-spine/requirements.txt`
- `experiments/X-9102-parametric-reset-spine/.gitignore`
- `experiments/X-9102-parametric-reset-spine/.gitattributes`
- `experiments/X-9102-parametric-reset-spine/results/parametric-reset-spine-q71-gates3-70.json`
- `research/regular-sanctuary/claims/O-9102-parametric-reset-spine.md`
- `research/regular-sanctuary/CLAIMS.md`
- `research/regular-sanctuary/README.md`
- this report

## Claims affected

- `O-9102` — new, `PROPOSED`
- `X-9102` — new, `EMPIRICAL` experiment record with exact replayable
  certificates
- `L-9113` — not changed; its reset family and required-factor lemma are used
- `L-9114` — not changed; its broader gate-2 scope is preserved

## Recommended next actions

1. Independently reconstruct O-9102 from the finite-run factor argument and
   the four alignment equations.
2. Relax each nonadvancing transition from fixed target `r0` to a small
   symbolic choice among earlier states. Determine what replaces the
   required-factor invariant.
3. Retain exact least guarded reachability for candidate adjudication, but use
   arithmetic abstractions rather than raw BDD expansion when guard functions
   grow exponentially.
4. If a future partition reaches SAT, require the artifact to contain the
   complete DFA and replay it through both checkers before reporting it.

## Organizational improvement ideas

For symbolic family eliminations, store three boundaries separately:

1. the finite parameter specification and deterministic encoding digest;
2. the proof object or parametric witness establishing the status; and
3. a separately implemented checker receipt.

This prevents a bare solver label from being mistaken for a proof and makes
`SAT`, checkable `UNSAT`, computationally observed `UNSAT`, and `UNKNOWN`
visibly different artifact states.
