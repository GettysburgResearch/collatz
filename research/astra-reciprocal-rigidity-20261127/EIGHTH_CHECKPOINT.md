# Full denominators, first smaller meetings, and the exact escape cost

**PROPOSED research. Collatz remains open.** This checkpoint reaches three
ordinary arithmetic questions directly: the least possible full reduced
denominator at a prescribed cycle period; the wait for any smaller source
to meet a long-ascent trajectory; and the positive defect required by an
escaping component. Each conclusion retains its exceptional set or
unknown quantity. The finite Lean consumers do not formalize all of the
asymptotic proofs.

## A denominator exponent for every word at almost every period

Let `d_min(n)` be the least full reduced denominator among all nonzero
rational shortcut cycles of **least** period `n`, of either sign. Put
`p=log₃2` and `h*=H₂(p)=0.9499555271…`. The
[ascent census](cycles/phase8/ASCENT_CENSUS.md) proves that for every fixed

\[
             0<\theta<\frac1{1+h_*}=0.5128322087\ldots,
\]

the set of periods satisfying `d_min(n)>n^θ` has natural density one.
The explicit rational exponent `θ=20/39=0.5128205128…` is allowed;
two exact integer comparisons certify the required entropy slack below
`19/20`. At each retained period this conclusion
holds for **every** primitive parity necklace and both signs, regardless
of how unusual its ordering is. The theorem uses neither the Subspace
Theorem, a quantitative irrationality measure, nor a large computational
verification floor.

Here is the mechanism, including the role of least period. Write the
cycle magnitudes as `y_i=a_i/d`, and their reciprocal values as `r_i`.
For cycles staying above a large fixed real floor `M`, use the rational
majorant `b_i=r_i/2` at odd inputs and zero at even inputs. Its sum
dominates the absolute logarithmic cycle gap
`g_C=|n_C ln2−u_C ln3|`. Add the telescoping correction

\[
                    Q_i=b_i+B(r_i-r_{i+1}).
\]

Future minima of the partial sums turn these signed corrections into
nonnegative periodic charges. Their total still dominates `g_C`. At
every positively charged phase, **every** subsequent partial sum of
`Q_i` is nonnegative. A discrete geometric-sum estimate gives

\[
 \frac{y_{i+j}}{y_i}\ge(1+1/(2B))^{-j},\qquad
 \frac{y_{i+j}}{y_i}\le\frac{(3+1/M)^q}{2^j}.
\]

The charged phase therefore has odd frequency at least `p_{M,B}` in
every prefix, with `p_{M,B}→p` as `M,B→∞`. At fixed denominator `d`,
look through `floor(log₂(dX))` parity bits for phases of real height at
most `X`. Each word has at most two numerator representatives. The
binomial tail counts `O_h((dX)^h)` charged phases for any fixed `h>h*`.
Since a charge is at most `(B+1/2)/y_i`, summing over height shells gives

\[
            \sum_{d_C=d,\ \min|C|\ge M}g_C=O_h(d^h).
\]

Cycles that dip below `M` need a different argument. A least period
`n∈[N,2N]` supplies `n` distinct integer numerators, so its largest
magnitude is at least `N/d`. Before that maximum, choose the last
crossing into `[M,2M]`. The following segment stays above `M` for at
least `floor(log₂d)` steps whenever `d≤N^{θ₀}`, for a suitable fixed
`θ₀>1/(1+h*)`. This follows from the true per-step growth factor
`c_M=(3+1/M)/2`, with `d^(1+log₂c_M)=o(N)`.
The witness consequently has at least `p_M(t−1)` odd bits in its
length-`t` prefix. There are only `O_h(d^h)` such witnesses at each
denominator, and distinct cycles cannot share a witness phase.

Combining the cases proves the multiplicity-sensitive estimate

\[
 \#\{C:N\le n_C\le2N,\ d_C\le D,\ g_C\ge b\}
                 \ll_h D^{1+h}(1+b^{-1}),
 \qquad h_*<h<1,\quad D\le N^{\theta_0},\quad b>0.
\]

Choose a slowly shrinking gap threshold. Cycles above it are too few
when `D=N^θ`, `θ(1+h)<1`. A period below it must satisfy
`||n log₃2||→0`; ordinary equidistribution makes those period values
a set of density zero. This last step counts periods, rather than
silently counting all cycles on a near-resonant period.

The [uniform signed census](cycles/phase8/DENOMINATOR_CENSUS.md) also
retains complete-denominator gap moments and growing-cutoff counts of
distinct period vectors. The [shrinking-floor proof](cycles/phase8/SHRINKING_FLOOR.md)
gives a complementary elementary symbolic escape estimate, uniform even
as the real floor approaches zero. Those earlier bounds are weaker than
the final unrestricted exponent but explain the change in strategy.
Paper 217 is credited for the future-minimum charging method; the
denominator-uniform charged-phase count and long-cycle crossing witness
are the consumers proved here.

