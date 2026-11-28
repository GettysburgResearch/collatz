# Checkpoint 04: sharp inverse clocks, moving sparse periods, and native phase tests

**The nine-hour pass continues; Collatz remains unresolved.** This is the
coordinator's reconstruction of the frozen fourth scientific snapshot.
The new results are written deductions with the external inputs specified
below. The local Lean replay checks exactly its declarations. It does not
formalize the analytic or Diophantine papers on which a written argument
depends. Phase-five experiments and every `.draft` file are excluded.

## Uniform actual inverse rows and the critical entropy question

The strongest new positive results concern genuine predecessors at a
supplied ordinary target, with both the odd depth and the physical clock
fixed. They retain the real affine correction. This is a stricter
interface than an average over ternary addresses.

| Claim | Review | Argument and scope |
|---|---|---|
| `machinery/phase4/LINEAR_DEVIATION_ROWS.md`: a Gaussian lower bound throughout a linear window | VERIFIED WITH SOURCE QUALIFICATIONS | Divide the depth into comparable central blocks. Vary each block total through a square-root window and count the zero-sum vectors by symmetric unimodality and Chebyshev. The resulting multiplicity cancels the unwanted product of square-root losses. Actual paths recover their block boundaries and totals, so all retained families are disjoint. The affine corrections form a geometrically bounded sum. Reserving a final central block retains an exponentially growing odd modulus. The imported input is the pinned central bounded-real row and this pass's mixed-modulus extension. |
| `SHARP_MODERATE_DEVIATIONS.md`: exact worst-target quadratic constant | VERIFIED WITH SOURCE QUALIFICATIONS | For each fixed central width B, the onset may change but one positive cylinder and one real cutoff can be kept. Read Wren 10/v3, Proposition 4.5 and Lemma 4.6, and Weaver–Wren 48/v2, equations (70)–(83), directly. The selected families do not depend on B; telescoping the limiting functions on one fixed cylinder then allows a later generation to handle any fixed B. Compose about t²/B² blocks, keep the precise square-root prefactor, and take B to infinity after the moderate-deviation limit. Averaging all compositions over unit target residues gives the matching upper bound. The minimax normalized logarithm is exactly −1/4. The upper bound concerns a worst target, not every specified target. |
| `STOPPING_TIME_TAIL_RIGIDITY.md`: one power-saving slow tail is a global theorem | VERIFIED WITH SOURCE QUALIFICATIONS | A nonterminating ordinary root supplies central predecessor rows that contradict any power saving. A terminating root with excessive delay supplies the same contradiction quantitatively after choosing the largest admissible row depth. This turns one bound for the full exceptional population into uniform logarithmic stopping and, with Inselmann's power-dense precritical law, into every tail bound above the central coefficient. The terminating-basin-only version gives a uniform bound only on finite stopping times. At or below the central coefficient, one fixed off-cycle seed already prevents a power saving. |
| `SLOW_TERMINATING_SPECTRUM.md` and the final section of `SHARP_MODERATE_DEVIATIONS.md` | VERIFIED WITH SOURCE QUALIFICATIONS | The row amplification gives a lower spectrum in terms of the extremal finite-delay coefficient. The sharp row curvature yields a quadratic lower bound on the slow terminating population close to the central coefficient. For every octave, choose the odd depth first and the exact total second; sources just below the octave are doubled. Odd parts distinguish the doubled sources. No sharp upper spectrum is claimed. |
| `TILTED_ENTROPY_TRANSFER.md`: full entropy rate at the worst ordinary target | VERIFIED WITH SOURCE QUALIFICATIONS | An absolutely continuous tilted law is equivalent to unit Haar through the positive inverse kernel. The coding posterior has information rate equal to geometric entropy minus log 3, since the endpoint density terms divided by depth tend to zero in probability. A finite collection of good stored words becomes a stationary state-action occupation flow. Fresh unused trits give the exact finite transition kernel; conditioning on the fuller history establishes the entropy inequality. Mix flows before dividing by state mass. The positive finite-policy theorem then supplies an all-source law of large numbers. A cheap reserved portion corrects the total exactly; increasing the last exponent by a multiple of six preserves the terminal unit class and improves the real offset. One fixed initial exponent makes the final correction at most one. The entropy rate is uniform over actual targets, including moving targets. |
| `EXTENDED_TILTED_INTERVAL.md`: exact extension of the scalar regularity certificate | VERIFIED WITH SOURCE QUALIFICATIONS AND AN EXACT INTEGER CERTIFICATE | Read the recovered primary Leen v1 TeX, Theorem B, the entropy-envelope lemma and all of Section 3 including Theorem 3.7. Its general scalar criterion applies on both sides of 1/2. The independent program proves it throughout [0.21, 0.5] using 2,900 rational parameter cells and 8,211 left Riemann rectangles. All logarithm, square-root, endpoint and integral comparisons round in the required direction. The smallest certified gap exceeds 1/10,000. Together with the author's [0.5, 0.550024] interval this supplies the entire stated range. The private formal development described by Leen is not part of our replay. |
| Same note: optimized counting dimension of any ordinary escaping grade | VERIFIED WITH SOURCE QUALIFICATIONS | Apply the supplied-target entropy theorem at the least vertex of a later grade, along a subsequence attaining the least-height growth rate. Optimize the geometric entropy over its mean clock using the relative-entropy variational identity. The optimizer lies between 1/3 and 1/2, inside the newly certified interval. The resulting unique exponent s solves `(2^s−1) 3^(1−s) exp(gamma*s)=1`. Its universal lower endpoint is log₂(3/2), improving the central-row endpoint log₂(4/3). This is a lower counting/box bound, not the strict upper bound that would exclude an escaping grade. |

