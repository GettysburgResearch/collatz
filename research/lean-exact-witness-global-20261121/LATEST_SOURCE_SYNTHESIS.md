# Latest source synthesis and the unbounded rewrite route

**Full Collatz and the original residue implication remain OPEN.** This pass
inspected the substantive changes on the current research branches, including
new commits on older PRs. It used those interfaces to construct the new
source-gap multiset program. This is a focused research synthesis, not a fresh
independent replay of every imported project.

## Frozen current sources

The paths below identify the mathematical sources of the summaries. The full
head pins delimit this inspection; later commits are outside its scope.

| PR | Frozen head | Substantive interface and remaining input |
|---|---|---|
| 173 | `fa0c9e2a2851e6324391e39c17afcb5913185aec` | `research/lean-shell-cover/ForwardSection.lean`, `SectionDynamics.lean`, `RisingReturns.lean`, and README section 6. Every positive orbit reaches an odd marked number near a power of two within an explicit clock bound. The marked set has density zero. Eventual descent under successive section returns is equivalent to Collatz; first returns can increase by every prescribed factor. Successive-return descent remains open. |
| 174 | `c92cd473de3b85ceb945702a726d2eb7350a6af8` | `research/psi-closure-20261121/README.md` and `routes/{cover,layers,pow3}/`. Adds an unbounded ordinary-walk descent-radius obstruction, exact source-certificate layer formulas, and powers-of-three families. No universal reverse-closure input is supplied. |
| 175 | `8ba80e8cf3d243850611b477cf149dfb3dab2c01` | `research/lean-global-closure-20261121/CollatzGlobalClosure/{EndpointSteering,SiblingRigidity}.lean`, `GLOBAL_ATTEMPTS.md`, and `FIXED_CLOCK_SYNTHESIS.md`. Exact arbitrary high-bit lifting and prescribed-endpoint rays; a ternary order lower bound for the specified equal-count parity-cell-preserving merger. The global rank searches do not supply a successful universal rank. |
| 176 | `ad9a0611d22b48c0fd0c1da31091179654ba31a9` | `research/lean-global-resolvent-20261121/{PRIMITIVE_SURVIVAL,FLUX_ATTEMPT,BROAD_RESET_AND_COVERAGE}.md` and `lean/Collatz/OddReset.lean`. Exact ordinary source-cylinder partition and primitive-source survivor mass, with an exponentially small higher-lift remainder; the primitive mass limit is open. An arbitrary-parent odd-state reset is proved for depth at least seven. Its path arithmetic is reused and strengthened here. |
| 178 | `cda78d92f404dd3219a7a4ed9322706654eddf29` | `research/lean-global-20261121/{COMMON_RANK,COVERAGE_ATTEMPT,MIXED_RETURN_ATTEMPT,GLOBAL_FORCING}.md`. A common rank for guarded source-witness transformations, a cofinal family outside those guards, and exact retraction of balanced inverse extensions. These restrict the specified selectors; they do not exclude asymmetric source-gap replacements. |
| 179 | `27a2c7414fdb92eeca57ad552a9ab5c36d8430d8` | `research/lean-descent-20261121/README.md` and `lean/Collatz/{HalfCrossing,BudgetTransfer,UnitBudget,TernaryLadder}.lean`. This head was unchanged. A first coefficient half-crossing with a bounded odd-step cost implies ordinary descent. Unequal-clock budget transfer and an unbounded inverse ladder are proved with explicit guards. The all-unit budget/coverage assertion remains open. |
| 180 | `f87cb69b3dd86257731ddfbab58c87bf3b5f63d6` | `research/lean-ordinary-closure-20261121/{GLOBAL_SEARCH_ROUTES,PURE_PSI_CHECKPOINT}.md` and `lean/Collatz/PsiParity.lean`. A uniform even-source two-way psi rule and an exact odd-source criterion supplement the incomplete comparison tables. Selected odd/even transports contain literal reciprocal loops, so their different successful ranks cannot simply be united. |
| 181 | `5f03d809b4495802971211ef13ff905f741d700d` | `research/lean-global-target-20261121/closure/{UNPAID_EXIT,RESET_BOUNDARY}.md`, `global/FLOOR_ATTEMPT.md`, and `lean/Closure/UnpaidExit.lean`. Actual expanding chains can exhaust their binary charge and take a contracting exit while retaining net expansion. The least bad floor does not supply the missing source absorption or five-energy estimate. A different certificate order remains available. |
| 182 | `cd3d4f3acad8b43ea07af764f28662f0eca7634e` | `research/lean-dyadic-descent-20261121/{README.md,OffsetDescent.lean}`. This new PR appeared during the publication refresh and is based on PR173. It gives the exact positive-quotient threshold for strict descent of `2^t*q+r`, a sound and complete finite evaluator, and sufficiently high dyadic lifts of each supplied convergent offset. It does not assert that the smaller endpoint is marked or provide all-marked descent. |

