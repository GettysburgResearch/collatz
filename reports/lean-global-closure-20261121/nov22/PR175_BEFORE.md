# PR175 description before the 22 November continuation

Observed head: 2bc2ad37b490a5aea63658eaf657bc048da4532e

## Current result and status

**Full Collatz remains OPEN.** This continuation attacked the full closing step through complete certificate induction, ordinary inverse mergers, and source-preserving analytic transport. It adds a fresh checked Lean packet and a literature-led global potential estimate with explicitly pinned analytic hypotheses.

**Published head:** `2bc2ad37b490a5aea63658eaf657bc048da4532e`
**Tree:** `88c6d3ad6977277275dde6688bea22ad1366a214`
**Lean scientific checkpoint:** `2055b8a311ab87d07bffc730154a7f8546fe382c`

[Whole-repository attack](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/research/lean-global-closure-20261121/WIDE_CLOSURE_ATTEMPT.md) · [Latest literature synthesis](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/research/lean-global-closure-20261121/LITERATURE_CLOSURE_ATTEMPT.md) · [Validation record](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/reports/lean-global-closure-20261121/wide/VALIDATION.md)

### 1. A new global weighted potential estimate — written and independently reviewed

The late refresh inspected PR177 at a0a0d76f91b4e3846c1b1f0706cad56cb6098317, PR180 at d0349de2108abb7c8fb8393c086610e3372df116, PR183 at 907a540943090968bc683b1b9246208e9053c1f8, and PR185 at 6d2765ef462fb575c49d4133b54286be7ffe68ec. The initial 143-PR inventory remains frozen separately.

Let V be PR180's canonical least excessive majorant and H(n)=V(n)/n. Under that head's displayed uniform unit-predecessor population bound, with absolute constant c, the new deduction proves:

```text
sum_{n<=X, nonperiodic odd ternary unit} V(n)/n
  <= [4*X^(39/40) + floor((3/5)*log2 X)]/c
  <= (5/c)*X^(39/40).

sum_{n nonperiodic odd unit} (V(n)/n)^p / n^s
  <= 5*s / [c^p*(s-39/40)]       (p>=1, s>39/40).

In particular:
sum V(n)/n^2 <= 200/c;    sum V(n)^2/n^3 <= 200/c^2.
```

The proof represents V by actual finite stopping cutsets. Nonperiodicity makes their complete ordinary predecessor basins disjoint, giving a weighted antichain budget. Finite reachability-chain ranks and the corrected preperiod cylinder count turn that budget into the all-target weighted upper bound. This removes the logarithmic loss of the first superlevel-only argument.

[Full deduction](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/research/lean-global-closure-20261121/CANONICAL_POTENTIAL_SUPERLEVELS.md) · [Independent exact-hash review](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/reports/lean-global-closure-20261121/wide/CANONICAL_POTENTIAL_REVIEW.md)

These are **written deductions under the stated population/finite-envelope inputs**, not Lean theorems. Nonperiodic means the target is not itself on a cycle; convergent preperiods are included. The result does not prove uniform marked sublinearity or exclude additional cycles.

### 2. Exact transport retains each original source

With h=G/n for the pinned harmonic minorant and the actual inverse Doob kernel K, every original mass a satisfies:

```text
h(q)*K^k(a/h)(q) = sum_{U^k(n)=q} Lambda_k(n)*a(n).

exp(-200/3) <= Lambda_k(n) <= 1
  on every actual path ending at a nonperiodic endpoint.
```

The correction bound is independent of depth and the moving endpoint; it uses the finite-chain count, not the population theorem. The new global moment supplies the concrete finite seed a(n)=G(n)/n^2 on the nonperiodic domain. The transformed and true source-fiber masses are comparable by the explicit fixed factor exp(200/3).

The moving-root expectation estimate needed to exclude escape is still open. The note also proves that no nonzero finite positive mixture of the stated Abel approximants is undiscounted excessive on all ordinary odd unit targets, using the actual inverse chains above 2*3^k-1.

[Source-retaining identities, mixture proof, and closing test](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/research/lean-global-closure-20261121/LITERATURE_TRANSPORT_ATTEMPT.md)

### 3. New core Lean results

