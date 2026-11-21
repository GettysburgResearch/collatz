# Exponentially many ancestors in the mandatory shrinking section

**Lean-checked partial results; full Collatz remains OPEN.** This checkpoint
builds directly on PR173's new forward-section theorem. It supplies a large,
injective population of ordinary ancestors **inside that same section**, an
explicit finite certificate from a passing survivor count, and a comparison
of entire finite survivor populations. The upper survivor estimate needed to
complete the theorem is still unproved.

The map throughout is the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

`Basin n` means an actual finite iterate reaches one. All sources and
endpoints are ordinary natural integers. The imported sources are frozen at
PR173 commit `fa0c9e2a2851e6324391e39c17afcb5913185aec`; the four files are
unchanged, and [upstream-pins.json](upstream-pins.json) records their hashes.

## 1. The new result being used

Write \(d=\lfloor\log_2 x\rfloor\). PR173 marks the odd integers satisfying

\[
(d+1)(x-2^d)\le70\,2^d.
\]

It proves that every positive forward orbit visits a mark in fewer than
\(4\lfloor\sqrt n\rfloor+\lfloor\log_2 n\rfloor\) shortcut steps, and that
the number of marks below \(N\) is at most \(426N/(\lfloor\log_2N\rfloor+2)\).
It also proves first positive marked returns can expand by arbitrarily large
factors. These are credited imported results, not new claims of this packet.
[ForwardSection.lean](lean/ForwardSection.lean) ·
[SectionDynamics.lean](lean/SectionDynamics.lean) ·
[RisingReturns.lean](lean/RisingReturns.lean)

The imported forward reduction says that convergence on all marks suffices.
The result below replaces that zero-exception requirement with a finite
count permitting exponentially many unresolved marks at each passing stage.

## 2. A population in the actual band

Put \(\alpha=\log_2 3\). Call \(Q\) admissible if \(Q\ge16\) and some
nonnegative integer \(a\), coprime to \(Q\), satisfies

\[
|Q\alpha-a|\le1/Q.
\]

`goodScale_cofinal` proves these scales are unbounded. There is no assumption
of bounded continued-fraction coefficients or a stronger irrationality estimate.

**For every admissible \(Q\), every ternary unit \(q\le2^Q\) has at least
\(2^Q\) distinct marked odd ancestors \(x_w\) with**

\[
2^Q\le x_w<2^{10Q},\qquad
T^{k_w}(x_w)=q,\qquad
7Q-5\le k_w<11Q.
\]

Here a ternary unit is an integer not divisible by three; this condition
already excludes zero. The binary word \(w\) ranges over \(\{0,1\}^Q\).
No convergence assumption is made about \(q\). These are actual ancestors,
not approximations or points in a completion.

The main compiled interfaces are `marked_ancestors_with_clocks` and
`marked_ancestors` in [BandCriterion.lean](lean/BandCriterion.lean).
The lower height bound follows from `oddFan_lower` and the constructed
root bound. The outputs therefore move to infinity with the scale.

### Construction and error budget

Start at \(y=2^Qq\). Apply \(p<Q\) of the existing four-clock inverse lifts.
Their value \(z=L^p(y)\) satisfies

\[
2^Q\le z<2^{5Q},\qquad T^{4p+Q}(z)=q.
\]

The rational rotation grid selects \(p\) so that, for an integer \(Z\),

\[
\frac1{4Q}\le\log_2z-Q\alpha-Z\le\frac7{2Q}.
\]

The inverse-lift logarithmic error is at most \(4/y\). The proof uses the
buffer \(16Q\le2^Q\), so this is at most \(1/(4Q)\).
[BandSteering.lean](lean/BandSteering.lean)

Now apply the existing binary inverse fan for \(Q\) generations. Its raw
leaves \(X_w\) are distinct and all reach \(z\) at clock \(6Q\). Their exact
bounds put the entire population in a strict octave: \(X_u<2X_v\) for every
pair. Each leaf has an explicit initial padding \(b_w\le5\); remove it to
obtain the odd integer \(x_w=X_w/2^{b_w}\).

Oddification preserves injectivity. Equal odd parts would make two raw leaves
dyadic multiples of one another, impossible inside a strict octave unless
the leaves were equal. The exact phase identity is

\[
\log_2x_w=\log_2z+(6Q-b_w)-Q\alpha-e_w,
\qquad 0\le e_w\le4/z\le1/(4Q).
\]

Consequently the phase of every odd leaf is above an integer and at most
\(7/(2Q)\) above it. Its binary digit count is at most \(10Q\), making the
product at most \(35\). This is exactly PR173's sufficient phase condition
for membership in its original marked set. The full ordinary clock is
\(7Q+4p-b_w\), giving the stated common clock interval.
[FanGeometry.lean](lean/FanGeometry.lean)

## 3. A finite count that certifies a whole range

Define the finite, decidable set

\[
S_Q(t)=\{x<2^{10Q}:x\text{ is marked and }
                T^j(x)\ne1\text{ for every }0\le j\le t\}.
\]

The theorem `band_count_finite_certificate` proves

\[
\boxed{|S_Q(t)|<2^Q\quad\Longrightarrow\quad
\forall q\le2^Q,\ 3\nmid q\Rightarrow
\exists j\le\max(1,t),\ T^j(q)=1.}
\]

Thus a passing test can leave as many as \(2^Q-1\) marked starts unresolved.
The conclusion retains the same observation deadline, except for the
necessary adjustment from zero to one.

