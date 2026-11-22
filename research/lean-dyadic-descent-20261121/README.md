# Forced-band descent, coefficient escape, and invariant labels

**Full Collatz remains OPEN.** This packet builds on PR173 at
`fa0c9e2a2851e6324391e39c17afcb5913185aec` and proves unbounded families of
actual marked-to-marked descents in Lean. It does not assume convergence of
every marked input. PR182 contains the new work and is stacked on PR173.

The map is the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

For `d = floor(log₂ n)`, PR173 marks the odd integers satisfying
`(d+1)(n-2^d) <= 70*2^d`. Its proved bounded-visit theorem makes the first
positive marked-return map `R` total. Its `collatz_iff_return_descent` says
that full Collatz is equivalent to eventual strict descent under `R` for
**every** marked input above one. These are imported results, not new claims.

## Continued attacks: polynomial rigidity and canonical-source occupation

The [continued synthesis](CONTINUED_SYNTHESIS.md) builds on the published
literature checkpoint and the newly refreshed PR176/PR185 sources. It adds
two positive written deductions and 22 audited Lean interface statements.

[INVARIANT_CORRELATION.md](INVARIANT_CORRELATION.md) extends ordinary-label
decorrelation to every fixed real polynomial phase, with correct centering
for rational phases. One positive approximation gap works over all finite
degrees and coefficients. The polynomial-phase Besicovitch class is strictly
larger than the earlier linear class; membership of an actual basin remains
unproved. An explicit zero-entropy control now satisfies doubling exactly,
while its averaged shortcut defect vanishes and its distance from every
`[0,1]`-valued model with an ordinary mean remains one half.

[HARMONIC_CAPTURE_BRIDGE.md](HARMONIC_CAPTURE_BRIDGE.md) computes the entire
Green potential of the unchanged canonical source seed under actual
ordinary transport, including time zero and source collisions. It gives a
normalized occupation bound and a summable weighted space-time collision
budget. The spatial weight and the whole-predecessor floor are retained;
neither moving-root contact timing nor unweighted absorption is inferred.

[CANONICAL_ESCAPE_LABEL.md](CANONICAL_ESCAPE_LABEL.md) joins the two lanes:
the harmonic construction gives a bounded ordinary invariant label positive
on escapes and zero on eventual cycles. The polynomial gap extends to any
bounded complex invariant label, so polynomial-phase approximation of this
specific function would exclude escapes. Its approximation remains unproved;
nontrivial cycles remain a separate obligation.

[PolynomialLift.lean](PolynomialLift.lean) checks the all-degree affine
substitution and commutator interface. [HarmonicCapture.lean](HarmonicCapture.lean)
checks the seed identity, finite and infinite Green bounds, and collision
series core under explicit hypotheses. The measurable and actual-kernel
applications remain separately reviewed written mathematics. Use
[replay_continued.py](replay_continued.py) for their fresh build and complete
public-theorem audit; actual evidence is in the
[continued report](../../reports/2026-11-21-dyadic-descent/continued/README.md).

## Earlier literature continuation: the ordinary-label bridge

The [new synthesis](LITERATURE_SYNTHESIS.md) connects the literature to the
remaining ordinary-source obligations. Its strongest positive result is a
source-qualified written rigidity theorem, separate from the Lean modules:
every ordinary Boolean label satisfying `f(Tn)=f(n)` has logarithmic cancellation
against each fixed nonconstant real exponential. A nonconstant Boolean
label stays one fixed positive distance from every trigonometric-polynomial
approximation, uniformly over all real frequencies. Thus qualitative
Besicovitch almost-periodicity of the basin-of-one indicator would force
full convergence under the retained analytic inputs. Such approximations
have not been constructed.

[LITERATURE_RIGIDITY_BRIDGE.md](LITERATURE_RIGIDITY_BRIDGE.md) gives the full
proof through a compact affine system, exact ordinary branch changes, and
the earlier stationary-density FLOOR and logarithmic-population LOG inputs.
It does not use the newer joint-clock natural-density claim, does not claim
existence of the label's logarithmic mean, and does not evaluate an arbitrary
almost-everywhere stationary density at ordinary integers. Its explicit
zero-entropy control shows why low complexity and approximate invariance
alone cannot supply the missing almost-periodic regularity.

