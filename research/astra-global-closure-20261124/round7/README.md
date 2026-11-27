# One directed suffix, ordinary-orbit determinants and completed paired fibers

**Collatz remains OPEN.** This continuation starts from the published round-six head fbe68bf1b13b797843691080d782f4262a5c4468 and the refreshed repository interfaces. It supplies two finite directed global equivalences, a single-suffix reduction of the actual head series, a new determinant estimate along one fixed ordinary escape, and a completed central paired construction with its exact ordinary-target cost. The asymptotic results are proposed written proofs with the named external inputs. Lean checks the finite arithmetic and the directed global consumers; it does not formalize the external analytic theorems.

Use the positive shortcut Collatz map

\[
T(x)=\begin{cases}x/2,&x\ \text{even},\\(3x+1)/2,&x\ \text{odd}.\end{cases}
\]

Let \(C(x)\) mean that some iterate is 1. An odd ternary unit is a positive odd integer not divisible by three.

## 1. A single directed unit implication is sufficient

Each of the following statements separately is equivalent to Collatz:

\[
\forall u\text{ an odd ternary unit},\quad C(u)\Longrightarrow C(3u);
\]
\[
\forall u\text{ an odd ternary unit},\quad C(3u)\Longrightarrow C(u).
\]

The first implication has a complete 40-leaf affine descent certificate; the second has 172 leaves. They use ordinary steps in either direction and only the displayed orientation of the extra unit comparison. Every certified source progression ends at a strictly smaller positive integer. Strong induction consumes the literal finite cover. The largest residue moduli are 144 and 186624, respectively. This is an unconditional equivalence, with the unit implication still a hypothesis.

A separate 33-leaf substitution connects every positive odd \(n\) to \(3n\) by ordinary segments and odd-unit comparisons. Its 59 comparison positions give, for any invariant label,

\[
D_{\rm odd}(X)\le59D_{\rm unit}((59/3)X),
\]

where each count concerns actual tripling disagreement. No distribution of labels or finite synchronization deadline enters this inequality.

PR197's existing routing then needs just **suffix 57 modulo 81**. For \(27b=2^ku+1\), the head parent \(y=8b-1\) and child
\[
x=81y+57=2^{k+3}(3u)
\]
reach \(u,3u\) at the same clock \(k+3\). Powers \(k\) in an arithmetic progression place these heads in any fixed open mantissa arc inside \((7,8)\), any fixed row congruence class, and any fixed initial-even requirement. Either one directional condition on every sufficiently high selected head is already sufficient.

Let \(a_j\) count all actual head disagreements in \([7\cdot81^j,8\cdot81^j)\), normalized by \(81^j\), and let \(s_j\) count both directions on this restricted single suffix with the same normalization. Then
\[
\sum_j a_j<\infty\quad\Longleftrightarrow\quad\sum_j s_j<\infty.
\]
The finite affine substitution and harmonic-weight comparison also transfer an \(o(X^\alpha)\) count for every fixed \(0<\alpha<1\). At \(\alpha=.84\), the pinned predecessor-based rigidity criterion therefore gives a sufficient closing estimate without the newer positive-density floor. This exponent concerns the union of the two directions.

The pointwise test can be reduced further by requiring that the odd part of the child be at most any prescribed function of the row tending to infinity. That growing restriction is only a pointwise equivalence: its row fractions can already be summable without resolving any particular test.

The selected odd pairs left in round six also have an exact interface. Six physical prefixes cover all 243 relevant ternary cells. Together with one native case, they send each supplied odd pair \((v,9v+2)\) into one pair \((u,3u)\) in the same ordered ordinary components, with \(u<24000v\). On the residual \(3^{18j}-1\) family the first arm has an explicit path to 1. Its triple remains the open arm. The actual first-arm clock increases in this construction, so that clock is not a decreasing induction parameter.

[Directed certificates and series](head/README.md) · [Selected odd pairs](head/ODD_RAY.md) · [Global Lean consumer](head/UnitTripling.lean) · [Literal odd-pair Lean proof](head/OddUnitLift.lean).

## 2. Full cancellation on one fixed ordinary escape

Fix an ordinary source \(n\) with an injective forward orbit \(x_i\), and write \(p_i\) for its odd count. The companion clocks and carry are
\[
Q_i=3^i,\qquad A_i=2^{i+p_i},\qquad
C_i=\sum_{j<i}e_j2^{j+p_j}3^{i-1-j}.
\]
Its rational periodization has reduced denominator
\[
\frac{|A_i-Q_i|}{G_i},\qquad G_i=\gcd(|A_i-Q_i|,C_i).
\]
Here \(G_i\) is the entire numerical cancellation, including every prime power.

