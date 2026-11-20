# Evidence for the three-package Dirichlet research packet

The mathematics starts in the
[scientific packet](../../research/gemini-dirichlet-global-20261120/README.md).
This directory records source identity, proof-review scope, and execution.
The packet is PROPOSED research. Neither these receipts nor repository
integrity establish Collatz.

## Inputs and exact source revisions

The thirty extracted files from the three user-supplied ZIP archives are
[preserved byte-for-byte](../../archive/gemini-followups-20261120/README.md),
with a manifest of original ZIP and extracted-file hashes. The files'
original proof-status labels remain source text, not accepted verdicts.

[source-pins.json](source-pins.json) identifies the main base and the exact
repository revisions used for dependencies and comparisons. Its twelve
file hashes were computed from the pinned Git objects. Later revisions of
those branches are outside these review claims.

The finite variation input is PR146 at
`7d04c4dd756cfe495eb3eee78eba35a99085cd2a`. Three byte-exact source proofs
are cached separately under the source archive, with their own manifest,
so the new finite replay can run without network access or another worktree.
PR148, PR149, PR151, PR152, and PR153 provide the separately identified
comparison results; they are not imported wholesale.

## Independent mathematical reviews

| Review | Scope and outcome |
|---|---|
| [Ordinary analytic argument](ORDINARY_DIRICHLET_REVIEW.md) | Reconstructed the dyadic kernel, odd/full norm factor, complex coarea, full-sequence logarithmic limit, irrational rotation, five-ray transfer, and critical-moment claims. Two scope clarifications were incorporated. No remaining analytic objection at the frozen note. |
| [Finite ordinary variation input](TRIPLING_VARIATION_REVIEW.md) | Reconstructed the neighbor comparisons, complete residue coverage, all seventeen edges, and bounded congestion. Supplies explicit conservative constants and verifies that no additive error or logarithmic multiplicity is hidden. |
| [Exact Farkas certificates](FARKAS_CERTIFICATE_REVIEW.md) | Independently derived all 810 residual-coordinate formulas, checked outward interval bounds and contradiction signs, and verified the two-point scope. No r8 or interval-cover conclusion is included. |

The ordinary analytic review is pinned to note SHA-256
`d5229d794b97ba4c7663f105388ed597251d34fd678cc2189c39ebf0c7b43c74`;
[its review receipt](dirichlet-analytic-review.json) records the source and
review hashes. These are independent argument reconstructions by collaborating
agents, not external journal review or proof-assistant verification. The root
agent also checked the arguments and the endpoint companion during assembly.

## Exact scoped replay

[exact-replay.json](exact-replay.json) records **eight successful runs**:
each of four new checkers ran in normal and optimized Python, and each pair's
complete receipt payloads matched. The driver also rejected a deliberately
damaged serialized Farkas normalization in both interpreter modes. Every
new verification condition remains active under `-O`.

The exact controls include:

- Four ordinary affine merger cylinders, all 72 required residue witnesses,
  eight affine trajectory identities, all seventeen chain edges, and 2,079
  exact rational scalar-kernel controls, including the missing-factor
  negative control.
- All 81 and 729 coordinates of the two supplied Farkas vectors, evaluated
  with outward integer intervals; uniform feasible controls at exponent one;
  and 36 finite incidence checks supporting the separately proved matrix
  formula.
- Coefficient and Parseval identities, representative all-period controls,
  both exact rational-cycle counterexamples, legal inverse letters, and the
  denominator-height sign correction.
- The complete 162-state Bellman equality and policy, equality with the
  exported certificate, whole-cylinder compiler integration controls, the
  supplied affine counts, nine rational-cycle controls, and exact finite
  averaging identities.

The universal statements rest on the adjacent written proofs. These finite
checks do not replace the infinite summation, analytic continuation,
irrational-rotation, minimax asymptotic, or operator arguments. In particular,
none proves that a hypothetical ordinary separating boundary has the missing
finite moment.

## Original numerical replay

[original-replay.json](original-replay.json) records seven outer commands
executing all **ten original leaf scripts** in temporary copies. All returned
success. The archived source files were authenticated again afterward.
This is reproduction of supplied computations, not acceptance of their
mathematical labels or a formal build of the Lean skeleton.

The v3 generated receipt and exported decimal-vector JSON reproduced
byte-for-byte. The v2 generated receipt differed at two floating-point error
fields, by ordinary roundoff-size values. The complete differences are in
[original-replay-differences.json](original-replay-differences.json); no
original file was overwritten or resealed.

## Repository validation boundary

The scientific commit was published and read back from the remote branch:

- Commit: `4937497e153c7894c42f8fbcd1bd3ec1d8487d0a`.
- Tree: `7c5f0f2211a020f1a49f8cb08efd39b34463a6f8`.
- Base: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.

A separate clean, complete checkout of that exact commit then ran
`python -X utf8 -B tools/validate.py --regressions --receipt PATH_OUTSIDE_CHECKOUT`.
All **eleven commands passed**. The checkout's 375 tracked files, commit,
and tree were unchanged afterward. The complete output is preserved in
[repository-validation.json](repository-validation.json).

The four new checkers also ran again in both interpreter modes from this
published checkout: eight successful replays and two expected rejection
controls. Every complete mathematical payload and every scientific-file
hash matched the prepublication run. See
[published-exact-replay.json](published-exact-replay.json) and the
[publication record](publication.json).

These receipts are added in a subsequent documentation commit. The tested
revision is the scientific parent specified above; no receipt is attributed
to the later commit containing itself. The final branch head is reported in
the PR after remote readback. This is local execution of the repository's
complete gate, not a claim that GitHub Actions ran successfully. No scientific
file changes in this evidence-only follow-up.
