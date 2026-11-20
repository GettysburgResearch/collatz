# Published scientific snapshot and actual checkout validation

Repository: `GettysburgResearch/collatz`.
Branch: `research/allhands-global-closure-20261120`.
Base main: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.

The scientific packet was published at
[`e1be45b8a94ef8ad5c00761c4dffd4d51da26138`](https://github.com/GettysburgResearch/collatz/commit/e1be45b8a94ef8ad5c00761c4dffd4d51da26138),
with tree `86d833ea5dee2c760105638564ae3349334849eb`.
The publication follow-up adds only this record and the actual checkout
receipt. All scientific files, reviews and finite replay outputs are unchanged.

## Results and scope

The [research overview](../../research/allhands-global-closure-20261120/README.md)
sets out the prime-support peak theorem, exact positive circulation, and an
independent reconstruction of the now-overlapping depth-two certificate
mechanism. The [source refresh](../../research/allhands-global-closure-20261120/LATEST_146_COMPARISON.md)
credits PR146 at `e238c63a5d57f96bb063b7472498d1977df51951`, which advanced
during this round. The failed uniform-J and prime-creation transfers are
retained with their precise missing conditions.

All mathematics remains PROPOSED. The [review record](README.md) separates
AI proof reconstruction, reused producer code, independently implemented
acceptance code, source-qualified inputs, and finite execution. No complete
Collatz proof, external formal rebuild, or human referee acceptance is claimed.

## Executed verification

The six packet programs ran normally and under `-OO`, for twelve successful
executions. Every output matched its retained report byte for byte, including
the six normal/optimized comparisons. The actual commands, program hashes,
output hashes and times are in [execution-receipt.json](execution-receipt.json).

After the branch was published, its exact scientific commit was fetched back
into a separate complete detached checkout. The 345-file tree was clean
before and after:

    python -X utf8 -B tools/validate.py --regressions

All eleven commands passed. The exact input commit and tree, commands,
output, exit codes, and timestamps are retained in
[scientific-checkout-validation.json](scientific-checkout-validation.json).
The 29 content hashes in [CONTENT_MANIFEST.json](CONTENT_MANIFEST.json) were
also checked against that fetched checkout. Local relative links in the new
packet were checked before publication.

These checks validate file identity, repository integrity and specified
bounded examples. The universal arithmetic statements depend on their
written proofs and explicitly named source inputs. The remaining global
implication is open.

This receipt intentionally identifies its earlier scientific commit. The
final publication-head validation is reported separately in the pull request
to avoid a commit claiming to contain its own hash.
