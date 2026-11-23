# PR178 body before the profound-step checkpoint

Frozen head: `4e204f54136c79cf8c9393b34e3330594f99ae0a`.
Previous title: Collatz: triadic convergence rank and pressure collision bounds.
Archived from the live PR body at the start of this pass; trailing line whitespace and the final newline are normalized. The exact original body is retained in PR178_AT_4e204f5.json.

---

# Triadic convergence rank and actual-source pressure bounds

**Full Collatz remains OPEN.** This is a research checkpoint with a concrete Lean closing implication, an explicit written finite arithmetic certificate, and three further attacks on the remaining global steps.

Current head: `4e204f54136c79cf8c9393b34e3330594f99ae0a`
Tree: `b2b656ed1ede2562734e8787b1da7fe433f866a7`
Parent: `2169884b64871b448cda16c7d74a0d5914ed870b`

Start with the [scientific packet](https://github.com/GettysburgResearch/collatz/blob/4e204f54136c79cf8c9393b34e3330594f99ae0a/research/global-closure-20261123/README.md) and the [execution/review record](https://github.com/GettysburgResearch/collatz/blob/4e204f54136c79cf8c9393b34e3330594f99ae0a/reports/2026-11-23-global-closure/README.md). This checkpoint adds 35 files; the [manifest](https://github.com/GettysburgResearch/collatz/blob/4e204f54136c79cf8c9393b34e3330594f99ae0a/reports/2026-11-23-global-closure/FILES.json) binds the other 34 files. Earlier work is preserved, including the [previous PR description](https://github.com/GettysburgResearch/collatz/blob/4e204f54136c79cf8c9393b34e3330594f99ae0a/reports/2026-11-23-global-closure/archive/pr178-before-global-closure.md).

## Why this change

The previous rational-dual machinery decided supplied candidates but left a global closing construction unresolved. The newest peer work also sharpened the actual collision lower bound and supplied ordinary pressure measures. This checkpoint attacks the missing convergence implication, the arithmetic construction it requires, the actual-law upper estimate, and unrestricted full-denominator cycle exclusion.

The [source snapshot](https://github.com/GettysburgResearch/collatz/blob/4e204f54136c79cf8c9393b34e3330594f99ae0a/research/global-closure-20261123/SOURCE_SNAPSHOT.json) covers metadata and bodies for all 145 PR records, 122 open at access time. Selected proof files were read at exact heads; this is not an audit of all proofs. The [late refresh](https://github.com/GettysburgResearch/collatz/blob/4e204f54136c79cf8c9393b34e3330594f99ae0a/research/global-closure-20261123/LATE_REFRESH.md) records PR176's additional advance to c82e3c1be894f655b40dcb61bf6d309a8f664e67 and the two pressure/band proof files read before publication.

## Strongest positive result: a terminating triadic pair

[Triadic proof](https://github.com/GettysburgResearch/collatz/blob/4e204f54136c79cf8c9393b34e3330594f99ae0a/research/global-closure-20261123/duality/TRIADIC_RANK.md) · [Lean implementation](https://github.com/GettysburgResearch/collatz/blob/4e204f54136c79cf8c9393b34e3330594f99ae0a/research/global-closure-20261123/duality/lean/TriadicDualClosure.lean) · [independent review](https://github.com/GettysburgResearch/collatz/blob/4e204f54136c79cf8c9393b34e3330594f99ae0a/reports/2026-11-23-global-closure/duality-review.md)

For one fixed positive ordinary input and one finite signed triadic candidate a/3^r, all-time complementary parity implies that the actual shortcut orbit reaches 1. The formal theorem `CollatzTriadicDual.alltime_triadic_candidate_reaches_one` uses the literal deterministic paired trajectory, with its rational interpretation and equality to the original orbit proved in the module.

The natural-number lexicographic rank is `(r, 2*x*abs(w) + indicator(w=1))`. A denominator drop pays for an original-even step when r>0; otherwise the product decreases, with the indicator handling the integral 1-to-2 tie. A zero dual numerator forces an impossible all-odd ordinary tail. No cycle-exclusion or drift premise is assumed.

**Written finite certificate:** let N=bitlength(n), B=max(1,|a|,3^r), L=bitlength(B), and H=8N+(9r+8)L+2. Let b_H be the number of even original inputs and D_H the complete complementary affine carry of the actual H-step prefix. Then

```text
2^H divides 3^(b_H)*a + 3^r*D_H
```

forces the original input to reach 1 by H. The endpoint congruence enforces the whole parity prefix; the proof handles finite zero-numerator tails explicitly. The finite horizon is independently reviewed written mathematics, not an additional Lean claim.

**Still open:** construct a,r satisfying this certificate at their own height-dependent horizon for every fixed positive n. The coupled-carry construction was attempted; no universal small-residue saving was obtained.

## Other direct closure attacks

| Attack | Result and remaining boundary |
|---|---|
| Actual-source pressure/collision | [Proof](https://github.com/GettysburgResearch/collatz/blob/4e204f54136c79cf8c9393b34e3330594f99ae0a/research/global-closure-20261123/escape/PRESSURE_COLLISION_ATTACK.md): the ordinary pressure off-diagonal is at most 2*zeta(s)^2*Q^(-s). The actual retained-source law has growing density and entropy costs. Probability normalization improves the transfer to one density factor, but the resulting comparison bound still exceeds the critical target by a divergent logarithmic factor, uniformly for every s>1, even s approaching 1. This bounds the proposed comparison expression, not the actual off-diagonal. The needed nonuniform bilinear estimate remains open. Upstream positive bounded flow hypotheses remain source-qualified. |
| Complete cycle denominator | [Proof](https://github.com/GettysburgResearch/collatz/blob/4e204f54136c79cf8c9393b34e3330594f99ae0a/research/global-closure-20261123/cycles/INTEGRAL_MAHLER_CLOSURE_ATTEMPT.md): a nonzero finite odd-ray dyadic lift is nonrational, so Adamczewski–Bell excludes the hoped-for independent 3-Mahler equation for that same series. The triangular torus normalization retains exactly D/gcd(C,D), D=2^A-3^p, as its minimal isogeny degree. Degree-one exclusion for all nontrivial primitive positive words remains open. |
| Global ordinal interpretation | [Attempt](https://github.com/GettysburgResearch/collatz/blob/4e204f54136c79cf8c9393b34e3330594f99ae0a/research/global-closure-20261123/ORDER_CONSTRUCTION_ATTEMPT.md): two literal AYH rules already obstruct the direct strictly increasing, single total well-order interpretation, despite that two-rule subsystem terminating. This scoped observation does not exclude marked or source-dependent arithmetic ranks. |

The finite escape core also checks an exact common-source collision from 41: different critical four-gap words end at 425 and 911, both 20 modulo 81. Equal endpoint residues therefore do not provide the actual repeated-word premise. Repeated-block divisibility is credited to earlier PR178 work, rather than claimed as new mathematics.

## Formal checks and independent review

- Lean 4.34.1, compiler commit 5045d0056413266e57c625dcd7c365b10e377c52; Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612.
- Two new implementation modules and their two dedicated audit modules freshly compiled with warnings treated as errors; the escape modules also use autoImplicit=false.
- 22 authored public theorem declarations audited: 12 in TriadicDualClosure and 10 in PressureCollisionCore. The duality audit additionally covers its six definitions, two types and selected constructors/projections. These are declaration inventories, not novelty counts.
- Only subsets of propext, Classical.choice and Quot.sound occur. No sorryAx or custom research axiom occurs in the audited declarations.
- Separate agents independently reconstructed the arguments and freshly rebuilt the formal cores. Reviews bind exact final source hashes. Root contributions to the finite horizon and linear-density estimate are disclosed and independently reviewed.
- The finite horizon, infinite pressure estimates, Mahler/torus arguments and ordinal observation retain written-proof scope. The external Mahler theorem remains source-qualified.
- Dependency objects were reused. No historical research proof corpus was rebuilt.

## Exact-commit repository gate

Executed in a clean complete detached checkout of the current head:

```text
python -X utf8 -B tools/validate.py --receipt <outside-checkout>/checkout-validation.json
```

All five default commands exited zero. The checkout had 582 tracked files and was clean before and after. All 34 manifested files matched their hashes in this checkout. The receipt SHA-256 is `3c9042a610fc88f371b47e09b22174272327f3c7838254f893363e13bb147e15`.

The API-created tree matched the local staged tree exactly. The branch was advanced without force using the expected prior head. Subsequent GitHub reads confirmed the branch head, PR head, complete tree and sole parent shown above. Repository validation certifies checkout integrity and scoped controls; it does not prove Collatz.

<details>
<summary>Exact checkout-validation receipt</summary>

```json
{
  "schema": "collatz-checkout-validation/v1",
  "started_utc": "2026-11-23T02:08:23.005893+00:00",
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
      "seconds": 0.077
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
      "seconds": 0.249
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
      "seconds": 0.032
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
      "seconds": 0.057
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
      "seconds": 0.041
    }
  ],
  "success": true,
  "checkout": {
    "commit": "4e204f54136c79cf8c9393b34e3330594f99ae0a",
    "tree": "b2b656ed1ede2562734e8787b1da7fe433f866a7",
    "tracked_files": 582
  },
  "checkout_after": {
    "commit": "4e204f54136c79cf8c9393b34e3330594f99ae0a",
    "tree": "b2b656ed1ede2562734e8787b1da7fe433f866a7",
    "tracked_files": 582
  },
  "finished_utc": "2026-11-23T02:08:23.492095+00:00"
}
```

</details>

**Remaining global obligation:** prove the universal triadic-certificate construction, or supply an independently valid full-convergence route. Neither escape exclusion nor unrestricted nontrivial-cycle exclusion is claimed.
