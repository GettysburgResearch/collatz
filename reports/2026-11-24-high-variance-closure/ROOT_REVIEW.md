# Review of the inverse-tree, measure and ordinary-transfer checkpoint

Base: PR182 at `f5e65dbad5eaf2a5f85cde8916e91fe6e5102e67`.
Scientific packet: `research/high-variance-closure-20261124/`.

## Outcome and review boundary

Collatz remains open. The work targets a rank or contraction retaining every
ordinary source, including a hypothetical least counterexample. No density
statement, formal diagnostic or conditional closing criterion is treated as
universal termination. This review covers the exact sources bound by
SOURCE_MANIFEST.json, not subsequent remote heads.

Three GPT-6.2 Astra lanes developed the rank, arithmetic and band arguments.
The coordinating agent independently reconstructed their central equations
and quantifiers. The arithmetic lane reviewed the diffuse interpolation and
finite-clock theorem; the rank lane reviewed the ordinary endpoint moment;
the band lane reviewed the antipode/IFS, sparse-reset construction and
quarter-shift minimax. These are model-assisted mathematical reviews, not
human referee acceptance.

## Reconstructed results

1. **Full envelope comparison — VERIFIED and kernel checked at its stated
   definition.** The root reconstructed the matched positive/negative
   affine identity, the extension past the negative root by its cycle,
   the source-31 tail inequality, the finite box and the target witness.
   The operational tree definition includes every defining inverse valley;
   conversely an odd negative rational reaching -5 below -1 can complete
   its current valley on the -5 cycle. This identification is written.
   Lean proves the strict comparison of the operational real suprema.
   Python exhausts the entire finite candidate sets above the selected
   thresholds and classifies every member by an actual terminating negative
   calculation. A budget overrun raises an exception. It is not a general
   negative-orbit membership oracle.
2. **Nonlinear repair — VERIFIED WITH SCOPE.** The exact pullback ratio is
   g times one plus a strictly positive term. The extra odd gcd factor has
   the favorable sign. This gives nonincreasing suprema, but strictness
   only if a maximizing target center exists. The explicit root-cycle
   family drives K_c to one without attainment on the full 1-basin. The
   general real inequality has its own Lean theorem; the supremum argument
   is written.
3. **Real/dyadic tower — VERIFIED, SOURCE-QUALIFIED where stated.** B_k is
   nondecreasing and its even-step product is explicit. Bounded-real
   agreement forces actual escape unconditionally. The converse uses the
   pinned injective-orbit count. The prescribed real antipode additionally
   uses the full correction sum below 17/50 and the external convergence
   floor. The product bound applies to the entire infinite injective set,
   so the strict limiting bound is justified. Both IFS images and the
   denominator/error estimates were reconstructed. The joint error lacks
   the power saving needed by the cited finite-place Subspace Theorem.
4. **Diffuse interpolation — VERIFIED as a written construction.** At each
   stage the spike attains its global maximum at the chosen ordinary
   point. Nondecreasing proper labels control the global previous maximum;
   finite isolation and a summable leakage budget control every previously
   processed point. The singular and Haar alternatives both have finite
   total mass. The ordinary debiting equivalence assumes termination only
   in its forward stopping-time construction. The finite optimization
   does not produce a horizon-uniform source bound. The residual infinite
   potential on the completion is consistent with ordinary finiteness.
5. **Sparse-reset realization — VERIFIED as a written all-ordinary
   construction.** The selector is a total finite algorithm. Its output
   satisfies x>=sqrt(n), making image membership decidable by n<=x^2.
   Compact irrational-rotation covering is used only at a fixed depth,
   where the actual correction is uniformly small at large inputs. This
   proves density zero for the image itself. The valuation-pair tail is
   (K+1)/2^K, and fixed finite physical preimages preserve density zero.
   The marked source containing the selected hit begins by the search
   horizon. Thus F is finite on all ordinary inputs, proper and computable,
   with the exact debit outside the marks. The actual reset 7->13 defeats
   an attempted unrestricted debit.