[AffineRigidity.lean](AffineRigidity.lean) checks the finite harmonic,
algebraic translation and continuous-density interfaces used by that
argument. It keeps genuine group division and all topological hypotheses;
it does not formalize the entire measure-theoretic proof.

The certificate attack yields a sharp structural obstruction in
[LiteratureCertificate.lean](LiteratureCertificate.lean): for supplied
complete tails rooted at `729j+7`, every smaller-rank child retaining that
tail, with arbitrary prefix length and initial even run, has source
`S'<=13824j+130` while the parent is `S=15552j+148`. The sharp comparison is
`9S'+14<=8S`. An explicit unbounded fully certified family also defeats
every fixed direct forward-lookahead budget for this suffix-preserving
strategy. Its large-gap suffix, changing source/target, and distinction from
asymmetric mergers are stated in the
[complete scope note](LITERATURE_CERTIFICATE_BRIDGE.md).

The [coefficient literature audit](LITERATURE_COEFFICIENT_BRIDGE.md) records
which candidate estimates were already known and why their density-one
quantifiers do not prove a pointwise stopping theorem. The
[late source ledger](LITERATURE_SOURCES.json) reconciles the branches updated
after the preceding whole-repository snapshot without extending any review
verdict to an unread claim.

Use [replay_literature.py](replay_literature.py) for a fresh build of the
three pinned prerequisites, both new modules and their complete public
statement audit. Actual execution and written-review scopes are in the
[literature-round report](../../reports/2026-11-21-dyadic-descent/literature/README.md).

## Whole-repository reassessment: finite counts and complete certificates

The [broader synthesis](WHOLE_REPO_SYNTHESIS.md) and
[complete 145-PR metadata inventory](WHOLE_REPO_INVENTORY.json) step outside
the recent band families and reconnect the older coefficient, rank, mass,
ordinary-extraction and cycle programs. The inventory is not a claim of a
fresh line-by-line proof review of every branch. Two concrete developments
result, in three new Lean modules.

**An unconditional finite coefficient alternative.** Put
`C_t(n)=3^(oddCount t n)/2^t`. For every ordinary source `n` and `B>=1`, set

\[
k=70(\lfloor\log_2B\rfloor+3),\quad M=2^k,\quad
N=n+M+1,\quad H=6B^2(n+N)+1.
\]

[CoefficientPeaks.lean](CoefficientPeaks.lean) proves

\[
\exists t\le H:\qquad C_t(n)<1\quad\text{or}\quad C_t(n)>B.
\]

It also proves
`H<=12*B^2*n+6*2^210*B^72+6*B^2+1`. The observation time is explicit and
coarse. [CoefficientCounting.lean](CoefficientCounting.lean) supplies the
exact residue moment and packing estimate; the dynamics module proves its
own finite injectivity from the provisional coefficient strip. No global
nonperiodicity or random-parity premise is assumed. The older orbit-Mellin
work already proves qualitative coefficient escape; the
[new note](COEFFICIENT_PEAKS.md) credits that overlap. An upper exit remains
possible, so this is not universal coefficient stopping.

**A further complete-certificate rank decrease.**
[CertificateBoundary.lean](CertificateBoundary.lean) treats a guarded part
of PR177's remaining initial-even-run-two/first-odd-gap-four case. From a
supplied complete certificate for `q=4p+1` beginning with gap four, it
constructs a complete child source `S'=8z` with `S'>=4q+4`. Every old target
up to `2*(4q)+1` fits unchanged inside the child's interval. The same grade
comparison removes grade eight and inserts only grades at most seven,
preserving the literal arbitrary suffix. The
[precise statement](CERTIFICATE_BOUNDARY.md) retains all four guards on `p`
and the lower-rank induction hypothesis. The source certificate may grow
while its rank decreases; this is not ordinary descent of the target.

**A separate analytic audit.**
[PREDECESSOR_POPULATION_AUDIT.md](PREDECESSOR_POPULATION_AUDIT.md)
independently reconstructs PR180's written joint-clock implication to
`cX/a` actual predecessor populations. It authenticates the source bytes
and checks the exact primary renewal estimate, weighted counting norm,
complete-clock convolution and duplicate removal. Its scope is an audited
written derivation, not a Lean theorem. No checked theorem in this packet
imports that analytic claim as an axiom.

