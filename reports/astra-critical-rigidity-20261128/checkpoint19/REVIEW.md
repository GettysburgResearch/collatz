# Nineteenth coordinating mathematical review

This checkpoint adds eight proposed written notes, five exact finite control
programs and ten connected Lean theorem roots. The coordinator reconstructed
each proof, and both other mathematical lanes independently reviewed the new
analytic results. The strongest conclusions are the sharp full-denominator
rate for near-octave rational cycles, all-height sparse-target avoidance and
an explicit computable mask showing the sharp summability boundary.

These statements have different evidence scopes. The true finite arithmetic
modules are freshly compiled. The asymptotic arguments are written, with
their original inputs identified. Modified integer rules are explicitly
different from the genuine shortcut.

## Complete denominator: from one cell to the sharp exponent

[Chronological rank](../../../research/astra-critical-rigidity-20261128/cycles/NEAR_OCTAVE_CYCLE_DENOMINATORS.md)
uses the actual bi-infinite unfolded sequence
\(V_i=2^{E_i}x_i\) of a positive primitive rational cycle.
Let \(p\) be its odd period, \(A\) its division total,
\(P=p/\gcd(A,p)\), and \(r\) its minimum rational recurrence degree.
The complete reduced common denominator is \(q\).
The proof retains
\[
 P\le r\le p,\qquad r=p\text{ if }\gcd(A,p)=1,\qquad
 r\ge p/4\text{ if }\gcd(A,p)\text{ is a prime power}.
\]

The deweighted positive sequence has exact period \(p\).
Its positive zero Fourier mode forces the radical \(2^{A/p}\)
into every annihilator. For a prime-power factor of the sheet count,
an active Fourier character supplies the further degree.
Over the maximal abelian field the radical extension still has degree
at least \(P/2\): otherwise a real root of \(X^d-2\), \(d>2\),
would generate an abelian, hence normal, real field containing its
nonreal conjugates. The extension tower gives the stated lower bound.
The true clock and the irrationality estimate give
\(\log m=O(\log\min(P,m))\), so minimum height cannot become an
unaccounted exponential cost.

The first note obtains a near-linear lower bound for \(\log q\) up
to powers of \(\log D\), \(D=\min(r,m)\), and a much stronger fixed-width
denominator exponent as the width approaches two.
A sum collision at one actual base propagates backwards around the cycle
through the full ternary guard, forcing a rational annihilator of degree
less than \(r\). Thus every selected cell is a physical \(B_h\) set,
without any assumption on \(q\). Its forward code can run across
arbitrarily many genuine laps.

[All-cell coding](../../../research/astra-critical-rigidity-20261128/cycles/POOLED_CYCLIC_DENOMINATOR.md)
then uses every short chronological offset, with a separate true calendar
for each angular cell. The crucial physical estimate is
\[
 \sum_{t=i}^{i+s-1}\log_2(1+1/(3x_t))
 =\frac{s}{6m(\log2)^2}+O(\eta+m^{-\delta}),
 \qquad 0\le s\le m,
\]
uniformly in the base and all laps. Away from the small upper-sheet arc,
\(m\log_2(1+1/(3x_t))\) is the fixed bounded-variation function
\(2^{-\theta}/(3\log2)\).
Continued-fraction grids in blocks of length \(\sqrt m\), with the
actual \(O(1/m)\) drift retained, bound both this average and the
exceptional arc occupation. No Diophantine assertion is made about
the perturbed auxiliary slope used to assign cells.

[Sharp chronological rate](../../../research/astra-critical-rigidity-20261128/cycles/POOLED_CYCLIC_DENOMINATOR_RATE.md)
proves, for every fixed \(\alpha>\mu_0-1\),
\[
 \eta\ll(\log D)^{-\alpha},\quad D=\min(r,m)
 \quad\Longrightarrow\quad
 \liminf\frac{\log_3 q}{D}\ge1.
\]
The explicit choice \(D=\min(P,m)\) is also valid.
For coprime clocks with \(\liminf m/p\ge1\),
\(\log_3q/p\to1\); this is the maximal rate permitted by
\(q\mid 2^A-3^p\). The classical bound permits \(\alpha>4.116201\);
the separately audited logarithm input permits \(\alpha>2\).

The leading constant was checked separately from the earlier
logarithmic-loss argument. Take all offsets below \(D\) and a common
order \(h=\lceil\exp((\log D)^{(1+u)/2})\rceil\), where \(u>1\)
and the guard length is \((\log D)^u\).
In a cell of size \(K_j\), give each nonreference label any multiplicity
through \(\lfloor h/K_j\rfloor\), then pad with the reference.
Exact \(B_h\) decoding yields at least
\((1+\lfloor h/K_j\rfloor)^{K_j-1}\) different coordinate sums.
Therefore its active coordinate count is at least
\((1-o(1))(K_j-1)\), uniformly in cells.

