# Fourth checkpoint: independent mathematical review

**Scope and verdict.** Collatz remains open. The root reconstructed the statements below from their definitions, inspected the entire new Lean and control sources, and ran the recorded checks. VERIFIED here means the indicated finite statement or written implication, with the dependencies and limits stated in its row. It does not promote the complete research programme to a proof.

The parent of this packet is PR201 at
093e75d9fc31294b42519339be3b601ad7e37d42. Exact integrated source hashes are in
[FOURTH_CHECKPOINT_MANIFEST.json](FOURTH_CHECKPOINT_MANIFEST.json).
The [fourth checkpoint](../../research/six-hour-20261127/FOURTH_CHECKPOINT.md)
is the scientific entry point.

## 1. Located CRT period exclusion and the separate minimum census

**VERIFIED as written finite mathematics plus exact replay; partial formal kernels.**

The hypotheses are an ordinary positive primitive odd cycle, exact valuations
one or two, and maximum at most \((16s+7)/3\), where \(s\) is its minimum.
The previous complete finite screen leaves 25 possible reduced clock pairs
for \(s\ge2^{71}\), \(p\le10^{1000}\). These are necessary pairs, not constructed
cycles. The root had independently reconstructed that screen, including its
directed logarithms, Farey coverage, integer dyadic order, and rank distortion.

For the new intersection, the root derived the two source residues directly.
Reading a past backwards gives
\[
 a_-=\sum_{j=1}^k3^{j-1}2^{-E_j}\pmod {3^k}.
\]
The carry recurrence is \(C_j=2^{e_j}C_{j-1}+3^{j-1}\).
For the future, the complete affine numerator and the odd terminal bit give
\[
 a_+=2^A-\sum_{j=1}^f2^{E_{j-1}}3^{-j}\pmod {2^{A+1}}.
\]
The factor \(3^{-f}\) on the initial \(2^A\) reduces to the same \(2^A\)
modulo \(2^{A+1}\). Both moduli are fixed throughout a histogram pass for a
specified final future grade.

The additive CRT address is the sum of the two separately inverted residues,
on the circle with physical circumference \(3^k2^{A+1}\). For each word,
downward rounding of each angular increment costs less than one bin. The
combined error is less than \(k+f\) bins; the future constant contributes a
common half-turn. It is legitimate to suppress that half-turn only because
the final interval estimate is uniform in its unknown location.

The root independently expanded the centered covariance. For histograms of
length \(M\), with totals \(n,m\), it gives the exact peak cap
\[
 \left\lfloor\frac{nm+\sqrt{(M\sum H_i^2-n^2)
                                    (M\sum K_i^2-m^2)}}M\right\rfloor.
\]
Replacing the square root by its integer floor before the division leaves
this floor unchanged. Multiplying by
\(\lfloor MW/(PQ)\rfloor+k+f+2\) bounds an arbitrary physical interval of
width \(W\). This also covers multiple full turns: lift the circular bins to
the real line, and charge each actual source to one lifted integer slot.
Duplicate word pairs would overcount, which is safe for this upper bound.
No independence or distribution assumption is used.

The root checked the directions in both height estimates. An upper bound on
\(\epsilon=h/p-\log_2 3\) gives the lower height bound via
\(\epsilon>1/(16s+8)\). A lower bound on \(\epsilon\), together with the
previous rank-averaged estimate \(s\epsilon<7/20\), gives the upper height
bound. The three physical bands cover every normalized rank point exactly
where needed; retaining an extra band only weakens the exclusion.

The checker imports the frozen directed logarithm routine and all 25 pairs.
Its 78 literal short word pairs use independent affine recurrences and
explicit CRT search. The bucket equality, angular rounding, wraps and
interval caps were all reconstructed and then replayed. Every production
upper population is strictly below its compulsory rank population.

The independent minimum census supplies the missing small-height range,
without using a general trajectory verification. At an actual minimum,
the reverse homogeneous ratio is the true predecessor ratio multiplied by
the positive correction product. The future homogeneous ratio is the true
successor ratio divided by that product. This gives exactly the relaxed
prefix inequalities used in the two 30-edge enumerations.