For each fixed \(\epsilon>0\), the new written determinant argument proves:

| Hypothesis on that same orbit | Number of \(i\le X\) with \(\log G_i\ge\epsilon i\) |
|---|---|
| \(x_i=O((i+2)^C)\), fixed \(C\) | \(O_{n,C,\epsilon}((\log(2+X))^2)\) |
| \(\log(x_i+1)=O(i^\beta)\), fixed \(0<\beta<1\) | \(O_{n,\beta,\epsilon}(X^\beta)\) |

It uses degree-\(d\) homogeneous forms through \((1:1:0)\). The exact content of their evaluation vector is \(G_i\). The real, binary and ternary determinant estimates cancel the leading clock factors. A grouped Vandermonde term proves nonvanishing when the selected clocks are sufficiently separated relative to the actual binary agreements of their ordinary endpoints. The latter valuations are bounded by the endpoint heights in the two displayed regimes. This argument allows the genuine dyadic companion value to be transcendental.

There is also an individual-clock result under the explicit additional hypothesis that the genuine companion is algebraic. Schlickewei's Subspace Theorem applies to primitive integer evaluation vectors. The earlier fixed-source Siegel argument excludes the exceptional rational subspaces. It gives \(\log G_i=o(i)\) on every subsequence where the real zero-trial companion is subexponential. This includes every physical record height, and every clock on an escape whose exponential growth rate has a limit. Conversely, infinitely many fractional losses there would prove the genuine scalar transcendental.

These estimates do not force a single large cancellation. Full leading denominators can coexist with an escaping parity stream. At a complete physical cycle lap, the Vandermonde factor involving the initial source vanishes exactly; the proof does not exclude a nontrivial ordinary cycle.

[Determinant proof](arithmetic/README.md) · [Algebraic alternative](arithmetic/ALGEBRAIC.md) · [Finite Lean kernel](arithmetic/CompanionContent.lean).

## 3. Complete central pairs and the ordinary endpoint

Under the named one-arm floor F and the named ordinary trajectory estimate H, every sufficiently large central clock row at each fixed supplied ordinary unit \(q\) has a near-optimal family of first-arm predecessors. A subfamily of size
\[
G\exp(-O_{q,m}(\sqrt{e\log e})),\qquad G=2^e/3^p,
\]
has one exact companion endpoint \(Y\) and one odd-count difference \(k\), for any fixed multiplier \(m\). Both \(\log(1+Y)\) and \(|k|\) are \(O_{q,m}(\sqrt{e\log e})\). The weaker \(o(e)\) version uses F and Inselmann's trajectory theorem instead of H. These statements keep \(q\) fixed; they do not assert \(Y=mq\).

For \(m=5\), exact state steering and a short binary extension give genuinely completed ratio-five rows with equal odd counts, a bounded real offset, and the same near-optimal exponential rate. Their ordinary endpoint \(Q\) is controlled precisely:
\[
2^hQ\equiv M\pmod{3^{P+1}},\qquad
0<M<2^h,\qquad
\frac{M+3^{P+1}}{2^h}\le Q<1+6\cdot3^P,
\]
where \(h=O_q(\sqrt{e\log e})\) and \(P=p+O(h)\). Thus the correction uses sublinear clocks but its fine ternary cell has no small ordinary representative. In fact the constructed \(Q\) is its least positive odd representative, as reconstructed in the independent review. The supplied target \(q\) has not been retained.

Two unconditional results identify the cost of possible repairs:

* If an \(e\)-step prefix with \(p\) odd inputs ends at \(q<3^p\), every other positive source with the same prefix ends at \(q+3^pt\), \(t\ge0\). A further \(h\)-step visit to \(r\) with \(2^hr<q+3^p\) forces the original source and the actual future \(T^hq=r\). At a nonperiodic \(q\), a positive return through a different lift costs at least \(\log_2(1+3^p/q)\) clocks. The theorem also treats arbitrary short tail replacements.
* The full ordinary graph of completed ratio-five inverse blocks has distinct terminal roots 1 and 5. Their terminal descendant classes give a nonconstant bounded edge invariant for every supported stochastic reweighting or finite inducing. A general Liouville claim on that full marked graph is therefore false, even though both terminals converge under ordinary Collatz.

