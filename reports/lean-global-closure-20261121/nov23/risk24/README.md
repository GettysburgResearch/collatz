# Execution and review scope: triadic certificates and primitive denominators

Date: 23 November 2026. Repository: `GettysburgResearch/collatz`, own PR175.
This is an exploratory continuation; **full Collatz remains OPEN**.

The [scientific entry point](../../../../research/lean-global-closure-20261121/risk24/README.md)
contains the mathematical statements and their remaining hypotheses.
This report records what was read, executed, and internally reconstructed.
It does not promote repository integrity into mathematical evidence.

## Repository snapshot

The initial refresh read metadata for all 145 pull requests returned by the
two-page API listing, including older PRs with newer commits. Scientific
inspection was selective: the research map, integrated front door, scoped
errata, open obligations, and the relevant active source files were read.
This is not a claim to have audited every file on every branch.

[repo-refresh.json](repo-refresh.json) preserves the initial metadata and a
late refresh of the 12 most recently updated PRs. Main remained
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Our confirmed publication parent was
`8870528daa6a13cc941d602e578e35c8bfa4bf4f`, tree
`31c08fb8e47fc17cfec34dfd1f55a75aeb6c6f5d`.
PR146 remained at `f431078244e868dc699fad011044f0d5e7f76437`.

The principal source pins are retained in the scientific notes themselves:

| Source | Exact head or science commit | Inspected interface |
|---|---|---|
| PR177 | `6de3e304bb49a93a6c5ef0e5563137e75c7defb4` | `HIGH_VARIANCE_ESCAPE.md`, HE2 and HE18–HE24a; `HIGH_VARIANCE_ARITHMETIC.md`, carry circulation; finite witness boundary |
| PR185 | `e04daab0a0ddd59c80f5d16a51b9943fd5149e6c` | `PRIMITIVE_RESIDUAL_DEGREE.md`, Sections 1–4; `PRIMITIVE_DENOMINATOR_GROWTH.md`, separately qualified factor gap |
| PR185 metadata | `2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d` | Later head changed reports rather than the above science |
| PR178, initial | `2169884b64871b448cda16c7d74a0d5914ed870b` | General rational-dual verifier, sibling digit interface, and moving-prime cycle attempt |
| PR180, initial | `04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2` | `ANALYTIC_GLUING.md` and `ENTROPY_RIGIDITY.md`; exact ordinary path laws and canonical trace qualifications |
| PR182, initial | `aa12c13601cacec2c8496f1349b4947457dc1b45` | High rational cycles and the full-denominator gap |
| PR186 | `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493` | Selected arithmetic, ergodic, and transfer-operator literature interfaces |

Four PRs advanced during this run. Their changed science was inspected at
the pinned late heads; findings and overlapping results are recorded in
the scientific entry point and `review-scope.json`. Earlier source pins in
the frozen proof notes remain historical, exact dependencies, not claims
about the final latest head.

## New formal execution

[new-source-checks.json](new-source-checks.json) is the actual combined receipt.
The new driver compiled unchanged copies of `TriadicDual.lean` and
`SiblingSourceSeparation.lean`, appending axiom-print commands in a temporary
directory. It audited all 26 public theorem declarations and `stopClock`.

- Lean: 4.34.1, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Lean binary SHA256: `e8baaa71855a616dc351028f3ad2200051b0671f423a1696a100e809302d5550`.
- Driver SHA256: `158f15388834c6ce1ced7b521e4f1da4337a38977dee182b5f8705500c8b66bc`.
- Both source compilations exited 0. All requested axiom reports were present.
- The reported theorem/function axioms are only `propext` and `Quot.sound`;
  there is no custom axiom, `sorryAx`, or `native_decide` dependency.
- Three unused-simp-argument warnings are preserved in the receipt. They do
  not prevent compilation and were not suppressed or erased.

This execution establishes the discrete rank, total stopping clock, finite
certificate consumer, and the general distinct-source lemma. It does not
formalize the construction of the 2-adic autoconjugacy, the infinite network
analysis, the denominator degree proof, or a universal successful certificate.
No old project Lean module was rebuilt, and no inherited long computation
was rerun.

## Written proof reconstruction

[review-scope.json](review-scope.json) binds the internal reviews to file
SHA256 hashes. These are research checks by collaborating agents, not a
claim of external peer review or Lean verification of the written analysis.

The root reconstructed the new prime-power budget and degree bound, the
triadic equivalence and its formal interface, the distinguished-gcd
continuation, and the sibling transport calculation. The two nonauthor
research lanes independently reconstructed the root's actual-component
network construction. Its reviewed hash is recorded separately.

For the denominator consequence, PR185's finite Fourier structure was
inspected directly. Its later factor-gap result retains its stated
two-logarithm estimate and finite continued-fraction certificate. That
inherited certificate was not freshly executed here. The elementary new
degree bound does not depend on it.

The primary literature inspected for the exact interfaces included
Monks–Yazinski's autoconjugacy manuscript, Sterin–Woods' base-conversion
paper, Grieve–Wang's moving-target gcd theorem, Corvaja–Zannier's fixed
polynomial gcd theorem, and the standard network capacity criterion as
stated in Benjamini–Hermon's recurrence paper. None is cited as supplying
the unresolved universal arithmetic step. Exact links and hypotheses are
kept next to the mathematical arguments.

## Exact publication gate

After the review files and manifest are frozen, the publication procedure
creates the commit object without moving the branch. It fetches that exact
commit into a clean complete checkout and runs:

~~~bash
python -X utf8 -B tools/validate.py --receipt /absolute/path/outside/checkout/published-checkout-validation.json
~~~

The resulting exact commit, tree, command outcomes, and receipt SHA256 are
recorded on PR175 only after that execution succeeds. The branch is then
advanced with a non-forced, expected-parent update, and the remote ref and
PR head are read back. An exact receipt cannot be embedded in the same
commit whose bytes it validates; this report does not claim otherwise.

[previous-pr-description.json](previous-pr-description.json) preserves the
preceding published PR description, including its exact checkout receipt
and source pins. [FILES.json](FILES.json) lists the new packet files and
their SHA256 values, excluding the manifest itself.

The branch keeps all earlier checkpoints. Main, workflows, settings, and
other contributors' branches are outside this publication's scope.
