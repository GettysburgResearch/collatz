# Collatz investigation, 20 November 2026

## Outcome

No proof of the Collatz conjecture was obtained. The delivered mathematical
work is the [robust inverse-credit packet](../../research/robust-inverse-credit/README.md):

1. An explicit, independently verified inverse-cone compiler with cost
   \(k\le\lfloor(13t+65)/6\rfloor\), extending PR #141's \(7/3\)
   finite-credit construction.
2. A general min-plus argument converting uniform finite-horizon inverse
   cost into a robust finite potential, together with a converse by
   positive random perturbation.
3. Subject to the stated external stationary-uniqueness theorem, equality
   between the infimum robust-credit slope and the infimum stationary
   mean among positive local policies at a fixed cap.
4. A separately regenerated and exactly verified small positive policy
   with stationary mean between 1.937 and 1.938. Under that external
   uniqueness theorem, the bridge proves existence of a cap-six robust
   certificate of slope 39/20. No explicit table or additive constant for
   that robust certificate is supplied.
5. Exact elementary obstructions to the attempted synchronized merger
   amplification and isolated two-edge precision actuator.

The explicit 13/6 theorem uses no external analytic theorem. The
stationary-policy bridge has an explicit source qualification. Neither
result gives forward descent or a complete ordinary merger selector.

## Frozen inputs

| Input | Frozen commit | Principal role |
|---|---|---|
| Main | `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` | Integrated science, instructions, errata and validation baseline |
| PR #146 | `fcb2b72847a82da5c6ebdc81ae4022ba9c03ae3d` | Latest binary merger bounds and pointwise merger equivalence |
| PR #145 | `dd245a712f985909f541590e3f6c179b7ba011e4` | Pressure, ordinary fibres, one-step lag, binary-run overlap |
| PR #144 | `df756794e1d8de5cabff148ef433df505e3b68b4` | Direct pressure and coercivity route |
| PR #141 | `5025ef464d4b6d4f4a412a3e33c3477de68dfa8b` | Earlier explicit inverse-credit compiler and counting obstruction |

The exact path-level predecessor and external sources are listed in
[PROVENANCE.md](../../research/robust-inverse-credit/PROVENANCE.md) and
[MERGER_AND_HEIGHT.md](../../research/robust-inverse-credit/MERGER_AND_HEIGHT.md).
Later heads do not inherit this review.

## Review boundary

The explicit table was produced by one research agent and checked with a
separately written scalar verifier by another. The parent reconstructed
the all-lift argument and reran both verifiers. A further independent
agent red-teamed the complete explicit proof and D1–D4.

The reviews found no gap within their stated scope. They required two
useful clarifications, now included: the uniqueness hypothesis concerns
all Borel stationary probabilities, and the source-qualified cone
corollary explicitly assumes \(0<c<3^t\). The final shortcut target may
be even, so its last block is not always a whole odd-map step.

- [Independent mathematical and numeric review](INDEPENDENT_REVIEW.md).
- [Detailed explicit-certificate review](EXPLICIT_CERTIFICATE_REVIEW.md).
- [Independent scalar checker](verify_credit_independent.py) and
  [its delivered-certificate receipt](credit_independent_report.json).
- [Small positive-policy receipt](small_policy_report.json).

These are agent reviews and exact arithmetic replays. No external formal
proof build, human peer review, or independent reconstruction of the
infinite-dimensional stationary theorem is claimed.

## Checks actually performed

| Check | Result and precise scope |
|---|---|
| Main integer credit verifier | PASS; 354,294 unit rows, 1,062,882 selected-action lifts, maximum credit 66, terminal minimum one |
| Independent scalar verifier | PASS on the delivered gzip certificate; same rows, lifts and action counts |
| Forward affine cone replay | PASS; 6,575 cones, including every unit tail through depth eight and selected tails of depths 40, 100 and 1,000 |
| Negative credit control | Zero potential rejected at residue five |
| Small-policy integer verifier | PASS; 486 policy rows, 162 cells, rational bias inequalities, stochastic rows and positive fifth matrix power |
| Small-policy negative controls | Zero bias and zero action labels rejected |
| Independent C++ synthesis | Reproduced the identical 354,294 potential values at iteration 670 |

The table-byte SHA-256 is
`2f12342f3a4a25ff8ed31c03ddba77b66a17d8bfea62dfaac0c0ea1cbb3273dc`.
The small-policy file SHA-256 is
`9a9545c9cfc2e6e178b773c9ce255ef4b183e96cc3037e97bb67eb1050f9d6df`.

The optional synthesis programs are not in the verifier trust base.
Floating arithmetic proposed the small policy and bias; exact integers
verified the exported certificate. A targeted 15/7 credit search at
precision 13 and action cap ten did not stabilize through 2,000
iterations. That bounded failure is not an impossibility theorem.

Repository validation is recorded separately against the committed
content snapshot. It checks repository integrity and the declared bounded
regressions, not universal Collatz convergence.

## Directions investigated without a closure

The pressure route still needs control at moving ordinary targets, or an
equivalent exclusion of boundary mass at infinity. Integrability of a
stationary profile does not control its value on every exceptional
ordinary trajectory. No uniform trace estimate was proved here.

The initially considered bounded signed-digit route overlapped with
PR #145's existing binary-run results and was not promoted as a new
contribution. Finite ternary steering probes were also superseded by
stronger external routing and stationary-law claims found during the
source review.

The merger work identified exact failures of two proposed constructions.
A common inverse word on the special binary merger pair can contain at
most one odd inverse. A lone equal-cost two-edge redistribution pays an
exponential exponent to retain an increasing number of ternary digits.
These facts restrict those constructions; they do not exclude
asynchronous mergers or coordinated longer words.

## First remaining inference toward a full proof

Every positive ordinary input must be shown to reach a smaller source,
merge with a lower-rank source, or satisfy another complete termination
criterion. Controlled inverse paths and full residue coverage do not
supply exact ordinary equality or the required height comparison. The
packet makes no claim that the source-qualified 39/20 existence theorem
closes that gap.