For \(P=3^{30}\), \(Q=2^{A+1}\), write a candidate minimum as \(b+Qt\).
Multiplication by \(Q^{-1}\) modulo \(P\) turns the physical interval into
two disjoint sorted runs. The bound \(PQ>2^{71}-1\) guarantees only the first
CRT period is needed. Binary searches include both endpoints correctly;
the subsequent lower-height check discards the unwanted initial segment.
All arithmetic is integral. The 2,510,811 past words and the two future-grade
lists lead to 555,231 and 136,825 actual candidates, respectively.

Every retained candidate is then followed as an ordinary integer and exits
the strip or uses a valuation above two. The latest exits are at odd steps
53 and 52. All 524,287 smaller odd minima from 3 through \(2^{20}-1\) also
fail, by step 24. A separate source-by-source scan through 32,767 matches
the complete short CRT census. At minimum one the actual odd map is fixed
at one, so no other primitive cycle can have that minimum.

Together these statements imply \(p>10^{1000}\) on the restricted branch.
The earlier CRT paper correctly labels Barina as an external optional input
for its own statement; the new minimum census removes that dependency from
the combined result. No result excludes the remaining periods or the other
least-disagreement alternative.

Lean checks the CRT address, word-rounding bound, centered covariance,
two-run arithmetic and finite trapping implication. It does not formalize
the entire rank theorem, period enumeration or Python algorithm.

## 2. Monotone completions and the bounded-corrector obstruction

**VERIFIED written construction and finite controls; three formal order lemmas.**

Normalize each odd grid site \(x\in[B,U]\) to \(m=2^jx\in[4B,8B)\).
Its valuation factor \(c\) is one of 1, 2, 4, and the unrounded image is
\(3m+c\). For distinct consecutive integer positions the factor change is
at most three, which proves monotonicity. At the octave seam the next
image is larger too. Rounding down or up on the entire dyadic extension
therefore gives a monotone lift commuting with doubling.

The root checked the periodic-slope argument by taking a common multiple
of two periods and comparing two representatives within one octave.
Monotonicity bounds their displacement difference by less than one octave,
so their integer octave gains agree. A physical cycle follows both
completions with exactly the same clock ratio. A strict gap between the
two rotations therefore excludes such a cycle.

The controls independently compare the edge routine against sorted adjacent
dyadic levels, certify 65 successive bands of odd minima through 1,000,001,
and retain the wider-grid failures of the converse at 9 and 11. Equality
of the completion rotations is not a cycle certificate.

For the common-path obstruction, choose an angular interval separated
from the first \(L+1\) rotation cuts. The exact valuation cylinder has
modulus at most \(4\cdot3^L\). The stated condition
\(64(L+1)3^L\le s\) leaves the asserted number of ordinary sources in the
interval. The affine error is at most \(2j/3\) at step \(j\), using the
bounded ratio between two fractional rotation coordinates. It is smaller
than the available cut margin, so the actual path stays in \([s,2s)\).

Along those paths the scaled mean correction tends to
\(1/[6(\log2)^2]\). The root checked the factor from the uniform rotation
average of \(2^{-u}\), namely \(1/(2\log2)\). Telescoping any lower proposed
drift requires an oscillation growing linearly with \(L\), hence on the
order of \(\log s\) along the constructed range. This rejects a uniformly
bounded corrector of the displayed kind. It does not reject correctors
whose oscillation grows or arguments based on longer physical orbits.

## 3. Gap-four closure and delayed positive sites

**VERIFIED kernel statements and exact controls. Density extensions retain a
separately inspected written input.**

For \(m=11+162j\), the root substituted \(2^{m-5}=64+243v\) and obtained
the actual canonical integer \(W=1601+6144v=(z-31)/2\).
Its ten-step lower prefix reaches \(M_{m-4}\), and its eleven-step upper
prefix reaches \(27\cdot2^{m-5}-17\), with the displayed grades.
This is an ordinary query with \(0<W<z\), not a signed surrogate.

