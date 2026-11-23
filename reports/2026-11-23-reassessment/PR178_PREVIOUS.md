# PR178 before the reassessment checkpoint

Head: `c91b80a3156e640ad471cf30c47721145ae21eb1`

Title: Collatz: finite rational certificates and fast ordinary flows

# Central-step checkpoint — 23 November 2026

**Full Collatz remains OPEN.** This checkpoint adds an explicit finite certificate with arbitrary odd denominators, a constructive comparison between inverse and actual orbit collisions at every modulus, a complementary-cycle denominator bound, and an all-candidate analysis of the improved triadic budget. It was developed in four parallel lanes and independently reviewed. Twelve finite lemmas have Lean proofs; the larger results have written proofs with their formal boundary stated explicitly.

[Research packet](https://github.com/GettysburgResearch/collatz/blob/c91b80a3156e640ad471cf30c47721145ae21eb1/research/central-step-20261123/README.md) · [Reports and reviews](https://github.com/GettysburgResearch/collatz/blob/c91b80a3156e640ad471cf30c47721145ae21eb1/reports/2026-11-23-central-step/README.md) · [Exact commit](https://github.com/GettysburgResearch/collatz/commit/c91b80a3156e640ad471cf30c47721145ae21eb1)

## Why this changes the construction problem

The previous packet left a comparison-rate obligation in the collision approach and used a triadic witness search. The new ordinary flow supplies that rate constructively, while preserving the original root's entire inverse law. The new finite certificate allows every positive odd denominator, with an explicit candidate-dependent test horizon. Neither construction presupposes a universal successful witness or the missing actual-orbit collision bound.

## 1. Explicit finite rational certificate

[Statement and proof](https://github.com/GettysburgResearch/collatz/blob/c91b80a3156e640ad471cf30c47721145ae21eb1/research/central-step-20261123/rational/FINITE_RATIONAL_CERTIFICATE.md) · [Independent review](https://github.com/GettysburgResearch/collatz/blob/c91b80a3156e640ad471cf30c47721145ae21eb1/reports/2026-11-23-central-step/rational-review.md)

For a fixed positive integer n, integer a, and odd positive q, iterate the literal shortcut orbit x_k and the signed numerator map S_q(w)=w/2 for even w and (3w+q)/2 for odd w. Set:

```text
J = 2q + 2
M = n max(1, |a|) (4q)^J
L = the least positive integer with M < 2^L
H = [J(4q + 3) + 1]L + J
```

**If x_k and S_q^k(a) have opposite parity for every 0 <= k < H, the ordinary orbit enters a positive integer cycle before H. Its primitive period is at most 2q.** The proof uses a positive integer excursion potential, enough visits to the full signed interval [-q,q], and an extra parity window that forces a repeated ordinary state. Zero is included.

The finite test is equivalently the complete-prefix congruence `2^H | 3^(b_H) a + q D_H`. The carry and clock come from the unchanged actual source. No all-time legality or periodic dual is assumed. For a triadic denominator q=3^r, the resulting complementary denominator is one, giving convergence to the standard cycle; PR176's specialized triadic horizon is substantially smaller.

Monks–Yazinski's qualitative rational-autoconjugacy/nondivergence reduction is credited in the note. The explicit finite horizon is derived here without a historical-priority claim. Constructing a successful candidate that funds its own horizon for every positive input remains open. Universal success in the broader rational class would first exclude escape; nontrivial cycles would still require control.

## 2. Construct the rate on the same ordinary component

[Fast equivalent flow](https://github.com/GettysburgResearch/collatz/blob/c91b80a3156e640ad471cf30c47721145ae21eb1/research/central-step-20261123/stationary/FAST_EQUIVALENT_FLOW.md) · [Independent review](https://github.com/GettysburgResearch/collatz/blob/c91b80a3156e640ad471cf30c47721145ae21eb1/reports/2026-11-23-central-step/stationary-review.md)

Given the stated positive harmonic flow on a hypothetical escaping ordinary component, exponentially reweight the mass by its first attachment index to the forward spine. The resulting fixed positive harmonic flow has the same capacity and keeps the whole inverse path law at the original root exactly unchanged.

For every deterministic finite inverse-clock list and every finite quotient Q, the new inverse endpoint average zeta_N and the original empirical law pi_N satisfy:

```text
TV(zeta_N, pi_N) <= D/N
(1-delta_N)_+^2 Col_Q(pi_N) <= Col_Q(zeta_N)
Col_Q(zeta_N) <= (1+delta_N)^2 Col_Q(pi_N)
delta_N = sqrt(2) D / sqrt(N)
```

The comparison is simultaneous at all moduli, including growing precision. The fixed-root floor survives; a global uniform reciprocal floor on the whole component is not asserted for the changed law. The construction gives a comparison, not a collision upper estimate.

With the full PR182 source boxes, for 1 <= m < N the exact remaining consumer is:

```text
Col_(3^m)(zeta_N)
  <= [(sqrt((N-m) B_(N,m)) + m + D)/N]^2
B_(N,m) = (sum_B sqrt(N_B/(N-m)))^2
```

All translated carries, source heights, cross-box terms, and omitted mass remain. No subexponential estimate for the actual effective box count was obtained. PR180's finite-Shannon-deficit and geometric-iid branches retain their separate limit-order qualifications.

## 3. Complementary-cycle capacity

[Complete denominator bound](https://github.com/GettysburgResearch/collatz/blob/c91b80a3156e640ad471cf30c47721145ae21eb1/research/central-step-20261123/cycles/COMPLEMENTARY_DENOMINATOR_CAPACITY.md) · [Independent review](https://github.com/GettysburgResearch/collatz/blob/c91b80a3156e640ad471cf30c47721145ae21eb1/reports/2026-11-23-central-step/stationary-review-cycles.md)

A nontrivial positive integer shortcut cycle of primitive length K has fully reduced complementary rational denominator q > K/2. The core has K=2 and q=1, giving the uniform conclusion K <= 2q. The proof uses distinct odd numerator states, a strict convexity estimate, and exact integer comparisons. It retains all gcd cancellation in the numerical denominator. A continuous refinement is included.

This supplies the period bound only after the finite rational certificate proves an actual eventual cycle. It does not supply an upper bound on the complementary denominator or exclude every nontrivial cycle.

## 4. All-candidate triadic selection and its true cost

[Optimized selector and height](https://github.com/GettysburgResearch/collatz/blob/c91b80a3156e640ad471cf30c47721145ae21eb1/research/central-step-20261123/triadic/OPTIMAL_SELECTOR_AND_HEIGHT.md) · [Independent review](https://github.com/GettysburgResearch/collatz/blob/c91b80a3156e640ad471cf30c47721145ae21eb1/reports/2026-11-23-central-step/cycles-review-triadic.md)

Using PR176's improved weight `F(r)=prod_(j<r)(1+3^j)` and horizon `9 bl(n F(r) max(1,|a|))+1`, the new note optimizes over every signed triadic numerator and exponent.

- Every positive separable weight whose product `x |w| G(r)` is nonincreasing on all eligible nonterminal paired steps must satisfy `F(r) G(0) <= 4^r G(r)`. Hence this entire potential class retains the leading quadratic logarithmic denominator cost.
- For a fixed reduced nontriadic rational target u/d, every K-bit matching triadic candidate satisfies `2^(K+1) <= (2d+3|u|) F(r) max(1,|a|)`. This is uniform over numerator, exponent, and terminal choices; the optimal logarithmic cost has rate one.
- The odd-denominator approximation discussion retains the loss of bits when an even denominator is normalized and the ordinary source-height budget. It does not infer that a generic obstruction is a small-source Collatz counterexample.

## Verification and exact source boundary

The initial refresh covered the 30 most recently updated open PRs, plus this PR and main. The changed working inputs were frozen at PR175 `53ba1e1ffc46bf022433c2124a62682ad8dd4739`, PR176 `fb402404deb810bd8e32e596993739bb5a6967d1`, PR177 `aaa132e904e4e6d0b438e963f76d72d79e2c7f34`, PR180 `a436db7b85f37abafea25f42d6f34afed02a29c0`, and PR182 `a7fd3ac9e5bff7412858df23d776bb847e9c1371`. Exact file roles and hashes are in the source ledgers. This was not a new audit of every historical PR.

- Seven rational-excursion and five weighted-selector theorem declarations passed strict author builds and separate fresh independent builds under Lean 4.34.1, with `autoImplicit=false` and `warningAsError=true`.
- Mathlib is pinned to `d13f23b723b8a846827a245b89c10fc7d3f11612`; existing dependency objects were reused. The old Collatz Lean corpus was not rebuilt.
- Every authored theorem is covered by the committed axiom logs. Only `propext`, `Classical.choice`, and `Quot.sound` appear.
- Four independent written reviews bind the exact new mathematical source bytes. The full visit-count/parity certificate, flow construction, cycle theorem, and selector interpretation are not claimed to be fully formalized.
- The exact publication tree contains 38 added files. The packet manifest checks all 37 other new files; frozen review hashes and compiled-source hashes match the committed bytes.

### Required repository gate

The default gate ran successfully in a **clean, complete checkout of c91b80a3156e640ad471cf30c47721145ae21eb1**, tree `7fe34f992101d615f59b722d313f453ccaffc685`, with **660 tracked files**. All five required subprocesses exited zero. The checkout remained clean. The optional `--regressions` bundle was not requested or run; the gate includes its own bounded self-tests. This gate checks integrity and selected finite controls, not Collatz.

```text
python -X utf8 -B tools/validate.py --receipt <outside-checkout>
validation receipt SHA-256:
6f1ca5aea8f1360d2f889c47b9cd16ed0d028cfc3758aa515accfeeb52679eab
packet manifest SHA-256:
673709f3912e0eec6fc7edf9f6446b4f6e36d23c645d960b8cce25ff25a8a45d
```

<details>
<summary>Exact external checkout-validation receipt</summary>

```json
{
  "schema": "collatz-checkout-validation/v1",
  "started_utc": "2026-11-23T03:42:08.019578+00:00",
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
      "seconds": 0.081
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
      "seconds": 0.257
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
      "seconds": 0.033
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
      "seconds": 0.052
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
      "seconds": 0.031
    }
  ],
  "success": true,
  "checkout": {
    "commit": "c91b80a3156e640ad471cf30c47721145ae21eb1",
    "tree": "7fe34f992101d615f59b722d313f453ccaffc685",
    "tracked_files": 660
  },
  "checkout_after": {
    "commit": "c91b80a3156e640ad471cf30c47721145ae21eb1",
    "tree": "7fe34f992101d615f59b722d313f453ccaffc685",
    "tracked_files": 660
  },
  "finished_utc": "2026-11-23T03:42:08.526689+00:00"
}
```

</details>

## Prior checkpoint and remaining proof obligations

The previous PR178 body at `e6ed7f1429ced4b58b85ca9006edd9a3a12ca193` is preserved [exactly as JSON](https://github.com/GettysburgResearch/collatz/blob/c91b80a3156e640ad471cf30c47721145ae21eb1/reports/2026-11-23-central-step/PR178-before.json) and as a [readable archive](https://github.com/GettysburgResearch/collatz/blob/c91b80a3156e640ad471cf30c47721145ae21eb1/reports/2026-11-23-central-step/PR178-before.md). Earlier work remains in the branch history.

The direct next construction targets are: (1) a candidate at the unchanged positive source satisfying its own finite horizon, preferably in the triadic class or with additional denominator control; and (2) an actual future-source collision or complete-box estimate compatible with the stationary limit being used. The new results sharpen those targets but do not discharge them.
