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
[source-heads.json](source-heads.json) inventories105 open PRs and20
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

At this scientific-content stage, clean-checkout publication executions
have not yet been recorded in this file. The publication metadata child
will add the actual content-commit receipts and exact identities. It
must preserve every file in CONTENT_SHA256.json. The final PR describes
the separately observed checks on its actual final head; a receipt
cannot recursively contain its own future commit identity.

The manifest deliberately excludes itself, this publication README,
VALIDATION.md, and the execution receipt JSON files. It includes the
scientific notes, scripts, frozen reports, reviews, source comparisons,
source inventory, replay driver, and active research index.