**A written qualitative regularity theorem.**
[PROFINITE_LABEL_RIGIDITY.md](PROFINITE_LABEL_RIGIDITY.md) shows that a
nonconstant ordinary invariant Boolean label has one positive logarithmic
mean error floor against every `[0,1]`-valued periodic function of period
`2^a*3^b`, independent of the conductor. Thus qualitative mean approximation
would already force constancy; no approximation rate is required. This
separate measure-theoretic argument uses the earlier marginal atom floor
and logarithmic population, without the later joint-clock claim. It is a
written, source-qualified result, outside the Lean count. Constructing such
approximants for the basin-of-one label remains open.

Use [replay_reassessment.py](replay_reassessment.py) for a fresh build of
the two pinned inputs, all three new modules and their complete public
theorem audit. The [reassessment report](../../reports/2026-11-21-dyadic-descent/reassessment/README.md)
records the actual checks separately from the preceding continuation.

## Earlier continuation: three attacks on universal coverage

The continuation develops three separate routes, with their actual ordinary
sources and their remaining coverage obligations kept explicit. The detailed
proof packets are [exponent coverage](EXPONENT_COVERAGE.md),
[temporal density](TEMPORAL_DENSITY.md), and
[original-source mergers](MERGER_DISPATCH.md).

### A. Growing certificate budgets with a fixed power saving

[ExponentCoverage.lean](ExponentCoverage.lean) strengthens the earlier
selected-exponent construction. There are arbitrarily large `q` such that,
with `H=floor(q/10)`, **every** supplied odd-offset certificate
`T^h(r)=1`, `h<=H`, works simultaneously at **every** exponent in

\[
2q+H+1\le d\le12q-H.
\]

For `n=2^d+r`, the result supplies a positive actual marked-return index `k`
and a marked endpoint `y=R^k(n)` with

\[
y<n,\qquad y^{120}<n^{119},\qquad
\operatorname{Basin}(n)\ \Longleftrightarrow\ \operatorname{Basin}(y).
\]

The certificate budget grows with the chosen scale. No separate fixed
offset-size budget is imposed: the supplied certificate itself gives
`r<=2^h<=2^H`. A reusable coefficient guard permits an exponentially growing
saving factor `2^(H+1)`; elementary integer powers then give the displayed
source-scale saving. The proof uses the same positive approximants already
constructed in this packet, without a new Diophantine assumption.

On the offset-one ray, whole blocks `2q+1<=d<=12q` have this power saving.
The exact counting theorem consequently supplies arbitrarily large cutoffs
`M` for which **at least `5M/6` positive exponents `d<=M`** have such a
marked-return certificate. This is an upper-density statement about
exponents, not a density statement about all natural starting values, and
not a claim that every cutoff has that proportion.

Two gaps remain. The selected blocks are not proved to cover every prescribed
exponent. Also, a forced-band offset can be of order `n/log n`, whereas these
growing-budget blocks still require a short supplied certificate and imply
`r^21<n`. An arbitrary marked source does not automatically meet that budget.

### B. Uniform finite temporal bounds

[AnalyticCoupling.lean](AnalyticCoupling.lean) and
[TemporalDensity.lean](TemporalDensity.lean) apply to one actual odd orbit
`x_j`, assuming only that its first `N` observed states are distinct. They
prove the exact harmonic budget

\[
\sum_{j<N}\frac1{x_j}\le H_N\le1+\log N,
\]

and use it in the actual height/valuation identity and in a finite Fourier
estimate. For every positive integer frequency `a`,

\[
|1-e^{2\pi i a\log_2 3}|
\left|\sum_{j<N}e^{2\pi i a\log_2x_j}\right|
\le2+4\pi a H_N.
\]

Thus the normalized phase average is `O_a(log N/N)`, with no assumed escape
rate or random-residue model. The full valuation identity is retained too:
if the endpoint is at least the starting value, the total halving exponent
is at most `N log_2 3+H_N`.

Combining the finite estimate with the unchanged PR178 trigonometric kernel
gives a uniform temporal-count bound. If `V_n(N)` counts marked states among
the first `N` odd states, then

