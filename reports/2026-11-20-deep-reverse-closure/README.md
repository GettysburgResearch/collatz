# Review and replay guide

The [scientific overview](../../research/deep-reverse-closure-20261120/README.md)
is the entry point for the mathematics. **Full Collatz remains open.**
These records describe internal agent reconstructions and executed finite
checks. They are not human referee acceptance, proof-assistant verification,
or acceptance of another packet's unstated hypotheses.

## Independent claim-level reconstructions

| Claims | Review | Separate finite implementation |
|---|---|---|
| K1--K3: exact reverse kernel, rank-five congruences and residuals | [Reverse-kernel review](REVIEW_REVERSE_CERTIFICATE_KERNEL.md) | `check_reverse_kernel_review.py` uses literal ordinary clocks and a separately enumerated last-gap congruence. |
| H1--H5: conditional height bound, initial interval, finite fourth-valuation list and rank exclusions | [Height review](REVIEW_LEAST_FAILURE_HEIGHT.md) | `check_height_review.py` uses rational affines in the global source, independently of the author's cell-coordinate implementation. It covers all 71 source paths. |
| FE1 and qualified rigidity consequences | [Five-energy review](REVIEW_FIVE_SLICE_ENERGY.md) | `check_five_energy_review.py` independently reconstructs every affine query, guard, row injection, the complete cover and the exact congestion constants. |
| CS1--CS3: complete shifted-smooth boundary and exact exits | [Shifted-smooth review](REVIEW_SHIFTED_SMOOTH_COMPLETE.md) | `check_shifted_smooth_review.py` independently checks the finite complement, exact exits and visit-count controls. The named two-logarithm theorem remains an external input. |
| PP1--PP2: pure-power local core behavior and scope of a finite prime pool | [Pure-power review](REVIEW_PURE_POWER_CORE.md) | `check_pure_power_review.py` keeps the PR146 exponent progression separate from the unrestricted finite-pool construction. |
| G2--G4 and the basin residue lemma | [Guarded-clock review](REVIEW_GUARDED_CLOCK.md) | `check_guarded_clock.py` checks complete finite predecessor trees and actual compressed upper certificates without materializing enormous powers of two. |
| C3S1--C3S3: adaptive exclusion of the complete single-run certificate family, with unbounded rank, and the next explicit Mersenne target | [Single-run review](REVIEW_C3_SINGLE_RUN.md) | `check_c3_single_run_review.py` separately checks the height bases, all small parameter classes, exact clocks, compressed ordinary source congruences, and the rank-six target. |
| W1--W2: unbounded depth for cheaper Mersenne witnesses | [Mersenne-depth review](REVIEW_MERSENNE_WITNESS_DEPTH.md) | `check_mersenne_depth_review.py` independently reconstructs small-word exceptions, rational-center congruences and the slope/intercept inequality. |
| Partial five-energy renewal from PR162, with its uncovered remainder | [Partial-renewal review](REVIEW_PARTIAL_FIVE_RENEWAL.md) | A separate written reconstruction of the physical pair, exact inverse fibers, positive finite-cutoff summation and repair-mass identity; no finite computation is needed for this deduction. |

Each review identifies its exact manuscript hash; the content
manifest fixes the packaged files. Renaming or copying a file does not
change its mathematical content. The five certificate retains its author's
filename `five_cover_candidates.json`, but the published certificate is a
complete verified cover, not an incomplete search candidate.

The hash-pinned review notes retain the exploration folders and standalone
report filenames used when those reviews were performed. The publication
consolidates fresh outputs under each script's name in `packet-replay.json`;
use the repository-relative commands below for reproduction. No missing
exploration directory is required to run a packaged checker.

## What the finite checks actually establish

The universal conclusions use written arguments: affine identities on whole
progressions, complete finite residue covers, exact positive summation,
induction on a single least failing ordinary source, and the explicitly
quoted logarithm bound. Literal finite trajectories certify only the
specified numerical exceptions. Sampled large values do not prove an
unbounded theorem.

Compressed certificates state exact integer exponents and finite words,
verify their integrality and parity by modular arithmetic, and end with an
exact power-of-two halving run. Such a check is not a literal iteration for
billions of clocks. In particular it makes no assertion that a whole
unbounded family was individually enumerated.

The source PR146's Lean files were not built here. The new Python checkers
are not formal proofs in Lean. The independent reviewers do not import
their respective author implementations, although they necessarily inspect
the same theorem statements and finite certificate data.

## Reproduce the complete-checkout checks

Use a complete clean checkout of the scientific commit identified in
[VALIDATION.md](VALIDATION.md). Store receipts outside that checkout:

```bash
python -X utf8 -B research/deep-reverse-closure-20261120/check_packet.py --receipt /tmp/deep-reverse-packet-replay.json
python -X utf8 -B tools/validate.py --regressions --receipt /tmp/deep-reverse-repository-validation.json
```

The first command checks every content-manifest hash and runs every
scientific checker both normally and with `-OO`, requiring byte-identical
reports. It records the actual commit and tree, requires a clean checkout
before and after, and refuses an in-checkout receipt destination. The
second command runs the repository's existing structural and bounded
regression checks. Neither command labels these checks a Collatz proof.

Actual execution receipts are appended in a later documentation-only
commit. A receipt for one commit is not claimed to be an execution of a
later commit. The final branch head is checked separately, and its
scientific content is compared with the manifest.
