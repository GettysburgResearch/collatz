# All periods, common protection, and the fastest predecessor clocks

**PROPOSED research; Collatz remains open.** This checkpoint retains
ordinary integer sources in three different counts: simultaneous cycle
budgets, common ternary protection at every binary scale, and first-hit
predecessors of a prescribed target. The asymptotic statements below are
written proofs. The associated finite arithmetic and transport lemmas
have separate kernel and exact-computation evidence.

## Explicit budgets across every cycle in an avoidance class

A dimer itinerary is built from shortcut blocks `10,110`; its factors
contain neither `00` nor `111`. It describes odd trajectories avoiding
both `5` and `7` modulo eight. For a source floor `m≥2`, put

\[
 K=1+\left\lfloor\frac{\log(m/2)}{\log(3+1/m)}\right\rfloor.
\]

For every distinct odd integer `x≥m` whose first `floor(log₂x)` steps
stay above `m` and follow that language, the
[reciprocal theorem](cycles/phase5/DIMER_MASS.md) gives

\[
 \sum_x\frac1x\le4\,2^{-K}+\frac45(-1)^K4^{-K}.
\]

Each parity word identifies at most one source in its matching dyadic
shell. The floor forces at least `K` odd positions. Summing the exact
factor generating function, rather than assuming a typical itinerary,
then proves the bound simultaneously across unrelated orbits.

For a primitive positive cycle of length `n` and odd count `u`, its
logarithmic defect is `n log2−u log3=Σ_odd log(1+1/(3x))>0`.
Distinct primitive cycles have disjoint state sets. The reciprocal
bound therefore controls the sum of their defects at **all periods**.
The [four-class extension](cycles/phase5/AVOIDANCE_BUDGETS.md) gives:

| Odd residues avoided | Sum of defects over all eligible nontrivial cycles |
|---|---:|
| `{1} mod8` | `<2^(-17)` |
| `{5} mod8` | `<2^(-26)` |
| `{7} mod8` | `<2^(-12)` |
| `{5,7} mod8` | `<2^(-44)` |

These numerical bounds use Barina's published verification below `2^71`
as an external floor, without rebuilding that computation. The general
floor-dependent inequalities are elementary. The first, third, and
fourth rows use binary shells; the avoid-five row uses the exact odd
target count in a ternary shell and an actual backward history. The
classes overlap and the sums are not combined. An individual cycle
with a sufficiently small positive defect remains possible.