PR146 remained at `f431078244e868dc699fad011044f0d5e7f76437`, and main
remained at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The publication receipt
records the actual refresh and verification separately from these mathematical
summaries. No theorem from a newly inspected branch is silently added as an
axiom of the owned Lean project.

## Positive synthesis: one order for arbitrarily long replacements

The source-gap multiset order removes the fixed numerical energy base and
inserted-length cutoff from the earlier PR177 catalogues. It compares counts at
the highest changed grade. An initial even run of length `e>0` has grade
`2e+1`; an accelerated odd exponent `a` has grade `2a`. This distinction permits
an even run to pay for any finite number of odd exponents no larger than that
run. Every ordinary shortcut step before reaching one also decreases the same
order. See [the unbounded rewrite packet](UNBOUNDED_GAP_REWRITES.md).

This gives a concrete strengthening of PR176's reset. Its actual paths remain
valid at every natural loop depth `l`, including zero. The old depth-seven
condition was needed for ordinary-height decrease. For an initial even
valuation `e>=5`, the new source word

\[
(1,2,5)\mathbin\Vert1^l\mathbin\Vert(3,e)\mathbin\Vert\mathrm{tail}
\]

strictly decreases the graded multiset, even if its source is larger. The
entire supplied tail is preserved. In the associated valuation selector the
threshold drops from `v3(2P-1)>=11` to `>=4`, with the same normalized-unit
condition and the additional even-run guard.

The new `compiled_certificate_reset` then admits **arbitrary finite paired
entrance words** `W,V`. Their exact correction identity supplies all ordinary
intermediate guards. A checked source word

\[
W=(1,2,1,2,1,2,3,3)
\]

lowers the required initial even valuation to three. The target word may have
larger exponents; only the complete known-source certificate is ranked. There
is no bound on entrance length, loop depth, or inherited tail length. The
formal source is [UnboundedGapReset.lean](lean/Collatz/UnboundedGapReset.lean),
which attributes the reused arithmetic to the exact PR176 pin above.

These resets transform the pair `(known=P/2,wanted=P-1)` into
`(known=m,wanted=2m-1)`. They therefore belong in the generic comparison-pair
kernel, with their proved target implication and source rank decrease. They
are not implicitly converted into multiplication-only queries. A successful
rule covering every activated pair and every supplied certificate is still
the open global obligation.

## The sparse-section synthesis attempted

The new section theorem gives a forced forward visit on each ordinary orbit,
which is more than an inverse representative in a band. Combining it with the
current moment and population estimates did not supply the required loss:

- PR176's survivor mass charges each fixed original source by `n^-4`. Moving
  its endpoint to a sparse section does not remove that source atom. An actual
  absorption estimate remains necessary.
- The section count `O(N/log N)` is larger than the predecessor population
  lower bound on the scale `N^0.84`. Those two inequalities do not contradict
  a surviving component.
- A globally least bad integer need not itself be marked. Its forced marked
  endpoint can be larger, and its offset above a power of two need not lie
  below the original least bad integer. Conversely, the least bad marked
  integer does not give convergence of every smaller ordinary integer. A
  low-offset proof needs an actual smaller marked return or another common
  well-founded state rank.

The high-bit identity needed in that route was already available as PR175's
`EndpointSteering.orbit_shift` and `odds_shift`. It was identified for reuse
and attribution. The newly inspected PR182 gives the sharper usable interface:
when `3^p<2^t` and `q>0`, descent of `2^t*q+r` is equivalent to

\[
q\ge1+\left\lfloor
\frac{\max(T^t(r)-r,0)}{2^t-3^p}
\right\rfloor,
\qquad p=p_t(r).
\]

This retains the affine correction. Its theorem
`eventually_dyadic_descent` supplies a suitable clock for each fixed offset
already known to converge; the clock need not fit the exponent of a given
marked input. No result from PR182 is imported into the present source-gap
Lean kernel. The positive checkpoint pursues the unbounded source replacement
program above, retaining its precise coverage obligation.
