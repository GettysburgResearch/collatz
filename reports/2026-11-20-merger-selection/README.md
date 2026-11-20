# Ordinary merger selection — sources, review and execution

**No full Collatz proof is claimed.** The scientific entry point is
[ordinary merger selection](../../research/ordinary-merger-selection/README.md).
This directory records bounded execution, independent argument reviews,
frozen dependencies and the exact publication-validation boundary.

## What changed

The packet adds a fixed 37-step factor-three smaller-partner family,
three strict reductions of the same five-ray obligation, and a compiler
realizing every nonempty finite word in two of those reductions by
infinitely many actual positive inputs with explicit terminal paths.
It also reduces every signed-target representation at a fixed signed
complexity to one finite ordinary set, settles the first two complexity
levels, and proves an explicit two-visit spacing inequality.

A separate source-qualified composition improves the height cost of
placing a long consecutive block in any ordinary component. The exact
stopping-defect criterion explains why a dense family of affine-success
cylinders cannot be silently treated as a complete ordinary selector.

The remaining gaps are stated alongside the proofs: all-input guard
coverage, convergence of every signed-complexity target set, and an
upper gap/failure bound strong enough to contradict the necessary
lower bounds. The supplied selector returns UNRESOLVED at uncovered
parameters, beginning with 2 when only its symbolic terminal is used.

## New finite replays actually executed

| Program | Executed scope | Report |
|---|---|---|
| `check_merger_selector.py` | Both 37-step identities and all prefix inequalities; 30 binary/ternary resistance fixtures; 258 six-step guard pairs; 108 repeated-rule steps; 20 symbolic terminals; 3 terminal-ending repeated runs; all 6 nonempty mixed words through length 2; 3 composed third-guard certificates; 8 malformed-input rejections. | [Merger replay](merger-selector-report.json) |
| `check_signed_target_reduction.py` | 11,791 exact signed first-hit representations, 20,632 dyadic normalizations, 10,032 strict descent witnesses; complete finite target sets through level 6; both small terminal lists and exact constants. | [Signed-target replay](signed-target-report.json) |
| `check_affine_boundary.py` | 1,760 convergent affine fixtures; 1,644 legal positive lifts; 52,362 negative forced-clock checks; 130 dyadic exceptions; 129 signed tests; 4,876 ordinary prefixes; 3 mutations. | [Affine replay](affine-boundary-report.json) |
| `verify_run_placement.py` | 14 all-lift affine identities, 16 ordinary blocks, 56 starts at common target clocks, 9,682 route-search states; 3 altered-data controls. | [Placement replay](run-placement-report.json) |

All four programs use integer arithmetic for the reported certificates.
Finite guards and fixture counts do not establish a universal cover.
The sample inverse-routing budget 120 is not a universal theorem
constant. No new Lean check is claimed.

## Independent review

- [Affine and merger review](AFFINE_REVIEW.md): AC1/AC2, ordinary legality,
  exact rank and clocks, the mixed-word theorem, and the final checker.
  The review preserves the initial hashes and records the final hashes.
- [Mixed-word review](REVIEW_MIXED_FIVE_RAY_WORDS.md): a separate algebraic
  reconstruction and 28 ordinary realizations across all 14 nonempty
  words through length 3; [independent receipt](mixed_word_review_report.json).
- [Signed-target review](REVIEW_SIGNED_TARGET_ARITHMETIC.md): STA1–STA4
  at their explicit dependency boundary;
  [independent finite-set reconstruction](signed_review_report.json).
- [Geometry source audit](GEOMETRY_SOURCE_AUDIT.md): exact imported
  quantifiers and why first-landing counts or inverse-cone compilation
  cannot be substituted for supplied-target routing.
- [Root reconstruction](ROOT_REVIEW.md): independent algebra,
  positivity, rank, constant and implementation checks.

The negative-clock implementation defect found in review is fixed.
Supplied meeting certificates now require positive integer sources and
endpoints and nonnegative integer clocks. The assertion-based checkers
reject execution under `-O` instead of silently disabling validation.

## Complete-checkout validation

Repository integrity is a separate gate from the new arithmetic replays
and from mathematical proof review. The complete command is:

```sh
python -X utf8 -B tools/validate.py --regressions --receipt /tmp/collatz-merger-content-validation.json
```

The publication workflow validates the clean complete scientific content
commit and adds its exact receipt in a subsequent documentation commit.
The receipt identifies the tested commit and tree; its verdict does not
silently extend to later scientific edits.

[Frozen provenance](PROVENANCE.md) · [Scientific content hashes](content-sha256.json).