The scalar computation is independently reproducible without floating
point. Its input manuscript has SHA-256
`3855fc67c0c30c0e8e78af3de93fd85279d4376f2cb7c1e5d63d24433ce70afc`
for the v1 TeX. The theorem remains source-qualified: a correct new
interval calculation is not a new verification of all the source's
analytic machinery. The source and access URL are recorded in the note.

### The optimal inverse slope now has an exact reverse-entropy formulation

`CRITICAL_REVERSE_ENTROPY.md` retains the unresolved endpoint rather than
claiming it from the known forward entropy dimension. Weaver 150, §7,
already asks for sublinear reverse entropy; the new scope is its
quantitative equivalence to the optimal cost and uniform cell floor.
Write L for the
Haar optimal mean inverse cost, a* for the critical geometric mean, and
D⁻ₙ for relative entropy with **Haar as the first argument**. The review
reconstructs the bounds

\[
 I_*(L)\le \liminf D^-_n/n\le\limsup D^-_n/n
       \le -\log(1-\theta_*)\,(L-a_*).
\]

The finite-window theorem and positive-policy perturbations first show
that the worst supplied target's minimum cost divided by depth tends to
L. The two initial-trit conditional means differ by only a bounded
amount, giving convergence in Haar probability as well. A block schedule
then constructs a legal infinite route of mean L from **every** supplied
unit, without claiming that L is the cheapest rate at exceptional points.

At criticality a word of cost S has weighted mass exactly exponential in
`−(S−a*n)`. Keeping a minimum-cost word proves the upper reverse-entropy
bound uniformly on every cell. Conversely, Haar-typical cells have cost
at least any fixed value below L. Their critical-law mass is bounded by
the geometric upper-tail probability. A Markov bound and the uniformly
bounded negative entropy contribution give the lower bound. Therefore
the optimal slope equals the entropy ceiling exactly when reverse
entropy is sublinear; equivalently, every unit cell has a uniform
subexponential density floor. The already known entropy in the opposite
direction does not supply that floor.

Two exact controls defeat proposed shortcuts to that endpoint.

- Changing a single low ternary digit from the address −1 to −7 changes
  the minimum cost by a linear amount. The negative inverse paths from
  −7 cannot reach −1 and have absolute vertices at least five; the
  elementary ratio is at least 14/5. Positive representatives of those
  finite cells have the same finite costs. This rules out a uniform
  bounded-difference premise, while leaving rare-influence concentration
  open.
- A unit-address set of Haar measure comparable to exp(−sqrt(n)) can be
  inaccessible from almost every root at every sublinear cost. Take one
  short real interval of standard ternary representatives. For a fixed
  inverse length and total, every endpoint has the same initial real
  phase up to an exponentially small correction. A union over the
  polynomial number of clock pairs still misses that interval almost
  surely. Thus entropy size alone cannot justify universal cheap
  routing. The actual Collatz cheap-address set needs a separate
  dispersion argument.

## Full rational denominators with moving coefficients and templates

