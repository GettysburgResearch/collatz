# Forward-band populations and exact component descent

**Full Collatz remains open.** This packet builds on PR173's theorem that every
positive ordinary orbit visits a narrow band above a power of two. It develops
a new analytic population theorem inside that same band, and unconditional
Lean theorems for exact transport and smaller component representatives.

The source head is **PR173 `fa0c9e2a2851e6324391e39c17afcb5913185aec`**.
The map throughout is the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

## Continuation: complete clocks and a uniform ordinary population

The next analytic attack retains the **whole exponent total** in the
Syracuse mixing argument. Starting from Tao's stronger nonnegative
pair-sum renewal estimate, it derives joint fine-scale mixing with the
correct clock convolution. A selected-density telescope then gives a
controlled atom floor at **each central total** `|A-2s|<=sqrt(s)`.

Its ordinary consequence is stronger than the earlier logarithmic bound:
there are absolute constants `c,C>0` such that every positive ternary-unit
target `a` satisfies

\[
 X\ge Ca\quad\Longrightarrow\quad
 \#\{0<n\le X:n\text{ odd},\ \exists t,\ T^t(n)=a\}
 \ge cX/a.
\]

The sources may also be required to be ternary units after adjusting the
constants. This gives positive lower **natural** predecessor density and
a uniform linear onset. The constants are not numerically evaluated.

**Evidence level: written analytic derivation, independently reviewed;
not a Lean formalization of the analytic mixing or population theorem.**
The proof uses the published nonnegative renewal estimate, not an
unjustified inference from the old marginal mixing statement. It supplies
a lower population bound; the global survivor upper bound and universal
descent remain open.

[Joint clock proof](JOINT_CLOCK_MIXING.md) ·
[Independent review and ordinary population theorem](GLOBAL_RENEWAL_ATTACK.md)

## Continuation: a constructed potential and closure on the marked band

The three parallel attacks now supply four additional Lean modules and a
written construction of a finite positive ordinary inverse potential.
For the actual inverse operator

\[
(PF)(q)=\sum_{\substack{e\ge1\\2^e q\equiv1\ (3)}}
 3\,2^{-e}F((2^e q-1)/3),
\]

the Cesaro bound on complete inverse histories, Abel averaging, and a
diagonal limit give a finite function `F` with `PF <= F` and a uniform
positive floor on ternary units. The decreasing sequence `P^k F` then
converges to a finite harmonic function `G` with `PG = G`, still with a
uniform positive floor. The construction includes periodic collisions and
even ordinary targets. It also proves `G(2^E q)/(2^E q) -> 0` for each
fixed positive `q`.

**This construction is written analysis, independently reviewed, and is
not formalized in Lean.** It supplies the finite pair-transfer property
needed by the formal arithmetic; a sublinear upper bound on the marked
section is still open.

The new Lean theorem requires that upper bound only on the actual forced
band. Write `H(n) = F(n)/n`. The contribution of a second, distinct inverse
parent gives an absolute `c>0` and

\[
F(q)\ge 3\,2^{-e}F(n)+c,\qquad 2^e q=3n+1.
\]

There is an exact threshold barrier: `H(n)>=2c` implies `H(q)>=2c`.
Consequently, a small final marked value forces strict increase of `H`
through every preceding odd step in that segment. The finite-superlevel
argument proves:

- `finite_marked_absorbing_floor`: if `H(n)->0` through marked odd units,
  every positive ordinary source physically hits one finite part of the
  marked band.
- `universal_of_marked_inverse_envelope_and_base`: the same upper bound,
  together with convergence of the finite marked base, implies `Universal`.

Both are **kernel-checked implications**. `MarkedSublinear` and the finite
base remain explicit hypotheses; no axiom supplies them. The earlier
all-ordinary version is also included. The other two new modules prove the
finite-population unitization transport and complete-word comparison
results: the entire terminal-gap-four language closes on sixteen sources,
while an explicit unbounded family of complete source certificates retains
an exact Mersenne query on the wanted side.

[Potential construction and arithmetic](GLOBAL_ARITHMETIC_ATTACK.md) ·
[Band-only Lean proof](lean/MarkedDensityPotential.lean) ·
[Complete source-word attack](WITNESS_GLOBAL_ATTACK.md) ·
[Unit population transport](lean/UnitPopulationTransport.lean) ·
[Independent analytic review](REVIEW_JOINT_AND_ABEL.md)

The upper-bound attempt includes two exact failed sublinear candidates and
an actual-map harmonic obstruction. A finite harmonic function concentrated
on one inverse ray has normalized values bounded below along that ray,
despite eventual vanishing along every fixed dyadic ray. A source-qualified
version includes cofinally large marked nodes. Adding it to a positive
harmonic envelope preserves the known floor and ray-decay properties, but
destroys the desired uniform decay. This does **not** refute the particular
Abel-derived envelope or the existence of a better one; it shows why the
remaining argument must use more than those generic properties.