For each target, at least one of its \(2^Q\) distinct marked ancestors must
have hit one by the deadline. The target then also hits one by that deadline,
regardless of whether its meeting clock comes before or after the ancestor's
visit to one. The checked lemma `hitBy_at_hit` explicitly handles the
\(1\to2\to1\) cycle; it does not assume that reaching one makes the shortcut
orbit stationary. [CountCriterion.lean](lean/CountCriterion.lean)

The resulting **fully composed** equivalence is

\[
\boxed{\mathrm{Collatz}\quad\Longleftrightarrow\quad
\forall K\ \exists Q\ge K,\ Q\text{ admissible},\ \exists t:\ |S_Q(t)|<2^Q.}
\]

This is `collatz_iff_band_survivor_count`. The geometry and cofinality on its
right-hand side are proved. **The asserted upper survivor count is not.**
The result detects nontrivial cycles as well as divergent positive orbits.

## 4. Whole finite populations, at the same clock

The different target fans may overlap. Their ordinary clock interval controls
that overlap exactly. For a finite set \(A\) of unit targets at most \(2^Q\),
map each pair \((q,w)\) to \((x_w,k_w)\). Equality of both output coordinates
recovers \(q=T^{k_w}(x_w)\), and the individual fan's injectivity recovers
\(w\). Therefore, for every property \(P\) inherited by ordinary ancestors,

\[
2^Q|A|\le(4Q+5)
\#\{x<2^{10Q}:x\text{ marked and }P(x)\}.
\]

This is `band_component_population`. It uses the actual construction, not an
assumed fan or an external predecessor-counting theorem.

There is a stronger finite specialization. Let \(U_Q(t)\) be the units at most
\(2^Q\) that have not hit one by clock \(t\). For every \(t\ge1\),

\[
\boxed{2^Q|U_Q(t)|\le(4Q+5)|S_Q(t)|.}
\]

Both sides are finite experiments at the **same ordinary clock**. No source
is assumed to be an eternal counterexample. This is
`band_finite_survivor_population`.
[PopulationTransfer.lean](lean/PopulationTransfer.lean)

## 5. What the completion attempts established

The attempts sought an upper estimate for \(S_Q(t)\), or a deterministic
descent across several marked returns. Neither has been established.

The exact source-weight calculation prevents one misleading shortcut. If
\(E(n)\) is the first marked visit and \(w(n)=n^{-4}\), then
\(G(m)=\sum_{E(n)=m}w(n)\) preserves the entire original mass. For every
constant \(C\), some marked \(m\) satisfies \(G(m)>Cw(m)\). The same is true
for the first positive return. These statements are checked in
[SectionTransport.lean](lean/SectionTransport.lean). Counting fewer available
endpoints does not shrink a fixed surviving source atom.

The section does support the summable critical weight
\(1/[n(\lfloor\log_2n\rfloor+1)]\). Its possible multi-return use, the
ternary-residue correlations still requiring control, and the exact failed
endpoint domination estimate are in
[SECTION_TRANSPORT.md](SECTION_TRANSPORT.md).

The direct offset approach also needs an additional mechanism. Although
\(n=2^d+r\) shares \(r\)'s first \(d\) parities, the smaller offset's
convergence certificate need not fit inside that window. The explicit marked
family \(2^{4m}+2^{3m}-1\) has offsets \(2^{3m}-1\) that do not descend at
any clock through \(4m\). This written obstruction and the exact coupling
identity are in [ARITHMETIC_BAND_FRONTIER.md](ARITHMETIC_BAND_FRONTIER.md).
They are not claimed as additional checked Lean modules.

The population construction is a lower bound on the footprint of any surviving
component. Completing the proof requires an upper bound, or an all-input
multi-return rule that supplies one. The leading-phase recurrence and the
finite residue-mixing identity do not presently supply that inference.
[UPPER_COUNT_ATTEMPT.md](UPPER_COUNT_ATTEMPT.md) records the separate attempt
at this closing estimate, the necessary observation-time bound, and a
source-qualified alternative analytic target without importing it into Lean.

## Checkpoint 6: a faster forward entrance

[FastForward.lean](lean/FastForward.lean) extends this packet with the
uniform theorem `n<=2^Q -> exists t<9Q, Marked (orbit t n)` at every
admissible `Q`, and the height ceiling `orbit t n<2^(10Q)`. It also retains
exact ordinary merger clocks when a sufficiently small supplied partner is
moved into the marked band. The exact denominator `306` gives a concrete
entrance bound of 2,754 steps through the range `n<=2^306`.

The new finite proof, its analytic polylogarithmic corollary, and its
separate replay are documented in the [checkpoint-6 guide](../overview/README.md).
The earlier `section/check.py` remains the checkpoint-5 replay; use
`overview/check.py` for the new chain. The survivor upper count remains open.

## Replay and evidence

Use Lean **4.34.1**, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612` and its cached dependencies:

```sh
python3 check.py --mathlib /absolute/path/to/mathlib4 \
  --lean /absolute/path/to/lean-4.34.1-linux/bin/lean \
  --out /absolute/path/to/new-empty-output \
  --receipt /absolute/path/to/section-lean-receipt.json
python3 check_return_transport.py
```

The script checks exact source and runtime pins, compiles the four imported
modules and all six new modules into a fresh output directory, and executes
[Audit.lean](lean/Audit.lean) over every public theorem in the new modules.
It treats warnings as errors and records source hashes before and after the
run. Single-thread execution avoids unnecessary import contention.

The accompanying report distinguishes Lean proof checking, the exact finite
Python witness, and the repository's required structural gate. None of these
is described as a proof of the unresolved global survivor estimate.