| Claim | Review | Argument and scope |
|---|---|---|
| `cycles/phase4/MOVING_RESIDUES.md`: small-height rational residues | VERIFIED WITH SOURCE QUALIFICATIONS | Apply Grieve–Wang to `Z−1` and `W−r` with the actual full clock monomial and moving rational representative. An exponentially large common divisor excludes the small-gcd alternative. A fixed small-height character, explicit in the proof of Theorem 3.1, becomes an exact equality because both sides have subexponential height and agree modulo an exponential modulus. The representative is a two-three unit. Its remaining exponent lies in the reduced period direction, with the exact order modulo the chosen divisor. At the full determinant that order is the clock gcd; it can be smaller on a principal subfactor. |
| Same note: proper arcs between small actual endpoints | VERIFIED WITH SOURCE QUALIFICATIONS | Remove the endpoints' common gcd before applying the moving-residue result, retaining all common prime powers. The reduced endpoints are units modulo the remaining divisor. The forced rational ratio is dyadic because all physical cycle numerators are three-units. Distinct phases of one primitive cycle with the same odd core lie on one even-halving chain; a proper arc containing some but not all odd departures cannot join them. Consequently the proper numerator has only subexponential gcd with the full determinant. On an ordinary cycle the two complementary numerators themselves have subexponential gcd and a reduced ratio of the stated exponential height. |
| `MOVING_SPARSE_SUMS.md`: sharp sparse denominator rate and rational quantization | VERIFIED WITH SOURCE QUALIFICATIONS | Quotient the finite lattice of limiting exponent vectors by its zero-limit relations, retaining every finite-input discrepancy in a coefficient of sublinear height. A fixed root factorization has equally large outside-six valuation mass on every component; this follows from the total determinant mass and the height upper bound on each component. Active components have only sublinear gcd with the moving sparse polynomial by Grieve–Wang. Inactive factors divide it exactly. The placewise positive-part inequality handles shared primes. A finite Fourier uncertainty inequality leaves at least a 1/r fraction active under positivity, separated dyadic dates, or the stated stable real evaluation. Galois stability forces the denominator of the limiting rate to divide the clock gcd. |
| Same note: positive sums and large least prime of the clock gcd | VERIFIED | This stronger conclusion uses positivity. Normalize a root to beta with beta^d=zeta/R. Because the relevant conductor has no primes two or three, the constant-term valuations of any monic factor force the full degree d. Group by its power basis. Every surviving coefficient is a positive rational sum of fewer roots of unity than the least prime in their order; induction through the cyclotomic extensions excludes its vanishing. All components are active. For two terms, the odd-order phase already excludes a negative rational ratio. The signed two-term counterexample shows why this improvement cannot be attached to separated dates alone. |
| `MOVING_POWERED_WORDS.md`: any fixed number of moving powered templates | VERIFIED WITH SOURCE QUALIFICATIONS | Discard macroscopically negligible pieces into the connectors and center each surviving affine block at its own fixed point. The exact telescoping identity produces at most r small-height, possibly signed boundary jumps. Macroscopic separation of their dyadic dates survives the sublinear valuation corrections. They cannot all vanish in a primitive long cycle, because then a single short template already returns to the starting state. Compare the complete rational denominator in both directions, including coefficient denominators outside two and three. The sparse theorem gives rate at least 1/r and the same quantization. No estimate uniform in growing r is claimed. |

Precedence is retained. PR212 at `505d3fe782922904e86477990cc5d41e9110edda`
already has the fixed-coefficient sparse rate, fixed-dictionary powered
words, and the two-moving-template case. The present formulation permits
arbitrary rational coefficients of sublinear height and any fixed number
of simultaneously moving templates and connectors. It does not exclude
arbitrary complex period words. The positive large-prime improvement
received a separate independent reconstruction by the escape agent.

The new finite controls include 1,398 positive three-template displays,
1,382 primitive displays, 1,376 signed jump cases and 151 comparisons
where the physical denominator differs from the sparse auxiliary one.
A primitive (26,16) word cancels the whole nonprincipal factor 14,753,
leaving denominator 1,631. This rejects a blanket nonprincipal
noncancellation assertion; it is not an asymptotic test.

## Observable phase laws through the whole native critical window

The fixed-shell observable now has a finite monotone version. Average the
endpoint law at physical dates t and t+3, separately on the actual
integer intervals [X,21X/20] and [5X,21X/4]. The total-variation distance
decreases at every finite date. The exact correction-cone argument bounds
each literal escaping fraction by this distance. If every tested start
terminates at one, the distance becomes exactly zero after a finite date;
an observed zero certifies boundedness of every tested start under the
cited high-simple-segment bound and verification floor.

The stronger reason is a finite whitelist. Every common nonperiodic
endpoint lies in the union W of the forward orbits through the fixed
verified floor. Otherwise both prefixes are simple and high, whereas the
four date-pair ratios force at least one correction to be at least 4/3.
The imported correction bound is strictly smaller. The all-clock atom
bound makes the entire transient overlap O(|W|/sqrt(log X)), uniformly
in the date. On actual cycles, the pinned native periodic-phase law gives
the same Gaussian captured mass on both shells. Compactness of the
extended normalized-clock line upgrades the sequential statement to a
uniform statement over all t. This is the full critical profile in
`escape/phase4/FINITE_SHELL_DETECTOR.md`.

