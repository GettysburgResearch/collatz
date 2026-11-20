# Validation and publication record

The mathematical content of this research packet was published to
[PR #148](https://github.com/GettysburgResearch/collatz/pull/148) at commit
`4312e70370a89e474bc8812734760c7de9798315`, tree
`bd783a96fd9f76ec453d2e633a42384d64c62887`.

That exact commit was fetched from GitHub and checked out detached in a
separate, clean, complete worktree with **346 tracked files**. The tests below
ran there on 20 November 2026. These receipt files and the links to them were
added afterward; the receipts do not pretend to contain their own commit.

## Repository validation

```sh
python -X utf8 -B tools/validate.py --regressions --receipt RECEIPT.json
```

All **11** commands exited zero. The final status was:

```text
PASS checkout validation; not mathematical verification
```

The checkout commit, tree and tracked-file count were identical before and
after execution. The actual command arguments, output, timing and scope are
preserved in [checkout_validation.json](checkout_validation.json). This checks
repository structure, frozen identities and the bounded regression bundle.
It does not certify the new mathematics.

## New elementary and cycle checks

The parent ran these four commands in that same clean published checkout:

```sh
python -X utf8 -B research/forward-bridge-20261120/check.py
python -X utf8 -B research/independent-attack-20261120/check_cubic_descent.py
python -X utf8 -B research/independent-attack-20261120/check_square_obstruction.py
python -X utf8 -B research/independent-attack-20261120/check_minimum_defect.py
```

All passed. [research_validation.json](research_validation.json) records the
actual output and exact SHA-256 of every executed checker. It also records
the successful digest comparison for the policy fetched from GitHub and a
check that all 44 relative links in the new packets and reviews have existing
local targets. The link check does not validate external websites or headings.

The all-family mathematics is supplied by the written proofs and their
qualified analytic dependencies. The finite replay ranges do not justify
an extrapolation to every integer.

## Inverse certificate verification

The author executed the documented end-to-end command after freezing the
certificate and verification implementation:

```sh
python -B research/inverse-escape-20261120/verify.py research/inverse-escape-20261120/certificate.json
```

It rebuilt the C++ fixed-policy reconstructor, reached the exact fixed point
at iteration 202, authenticated all 43,046,721 reduced credits, checked every
selected reduced inequality, passed 740 affine replays and rejected the
zero-credit and truncation controls.

Separately, the independent reviewer executed the reconstructor afresh,
expanded and compared all 344,373,768 full-table bytes, checked all 86,093,442
physical states against the published policy, directly checked 258,280,326
collapsed lifts and all terminal bounds, and replayed 2,220 ordinary forward
paths. Three independent corruption controls were rejected. These are actual
executions, separately described with exact source and artifact hashes in
the [independent inverse review](../inverse-physical-review-20261120/README.md)
and its JSON receipts. The parent additionally reconstructed the proof and
read the load-bearing verifier formulas.

The clean remote checkout's policy digest is
`977c546492b6882bdd3da68bb392a83945c8ebadda308c362c583312ec0c5703`, exactly
the reviewed artifact. It contains a finite all-lift certificate, whose
universal inverse consequence is proved in P1. The finite ordinary replays
are additional implementation checks, not the source of that quantifier.

## Honest scope

The publication contains independent reconstruction by separate research
agents, not formal proof-assistant verification or external mathematical
acceptance. The cycle argument retains its stated logarithmic-form and
p-adic Subspace Theorem dependencies. No universal forward convergence
argument was obtained. No failure of a finite search is promoted to an
all-precision impossibility result.