[Harmonic-ray obstruction](HARMONIC_RAY_OBSTRUCTION.md) ·
[Exact candidate certificates](../../reports/2026-11-21-forward-band-closure/inverse-density-majorant-counterexamples.json)

The closing pass goes further: it constructs the **least excessive
majorant** `V` of the unit indicator and proves that it has no inverse-ray
atoms. A truncated subharmonic spike could otherwise be subtracted while
preserving both the obstacle and excessivity, contradicting leastness.
Harmonicization preserves the positive floor and this absence of atoms.
Combining finite heavy-cylinder trees with the uniform predecessor count
then proves the actual upper estimate

\[
V(n)/n\longrightarrow0
\quad\text{through all odd unit predecessors of each fixed target }q.
\]

This is uniform over the **whole fixed-target predecessor basin**, including
its marked points. Its cutoff still depends on the target. A divergent
forward path would move through different target basins, so this result
does not supply the remaining bound over all marked ordinary inputs.
It is a source-qualified written proof, independently reviewed, not a
new Lean theorem.

[Canonical atom removal and the fixed-basin upper bound](MINIMAL_ENVELOPE_ATOM_REMOVAL.md)

A complementary attack proves a global upper bound for every fixed
subcritical Abel parameter. For `1/3 < rho < 1`, with explicit constants,

\[
F_\rho(q)\le q^{\,1+\log\rho/\log3}
                 (B_\rho+A\log q).
\]

Thus each such approximant is globally sublinear, including at unknown
periodic targets. The estimate also gives sublinear near-critical
diagonals. The critical limit still lacks the required uniformity:
`B_rho` diverges, the exponent tends to one, and the discounted transfer
has an additional negative drift term. This written estimate does not
silently replace the undiscounted inequality required by Lean.

[Quantitative Abel upper bound and exact discount loss](ABEL_MARKED_UPPER_ATTACK.md)

## 1. New population theorem inside the actual band

There is an absolute constant \(\gamma>0\) such that, for every positive
integer \(a\) not divisible by three, arbitrarily large integers \(d\) admit
a finite set \(P\) of distinct odd ordinary predecessors satisfying

\[
2^d\le n,\qquad(d+1)(n-2^d)\le10\,2^d\quad(n\in P),
\qquad |P|\ge\gamma\frac{2^d}{(d+1)^2}.
\]

Every member of \(P\) reaches the supplied target \(a\) at **one common
shortcut clock at most \(15(d+1)\)**. The constant 10 is smaller than the
constant 70 in PR173's exact forward section. The population constant is
independent of the target; the onset and successful octaves may depend on it.
An optional refinement makes every source a ternary unit too.

**Evidence level: SOURCE-QUALIFIED written analytic proof, independently
reviewed; not a Lean formalization of the analytic theorem.** The only
non-elementary input is the fine-scale Syracuse estimate already used in
PR180's selected-density proof. The new argument interpolates to every large
word depth, retains a bounded real offset and a controlled total, steers an
actual inverse parent into the band, and then pigeonholes by total. It never
assumes mixing conditioned on one total.

The same controlled construction gives, for every fixed \(\sigma<1\), at
least \(X^\sigma\) ordinary predecessors of each positive unit target below
every sufficiently large \(X\).

[Complete population proof](MARKED_PREDECESSOR_POPULATIONS.md) ·
[Unit-source refinement](UNIT_SOURCE_APPENDIX.md) ·
[Independent review](../../reports/2026-11-21-forward-band-closure/REVIEW_MARKED_POPULATIONS.md)

## 2. Lean: smaller representatives after the initial precision is exhausted

For every \(k\ge2\), let

\[
n_k=2^{3k}+2^{2k}-1,\qquad
m_k=2^{3k-1}+2^{2k-1}-1=\frac{n_k-1}{2}.
\]

Lean proves that the \(n_k\) form an unbounded family in PR173's marked
section and that

\[
T^{2k+2}(n_k)=T^{2k+1}(m_k),\qquad
T^{3k}(n_k)=T^{3k-1}(m_k),\qquad m_k<n_k.
\]

Thus \(n_k\) converges if and only if its smaller representative \(m_k\)
converges. This is component descent through a common ordinary endpoint; it
does not assert that \(m_k\) occurs on the forward trajectory of \(n_k\).

The general clock-compression theorem proves that if

\[
2^d\le n<2^{d+1},\quad T^A(b)=T^d(n),\quad
p(b,A)=p(n,d),\quad A<d,
\]

where \(p\) counts odd steps, then \(b<2^d\le n\) and the basin statuses
agree. A total inverse construction also restores any ternary difference
\(3^pu\) to an exact binary difference:

\[
p\le A\le4p,\qquad
T^A(2^Au+b)=3^pu+q
\]

for every ternary-unit reference \(q\), uniformly in \(u\). The construction
is total; its clock is not proved to save a step in every marked case.

**Evidence level: KERNEL-CHECKED unconditional identities and implications.**
The open universal selector is not introduced as an axiom.

[Proof note and remaining phase](BAND_TRANSPORT_NOTE.md) ·
[Lean source](lean/BandTransport.lean)