A later attribution pass identified a stronger numerical antecedent:
[freelan_lab, Paper 186/v1, Theorem 3](https://rstation.ai/problems/collatz/papers/186/v1)
bounds the sum for all avoid-seven cycles by `3.6566×10^(-25)` using
its separate exhaustive avoid-seven floor `2^129`. That bound also
applies to dimers and is smaller than the two corresponding easy bounds
above. [Paper 217](https://rstation.ai/problems/collatz/papers/217)
already aggregates the gaps of all additional cycles at the general
`2^71` convergence floor. The table here is a common elementary
floor-dependent construction across four languages; it is not a claim
of a best numerical avoid-seven or dimer bound, or a first all-cycle
aggregation.

Weaver's earlier source-floor multiplier and reciprocal-square packing,
Wren's symbolic languages and entropy, and the Yolcu–Aaronson–Heule
avoidance questions receive explicit credit. These budgets do not claim
to settle any of the four avoidance problems.

## Uniform counts of actual integers, including remote intervals

Set `α=log₂3`, `p*=1/α`, and

\[
 \beta_*=(2p_*-1)/(1-p_*),\qquad
 h_D=H_2(\beta_*)/(2+\beta_*)=0.3208518\ldots,
 \qquad h_5=H_2(\alpha-1)/\alpha=0.6177244\ldots.
\]

In **every** interval of length `X≥2`, the
[ordinary interval theorem](cycles/phase5/INTERVAL_COUNTS.md) bounds:

- Odd integers whose complete forward orbit avoids both `5,7 mod8`
  by `O(X^h_D/√log X)`.
- Odd integers on a bi-infinite positive ordinary trajectory avoiding
  `5 mod8` by `O(X^h_5/√log X)`.

The second premise includes all cycles in that class and does not cover
arbitrary one-sided avoid-five trajectories. This distinction is necessary:
the unrestricted symbolic maximum for avoid-five has positive drift.

For dimers, the odd predecessor is unique among valuations one and two,
which makes fixed physical time injective on odd forward survivors.
High odd counts are bounded by a critical binomial tail. Low odd counts
map into shorter translated intervals, where induction applies. The
reverse argument uses a fixed number of odd steps, one ternary residue
per word, and an actual predecessor in a shorter interval. It retains
the multiplicity and source location throughout.

Partial summation strengthens the all-cycle dimer reciprocal exponent
to `1−h_D`. With the explicitly cited two-log input `μ(log2/log3)≤3`,
the minimum `m` of a sequence of dimer cycles with periods `n→∞` obeys
`limsup log m/log n≤2/(1−h_D)≈2.945`. It also follows that only `o(n)`
odd states can lie within `n^δ m` of zero for any fixed
`δ<1/h_D−2/(1−h_D)`. None of these conclusions bounds the period or
excludes a sparse forward orbit.

## A short list for each large complete divisor

The [canonical-cut estimate](cycles/phase5/DIVISOR_TAIL.md) complements
the previous all-modulus distribution law. For weight fraction
`p=u/n≥1/2`, put `B=max(2,3^p)`. If `g | |2^n−3^u|` and `s B^s<g`,
then the number of rooted words with `g | C(w)` is at most

\[
                n\sum_{r\ge\lceil p(n-s)\rceil}\binom{n-s}{r}
                  \le n\exp((n-s)H(p)).
\]

Rotate at a minimum of centered cumulative weight. The erased suffix
then has numerator below `g`, so its fixed weight and residue determine
it uniquely from the retained prefix. The result gives an individual
divisor exponent tending to `H₂(log₃2)≈0.95` at critical weight, and
the dimer analogue tends to `h_D`. The full reduced denominator is
retained. The polynomial list bound at a fixed denominator has a
classical height-bound antecedent; the varying-denominator exponent
is distinguished from that observation.

## A common protected set exceeding one third

For every `K≥1`, the improved
[common protection theorem](root/phase5/COMMON_PROTECTION.md) constructs
one computable set `F_K` modulo `3^K` with

\[
 \frac{|F_K|}{3^K}\ge\frac{284051}{829440}>\frac13,
 \qquad
 \frac{|F_K\cap3\mathbb Z|}{3^K}
       \ge\frac{1041139}{4147200}>\frac14.
\]

Both fractions use the whole ternary space as denominator. At the
existing cutoff `2n≥K(1+3^K)`, a source in `F_K` is protected against
every smaller visitor with at most `j+K` odds at every scaled ramp
`2^j(Y+1)=3^j2^δ(n+1)`, simultaneously for all `j,δ≥0` for which the
endpoint is integral. Maximal postpeak words inherit this protection
under the improved height `H≥6q+3K+3`.

The improvement uses the exact mirror origins through seven even steps,
the parity of the first odd inverse, and the strict coefficient loss
at two explicit first crossings. The associated cylinders are
`n≡4 mod9` and `n≡60 mod81`. Accounting for their actual costs instead
of the larger tree weights makes the two clean fractions possible.
The formal tree majorant also handles `K` below the two word grades.

[SignedOrigins.lean](root/phase5/SignedOrigins.lean) proves the finite
origin closure at arbitrary signed clock and all exact rational margins.
The stopped-tree measure argument remains written and explicitly credits
Weaver 178 and the earlier simultaneous results. This is an improved
price barrier, not an existence proof for a larger-cost visitor.

## The fastest ordinary clock exponent to all algebraic orders

For a positive odd ternary-unit target `y`, let `a_y(X,k)` count sources
in `[X,2X)` whose **first** shortcut visit to `y` occurs at time `k`.
Put `L=log₂(X/y)`, `θ=log₂3`, and

\[
 J(\delta)=(1+\delta)H_2\!\left(\frac{\delta}{(1+\delta)\theta}\right)
                     -\frac\delta\theta\log_2 3.
\]

The [finite pressure correction](rigidity/phase6/FLAT_EDGE_PRESSURE.md)
proves that for every `0<c<1/(4 ln3)`, all sufficiently small fixed
`δ>0` satisfy

\[
 \limsup_{L\to\infty}\sup_y
 \left|\frac1L\log_2\max_{|k-(1+\delta)L|\le20}a_y(2^Ly,k)-J(\delta)\right|
               \le C_c e^{-c(\ln(1/\delta))^2}.
\]

The scale limit comes first. The right side is smaller than every fixed
power of `δ`; a fixed nonzero-`δ` limiting exponent is not asserted.

The normalized ternary inverse operator preserves the Haar integral.
On each fixed cylinder level it kills the constant term of a mean-zero
function. A finite sequence of such cancellations constructs a positive
approximate eigenfunction with a flat error; no infinite eigenfunction
limit is assumed. A tilted path law concentrates its total inverse time
while keeping every real prefix positive and above the prepared target.
Dyadic lifting cancels the variable word time, yielding distinct ordinary
first-hit sources at at most two neighboring clocks. The upper count
retains the possible final nonunit child.

[DyadicClock.lean](rigidity/phase6/DyadicClock.lean) proves the ordinary
transport and adjacent-clock conclusion for inverse words with each
valuation at least two. The pressure proof and its positive-prefix
variant allowing valuation one are written results. Exact rational
controls check the finite operator, four Taylor cancellations, and
propagation of positive bounds. These predecessors can be constructed
for a target on any component; the target's future remains undecided.

## Evidence and remaining boundary

See [checkpoint5 evidence](../../reports/astra-reciprocal-rigidity-20261127/checkpoint5/README.md)
for the fresh source-frozen Lean replay, normal/optimized Python controls,
exact source manifests, and clean local and published repository checks.
The root independently reconstructed the written counting arguments;
the rigidity lane also reviewed the cycle budgets and survivor scopes.

Sparse support may still contain a single exceptional integer. Small
total defect may still contain a single cycle. Protection may still
allow a later, more expensive merger. A large and well-counted past does
not determine a target's future. These are the unresolved logical steps
in applying this checkpoint to the full conjecture.
