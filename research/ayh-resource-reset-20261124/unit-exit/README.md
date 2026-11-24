# Quantitative unit escape and the remaining two-class geometry

**Collatz remains OPEN.** This checkpoint proves an explicit arithmetic escape estimate for actual tripling disagreements, removes summable portions of the ordinary two-head graph, and identifies local information carried by the colors of physical trit truncations. The finite algebra has a fresh Lean build; the analytic theorems are proposed written deductions with their source qualifications below. The baseline is PR 197 at `2c1397d2adcadc620381bca20c465f3bf31a6f8e`.

Use the positive shortcut map
\[
 T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]
An invariant binary label satisfies \(f(T(n))=f(n)\). The principal application is the indicator that a positive integer eventually reaches 1. Call an odd \(x\) a tripling defect if \(f(x)\ne f(3x)\); a *unit* means an integer coprime to three. Counts below concern these actual labels. A failed finite merger certificate is only an upper-counting device.

## 1. An explicit escape from the nonunits

Let \(D_U(Y)\) count odd unit tripling defects through \(Y\). Set
\[
                         \sigma=\frac{2001}{5000}.
\]
For \(X\ge2\) and \(1\le Z\le X\), all but
\[
                O\!\left(\frac{XZ^{-\sigma}}{\sqrt{\log(2X)}}\right)
\tag{1}
\]
of the defects in \([X,2X)\) have a unit defect \(y\in[X,CXZ]\) with the **same ordered labels**. On each octave these witnesses can be assigned injectively. Consequently
\[
 \#\{x\in[X,2X):f(x)\ne f(3x),\ x\text{ odd}\}
 \le D_U(CXZ)+O\!\left(\frac{XZ^{-\sigma}}{\sqrt{\log(2X)}}\right).
\tag{2}
\]
The square root uses the source-qualified native pair estimate P. Removing that square root leaves a theorem using the new exact arithmetic and finite certificate alone. The number of odd defects at most \(X\) whose continuation never reaches a unit is \(O(X^{1/5})\), also without P or a density hypothesis.

### Why the arithmetic contracts

At a nonunit \(x=3s\), \(s\) odd, exact ordinary identities give
\[
 f(3s)=f(16s+1),\quad
 f(3(16s+1))=f(32s+1),\quad
 f(3(32s+1))=f(9s).
\]
If the outer labels differ, exactly one of the two successor edges differs, and it has the same orientation. Following it gives the expansions
\[
                         x\longmapsto 2^e x/3+1,
                         \qquad e\in\{4,5\}.
\]
Avoiding a unit imposes one ternary congruence per step. Meanwhile each step fixes another four or five binary digits of the successor. Some resulting binary prefixes force the successor and its triple to merge. Such words cannot occur in any uninterrupted true-defect path, including as a block far into that path.

Two independently written decoders, one using modular integer residues and one using rational shadows, produce the same allowed length-22 dictionary. Its overlap graph has **4,218 vertices and 5,349 edges**. Exact row-sum bounds on its 512-step unweighted paths and 86-step rationally weighted paths imply, respectively,
\[
 \#\{\text{admissible words of length }t\}\ll3^{t/5},\qquad
 \sum_{t\ge0}\sum_{|w|=t\text{ admissible}}3^{-t}
                  \left(\prod_{e\in w}\frac{2^e}{3}\right)^\sigma<\infty.
\]
This is an all-length consequence of a finite forbidden-block certificate. It uses no independence law for the actual defect choices. Stopping at the first product of slopes above \(Z\) gives (1). Within each stopped ternary class, the still free original binary parameter supplies the native square root; the argument does not restart a distribution at the exit.

[Full escape proof](UNIT_EXIT.md) · [exact checker](check_nonunit.py) · [Lean arithmetic and shadow soundness](NonunitExit.lean) · [replay and independent review](../../../reports/ayh-resource-reset-20261124/unit-exit/README.md).

### A logarithmic moment on one suffix

