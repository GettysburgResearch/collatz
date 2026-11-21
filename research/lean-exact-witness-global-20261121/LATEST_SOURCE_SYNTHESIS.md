# Latest source synthesis and the unbounded rewrite route

**Full Collatz and the original residue implication remain OPEN.** This pass
inspected the substantive changes on the current research branches, including
new commits on older PRs. It used those interfaces to construct the new
source-gap multiset program. This is a focused research synthesis, not a fresh
independent replay of every imported project.

## Frozen current sources

The paths below identify the mathematical sources of the summaries. The full
head pins delimit this inspection; later commits are outside its scope. The
second refresh below includes the newly created PR183 and PR184 and updated
PR175, PR176, PR178, PR180, and PR182, through the parent refresh at
**2026-11-21 15:44:50 UTC**. PR177 is this working branch, not an imported
source.

| PR | Frozen head | Substantive interface and remaining input |
|---|---|---|
| 173 | `fa0c9e2a2851e6324391e39c17afcb5913185aec` | `research/lean-shell-cover/ForwardSection.lean`, `SectionDynamics.lean`, `RisingReturns.lean`, and README section 6. Every positive orbit reaches an odd marked number near a power of two within an explicit clock bound. The marked set has density zero. Eventual descent under successive section returns is equivalent to Collatz; first returns can increase by every prescribed factor. Successive-return descent remains open. |
| 174 | `c92cd473de3b85ceb945702a726d2eb7350a6af8` | `research/psi-closure-20261121/README.md` and `routes/{cover,layers,pow3}/`. Adds an unbounded ordinary-walk descent-radius obstruction, exact source-certificate layer formulas, and powers-of-three families. No universal reverse-closure input is supplied. |
| 175 | `06215e69346c4d32bf970af9c846a6894586c1e7` | `research/lean-global-closure-20261121/CollatzGlobalClosure/{BandOffset,SectionResetReturns,BandCollision,SectionFeatureRanks}.lean`. Adds whole-cylinder descent transport, cofinal first returns increasing both height and `v2(n+1)`, and cofinal collisions excluding a strict first-return rank depending only on those two features. The arbitrary high-bit lifting and guarded merger interfaces remain available; no universal rank or coverage is supplied. |
| 176 | `3dbe5542fd6a5a1d63b354225d92391471c17002` | `research/lean-global-resolvent-20261121/section/{README,SECTION_TRANSPORT,UPPER_COUNT_ATTEMPT}.md` and `section/lean/{BandCriterion,CountCriterion,PopulationTransfer,SectionTransport}.lean`. Adds exponentially many actual marked ancestors with controlled clocks, a finite section-survivor count certifying a whole range, and a pooled same-clock population inequality. First-visit and return transport preserve original source mass; no constant dominates the transported mass by the endpoint fourth-power weight. The upper survivor estimate remains open. The earlier reset arithmetic is reused here at its separately named historical pin. |
| 178 | `a8a0736e2f8e98e363a37030327d884fe0d97ed6` | `research/band-return-20261121/` and its `BandBridge`, `ReturnFourier`, and `MarkFrequency` modules. Adds an unbounded explicit family with actual positive first-return descent. On each injective ordinary odd orbit, every nonzero leading-phase Fourier average vanishes and marked temporal frequency is zero. Neither conclusion controls the integer halving drift. Earlier guarded common-rank transforms and their coverage limitations remain unchanged. |
| 179 | `27a2c7414fdb92eeca57ad552a9ab5c36d8430d8` | `research/lean-descent-20261121/README.md` and `lean/Collatz/{HalfCrossing,BudgetTransfer,UnitBudget,TernaryLadder}.lean`. This head was unchanged. A first coefficient half-crossing with a bounded odd-step cost implies ordinary descent. Unequal-clock budget transfer and an unbounded inverse ladder are proved with explicit guards. The all-unit budget/coverage assertion remains open. |
| 180 | `9010a8790535002b6d9ff92304f0ba289e2e98fe` | `research/lean-forward-band-20261121/{MARKED_PREDECESSOR_POPULATIONS,DIVERGENT_ORBIT_PHASES}.md` and the `DenseBandFans` interface. A source-qualified analytic predecessor bound yields marked populations of order `2^d/(d+1)^2` in arbitrarily high, target-dependent octaves, with a common clock at most `15(d+1)`. The written analytic argument also gives summable reciprocal heights on a divergent orbit from that density premise. Those analytic inputs are not silently promoted to Lean theorems. The matching eventual survivor upper bound is open. |
| 181 | `5f03d809b4495802971211ef13ff905f741d700d` | `research/lean-global-target-20261121/closure/{UNPAID_EXIT,RESET_BOUNDARY}.md`, `global/FLOOR_ATTEMPT.md`, and `lean/Closure/UnpaidExit.lean`. Actual expanding chains can exhaust their binary charge and take a contracting exit while retaining net expansion. The least bad floor does not supply the missing source absorption or five-energy estimate. A different certificate order remains available. |
| 182 | `8372e302041a55057742a9e6ee9b4fa600c88fdb` | `research/lean-dyadic-descent-20261121/{OffsetDescent,MarkedOffsetReturn,InfiniteDescent,PhaseFrequency}.lean`. Adds actual lower marked returns for every prescribed contraction factor along selected dyadic lifts of a fixed certified offset; overlapping explicit windows cover `2^d+1` for `3<=d<=1603754`. It also derives leading-phase Fourier cancellation and a low-bit mean obstruction to escape. The required all-input choice of a successful lift or low-bit frequency law remains open. |
| 183 | `8659cf62ac685540cadeef320e596c852fbb0959` | `research/band-completion-20261121/lean/{BandDescent,BandRotation,BandMass}.lean` and `mass/RENEWAL_ATTEMPT.md`. A complete offset certificate fitting its binary window, with an explicit endpoint room guard, now gives an actual lower marked return. A sufficiently early marked return forces descent, but such an early return need not exist. The first-entrance fourth logarithmic moment of original source mass is finite; total surviving occupation across returns remains open. |
| 184 | `366dab89ee9548084ab9b5e4e90ff82abf287a20` | `research/lean-band-coupling-20261121/lean/{ClockSteering,OffsetHorizon,ReturnClock,RisingMerge,SourceBoundedMerge,LowerMarkedMerger}.lean` and `LATEST_CONNECTIONS.md`. Gives budgeted phase steering, exact merger formulas beyond the shared-bit horizon, explicit smaller ordinary partners for an entire rising family, and a lower marked partner from a sufficiently small ordinary merger. Its source-bounded and lower-marked merger criteria are equivalent to full Collatz; their universal coverage is not established. |

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

