# Assessment of the three-hour full-proof pass

**28 November 2026. Collatz remains open.** The useful outcome is a
smaller full-proof target, an exact representation of that target on the
joint real/ternary stationary process, and quantitative control of a
positive rational reference process. We also identified concrete ordinary
controls that prevent transferring those reference estimates without an
additional arithmetic argument.

This assessment separates written deductions, source-qualified deductions,
local formal checks, and the first unsupported step. The record is in
[PR218](https://github.com/GettysburgResearch/collatz/pull/218); the
coordinator's [final review](../../reports/astra-full-proof-20261128/FINAL_REVIEW.md)
records the independently reconstructed interfaces and verification scope.

## 1. The most direct full-proof target

Use the actual shortcut map on positive integers,

\[
T(n)=
\begin{cases}
n/2,&n\ \text{even},\\
(3n+1)/2,&n\ \text{odd}.
\end{cases}
\]

Let \(Q_t(n)\) count odd departures before the physical date \(t\), let
\(\lambda=\log_2 3\), and set

\[
 M=\left\lfloor\frac{k}{1-\lambda/2}\right\rfloor,\qquad
 g\sim k^{3/5},\quad g\ \text{even}.
\]

All expectations in this section are over the original ordinary
integers \(1\le n\le2^k\). The sufficient statement is

\[
\boxed{\displaystyle
 \liminf_{k\to\infty}
 \frac{\mathbb E[Q_{M+g}(n)-Q_M(n)-g/2]}g\le0.}                 \tag{1}
\]

This one signed first moment would exclude both an additional cycle and
an escaping orbit. It requires neither an upper bound for every starting
integer nor convergence of the entire parity distribution.

Here is the shortest proof interface. Put
\(\beta=1/\log_2(10/3)\), \(b=\beta-1/2>0\),
\(W=\sqrt{k\log(k+2)}\), and \(x=T^M n\). A pointwise positive
product inequality gives
\[
 Q_{M+g}-Q_M-g/2
 \ge bg\,{\bf1}_{\{\tau_1>M+g\}}-\beta\log_2 x.
\]
Weaver's actual first-passage theorem lands the original source at a
polylogarithmic height within \(O_A(W)\) dates of \(M\), outside
\(O_A(k^{-A})\) of the population. Each positive step changes size
by a factor in \([1/2,2]\), so
\(\mathbb E\log_2 x=O_A(W+k^{1-A})\). Therefore
\[
 \mathbb E[Q_{M+g}-Q_M-g/2]
 \ge bg\,\Pr(\tau_1>M+g)-O_A(W+k^{1-A}).
\]
On a positive suffix the odd undivided multiplier is at most \(4\);
before visiting \(1\) it is at most \(10/3\). Their strict difference
supplies the gap. No estimate for the centered count at \(M\) is
needed for this direct suffix proof. Thus (1)
forces the proportion of sources not yet at \(1\) to vanish along a
subsequence. A positive counterexample has a bad forward odd ternary
unit, whose ordinary predecessors have positive lower density,
contradicting that conclusion.

The outside density theorem is used with its stated scope and
outsider-reported Lean provenance. The first-passage input is a written
outside theorem. The complete new first-moment deduction is written,
not locally formalized.
[Full proof and normalization](descent/FIRST_MOMENT.md) ·
[Outside density provenance](arithmetic/OUTSIDE_INPUTS.md) ·
[Coordinator reconstruction](../../reports/astra-full-proof-20261128/CHECKPOINT_04_REVIEW.md).

The target also has a particularly concrete form. If \(b_0(y)=y\bmod2\),
then

\[
 b_0(y)+b_0(Ty)-1
 ={\bf1}_{y\equiv3\ (4)}-{\bf1}_{y\equiv0\ (4)}.
\]

Pairing the \(g\) dates makes (1) an upper bound on a signed ordinary
endpoint flux. The standard pair \(1,2\) contributes zero. The finite
identity and its paired-clock sum are locally checked in
[EndpointFlux.lean](descent/EndpointFlux.lean). **The upper bound on
the original-source average is still open.**

## 2. A whole-source stationary representation with no accumulated fibre error

The most promising structural reformulation found by the coordinator
starts from a concurrent PR217 integer-window lemma. It preserves every
word, grade, endpoint, and original positive source simultaneously.

Let a length-\(h\) fair word have affine map
\(F_w(x)=3^{q(w)}2^{-h}x+B_w\). Act with this same word on an
independent seed \((R,Z)\), where \(R\ge0\) is real and
\(Z\in\mathbb Z_3\). Select positive integer endpoints \(y\) satisfying

\[
 F_w(Z)\equiv y\pmod{3^{q(w)}},\qquad
 0<y-F_w(R)\le3^{q(w)}2^{-h}N.                                  \tag{2}
\]

The selected word/endpoint pairs are in exact bijection with the
ordinary integers in the shifted interval
\(\lfloor R\rfloor+1,\ldots,\lfloor R\rfloor+N\).
The complete ternary congruence reconstructs an integer source; reverse
parity forces its actual binary itinerary. For any bounded payoff \(G\),
replacing the original interval by this simultaneous representation
therefore costs at most

\[
 \frac{2\|G\|_\infty}{N}\mathbb E\min(R,N).                       \tag{3}
\]

There is no factor counting grades or endpoints in (3).
With the jointly stationary seed and any \(0<\alpha<1\), it is
\(O_\alpha(\|G\|_\infty N^{-\alpha})\).

If \(N\le2^h\), at most one endpoint is selected for each word. The
selection event has conditional probability exactly \(N2^{-h}\),
even after fixing the entire seed. Its normalized conditional payoff
is the original-source statistic, with the error (3). Taking
\(h=M+g,\ N=2^k\), and \(G=(Q_h-Q_M-g/2)/g\) rewrites (1) as
one conditional stationary expectation.

This is useful because it removes a genuine accumulation of
pointwise errors. It leaves a difficult conditional correlation:
the word's odd count and the rare selection event are not independent.
The probability of selection is exponentially small. A stationary
marginal, an unconditional central limit theorem, or a polynomial
absolute error cannot settle the conditional sign.
[Exact proof, moment constant, and open conditional inequality](ACTUAL_SOURCE_STATIONARY_TRACE.md).

There is also a concrete reason not to seek a fresh fair suffix.
Outside a vanishing fraction, the actual state at date \(M\) lies
below \(2^{O(\sqrt{k\log k})}\). Its following \(g\) parity bits
are determined by that one integer, so their conditional entropy
is \(o(g)\), even though an unconditioned fair suffix has entropy
\(g\log2\). A zero signed mean is compatible with this sparse
support; independent fair continuation is not.
[Conditional suffix support](parity/CONDITIONAL_SUFFIX_SUPPORT.md).

Priority belongs to PR217 for the fixed-fibre window lemma; this packet's
extension is the simultaneous source injection and the single conditional
full-proof target. The external finite formal receipt for that earlier
lemma was not rebuilt by this pass.
At the closing review, PR217's later head also contained the whole-law
aggregation, a two-copy collision consumer, and the exact one-copy
normalization. That concurrent overlap is explicitly credited in our
note. Optimizing the displayed fractional-moment constant also gives
the sharper error \(O(\log N/N)\); the conditional sign remains open.

## 3. The positive rational reference process is now quantitatively controlled

For an integer source size \(N=2^k\), put
\[
 Kf(y)=\frac{{\bf1}_{y>1/2}}3
       \sum_{e\ge0}f\!\left(\frac{2^e(2y-1)}3\right).
\]

Starting uniformly from the positive mesh
\(u/3^r,\ 1\le u\le N3^r\), the integer endpoint at the formal
\(r\)-th odd departure has probability \(K^r f_N(y)\), where
\(f_N=N^{-1}{\bf1}_{(0,N]}\). This is an exact arithmetic partition,
including numerators divisible by \(3\); the formal date need not be
the first date at which the reduced state is integral.
[Mesh identity](parity/LITERAL_ENTRANCE_KERNEL.md).

The new killed version \(K_a\) retains only the starting and recorded
post-odd states at least \(a\). It retains the original normalization:
the lost mass is not redistributed. Write
\[
 r_*=\frac{k}{2-\log_2 3},\qquad r=r_*+h,\qquad 0<h=o(k).
\]
At every fixed or growing floor \(a\ge32\), a positive two-power
majorant proves
\[
 K_a^r f_{N,a}(y)
 \le C e^{-ch^2/k} y^{-1-u},
 \qquad u\asymp h/k.
                                                                    \tag{4}
\]
Consequently total survival is at most
\(Cu^{-1}a^{-u}e^{-ch^2/k}\).

The essential point is that the affine \(+1\) correction is absorbed
at a fixed floor. One uses
\(V_p(y)=y^{-p}+C_2y^{-3/2}\) and
\[
 K_a V_p\le\rho_p V_p,\qquad
 \rho_p=\frac{3^{p-1}}{2^p-1}.
\]
The auxiliary power has a strict uniform margin at \(y\ge32\);
\((\log\rho_p)'_{p=1}=-\log(4/3)\) supplies the critical date.
This avoids a loss growing like \(k/a\).

A separate elementary coupling improves total survival all the way
down to floor \(1\):
\[
 \sum_{y\ge1}K_1^r f_{N,1}(y)
 \le C e^{-ch^2/k}\qquad(\sqrt{k}\ll h=o(k)).                       \tag{5}
\]
The genuine rational numerator has enough binary precision for the
initial fair prefix. Its actual path is dominated by a fair real
affine process started at \(N\), with no assumed independence between
the numerator's size and its bits. After the critical contraction,
a killed drift for \(C_0+\sqrt{x}\) forces a visit below \(1\).
On the subcritical side \(r=r_*-h\), rational recorded-floor
survival tends to one at the corresponding moderate rate.
[Full elementary proofs and exact native flux](mass/ABSORBING_RATIONAL_FLOOR.md).

These are written all-scale estimates, independently reconstructed by
the coordinator and both other research lanes. They are not Lean
theorems in this packet.

### Why the reference bound does not already prove Collatz

Every positive ordinary integer stays at least \(1\) forever. Thus
the whole ordinary population has survival exactly one at floor \(1\),
while the genuine positive rational populations in (5) have survival
tending to zero. No departing edge or artificial symbolic process
is needed for this discrepancy.

For a union \(B\) of complete ordinary components lying above floor
\(a\), the exact comparison is
\[
 \frac{\#(B\cap[1,N])}{N}
 -\sum_{y\in B}K_a^r f_{N,a}(y)
 =
 \sum_{d=1}^r\sum_{y\in B}
 (3{\bf1}_{y\equiv2\ (3)}-1)K_a^d f_{N,a}(y).                    \tag{6}
\]
The remaining quantity is an actual signed ternary flux.
A hypothetical bad component lies above the verified finite core.
Its left side stays positive by predecessor density and (4).
An upper bound contradicting that positive mass would prove full
Collatz. **Such a bound is open.**

At floor \(1\), the full ordinary component mark already supplies
a concrete critical band with nonzero accumulated flux. The
[one-edge controls](mass/ONE_EDGE_ENTRANCE_CONTROL.md) additionally
show that known convergent predecessor cones with arbitrarily large
floors can lose reciprocal-scale mass through one real edge.
Any valid high-floor comparison must use the absence of such exits
and the arithmetic exclusion of the standard component.

## 4. The future-minimum obstruction is confined to intermediate widths

There is further source-qualified progress on the actual signed
comparison, rather than on the reference law alone.
For \(R\) odd departures define the positive correction product
\[
 W_R(x)=\prod_{j=1}^R\frac{3z_j}{3z_j+1},
\]
where \(z_j\) are the actual odd-departure inputs, including rational
ones. A word of \(r\) runs gives \(A_rx+B_r\); write \(Y=NA_r\).
The exact denominator increment is a sum over ordinary endpoints
\(B_r<y\le B_r+Y\), with signed trit
\(3{\bf1}_{y\equiv2\ (3)}-1\) and weight
\[
 \frac{y-B_r}{Yy}\,W_{R-r}(y).
\]
The prefix product cancels the dangerous inverse interval width:
the displayed nonnegative factor is at most \(1/y\).
An arbitrary intrinsic path mark can be retained.

The resulting microscopic bound is uniform over all denominator
levels together:
\[
 \sum_{r\le R}
 |\text{individual contributions with }Y\le\varepsilon|
 \ll\varepsilon(1+|\log\varepsilon|)^3.
\]
Its proof uses a uniform occupation bound for the log-slope walk and
Weaver's real anti-concentration estimate, with the full actual
word/endpoint dependence retained.

Now mark the entire trajectory as staying at least \(a\). The external
fixed-barrier estimate bounds the count of ordinary future survivors
through \(X\) by \(O_\theta(Xa^{-\theta})\), for
\(0<\theta<0.0500\). Weighted occupation then proves that **all
widths \(Y\le a/2\), summed over every level, cost \(o(1/a)\)**.
[Uniform proof and first-repeat extension](descent/SURVIVAL_WINDOWS.md).

The opposite tail can also be removed. Choose
\[
 k=\lceil a^\delta\rceil,\qquad 0<\delta<\theta/2,\qquad
 R=\lfloor r_*+v k^{3/5}\rfloor .
\]
For every fixed \(0<\epsilon<\delta\), the full signed contribution
from widths \(Y\ge\exp(a^\epsilon)\) is \(o(1/a)\).
For each fixed word, all prior states increase affinely with the
candidate ordinary endpoint. Thus its complete prefix floor becomes
one lower cutoff on the endpoint interval. At a short common clock,
large ordinary starts cannot yet have crossed the floor, so the
remaining future-floor mark is a genuine terminal-state test.
This is the specific setting in which the pinned PR215 signed
starting-trit estimate applies; it is not a theorem for arbitrary
history-dependent marks.
[Wide-width proof and source pin](descent/INTERMEDIATE_FLOOR_WIDTHS.md).

The killed rational estimate makes the final reference mass
\(o(1/a)\) at the same calibrated source size. A genuine large future
minimum \(a\) that is a ternary unit, however, has ordinary first-landing mass
\(\gg1/a\). Therefore any escaping orbit would force that signed
mass into
\[
                 L_a\le Y<\exp(a^\epsilon),\qquad
 L_a=\frac{3a+1}{2}\exp(-R/(3a))=(3/2-o(1))a.                   \tag{7}
\]
The exact lower support is stronger than the all-horizon small-width
estimate at this calibrated horizon. The last odd input is
\((2y-1)/3\ge a\), while
\(Y=NA_r\ge A_rx=yW_r\ge y\exp(-R/(3a))\). Thus the contribution
below \(L_a\) is identically empty. This version of the two-tail
localization needs no stationary anti-concentration argument on
the lower side; the uniform all-horizon bound remains a separate result.
An escaping trajectory supplies arbitrarily large future minima.
A single additional cycle supplies one fixed minimum. The
asymptotic statement (7) alone does not eliminate that cycle.

There is a separate finite all-fates test: stop the correction
product at the first repeated state and multiply by
\({\bf1}_{\tau_1>\sigma_R}\). It retains a uniform positive weight
on every bad ordinary trajectory, including the first lap of an
additional cycle, while its rational reference mean is
\(O(\exp(-c h^2/k))\) when \(R=r_*+h\) and
\(\sqrt{k}\ll h=o(k)\). The latter estimate has an elementary
proof from the actual numerator's fair binary prefix; it does
not need the recursive rational entrance clock or real
anti-concentration input.
The comparison for that test remains open. Its all-fates version
does not require an oracle for the infinite future.
An alternative elementary bound gives every bad ordinary source
weight at least \((2R+1)^{-1/6}\), by summing the reciprocals of
distinct odd departure states. Thus a vanishing native mean after
multiplication by \(R^{1/6}\) is a full-proof sufficient condition
using only this elementary path bound and the qualified predecessor
density theorem. At the closing review we also included Weaver's
elementary distinct-orbit packing proof: one orbit has
\(O(Y^\eta)\) distinct states through \(Y\), with
\(\eta=H_2(3/5)<1\). Its reciprocal sum is uniformly bounded,
so the stronger constant lower bound follows within the packet
without a finite verification floor. This finite full-proof consumer
needs the separate positive-predecessor theorem, but no additional
analytic mixing hypothesis for either of its two weight bounds.
[Clock-height separation](descent/CLOCK_HEIGHT_MARK.md) ·
[Repeat-stopped finite consumer](descent/SURVIVAL_WINDOWS.md) ·
[Elementary packing and actual native boundary](mass/REPEAT_STOPPED_NATIVE_BOUNDARY.md).

Two closing identities expose what the failed final approaches leave.
Pairing the same reduced rational origin across denominators leaves a
geometrically discounted downward-minus-upward width current.
An eventual upward crossing on that same origin does not cancel its
earlier downward crossing; the actual floor-one system carries
asymptotic current one. A successful comparison must relate different
origins or use additional arithmetic about their crossings.

For the repeat-stopped product's native limit \(L\), the exact
one-step equation is \(L(n)-c(n)L(Tn)=g(n)\). Its source \(g\) is
supported precisely on nonstandard cycle vertices. Iteration leaves
a positive terminal weight on escape and the explicit cycle charge
on an additional cycle, while the entire component of \(1\)
contributes zero. The accompanying Abel identity preserves these
terms. Neither positive telescoping nor scalar stationary smoothing
has removed them.
[Same-origin width current](descent/INTERMEDIATE_FLOOR_WIDTHS.md) ·
[Native cycle charge and escape boundary](mass/REPEAT_STOPPED_NATIVE_BOUNDARY.md).

## 5. Ranked directions for the next full-proof dispatch

The first two are different attacks on the same sufficient statistic;
they should not be counted as independent mathematical progress.

| Priority | Load-bearing target | What would complete the argument | Principal obstacle now exposed |
|---|---|---|---|
| 1 | Signed native parity mean | Prove (1), even along one unbounded sequence of source sizes | Actual positive endpoint correlations after the critical clock |
| 2 | Full real/ternary conditional trace | Prove the sign of the single conditional statistic defined by (2) | Rare-event normalization and all growing conductors; the grade must stay coupled to the event |
| 3 | Complete-component killed-floor comparison | Bound the accumulated native trit flux in (6), or the finite first-repeat test | Real ordinary controls retain critical flux; future minima localize escape to the intermediate widths (7) |
| 4 | Ordinary first-hit record normalization | Prove \(L(1)=1+E(1)\) in the retained harmonic ledger | The unresolved mass is a positive sum over actual first-hit records, not the exponentially small error term |
| 5 | All-rank ordinary descent from an upper certificate | Produce a smaller ordinary bad source or a genuine merger from every surviving negative release | Repeating the known upper cycle evolves the original lower Collatz trajectory and never removes its negative chart |

The record route has a complete signed calendar:
late harmonic deaths, up to exponential error, occur at dates
\(4q+1\) and are indexed by actual first-hit paths to \(1\).
The finite coefficient \(a_q\) has bounded height and length, and
\[
 J_\infty=1+E(1)-L(1).
\]
The missing normalization is the entire remaining mass problem.
Computing more coefficients without a uniform tail or a same-source
loss theorem would not close it.
[Record flux](mass/RECORD_FLUX.md).

The descent route now treats upper certificates of arbitrary odd
rank. Nonnegative signed release gives eventual descent on each
fixed certificate row. Negative release persists under every
appended upper lap, and its exact recurrence is the original
ordinary lower trajectory. The earlier reduction turns a hypothetical
counterexample into a canonical bad source \(z\) with \(3z\)
convergent; every such fixed source enters the negative chart
after enough padding of its upper certificate. A new merger or
arithmetic ordering is needed beyond it.
[All-rank shadow and persistence proof](descent/UPPER_CERTIFICATE_SHADOW.md) ·
[Internal-prefix criterion](descent/INTERNAL_PREFIX.md).

## 6. Evidence and claims deliberately not made

Eight local Lean modules were rebuilt from a fresh temporary object
directory with Lean 4.34.1 and warnings as errors. They print 24
audited theorem roots. The roots use only the displayed standard
axioms, or subsets of them. A ninth new module, SignedDeathClock,
has a separate agent-produced local compile with its two pinned
PR200 parents. The coordinator did not represent that ninth module
as part of the eight-module fresh replay.
[Eight-module receipt](../../reports/astra-full-proof-20261128/ALL_LOCAL_LEAN.json) ·
[Separate death-clock receipt](mass/signed_death_lean.json).

Those files verify finite identities, conditional consumers, specific
arithmetic controls, and the stated death-clock interface. They do
not formalize the new analytic estimates in Sections 1–4.
The rational denominator-191 module checks its specified finite range
and one 40-step, 25-odd lap; it is not a convergence theorem for all
inputs of that map.

The retained outside Mazur and Lau density statements have
**outsider-reported Lean evidence and were not rebuilt here**.
The optional natural-mean corollary uses Valbuena's fixed-target
natural-density existence theorem, with the same explicit
outsider-reported status and no local rebuild.
The external fixed-barrier result distinguishes its written
assembly from the reported Lean checks of underlying parameter
lemmas. Weaver's first-passage and real anti-concentration arguments,
and the pinned PR215 transport theorem, are used as written
source-qualified inputs. Outside finite-verification inputs to
simple-path bounds were not rerun here.

Two purported full-proof imports were inspected at their actual
statements. One asserts a false bounded certificate as a project
axiom; the other terminal statement does not express reachability
and has a contradictory auxiliary bound. Our local Lean checks
refute the specific certificates independently. We do not claim
the outside projects failed to compile, and we do not use their
purported full conclusions.
[Exact outside-source scope](arithmetic/OUTSIDE_INPUTS.md).

The finite arithmetic checks support their explicitly enumerated
ranges. The clean-checkout validator checks repository integrity.
Neither is being used as evidence for the unresolved asymptotic
signs. The next useful success must settle one of the load-bearing
estimates above on original positive integers, with its actual
normalization and universal quantifiers intact.
