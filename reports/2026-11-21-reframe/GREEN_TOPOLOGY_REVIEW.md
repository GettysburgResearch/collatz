# Independent paper review: compact Green topology

**Verdict: VERIFIED at the stated paper-proof scope and frozen source below.**
This review accepts the dense residual Haar-null infinite-Green set and
the discontinuity corollary. It is not a Lean verification or a Collatz
closure verdict.

## Reviewed source and dependencies

- Source: `research/reframe-20261121/GREEN_TOPOLOGY.md`.
- SHA-256: `5e3242f7d6aaf4233e5313a34fa628b67b8461fb2c85de8504743c05baa79b57`.
- Reviewer: the global-mass agent, independently reconstructing the
  root-owned topology argument.
- Compact moment dependency: `GREEN_FRACTIONAL_MOMENTS.md`, SHA-256
  `b54169b4ee8f2530688984d9816872eebff88cc668a34710506bbc4ad7caaf6b`,
  specifically GF1 and the whole-word pressure expansion.
- Ordinary finiteness dependency: the first-hit/cycle Green estimate in
  `GLOBAL_MASS.md`, equation `(G10)`, with the credited PR169 scope.

The source was read in full and its SHA-256 recomputed locally before
writing this review. The mathematical reconstruction was also performed
before the root-owned note was finalized. No source edits were made by
this reviewer.

## Reconstruction and checks

**Legal prefixes and neighborhood control.** At every ternary unit, the
powers of two traverse all six units modulo nine. The guard
`2^a*zeta mod9 in {4,7}` therefore admits a positive exponent and returns
a unit inverse child. Iterating gives a legal word of arbitrary length.
Its forward affine image `E_w=R_w(X)` contains the original point and
has diameter at most `3^(-r)`. Thus the whole image, not merely one
representative, lies in any prescribed neighborhood at sufficient depth.

**Composition orientation and periodic legality.** Appending `L` exponent-one
letters gives `S_L=R_w o R_1^L`. The fixed-point identity permits inverse
letters to be removed in the order `w,1,...,1`, as required. Each suffix
image is a unit because every `R_a` maps all of `Z_3` into its units.
The fixed point is therefore in `E_w`, the entire inverse block is legal,
and its repeated concatenations are legal. There is no missing
intermediate-state hypothesis.

**Pressure and rational sign.** The real affine multiplier is
`J_L=3^(r+L)/2^(A+L)`, which exceeds one for sufficiently large `L`.
Repeating the block contributes `J_L^(2k)` to the pressure at depth
`k(r+L)`, proving infinite Green mass there. The affine correction is
strictly positive, so the fixed point has the displayed form
`C_L/(2^(A+L)-3^(r+L))<0`. Its denominator is a ternary unit. The source
correctly calls these negative rationals; it does not claim negative
integers or positive ordinary counterexamples.

**Continuity, category, and measure.** The coefficient sum over all words
at fixed depth `q` equals `3^q`, so the clopen word expansion converges
uniformly and the finite pressure is continuous. The increasing partial
Green sums make `G` lower semicontinuous. Each `{G>M}` is open and dense,
and their countable intersection is precisely `{G=infinity}`. Density
already follows from the constructed periodic points, and the Baire
argument is also valid on the compact unit space. A finite positive
fractional Haar moment from GF1 makes this infinite set Haar-null.

**Canonical discontinuity corollary.** Every finite-valued point has
infinite-valued points in every neighborhood, so the canonical extended
Green function is discontinuous there. Ordinary Green finiteness applies
to every positive odd ternary unit, including positive periodic targets.
The stated corollary therefore holds at every such ordinary integer.

## Scope retained

The topological and Haar conclusions concern the specified compact inverse
Green function. They do not exclude positive cycles, produce positive
escape, or supply the ordinary sampling limit `(F11)`. The source retains
these distinctions explicitly. No gap was found in the claimed topology
theorem or its discontinuity corollary at the frozen hash above.
