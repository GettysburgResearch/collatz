# Closing proposal after the unconventional pass

**OPEN. This is a research proposal with proved local and infinite-family
components, not a complete proof of Collatz.** The pass began on 26 November
2026 at 18:46 UTC and used three parallel GPT-6.2 Astra agents at ultra effort.
The exact source revision and the results of fresh compilation are recorded
in the accompanying replay receipt. This document separates the mathematical
proposal from that execution evidence.

The strongest direct contribution is a smaller **canonical ordinary source**
on new explicit subprogressions of the hard Mersenne family. It retains both
physical orbit labels and transfers every supplied upper hitting certificate
with an exact cost. The main analytic contribution controls all clocks in the
paired return grammar. The most speculative contribution is an algebraic-unit
and regulator construction; its remaining prime boundary is explicit.

## 1. The pointwise obligation

Use the shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
\qquad C(n)\Longleftrightarrow \exists H\ge0:T^H(n)=1.
\]

The existing minimum construction in
[MinimumFailure.lean](../astra-minimum-source-20261124/minimal/MinimumFailure.lean)
starts from a positive counterexample and produces a least odd tripling
disagreement with its orientation proved. In particular its bad multiple of
three is smaller than every other bad positive multiple of three. The
[existing full-proof consumer](../astra-ultra-closure-20261125/intake/MinimumClosure.lean)
shows exactly what a universally available smaller multiple in that same
component would imply. Its descent premise remains open.

The canonical reverse-disagreement route instead works with a positive
\(z\equiv17\pmod{48}\), a bad lower component, and an actual certificate
\(T^H(3z)=1\). A smaller canonical \(y\) is useful when the construction
provides both

