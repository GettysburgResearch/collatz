# AYH continuation: persistent carry cuts and two certified orders

**PROPOSED, self-audited only. No full Collatz proof.** Additive continuation of PR #141, parent `b62f56cda3ebe1f77ea843740e37199ae0685bee`. Earlier proofs, accepted-status registries, main and workflows are unchanged. No independent AI-agent launcher was available; parallel workers here are computational processes, not a newly launched agent swarm.

Read [PROOF.md](PROOF.md) for exact statements, proofs, source credit and failure boundaries.

## What changed

**An all-cap finite-core theorem.** A separated-binary-block identity turns sufficiently large gaps into a forced popcount increase. For every fixed S, all trajectories remaining at most S ones lie in an explicit finite adaptive core. Thus bounded popcount is equivalent to eventual periodicity of an ordinary orbit. This is not yet convergence to 1: arbitrary caps can in principle contain nontrivial cycles.

**An order covering all eleven AYH rules under a precise value guard.** Complete cap-ten verification, plus the analytic outside-core theorem, proves that every odd source reaches 1 or exits ten ones within 79 odd events. The well-founded rank is `(q10(oddpart(value)), v2(value), H(word))`. Its schedule-independent literal rewrite budget is `H + 80(bitlength(value)-1) + 3239`. The guard stops at cap exit; this is not an unrestricted termination rank.

**A different order that does not cap intermediate digit counts.** A finite low-set-bit forest supplies descent from EVERY starting integer above 1 with at most eight ones, at ANY bit positions, within 552 shortcut steps. Its 618,416 disjoint residue cylinders also cover exactly the rational proportion recorded in `sparse.json`, approximately 90.59% of odd integers. Each macro repays the ORIGINAL numeric source, and `(source, remaining clock, H)` is a compatible augmented order for arbitrary admitted macro composition. Failure of the selector remains possible.

**A complete finite basin, not a cutoff sample.** There are exactly 151,320 positive odd sources that converge while never exceeding ten ones. The independent-implementation checker reconstructs this whole set by inverse BFS and compares it with direct forward replay. This does not say that every initial source with ten or fewer ones converges: it may exit the cap.

## Files and replay

- [Producer and guarded selector](../../experiments/ay-persistent-20261031/run.py)
- [Standalone reconstruction](../../experiments/ay-persistent-20261031/verify.py), which imports neither producer nor repository modules
- [Literal SRS, large-block and negative controls](../../experiments/ay-persistent-20261031/controls.py)
- [Complete-core summaries and hashes](../../reports/ay-persistent-20261031/core.json)
- [Sparse-forest summaries, density and hashes](../../reports/ay-persistent-20261031/sparse.json)
- [Controls](../../reports/ay-persistent-20261031/controls.json)
- [Execution receipt](../../reports/ay-persistent-20261031/receipt.json)
- [Scope and review](../../reports/ay-persistent-20261031/REVIEW.md)

Run from a checkout root using Python 3.10 or newer, with the standard library only:

```sh
python experiments/ay-persistent-20261031/run.py core --workers 4 --output /tmp/core.json
python experiments/ay-persistent-20261031/run.py sparse --output /tmp/sparse.json
python experiments/ay-persistent-20261031/verify.py core /tmp/core.json
python experiments/ay-persistent-20261031/verify.py sparse /tmp/sparse.json
python experiments/ay-persistent-20261031/controls.py
```

The core producer's `--workers 1` mode gives identical output. Repeat with `python -O`; validation uses explicit exceptions, not optimization-disabled assertions. Full source inventories regenerate deterministically rather than committing millions of rows. Sparse verification includes 72,618,522 physical shortcut steps plus two marked shadow-root steps, exact affine numerators, and exact cylinder disjointness.

## What remains

Neither cap exits nor FAILED_GUARD outcomes are convergence proofs. Arbitrarily increasing the cap can increase the rank, and a numeric descent from a sparse source may lead to a denser one. The missing global theorem is a source-persistent, paid bridge between these regimes, or a universal successful selector. This packet offers two explicit orders and an all-cap reduction, not that bridge. External mathematical priority and independent peer acceptance are not claimed.
