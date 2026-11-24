## The remaining problem

The actual two-color head disagreement still has no summable bound. This revision concentrates the tested source classes, derives a joint estimate for two smaller witnesses, and supplies additive structure around actual sources and target pairs. **Collatz remains open.** Three GPT-6.2 Astra streams developed these attacks; the coordinator reconstructed them and ran the formal build.

**Current scientific packet:** [Four-suffix reduction, late witness geometry and synchronized alternatives](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/README.md).
**Evidence:** [execution and written reviews](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/reports/ayh-resource-reset-20261124/crossing-step/README.md) · [source ledger](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/SOURCES.json) · [current PR comparisons](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/reports/ayh-resource-reset-20261124/crossing-step/LATEST_INTAKE.md).

This checkpoint starts from `6eb986b0ce0b1836a356474d25d709ed4e948b67`. It changes 35 files: 33 additions and two navigation updates. Earlier mathematical packets and their evidence remain intact; the preceding complete PR description is preserved [here](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/reports/ayh-resource-reset-20261124/crossing-step/PRIOR_PR_DESCRIPTION.md).

## 1. The whole head series reduces to prescribed suffixes

For any invariant label, summability of the full original head-disagreement series is equivalent to summability in any fixed open head arc on one prescribed suffix per row, using the periodic schedule `0, 27, 45, 57` according to the row index modulo four. All counts keep their **original row weights**. The stronger version permits four distinct level classes modulo any fixed M>=4, separate arcs, any fixed number of initial even child steps, and the corresponding parent residue restrictions.

The comparison is quantitative: the full row is bounded by a finite shift of the restricted series convolved with `(q+1)81^(-q)`, plus a summable bottom term. The construction has bounded multiplicity and bounded scale distortion; the only recursive coefficient is exactly `1/81`. It also transfers every fixed little-o power bound below one. The route uses no component-density estimate. Converting summability to universal convergence uses the separately source-qualified fixed-target input; the classical `.84` variant instead uses the published Krasikov–Lagarias predecessor theorem.

[Exact arithmetic](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/FOUR_SUFFIX_ROUTING.md) · [series comparison](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/FOUR_SUFFIX_EQUIVALENCE.md) · [periodic schedule](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/PERIODIC_FOUR_SUFFIX_SCHEDULE.md).

## 2. Late witnesses require transverse spread and linear variation

On the physical slab `3d <= t <= 3.1d`, outside any prescribed inverse-power fraction of original children, every discordant source has a positive frequency of genuine smaller discordant head witnesses on every D-clock interval with `D >= (log d)^6`. Any selection of those witnesses uses at least order `sqrt(D/log d)` distinct centered exponents and has total variation at least `delta D`.

The proof uses one explicit coarse ordinary source coordinate, with more than `.39d` available bits and fewer than `.31d` bits consumed by the whole test. Conditional on its exposed prefix, the next target parent has an odd affine slope and a fixed head suffix. Disjoint blocks give a multitime finite-grid product estimate. A factorial-moment bound controls prescribed tracks and sufficiently small exponential banks of them; it does not assert new random bits at a landed endpoint.

[Late tracks](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/LATE_WITNESS_TRACKS.md) · [variation and decoder bound](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/TRACK_VARIATION.md).

## 3. Joint graph incidence and simultaneous symmetric target pairs

Each typical discordant source supplies order `d^2` pairs of smaller discordant heads away from the narrow ballistic diagonal. A fixed pair has a unique relative integer clock and trit exponent by classical two-logarithm separation. If Gamma_j sums `1/z1` over the compatible target edges, the original row obeys

`a_j <= O_A(d^(-A)) + O_A(sqrt(log d)/d^2) Gamma_j`.

Reprojecting at the **two targets together** gives many symmetric neighboring edges of the form `(z1 +/- 81*2^v L, z2 +/- 81*3^w L)`, retaining all four actual child/parent colors and the exact rounding correction. These neighbors are actual colored edges; their realization as outputs of further original trajectories is not claimed.

[Joint recurrence](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/WEIGHTED_TWO_HEAD_GRAPH.md) · [simultaneous target midpoints](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/JOINT_TARGET_MIDPOINTS.md).

## 4. Literature-based structure through the actual source

Apply Bloom–Sisask's published Kelley–Meka progression-counting theorem to the **poor centers** of each retained exact-future fiber. Almost every actual source is thereby the midpoint of many symmetric alternatives in its own fiber. Backwards pruning gives a chronological ternary tree of depth order `h/(log h)^12`, with distinct positive leaves and prescribed parity-splitting windows, preserving every recorded future.

A Hellinger martingale also bounds the accumulated squared conditional source-bit biases by order `log h`, with an exponential tail. A separate window incidence removes a summable locally sparse portion of actual discordance. The native-clock theorem identifies the finite-search boundary: on square-root-order mass, even the entire rich fiber has no child-to-parent meeting at any two clocks through the recorded horizon. Eventual convergence remains compatible with this finite fact.

