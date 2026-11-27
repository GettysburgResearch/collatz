# Six-hour Collatz research sprint: results and remaining obligations

**Status: PROPOSED research. The Collatz conjecture remains open.**

This sprint did not prove that every positive integer reaches one. It
produced written arguments, finite formal consumers, exact arithmetic
controls and explicit counterexamples to several tempting strengthenings.
The strongest conclusions concern full cycle denominators, the first
meeting with a smaller orbit, and the cost of an escaping component.
Their outstanding pointwise obligations are stated below.

The work is collected in [draft PR211](https://github.com/GettysburgResearch/collatz/pull/211).
The branch began at main commit
ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a. Three GPT-6.2 Astra agents at
ultra reasoning worked on cycles, descent and analytic rigidity, with
cross-reviews and independent root reconstruction of the principal proofs.
The session began on 27 November 2026 at 12:13:10 UTC.

## What was read and what was actually checked

The initial intake read the repository entry instructions, research map,
integrated packet, results catalog, scoped errata and selected current
frontier proofs. [INTAKE.json](INTAKE.json) freezes the complete metadata
inventory of 146 then-open pull requests, including their full heads.
That is a source map, not a claim that every proof in those 146 pull
requests was independently verified. The recent packets most directly
connected to the chosen routes were read at pinned heads; their paths
and antecedents appear beside the consuming claims.

Across ten execution checkpoints, the root independently rebuilt
**57 distinct local Lean modules**. Their printed public axiom
inventories contained only the permitted standard axioms. The replay
used Lean 4.34.1, pinned mathlib source, fresh local outputs, one worker,
warnings as errors and no asynchronous elaboration.

The root also replayed **39 distinct finite Python programs** in normal
and optimized modes, with matching outputs. The complete sixfold energy
calculation was run twice from frozen GMP/C++ source. Its 61 cell phase
matrices and 1,441 complete block phase intervals all passed their exact
integer inequalities. Complete clean local and API-published science
checkouts passed all eleven repository regression commands at every
checkpoint. The [evidence archive](../../reports/astra-reciprocal-rigidity-20261127/)
retains source hashes, exact trees, commands, outputs and scope statements.

These checks have different meanings. A bounded enumeration checks its
enumerated cases. A Lean module proves its declared theorem. Repository
validation checks integrity and its bounded regression bundle. None of
them silently formalizes a neighboring analytic theorem. In particular,
the final asymptotic results below are written proofs, with the named
external inputs retained where they are used.

## 1. Full denominators at a density-one set of least periods

Use the shortcut map
\[
 T(n)=
 \begin{cases}
 n/2,&n\text{ even},\\
 (3n+1)/2,&n\text{ odd}.
 \end{cases}
\]
For rational inputs of odd reduced denominator, parity means numerator
parity. Let \(d_{\min}(n)\) be the least full reduced denominator among
all nonzero signed rational cycles of least physical period \(n\).
All phases of a cycle have the same reduced denominator.

Put
\[
 p=\log_3 2,\qquad h_*=H_2(p),\qquad
 \theta_F=\frac1{2h_*}=0.5263404293\ldots,
\]
where \(H_2(p)=-p\log_2p-(1-p)\log_2(1-p)\).
The final [joint denominator census](cycles/phase8/FAREY_CENSUS.md) gives
\[
 d_{\min}(n)>
 n^{\theta_F}(1+\log n)^\lambda
 \quad\text{at a set of periods of natural density one}
\]
for every fixed
\[
 \lambda<
 \lambda_F=\frac{3/2-h_*}{2h_*}=0.2895106439\ldots.
\]
Thus \(\lambda=11/38\) is allowed. At each retained period, the assertion
holds for every primitive word and both signs. It controls the full
reduced denominator, including cancellation between the complete affine
numerator and denominator. It is not a statement about the average word
or only selected prime factors.

The earlier [ascent census](cycles/phase8/ASCENT_CENSUS.md) proves every
exponent below \(1/(1+h_*)=0.5128322087\ldots\), including the explicit
\(20/39\). The [endpoint refinement](cycles/phase8/ENDPOINT_CENSUS.md)
reaches that exponent and adds a logarithmic factor. Counting all
denominators together gives the stronger final exponent above.
The arguments use elementary counting and irrational equidistribution;
they require no quantitative irrationality measure, Subspace Theorem,
finite Collatz verification floor or convergence assumption.

### Why the argument works

Two distinct rational phases \(a/d,b/e\) of the same sign, with
\(d,e\le D\), that share \(t\) native parity bits satisfy
\(2^t\mid ae-bd\). If their magnitudes lie in an interval of width
\(X\), then \(0<|ae-bd|\le D^2X\). Once \(2^t>D^2X\), at most
one such phase realizes each word across the entire denominator range.

For cycles whose real magnitudes stay above a floor \(M\), start with a
rational majorant of the logarithmic cycle gap and add a telescoping
reciprocal-height correction. Future minima of the corrected partial
sums produce nonnegative cyclic charges. Their total dominates the
cycle gap. At every phase carrying a positive charge, all future
prefixes satisfy a lower bound on odd frequency close to \(p\).
At phase height \(y\), the charge is at most \((B+1/2)/y\), where
\(B\) is the chosen correction parameter.
Paper 217 is credited for the future-minimum charging architecture.

A different witness handles a cycle that dips below \(M\). Its least
period supplies \(n\) distinct numerators, so its maximum is at least
\(n/d\). Take the last crossing of \(M\) before that maximum. The
whole excursion through the maximum and back toward the floor stays
above \(M\). Both the ascent and descent require time. Their combined
lower bound makes the segment long enough to read the required parity
digits uniformly for \(d\le D\le N^{11/20}\), where the least period
lies in \([N,2N]\). Distinct cycles cannot share that witness.

The final improvement uses the whole prefix condition. A centered
Bernoulli walk must survive at the beginning, survive in reverse at the
end, and hit the prescribed endpoint through the middle. These three
factors give a uniform \(t^{-3/2}\) saving in the word count. Taking
the floor and correction parameter proportional to \(\log(2D)\)
produces the joint denominator bound
\[
 D^{2h_*}\bigl(\log(2D)\bigr)^{h_*-3/2}.
\]
It bounds the total charge of high-minimum cycles and the number of
low-minimum cycle witnesses. Separating large from small logarithmic
cycle gaps yields the displayed theorem. A small gap forces
\(\|n\log_3 2\|\) to be small; irrational equidistribution makes those
period values sparse.

**What remains:** an integer cycle has denominator one and can occupy
one exceptional period. A density-zero exceptional set can contain a
particular integer. No step in this argument removes every exceptional
period.

## 2. Why a hypothetical cycle cannot be amplified by simple splicing

The [rotation-splice argument](cycles/phase9/ROTATION_SPLICES.md) proves
that mixing full rotations of a positive ordinary primitive cycle incurs
a denominator cost:
\[
                              d'\ge cP^2,
\]
where \(P\) is the resulting least physical period and \(c>0\) is
absolute. As the parent period grows, the lower bound exceeds every
fixed power of \(nk\), where \(n\) is the parent period and \(k\)
is the least dictionary period of the mixed word. Pure repetition instead
preserves the parent's least period and denominator.

The elementary step uses strict same-side convexity of affine anchors
and a nonzero dyadic cross difference. The quantitative size estimates
use the cited logarithm-separation bound. The argument explicitly keeps
the least dictionary period separate from the least physical period.
PR200's prior compact-shadow divisibility argument receives credit.

At the minimum of an ordinary cycle of least period \(N\), every proper prefix
of length \(N-o(N)\) has cyclic denominator \(2^{N+o(N)}\). The exact
full return has denominator one. The proper-prefix displacement is
nonzero; at the full return it is zero. The two endpoint congruences
transport the same integer, so they cannot be multiplied as independent
conditions.

The [record-type criterion](cycles/phase10/RECORD_TYPES.md) identifies
another precise obstruction. At critical weight \(u=\lfloor np\rfloor\),
every cyclic word can be split after rotation into two contracting
pieces exactly when \(\{np\}\) is not a new lower record among earlier
fractional parts. At a lower record, every word of this type is primitive.
Its physical height order is exactly the order of
\[
                              H_j=nU_j-uj,
\]
where \(U_j\) counts prior odd letters. From the unique minimum, every
proper prefix expands homogeneously. The first coefficient contraction
occurs at the exact return.

Positive rational cycles realize all these record types. For example,
\((19,31,49,76,38)/5\) realizes the word \(11100\) of type \((5,3)\).
These structural restrictions therefore do not by themselves exclude
the type. They explain why the denominator theorem does not extend to
all periods by either repetition or a contracting-piece decomposition.

## 3. A sharp law for meeting a smaller ordinary orbit

Prescribe \(H\) initial odd shortcut steps, leaving the next bit free.
Let \(\tau_H=0\) if the original trajectory has already met the complete
orbit of some smaller positive source by clock \(H\). Otherwise
\(\tau_H\) is the additional original clock of its first such meeting.
The smaller visitor may take any number of steps.

The [synchronization result](descent/postpeak/stopped/SYNCHRONIZATION.md)
proves
\[
 \Pr(\tau_H>t)\le C(t+1)^{-1/2}\quad(H\ge2),
\]
and a matching lower bound for \(H\ge400\) and \(6(t+1)\le H\).
These are relative ordinary source densities. The upper bound already
uses the one smaller source \((n-1)/2\); the lower bound allows every
smaller source and every visitor clock. The upper is an explicit
consumer of the known adjacent counted-pair theorem, credited to
Said Duran and Leen through Weaver 124.

The [stopped law](descent/postpeak/stopped/STOPPED_LAW.md) describes each
postword by exact signed-offset classes and ternary predecessor guards.
It also locates a visible atom: for sufficiently large \(H\), more than
1.061% of the specified cylinder \(O^H EO\) has its first smaller-orbit
meeting exactly at original clock \(H+2\).

### The final result applies to an actual growing finite sample

The [clock-law supplement](descent/postpeak/stopped/CLOCK_LAW_SUPPLEMENT.md)
samples actual integers in \([X,2X)\), conditioned on those initial
\(H\) odd steps, with
\[
 400\le H\le\frac{\log_2X}{120},
 \qquad T=\lfloor H/6\rfloor-1.
\]
The joint distribution of their first \(T\) postbits and complete
waiting clock, including any infinite sample value, is within
\[
                     O(H^{-1/2}+HX^{-1/450})
\]
in total variation of the explicit model using fair binary bits and
an independent Haar ternary coordinate.

The proof pays errors relative to each thin full binary subcylinder.
It compares finite inverse words in both directions, and separately
bounds long physical arrivals and long profitable Haar inverse words.
This preserves the actual integer sample while \(H\) grows. It does
not substitute an independent infinite parity sequence for one fixed
ordinary source.

The limiting clock has tail of order \(t^{-1/2}\), is finite almost
surely, and has infinite mean. At each fixed finite \(H\), however, the
ordinary density-law clock has all moments finite. Using Weaver 178's
prior unconditional exponential first-meeting tail gives
\[
 \mathbb E[\tau_H^a]\asymp_a
 \begin{cases}
 \log H,&a=1/2,\\
 H^{a-1/2},&a>1/2.
 \end{cases}
\]
In particular its complete mean is \(\Theta(\sqrt H)\). Moments of
positive order below one half converge to those of the limiting model.
The supplement also proves these orders in growing finite shells with
the explicit cap \(X^{1/(100a)}\). It does not assert an untruncated
empirical moment bound for a fixed finite sample.

**What remains:** a density law can miss an individual positive
integer. Meeting a smaller orbit is valuable for induction, but the
available law does not guarantee that meeting for every source.

A final [fixed-target corollary](descent/postpeak/stopped/FIXED_TARGET_COUNTED_DENSITY.md)
sharpens the synchronization boundary. For every fixed positive target
\(a\), the set of sources \(n\) for which some common clock \(t\)
satisfies both \(T^t(n)=T^t(a)\) and \(F_t(n)=F_t(a)\) has natural
density zero. This covers periodic and escaping target trajectories.
The proof uses the cited density-one adjacent counted-fusion theorem,
an integer label whose cycle integral vanishes, and disjoint label sets
under multipliers \(2^r3^s\) close to one. It is an explicit consequence
of the same clock-phase mechanism developed earlier in the packet.
Changing adjacent pairs can synchronize on a set of density one while
synchronization with every fixed counted target has density zero.
Ordinary arrivals at target one still have positive lower density.
The root and rigidity independently reconstructed this final supplement.

## 4. An exact cost for an escaping component

For the shortcut slopes \(a(n)=1/2\) or \(3/2\), take a total computable
rational function \(0<u(n)\le1\), and define
\[
 d_u(n)=\max\{0,\log(a(n)^2u(n)/u(Tn))\},\qquad
 D_u(X)=\sum_{n\le X}d_u(n).
\]
The [escape-flux identity](rigidity/phase9/ESCAPE_FLUX.md) says that the
number \(c\) of escaping components, including the value infinity, is
\[
 c=\min_u\liminf_{X\to\infty}\frac{D_u(X)}{2\log X}
  =\min_u\limsup_{X\to\infty}\frac{D_u(X)}{2\log X}.
\]
The class can be restricted to edge defects at most \(2\log3\).

Each disjoint escaping trajectory costs at least \(2\log X-O(1)\)
before its first height crossing. This lower bound uses the main
repository's written finite simple-path reciprocal estimate. An explicit
stopped-slope construction attains the rate when the finite number of
escaping components is known existentially. The
[integer-budget refinement](rigidity/phase10/FIRST_CROSSING_BUDGET.md)
requires only a proposed component count in its program, but its totality
is equivalent to that budget being adequate; the correct count is not
known.

Unconditionally, delayed first-crossing marks give positive computable
functions with arbitrarily small weighted defect sums. Their decreasing
limit is positive exactly at bounded starts. At an escaping start the
limit is zero. Thus vanishing ambient error does not recover the positive
limit needed to exclude that start.

A [separate true-height functional](rigidity/phase9/CYCLE_AND_ESCAPE_COST.md)
also detects nontrivial cycles. Its minimum is infinite if escape
exists; otherwise it is the sum of \(\log(1+n^{-2})\) over periodic
states outside \(1,2\). Its value is zero exactly when Collatz holds.
The identity characterizes that value; it does not establish that it
is zero.

## 5. Counterexamples that clarify the remaining proof obligations

The final packet retains failures of plausible shortcuts instead of
using them implicitly.

| Proposed inference | What the packet establishes |
|---|---|
| Equal-clock synchronization can replace every ordinary merger pointwise. | At \(n=7\), the smaller source \(3\) meets the original orbit at \(5\), while the canonical post-ramp pair \(26,8\) never synchronizes at equal clocks. The earlier equality is a density identity. |
| Arbitrarily long positive lifts give one positive infinite exceptional source. | The signed ray from \(-5\) has maximal, expanding prefixes and arbitrarily large positive finite lifts. The unique source realizing the entire ray remains \(-5\). |
| Many predecessors of a bad minimum amplify the number of bad minima. | No smaller visitor anywhere on a complete future is exactly the property of being the minimum of one's orbit component. There is one such minimum per component. |
| Population estimates and preserved finite traces exclude escape. | A sparse changed-map construction plants an escaping spine while preserving the specified trace and population properties. It is explicitly a changed map. |
| Complete smaller-meeting clocks above a finite cutoff determine convergence. | Changing one arbitrarily high known-convergent odd gate into a fixed point preserves every such clock above its finite future, while two positive-lower-density basins force separated long-time odd frequencies. |
| Positive color densities, negligible adjacent boundary and dilation identities force one component. | A generic coloring has both colors of density one half, exact invariance under multiplication by two and three, and adjacent boundary of density zero. The exact affine Collatz relation is still a separate requirement. |
| The other predecessor branch always has a uniform inverse-logarithmic relative share. | Weaver Paper 202 already gives counterexamples in the tree of one. The source check prevented use of this false unrestricted estimate. |

The underlying proofs and exact scopes are in
[SIGNED_EXCEPTION.md](descent/postpeak/stopped/SIGNED_EXCEPTION.md),
[ONE_SITE_MUTANT.md](descent/postpeak/stopped/ONE_SITE_MUTANT.md),
[GENERIC_COLORING.md](descent/postpeak/stopped/GENERIC_COLORING.md),
[SPARSE_SPINE.md](rigidity/phase11/SPARSE_SPINE.md), and
[SIBLING_SHARES.md](rigidity/phase12/SIBLING_SHARES.md).
Konieczny's related asymptotic-automaticity construction is credited
beside the generic coloring.

For the true map, an escaping odd seed \(s\) prime to three would force the full
other-parent shares along its successive odd states \(x_j\) to satisfy
\[
 \sum_j\frac{d(3x_j+1)}{d(Tx_j)}
                 \le\log(1/d(s)).
\]
Here \(d\) is one common predecessor-density profile and fixed-target
positivity is an external input. The main-path masses stay above
\(d(s)>0\). Weaver and Wren's earlier logarithmic sibling proposal and
summability argument receive explicit credit.

The [finite-seed reduction](rigidity/phase12/FINITE_SEED_REDUCTION.md)
then applies Weaver's uniform bound for a basin with no small ancestor.
For each fixed \(\eta>0\), every odd target with \(d(x)\ge\eta\) lies
on the forward orbit of one of finitely many small seeds. A logarithmic
lower-share assertion restricted to this positive mass floor is
equivalent, under those inputs, to absence of escaping orbits. If every
orbit is bounded, its high-mass sector is finite and the assertion is
vacuous above it. This does not provide a new independent proof of
boundedness; it identifies where the proposed comparison stores the
remaining difficulty. The earlier Valbuena/Wren qualitative equivalence
is credited.

## 6. A computable finite-source variance target

For a positive source \(y\), let \(F_t(y)\) count odd departures in its
first \(t\) shortcut steps. Define the finite quantities
\[
 L_X=\left\lceil\log_2(2X)\right\rceil^2,\qquad
 V_X=\operatorname{Var}_{1\le y\le X}\!\left(\frac{F_{L_X}(y)}{L_X}\right).
\]
The [source-variance reduction](descent/postpeak/stopped/SOURCE_VARIANCE.md)
proves, using the two named Mazur inputs below,
\[
 \text{Collatz holds}\quad\Longleftrightarrow\quad\liminf_{X\to\infty}V_X=0.
\]
In fact convergence implies \(V_X\to0\), while any counterexample forces
\(\liminf V_X>0\). This is an equivalence with a still-unproved premise.
The sprint supplies no claim that this variance actually tends to zero.

The external inputs are the July 2026 natural-density logarithmic-time
arrival theorem for every diverging threshold, and the September positive
lower predecessor-density theorem. Their source pins and status are
retained in the manuscript. They were read, not rebuilt in this sprint.

The new diagonal argument fixes a target \(a\). The maximum first
arrival time from its basin members below any fixed bound is finite.
Choose a diverging threshold so slowly that this maximum is at most
\(\sqrt{\log n}\). The July theorem then makes all but \(o(X)\) members of that basin
below \(X\) reach \(a\) in \(O(\log n)\) raw steps. If Collatz holds,
almost every source below \(X\) therefore spends all but \(o(L_X)\)
of its counted steps alternating on \(1,2\), and the variance vanishes.

Conversely, the predecessor theorem gives a positive fraction of
convergent sources and, if a counterexample exists, a positive fraction
of nonconvergent sources. The first population has odd fraction
\(1/2+o(1)\). Every orbit in the second population stays at least three,
so its product of step ratios forces odd fraction at least
\[
 \frac1{\log_2(10/3)}-o(1)=0.5757166424\ldots-o(1).
\]
Those separated populations force a positive variance lower bound.

The deadline is essential. Through \(t\le\log_2X\) at dyadic cutoffs,
the exact parity coding already gives variance \(1/(4t)\), irrespective
of the fate of ordinary orbits. The new test lies beyond that coding
horizon. Proving collapse there would be a substantive source-wise
advance, not another consequence of short-word equidistribution.

## What a decisive next step would need to supply

For cycles, a result must control a particular exceptional least period
and its full denominator. Another additive distributional error that
dominates the mass of one integer necklace is insufficient. At a
lower-record type, it must also respect the absence of a contracting
split and the exact cancellation at full return.

For escape, one concrete sufficient target is a strictly positive
bounded computable function whose lower logarithmic defect rate is
less than one. The flux identity would then exclude every escaping
component. The existing approximate functions do not meet the required
positivity limit. Alternatively, a source-wise smaller-merger theorem
for every residual component minimum would close the induction route.
The finite-source variance criterion gives a third precise target:
control independent ordinary sources at a clock growing faster than
their binary coding horizon, strongly enough to prove a vanishing
subsequence of \(V_X\).

The proof obligations concern one fixed ordinary source, its unbounded
future and exact arithmetic. The sprint supplies stronger estimates,
formal finite mechanisms and several reasons that superficially similar
population statements do not discharge those obligations.