This gives a concrete strengthening of PR176's reset at the historical source
pin `ad9a0611d22b48c0fd0c1da31091179654ba31a9`, in
`research/lean-global-resolvent-20261121/lean/Collatz/OddReset.lean`.
Its actual paths remain
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
which attributes the reused arithmetic to that historical PR176 pin. Updating
the inspected PR176 head does not change this dependency.

These resets transform the pair `(known=P/2,wanted=P-1)` into
`(known=m,wanted=2m-1)`. They therefore belong in the generic comparison-pair
kernel, with their proved target implication and source rank decrease. They
are not implicitly converted into multiplication-only queries. A successful
rule covering every activated pair and every supplied certificate is still
the open global obligation.

## The first sparse-section synthesis

The new section theorem gives a forced forward visit on each ordinary orbit,
which is more than an inverse representative in a band. Combining it with the
current moment and population estimates did not supply the required loss:

- PR176's survivor mass charges each fixed original source by `n^-4`. Moving
  its endpoint to a sparse section does not remove that source atom. An actual
  absorption estimate remains necessary.
- The section count `O(N/log N)` is larger than the earlier predecessor
  population lower bound on the scale `N^0.84`. The second refresh strengthens
  the available marked population to `N/(log N)^2`, with the analytic
  qualification below; an upper bound on actual survivors is still needed.
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
marked input. The newer marked-return results below go beyond that initial
checkpoint. No result from these inspected section branches is imported into
the present source-gap Lean kernel.

## Second refresh: actual marked descent and ordinary mergers

The new positive bridge in PR183, `offset_certificate_return_descent`, is
stronger than ordinary descent alone. Let `n=2^d+u`, `u>0`, and suppose the
supplied ordinary certificate satisfies `T^k(u)=1` with `k<=d`. Put

\[
B=\left\lfloor\frac{2^d}{u}\right\rfloor+1.
\]

The lifted endpoint is at most `B`. If

\[
4\lfloor\sqrt B\rfloor+2\lfloor\log_2B\rfloor\le d,
\]

the bounded forward-section theorem produces a marked point strictly below
`n`, on its actual forward orbit. This is an input to marked-return induction
with every size and clock condition retained.

PR184's `lower_marked_from_small_merger` extends that height argument to any
positive ordinary merger partner `x`: from `T^a(x)=T^b(n)` and

\[
4\lfloor\sqrt x\rfloor+2\lfloor\log_2x\rfloor
  \le\lfloor\log_2n\rfloor,
\]

