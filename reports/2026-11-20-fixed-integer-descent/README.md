# Investigation: fixed ordinary integer descent, 20 November 2026

**No complete Collatz proof was obtained.** This branch preserves a new
bounded-run finite-core result, three adaptive merger reductions, an
improved translated-interval record bound, their computational certificates,
and precise statements of the remaining gaps.

The scientific entry point is the local
[proof-packet overview](../../research/fixed-integer-descent/README.md).
This report records source pins and evidence. It does not replace the
repository's integrated scientific status or promote unrelated source
claims.

## Strongest supported conclusions

1. **Complete bounded-run reduction.** For every fixed bound on binary
   one-runs, an explicit finite adaptive core contains every ordinary odd
   orbit that never exceeds that bound. A signed lower shadow extends the
   existing positive-shadow popcount construction to long one-runs.
2. **Universal six-run alternative.** Every odd source within cap six
   reaches 1 or leaves the cap within 107 odd events. The complete core
   has 19,371,072 sources; its capped basin has exactly 157,728 sources.
   The largest such successful odd source is 68,719,605,301. There is no
   nontrivial positive cycle confined to six runs.
3. **One smaller comparison suffices on three unbounded guarded families.**
   The `Good` valuation guards in FM-002 reduce `P(n)` to one strictly
   smaller `P(a)`. Eight coefficientwise certificates add 35 odd residue
   exclusions beyond the 48 inherited from PR #146, out of 192 classes
   modulo 384. Universal coverage remains open.
4. **Recursive finite-path occupancy.** An exact finite recursion bounds
   the occupancy of *any translated interval* on one simple ordinary path.
   It yields a uniform `O(X^(19/20))` bound and tighter conditional
   coefficient-record clocks. Neither a predecessor-basin estimate nor
   universal stopping follows.

The first two claims cover infinitely many possible input integers by
proof of finite reduction. The finite trajectory censuses alone would
not support those quantifiers. The merger predicates likewise have
coefficientwise proofs on whole classes, not only sampled evidence.

## Source pins and scope

| Source | Frozen head | Clauses used |
|---|---|---|
| Main | `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` | `research/astra-three-routes/pass3/FINITE_RECORDS.md`, T-A3-651--653: finite reciprocal budget and near-source record window |
| PR #141 | `5025ef464d4b6d4f4a412a3e33c3477de68dfa8b` | `research/ay-persistent-20261031/PROOF.md`, HC-1--HC-3 and HC-5--HC-6: popcount-core mechanism and guarded rewriting transfer |
| PR #146 | `7d04c4dd756cfe495eb3eee78eba35a99085cd2a` | `research/upper-bit-mergers/THREE_RAY_SMALLER.md`: seven class certificates and finite `81h` convergence implication; nearby pair mechanisms credited |
| PR #148 | `6ff18e4f63be8f3bece76215fcfe44d83b001d7f` | Context and overlap check only; no inverse compiler or powered-cycle theorem imported as a dependency |
| PR #149 | `92c0129e794dde3ec55ceec470a12d51ba3f7e2f` | Context and closure-boundary audit only; no global potential estimate assumed |

The current GitHub heads were queried at the beginning of this pass. The
local PR #149 reference checkout had its scientific-content commit
`9dcb3b35a8e407af7635469f5643e9fa2f5a1077`; the remote head above also
contains subsequent provenance/attribution documentation. No review of
the entire later branch is claimed. Main's source tree was cloned into
a new branch; existing research and frozen evidence were not changed.

Garcia--Tal's 1999 orbit-sparsity mechanism is credited in the interval
paper. Its author publication page was read; the publisher PDF returned
HTTP 403 on the direct retrieval attempt. The new local interval proofs
are self-contained and do not import a constant from that inaccessible
PDF. Yolcu, Aaronson and Heule receive the original rewriting-system and
Collatz-equivalence attribution. No exhaustive external novelty audit is
claimed.

## Computational evidence

