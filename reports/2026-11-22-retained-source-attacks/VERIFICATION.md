# Verification scope: retained-source attacks

Date: 22 November 2026. Starting PR180 checkpoint:
`a66a44c9bf058cd7efe1018827ddda9a13297a21`.

**This is a research checkpoint. Collatz is not proved.** The new work
consists of four direct closing attempts with scoped written deductions,
two finite Lean declarations, and four independent reconstruction reviews.
It changes no earlier proof packet or conjectural status.

## Fresh Lean execution

Executed from the new research checkout:

```sh
python research/retained-source-attacks-20261122/check_lean.py \
  --mathlib /workspace/scratch/46eba7b29f50/lean-runtime-next/mathlib4 \
  --lean /tmp/collatz-180-fast/bin/lean \
  --report-dir reports/2026-11-22-retained-source-attacks
```

**PASS.** `SurvivalCurvature.lean` and the separate `SurvivalAudit.lean`
compiled into a fresh temporary output directory, with warnings treated
as errors. Both public theorem audits report only `propext`,
`Classical.choice`, and `Quot.sound`. No earlier project Lean module was
imported or recompiled.

Compiler: Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`.
Mathlib checkout: `d13f23b723b8a846827a245b89c10fc7d3f11612`.

The formal statements concern the literal finite polynomial
`prod (1 - z/(3n+1))`, its first two formal derivatives, the exact
negative moment determinant, and strict negativity for a nonempty list
of ordinary states. They do not formalize the infinite operator,
canonical path law, external routing theorem, or Collatz convergence.

[Compiler receipt](lean-check.json) · [Complete compiler output](lean-build.log) ·
[Public statement inventory](../../research/retained-source-attacks-20261122/THEOREMS.json).

## Independent mathematical reconstruction

The four notes were reviewed by researchers other than their authors:

| Note | Review focus |
|---|---|
| Legal descent | Full original interval premise, exact window integrality, complete grade, all-length gap obstruction, propagated carry and original slack |
| Sibling mass | Primary v4 route count, actual integer legality, critical-weight cancellation, full stopping antichain, periodic extension and density normalization |
| Canonical charge | Both inverse probability rows, finite signed entropy sum, clock endpoints, whole ordinary path law, physical normalization and nonremovable pole |
| Analytic parameter | Uniform actual-path product bound, weighted operator norm, entire order, Laplace moment contradiction, unchanged-source curvature and finite Lean algebra |

[REVIEW_SCOPE.json](REVIEW_SCOPE.json) binds each proof and review by
SHA256, as well as the two compiled source files. The only analytic
wording correction requested was replacing a full-path count equality by
an inequality when summing over a subset. The final reviewed note contains
that correction. The canonical reviewer also requested the pointwise
identification at parameter one and the explicit complex continuation
domain; both are present in its bound source bytes.

These are independent in-session reconstructions. They do not certify
the entire external analytic proof chain in the recent routing manuscript
or re-audit the earlier canonical construction. Each imported statement
retains its precise source qualification. No review verdict extends to
the open global closing estimate.

## Source and artifact checks

The source snapshot contains metadata for 122 open PRs and 20 exact
inspected file pins with Git blob and SHA256 identities. Primary literature
version, location, use and access limits are recorded separately. JSON
parsing, relative links, the four proof/review bindings and the two
compiled-source identities were checked.

The complete-checkout repository integrity gate is run after committing
and again on the fetched published commit. Its execution receipt is
generated outside the checked checkout, and its exact identity is recorded
in the PR description after read-back. That gate checks repository
integrity; it is separate from the mathematical reviews and Lean scope
above. The optional historical regression bundle is not part of this
checkpoint's replay.

The previous PR description is preserved in
[pr-description-before.json](pr-description-before.json).