it constructs a marked `y<n` in the same ordinary component. The result need
not be a forward iterate of `n`, but the exact equality of later iterates
transfers convergence. Its `collatz_iff_marked_merger_descent` therefore permits
induction on marked integers using smaller marked component partners. An
alternative `SourceBoundedSectionMerge` retains the *original* ordinary
source in the bound `x<n`, even when its first marked visit is larger.

This is a productive change of direction for the previously rising family
`n_m=2^(4m)+2^(3m)-1`, `m>=2`. PR184 gives a smaller ordinary partner for
every member: `(2*n_m-1)/3` when `m` is odd, and `(3*n_m-1)/4` when `m` is
even, with explicit merger clocks. Thus its long rising prefix does not
prevent a component-based proof. These partners are not asserted to satisfy
the much stronger square-root room guard above.

PR182 also now proves `arbitrarily_strong_certified_offset_descents`: for each
fixed odd offset `r` with a supplied certificate, and each factor `C` and
height bound `N`, there are `d` and an actual marked return `y` such that

\[
n=2^d+r>N,\qquad C y<n.
\]

Both `n` and `y` are marked. The proof appends terminal `1,2,1` cycles and
uses arbitrarily large one-sided rational approximations to `log_2 3`.
It chooses the new exponent `d`; it does not produce a merger from every
previously prescribed `2^d+r` to one of those selected inputs. The exact
PR184 rebasing formulas show what such a transfer would require: an
alternative positive ordinary history to the shared endpoint with a strict
source-size saving. Replaying the original history gives equality, not that
saving.

## Second refresh: section populations and source mass

PR176's `marked_ancestors_with_clocks` constructs, at every admissible
Diophantine scale `Q`, at least `2^Q` distinct actual marked ancestors of each
unit `q<=2^Q`. Their heights lie in `[2^Q,2^(10Q))` and their clocks to `q`
lie in `[7Q-5,11Q)`. Admissible scales are proved cofinal. If `S_Q(t)` counts
marked starts below `2^(10Q)` not yet reaching one by clock `t`, then
`band_count_finite_certificate` proves that

\[
|S_Q(t)|<2^Q
\]

certifies convergence of the entire unit range `q<=2^Q`, with deadline
`max(1,t)`. `band_finite_survivor_population` retains multiplicities across
targets and proves the same-clock inequality

\[
2^Q|U_Q(t)|\le(4Q+5)|S_Q(t)|\qquad(t\ge1).
\]

This is a lower footprint of actual survivors; its required upper estimate
is not supplied by the section's ordinary counting bound.

PR180 supplies a stronger **source-qualified analytic** marked population:
for every positive ternary unit `q`, arbitrarily high target-dependent octaves
contain at least `gamma*2^d/(d+1)^2` distinct marked predecessors of `q`, at
one common clock at most `15(d+1)`. The analytic derivation invokes the
earlier logarithmic predecessor-density work and its mixing input; it is
not an unconditional theorem imported into this Lean project. PR184's
return-clock lower bound limits the number of high marked visits on any
such path to order `d/log d`. That bound counts visits on a path, not the
number of surviving sources. The upper estimate needed to contradict these
fans must hold eventually throughout the octaves, because a target's witness
octaves need not coincide with a separately favorable subsequence.

PR183 proves the useful finite first-entrance moment

\[
\sum_{n\ge1}n^{-4}
 \bigl(1+\lfloor\log_2 E(n)\rfloor\bigr)^4
 \le4096\sum_{n\ge1}n^{-2}<\infty,
\]

where `E(n)` is the first actual marked visit and the weight remains that of
the original source `n`. Its written renewal calculation also localizes the
old primitive survivor moment at the section with an explicit error tending
to zero. Neither result supplies a uniform return moment or absorption
across all subsequent returns. The Lean PR176 transport results prove exact
source-mass conservation and rule out domination by a fixed multiple of the
endpoint weight `m^-4`.

Finally, PR178 and PR182 prove vanishing nonzero leading-phase Fourier
averages on an injective escaping odd orbit; PR178 also proves zero temporal
frequency of the shrinking marked set. PR180's source-qualified reciprocal
summability gives a stronger asymptotic rotation statement. The low-bit
valuation mean needed to force height contraction is still a separate
arithmetic input: leading logarithmic phase discards the integer powers of
two. None of these phase results supplies `GapComparison.Complete` or the
universal smaller-component-partner cover.

The current constructive route therefore keeps its complete known-source
certificate, literal inherited tail, ordinary target implication, and one
well-founded multiset order. The newly published asymmetric and low-gap
rules enlarge its proved domain. A proof that every activated pair meets a
legal rule remains the global obligation; the new section results identify
additional sound interfaces for such a rule rather than discharge it.