| Evidence | Actual scope |
|---|---|
| [Cap-six core report](arithmetic-run-cores-cap6.json) | Complete adaptive core; 37,448,205 literal odd edges; separate inverse BFS equality on all 157,728 successes |
| [Earlier cap-five report](arithmetic-run-cores.json) | Preserved prior checkpoint through cap five; not silently overwritten by the larger run |
| [Modular hitting report](modular-run-hitting.json) | 73,400,320 residue/cap/shift state checks; exact maxima at the stated moduli, ordinary upper bounds via M1 |
| [Independent modular report](modular-independent-audit.json) | Separate prefix/suffix cycle algorithm, 33,554,432 cap/shift tests at modulus `2^24` for caps five and six |
| [Independent run-core report](run-core-review.json) | Separate tree construction, string run count, and literal halving through cap four; no independent cap-six enumeration claimed by that reviewer |
| [Merger report](merger-report.json) | Eight symbolic rows; 25,002 adjacent cases; 16,145 bounded adaptive cases; 705 large-valuation cases; 5,120 neighborhood replays; nine rejected controls |
| [Finite-path report](drift-report.json) | 8,191 parity words; 16,382 ordinary lifts; translated interval and coefficient-record replay; four rejected controls |
| [Recursive interval report](interval-bootstrap-report.json) | Full recursive minimum through width 4096; restricted-policy upper bounds for larger widths; 55,296 literal translated-window checks |
| [Guarded rewriting report](rewriting-report.json) | All eleven rules on 19,531 proper words; 501 schedules and 32,693 literal rewrites; large one-run inputs through 4096 bits |

Counts in different rows overlap and must not be added as a count of
distinct trajectories. Neither a file digest nor repository integrity
validation proves a mathematical statement. The large-width interval
policy values are explicitly upper bounds, not the full recursive minima.

## Independent reconstruction

The three delegated investigations were followed by cross-review and a
root reconstruction of the signed-cut algebra, adaptive core coverage,
merger paths, and interval induction. Review records pin file bytes and
state what the reviewer actually replayed:

- [Run-core review](RUN_CORE_REVIEW_BY_DRIFT.md).
- [Modular certificate review](MODULAR_REVIEW.md).
- [Adaptive merger review](MERGER_REVIEW.md).
- [Recursive interval review](INTERVAL_REVIEW.md).
- [Guarded rewriting review](REWRITING_REVIEW.md).

The reviews caught and corrected a missing "nontrivial" in one draft
cycle statement and an incorrect numerator in an explanatory merger
constant. Corrections were made before the corresponding frozen review.
Different agents can still share mistakes. These records are independent
reconstructions within an agent team, not external peer review or formal
verification. The research claims remain PROPOSED for repository review.

## Replay commands

From a clean complete checkout, run repository validation separately from
the new scientific replays:

```bash
python -X utf8 -B tools/validate.py --regressions
python -X utf8 -B experiments/fixed_integer_arithmetic.py --max-cap 6 --compare reports/2026-11-20-fixed-integer-descent/arithmetic-run-cores-cap6.json
python -X utf8 -B experiments/fixed_integer_run_hitting.py --extended --compare reports/2026-11-20-fixed-integer-descent/modular-run-hitting.json
python -X utf8 -B experiments/fixed_integer_mergers.py --compare reports/2026-11-20-fixed-integer-descent/merger-report.json
python -X utf8 -B experiments/fixed_integer_drift.py --compare reports/2026-11-20-fixed-integer-descent/drift-report.json
python -X utf8 -B experiments/fixed_integer_interval_bootstrap.py --compare reports/2026-11-20-fixed-integer-descent/interval-bootstrap-report.json
python -X utf8 -B experiments/fixed_integer_rewriting.py --compare reports/2026-11-20-fixed-integer-descent/rewriting-report.json
```

The complete cap-six replay is materially larger than the other commands.
All programs use standard-library exact integer or rational arithmetic.
The [validation note](VALIDATION.md) distinguishes the clean-checkout
executions, the final publication identity, and the earlier research runs.

## Failed strengthening and the next missing inference

For the one-run inputs `n_a=2^a-1`, the first `a-1` odd states remain above
the initial source. Therefore no finite guaranteed first-descent clock can
depend only on the initial number of runs. A cap exit does not repay the
original numeric comparison.

The merger guards also remain incomplete: even known convergers can lie
outside a bounded search's certificates. Neighborhoods constructed from
known convergent seeds do not prove convergence of an unproved seed.

The interval recursion bounds how many coefficient records *could* occur,
while the closing argument still needs a certificate that the next record
does occur. It cannot turn sparse orbit states into a bound on an entire
nonconvergent predecessor basin.

The useful next step is a source-preserving repayment law across run-cap
increases, a complete lower-demand merger selector, or a proof of the
required ordinary coefficient crossing. No such global law is established
by this pass.