\[
(\lfloor\log_2N\rfloor+1)V_n(N)\le196608\,N.
\]

The constant is deliberately conservative; the parameterized finite
inequality retains sharper information. The endpoint at time `N` may repeat
an earlier value. For an infinite orbit the all-horizon result retains the
nonrepetition hypothesis, which actual unboundedness supplies by determinism.

Sparse temporal occupation does not eliminate a surviving source or remove
its transported mass. These estimates are compatible with PR173's infinitely
many forced visits. That missing coupling is not assumed.

### C. Smaller partners and four residual first gaps

[MergerDispatch.lean](MergerDispatch.lean) works directly with the original
ordinary source. Factor `9n+1=2^A u`, with `u` odd. Exact forward identities
give descent for all even `A>=4` and all odd `A>=9`, in addition to the
elementary cases `A=0,1`.

For odd `A=2b+3>=9`, the explicit positive partner

\[
w=2\,3^b u+1<n
\]

satisfies `w=T^(2b+2)(n)` and `T(w)=T^(2b+3)(n)`. The smaller partner is
itself an earlier forward iterate. Consequently every original source `n>1`
whose orbit never drops below `n` must satisfy

\[
v_2(9n+1)\in\{2,3,5,7\}.
\]

This applies in particular to a least nonconvergent source and to the minimum
of a nontrivial cycle. It cannot be applied indiscriminately to all later
points of an orbit: a larger later value can descend locally while staying
above the original floor. The four remaining classes are still unbounded
ordinary families; a complete lower-source selector for them is not supplied.

### An exact obstruction to the simplest offset induction

The finite theorem `first_marked_offset_above_source` checks an actual
ordinary source

\[
n=2^{601}-1.
\]

Its first marked shortcut iterate occurs at clock seven:

\[
x=T^7(n)=3^7 2^{594}-1
 =2^{605}+\bigl(139\,2^{594}-1\bigr).
\]

The canonical offset at that first marked hit is **larger than the original
source**, since

\[
\bigl(139\,2^{594}-1\bigr)-n=11\,2^{594}>0.
\]

The same kernel check verifies that none of clocks zero through six is
marked and that all states through clock seven are odd. Thus the example
also uses seven actual odd steps. An offset smaller than a later marked
value need not be smaller than the original induction source. This is an
obstruction to that proof shortcut, not a nonconvergent Collatz orbit.

### Reproduction and provenance

`SOURCES.json` pins the unchanged PR173 imports and the three byte-identical
PR178 vendor modules. `replay_continuation.py` compiles the continuation with
warnings treated as errors and audits every new public theorem. Its optional
baseline reuse mode embeds the actual earlier successful receipt and checks
the unchanged source hashes and compiler pins. Execution evidence is kept in
the [continuation report](../../reports/2026-11-21-dyadic-descent/continuation/README.md).

The previous checkpoint's results and their original evidence follow below.

## 1. Main new theorem: arbitrary marked-return contraction

For every natural factor `C` and lower bound `N`, there are natural numbers
`d,y,k` such that

\[
\begin{gathered}
n=2^d+1>N,\qquad n\text{ and }y\text{ are marked},\\
k>0,\qquad R^k(n)=y,\qquad y<n,\qquad Cy<n.
\end{gathered}
\]

This is `power_plus_one_arbitrarily_strong` in
[InfiniteDescent.lean](InfiniteDescent.lean). It has no unresolved convergence
premise. In particular, these are arbitrarily strong contractions on an
unbounded set of actual positive ordinary inputs, not finite parity words or
changing finite witnesses for an imagined infinite orbit.

The more general theorem `arbitrarily_strong_certified_offset_descents` fixes
any **odd** offset `r` with a supplied finite certificate that `r` reaches one.
For every `C,N` it supplies the same conclusion with `n=2^d+r`. It also proves
`Basin n ↔ Basin y` through the actual ordinary path. The offset is fixed
before the exponent is selected.

The result is about a later marked return. It neither claims `k=1` nor
convergence of the selected lifted input. PR173's arbitrary first-return
expansions and this result's arbitrary later contractions concern different
quantifiers and are compatible.