The periodic table for every delayed \(m=12\cdot2^{18k}-1\) was checked
against the long-turn recurrence. Splitting \(m-5\) into quotient and
remainder modulo 11 gives five phases. Increasing \(k\) by five changes
the relevant exponent by a multiple of the required power of two.
The grade-compensated equalities therefore lift from the finite residues
to the enormous actual sources. Six initial rows cover the small
parameters that cannot use the periodic stability inequality.

The resulting earlier exponent is positive and at least forty bits below
the parent exponent. The previously proved earlier-good theorem supplies
its goodness under the two stated leastness implications. Paying the
canonical query proves the gap-four exponent good, and adjacent even
Mersenne routing supplies gap three. No bounded-cycle-only floor premise
is inserted.

The delayed unit recurrence
\(U_{b+1}=U_b+2^{b+3}U_b^2\) follows by squaring the exact power identity.
The root checked its oddness and stabilization modulus. The three positive
prefix charts, followed by repeated two-step turns, give the actual
sites \(U_{18k},27Y_k+2,Y_k+2\). A supplied same-clock merger of the last
two returns every strictly earlier Mersenne under the same leastness
premises. The control checks finite binary residues; the all-parameter
positive-site identities and their implication are Lean theorems.

The density theorem uses PR146 at
f431078244e868dc699fad011044f0d5e7f76437, specifically
research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md and
research/upper-bit-mergers/THREE_RAY_UPPER.md. The root fetched this
commit and read both complete proofs. The oriented two-word process
gives a finite binary-residue absorption bound, not just an assertion
about permanent ordinary basins. Its equal-slope absorbing word is an
algebraic identity on its cylinder. This is why it can also be
specialized to odd-denominator rational starts in the clock obstruction.

For the positive pair the fixed parameters are \((s,d)=(3,-52)\).
After discarding at most \(O(h)\) small original parameters, the unit
stabilizes modulo \(2^h\). Powers \(3^{9k-3}\) visit distinct residues
in each period on every odd-stride progression. At
\(h=\lfloor\log_2 K\rfloor\), at most eight periods suffice.
The resulting \(O(K/\sqrt{\log K})\) exceptional count does not
decide a prescribed exceptional parameter.

For the growing native clock obstruction, the root reconstructed the
marked rational state \((r_q(a)-q,T^a(3^{-q}-1))\).
An actual synchronized meeting after \(H\) must match both its slope
grade and its offset. There is one native suffix at each length
\(j\le J\), so fewer than \(2^{J+1}\) marked target states qualify.
A marked state cannot repeat along one signed trajectory: its grade
would force only even steps, and a repeated value would then have to
be zero. The root read PR192's pinned nonzero proof for all \(q\ge2\).

The relation \(d_q=3d_{q+1}+2\) and PR146 at \((s,d)=(1,2)\) merge all
but \(O(Q/\sqrt{\log Q})\) neighboring trajectories into synchronized
runs. Their augmented grades agree after absorption. One run can visit
each marked state at only one native valuation time. This gives the
stated \(O(\log K+2^J K/\sqrt{\log K})\) bound and its
\((1/2-\epsilon)\log_2\log_2 k\) typical extra window.
This is a written, source-qualified result; it is not included among
the new Lean theorem audits.

## 4. Principal traces and the ordinary diagonal

**VERIFIED written implications, finite ordinary controls and eight arithmetic
kernel statements. No assertion of language exhaustion.**

The root followed every prescribed inverse at the least positive odd
terminal. Legality modulo \(3^n\), positivity and oddness give its least
positive ordinary seed. Raising the terminal by \(2\cdot3^n\) raises
that seed by \(2^{A+1}\). This proves the exact identity
\(\rho_n(y)/y=R/(m+G)\).

The letters one and two are uniquely decoded backwards from the terminal
residue, so these safe words have distinct ternary cells. Different
words at a fixed depth also have distinct ordinary least seeds.
On a fixed script the minima are nondecreasing and stabilize exactly
when one ordinary integer realizes the whole script. Pairing the
affine-correction terms gives \(G\le7\). The already reviewed uniform
posterior theorem supplies bounded increasing \(R\) on this entire
language, including scripts starting with two.