An integer cycle has denominator one. The theorem would force its
period into the exceptional density-zero set; it does not prove that
this set contains no integer-cycle period. Rational positive cycles of
every least period at least two exist, so the statement has content
independently of whether an additional integer cycle exists.

## A sharp law for the first smaller-orbit meeting

Condition ordinary sources on their first `H` shortcut steps being odd.
Let `τ_H=0` if a smaller positive source has already reached the original
orbit through clock `H`; otherwise let `τ_H` be the subsequent original
clock of the first such meeting. Every visitor clock is allowed. The
[synchronization theorem](descent/postpeak/stopped/SYNCHRONIZATION.md)
proves absolute constants `c,C>0` with

\[
 \Pr(\tau_H>t)\le\frac C{\sqrt{t+1}}
       \quad(H\ge2,\ t\ge0),
 \qquad
 \Pr(\tau_H>t)\ge\frac c{\sqrt{t+1}}
       \quad(H\ge400,\ 6(t+1)\le H).
\]

The probabilities are relative natural densities on the actual dyadic
source cylinder. The lower bound allows all smaller sources. The upper
bound already follows from the single smaller source `m=(n−1)/2`.

Indeed, if `n=2^H v−1`, the two initial ramps end at
`x=3^H v−1` and `y=3^(H−1)v−1`, and `x=3y+2`. The adjacent pair
`2y,2y+1` maps to `y,x` in one step. The known counted-fusion tail for
adjacent two-adic sources is `O(t^(−1/2))`. The affine map in `v` has
odd slope, so its finite residue tests transfer exactly to the ordinary
source cylinder. Said Duran's pair chain and Leen's pair-tail estimate,
as restated in Weaver 124, are explicit external inputs. This checkpoint
does not claim the adjacent-pair result as new.

There is also an exact reduction for this prescribed visitor. For each
fixed `H,t`, the density that its **complete** orbit misses the original
trajectory through `H+t` equals the finite canonical counted-pair
survival probability, independently of `H`. Finite alternative visitor
clocks have different affine slopes except at the aligned clock. A
later visit after alignment would make the target periodic; ordinary
periodic states have zero density by the image-compression estimate.
The residual unaligned set tends to zero as the comparison deadline
increases. This order retains the original positive source throughout.

The lower bound uses the signed-offset classification. Among length-`t`
postwords there are at least `binom(t,floor(t/2))` maximal words. Each
protects more than one third of its cylinder in the stated range, even
against unbounded visitor clocks. Thus the fraction protected is at
least a constant times `2^(−t)binom(t,floor(t/2))`.

The same two-sided order holds in actual finite shells, simultaneously
for `400≤H≤(log₂X)/120` and `6(t+1)≤H`, among sources in `[X,2X)`
with the initial odd run. The proof charges the discrepancy relative to
each thin source cylinder. A fixed-height density limit is not substituted
for this uniform statement.

### The limiting law and a visible first-meeting atom

For a fixed maximal postword `w`, collect its signed-offset deficits
into the finite set `D_w`. The [stopped law](descent/postpeak/stopped/STOPPED_LAW.md)
gives an explicit ternary guard probability `p(D_w)` such that

\[
                         p_{H,w}=p(D_w)+O_w(2^{-H/2}).
\]

Stop every reverse competitor at its final required odd step. Short
signed stops must pass through `−1`; their earlier origins are exactly
the reflected first-hit origins of one. A single-origin injection counts
all remaining stops, producing a summable error. The pointwise
low-grade cone is retained as a separate hypothesis in this reduction.

The postwords `E` and `EO` have deficit sets `{0}` and `{0,1}`. Exact
fourth-odd stopping charges on the ternary ball `N≡60 mod81` prove

\[
                   p(\{0\})-p(\{0,1\})>0.01061084.
\]

Consequently, for all sufficiently large `H`, more than one percent of
the specified cylinder `O^H EO` has its **first** smaller-orbit meeting
at precisely original clock `H+2`. This is a location statement about
actual first meetings; it does not decide the visitor's eventual fate.

The [joint profile](descent/postpeak/stopped/PROFILE.md) uses independent
fair postbits and a Haar ternary coordinate. It approximates the full
postword and meeting position through `floor(H/6)−1` with exponentially
small total-variation error. Its limiting clock `τ` satisfies
`Pr(τ>t)≍(t+1)^(−1/2)`: it is finite almost surely, has infinite mean,
and has finite positive moments exactly for orders below one half.
The untruncated ordinary clock laws converge in total variation at
rate `O(H^(−1/2))`; the short-window truncated mean is `Θ(√H)`.

### Why fair-measure coverage still does not give pointwise coverage

