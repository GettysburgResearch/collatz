# Occupation, concentration, and arithmetic realization

Status: **PROPOSED**. This is exploratory research, not a Collatz proof or an externally reviewed result. No claim of literature priority is made.

## Publication repair

On 2026-10-30 the preceding chat reported a four-agent packet on `research/novel-swarm-20261030`, but explicitly did not confirm its push. Live branch search returned no matching branch, and the all-state PR query for that exact head returned `[]`. The current runtime contained none of the alleged packet files. Context retrieval recovered only summaries, not proofs, source bytes, commit IDs, or execution receipts.

Consequently this directory is a **new reconstruction and continuation**, not a byte-for-byte recovery. The previous counts (1,978 automata, 4,283 trees, 98 certificates), independence claims, finite-dimensional rigidity, automatic-component rigidity, and comparison-network claims are not adopted as evidence here. The old assertion of a weighted occupation theorem is replaced by an explicitly defined unweighted odd-time theorem below. Its numerical constant agrees, but equivalence to the missing old statement is not asserted.

Base: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; base tree: `1c25c17df24491de6187445f1a1d355d5a7660c3`.

## Mathematics

[OCCUPATION.md](OCCUPATION.md) gives a self-contained reconstruction of the singular-mass obstruction, including the singular point, invariance, the absolutely continuous component, a fixed-floor extension, and a sharp abstract countermodel.

For the odd accelerated map `U(n)=(3n+1)/2^a(n)`, every weak occupation limit of a positive orbit tending to infinity has singular mass at least `2-log_2(3)`, approximately 41.5%, relative to normalized Haar measure on the odd 2-adics. Stationarity and the valuation-mean bound alone cannot improve this constant.

The continuation examines quantitative cylinder concentration and the distinction between stationary local models and one fixed ordinary source. Any additional claim needs its own proof and reproducible evidence; none is accepted merely because it resembles the earlier chat summary.

## Execution scope

This initial publication contains proof text, not a computation receipt. Direct Git transport failed because the container could not resolve `github.com`; connector reads and writes are available. A full repository checkout/validator run has not been performed. This session has no callable multi-agent launcher; separate research tracks and computational workers must not be represented as independent AI reviewers.
