# Closure-attacks review and execution record

The [scientific packet](../../research/closure-attacks-20261120/README.md)
contains the results and remaining mathematical gaps. This report directory
keeps source identities, independent reconstruction, and actual execution
separate from those claims.

- [ROOT_REVIEW.md](ROOT_REVIEW.md) records the root's mathematical
  reconstruction and its exact scope.
- [CONTENT_SHA256.json](CONTENT_SHA256.json) freezes the scientific notes,
  checkers, expected reports, peer reviews, and root review.
- [run_checks.py](run_checks.py) requires a clean complete checkout,
  verifies those hashes, and executes five fresh report comparisons.
  Its receipt must be written outside the checkout.
- [VALIDATION.md](VALIDATION.md) identifies the actual scientific commit
  and the attached execution receipts.

The peer reviews were completed before the GitHub scientific commit
existed. They pin exact file bytes rather than asserting an invented
commit. Later execution receipts identify the real checked head and tree.

Reproduce in a clean checkout:

    python -X utf8 -B reports/2026-11-20-closure-attacks/run_checks.py --receipt /tmp/closure-science-receipt.json
    python -X utf8 -B tools/validate.py --regressions --receipt /tmp/closure-repository-receipt.json

Use fresh output paths: the scientific driver refuses to overwrite an
existing receipt. The second command is the repository's established
11-command integrity and regression bundle. The new exact checks use
explicit exceptions and do not depend on Python assertions.

The finite evidence supports the stated checks, including all-lift affine
identities. It does not establish the missing physical five law, a global
single-slice energy comparison, or unrestricted cycle exclusion. PD and
the named analytic source inputs retain their source-qualified status.