### How the proof obtains the marked contraction

Let a supplied offset certificate have length `h` and `p` odd inputs:
`T^h(r)=1`. Appending `s` copies of the actual two-step cycle `1→2→1` gives
`h+2s` clocks and `p+s` odd inputs. Exact high-bit transport then proves

\[
T^{h+2s}(2^{h+2s+1}+r)=2\,3^{p+s}+1.\tag{1}
\]

Write `q=p+s` and `alpha=log₂3`. The new one-sided approximation theorem
constructs arbitrarily large `q` and integers `a` with

\[
0<q\alpha-a<\frac2q.\tag{2}
\]

The positive side matters: the endpoint must lie above a power of two.
The proof does not assume any bound on the continued-fraction coefficients
of `alpha`. Take a coprime rational grid `A/Q` from PR173 and choose
`1<=j<Q` with `Aj=1+Qb`. If `eta=Q alpha-A`, then

\[
Q(j\alpha-b)=1+j\eta\in(0,2).
\]

Thus `0<j alpha-b<2/Q<2/j`. PR173's integer-power separation bound, applied
twice, forces these selected `j` to be arbitrarily large. This is a finite
ordinary modular argument at every selected scale.

For `y=2*3^q+1`, the additional logarithmic correction is at most `1/q`.
Therefore its phase above the integer `a+1` is at most `3/q`. Its number of
binary digits is at most `5q`; the product is at most `15`, inside the already
proved phase-to-section test with constant `35`. Consequently `y` is marked.

The source exponent is `d=h+2(q-p)+1`. As `q` increases, this source is also
marked: `r` is fixed while `2^d/(d+1)` grows. The endpoint-to-source size
ratio is governed by `(3/4)^q` times a constant depending on the original
certificate. The Lean proof uses elementary integer power inequalities,
including `3^5<2^8`, to repay that constant and any prescribed factor `C`.
Finally, PR173's `captures` theorem places (1)'s marked endpoint in the
actual first-return dynamics and the strict size drop forces its return
index to be positive.

## 2. Exact finite certificates and explicit exponent windows

[OffsetDescent.lean](OffsetDescent.lean) proves the counted transport identity

\[
T^t(2^t q+r)=3^{p(t,r)}q+T^t(r).
\]

For a contracting prefix `3^p<2^t` and `q>0`, strict descent is equivalent to

\[
q\ge1+\left\lfloor
\frac{\max(T^t(r)-r,0)}{2^t-3^p}
\right\rfloor.\tag{3}
\]

The finite checker is proved both sound and complete for the actual lifted
descent. An accepted positive quotient certifies all larger quotients.
In particular, an actual descent of `r` at clock `t` certifies ordinary
descent of every `2^d+r` with `d>=t`. This alone does not certify a marked
endpoint; the following result adds that condition.

[MarkedOffsetReturn.lean](MarkedOffsetReturn.lean) checks source and endpoint
band membership by integer inequalities. If `T^t(r)=1`, `q=p(t,r)+s`,
`d=t+2s+e`, and `e>0`, its endpoint is `3^q*2^e+1`. With
`2^a<=3^q<2^(a+1)`, the sufficient endpoint guard is

\[
(a+e+1)(3^q-2^a+1)\le70\,2^a.\tag{4}
\]

Together with the explicit source-width and coefficient guards, (4) yields
an actual positive marked-return index, strict descent, and basin equivalence.
The width guard is sufficient and conservative; only (3)'s quotient threshold
is advertised as exact.

Three integer certificates give an explicit instance:

| `q` | Binary exponent `a` of `3^q` | Ordinary clock | Covered source exponents `d` |
|---:|---:|---:|---:|
| 1 | 1 | 2 | 3 through 70 |
| 12 | 19 | 24 | 25 through 5,134 |
| 665 | 1,054 | 1,330 | 1,331 through 1,603,754 |

The intervals overlap. The single kernel-checked theorem
`power_plus_one_overlapping_windows` therefore gives a smaller marked return
for every `2^d+1` with `3<=d<=1,603,754`. The numbers `2^d+1` are never
enumerated by this proof; the integer certificate controls the entire
exponent interval. This is an illustration of the general mechanism, not a
claim that a finite exponent bound settles the remaining inputs.