At one date an active cell center belongs to one grid interval plus
\(o(1)\) of a grid interval. At most two cells qualify. This first gives
a coding horizon \(n\gg D\). A second cell requires the base angle to
lie in a union of only polylogarithmically many seam intervals of total
length \(o(1)\). Actual-window discrepancy, using \(\sqrt D\) blocks
and the already established \(n\gg D\), makes that exceptional fraction
\(o(1)\), uniformly even over arbitrarily many laps.
Hence the total active capacity is at most \((1+o(1))n\), while the
multiplicity count needs \((1-o(1))D\).
Subtracting \(\log h+\log m=o(D)\) from the full-denominator coding
horizon gives the leading constant one.

The exact controls include 3,221 genuine primitive rational cycles,
44 proper recurrence ranks, and 22 mixed six-sheet cases. Two larger
positive cycles have periods 41 and 306 and complete denominators of
59 and 476 bits. Every base and all chronological offsets are checked
in the pooled codes. The 105,132 padded-vector comparisons are finite
selected multiplicities across four views; they are not an exhaustive
enumeration of every multiset at the displayed large order.

## Avoidance across all high scales

[All high targets](../../../research/astra-critical-rigidity-20261128/literature/ALL_HIGH_TARGETS.md)
proves, for every possibly infinite deterministic
\(F\subset[R,\infty)\),
\[
 \Pr(\exists t\le\tau(U_X):T^tU_X\in F)
 \le C\sum_{i\ge0}
 \sqrt{\frac{|F\cap[2^iR,2^{i+1}R)|}{2^iR}}+o(1),
\]
uniformly as \(X,R\to\infty\) independently.
The entire high part of any actual forward orbit is an admissible
vanishing-cost mask, uniformly even when that orbit varies with the
cutoffs. The law of the entire infinite visited subset then has the
same component-mixture total-variation description.

One cannot simply sum the single-shell asymptotic error.
The proof instead uses the finite true-word square-root bound,
a native Bernoulli deadline estimate, and original quantitative
first-passage transport from the original source at each height
\(z_j=b^{\alpha^{-j}}\), \(\alpha=1001/1000\).
A reference path reaches below its next threshold within
\(\lfloor(\log z)/10\rfloor\) native dates except with probability
\(O(z^{-c})\). Its odd observations before that entrance lie in
\((z,z^2]\). Each fixed target shell is therefore charged only
\(O_\alpha(1)\) times. The transport errors
\(O((\log z_j)^{-c})\) are summable on the geometric logarithmic grid.

Each transported test includes the actual success mask and may include
a failed subsequent passage; no landing is replaced by a uniform
restart. Overshoots of several gates produce zero intervening tests.
Properness of the minimum is used once at a fixed bottom cutoff:
finitely many possible bottom landing values have finitely bounded
stopped paths. The source and target cutoffs tend to infinity before
that bottom cutoff is released. Even targets retain their last genuine
odd ancestor, with a summable geometric scale cost.

The coordinator checked this use of the exact quantitative frequency-zero
Transport statement in Leen's original manuscript, rather than relying
on a qualitative limit. The stationary square-root input remains
Weaver's original Paper146/v1, as credited in checkpoint eighteen.
The uniform located-interval orbit bound is also an original written
Leen input.

## A computable sparse mask that almost every true trajectory hits

[Sharp multiscale targets](../../../research/astra-critical-rigidity-20261128/literature/SHARP_MULTISCALE_TARGETS.md)
constructs one computable odd set \(F\) with
\[
 2^{-j}|F\cap[2^j,2^{j+1})|
 \ll(\log j)^{12}/j^2,
\]
yet almost every actual positive source hits it before the global minimum,
within \(O(\log n/(\log\log n)^2)\) native dates and at height
\(n^{1+o(1)}\).
All dyadic square-root \(\ell^q\) tail costs vanish for every \(q>1\).
Thus no such \(\ell^q\) norm can replace the \(\ell^1\) cost above,
even for a single fixed set and all source cutoffs.

This positive hitting construction uses elementary finite arithmetic and
concentration, without the recent asymptotic minimum or stationary
density inputs. At grade \(k\), a multiple of three, use all valuation
words of total \(4k/3\). There are
\(\binom{4k/3-1}{k-1}\) words. Their target residues occupy at most
\(Ck^{-1/2}2^{-2\lambda k}\) of the ternary grid, while an iid block
succeeds with probability at least
\(ck^{-1/2}2^{-\lambda k}\),
\(\lambda=\log_2 3-4/3\).
Residue collisions are allowed and counted.

The height-dependent depth is chosen using only finite rational
comparisons involving \(27/16\), not a numerical rounding assumption.
A bounded depth buffer makes the same test valid at every actual height
visited during the short prefix. Disjoint odd-gap blocks succeed with
probability tending to one. Their random native cost fits the supplied
prefix with exponentially small failure, and the complete parity
dictionary transfers the event to every interval containing at least
\(2^{20K}\) consecutive sources.

