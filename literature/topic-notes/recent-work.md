# Recent Collatz work: dated primary-source index

This note is deliberately not called a comprehensive survey.

## Almost-all theory

Tao proves that for every function tending to infinity, the minimum value attained by the Collatz orbit is below that function for almost all starting values in logarithmic density. This is a major almost-all theorem, not a proof for every orbit and not evidence for an explicit divergent orbit. [@Tao2022]

## Computation

Barina reports exhaustive verification for every positive start below `2^71` using high-performance computation. Finite verification does not address all integers. [@Barina2025]

Elsenhans reports experiments on individual random inputs with billions of decimal digits. Testing isolated huge numbers is categorically different from verifying all starts below a bound, so it is not used as a verification-limit citation in this suite.

## Algorithms and representations

Angeltveit's 2026 preprint gives an improved algorithmic framework for checking all `n<2^N`. It should be cited as a preprint and treated independently of peer-reviewed theorem status. [@Angeltveit2026]

Stérin and Woods give a refereed exact binary/ternary quasi-cellular-automaton representation and prove a base-conversion embedding. This is directly relevant to mixed-radix carry and rewriting work. [@SterinWoods2020]

## A 2025 version-discrepancy warning

The discovery metadata for Liu's *Counting the Collatz numbers* advertised a bound `π(x)≥x^0.946`. The current arXiv version 2 PDF instead states and proves only `π(x)≥x^0.3227`, explicitly retaining `0.84` as the historical record. The literature suite cites the current PDF, not the stale search abstract. [@Liu2025]

This is a concrete reason to record inspected version numbers and theorem text rather than trusting index snippets.

## Bibliographic navigation

Lagarias's surveys, edited volume, and annotated bibliography remain the most reliable historical entry points; current claims should still be checked against primary papers. [@Lagarias1985; @Lagarias2003Bibliography; @Lagarias2010]

No located source through the snapshot date establishes a proof or disproof of the standard Collatz conjecture.