[Centered fibers](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/SYMMETRIC_FUTURE_FORKS.md) · [conditional information](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/RETROSPECTIVE_INFORMATION.md) · [native-clock boundary](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/research/ayh-resource-reset-20261124/crossing-step/NATIVE_FIBER_CROSSING.md).

## What Lean checked

The coordinator freshly compiled four new modules and the exact PR 193 finite certificate, with Lean 4.34.1, Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, one worker, auto-implicit arguments disabled, and warnings as errors. The build exited 0 in 213.743 seconds with empty stderr. Every one of the **18 new public theorems**, and all three public imported certificate roots, has only subsets of `propext`, `Classical.choice`, and `Quot.sound` in its transitive axiom report.

| New module | Public theorems | Checked scope |
| --- | ---: | --- |
| HeadRayRouting | 7 | Exact label routes, ternary phase choice and tripling consumer |
| FourSuffixClosure | 3 | Actual directed return and global basin-of-one equivalence under the explicit four comparisons |
| LateWitnessTracks | 3 | Projected target arithmetic, odd-affine residue permutation and test count |
| SymmetricFutureForks | 5 | Poor-center implication, prefix shifts and parity splits |

The imported PR 193 certificate is byte-exact Git blob `797e2629e931551cc5913acbe7ef314aea489cd2`; its kernel finite cover was rebuilt from source. The new global consumer has no probability or density hypothesis, but its four multiplier comparisons remain hypotheses. Irrational routing, source counting, probability estimates, progression pruning and full analytic conclusions remain **written proofs**.

[Build log](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/reports/ayh-resource-reset-20261124/crossing-step/lean-build.log) · [execution metadata](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/reports/ayh-resource-reset-20261124/crossing-step/lean-build.json) · [complete axiom inventory](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/reports/ayh-resource-reset-20261124/crossing-step/axiom-audit.json) · [coordinator reconstruction](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/reports/ayh-resource-reset-20261124/crossing-step/ROOT_REVIEW.md) · [frozen source hashes](https://github.com/GettysburgResearch/collatz/blob/2c1397d2adcadc620381bca20c465f3bf31a6f8e/reports/ayh-resource-reset-20261124/crossing-step/source-hashes.json).

The positive-map row-zero convention was corrected during integration; all counted parents are positive. Recent external merger, growing-block and fixed-target estimates retain their SOURCE-QUALIFIED status. They were not relabeled as locally rebuilt formal proofs.

## Exact remaining closing estimate

The graph now has both transverse spread and many parallel symmetric neighbors. These facts do not bound its total weighted degree. For example, `Gamma_j << d/(log d)^(3/2+epsilon)` for a fixed positive epsilon would make the original discrepancy series summable. A direct summable bound on the periodic prescribed-suffix series would settle the same obligation. Neither bound is established by this revision.

The connection to Emre Yolcu, Scott Aaronson and Marijn Heule is through their mixed binary/ternary rewriting architecture and the directed return already recorded in their section 4.5. The new constructions refine that ordinary-head obligation. They do not claim a terminating interpretation for the complete eleven-rule system.

## Published-head validation

Published head: `2c1397d2adcadc620381bca20c465f3bf31a6f8e`.
Published tree: `ac6707bcc50a631b7fcc3cb99844be77cf609ba5`.
Clean complete checkout: **508 tracked files**.
All **five** default validator commands passed at this exact head. The remote tree matched the tested local tree before publication. Earlier expensive regression bundles were not rerun. This is repository integrity evidence, separate from mathematical verification.

Command:

```text
python -X utf8 -B tools/validate.py --receipt /workspace/scratch/33d115a3cb8d/crossing-publish/published-validation.json
```

Receipt SHA-256: `e0668f75b1af8d023bf4cfa89601adcc06f763f05358b1b66c368102bbddffaa`.

<details>
<summary>Complete receipt for the exact published head</summary>

```json
{
  "schema": "collatz-checkout-validation/v1",
  "started_utc": "2026-11-24T11:02:44.601956+00:00",
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
      "seconds": 0.16
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
      "seconds": 0.331
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
      "seconds": 0.046
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
      "seconds": 0.102
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
      "seconds": 0.039
    }
  ],
  "success": true,
  "checkout": {
    "commit": "2c1397d2adcadc620381bca20c465f3bf31a6f8e",
    "tree": "ac6707bcc50a631b7fcc3cb99844be77cf609ba5",
    "tracked_files": 508
  },
  "checkout_after": {
    "commit": "2c1397d2adcadc620381bca20c465f3bf31a6f8e",
    "tree": "ac6707bcc50a631b7fcc3cb99844be77cf609ba5",
    "tracked_files": 508
  },
  "finished_utc": "2026-11-24T11:02:45.315143+00:00"
}
```

</details>