A second event through date \(16K\) provides a genuinely smaller later
state than every state through date \(K\). The additive correction is
bounded using the actual lower height \(n2^{-16K}\). Thus the early hit
strictly precedes the true global minimum without invoking a proper
minimum law. The extension with exponent \(0<a\le1\) has density
\(j^{-2a+o(1)}\) and hitting time \(j^{a+o(1)}\).
The matching lower power bound for possible observation time uses the
separately source-qualified all-height theorem.

Finite controls replay 13,182 tilted words with real residue collisions,
16,384 complete native parity words, 8,192 gate-test identities including
7,196 double overshoots, 51,787 true even ancestors, and 504 exact
height-depth comparisons. These check interfaces rather than infer
the asymptotic hitting probability from experiments.

## Finite time-window observables

[Ordinary collisions in time windows](../../../research/astra-critical-rigidity-20261128/ordinary/ORDINARY_COLLISIONS_IN_TIME_WINDOWS.md)
gives an unmarked finite-path escape detector.
At the central clock \(H=\mu\log X+\sigma u\sqrt{\log X}\), compare
the event that all \(k\) full traces through \(H\) intersect with the
event that their last \((\log X)^{1/4}\) observations intersect.
The events are nested; their probability difference tends to
\(\Phi(u)^k\sum_{C\ {\rm divergent}}d_C^k\).
No prescribed high shell, unknown component clock, or minimum date
is needed to compute the finite observable. The limiting value is not
evaluated.

For a terminal window of width
\(w\sigma\sqrt{\log X}\), divergent components contribute the probability
that independent normal minimum clocks have maximum at most \(u\)
and range at most \(w\); periodic components contribute \(\Phi(u)^k\).
The review checked common witnesses before minima using all-height
avoidance, bounded low witnesses, finite minimum truncation, and exact
arrival offsets on a shared injective tail.

Fixed-lag anchored tests also recover period-resolved basin powers:
\[
 b_k(t)=\sum_{C\ {\rm periodic}}d_C^k
                 \min(1,t/P_C)^{k-1}.
\]
Two successive differences, divided by
\(t^{k-1}-(t-1)^{k-1}\), recover the mass powers at exact period \(t\).
Gaussian anti-concentration removes divergent fixed-lag hits.
Finite controls separate 9,216 true ordinary pairs from 15,552 synthetic
injective-tail cases and 40,068 synthetic phase tuples.

## Bounded changes on one orbit and formal arithmetic

[One sparse divergent orbit](../../../research/astra-critical-rigidity-20261128/literature/ONE_SPARSE_DIVERGENT_ORBIT.md)
gives explicit computable modified maps with exact even halving and
all changes on one growing orbit of odd multiples of three.
The modified spine has only \(O(\log X)\) states through \(X\).
Every true predecessor of one of these ternary multiples lies on its
initial dyadic halving ray, so the entire incidental capture set has
only \(O((\log X)^2)\) elements.

One version preserves the complete true stopped-path law outside that
null set while diverting the whole genuine basin of one into divergence;
its largest additive change is four. A version preserving the known
one-two cycle uses changes of size at most two at an arbitrarily high
anchor, diverts its positive predecessor mass, and changes the stopped
path law by an arbitrarily small limiting mass. The Brownian and phase
statements use the identified original laws and the exact prefix
comparison. These are changed rules, not ordinary counterexamples.

[Unit changes on ternary multiples](../../../research/astra-critical-rigidity-20261128/literature/UNIT_PERTURBATION_ON_MULTIPLES_OF_THREE.md)
identifies a precise boundary: a trajectory of a rule differing by at
most one, with exact even halving, that stays in multiples of three has
its tail divided by three equal to a genuine shortcut orbit.
The sparse converse from a hypothetical divergent true orbit is stated
set-theoretically; membership in that orbit is not presumed decidable.
The dense explicit converse is computable.

Fresh central Lean 4.34.1 compilation and separate import audited:

- OneSparseOrbit: five new roots proving persistence of ternary units
  after an odd step, the complete dyadic predecessor classification,
  bounded growing spine edges, its actual modified iteration, and the
  exact shared-prefix theorem.
- SparseNativeTargets: five new roots proving exact native balance and
  endpoint decoding, the height/divisor target criterion, gap grade
  and clock, the last-gap ternary residue, and a finite cardinality
  bound on actual visiting sources by eligible target counts.

The 13 existing affine roots were also freshly compiled and audited.
Only Classical.choice, Quot.sound and propext occur.
The total is **113 packet-runner roots + three logarithm
specializations + one motif specialization = 117 distinct local
public theorem roots**. Cached pinned third-party objects were reused;
no cold Mathlib rebuild or independent LeanChecker run is claimed.

Five programs passed central normal and optimized replay with identical
output and stable sources, matching author receipts byte for byte.
The source manifest pins every selected source and replay dependency.
This checkpoint is published only after complete repository integrity
validation in a clean detached checkout; the preceding checkpoint's
validation receipt is included here.

No statement evaluates the finite-path escape limit, proves universal
descent, or excludes every cycle. The sharp cycle rate is at its
explicit shrinking-width and chronological-rank scope. The explicit
thin-mask hitting theorem concerns genuine trajectories; the growing
spines concern modified maps.