\[
T^i(y)=T^j(z),\qquad T^{H'}(3y)=1.
\]

These are literal ordinary equalities. The new theorem below supplies them
on specified original indices. An existence theorem with a freely selected
index, even at arbitrarily large depth, does not discharge the universal
premise for a given least disagreement.

## 2. A canonical descent that is already a Lean theorem

Put

\[
m=11+162j,\qquad z_j=\frac{2^{m+7}-271}{81},\qquad
Z_0=\frac{2^{m+19}-1293643}{3^9}.
\]

The signed seed \(-1293643/3^9\) supplies an actual positive lift whenever
the displayed expression is integral. If \(3^k\mid Z_0+1\), set

\[
W_k=-1+\frac{2^k(Z_0+1)}{3^k}.
\]

The lower and upper physical paths satisfy

\[
T^{k+19}(W_k)=2^m-1,\qquad
T^{k+21}(3W_k)=2^{m-2}.
\]

Their odd counts are \(k+9\) and \(k+8\). The original parent reaches
the same two checkpoints in seven and nine clocks, with four and three
odd departures. Thus **every** given hit from \(3z_j\) transfers to
\(3W_k\) with \(k+12\) added clocks and \(k+5\) added odd departures.
At \(k=80\), the integer inequality \(2^{139}<3^{89}\) proves
\(2^{40}W_k<z_j\).

For a direct return to the canonical class, impose three more ternary
digits, \(W_k\equiv10\pmod{27}\), and use

\[
y=\frac{16W_k-7}{9}.
\]

Then \(y\equiv17\pmod{48}\), the lower path reaches \(2^m-1\) at
clock \(k+23\), and the upper reaches \(2^{m-2}\) at clock \(k+25\).
For \(k\ge9\) one has \(0<y<z_j\). Every supplied hit at clock \(H\)
from \(3z_j\) becomes a hit at clock \(H+k+16\) from \(3y\), with
exactly \(k+7\) additional odd departures.

For each \(k\ge9\) a single class modulo \(3^{k+7}\) of the original
index \(j\) satisfies these conditions. At \(k=9\) it is
\(j\equiv4471574\pmod{43046721}\). The classes for different \(k\)
are disjoint because they specify the exact valuation of \(Z_0+1\).
They project to \(j\equiv3533\pmod{19683}\).

The fully quantified Lean statement `signed_narrow` says that for every
\(k\ge9\) and every index cutoff, there is an ordinary index above that
cutoff with a smaller positive canonical representative, both exact paths,
and the transfer of **any** supplied upper certificate. Its proof uses
the actual shortcut map. It does not assume that the original lower orbit
converges.

Read [the complete proof and provenance](descent/SIGNED_MERSENNE.md),
[the physical kernels](descent/SignedMersenne.lean),
[the digit-lifting theorem](descent/SignedIndex.lean),
[the broad cofinal theorem](descent/SignedHardFamily.lean), and
[the canonical theorem](descent/SignedNarrow.lean).

**Novelty boundary.** Arbitrarily large gains on cofinal hard subfamilies
were already available in PR197. Two signed rows found in this pass were
exact rediscoveries of its canonical two-center rows. The uniform
\(17\leftrightarrow11\) exchange was also already known. The present
contribution is the different seed and address, the \(2/3\) contraction
per extra lower odd, the shorter canonical entrance, and explicit upper
certificate accounting. The packet preserves the older rows as controls.

## 3. Why density does not close the missing index

Applying the earlier affine-pair absorption estimate to the *actual*
postpeak states gives a complementary result. Compare \(z_m\) and
\(z_{m-162a}\), where \(a\ge1\). Their lower peaks are

\[
3^m-1=3^{162a}(3^{m-162a}-1)+(3^{162a}-1).
\]

Inside every fixed odd-modulus progression of hard indices, all but
\(O(J(1+a)/\sqrt{\log(2J)})\) of any eligible \(J\)-term interval have
an actual merger of these peaks. On those indices the smaller source is
already canonical and every upper certificate transfers with **the same
odd count** and \(162a\) fewer clocks. The estimate is uniform in the
location and odd modulus of the progression. This is an application of
PR146's written theorem and its earlier exponential-parameter method;
it is not a newly proved probabilistic absorption theorem or a Lean
formalization of that theorem. See [Postpeak density](descent/POSTPEAK_DENSITY.md).

The exact missing inference is crossing the cut at a specified least bad
source. A toy label sequence that is good below one index and bad from
that index onward satisfies density-one agreement with every fixed
backward shift: only finitely many indices cross its boundary. Even
positive-density amplification of one bad label would not, by itself,
preserve leastness at the amplified sources. A valid completion needs a
physical link crossing this particular cut, or a new invariant forcing
such a link. It cannot be inferred from the density estimate alone.

The final direct-source test is stronger than a finite example. For
\(m=12\cdot2^{18r}-1\), \(r\ge1\), a Lean theorem shows that
the ordinary peak \(3^m-1\) does not meet **any** earlier peak
\(3^t-1\), \(t<m\), when the two independent clocks are both at
most \(18r+4=\lfloor\log_2m\rfloor+1\). These hard exponents
occur cofinally in every prescribed ternary class of the original
index. An elementary size bound also shows that a merger from the
later peak to the earlier one requires a clock larger than \(m-t\).
This makes the obstruction to short-distance amplification explicit.
The [delay note](descent/POSTPEAK_DELAY.md) distinguishes these
formal results from its further source-qualified mixed-phase argument.

The final attack also found **paid repairs at these preassigned
parents**, without changing their high binary cofactor. The
[late supplement](descent/PAID_DELAY_REPAIRS.md) supplies exact
affine certificates for the first thirty parameters. For the first
two, at exponents 3,145,727 and 824,633,720,831, it constructs
smaller canonical sources and transports every original upper hit
with costs respectively `+8 clocks, +6 odds` and `-16 clocks,
+2 odds`. The other twenty-eight have an actual same-component
representative smaller by more than `2^40`, using the prior
quantitative-return consumer for canonical descent. A specified
infinite class of the same preassigned parameters also enters the
depth-nine canonical bridge. These are successful original-source
comparisons beyond the delay; an all-parameter theorem remains open.

## 4. All-clock control of paired returns

For common-clock returns

\[
(Y,3Y-1)\longrightarrow(X,3X-1),
\]

retain the actual normalized integer carry, the two odd counts, and
their difference. The carry is nonzero on an unmerged positive pair.
It is not replaced by an independently chosen rational center.

The [gap-entropy argument](operator/GAP_ENTROPY.md) gives, for the total
number \(W(P)\) of return words of grade at most \(P\), across **all**
shortcut clocks,

\[
\log W(P)\ll(P+1)(1+\log\log(P+3))^2.
\]

Rank-zero holds have total cost \(O(P)\). For the remaining gaps, the
additive offset of a short intervening word is either zero, forcing
rank zero, or has controlled dyadic valuation by Yu's theorem on
logarithmic forms. Encoding the smaller of valuation spent and retained
and summing over scales produces the displayed bound. This is a written
proof with a source-qualified use of Yu; the finite carry and divisibility
lemmas are separately in Lean.

The [rank-twelve certificate](operator/RANK_PRESSURE.md) supplies a
stronger exponential estimate on the strip \(|r|\le12\), where
\(r=1+b-a\) and \(a,b\) are the lower and upper odd counts:

\[
W_{p,12}\le10(8.1)^p.
\]

The computation treats **every integer carry**, not only a bounded
carry census. An analytic square-root weight handles the infinite
tail; integer weight repairs handle a finite core and all predecessors
affected by those repairs. The final verification pass holds the
weights immutable. Its runtime receipt distinguishes ordinary execution
from the execution with undefined-behavior checks. The tail argument and
the connection to return-word counts are written mathematics, not a
claimed Lean verification of the C++ computation.

These estimates also quantify a coverage requirement. To enter one
prescribed source class modulo \(3^L\) for **every** ordinary terminal
in a fixed cylinder modulo \(3^b\), the rank-twelve grammar needs

\[
P\ge\frac{\log3}{\log2.7}(L-b)-O(1).
\]

There is a separate [positive paired-gain construction](operator/PAIRED_GAIN.md)
on explicit terminal congruences. It preserves both arms and permits
arbitrarily large height gain at growing cost. Its congruence hypothesis
cannot be supplied freely at one fixed terminal. Excursions outside
the rank strip and a universal fixed-source descent remain open.

An additional [coverage theorem](operator/SUFFIX_MASS.md) bounds
actual smaller ordinary sources reaching any point on the Mersenne
orbit through its first \(S\) even departures. The number of odd
departures and the total clock are unrestricted. A signed inverse cut
reduces every such witness to a target of the form \(2^{m+d}+A\).
The known reverse-prefix crossing inequality and a uniform physical
distortion bound then control all these targets together.

For a gain greater than \(2^{40}\), the independent distortion
certificate in this packet gives an index-space Haar bound below
0.07422 through the first 24 even departures. The stronger imported
four-thirds distortion theorem gives a bound below 0.03299 through
the first 32 even departures, with its published finite inputs retained.
For a length-\(J\) block of ordinary indices, the same bound plus a
vanishing error holds if the witness's excess odd grade is at most
\(\lfloor H_2(\log_3 2)^{-1}\log_3J\rfloor\).
This latter conclusion is an ordinary counting theorem; the unrestricted
Haar bound alone is not. The signed-cut method and first-crossing
inequality are credited to their prior literature. The application
retains actual height gain and the growing excess-grade budget.

The [joint obstruction](descent/JOINT_OBSTRUCTION.md) puts the two
comparison failures at the **same ordinary parent**. For arbitrary
\(P,H\ge4\), finite-depth ternary periodicity and CRT select
\(j\in[3^P2^{H-3},2\cdot3^P2^{H-3})\) that admits neither the
specified 40-bit smaller-source return through 24 even departures
at excess grade at most \(P\), nor a meeting with any earlier
Mersenne peak through independent clocks at most \(H\). Taking
\(P=H=n\) makes both budgets logarithmic in \(m\asymp6^n\).
This construction uses the independent distortion bound, not the
imported four-thirds constant.

The final pressure check also rejects a too-strong global extension.
There are unmerged state-graph loops of arbitrarily large clock
length \(L\), with only one odd departure on each arm and weight
\(1/9\). Hence a positive supersolution with a uniform per-clock
rate below one cannot exist on the entire graph. The rank-twelve
result survives. A global continuation must use odd-grade cost or
prove additional restrictions on charts reachable from the specified
starting state; the counterexample does not assert that reachability.

## 5. What the arithmetic machinery does and does not supply

The initial [squareclass descent](adelic/GROWTH.md) already gives an
actual convergence theorem if a specified dependence condition holds
at every growth triple. The later [Pell-field construction](adelic/PELL.md)
associates to each odd state the norm-one unit

\[
E_x=6x+1+2\sqrt{3x(3x+1)}.
\]

Repeated Pell fields in a short physical window force an explicit
height bound. Distinct quadratic characters give independent unit
directions. This proves growing arithmetic complexity along a putative
escape; no universal upper bound on that complexity has been obtained.

The [cubic lift](adelic/CUBIC_FIELDS.md) is more than a change of
notation. The real trace \(t_x=E_x^{1/3}+E_x^{-1/3}\) satisfies
\(t_x^3-3t_x=12x+2\); its cubic field has discriminant exactly
\(81\operatorname{disc}\mathbb Q(\sqrt{-x(3x+1)})\). The
distinct Pell labels give independent cubic Kummer radicals. Combining
the earlier rank bound with a block argument proves that, for every
fixed \(h\), a density-one set of \(h\)-edge windows of any
hypothetical injective positive orbit has full splitting group
\(S_3^h\). This statement concerns one fixed orbit. It remains
compatible with a cubic extension of local degree at most 27 at three:
global independent characters and one local completion have different
dimensions.

The same cubic lift supplies two coherent embeddings of the entire
physical orbit field at two, rather than new embeddings at each
window. A normalized norm-one element has valuations \(a,-a/2\)
at these choices and zero at every place above three, while its
physical real value tends to one. Its exact absolute-height formula
shows why this is not a small-height contradiction. These fixed-place
identities are recorded with their missing implication in C5.

The [local-unit analysis](adelic/LOCAL_UNITS.md) retains dyadic and
ternary logarithms, third-field poles, and the exact multiplicative
coordinate on a whole interval. Scaled physical path swaps exclude a
proposed completely additive prime potential and its stated convex or
concave correction. They do not exclude arbitrary rank functions.

The [regulator construction](adelic/REGULATOR_REPAIR.md) produces a
positive small Rogers-dilogarithm expression on an ordinary cycle and
clears every boundary contraction at primes above two and three with
coefficient denominator 288. A literal computation on the genuine
cycle at one shows a remaining contraction at seven. The common
ternary inertia sum retains a sign; full Galois averaging of this
particular expression does not, as exact rational-cycle controls show.

A separate [invariant stress construction](adelic/INVARIANT_STRESS.md)
cancels the first variation using four clock powers. It retains full
Galois invariance and a positive small real value while permitting
two-place corrections with bounded coefficient denominator. In a
totally real multiquadratic field the invariant exterior square of
global units is zero. The Bloch torsion grid therefore forces a
remaining finite-prime defect in this constructed expression. That is
a necessary defect, **not a contradiction to the existence of the
cycle**. Auxiliary corrections may themselves contribute primes.

This attempt has reached its precise missing step: derive a
Collatz-specific cancellation or exclusion of the entire remaining
boundary, with the real sign retained. The two-place cancellation
alone is insufficient, and the existing explicit surviving defect
prevents treating it as the full boundary identity.

## 6. Evidence and a concrete next proof obligation

The [root review](../../reports/astra-unconventional-20261126/SECOND_REVIEW.md)
records independently reconstructed arguments and limitations. The
[replay driver](../../reports/astra-unconventional-20261126/replay.py)
compiles all new Lean modules with warnings as errors and automatic
implicit variables disabled, audits every public theorem, compares
normal and optimized Python controls, and rebuilds the integer pressure
certificate normally and with undefined-behavior checks. The final
receipt pins the complete source tree and actual results. Repository
validation checks integrity rather than the truth of the written
infinite arguments.

The next direct target is a terminating ordinary procedure that, for
each surviving canonical disagreement, constructs a smaller positive
canonical representative and transports its supplied upper hit. It may
combine the signed bridge, a postpeak merger, and a paired return, but
must prove success at the **original** source. The arithmetic alternative
requires a full boundary theorem, and the transport alternative requires
a genuine global component argument. None of these universal steps is
proved by the present packet.