Stopping the dyadic clock in an ordinary-height shell yields
\(O(X^d)\) different principal seeds, where
\(2^{-d}+8^{-d}=1\). The possible unpaired terminal two is included.
Hence the reciprocal powers are summable for all exponents above \(d\).
Dominated convergence on the ordinary seed coordinate proves the
unnormalized trace limit and total-variation statement. This excludes
mass carried only by changing finite witnesses from the limiting sum.
It does not prove that the actual ordinary atoms are absent.

At any strict seed jump, the new seed gains at least the entire previous
dyadic modulus. Its principal terminal therefore exceeds half the
ternary modulus. This proves the stated entire-tail criterion; an
infinite subsequence of small terminals alone would not suffice.

The compression to \(3t/2\) on even inputs and \((9t+1)/8\) on
inputs 7 modulo 8 was checked in both directions. Both ranges are
ternarily disjoint and both positive inverses are deterministic.
The word-height envelope retains the affine intercept. It bounds an
ordinary inverse source by \(C\) in the unshifted height test; a finite
pigeonhole argument then gives one actual infinite seed from unbounded
word lengths. This inference uses bounded ordinary sources.

For shifted tests, the covering sum gives the stated Hausdorff-dimension
bound. In the coherent case, consecutive integer errors are congruent
modulo an exponentially larger ternary modulus, so they eventually
stabilize. This forces an ordinary shift but does not rule out shift zero.
The dyadic and ternary dimensions are not treated as independent at
an ordinary integer.

The C++ scan enumerates the complete backward stop rules for each
ternary shell, including the one-digit overshoot exactly when the
oldest letter is B. Each class contributes at most one integer in
its shell. The forward test uses the candidate's own height. The
root checked that 128-bit arithmetic suffices over the supported
depth range: \(t<2^{72}\), the dyadic overshoot is bounded, and the
maximal real growth per dyadic bit is \(3/2\). The intermediate
multiplication also stays below 128 bits.

At depth 42 there are 23 joint hits, all with finite future exits.
The Python control independently scans all integers through 59,049,
reconstructs every retained hit, and verifies the exact compressed
domains against the ordinary odd map. This is a finite two-height
test, not a general convergence census or proof of all-time emptiness.

## 5. Global prefix trace and harmonic birth reserve

**VERIFIED written equivalence and finite controls; six formal arithmetic
statements. The vanishing estimate is OPEN.**

The root reconstructed the trace directly from its original word
probabilities \(2^{-A}\). Dividing by the word-dependent centered
denominator gives \(1/(m+zG)\) exactly. At \(z=1\), only the mass of
accepted words in a ternary cell is kept; this is not a claim about
the whole-cell posterior. At \(z=0\), different words in one ternary
cell still have their own intercepts.

For the sparse-seed count, a cutoff at binary position \(j\) can be
inside a long exponent. The completed gate at that exponent still
forces at least \(4j/7\) odd departures among the first \(j\)
shortcut positions. The parity-prefix bijection and the binomial
entropy bound give exponent \(H_2(4/7)<1\). There is at most one
representative per binary residue in the selected ordinary shell.

The root also supplied and checked the alternative domination proof:
each fixed ordinary principal seed is born once and has one
deterministic continuation. It can disappear once, but cannot
reappear after its gate has failed. The summable total harmonic
birth budget therefore gives a finite measure on all such seeds.
Either argument supports dominated convergence without an
unproved stationary or ordinary-basin density hypothesis.

A positive nonperiodic orbit has distinct states tending to infinity.
The previously reviewed simple-path reciprocal bound, applied after
the last low visit, makes its correction product finite. An eventually
periodic orbit instead has geometrically growing correction.
This justifies the raw trace, centered boundary jump, and diagonal
parameter \(1/n\) separately. The centered full-Collatz equivalence
itself does not require the simple-path reciprocal input.

