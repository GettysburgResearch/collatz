# Global attempt: marked prefixes, certificate languages, and spectral weights

**Full Collatz convergence remains OPEN.** This pass steps back across the
repository's ordinary-source, counting, merger, symbolic, and operator routes.
Its strongest positive addition is a section-preserving merger theorem:
**every odd leading binary prefix of a marked integer is itself marked**.
It also establishes a fixed-block arithmetic budget for canonical certificates
and separates two different obstacles in the spectral route.

The new results and the unsuccessful closing steps are recorded together below.
No missing global premise is installed as a Lean axiom. The actual execution
boundary, exact commits, compiler output, and source hashes belong to the
[execution report](../../reports/2026-11-21-reframe/README.md).

## 1. What was reconsidered

The [repository snapshot](../../reports/2026-11-21-reframe/REPOSITORY_SNAPSHOT.json)
records all 143 PRs and 40 non-PR issues returned by GitHub at retrieval time.
Main was `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; this branch started
at `0bb13b800e4e97f9fd3091b1a3d2e98b49911b7c`, on
[draft PR178](https://github.com/GettysburgResearch/collatz/pull/178).
That is a metadata inventory, not a claim to have rechecked every source file.
The mathematical reading followed the main research map, integrated packets,
scoped errata, open obligations, and the frozen source heads named in the three
research notes.

The [publication refresh](LATE_UPDATE.md) records later heads of PR175,
PR180, and PR183, and the new PR185. Its eight-step physical word identity
adds a further guarded marked merger in part of the complementary rising
phase. This written composition does not change the frozen Lean inputs.

| Existing route | What it already supplies | What a full proof still needs |
|---|---|---|
| Ordinary extraction and coefficient stopping | Exact fixed-source/least-root equivalences, with completion counterexamples retained | A bound excluding an infinite supercritical word at each fixed positive source; cycle exclusion remains separate where required |
| Fixed-floor mass and predecessor populations | Finite counts, inverse fans, and conditional survivor criteria | A reusable bound for the actual fixed-floor survivors, with source and endpoint projections preserved |
| Complete-word ranks and merger induction | Well-founded comparisons and legal transformations, including some expanding moves | Successful coverage of every eligible ordinary input |
| Forced marked visits | Every positive ordinary orbit reaches the narrow marked section | A smaller marked component partner or actual return descent for every marked residual |
| Spectral and Green-weight methods | Exact transfer identities, finite inverse Green sums, and an escape-eigenvector construction | Arithmetic control that both excludes escape and retains the relevant vectors in the stated function space |

The reviewed main references for the first two rows are
[ordinary extraction](../integrated/ordinary-extraction/README.md),
[coefficient stopping](../integrated/coefficient-stopping/README.md), and
[exceptional mass](../integrated/exceptional-mass/README.md).
The latest PR177 complete-word order and PR173–184 section/merger work are
used at the exact heads in the notes, without importing their open coverage
premises as proved results.

## 2. A positive bridge that removes an unnecessary height loss

Use the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

PR173 marks an odd positive integer \(n\), with \(d=\lfloor\log_2n\rfloor\),
when

\[
(d+1)(n-2^d)\le70\,2^d.
\]

The new transport theorem says that if

\[
n=2^j x+c,\qquad 0\le j\le d,\qquad
0\le c\le n-2^d,\qquad x\text{ odd},
\]

then \(x\) is marked. It is strictly smaller if \(j>0\). The quotient
\(x=\lfloor n/2^j\rfloor\) satisfies the offset condition automatically
whenever it is odd. An actual merger \(T^a(n)=T^b(x)\) therefore transfers
convergence through smaller **marked** values directly.

The rounded-up quotient \(\lceil n/2^j\rceil\) is also marked whenever
it is odd and \(1\le j\le d\). The proof pays the rounding error from the
slack between the original and shorter binary heights. This supplies
additional candidates, including intermediate values
\(2^{d-j}+1\) for the offset-one family \(2^d+1\); existence of a merger
to any of those candidates is a separate assertion.

This matters because a general smaller ordinary partner need not have a
marked visit below the original source. The earlier general bridge needed
the expensive bound \(2^{H(x)}x<n\), where
\(H(x)=4\lfloor\sqrt{x}\rfloor+\lfloor\log_2x\rfloor\).
Dyadic partners satisfying the displayed shape guard need no such bound.

The composition covers PR180's whole solved rising phase:

\[
n=2^ku-1,\quad k\ge2,\quad u>0,\quad
3^{k-1}u\equiv3\pmod4.
\]

Its known word exchange merges \(n\) with \((n-1)/2\), which the new theorem
keeps inside the marked section. The complementary phase retains the old
odd-psi query; the phase guard is not dropped. Lean also states and proves
the exact equivalence between Collatz and a universal dyadic marked merger
cover. **The cover itself remains unproved.**

See [the merger attempt](UNIVERSAL_MERGERS.md) and
[MarkedDyadicTransport.lean](lean/MarkedDyadicTransport.lean).

The same note connects two population packets quantitatively. Certified
same-first-hit targets have disjoint full predecessor sets. Combining this
with marked-octave capacity and PR176's finite fan forces any common octave
supporting populations \(\gamma2^d/(d+1)^2\) for the resulting target set to
satisfy

\[
d+1\ge\frac{\gamma2^Q}{1562Q}.
\]

The targets have binary height at most \(10Q+1\). Thus arbitrarily large
target-dependent inverse populations cannot be replaced by a uniformly
small common octave. The disjointness and capacity steps are formalized in
[MergerPopulationPacking.lean](lean/MergerPopulationPacking.lean); the
composition with the separate finite-fan theorem is a paper deduction.

## 3. The exact arithmetic cost of pumping a certificate

For one fixed inverse word with \(A\) shortcut clocks and \(r>0\) odd steps,
write its affine inverse as

\[
F(q)=\frac{2^Aq-C}{3^r},\qquad
D(q)=(2^A-3^r)q-C.
\]

If \(q,F(q),\ldots,F^k(q)\) are ordinary integers, then

\[
3^{rk}\mid D(q).
\]

Unless \(D(q)=0\), this gives the explicit bound
\(3^{rk}\le|D(q)|\). An infinite ordinary chain of this one block must
therefore be constant at its exact fixed point. A fixed ordinary prefix
then gives equal sources, which contradicts different canonical first-hit
clocks. These implications are the formal statements in
[DiscretePump.lean](lean/DiscretePump.lean).

The [language argument](DISCRETE_CLOSURE.md) applies this budget to two
classes of word descriptions. Every regular language consisting only of
canonical literal parity certificates has a **uniform bound on odd-step
count**: an accepting cycle containing an odd step would be a forbidden
pump. Over a fixed finite alphabet of positive accelerated exponents,
the conclusion is stronger: **every context-free sublanguage of canonical
certificates is finite**. In the context-free pumping pattern, its rightmost
nonempty pump has a fixed suffix and supplies the same forbidden ordinary
chain. Infinite even-only pumps in other encodings are allowed, so the
encoding restriction matters. The language-theory deductions are paper
proofs, distinct from the formal arithmetic and first-hit core.

This does not defeat a finite set of rules carrying unbounded arithmetic
state. It identifies what cannot be discarded from the current certificate
architecture. The full closure attempt still needs a total successful
selector across its allowed changes of arithmetic state and word.

## 4. What the spectral attempt actually establishes

The [operator note](GLOBAL_MASS.md) follows the actual odd unit map and
keeps its ordinary inverse fibers. It gives two complementary conclusions.

First, a broad regular class of diagonal Hilbert weights cannot make the
operator hyponormal: weights \(\rho(n)=n^sV(n)\), \(s<1\), with
\(V\) positive and continuous on the ternary units. This includes finite
ternary residue weights and bounded continuous dependence on infinitely
many ternary digits. The proof uses Haar balance and the inverse fixed
point at \(-1\); it supplies actual positive-integer obstructions through
continuity, not a positive divergent orbit.

Second, the ordinary inverse Green construction does provide a useful
strict column-contraction weight. The new analysis tracks what happens to
the proposed escape eigenvector: along an injective forward orbit its weighted
terms stay bounded below by a fixed positive constant, so it leaves that
Hilbert space.
The older finite Green estimate is credited to its source. The additional
integrability analysis explains why simply using that weight does not close
the eigenvalue contradiction.

These are paper arguments, separate from the Lean audit. The note also
records the compressed-weight attempt and the exact inequality it would
still need. No spectral assumption is silently inserted into the marked
merger theorem.

Two further global deductions sharpen that boundary. The
[compact fractional-moment calculation](GREEN_FRACTIONAL_MOMENTS.md) gives
the exact threshold: the Green function has finite positive Haar moments
precisely below exponent one. It also rules out every nonzero nonnegative
integrable superharmonic compact density. The
[topological calculation](GREEN_TOPOLOGY.md) proves that the same Green
function is infinite on a dense `G_delta` of Haar measure zero, while it is
finite at every positive ordinary target. In particular, every positive
ordinary target is a discontinuity point of the compact function. These
results make the missing ordinary sampling assertion explicit; neither
Haar typicality nor topological density supplies it.

## 5. Formal build and evidence scope

The new build uses Lean **4.34.1** and clean Mathlib revision
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Only the two needed PR173 modules
are recompiled from their existing byte-identical frozen copies, followed
by the three new modules and the dedicated public-theorem axiom audit.
The earlier research packets are not replayed wholesale.

With the pinned toolchain on `PATH` and that Mathlib checkout's cache present:

```bash
MATHLIB_DIR=/absolute/path/to/mathlib4 \
  bash research/reframe-20261121/lean/build.sh
```

The script verifies source hashes and the clean Mathlib pin, then invokes
each Lean source with `-j1 -DwarningAsError=true`. It performs no installer
or network download. The execution report distinguishes kernel checking,
paper deductions, independent semantic reviews, and repository integrity.

## The full-theorem handoff

The central positive target from this pass is concrete: for **every**
marked \(n>1\), produce one of the ordinary dyadic mergers whose markedness
and strict decrease are now proved. The solved rising phase supplies a
whole family of these. The complementary phase, shifted-power residuals,
and arbitrary arithmetic-state changes are still uncovered.

The certificate and operator work test global alternatives to that target;
they do not manufacture the missing cover. This checkpoint therefore
advances the interfaces and rules out specific proposed completions while
leaving the full theorem explicitly open.