[search_windows.py](search_windows.py) discovers such certificates using exact
integer arithmetic. Its search bounds and selected offsets are explicit.
Python output is candidate-generation evidence; the displayed three-window
union is separately proved in Lean.

## 3. A parallel global attack: leading phases and low-bit bias

[PhaseFrequency.lean](PhaseFrequency.lean) establishes a property of **every
fixed hypothetical unbounded ordinary odd trajectory** `x_j`. For each
positive integer `k`,

\[
\frac1N\sum_{j<N}e^{2\pi i k\log_2x_j}\longrightarrow0.\tag{5}
\]

There is no assumed escape rate, summable reciprocal trajectory, or random
parity model. Determinism makes an unbounded integer trajectory nonrepeating,
and hence escaping. Its phase increment is `alpha` plus a perturbation tending
to zero. A telescoping complex-rotation identity proves (5). The frequency
variable here counts odd steps, not all shortcut clocks.

The same module gives the finite and asymptotic lower-bit restriction. Define

\[
L(x)=1+\mathbf1_{x\equiv1\pmod4}+\mathbf1_{x\equiv5\pmod8}
\le v_2(3x+1).
\]

On an escaping odd trajectory, for every `epsilon>0`, eventually

\[
\frac1N\sum_{j<N}L(x_j)\le\log_2 3+\epsilon.\tag{6}
\]

Uniform frequencies on the four odd residues modulo eight would instead give
the limit `7/4>log₂3`. Lean proves that such a limit excludes escape.
Equation (5) does not imply those low-bit frequencies. A nontrivial bounded
cycle is also outside the escape premise. The separate
[phase note](PHASE_FREQUENCY.md) gives complete written proofs of fixed-phase
interval frequencies and zero marked-visit frequency on an escaping orbit;
those two corollaries are identified as written mathematics, not extra Lean
declarations.

## 4. Exact remaining global obligation

The open assertion from PR173 is still

\[
\forall n>1\quad
n\text{ marked}\ \Longrightarrow\ \exists k>0:\ R^k(n)<n.
\]

The new arbitrary-contraction theorem supplies unbounded families of such
inputs, but it chooses their exponents. It does not justify replacing
`for every fixed certified r, arbitrarily large suitable d` with
`for every marked pair (d,r)`. Nor does it show that an arbitrary orbit enters
one of the newly certified descending families. In particular, applying the
theorem to the smaller offset of a least counterexample would select different
lifted inputs; it would not preserve that counterexample's trajectory or
failure. The full proof requires that missing coverage or transport argument.

The complementary analytic target is a proved relation between the leading
phases in (5) and the low-bit statistics in (6), strong enough to exclude
escape, together with a treatment of nontrivial cycles. No independence of
those processes is assumed here.

## Replay, evidence, and publication

The source pin and unchanged dependency hashes are in [SOURCES.json](SOURCES.json).
The toolchain is Lean 4.34.1 with mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The new files are compiled with
warnings as errors; principal axiom closures contain only `propext`,
`Classical.choice`, and `Quot.sound`. No admitted theorem, extra convergence
axiom, or native-decide trust shortcut supplies any mathematical conclusion.

With a populated mathlib checkout at that pin:

```bash
python -B research/lean-dyadic-descent-20261121/replay.py \
  --mathlib /absolute/path/to/mathlib4 \
  --lean-bin /absolute/path/to/lean-4.34.1-linux/bin \
  --out /absolute/path/outside/the/repository
```

The script checks source pins, rebuilds the three imported section modules
and four new modules sequentially, records every compiler result, audits the
printed dependencies, and checks that the source files did not change during
the run. It saves a receipt outside the repository. The separate repository
integrity command is `python -X utf8 -B tools/validate.py`; it does not verify
the mathematics. Exact execution receipts are recorded under
`reports/2026-11-21-dyadic-descent/`. The independent scope review is in
[REVIEW.md](REVIEW.md) and the report directory.

Checkpoint 1, `cd3d4f3acad8b43ea07af764f28662f0eca7634e`, published the exact
offset certificates. The next checkpoint adds the genuine marked-return
families, unbounded contraction theorem, and parallel phase/low-bit results.