Taking \(Z=(\log X)^{5/4}\) makes the normalized exception in (1) \(O((\log X)^{-4001/4000})\), summable over geometric octaves. Unique backwards ancestry and geometric growth give
\[
 \sum_{y\text{ odd unit defect}}\frac{(\log(2y))^{5/4}}{y}<\infty
 \quad\Longrightarrow\quad
 \sum_{x\text{ odd defect}}\frac1x<\infty.
\tag{3}
\]
The preceding checkpoint's route with \(p=3\) carries every unit defect to a literal four-trit head of suffix **57**, with comparable height, bounded multiplicity and the same parent–child label order. It may prescribe any fixed open mantissa interval, one level residue modulo a fixed modulus, and any fixed minimum number of initial even child steps. Thus a logarithmically weighted series on this single scheduled suffix suffices in (3). With the separately qualified fixed-target positive-density input M and the ordinary variation argument, that convergence would prove Collatz. The series itself remains unbounded by this work.

There is a separate conclusion using the published Krasikov–Lagarias predecessor exponent \(.84\), without M. If a counterexample exists, then **each orientation separately** must have unit defects satisfying
\[
 \limsup_{Y\to\infty}\frac{D_{U,\pm}(Y)}{Y^{42021/70025}}>0,
 \qquad \frac{42021}{70025}=0.600085\ldots.
\tag{4}
\]
Using P also gives the simpler log-corrected denominator \(Y^{3/5}(\log Y)^{3/4}\). The directed return paths of PR 146 transfer the lower count between the two orientations before the new escape. Both lower bounds pass to the corresponding parent–child patterns on the prescribed suffix-57 schedule along unbounded sequences of levels. Proving either one-way basin implication eventually on that schedule would therefore settle Collatz. [Oriented statement and proof](ORIENTED_UNIT_SUFFIX.md).

### A finer target at 17 modulo 48, with one exact descent

A second escape process starts from defects \(x\equiv1\pmod{16}\). At a ternary unit \(x\equiv1\pmod3\), the exact ordered exchange is \(x\mapsto(4x-1)/3\); at a multiple of three use the two successors above. Stop at \(x\equiv2\pmod3\), which in this input class means **17 modulo 48**. The three-letter forbidden-word graph has 12,969 states and 35,778 transitions. A separate exact replay proves
\[
 D_1([X,2X))\le3D_{17}([X,CXZ])+
 O\!\left(\frac{XZ^{-200/3599}}{\sqrt{\log(2X)}}\right),
 \qquad 1\le Z\le X^{1/10}.
\tag{8}
\]
Here \(D_1\) and \(D_{17}\) count true tripling defects in their named residue classes. The new route preserves their ordered labels. Backwards ancestry is unique, but the slowest step now gives up to three ancestors per octave. Its permanently unescaped inputs number \(O(X^{.93})\). The native square root again uses P.

Since \(200/3599>1/18\), choosing \(Z=(\log X)^9\) makes the discarded original row weight summable. The older PR 146 bounded-multiplicity reduction of all odd defects to \(1\bmod16\) then makes convergence of
\[
 \sum_{y\equiv17\ (48),\ f(y)\ne f(3y)}
                 \frac{(\log(2y))^9}{y}
\]
a sufficient condition for Collatz **under M**. Any fixed power saving in this residue's defect count would also suffice under M. The aggregate older reduction is not asserted to preserve a chosen orientation. The new \(.93\) permanent bound alone does not beat the classical \(.84\) population threshold.

Every remaining target also has a strictly smaller ordered-label representative:
\[
                 48t+17\longmapsto32t+11,
 \qquad (f(48t+17),f(3(48t+17)))=(f(32t+11),f(3(32t+11))).
\]
This identity is kernel-checked for every \(t\). Iterating strict descent would require a further route from the new class, which is not supplied. [Second escape proof](RESIDUE17_ESCAPE.md) · [separate exact checker](check_residue17.py) · [two Lean exchanges](UnitResidueExchange.lean).

## 2. A summable portion of the ordinary four-ray graph

For genuine head rows use \(R=81^j\), \(d=\log_2R\), and original weight \(1/R\) on children \(7R\le x<8R\). Regeneration supplies smaller genuine head edges at many physical times. Given two such heads \(z,y\) at relative time \(v\), advance the first head and its parent by \(v\) physical steps. Together with the fresh second pair they are four affine rays on one remaining ordinary parameter. Their entering grade intervals are
\[
 [L,U]=[\min(p_{\lfloor z/81\rfloor}(v),4+p_z(v)),
          \max(p_{\lfloor z/81\rfloor}(v),4+p_z(v))],
 \qquad [w,w+4].
\]
If these intervals are disjoint and only two symbolic classes remain at the intermediate deadline, both original pairs must use both classes. Some cross pair therefore reverses its weak grade order. It must reach a grade tie while its two affine records remain distinct.