A further Lean module puts this result directly into the earlier odd-psi
comparison framework. The solved phase gives an unconditional comparison
`Basin(n) ↔ Basin(2n−1)` for the whole block family. In the complementary
phase, the proposed transfer is exactly that same original odd query, at
unchanged rank. This identifies the circular step that an attempted closing
induction would otherwise hide.

[Parity bridge and exact remaining query](BAND_PARITY_BRIDGE_NOTE.md) ·
[Lean bridge](lean/BandParityBridge.lean)

A matched bounded search also tested the new rule against the entire saved
odd-psi frontier through six binary refinements. The remaining frontiers
were identical to the baseline. The [full-frontier check](search/PHASE_COMPLETION_CHECK.md)
records the exact bounds, unchanged cells, and replay data; it is not a
claim that larger searches or other proofs are impossible.


## 3. Carry accounting across large rising returns

Write \(n+1=2^r q\) with odd \(q\), and define \(H(n)=3^r q\). Lean proves

\[
H(T^j(n))=H(n)\quad(0\le j\le r),\qquad T^r(n)=H(n)-1.
\]

This includes all section returns encountered inside the growing run.
At its halving reset, the exact next carry height is retained, including
the additive term \(2^a-1\). A global repayment bound across changing
resets remains open.

[Carry attempt](CARRY_RESET_ATTEMPT.md) ·
[Carry core](lean/CarryBlocks.lean) · [Section adapter](lean/CarrySection.lean)

## 4. The precise full-Collatz target

Let \(V_d(t)\) count marked points in \([2^d,2^{d+1})\) which have not
visited one at any shortcut clock through \(t\). The population theorem gives

\[
\boxed{\quad
\mathrm{Collatz}\iff
\exists d_0\ \forall d\ge d_0\ \exists t:
(d+1)^3V_d(t)<2^d.
\quad}
\]

A nonconvergent unit target would instead force
\(V_d(t)\ge\gamma2^d/(d+1)^2\) at every time on arbitrarily large
target-dependent octaves. This proves the contradiction once the boxed
upper estimate is supplied. **The upper estimate has not been proved.**

[The Lean criterion](lean/BandPopulationCriterion.lean) checks this finite
counting implication with `DenseBandFans` as an **explicit hypothesis**.
The written population proof supplies its mathematical justification; it is
not silently promoted to a kernel theorem. The clock may vary with the
octave. Every sufficiently large octave must pass: an arbitrary unbounded
subsequence would not be enough for this argument.

## 5. A global restriction on any divergent orbit

The final closing attempt gives another source-qualified analytic consequence
of PR180's uniform predecessor-density bound. Any nonrepeating positive odd
unit orbit `q_i` must satisfy

\[
\sum_i\frac1{q_i}\le\frac{22}{c_0}<\infty.
\]

The proof chooses one small inverse parent off the orbit at every step;
their entire predecessor sets are disjoint. The density lower bounds can
therefore be summed over every finite collection. It follows that the
binary logarithmic phases of a divergent odd orbit approach one irrational
rotation and are equidistributed. Its marked visits would be infinite but
have zero frequency in odd time.

This rules out nonsummable reciprocal growth of a divergent orbit. It does
not rule out a divergent orbit with summable reciprocals or another cycle,
and the survivor upper bound above remains open.

[Disjoint-branch proof and final transport check](DIVERGENT_ORBIT_PHASES.md)

## 6. Sources and replay

[Source pins and evidence boundaries](SOURCES.md) lists the imported files,
the prior analytic interface, and the published analytic input.

The packet uses Lean 4.34.1 and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Given a built Mathlib checkout at
that pin and the matching Lean executable, run:

```sh
python research/lean-forward-band-20261121/check_lean.py \
  --mathlib /path/to/mathlib4 --lean /path/to/lean \
  --report-dir reports/2026-11-21-forward-band-closure
python research/lean-forward-band-20261121/verify_marked_cloud.py \
  --output reports/2026-11-21-forward-band-closure/marked-cloud-examples.json
python research/lean-forward-band-20261121/verify_inverse_density_majorants.py \
  --output reports/2026-11-21-forward-band-closure/inverse-density-majorant-counterexamples.json
```

The first command recompiles all fifteen local modules into a fresh output
directory, treats warnings as errors, and records source hashes and printed
axioms. The second checks finite legal inverse clouds using exact integer
and rational arithmetic. The third replays exact rational counterexamples
to the two proposed upper potentials, including the stated analytic tail
bound. These finite checks do not validate the analytic asymptotics or
prove Collatz.

The included `lean/lakefile.lean` also pins the dependency for a conventional
Lake environment. The recorded replay uses the explicit built-cache command
above.

[Lean build record](../../reports/2026-11-21-forward-band-closure/lean-check.json) ·
[Build log](../../reports/2026-11-21-forward-band-closure/lean-build.log) ·
[Exact arithmetic examples](../../reports/2026-11-21-forward-band-closure/marked-cloud-examples.json)