6. **Atomic transfer and quarter shift — VERIFIED as written, algebraic
   core kernel checked.** Ordinary inverse branches cover one full positive
   residue class per parity word; pulling back a supposed smaller positive
   endpoint proves the least-source/least-endpoint correspondence. The
   lift tail and average carry use the complete 2^k-word grid. The quarter
   identity supplies a parity-independent killing factor. Constant
   comparability preserves liminf and limsup root rates without asserting
   that a limit exists. The fixed-target minimax uses genuine long odd
   prefixes and even rays inside the same predecessor basin. The finite
   base below 20 is checked here. PR192's overlapping odd-clock reduction
   is explicitly credited.
7. **Tilted coupling — VERIFIED as a written obstruction to that estimate.**
   The two fresh parity bits are either equal or complements. Under one
   arm's tilt, mismatch jumps are biased, and the bounded stopped
   exponential process gives the finite-horizon lower bound. The large
   ordinary-grid condition excludes unequal-slope literal meetings. In
   the symmetrized law, the endpoint compensator exactly cancels the new
   mismatch killing. The ordinary cycle provides a second-moment lower
   bound, not a disproof of first-moment decay.
8. **Band clocks and boundary rays — VERIFIED as written with separated
   formal scope.** Both arms in the four-trit family are literal ordinary
   trajectories. Shared fair digit exposure is used only through its
   finite budget; dependence of the two arms is retained. The surplus is
   then continued deterministically. Gouillon's fixed two-logarithm bound
   excludes unequal-clock meetings after the stated height estimates.
   The boundary dichotomy, transfer equations and forbidden-gap family
   were independently reconstructed and kernel checked. Cantor geometry
   does not give a count of present-day boundaries. New opposite jumps
   can appear below a monochromatic cell; this blocks the proposed
   all-scale tripling propagation. The signed diagnostic coloring is
   explicitly not Collatz invariant. The twelve signed seed trajectories
   are exact finite checks.

## Corrections made during integration

- The compact-mass condition is `limsup eta_k([1,M]) > 0` for a fixed M,
  meaning mass bounded away from zero along a subsequence. Mere positivity
  at finite dates is insufficient. This quantifier was corrected before
  publication.
- The candidate rank's Python assertions were replaced by explicit guards,
  so optimized mode runs the same checks. No candidate remains unclassified.
- Broad Mathlib imports in the two band modules were narrowed and then
  freshly recompiled. Every public theorem is among the requested audits.
- The initial series/automaticity route was not imported as a new research
  result. The retained operator analysis acknowledges the newer PR192
  overlap at its full source SHA.
- The source-qualified high-floor input is not reported as a local replay.
  PR199's external M/R/N claims and PR200's draft Lean were read for intake
  only; this packet does not adopt their verification claims.

## Executed verification

`REPLAY.json` records the actual fresh compilation of five final modules,
24 complete named axiom inventories, the source and compiled-object hashes,
and all command outputs. Each module was copied into its own empty build
directory. The compiler was Lean 4.34.1 at
`5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`, using `-j1` and
`-DwarningAsError=true`. All passed. The allowed axiom set contains only
propext, Classical.choice and Quot.sound. No untrusted axiom or placeholder
was permitted by the audit.

Four exact control programs ran in normal and optimized Python with equal
outputs. They establish the three exact envelope values, 8191 parity-word
identities with three positive lifts per word, 16382 finite tilted adjacent
pairs, 520 forbidden-gap paths, 160 transfer pairs and twelve signed seeds.
Their bounded scope is separate from the written universal statements.

The measure construction, analytic transfer, minimax, real-address and
asymptotic arguments were not formalized in Lean. No whole-conjecture proof
was compiled.

## Publication evidence

SOURCE_MANIFEST.json binds the packet, this review and the scoped replay.
The complete-checkout default validator is run on the exact clean commit
before advancing the remote branch. Its receipt belongs in the PR body,
avoiding a self-referential commit receipt. The branch ref, PR head and
published sources are read back after the update. These are integrity and
publication checks, not mathematical proof.