A least odd seed in any bad component is at least three and every
forward odd site is no smaller. Its exact product gives
\(2^{A_n}\le(10/3)^n<2^{7n/4}\), so this same seed satisfies the gate
at every depth. Its principal representative is already no larger
at every finite depth, even before the seed becomes its own least
representative. Thus \(J_n\ge1/m\) at every depth, proving the direct
finite cutoff \(J_n<1/L\). Reaching one eventually forces repeated
exponent two and hence failure of the gate.

The sibling minima have at most one zero and total reciprocal at
most two. The root checked the even/odd recursion, including the
zero term. Multiplying by the parent modulus gives the per-parent
newborn cost \(2^{-A}\). The Chernoff factor is exactly
\((7/8)(7/6)^{3/4}<1\). The rational debt identity was separately
summed using the omitted geometric tail; its residual term has the
correct nonnegative sign. These yield nonincreasing upper reserves,
not a two-sided rate for disappearance of existing seeds.

The checker enumerates the complete accepted word tree through
depth 12, checks each actual child and its reciprocal cost, and
compares the whole tree with direct ordinary seed enumeration
through depth seven. It encloses the trace sums outwards with
integer floors and an explicit number of terms. Lean verifies
the sibling bound, debt row, envelope inequality, cutoff arithmetic
and two exact constant comparisons. It does not yet formalize
the entire trace equivalence or its convergence.

## 6. Character cancellation and late source intake

**VERIFIED finite-character identities and the triangle-bound obstruction.**

The root derived the coefficient normalization \(c(1)=3/2\), the
finite Fourier inversion on ternary units, and the product-character
Dirichlet expansion. All three dyadic twists remain nonprincipal
after multiplication by any ternary character, by CRT. Their
ordinary ordered series therefore converge at one; only a finite
character sum is interchanged.

The all-one exponent word gives \(\rho_k(-1)\ge(3/2)^k\), forcing
the nonprincipal coefficient norm to be at least
\((3/2)^k-3/2\). This is a lower bound on the loss in a uniform
triangle estimate, not a lower bound for the signed trace.
The principal contribution is constant in \(k\). The remaining
correlated sum is precisely the unproved target, with the
external trace implication retaining its original qualifications.
The escape agent independently reconstructed these calculations.

The root inspected MIT's primary reported GRH verification record
and its exact Dirichlet statements, without rebuilding the external
archive. No GRH assertion is used in the finite identities or the
coefficient-norm lower bound.

Late read-only intake included PR193 at
2796977d3f02ad57daeb7510f16da29527f9afde and PR200 at
bf7d52e78631954a9fd35e4ce973acd27738fc80. The root read the new
primitive-character and canonical-birth arguments in the former,
and the full second-checkpoint independent review in the latter.
The global trace credits the canonical-birth input explicitly.
Further heads PR192 at 75eac0cbc744469ae2886bc2f140685c484e9fe7,
PR200 at 2346db2d49030ef385b73e1ee3e27dcbff86d2d9 and
PR206 at 640bf7e511831a0ffc4f00462f12df81f8a8a619 were obtained
for continuing work. Those inventories are not a claim that
every mathematical file at those heads has been reviewed.

## 7. Execution evidence

The fresh complete Lean replay audited 53 declarations in its initial
group. The minimum census and global birth module added two and six
audits, respectively: 61 total, comprising 30 new printed declarations
and 31 dependencies. Only propext, Classical.choice and Quot.sound
occur. Each new project object was built afresh against the pinned
Lean 4.34.1 and mathlib revisions.

Seven controls ran both normally and with Python optimization.
Every complete JSON payload matched its archived output, and the
ordinary and optimized stdout bytes agreed. The diagonal control
independently compiled its C++ source in each run.

The first Lean driver attempt lacked the existing PaidCheckpoint
dependency and stopped with an unknown-module error. The corrected
complete dependency replay was successful. That setup error is not
counted as a mathematical rejection or a successful run.

[FOURTH_REPLAY.json](FOURTH_REPLAY.json) assembles the successful
execution groups without changing their individual rows and records
the source receipt hashes. The final driver can replay the whole
packet or its explicit minimum/global supplemental groups.
Repository validation is run separately on a clean complete
checkout and again on the actual published commit.