A separate Subspace Theorem argument treats sparse changes throughout a word. Fix a number \(s\) of altered **ordered odd positions**. If two actual words have the same central clock, odd count and ordinary endpoint, every altered odd rank is \(o(e)\), uniformly over that endpoint. The quantifiers keep \(s\) fixed; the conclusion does not concern an arbitrary \(o(e)\)-sized edit set or the ordinary Hamming distance of parity strings. For a single altered rank \(j\), the sharper exact constraint is \(2\cdot3^j\mid\Delta\), where \(\Delta\) is its displacement. This forces \(j=O(\log e)\). The written proof includes a nonvanishing argument for the last cluster and a dimension induction handling degenerate sums of units.

Tripling has a distinct physical boundary. For odd \(x\), the number \(T^e(3x)\) is prime to three at every positive clock. Thus the exact pair \((q,3q)\) has no such inverse starts at all, even with unequal positive clocks. Under F, the pair \((q,q)\) instead has \(\gg_q G/\sqrt p\) starts with first-arm offset at most \(1/2\) and odd counts \(p,p-1\). The entire cylinder \(x=23+32t\) supplies the initial merger. To propagate a failure of the directed unit implication, a construction must retain the convergence component of \(3q\) through a successor or common future; equality with \(3q\) itself cannot be the terminal requirement.

A concrete common-future construction survives this boundary. For every positive \(q\equiv271,433\pmod{486}\), write \(q=28+81t\) and \(x=1415+4096t\). Both are odd ternary units, and the literal words give \(T^{12}x=q\) and \(T^{13}(3x)=T(3q)\). This preserves the two ordered components of each such supplied pair. Its source satisfies \(x>q\); the construction alone supplies no descent or central count at an arbitrary target. The [independent review](../../../reports/astra-global-closure-20261124/round7/arithmetic/TRIPLING_REVIEW.md) gives both words, their carries and the infinite affine lift.

The two-ended bridge from the latest PR201 can also be composed with the bounded-offset paired construction. It retains \(\Omega(\sqrt p)\) actual initial complete marks at the same exponential rate, conditional on its named first-mark tail R in addition to F and H. This supplies genuine marks in the selected family, while the subsequent ratio-five correction still has the large ordinary endpoint \(Q\).

The missing fixed-target paired estimate still requires the needed relative state in the original central inverse family. One-arm abundance, short symbolic control and an almost-everywhere assertion about a ternary measure do not provide it.

[All statements, proofs and analytic qualifications](renewal/README.md) · [Sparse edits and the new bridge](renewal/SPARSE_EDITS.md) · [Tripling endpoints](renewal/TRIPLING_FIBER.md) · [Physical and graph Lean kernel](renewal/ShortSuffix.lean) · [Tripling Lean kernel](renewal/TriplingBoundary.lean).

## 4. Repository synthesis and remaining closing steps

PR197's new graph and future-fiber arguments are retained with their original event and normalization. PR193's latest head changes publication receipts only. The later PR201 two-ended bridge retains initial marked events at an exact ordinary endpoint, while leaving its terminal relative state open. Its new escape criterion concerns a uniform high-relative-offset tail; the small-offset families constructed here do not bound that tail. PR200's PT/FS distinctions and PR203's floor F remain explicit.

The present packet does not establish either directional unit implication, a summable single-suffix disagreement bound, an unavoidable denominator-cancellation contradiction, or the required central paired mass at every supplied ordinary target. Those are substantive mathematical gaps, rather than missing finite execution.

[Latest intake](../../../reports/astra-global-closure-20261124/round7/LATEST_INTAKE.md) · [Coordinator review](../../../reports/astra-global-closure-20261124/round7/ROOT_REVIEW.md) · [Frozen source ledger](SOURCES.json).

## 5. Formal and finite replay

The five local modules have no local project imports. The replay rebuilds them into an empty project cache using the pinned Lean/Mathlib environment, treats warnings as errors, and checks 40 selected transitive axiom inventories. Existing Mathlib and package objects are reused. The five finite arithmetic scripts are independently replayed under normal and optimized Python against their canonical outputs.

Use check_lean.py with explicit --lean, --mathlib, optional --runtime-library and --report-dir arguments. Use check_controls.py with --report. The resulting receipts record exact hashes and source immutability. The repository validator must also be run in a clean complete checkout of the publication candidate. These checks have separate scope from the proposed written asymptotic theorems and external inputs.
