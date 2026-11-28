# Checkpoint 08: strict finite-window improvement, Farey jumps, and ordinary critical moments

**The requested nine-hour pass continues. Collatz remains unresolved.**
The coordinator independently reconstructed the arguments described below.
This checkpoint contains the three phase-eight packets, the root rational
gap kernel, and the frozen machinery phase-nine strict-window theorem.
Later exploratory files are excluded. The principal structural result
rules out a finite controller attaining the unknown optimal Haar inverse
slope; it does not identify that slope with the entropy ceiling.

## Every finite window can be strictly improved

[STRICT_WINDOW_IMPROVEMENT.md](../../research/astra-nine-hour-20261128/machinery/phase9/STRICT_WINDOW_IMPROVEMENT.md)
proves, for the optimal mean gap \(c_W\) of the legal odd inverse MDP,
\[
 N=2\cdot3^{W-1},\quad n=24N+12,
 \qquad c_{W+n}\le c_W-3^{-n}/n\quad(W\ge2).
\]
Consequently the limiting mean \(L\) satisfies \(L<c_W\) at every finite
width. Weaver 127 proves convergence to the Haar optimum; Weaver 150
separates every finite width from the entropy ceiling. These inputs alone
do not exclude finite attainment of a lower unknown optimum. The new
argument addresses that separate question. The coordinator read both
primary theorem statements and the former's fixed-depth regeneration
proof. [Weaver 127, §12](https://rstation.ai/problems/collatz/papers/127) ·
[Weaver 150, §1](https://rstation.ai/problems/collatz/papers/150)

The finite Bellman equation has a deterministic minimizing selector with
all gaps at most \(N\), since two generates the ternary unit group.
Routing a maximum-potential state into the lower class containing a
minimum bounds the potential span by \(3(N-c_W)<3N\). In every coarse
state, choose the signed dyadic witness \(-2^{-k}\) with
\(N+2\le k\le2N+1\). An unrestricted first gap \(k+1\) reaches \(-1\),
then unit gaps keep it there. No capped first gap can start any route to
\(-1\) from this witness. The root
[NegativeAffineGap.lean](../../research/astra-nine-hour-20261128/phase8/NegativeAffineGap.lean)
proves that exclusion for the actual rational word map, with arbitrary
later positive gaps.

A legal baseline clears the dyadic denominator in at most \(k+1\) odd
edges. Its subsequent negative odd units have absolute value at least
five, because the route never reaches \(-1\). Telescoping
\(2^eM=3M'-1\ge(14/5)M'\) gives the stated cost excess, including the
entire Bellman span. The comparison survives on a complete fine cylinder
of conditional Haar mass \(3^{-n}\), containing positive ordinary lifts.
The control computes both plans from the initial \(W+n\) digits and
stores its choice for all \(n\) steps. Its unseen tail maps bijectively
to the tail above the terminal \(W\) digits. This preserves conditional
Haar tails at coarse block boundaries and permits repeated savings.
Finite occupation measures, or the larger-window Bellman inequality,
then convert the stored-plan controller into the claimed optimum bound.
The coordinator checked precisely which history is conditioned on; a
pointwise drift estimate along an arbitrary integer tail is not assumed.

### A certificate-dependent form

For any supplied width-\(W\) upper-cost certificate \(c\), action cap
\(R\), and bias span \(B\), set
\[
 M=R+6W+1,\qquad m=6M+3\lceil B\rceil+7.
\]
The same construction yields \(c_{W+m}\le c-3^{-m}/m\). Its witness
can be positive as a rational number. In every source cell an initial
gap in \([R+4,R+7]\), followed by \(W-1\) gaps in \([3,6]\), gives a
small positive word image of \(-1\). Every capped first inverse sends
that witness into \((-1/3,-1/4)\), which no positive-gap word image of
\(-1\) can occupy. The denominator and growth bounds then prove the
strict block saving. The root Lean kernel also proves this interval
entry and its word-image exclusion.

For Wren's imported width-22 certificate, the published physical gain
is \(\gamma=569908/10^6\), with physical bias span \(13.537636\).
Even-step drift gives \(R\le24\), and the odd-edge potential has span
less than 24. Thus \(M=157,m=1021\) gives
\[
 \Theta_\infty>\gamma+3^{-1021}/4084.
\]
Through Weaver's transfer theorem this includes the previous exact open
endpoint \((\log2-\gamma\log3)^{-1}\) among coefficients attained by
polynomially many terminating integers in every large octave. The
coordinator checked the published drift convention, numerical constants,
and transfer interface. The original multi-billion-state certificate
was not replayed. The displayed improvement is tiny; the structural
nonattainment theorem is the main result.
[Wren 154, Corollary 2 and Table 1](https://rstation.ai/problems/collatz/papers/154)

[AdaptiveBlockSaving.lean](../../research/astra-nine-hour-20261128/machinery/phase9/AdaptiveBlockSaving.lean)
checks fine-cell savings under uniform summation and stationary bias
cancellation. The complete MDP realization, signed denominator clearance,
and asymptotic interpretation remain written arguments. Finite controls
include true positive integer lifts and full uniform tail-reset laws for
plans depending on the highest observed input trit.

## An exact arithmetic staircase for cycle clocks

[DIGITAL_ROTATION.md](../../research/astra-nine-hour-20261128/cycles/phase8/DIGITAL_ROTATION.md)
defines the dyadically closed integer grid \(\Lambda_K\), upward rounded
tripling \(F_K\), and its order adjoint \(G_K\). If an ordinary positive
cycle has minimum \(m\), odd period \(p\), and total exponent \(A\), then
\[
                     \log_2 3<A/p\le\eta_{2m},
\]
where \(\eta_K\) is the common rational upward rotation clock. This holds
without a width or a count-coprimality hypothesis. Prefix counts have
zero discrepancy through integer test rays \(4m\), and their first
positive discrepancy is attained at \(4m+1\). Summation around a grid
orbit gives the clock comparison. If the physical cycle has odd width
below four, its clock equals the grid clock over every eligible octave.
Conversely, a periodic lower-grid orbit avoiding multiples of three and
four reconstructs a genuine odd cycle of width below four.

The new exact jump theorem is
\[
 \eta_K=a/q>\eta_{K+1}=a'/q'\quad\Longrightarrow\quad aq'-a'q=1,
\]
with both clocks reduced. Adding one resolution inserts exactly one
new dyadic ray. Sum the integer crossing differences between the two
periodic lifted orbits. The winding sum is the determinant. A positive
crossing must land at the single old successor and the single new ray;
injectivity on each periodic orbit permits at most one such pair, and
its crossing value is one. All other summands are nonpositive. The
coordinator checked octave normalization, least-period denominators,
and this one-pair argument. Every best upper rational approximation in
the denominator sense must therefore occur somewhere on the staircase.
An exceptional approximation by itself is not evidence of a physical
integer cycle.

[GridClock.lean](../../research/astra-nine-hour-20261128/cycles/phase8/GridClock.lean)
checks the prefix iteration, winding inequality, and true positive
exponent reconstruction from the stated floor/residue hypotheses.
[FareyClock.lean](../../research/astra-nine-hour-20261128/cycles/phase8/FareyClock.lean)
checks double-permutation summation and determinant one from the
one-pair crossing cap. The geometric cap and global staircase conclusions
are written proofs.

There is a precise limit to local averaging. For arbitrarily long
\(N\), genuine integer segments at \(K\asymp3^N\) realize every
admissible rounding-residual string of a fixed mechanical calendar.
Both all-zero and all-maximum strings occur through the information
horizon \(N=\log_3K+O(1)\). Their scaled correction averages approach
zero and twice the proposed uniform-digit coefficient. Compatible
bi-infinite local models retain the latter obstruction at all finite
residue precisions. The unresolved bound is a statement about complete
integer periodic orbits, not a finite-window martingale estimate.

A false common-support shortcut is explicitly rejected: at \(K=2\)
the upper and lower adjoints have distinct periodic representatives.
Their clocks agree in absolute value, but their separate digit bounds
cannot be combined on one orbit. Large exact plateau examples are
calibration, not an asymptotic theorem. Prior prescribed-schedule work
and the concurrent width-nine reconstruction are credited in the note.

## The ordinary integer critical moment is now explicit

[TILTED_ORDINARY_REPRESENTATIVE.md](../../research/astra-nine-hour-20261128/escape/phase8/TILTED_ORDINARY_REPRESENTATIVE.md)
uses the existing tilted Syracuse law \(\sigma\) with gap probabilities
\(3/4^e\). For its least positive odd representative \(r_j\bmod3^j\), put
\(X_j=3^j/r_j^2\). The full ordinary inverse trace gives
\[
 \mathbb E X_j^u=3^{(u-1)j}
 \sum_{x>0\text{ odd}:\ U^jx\in I_j}
 \frac{f_j(x)^2}{x^2}(U^jx)^{2(1-u)},
 \qquad f_j=\prod_{i<j}\frac{3U^ix}{3U^ix+1}.
\]
Every fixed source eventually satisfies the representative restriction.
A simple orbit has a uniformly positive limiting product, whereas a
cycle basin has product tending to zero. Thus
\[
 \lim_j\mathbb E X_j=\mathcal E
 =\sum_{x\text{ escaping, odd}}f_\infty(x)^2/x^2.
\]
All fractional moments below one decay exponentially, and \(X_j\to0\)
almost surely. Uniform integrability is therefore equivalent to absence
of every positive escaping orbit. The surviving first moment, if any,
is carried by explicitly exponentially rare events. The critical
entropy satisfies
\[
 \log(4/3)\mathcal E\le\liminf K_j/j
 \le\limsup K_j/j\le\log3\mathcal E,
 \qquad K_j=\mathbb E[X_j\log^+X_j].
\]
Even \(\liminf K_j/j=0\) is exactly a no-escape criterion. No such
bound is established here.

A subexponential moment at any order above one is much stronger: it is
equivalent to all positive sources entering a fixed finite collection
of cycles within a uniform \(O(\log n)\) native time. The coordinator
checked the forward and reverse implications, including the finite-cycle
minimum bound, simple first-entry product, and conversion from odd to
physical time. Known long terminating families already exclude a range
of high moment orders; their external stopping-time input is explicitly
cited and was read in the primary source. Weaver's original tilted law,
ordinary trace, and fixed-root quadratic bound are prior results.
[Weaver 9/v2, Proposition 11](https://rstation.ai/problems/collatz/papers/9) ·
[Weaver 127, Theorem 7 and Corollary 10](https://rstation.ai/problems/collatz/papers/127)

[SIZE_BIASED_CODING.md](../../research/astra-nine-hour-20261128/escape/phase8/SIZE_BIASED_CODING.md)
shows that the weighted conditional word entropy remains bounded.
The missing quantity is the tilted marginal relative entropy after
ordinary size bias. A signed control at the genuine fixed point \(-1\)
uses the same stationary law: all fractional moments disappear while a
normalized first moment survives. It does not assert a positive
counterexample or assume negative Collatz convergence.

[SUCCESSIVE_ROOT_POSTERIOR.md](../../research/astra-nine-hour-20261128/escape/phase8/SUCCESSIVE_ROOT_POSTERIOR.md)
proves bounded increasing posterior ratios along any hypothetical
escaping ray. The entire true reverse segment has posterior probability
tending to one uniformly in its additional length. Likelihood ratios
of higher-exponent alternative parents have a summable total budget.
Weaver's independent bounded conditional coding entropy implies the
same direction of summability for every coupling of stationary
marginals; singularity alone does not force an opposing budget at the
actual moving integers. The same posterior ratios distinguish entry to
one from escape or another cycle through a sharp growth threshold
\(4/3\). Entry to one also yields unbounded consecutive blocks in the
counted-fusion class, whereas an escaping source has a finite class.
The fixed-root lower row used for the former is a named prior input.

[TiltedTraceBounds.lean](../../research/astra-nine-hour-20261128/escape/phase8/TiltedTraceBounds.lean)
checks finite positive and negative product inequalities and true
forward exponential growth. The probability limits, moment equivalence,
and posterior statements remain separately reconstructed written proofs.

## Binary affine carriers and the full contracting boundary

[BIASED_BINARY_FUSION.md](../../research/astra-nine-hour-20261128/machinery/phase8/BIASED_BINARY_FUSION.md)
classifies affine overlap for the binary Collatz source with iid parity
bias \(\theta\ne1/2\). For \(g(x)=ax+b\), \(r=v_2(a)\), a nonzero common
part occurs exactly when
\[
       a=2^r3^k,\quad k\in\mathbb Z,
       \qquad b\in2^{\min(r,0)}\mathbb Z[1/3].
\]
On the union of aligned finite fusion cylinders the source-oriented
density is the constant
\((1-\theta)^r((1-\theta)/\theta)^k\); the rest is singular. Finite
cylinder likelihood is a nonnegative martingale. A positive finite
limit forces the integral odd-count difference eventually to be
constant, and equality of the future parities then identifies the
aligned states. Unequal slopes can agree at at most one point for
each word pair; the source law is nonatomic. Conversely the existing
canonical steering construction supplies a positive cylinder when the
algebraic conditions hold. The coordinator checked both the lattice
condition and the inversion needed for negative dyadic valuation.
[BinaryAffineLikelihood.lean](../../research/astra-nine-hour-20261128/machinery/phase8/BinaryAffineLikelihood.lean)
checks finite probability-ratio algebra, not martingale convergence.

[TWO_SIDED_AFFINE_RIGIDITY.md](../../research/astra-nine-hour-20261128/machinery/phase8/TWO_SIDED_AFFINE_RIGIDITY.md)
combines the binary future with the ternary past. For
\(\theta\ge\theta_*\), every rational affine map overlaps their product
exactly when it is one positive-gap word or its inverse; the shared
mass is the word probability. A genuinely reduced quotient with both
arms nonempty has incompatible terminal binary valuations. On a conull
set, all rational affine relations are therefore actual time shifts of
the bilateral model. This conull statement need not contain any
ordinary diagonal integer.

[TILTED_JOINT_FIBRES.md](../../research/astra-nine-hour-20261128/machinery/phase8/TILTED_JOINT_FIBRES.md)
adds the real past when the real drift contracts, namely
\(\theta<\log2/\log3\). The joint real/ternary coordinate recovers the
whole iid word. A direct lattice-coset count bounds residual prefix
entropy by \(O(\log n)\), while the stationary chain rule makes it
linear in the first-letter conditional entropy. This also extends the
positive 2,3 affine time-shift classification across all parameters;
for every biased parameter the binary result extends it to all
rational affine maps. The fair case outside the 2,3 group is not claimed.

The typical real conditional measure has exact dimension
\[
 \frac{(H_{\rm geom}-\log3)_+}{(\log2)/\theta-\log3}.
\]
The proof combines posterior prefix rates with lattice spacing at a
fixed total exponent, and uses an integrable real-tail bound to pass
between prefix mass and interval mass. The coordinator checked both
local-dimension inequalities and their restriction to good sets.
At a specified nonperiodic ordinary unit root, finite-depth conditioned
real laws instead concentrate onto the closed true first-hit correction
set, with an error bounded by a power of the least positive unit
ancestor. The additional unit trit is retained; no uniform ancestor
escape rate is assumed.

The broad boundary framework is prior work. The coordinator read
Brofferio's main theorem, the relevant Weaver 19/v2 ordinary-diagonal
and conditional-fibre statements, and the Feng–Hu projection-entropy
precedent before reviewing this explicit countable-gap treatment.
[Brofferio 2006](https://www.numdam.org/article/AIF_2006__56_2_499_0.pdf) ·
[Weaver 19/v2](https://rstation.ai/r/collatz/posts/33) ·
[Feng–Hu](https://arxiv.org/abs/1002.2036)

## Verification boundary

The strict fresh Lean replay and exact controls are recorded separately.
The replay covers every local declaration, including private helper
proofs, and permits only `propext`, `Classical.choice`, and `Quot.sound`.
It is not a fresh Mathlib build. Analytic external inputs and the written
infinite theorems are not promoted to kernel-checked results merely by
appearing next to a Lean file. The scientific-source manifest fixes the
reviewed snapshot; repository integrity is checked on a complete clean
checkout before publication and again at the exact published head.