`HARMONIC_SOURCE_PHASE.md` reduces the source side to one interval and one
date. Sample X<n≤3X with exact weights 1/n and inspect

\[
 \{\log_3(2^t T^t(n)/n)\}.
\]

Every nonperiodic endpoint outside W has phase in a common quarter arc,
by the exact correction identity. The periodic restriction becomes
circular Haar: proportional-interval counts give independence from the
logarithmic source coordinate, harmonic weighting makes that coordinate
uniform over one full turn, and moving rotations are handled by a
subsequence argument. Therefore the quarter-arc probability has the
stated explicit Gaussian transition, with escaping density retained in
its limit. Integer fourth powers test the event without logarithms or
odd-count reconstruction. A single Fourier coefficient also detects the
uncaptured mass with explicit positive lower and upper bounds. The
machinery agent independently reconstructed this proof. No theorem
forcing cancellation of that coefficient is asserted.

The pair process in `AFFINE_PAIR_RETURNS.md` is a separate genuine dyadic
result. Exposing one fresh bit at a time makes the odd-grade difference a
fair lazy walk. Its embedded jump chain is simple symmetric random walk;
holding times have the explicit valuation bound. A fractional-moment
contraction controls the normalized offset at recurrent zero levels.
Occupation and second moments give a uniformly positive chance of a
bounded-offset return from any history, and martingale convergence
upgrades this to infinitely many returns almost surely. For slopes one
and five, the finite variance, fourth moment and occupation estimates
are uniform. These do not assert infinite recurrence at an ordinary
integer.

`ORDINARY_PAIR_RECURRENCE_BARRIER.md` shows that the latter transfer is
actually false in general, even on terminating pairs. Among sufficiently
many powers-of-five starts, positive basin density forces a pair with
positive upper density of simultaneous termination. Symbolic fusion of
w and 9w shifts their accumulated grade by two. Once on the two-cycle,
the grade difference of another pair takes at most two consecutive
values, so one of two fixed nonresonant pairs eventually avoids grade
zero. The finite union argument requires only upper density. This
distinguishes one finite return beyond each fixed date from infinitely
many returns at the same ordinary parameter.

## Exact matrix membership and the formal boundary

`phase4/AFFINE_MEMBERSHIP.md` gives a complete elementary decoder for a
specified rational affine Collatz word. The reduced slope supplies the
word length through its denominator power of two. Offset parity gives
the first chronological branch, and the recurrence removes that branch.
A final exact coefficient check rejects malformed data. The decoder is
complete, sound, injective and polynomial in the rational input bit
length. This articulates the classical parity coding; no originality is
claimed for freeness. Vector reachability still quantifies over an
unbounded word, which the decoder does not decide.

The note also checks the direct interface of a 2024 flat-rational matrix
decision theorem. A finite union of flat products over GL₂(Z) has only
finitely many absolute determinants. The Collatz monoid has all
determinants 2^(-t), so it is not such a set in that representation. This
does not exclude other encodings. The primary Dhiman–Pandey reachability
nondefinability argument is reconstructed, including its generalized
q+d=2^s family, and its false explanatory aside about fixed constant
multiplication in base two is identified without attributing that error
to the main proof.

The four added Lean modules have deliberately narrower scopes:

- `AffineWordDecoder`: exact decoding, completeness, soundness and
  uniqueness of the cleared affine word code.
- `PositiveLift`: the physical numerator is the exact least value over
  aligned nonnegative representatives in the full formal period lattice.
- `SimpleArc`: the actual numerator recurrence forces every available
  halving; simple complementary mixed arcs cannot have a dyadic endpoint
  ratio.
- `PrefixOrbitWhitelist`: for a supplied orbit composition law, a repeat
  makes the endpoint periodic; a prefix classified as large by an
  explicit high-simple bound ends on a cycle or in the supplied low
  future whitelist. The four-lag numerical correction argument remains
  written mathematics. One may include zero in the auxiliary whitelist;
  this changes nothing for positive ordinary endpoints.

The complete fresh replay and all-declaration axiom audit are in
`CHECKPOINT_04_LEAN.json`. Five independent finite programs run normally
and with Python optimization; each pair has identical output in
`CHECKPOINT_04_CONTROLS.json`. The scientific source manifest fixes the
exact snapshot. Clean-checkout structural and regression receipts and
the exact published commit are retained separately. None of these
checks is a proof of the full Collatz conjecture.
