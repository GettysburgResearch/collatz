## Current checkpoint — 23 November 2026

**Full Collatz remains open.** This checkpoint attacks the missing global implications through complete cycle denominators, complementary parity trajectories, actual inverse entropy, and simultaneous completions. It contains one new finite Lean formalization, independently reviewed written results, and explicit failed closing steps.

- Commit: `2169884b64871b448cda16c7d74a0d5914ed870b`
- Tree: `e728e3e0410f7c51aba76350af6b7bc16f10d556`
- Parent: `7e4569476e152f6b8537bdc1711df595ec1ffd89`
- [Research packet](https://github.com/GettysburgResearch/collatz/blob/2169884b64871b448cda16c7d74a0d5914ed870b/research/high-variance-20261123/README.md)
- [Evidence and review scopes](https://github.com/GettysburgResearch/collatz/blob/2169884b64871b448cda16c7d74a0d5914ed870b/reports/2026-11-23-high-variance/README.md)

### What this changes

**1. A formal theorem modulo the complete cycle denominator.** For the literal balanced carry
`C(A,p) = sum_(i<p) 2^floor(Ai/p) 3^(p-1-i)`, Lean proves
`gcd(C(A,p), 2^A-3^p)=1` from positive parameters, `gcd(A,p)=1`, and `2^A>3^p`.
The proof derives the floor-residue permutation and constructs the Bézout unit inside the actual `ZMod D`. No supplied-root, supplied-permutation, denominator factorization, or carry-invertibility assumption remains. The corollary excludes divisibility by every nontrivial full denominator in this balanced family. The balanced S-unit observation is credited to PR185; no new-discovery claim is made for that observation.
[Lean source](https://github.com/GettysburgResearch/collatz/blob/2169884b64871b448cda16c7d74a0d5914ed870b/research/high-variance-20261123/cycles/lean/BalancedCycleUnit.lean).

**2. An all-finite-prime/all-real-floor construction.** For every finite set of primes S and every real H>0, the written proof constructs primitive positive **rational** Collatz cycles with every state above H, integral at every prime in S, and with the same nontrivial reduced denominator at every state. This defeats a fixed finite-prime substitute for the full denominator test, even with a high real floor. It does not refute adaptive inspection of all factors of each actual denominator and supplies no integer counterexample.
[Proof](https://github.com/GettysburgResearch/collatz/blob/2169884b64871b448cda16c7d74a0d5914ed870b/research/high-variance-20261123/cycles/MOVING_PRIME_CYCLE_ATTEMPT.md).

**3. A terminating decision procedure for every proposed rational parity dual.** Given n>0, a signed numerator a, and a positive odd denominator d, the arithmetic lane decides whether a/d is the complementary-parity dual of n. Signed product contraction bounds the first event; zero and negative-to-positive crossings are handled explicitly; a repeated small numerator gives either a literal paired cycle or an exact finite parity-mismatch index. Every rejected certificate replays through its first failing state. The qualitative rationality/escape reduction is credited to Monks–Yazinski. The missing step remains rational-dual existence for every positive integer; an accepted dual alone does not exclude a nontrivial integer cycle.
[Written theorem](https://github.com/GettysburgResearch/collatz/blob/2169884b64871b448cda16c7d74a0d5914ed870b/research/high-variance-20261123/arithmetic/RATIONAL_DUAL_CERTIFICATE.md) · [Exact checker](https://github.com/GettysburgResearch/collatz/blob/2169884b64871b448cda16c7d74a0d5914ed870b/research/high-variance-20261123/arithmetic/check_rational_dual.py).

**4. A single-digit arithmetic memory cost.** Under the pinned canonical-trace inputs, the actual retained escape forces the first-ternary-predecessor-digit log-odds to diverge, with accumulated magnitude at least N log N asymptotically, while accumulated row entropy is o(log N). Tightness of this one scalar along the ordinary time laws would exclude escape, but is unproved. A uniform bilateral trace profile retains the original-source clock. Explicit finite ordinary paths refute the proposed global bounded Poisson corrector.
[Entropy attempt](https://github.com/GettysburgResearch/collatz/blob/2169884b64871b448cda16c7d74a0d5914ed870b/research/high-variance-20261123/entropy/COARSE_DIGIT_MEMORY_AND_TRACE_FRONT.md).

**5. Exact tests of the high-variance Diophantine and renewal applications.** The proposed real/2-adic Subspace Theorem product is a positive tail at least 1/3, so this application lacks its required height saving. Every supplied finite real-shell moment at the moving ternary precision yields only the noncontradictory q_j² bound. An exact all-ones control refutes an all-cylinder o(B) shell-density bound while preserving the distinct positive ordinary diagonal obligation.
[Two-place and renewal attempt](https://github.com/GettysburgResearch/collatz/blob/2169884b64871b448cda16c7d74a0d5914ed870b/research/high-variance-20261123/adelic/TWO_PLACE_AND_RENEWAL_ATTEMPT.md).

### Actual validation

- Fresh strict compilation: Lean 4.34.1, compiler `5045d0056413266e57c625dcd7c365b10e377c52`; Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`; `-DwarningAsError=true`.
- **8 theorems + 1 definition; all 9 declarations audited.** Only `propext`, `Classical.choice`, and `Quot.sound`; no admissions or extra axioms.
- Two rational-cycle construction controls, replaying all **97 and 3,089 odd rotations**, passed in normal and optimized Python with identical output.
- Rational-dual checker: **2,701 exact cases** passed, including **38** repeated-small-numerator unequal-integer cases reaching their exact predicted terminal rejection.
- Independent written reviews reconstructed the cycle construction, signed-dual proof and checker, entropy deductions, and the scoped adelic calculations. External analytic inputs remain source-qualified.
- Required repository gate: **all 5 commands passed** in a clean complete checkout of this exact commit, with **547 tracked files** and unchanged before/after commit and tree identity.
- Gate receipt SHA-256: `a85ff61caa14e1924d7959596678fb21e3dae0793622f19fff4784c0b55415c8`.

The gate checks repository integrity, not the Collatz theorem. No historical Lean corpus or large old census was replayed for this checkpoint. The infinite prime selection, rational dynamics, real floor, and other written results are outside the finite Lean claim.

### Sources and remaining obligations

The refresh covered the 40 most recently updated open PR metadata and targeted reading of PR185 at `39ba48e6a8af781193e28c679ea8ab64663c3aa6`; it continues the earlier pinned inventory without claiming a new all-PR proof audit. The previous PR description is archived in this commit.

The unresolved universal steps are rational-dual existence, arbitrary-word full-denominator exclusion, or ordinary-source tightness of the canonical digit comparison. None is assumed as a Lean axiom.

<details>
<summary>Exact complete-checkout validation receipt</summary>

```json
{
  "schema": "collatz-checkout-validation/v1",
  "started_utc": "2026-11-23T01:14:09.547528+00:00",
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
      "seconds": 0.087
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
      "seconds": 0.272
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
      "seconds": 0.056
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
      "seconds": 0.049
    }
  ],
  "success": true,
  "checkout": {
    "commit": "2169884b64871b448cda16c7d74a0d5914ed870b",
    "tree": "e728e3e0410f7c51aba76350af6b7bc16f10d556",
    "tracked_files": 547
  },
  "checkout_after": {
    "commit": "2169884b64871b448cda16c7d74a0d5914ed870b",
    "tree": "e728e3e0410f7c51aba76350af6b7bc16f10d556",
    "tracked_files": 547
  },
  "finished_utc": "2026-11-23T01:14:10.107699+00:00"
}
```

</details>
