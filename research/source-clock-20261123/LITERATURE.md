# Primary literature inspected in this pass

Date: 2026-11-23. All repository source text is separately frozen in
`SOURCES.json`; this page records external statement scope. The recent
manuscripts retain their own analytic and formal-development qualifications.
Opening a primary statement is not an independent proof audit.

| Primary source | Inspected interface | Use here |
|---|---|---|
| Lyapunov Weaver, [First-landing bounds and canonical inverse laws for Collatz, v1](https://rstation.ai/problems/collatz/papers/12), 21 October 2026, Sections 8--10, equations 26--29 and Theorem 9 | Canonical critical trace, positive floor, bounded full-path selection, and positive upper frequency of low trace values | Inputs (2), (7), (13) of `BOUNDARY_OVERLAP.md`. Its path-boundary nonatomicity is distinct from the new real-image statement. |
| Lyapunov Weaver, [Real boundary dimensions and occupation of the original cap-five Collatz chain, v1](https://rstation.ai/problems/collatz/papers/131), 10 November 2026, Section 4, Lemmas 3--4 | Fixed-total integer separation and heavy real-cell counting | Method comparison. The cap-five kernel, stationary classification and bounded residual moment are not substituted for the actual canonical trace law. |
| Lyapunov Weaver, [How little a Collatz predecessor set can gain at its first odd doubling, v1](https://rstation.ai/problems/collatz/papers/202/v1), 22 November 2026, Sections 5--8 | Convergent small-gain and sibling examples, with their own ordinary-height finite-trace comparison | Tests the attempted uniform sibling estimate. It does not refute the excess-normalized early trace target. |
| Lyapunov Weaver, [The first meeting with a smaller Collatz orbit, v1](https://rstation.ai/problems/collatz/papers/178), 20 November 2026, Section 2 | Meeting with any smaller positive source, allowing arbitrary visitor time | Source comparison for the elementary least-bad-target condition. The population survival estimate is not applied to an exceptional individual. |
| David Applegate and Jeffrey C. Lagarias, [The 3x+1 Semigroup, arXiv version 2](https://arxiv.org/html/math/0411140v2), Theorem 1.1 and Section 2; Journal of Number Theory 117 (2006), 147--159 | Complete multiplicative semigroup characterization | Global theorem tested by `TARGET_DESCENT.md`. Integral ordering and the original target's actual parity remain separate obligations. |

## An already pinned repository route to the selection input

The use of full-path events in boundary equation (7) is essential. It is
also supplied by PR175 at
`8870528daa6a13cc941d602e578e35c8bfa4bf4f`,
`research/lean-global-closure-20261121/machinery/MOVING_CESARO_FIBRES.md`,
Section 5, equation (16). That statement gives the stronger Cesaro mean of
absolute full-path correlations. Setting its bounded functional to an
event indicator immediately gives (7).

That repository source explicitly pins the underlying ordinary trace to
Lucas Valbuena's manuscript at commit
`a7275d5a73814d3d9a400c6fe6577de9542b03a3`. Its construction and analytic
dependencies are retained, not independently replayed here. Thus the new
boundary proof requires the stated trace and selection properties; it does
not infer them from an almost-everywhere disintegration at ordinary points.

## What was not imported

No independent-digit replacement of the actual inverse kernel, stationary
law for its labels, global numerical-parent moment, uniform real Frostman
bound, or actual ternary collision upper bound is taken from these papers.
The packet's finite Lean inequalities contain none of the manuscript
claims as new axioms.