Let \(K\) be the initial interval distance. An unusually early tie costs a bounded-increment concentration tail. Otherwise the fresh second head must survive roughly \(K^2/\log d\) clocks before the tie, and the tied cross pair must survive a further macroscopic block. Their product can be taken at the observable first tie. There are at most two candidate exponents at each positive distance \(K\). Summing the whole exponent menu costs a harmonic sum, rather than its square-root-size cardinality.

The resulting bound on this portion of the true graph is
\[
                       \Gamma_{j,\mathrm{tested}}\ll d(\log d)^2.
\]
One comparison gives a near-harmonic original bound. With two comparisons in disjoint future bit windows, the normalized original multiplicity is
\[
                      O\!\left(d^{-3/2}(\log d)^{9/2}\right).
\tag{5}
\]
Thus sources supporting a positive density of such tested time triples have summable original row mass. Every possible marked witness is included in the multiplicity count; the argument does not select independent colored endpoints. [Four-ray estimate](DISJOINT_GRADE_CROSSINGS.md).

Two refinements narrow the overlapping case. The same bounds cover an overlapping fresh interval when the older pair reverses its own weak grade order. Also, the moving grades of either older endpoint form predictable tracks in the original coarse coordinate. Uniformly over the polynomial bank of actual anchors, at most \(C(1+W)\sqrt{D\log d}\) marked clocks can lie within width \(W\) of those endpoints. A positive frequency of marks therefore cannot remain inside sufficiently small neighborhoods of width \(c\sqrt{D/\log d}\). [Nested refinements](NESTED_GRADE_REFINEMENTS.md).

### Three-class comparisons at intermediate time gaps

Put \(V=\lfloor d^\alpha\rfloor\) and use integer lags \(V\le v\le2V\). Compare overlapping intervals, or a fixed menu \(|w-v/2|\le C\sqrt{V\log d}\), and retain at least three affine classes after a further \(d/10\) bits. The uniform triple input U1 gives the all-head first-moment bound
\[
 \frac1{RdV}\sum_x M(x)
 \ll_A d^{-A}+(\log d)\left(\frac{V\log d}{d}\right)^u,
 \qquad 1<u<3/2.
\tag{6}
\]
This is summable when \(\alpha<1/3\) and \(u\) is suitably chosen. Here \(M\) counts all head/time tuples.

A repeated-test argument extends the **positive density of distinct time pairs** conclusion to every \(0<\alpha<2/3\). At one pair of clocks, the complete original parameter grid bounds the union over all anchor choices by
\[
 q_d\ll \sqrt d\,\log d\,(V\log d/d)^u+d^{-A}.
\]
Dense time pairs yield many fixed-size tuples with disjoint test windows. Conditional iteration on that single original grid gives \(d^{-1/2}q_d^p\), including the original native survival only once. Choose \(u(1-\alpha)>1/2\), then \(p\) large enough, to obtain a summable power. Multiple qualifying heads at the same two clocks count once in this extension. [Repeated mesoscopic tests](REPEATED_MESOSCOPIC_TRIPLES.md).

These estimates leave an interior, order-preserving two-class configuration, as well as regimes outside their grade and clock hypotheses. They do not provide a bound for the entire weighted graph.

## 3. What the actual color answers must reveal

On any polynomial-density set of good discordant ordinary parents, expose the original native residue, the entire exterior high quotient of the late coarse coordinate, and polynomially many possible seed states for the two physical arms. Their subsequent affine descriptions can be tracked from successive low bits. At each regenerated clock, at most \(8+\lceil\log_2(1+s)\rceil\) color queries on ordinary trit truncations select a true discordant head in a prescribed open arc, where \(s\) is the current grade difference.

