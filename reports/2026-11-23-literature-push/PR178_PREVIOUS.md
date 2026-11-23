## Status and purpose

**Full Collatz remains OPEN.** This checkpoint steps back across the repository and pursues three direct closing arguments in parallel: construct an accepting dual candidate for each unchanged source, derive the required actual-law collision upper bound, and obtain an opposing full complementary-denominator restriction for a positive cycle.

The new results exclude broad proposed mechanisms and constrain counterexample behavior. They do not establish any of those universal closing premises.

- **Current commit:** [a9b23dcee61a4b65a63aa4e7ca653d875a405037](https://github.com/GettysburgResearch/collatz/commit/a9b23dcee61a4b65a63aa4e7ca653d875a405037)
- **Parent:** c91b80a3156e640ad471cf30c47721145ae21eb1
- **Entry point:** [Reassessment and three direct attacks](https://github.com/GettysburgResearch/collatz/blob/a9b23dcee61a4b65a63aa4e7ca653d875a405037/research/reassessment-20261123/README.md)
- **Repository synthesis:** [Seven architectures and their actual remaining implications](https://github.com/GettysburgResearch/collatz/blob/a9b23dcee61a4b65a63aa4e7ca653d875a405037/research/reassessment-20261123/REPOSITORY_REASSESSMENT.md)
- **Evidence:** [Source, review and build index](https://github.com/GettysburgResearch/collatz/blob/a9b23dcee61a4b65a63aa4e7ca653d875a405037/reports/2026-11-23-reassessment/README.md)

The snapshot covers all 145 open and closed PR records retrieved during this pass. The integrated map, older rewrite/merger work and changed direct interfaces were revisited. This is repository orientation plus targeted proof work, not a fresh proof audit of every branch.

## 1. Exact classification of global additive potentials

Using the primary Applegate–Lagarias semigroup theorem, the [cycle packet](https://github.com/GettysburgResearch/collatz/blob/a9b23dcee61a4b65a63aa4e7ca653d875a405037/research/reassessment-20261123/cycles/PRIME_POTENTIAL_AND_FULL_CLOSURE.md) proves a source-qualified written classification.

For the shortcut map T and a completely additive function F with values in an ordered abelian group,

$$
F(T(n))\le F(n)\quad\hbox{for every positive integer }n
\quad\Longleftrightarrow\quad
F(n)=v_3(n)c\quad(c\ge0).
$$

For the odd accelerated map U, the same classification holds on odd integers. Monotonicity only on odd sources prime to three already forces F to vanish on those sources. The semigroup argument uses the sign of every generator's three-adic valuation to preserve this source restriction.

This includes finite lexicographic vectors of additive prime features. Every such potential vanishes on every positive periodic orbit, including a hypothetical nontrivial one. The result does not classify nonlinear ranks, state-dependent prime weights, or a potential required to decrease only above an arbitrary floor.

A separate Lean-checked certificate uses the genuine ordinary paths

$$
25\to19\to29\to11,\qquad55\to83\to125,\qquad
25\cdot55=11\cdot125.
$$

The five additive edge changes sum to zero, so weak decrease on all five forces equality on each. This is a product balance between two open paths, not an integer cycle. The minimum source is 19 and the minimum endpoint is 11; no arbitrary-floor conclusion follows.

**Formal boundary:** the finite ordinary certificate is Lean-checked. The primary semigroup theorem, ordered-group classification and its shortcut corollary remain source-qualified written mathematics.

## 2. Every finite normalization of the proposed escaping graph explodes

The [collision packet](https://github.com/GettysburgResearch/collatz/blob/a9b23dcee61a4b65a63aa4e7ca653d875a405037/research/reassessment-20261123/collision/FINITE_CLOCK_AND_FIXED_SOURCE.md) retains one hypothetical escaping ordinary component and its positive harmonic flow nu. When applying the supplied flow construction, the state domain is the positive odd integers prime to three.

For any positive finite rates c such that

$$
M=\sum_n\nu(n)/c(n)<\infty,
$$

every unchanged source satisfies

$$
\sum_{j\ge0}c(U^j n)^{-1}\le M/\nu(n).
$$

Thus the minimal continuous-time process with those rates and exactly the original successor explodes almost surely, with expected lifetime at most M/nu(n). The normalized probability pi(n)=nu(n)/(Mc(n)) satisfies coordinatewise balance, but the minimal killed process loses all its mass as time tends to infinity. It is not stationary under pi. The obstruction covers every finite normalization, not merely power clocks.

For spine flow increasing to finite capacity C, its indicator f and finite cutoffs f_J have the exact defect

$$
\int Qf\,d\pi=C/M,\qquad \int Qf_J\,d\pi=0,
$$
$$
\|f_J-f\|_{L^1(\pi)}\to0,\qquad
\|Qf_J-Qf\|_{L^1(\pi)}=C/M.
$$

Here Qf is the pointwise rate expression; integrability does not establish generator-domain membership. Nonminimal conservative extensions with entrance or resurrection at infinity remain possible in scope, but require an extra boundary law.

**Formal boundary:** the deterministic infinite-series bound and flow-floor lemma are Lean-checked. The stochastic consequence and exact flux are independently reviewed written arguments. No replacement actual collision upper bound is obtained.

## 3. Quantitative growth gap for the canonical candidate stream

The [construction packet](https://github.com/GettysburgResearch/collatz/blob/a9b23dcee61a4b65a63aa4e7ca653d875a405037/research/reassessment-20261123/construction/REAL_GROWTH_GAP.md) uses the existing same-source canonical stream eta. Put N=bl(n), M_K=max_{j<=K}|eta_j| and alpha=log(4/3)/log(3). If K>=N and the actual shortcut orbit avoids {1,2} through K, it proves

$$
M_K>
\frac1{2\,3^{N/2}}
\left(\frac{2^{K+1}}{n+1}\right)^{\alpha/2}.
$$

The proof combines the full-carry jump at a parity defect with the maximum length of the final alternating block from the unchanged positive source. Nonconvergence forces exponential growth of this running maximum. Boundedness or subexponential growth would imply convergence.

**The required upper estimate remains unproved.** The attempted simultaneous-carry construction does not provide it. The note keeps its stronger escape-only consequence separate from possible nontrivial cycles and records the exact relation to the primary Monks q-analog. This lane is written mathematics; no Lean wrapper for the unresolved upper estimate is added.

## 4. Uniform repeated-word budget and exact remaining targets

For a positive odd source p whose first kd exact gaps are w repeated k>=2 times, where w has length d and total gap A, either U^d(p)=p or

$$
2^{(k-1)A+1}\mid U^d(p)-p,\qquad
2^{(k-1)A+1}<(3/2)^d(p+1).
$$

A nonperiodic exact prefix square therefore requires p+1>2(4/3)^d, uniformly over all templates.

Independent review caught and repaired the later-window corollary: it must retain both the preperiod cost and the condition U^{i+d}(p_0) != U^i(p_0). An initially nonperiodic source may enter a cycle. The corrected bytes, including this condition, are what was reviewed and committed.

The central implications remain explicit:

1. Prove an upper bound or construct a candidate at its own paid horizon for the fixed original source.
2. Bound the effective box mass for the original endpoint law at the required order of limits. Equal residue collisions have not been shown to force exact repeated words violating the height budget; complete carries and source quotients remain.
3. For a hypothetical nontrivial primitive integer cycle, oppose the retained capacity bound
   q=(2^K-3^b)/gcd(2^K-3^b,C_*)>K/2.
   The sufficient full-gcd lower bound giving q<=K/2 is explicitly OPEN. The new bilinear identity does not establish it because its integer complementary numerators vary with q.

## Sources and independent verification

Changed active source heads read in this pass:

| Source | Pinned head |
| --- | --- |
| PR176 | 4171e1fe40e41842af9f800bd821084b724cf8f9 |
| PR177 | f47a5ec51aa5853f104013a6d5046d6220ff7423 |
| PR180 | 7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161 |
| PR182 | cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c |

The [snapshot](https://github.com/GettysburgResearch/collatz/blob/a9b23dcee61a4b65a63aa4e7ca653d875a405037/reports/2026-11-23-reassessment/REPOSITORY_SNAPSHOT.json) and per-lane ledgers retain the other exact repository and primary-literature sources. Main was ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a at the snapshot.

Independent review reconstructed the written construction, collision and cycle deductions. The collision review is VERIFIED WITH FIXES because of the repaired later-window scope. The final synthesis and indices also received a separate scope review.

Both new Lean modules and their audits passed author and independent reviewer builds in separate output directories:

- **14 authored theorem declarations:** 12 finite-cycle certificate theorems and 2 deterministic clock theorems.
- Lean 4.34.1, compiler 5045d0056413266e57c625dcd7c365b10e377c52.
- mathlib d13f23b723b8a846827a245b89c10fc7d3f11612; dependency objects reused.
- autoImplicit=false and warningAsError=true.
- Axiom union only propext, Classical.choice and Quot.sound; no sorryAx.
- The older proof corpus was not rebuilt.
- [Frozen integration checks](https://github.com/GettysburgResearch/collatz/blob/a9b23dcee61a4b65a63aa4e7ca653d875a405037/reports/2026-11-23-reassessment/FROZEN_CHECKS.json) match all reviewed and compiled source bytes.
- [Complete new-file manifest](https://github.com/GettysburgResearch/collatz/blob/a9b23dcee61a4b65a63aa4e7ca653d875a405037/reports/2026-11-23-reassessment/MANIFEST.json): 34 entries, plus the self-excluded manifest itself; 35 added files, no prior files edited.
- Manifest SHA-256: cb324cbe1636425a005bfb80e44ddae9e0209ba52c30bcced1276d0e415d47b3.

## Exact-commit release gate

The default required command was run in a clean, complete detached checkout of this exact commit:

```text
python -X utf8 -B tools/validate.py --receipt /workspace/scratch/56e7a5765d0c/nov23e-integrity-receipt.json
```

**PASS.** Commit a9b23dcee61a4b65a63aa4e7ca653d875a405037, tree 791383b1b197ec4cee502bddb020a71769f0f85b, all 695 tracked files. HEAD, tree, parent, manifest coverage, reviewed/compiled source hashes and clean status were checked after validation. This gate checks integrity and the named bounded controls; it is not mathematical verification of Collatz.

Receipt SHA-256: 69e33ff50dd44fe47e0f75aaeda679ffae5ee1d9abb909adec4c02412dee1fee.

<details>
<summary>Exact default validation receipt</summary>

```json
{
  "schema": "collatz-checkout-validation/v1",
  "started_utc": "2026-11-23T04:42:21.056537+00:00",
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
      "seconds": 0.088
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
      "seconds": 0.251
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
      "seconds": 0.065
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
      "seconds": 0.071
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
      "seconds": 0.03
    }
  ],
  "success": true,
  "checkout": {
    "commit": "a9b23dcee61a4b65a63aa4e7ca653d875a405037",
    "tree": "791383b1b197ec4cee502bddb020a71769f0f85b",
    "tracked_files": 695
  },
  "checkout_after": {
    "commit": "a9b23dcee61a4b65a63aa4e7ca653d875a405037",
    "tree": "791383b1b197ec4cee502bddb020a71769f0f85b",
    "tracked_files": 695
  },
  "finished_utc": "2026-11-23T04:42:21.617778+00:00"
}
```

</details>

## Earlier checkpoints

The preceding finite rational certificate, fast equivalent flow, complementary-denominator capacity and triadic-cost work remain in the parent. The previous PR title/body is archived exactly in [PR178_PREVIOUS.json](https://github.com/GettysburgResearch/collatz/blob/a9b23dcee61a4b65a63aa4e7ca653d875a405037/reports/2026-11-23-reassessment/PR178_PREVIOUS.json), with a [readable copy](https://github.com/GettysburgResearch/collatz/blob/a9b23dcee61a4b65a63aa4e7ca653d875a405037/reports/2026-11-23-reassessment/PR178_PREVIOUS.md). This checkpoint adds to that work without relabeling its conditional conclusions as a full proof.
