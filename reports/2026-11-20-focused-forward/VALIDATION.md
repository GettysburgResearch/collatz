# Focused forward packet: exact publication and execution scopes

The scientific content and two forward reviews were published in PR #148 at
commit **`8f50cd6f61d59ff2cf5547604dd6a28349bd19af`**, tree
`88805a31ac52b45d14fa81114ade1aa5dec17417`.

The parent re-queried GitHub, fetched that commit, and selected it in a
separate clean, complete checkout with **372 tracked files**. All executions
below took place in that fetched checkout on 20 November 2026. The report
and these receipts were added afterward. The receipts identify their actual
source commit and do not purport to contain their own future commit hash.

## Complete repository validation

Executed:

```sh
python -X utf8 -B tools/validate.py --regressions --receipt /workspace/scratch/6c37546fb87e/focused-checkout-validation.json
```

All **11** repository validation and regression commands exited zero.
The final output was:

```text
PASS checkout validation; not mathematical verification
```

The actual receipt, including checkout commit, tree, tracked-file count,
commands, output and timing, is [checkout_validation.json](checkout_validation.json).
The commit and tree did not change during execution. A subsequent explicit
status check was clean. This is repository integrity and bounded regression
evidence, not a universal mathematical proof.

## New mathematical checkers executed on that commit

The parent compiled the published C++ source with:

```sh
g++ -std=c++17 -O3 -Wall -Wextra -Wconversion research/focused-forward-20261120/pressure/height_replay.cpp -o /tmp/collatz-focused-height-replay
```

The new binary's SHA-256 was
`74899d1cce9580e3b324ca43f9ce5ee6aa50cb2d52bd6b294149ac8732b4bc90`,
exactly matching the binary in the originating horizon-1,500 and
horizon-2,000 receipts.

The following six commands all exited zero:

```sh
python -X utf8 -B research/focused-forward-20261120/three-ray/check.py
python -X utf8 -B research/focused-forward-20261120/five-ray/check_finite_clock_barrier.py
python -X utf8 -B research/focused-forward-20261120/five-ray/check_paired_returns.py
python -X utf8 -B research/focused-forward-20261120/pressure/height_certificate.py --horizon 1000 --python --controls
python -X utf8 -B research/focused-forward-20261120/pressure/height_certificate.py --horizon 1000 --executable /tmp/collatz-focused-height-replay
python -X utf8 -B research/focused-forward-20261120/pressure/check_review.py --executable /tmp/collatz-focused-height-replay
```

The exact commands, output, expected exit codes, timing, and file digests are
in [research_validation.json](research_validation.json). The observed scopes
include:

| Packet | Checks actually performed |
| --- | --- |
| Three-ray | 2,000 grade pairs; 1,139 aligned pullback diagrams; 2,048 initial guard replays; 130 forced higher odd valuations; 360 prescribed next valuations; 156 constant/periodic schedule witnesses with exact stopping checks; 1,698 equal-factor divisibility checks; 16 variable finite schedules. |
| Five-ray finite clock | 8,191 affine words; 16,129 word pairs; 8,190 far-interval parameters and 8,190 natural-shell parameters; 256 paired-return replays; arithmetic margins and two negative controls. |
| Five-ray returns | 126 binary cells; all 100 cross-arm affine comparisons; 65,536 finite target-gate regressions; 384 rule replays; all 46,656 cells of the residue-domain period, with 1,520 permitting a reduction; 264 conditional-path and 2,048 scaling-model replays. |
| Root horizon 1,000 | Independent uncached Python and freshly compiled C++ agreed on all 9,759 candidates, root maximum 0 and maximum nonroot score -12. The C++ maximum first-hit odd depth was 113. The Python inverse-tree controls at horizons 0, 1, 10, 20, 30 and 40 also passed. |
| Independent pressure checker | 54 cutoff/horizon comparisons covering 3,420 candidate cases; 10,100 legal inverse-one letters; 199 local height-ratio comparisons; exact rational positivity of the all-scale coefficient. |

The proofs establish the all-family quantifiers in the stated local
results. These finite checks are supplementary evidence for their formulas
and implementation, not substitutes for those proofs.

## Assertion-disable controls

Each of the three assertion-based forward checkers was also invoked once
with `-O` and once with `-OO`, while retaining `-X utf8 -B`. All **six**
invocations correctly exited with status `1` and an explicit refusal to run
with assertions disabled. Those are expected negative-control successes,
not six successful verification runs.

The pressure checker uses explicit condition checks. Its normal run and the
independent Python/C++ comparison are recorded above.

## Saved exploratory witnesses, digests, and local links

The parent independently replayed all **178** selected paired-return rows
in the saved TSV, checking both ordinary paths, odd counts, target residues,
and the stated expansion direction. The listed ternary cylinders form an
antichain; their exact measure is `11842/59049`, normalized on all of
`Z_3`, equivalently the natural density of their integer residue classes.
This verifies those witnesses and their union, not completeness of the
exploratory search or the absence of a longer branch for any remaining target.

All **10** pressure audit-snapshot file digests and Git blob hashes matched
the fetched files. The receipt records SHA-256 for all **23** files added by
the scientific-content commit. The parent checked all **18** relative file
links in those new Markdown files. This checked local file targets, not
external pages or Markdown heading anchors.

## Originating large computations and independent reviews

The horizon-1,500 and horizon-2,000 computations were actually executed
before the publication. Their saved receipts, exact candidate cutoffs,
implementation bounds, and source hashes appear in the
[pressure packet](../../research/focused-forward-20261120/pressure/README.md).
The depth-2,000 run covered 328,208,203 odd unit candidates and returned
`W_2000(1)=0` under H1's exact height reduction.

The parent and independent reviewer did **not** repeat those two larger
runs during clean-checkout validation. They reconstructed the height theorem,
audited memoization and checked integer-overflow guards, independently
checked the cutoffs, reproduced the same compiled binary, and performed
smaller separate arbitrary-integer comparisons. The originating run,
independent implementation audit, smaller replay, and repository validator
are distinct evidence levels.

The independent three-ray reviewer additionally executed a separate direct
reconstruction of 256 mixed finite schedules and 468 exact periodic maxima,
covering 2,856 physical guarded returns. Its source and execution scope are
reported in [THREE_RAY_REVIEW.md](THREE_RAY_REVIEW.md). The parent reconstructed
the five-ray arguments, including the published Baker--Wuestholz input, as
recorded in [FIVE_RAY_REVIEW.md](FIVE_RAY_REVIEW.md).

## Mathematical boundary

The work includes independent agent reconstruction, exact finite arithmetic,
and source-qualified use of one analytic theorem. It has not been certified
in a proof assistant or accepted by an external mathematical review.

No universal ordinary merger selector, infinite-depth root bound, arbitrary
cycle exclusion, or all-time escape exclusion has been obtained. In particular,
none of the successful commands turns the finite statement `W_2000(1)=0`
into a statement about every horizon. Collatz remains open in this packet.