Let \(P_t\) be the public information at that clock, \(L_t\) its current color replies, and \(F_t\) the next fixed block of \(h\) coarse bits. For a contiguous late interval of \(D\ge(\log d)^6\) clocks and a retained source fraction \(w\),
\[
                   \sum_t I(L_t;F_t\mid P_t)
                      \ge \gamma D-h\log(Cd^C/w).
\tag{7}
\]
The proof compares the true joint law to a law rerandomizing only that next block. Every fixed selected head passes its finite failure test with small probability under the latter law, while actual regeneration gives a positive hit frequency. The entropy chain rule charges each bit deficit at most \(h\) times. This yields information in the present ordinary color answers even after the full exterior quotient is disclosed. It is not an upper bound on that information and hence not a contradiction. [Local color information](LOCAL_COLOR_INFORMATION.md).

The latest mixed-adic predecessor and antichain results give lower populations in substantially larger windows. They do not control this selected, power-short exterior cell or these conditional color answers. The [source comparison](../../../reports/ayh-resource-reset-20261124/unit-exit/MIXED_ADIC_SCOPE.md) credits the existing PR 201/203 results and states the scale mismatch.

## Formal and source boundaries

| Input or result | Evidence and use |
| --- | --- |
| Exact physical chain, unique directed successor, shadow lift and certificate soundness | Five new Lean theorems in `NonunitExit.lean` |
| Two-class order reversal and compulsory grade tie | Two new Lean theorems in `DisjointGradeCrossing.lean` |
| One-bit-lag transport, trit truncation and signed current identities | Six new Lean theorems in `PredictablePhysicalArms.lean` |
| Ordered unit exchange and the strict descent from 17 modulo 48 | Two new Lean theorems in `UnitResidueExchange.lean` |
| Two finite forbidden-block and pressure certificates | Fresh exact Python replays, each with two independent decoders; not Lean graph enumerations |
| P: native uniform pair tail | SOURCE-QUALIFIED PR 146 `GROWING_ADDITIVE_GAPS.md`, at `f431078244e868dc699fad011044f0d5e7f76437` |
| R: original regeneration and incidence | Previous PR 197 written results at the frozen baseline; their source qualifications persist |
| U1: uniform three-arm subcritical moment | SOURCE-QUALIFIED PR 195 `UNIFORM_TRIPLES.md`, at `1c6e750e2f6970e6d5456cba5a93c2f3de8c2a97`, including its stated mixed-clock uniformity input |
| Classical predecessor exponent \(.84\) | Krasikov–Lagarias, published Theorem 6.1; used with the PR 146 actual-label variation and directed-cut arguments |
| M: positive lower density for a fixed target | Separately source-qualified external reported formalization; used only by the stated summable-series and power-saving closing consumers |

The fresh Lean executions used version 4.34.1 and Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, with auto-implicit arguments disabled and warnings treated as errors. The main three-module build and the separate residue-exchange build cover **15 new public theorems**; all have only subsets of `propext`, `Classical.choice`, and `Quot.sound` as transitive axioms. No probability, pressure, information or infinite-series theorem is represented as fully formalized.

The connection to Yolcu, Aaronson and Heule is their mixed binary/ternary rewriting architecture and its ordinary directed-return obligation. The new forbidden-word certificate exploits both digit systems while keeping actual positive sources and their ordered colors. It does not give a terminating interpretation for their complete rule system. [Pinned sources](SOURCES.json) · [full execution and written reviews](../../../reports/ayh-resource-reset-20261124/unit-exit/README.md).

## Replay and the next mathematical step

From the pinned built Mathlib environment:

```sh
lake env bash /path/to/research/ayh-resource-reset-20261124/unit-exit/check_lean.sh
lake env bash /path/to/research/ayh-resource-reset-20261124/unit-exit/check_residue17_lean.sh
python -X utf8 -B /path/to/research/ayh-resource-reset-20261124/unit-exit/check_nonunit.py
python -X utf8 -B /path/to/research/ayh-resource-reset-20261124/unit-exit/check_residue17.py
```

The principal unresolved task is to bound the actual unit-defect moment in (3), or to control the order-preserving interior two-class remainder strongly enough to sum the original head rows. The information lower bound gives a precise alternative target: an incompatible upper bound for the current ordinary color observations on those same conditioned sources. None of these remaining estimates is supplied here.