The binary paths whose every finite prefix is maximal have fair measure
zero but full Hausdorff dimension one. With odd-bit probability `p>1/2`,
the maximal word in each offset fiber carries at least `(2p−1)/p` of
that fiber's mass. Nestedness and `p↓1/2` prove the dimension statement.
For nonrational two-adic sources this is exactly disjointness of the
complete orbit from every scaled companion
`3^(−δ)(x+1)−1`, `δ≥1`, even at unrelated clocks. In particular there
is a full-dimensional Haar-null set of disjoint adjacent two-adic pairs.

Every rational source is deliberately removed in that argument, including
every positive integer. It identifies an exception available to dyadic
parity information and does not construct an ordinary counterexample.

## An exact positive-defect cost for escaping components

Put `a(n)=1/2` at even inputs and `3/2` at odd inputs. For a total
computable rational function `0<u(n)≤1`, define

\[
 d_u(n)=\max\{0,\log(a(n)^2u(n)/u(Tn))\},\qquad
 D_u(X)=\sum_{n\le X}d_u(n).
\]

Let `c` be the number of escaping ordinary components, possibly infinite.
The [escape-flux identity](rigidity/phase9/ESCAPE_FLUX.md) proves

\[
 c=\min_u\liminf_{X\to\infty}\frac{D_u(X)}{2\log X}
  =\min_u\limsup_{X\to\infty}\frac{D_u(X)}{2\log X}.
\]

The candidate class can be restricted to `d_u(n)≤2 ln3`. The lower bound
telescopes along a simple escaping path up to its first height crossing.
The repository's finite simple-path reciprocal bound controls the
difference between true height growth and branch-slope growth. Each
disjoint escaping component costs `2 lnX−O(1)` before that crossing.

For the upper construction, mark first dyadic-height crossings of an
increasing finite seed list. A stopped maximal slope product gives
`u=B^(−2)`, whose defects occur only at marks. Finite threshold searches
terminate on either a crossing or a repeat. An escaping seed eventually
enters the list and therefore encounters marks at every later scale.

The [integer-budget refinement](rigidity/phase10/FIRST_CROSSING_BUDGET.md)
removes the need to hard-code unknown representative seeds. For a proposed
integer `r`, let `f_r(k)` be the largest `N≤k` for which seeds `1,…,N`
have at most `r` distinct first crossings of `2^k`. This is computable
and nondecreasing, and

\[
                        f_r(k)\longrightarrow\infty
                         \quad\Longleftrightarrow\quad c\le r.
\]

The stopped-envelope program is total precisely under this budget
condition. At the true finite value `r=c`, it has exactly `r` marks
per sufficiently high octave and satisfies `D_u(X)=2r lnX+O(1)`.
The program does not find the correct `r` or certify its own totality.

### Arbitrarily small weighted defects can lose positivity at the source

Delay the first marked octave to `K`, using a computably expanding seed
list. The resulting explicit positive functions `u_K` can satisfy

\[
           \sum_{n\ge1} n^{-s}d_{u_K}(n)\longrightarrow0
                   \qquad\text{for every fixed }s>0.
\]

They decrease pointwise to a function which is positive exactly at
bounded starts and zero at escaping starts. Thus this weighted smallness
does not provide the strict positivity at each original source that a
limiting escape certificate needs. The construction makes the lost
hypothesis visible at the same ordinary integer, rather than changing
the source as the deadline grows.

For comparison, the elementary horizon
`k(n)=max(0,floor(log₂n)−3)` and maximum slope through that horizon has
`Θ(X^{h*}/(logX)^(3/2))` violating sites per dyadic shell. The same order
attains the largest possible edge loss. Explicit increasing Mersenne
segments have unbounded accumulated signed defect while their odd
reciprocal sums tend to zero. The [prefix-maximum analysis](rigidity/phase9/PREFIX_MAXIMUM.md)
credits the existing meander statistics and explains why a uniform
reciprocal-budget repair fails for this concrete function.

A separate [total-defect characterization](rigidity/phase9/CYCLE_AND_ESCAPE_COST.md)
uses true height ratios and the summable charge `1+n^(−2)` outside
`{1,2}`. Its minimum is infinite if any trajectory escapes, equals the
sum of charges on all nontrivial periodic states if all trajectories are
bounded, and is zero exactly when Collatz holds. This exact reformulation
does not establish that its minimum is zero.

## Evidence and the remaining step

The root independently reconstructed the written arguments. The cycle,
descent and rigidity lanes cross-reviewed the new denominator, profile,
and defect proofs. [Checkpoint eight evidence](../../reports/astra-reciprocal-rigidity-20261127/checkpoint8/README.md)
records exact source hashes, fresh kernel replays, finite rational controls,
and clean-checkout validations. External pair synchronization, fluctuation
identities and the specified repository reciprocal estimate retain their
stated proof status.

No result here removes every exceptional rational period, proves a
smaller meeting for every fixed positive source, or forces the escape
cost to vanish. These are the remaining ordinary arithmetic obligations.