| Module | Kernel-checked scope |
|---|---|
| InverseBudget | Exact normalized quotient at every actual clock; unrestricted inverse extraction with the retained ternary carry; exact cost of ancestor padding. |
| ReservedMergerCompleteness | Canonical reserved splices are equivalent to actual mergers satisfying both binary horizons. |
| MaximalReserve | One uniquely chosen maximal ternary reserve per forward clock preserves every merger within that precise domain; its leading quotient is one or two. |
| AsynchronousReset | Arbitrary source, child-target, and parent-target words can preserve the entire supplied certificate tail and decrease the common multiset under displayed exact compatibility conditions. |
| TerminalReset | Every power-of-two source is covered as a recursive case under the smaller-certificate induction hypothesis, including arbitrary supplied terminal padding. |
| PeriodicTraceTail | Finite rational weighted tail bounds and exact Collatz scaling. Infinite population substitution remains a separate written deduction. |

EndpointSteering was ported to core Lean without changing its statements. Eight PR177 dependencies are copied byte-for-byte from 00a611094043afeb256d6532b477c0709e8ed270 and authenticated by both SHA256 and Git blob IDs.

[Core sources](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/research/lean-global-closure-20261121/CollatzGlobalClosureCore.lean) · [Inverse continuation](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/research/lean-global-closure-20261121/INVERSE_CARRY_CONTINUATION.md) · [Maximal reserve](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/research/lean-global-closure-20261121/MAXIMAL_RESERVE_REDUCTION.md) · [Complete-certificate attempt](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/research/lean-global-closure-20261121/ASYNC_CLOSURE_ATTEMPT.md)

### 4. Literature-inspired global certificate and merger attempts

The typed proof-term continuation keeps nested requests unevaluated, so it does not silently reuse an uncontrolled returned certificate. The two infinite psi schemas admit a multiset/inversion orientation. The interval fusion I_e(F_d(C)) <- I_(e+d+1)(C) gives an all-gap macro reducing the supplied source clock by exactly one. Its accumulated terminal even exponent remains unbounded; the terminal reset and source-clock decrease do not yet share a complete terminating rank.

The newest PR177 interval program already closes its terminal cases and all high-gap/high-even cases. Its residual low-alphabet interval selector remains open; our older terminal psi result is not mislabeled as closing that new obligation.

Yolcu–Aaronson–Heule's relative-termination distinction and Applegate–Lagarias's semigroup proof were read directly. The resulting multiplier proposition rules out any bounded-clock uniform ordinary repair for a fixed multiplier with a prime factor outside {2,3}. It does not rule out unbounded source-dependent repairs.

[Typed continuation and exact remaining terminal condition](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/research/lean-global-closure-20261121/PROVENANCE_TERMINATION_ATTEMPT.md) · [Physical merger/literature attempt](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/research/lean-global-closure-20261121/LITERATURE_MERGER_ATTEMPT.md) · [Newest PR183 coupling](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/research/lean-global-closure-20261121/LATE_MERGER_REFRESH.md)

## Actual validation

- A fresh complete checkout of the published Lean scientific commit compiled **all 16 core source units** using Lean 4.34.1, compiler commit 5045d0056413266e57c625dcd7c365b10e377c52, warnings as errors and autoImplicit=false. LEAN_PATH contained only the fresh output directory.
- **71 axiom reports**: 69 dependency lists and two reports of no axioms. The combined set is exactly propext, Classical.choice, and Quot.sound. No sorryAx or custom Collatz axiom is reported.
- All five required repository commands passed at that scientific commit. Exact build and repository receipts are committed.
- All five required commands passed again in a clean complete checkout of **2bc2ad37b490a5aea63658eaf657bc048da4532e**, with **415 tracked files** and unchanged checkout identity.
- All 16 published source hashes still match the successful source build. Build drivers and compiler/dependency pins are unchanged. The new canonical-potential file matches the independent review's exact SHA256.
- The previous 17-unit band/legacy build keeps its own historical receipt. The expanded 32-unit aggregate was not rerun; the new core packet was executed in full. Optional bounded regressions were not repeated.

