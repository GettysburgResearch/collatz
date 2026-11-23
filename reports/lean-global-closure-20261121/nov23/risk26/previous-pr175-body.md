## Current checkpoint: direct parallel attacks on the remaining closure steps

**Full Collatz remains open.** This update strengthens the unrestricted integer-cycle restriction, supplies a complete-carry reference estimate and exact actual-law transfer, and develops broader triadic candidate constructions. The new results retain the missing numerical gcd, actual-law concentration and witness-existence steps explicitly.

Current head: `bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17`. Parent: `53ba1e1ffc46bf022433c2124a62682ad8dd4739`.

[Scientific overview](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/research/lean-global-closure-20261121/risk25/README.md) · [Reviews and execution receipts](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/reports/lean-global-closure-20261121/nov23/risk25/README.md) · [Exact source bindings](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/reports/lean-global-closure-20261121/nov23/risk25/source-bindings.json) · [Frozen file manifest](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/reports/lean-global-closure-20261121/nov23/risk25/manifest.json)

### Integer cycles: residual degree and denominator versus the largest state

For every hypothetical primitive positive integer odd cycle of period p, let d be the degree after removing the complete polynomial gcd of the carry polynomial and X^p−2^A. The new actual-numerator root bound, followed by Matveev at the reduced clock A/p=a/b, gives m≤C d^K for its minimum and d≥c p^epsilon. The latter uses the pinned injective ordinary-state count; a separate elementary distinct-state argument gives a power bound with a logarithmic loss. The safe explicit exponent is approximately 3.2186×10^−10, so this is an asymptotic structural restriction with no useful finite threshold claimed.

The recurrence lattice bounds its maximum state by

`M ≤ exp(Lambda) ((3/2)^(d−1)(m+1)−1)`.

A separate complete cyclotomic calculation, including every permitted half packet over Q(sqrt(2)), gives

`D_pol ≥ c_0 [3/sqrt(1+sqrt(2))]^d d^(−K_0)`.

