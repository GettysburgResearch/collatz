# Review and publication record

Scientific entry: [Global forcing attempts](../../research/global-forcing-20261121/README.md).

**Collatz remains unresolved.** Proof reconstruction, finite computation
and repository integrity are separate evidence layers.

## Mathematical reconstruction

[ROOT_REVIEW.md](ROOT_REVIEW.md) pins the four proof files and reconstructs
their domains, all-parameter arguments, external inputs and exact gap.
The carry construction was also reconstructed by both other route
authors. The certificate author separately reconstructed the renewal,
and the arithmetic author separately reviewed the terminal-phase result.
These are internal reviews; no external referee acceptance or formal
proof-assistant verification is claimed.

Concurrent sources were refreshed after the initial proof freeze.
[SOURCES.md](../../research/global-forcing-20261121/SOURCES.md) and the
three LATEST_COMPARISON notes identify overlap, stronger neighboring
results and the still-unproved closing inputs. The metadata
[source-heads.json](source-heads.json) inventories 105 open PRs and 20
recent closed PRs. It is not a verdict on every branch.

## Reproduce this packet

In a clean complete checkout, with receipts placed outside that checkout:

    python -X utf8 -B reports/2026-11-21-global-forcing/run_checks.py --receipt /absolute/external/path/scientific.json
    python -X utf8 -B tools/validate.py --regressions --receipt /absolute/external/path/repository.json

The first command checks the content manifest and executes three
standalone scientific programs, each normally and with Python's -OO.
It requires exact byte equality with the complete frozen reports and
verifies that the checkout remains clean. These six executions cover
finite algebra, modular cases, rank computations, ordinary first-hit
certificates and the specified negative controls. Infinite run lengths,
arbitrary groups, and cycle ceilings are justified by the proofs, not
enumeration.

The second command is the repository's required bounded validation
bundle. Its integrity checks do not certify mathematical theorems.

## Publication receipts

The complete clean checkout at commit
`3aa75073e5d000b3ccf6ac29cbfbda1b14445c6c`, tree
`5e79c89edd930adc6ff7fc2021e872c7c021a0bd`, passed both commands above:

- [Scientific execution](scientific-execution.json): six executions,
  all 25 manifest files verified, every complete report byte-identical,
  and the checkout clean before and after.
- [Repository validation](repository-validation.json): all eleven
  required bounded commands passed in that actual checkout.

[VALIDATION.md](VALIDATION.md) records exact receipt hashes, the earlier
orchestrator correction, and the distinction between the executed content
commit and the later publication-metadata child. That child preserves
all 25 manifest entries. Its own actual final-head repository execution
and remote readback are recorded in the PR, rather than inventing a
self-referential receipt inside its own commit.

The [initial failed orchestration receipt](preliminary-scientific-failure.json)
is preserved. The carry checker uses `success: true`; the first runner
incorrectly expected `status: PASS` from all three programs. It stopped
even though the carry program had returned zero with the exact frozen
report. The runner now validates each declared schema. The scientific
programs, reports and mathematical proofs were unchanged by that repair.
The [initial repository run](preliminary-repository-validation.json)
passed on its separately identified earlier head.

The manifest deliberately excludes itself, this publication README,
VALIDATION.md, and the execution receipt JSON files. It includes the
scientific notes, scripts, frozen reports, reviews, source comparisons,
source inventory, replay driver, and active research index.