[Fresh source-build receipt](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/reports/lean-global-closure-20261121/wide/source-build.json) · [Scientific-checkout gate](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/reports/lean-global-closure-20261121/wide/repository.json) · [Scope and commands](https://github.com/GettysburgResearch/collatz/blob/2bc2ad37b490a5aea63658eaf657bc048da4532e/reports/lean-global-closure-20261121/wide/VALIDATION.md)

Final published-head repository receipt SHA256: `60ce4eafa713cd0fa11345e86f8111ec43c1b34bd8ad411f44cff8ab39cc6568`.

<details>
<summary>Actual final published-head repository receipt</summary>

```json
{
  "schema": "collatz-checkout-validation/v1",
  "started_utc": "2026-11-21T23:09:31.596153+00:00",
  "python": "3.12.14 (main, Aug 25 2026, 14:00:49) [Clang 22.1.3 ]",
  "platform": "linux",
  "scope": "structure, frozen identities and selected bounded regressions; not a proof of Collatz",
  "regressions": false,
  "commands": [
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_integration_state.py"
      ],
      "exit_code": 0,
      "stdout": "OK: durable front door and lifecycle practice; 8 integrated records (6 verified local proofs, 1 accepted refutation, 1 source-qualified periodic synthesis), 3 roadmap records, 13 reviewed research families, 314 curated local links, frozen 45/42 PR snapshot preserved.\n",
      "stderr": "",
      "seconds": 0.08
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_review_integration.py"
      ],
      "exit_code": 0,
      "stdout": "OK: 4 qualified assemblies, 9 namespaces, 14 exact blob pins, 8 exact subtree pins, 374 local links, 2 optimized guards; no mathematical verification\n",
      "stderr": "",
      "seconds": 0.261
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_review_integration.py",
        "--self-test"
      ],
      "exit_code": 0,
      "stdout": "SELF-TEST PASS: 8 invalid fixtures rejected; no repository scan or mathematical verification performed\n",
      "stderr": "",
      "seconds": 0.034
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/test_integrity_portability.py"
      ],
      "exit_code": 0,
      "stdout": "PASS: 11 real-Git mode/content/coverage controls; Windows metadata selection simulated on non-Windows; no complete repository scan\n",
      "stderr": "",
      "seconds": 0.093
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "reports/prepublic-2026-09-05/integration-d/check_followup.py",
        "--self-test"
      ],
      "exit_code": 0,
      "stdout": "PASS scoped D follow-up: 7 active files / 7 exact archived originals / 8 dispositions\n{\"overlap_band_cases\": 64, \"quotient_cases\": 81, \"scope\": \"finite edge cases only; not universal Collatz proof checking\", \"signed_residues\": 1584, \"strict_strip_counterexamples\": 2}\nInvalid scoped fixtures rejected: 8\n",
      "stderr": "",
      "seconds": 0.04
    }
  ],
  "success": true,
  "checkout": {
    "commit": "2bc2ad37b490a5aea63658eaf657bc048da4532e",
    "tree": "88c6d3ad6977277275dde6688bea22ad1366a214",
    "tracked_files": 415
  },
  "checkout_after": {
    "commit": "2bc2ad37b490a5aea63658eaf657bc048da4532e",
    "tree": "88c6d3ad6977277275dde6688bea22ad1366a214",
    "tracked_files": 415
  },
  "finished_utc": "2026-11-21T23:09:32.141017+00:00"
}
```

</details>

## Exact remaining full-theorem step

The new finite potential moments do not bound the multiplicative five-energy of an invariant component label. A proved source-retaining transfer with controlled multiplicity is still required. Taking a forward supremum already destroys harmonic integrability on the known predecessor basin of 5. The alternative constructive route still needs one total dispatcher and common well-founded rank across the low-interval cases and terminal resets. No complete selector, uniform moving-root decay, or full Collatz proof is claimed.

---

<details>
<summary>Earlier PR175 checkpoints and their original evidence</summary>

## Goal and status

**Full Collatz convergence remains OPEN.** This PR contains Lean attempts at the universal theorem. Its latest checkpoint builds directly on PR #173's new forced dyadic section, frozen at `fa0c9e2a2851e6324391e39c17afcb5913185aec`.

**Final head:** `06215e69346c4d32bf970af9c846a6894586c1e7`
**Final tree:** `43c87f6364792dfba95b212a6dd0843d9c79423e`
Scientific proof checkpoint: `d27ae7c160757a3c77e515136b1cd479a23de9b2`. The follow-up adds documentation and actual execution receipts; all Lean sources and the replay driver are unchanged.

[Band attack and remaining full-theorem gap](https://github.com/GettysburgResearch/collatz/blob/06215e69346c4d32bf970af9c846a6894586c1e7/research/lean-global-closure-20261121/BAND_ATTACK.md) · [Project guide](https://github.com/GettysburgResearch/collatz/blob/06215e69346c4d32bf970af9c846a6894586c1e7/research/lean-global-closure-20261121/README.md)

## New kernel-checked results

1. **Cofinal first-return reset.** For every factor C and cutoff L, construct an ordinary marked n>L with v₂(n+1)=1, whose actual first strictly positive marked return R(n) satisfies R(n)>C·n and v₂(R(n)+1)>C. Every coordinatewise monotone function of size and trailing-one depth fails as a strict return rank beyond a finite cutoff, even with an arbitrary preordered codomain.
2. **No arbitrary two-feature strict return rank.** Construct cofinal distinct marked endpoints of an actual positive-clock path with identical binary exponent and trailing-one depth. The entire intervening path stays above the prescribed cutoff. A separate Lean composition theorem excludes **every function of binary exponent and trailing-one depth** as a strict every-return rank, without monotonicity or linearity assumptions.
3. **Exact offset descent transfer.** A positive offset's strict descent lifts to every ordinary input sharing its entire binary prefix. A supplied convergence certificate works at its actual clock when the high-bit padding lasts that long. An explicit much thinner marked family n=2^(5m)+2^(4m)−1, together with its smaller offset, has no descent through any clock ≤5m.
4. **Ordinary construction tools.** Every finite odd-source parity cylinder occurs cofinally inside the exact marked set. A complete CRT/interval constructor supplies positive ordinary sources, exact division, the full legal word, and its endpoint identity.

[First-return construction](https://github.com/GettysburgResearch/collatz/blob/06215e69346c4d32bf970af9c846a6894586c1e7/research/lean-global-closure-20261121/SECTION_RESET_RETURNS.md) · [Equal-feature construction](https://github.com/GettysburgResearch/collatz/blob/06215e69346c4d32bf970af9c846a6894586c1e7/research/lean-global-closure-20261121/EQUAL_FEATURE_COLLISIONS.md) · [Offset closure attempt](https://github.com/GettysburgResearch/collatz/blob/06215e69346c4d32bf970af9c846a6894586c1e7/research/lean-global-closure-20261121/BAND_OFFSET_ATTEMPT.md)

## Full-theorem boundary

Ordinary descent below a marked start is weaker than descent among marked returns: its lower endpoint may be unmarked and the next mark may overshoot. The offset certificate can also outlast the available shared prefix. Neither a complete certificate transfer across the remaining ternary difference nor universal eventual marked-return descent has been proved.

The rank exclusions concern strict decrease **at every return** in the stated classes. They do not exclude richer ranks or eventual descent after a variable number of returns. No nonconvergent orbit or nontrivial positive cycle is claimed.

## Source and validation

The four PR173 source files are copied exactly, with a commit/hash manifest; they are upstream results rather than new contributions. Map/predicate composition is checked in Lean.

**Fresh complete build passed:** 17 compilation units, including the entrypoint, were compiled from their actual sources in a fresh output directory from a fresh complete GitHub checkout at the scientific commit. Every command used Lean 4.34.1, warnings as errors, disabled auto-implicit parameters, and the pinned mathlib revision. All 96 axiom reports contain only `propext`, `Classical.choice`, and `Quot.sound`; the finite reset witness has no axiom dependencies.

**Final-head gate passed:** all five required repository validation commands passed at `06215e69346c4d32bf970af9c846a6894586c1e7`, tree `43c87f6364792dfba95b212a6dd0843d9c79423e`, in the clean complete checkout with **378 tracked files**. The 17 final Lean source hashes and replay-driver hash were matched against the fresh proof-build receipt. The Lake configuration also loaded with the pinned runtime. The optional broad regression bundle was not rerun.

[Execution record](https://github.com/GettysburgResearch/collatz/blob/06215e69346c4d32bf970af9c846a6894586c1e7/reports/lean-global-closure-20261121/band/VALIDATION.md) · [Full Lean receipt](https://github.com/GettysburgResearch/collatz/blob/06215e69346c4d32bf970af9c846a6894586c1e7/reports/lean-global-closure-20261121/band/full-build.json) · [Scientific-head repository receipt](https://github.com/GettysburgResearch/collatz/blob/06215e69346c4d32bf970af9c846a6894586c1e7/reports/lean-global-closure-20261121/band/repository.json) · [Final closing attempts](https://github.com/GettysburgResearch/collatz/blob/06215e69346c4d32bf970af9c846a6894586c1e7/research/lean-global-closure-20261121/SEGMENT_MINIMUM_ATTEMPT.md)

Final-head repository receipt SHA256: `3a1621cdd1907ddb73f2f2111ff87628e0f873e10da0a2d7a0657cd76124ed99`.

<details>
<summary>Actual final-head repository execution receipt</summary>

```json
{
  "schema": "collatz-checkout-validation/v1",
  "started_utc": "2026-11-21T15:37:05.799273+00:00",
  "python": "3.12.14 (main, Aug 25 2026, 14:00:49) [Clang 22.1.3 ]",
  "platform": "linux",
  "scope": "structure, frozen identities and selected bounded regressions; not a proof of Collatz",
  "regressions": false,
  "commands": [
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_integration_state.py"
      ],
      "exit_code": 0,
      "stdout": "OK: durable front door and lifecycle practice; 8 integrated records (6 verified local proofs, 1 accepted refutation, 1 source-qualified periodic synthesis), 3 roadmap records, 13 reviewed research families, 314 curated local links, frozen 45/42 PR snapshot preserved.\n",
      "stderr": "",
      "seconds": 0.107
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_review_integration.py"
      ],
      "exit_code": 0,
      "stdout": "OK: 4 qualified assemblies, 9 namespaces, 14 exact blob pins, 8 exact subtree pins, 374 local links, 2 optimized guards; no mathematical verification\n",
      "stderr": "",
      "seconds": 0.283
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/check_review_integration.py",
        "--self-test"
      ],
      "exit_code": 0,
      "stdout": "SELF-TEST PASS: 8 invalid fixtures rejected; no repository scan or mathematical verification performed\n",
      "stderr": "",
      "seconds": 0.039
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "tools/test_integrity_portability.py"
      ],
      "exit_code": 0,
      "stdout": "PASS: 11 real-Git mode/content/coverage controls; Windows metadata selection simulated on non-Windows; no complete repository scan\n",
      "stderr": "",
      "seconds": 0.065
    },
    {
      "argv": [
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
        "-X",
        "utf8",
        "-B",
        "reports/prepublic-2026-09-05/integration-d/check_followup.py",
        "--self-test"
      ],
      "exit_code": 0,
      "stdout": "PASS scoped D follow-up: 7 active files / 7 exact archived originals / 8 dispositions\n{\"overlap_band_cases\": 64, \"quotient_cases\": 81, \"scope\": \"finite edge cases only; not universal Collatz proof checking\", \"signed_residues\": 1584, \"strict_strip_counterexamples\": 2}\nInvalid scoped fixtures rejected: 8\n",
      "stderr": "",
      "seconds": 0.054
    }
  ],
  "success": true,
  "checkout": {
    "commit": "06215e69346c4d32bf970af9c846a6894586c1e7",
    "tree": "43c87f6364792dfba95b212a6dd0843d9c79423e",
    "tracked_files": 378
  },
  "checkout_after": {
    "commit": "06215e69346c4d32bf970af9c846a6894586c1e7",
    "tree": "43c87f6364792dfba95b212a6dd0843d9c79423e",
    "tracked_files": 378
  },
  "finished_utc": "2026-11-21T15:37:06.384590+00:00"
}
```

</details>

## Earlier checkpoints retained

The PR also contains the all-width local-profile obstruction, parity-prefix merger rigidity, exact endpoint steering, deterministic relative-parity closure interface, and the recorded global rank searches. Their original claims and limitations remain in the project guide. No custom conjectural axiom, `sorry`, native evaluator shortcut, or unsafe proof mechanism supplies the unresolved universal step.


</details>