Consequently D_pol/M grows at least exponentially in d up to a polynomial factor, and at least as exp(c' p^epsilon) for sufficiently large hypothetical primitive periods. The cyclotomic calculation does not use the earlier finite factor-gap certificate. Its frozen manuscript retains its initial PROPOSED header; two later independent written reviews verify CV1–CV13 at its exact bytes.

This does not prove nondivisibility. Full numerical cancellation with Q_0(3) is still possible under the proved bounds. An explicit rational denominator-five control has numerical gcd 1,015,513 despite maximum reduced numerator 2773, so a rational height bound cannot supply the missing integer-specific step.

Proofs: [residual degree](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/research/lean-global-closure-20261121/risk25/INTEGER_RESIDUAL_DEGREE.md), [recurrence lattice](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/research/lean-global-closure-20261121/risk25/RESIDUAL_RECURRENCE_LATTICE.md), [complete cyclotomic value](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/research/lean-global-closure-20261121/risk25/CYCLOTOMIC_VALUE_SEPARATION_PROPOSED.md).

### Escaping source: critical complete-carry estimate and literal transfer cost

The balanced exact-total reference family has collision at full modulus 3^m bounded by C m^(5/2) 3^(−theta m), with theta=0.949955527188... . Sublinear widening preserves the exponent. The proof keeps the complete integer carry; finite ordinary realizations exist but their sources vary.

For the unchanged actual endpoint law, repeated words are combined before squaring and every omitted atom is retained:

`Col(zeta) ≤ (sqrt((R/L) J) + tau)^2`, where `J = L sum_w p_w^2`.

The pinned strict stationary collision gap forces an exponential word-density cost or an explicitly nonnegligible remainder. Neither actual upper bound is proved. The newly refreshed fixed-clock joining extends to the actual endpoint factor, but adding or conditioning on that independent clock leaves J and tau unchanged.

Proofs: [critical carry transfer](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/research/lean-global-closure-20261121/risk25/CRITICAL_CARRY_TRANSFER.md), [late fixed-clock extension](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/research/lean-global-closure-20261121/risk25/FIXED_CLOCK_EXTENSION.md).

### Triadic construction and new Lean arithmetic

The finite Mahler attack constructs the even coefficients from earlier coefficients by triadic arithmetic and closes the first coupled odd equations. General odd-index closure remains open.

The actual-source terminal anchor −x−1 and its affine congruence class retain the full denominator after both parities occur. Every integer polynomial calibrated at the standard cycle has full-denominator resets after the actual blocks 011 and 100. Higher-digit interpolation genuinely escapes these resets: calibrated polynomials over Z[1/3] have an exactly classified value lattice, and the full Newton interpolation class realizes every legal terminal value. That larger class reproduces the original complementary-residue lattice without a new smallest-numerator bound.

[SourceAwareTails.lean](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/research/lean-global-closure-20261121/risk25/SourceAwareTails.lean) contains 26 theorem declarations for the finite carry, reset and actual-source identities. It defines actual integer iteration and proves the required affine identity internally. All twelve printed key axiom inventories contain only `propext` and `Quot.sound`. No Lean proof of the infinite analytic arguments, interpolation classification or universal witness existence is claimed.

Written constructions: [source-aware tails](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/research/lean-global-closure-20261121/risk25/SOURCE_AWARE_TRIADIC_CONSTRUCTION.md), [higher-digit interpolation](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/research/lean-global-closure-20261121/risk25/HIGHER_DIGIT_INTERPOLATION.md).

### Latest repository comparison

The initial update-sorted refresh included 145 PR records. Five heads advanced during this pass: PR182 `cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`, PR180 `7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`, PR178 `c91b80a3156e640ad471cf30c47721145ae21eb1`, PR176 `4171e1fe40e41842af9f800bd821084b724cf8f9`, and PR177 `f47a5ec51aa5853f104013a6d5046d6220ff7423`. Their relevant closing interfaces were compared at the scopes recorded in the [late comparison](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/reports/lean-global-closure-20261121/nov23/risk25/PREPUBLICATION_COMPARISON.md). Frozen proof dependencies remain byte-identical at those later heads. PR146's observed head remained unchanged.

PR178's new equivalent-flow construction removes an inverse-clock comparison rate loss. The newest cycle and triadic notes strengthen their respective interfaces, but none supplies the missing distinguished gcd bound, actual collision upper or successful universal candidate. Their older proof and computational corpora were not rerun here.

### Checks actually run

- Lean 4.34.1 author execution and an independent root execution of the copied final new source: both exit 0; empty stderr; exact source hash and all printed axiom output retained.
- New cycle checker, normal and `-O`, Python 3.12.14 / SymPy 1.14.0: six exact controls and 76 rotations; identical outputs.
- New endpoint checker, normal and `-O`: exact-total words through m=12, 3902 positive ordinary replays, 24 strip cases and 873 actual occurrence cases; identical outputs.
- `git diff --cached --check`: passed.
- Remote constructed tree matched the reviewed staged tree exactly: `4f713ef619a0588a75591ab259f03a98f7e160bf`.
- Required `python -X utf8 -B tools/validate.py` on a complete clean checkout of this exact commit: all five commands exit 0, 595 tracked files, unchanged checkout identity before and after.

These finite executions and repository integrity checks are distinct from the reviewed written mathematical arguments.

<details>
<summary>Exact final-commit checkout validation receipt</summary>

Receipt SHA256: `61bbe149516f95ec6c03f6b4f1b73f274eda91bfb5eb8ad538da3198e3416abe`.

```json
{
  "schema": "collatz-checkout-validation/v1",
  "started_utc": "2026-11-23T04:04:15.690867+00:00",
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
      "seconds": 0.085
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
      "seconds": 0.27
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
      "seconds": 0.044
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
      "seconds": 0.054
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
      "seconds": 0.051
    }
  ],
  "success": true,
  "checkout": {
    "commit": "bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17",
    "tree": "4f713ef619a0588a75591ab259f03a98f7e160bf",
    "tracked_files": 595
  },
  "checkout_after": {
    "commit": "bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17",
    "tree": "4f713ef619a0588a75591ab259f03a98f7e160bf",
    "tracked_files": 595
  },
  "finished_utc": "2026-11-23T04:04:16.231199+00:00"
}
```

</details>

### Prior checkpoints and remaining theorem

This PR retains its earlier boundary, triadic-verifier and residual-denominator work. The [preceding PR description](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/reports/lean-global-closure-20261121/nov23/risk25/previous-pr-description.json) preserves its previous status and exact-head validation receipt; the [project overview](https://github.com/GettysburgResearch/collatz/blob/bfbe3fe1e4d4d63aec866dcd8fdf97fdd0e51e17/research/lean-global-closure-20261121/README.md) links the earlier scientific packets.

The remaining full-theorem obligations are complete numerical cycle noncancellation, a critical upper bound for the unchanged actual endpoint law, and universal construction of a triadic candidate passing its own paid horizon. No full Collatz proof is claimed.
