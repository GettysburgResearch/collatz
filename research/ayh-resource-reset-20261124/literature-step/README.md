# Actual source transfer, spatial mixing and future parity marks

**Collatz remains OPEN.** This fourth checkpoint pursues the global step behind the Aaronson–Yolcu–Heule head reduction. It connects that ordinary section to long-orbit estimates, quantitative irrational rotation and the Pliss selection principle. Four GPT-6.2 Astra attack streams and the parent developed and reviewed the work. The strongest new formal result is a positive time-density theorem for actual pairs whose convergence outcomes differ. The strongest new counting result transports power-small tests to actual sources after a long descent, with their original conditioning retained.

The six new Lean modules contain **21 public theorems**. Their exact statements are narrower than the full analytic arguments; the table below records that distinction. Neither the source transfer nor the closing criteria supply the remaining global estimate.

Throughout, the ordinary shortcut is
\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]
A common future permits two different finite clocks. Write \(p_n(t)\) for the number of odd inputs before clock \(t\), \(R=81^j\), and use the actual head edges \(x=81m+r\in[7R,8R)\), \(0\le r<81\). These are the same four-trit edges in the [previous kernel-checked reduction](../continuation/FIXED_HEAD.md), derived from the blocked AYH prefix. Every positive integer reaches that larger head section or the verified base in at most ten physical clocks.

## 1. Different convergence outcomes force many biased future windows

Suppose \(n\) never reaches one, \(T^q(u)=1\), and \(n\le2^L\). The checked base below 600 gives a floor on the bad orbit. Exact integer arithmetic proves, at **every** clock \(t\),
\[
8\bigl(p_n(t)-p_u(t)\bigr)\ge t-C,
\qquad C=5L+4q+4.
\]
No bound on the supplied hitting time \(q\) is assumed. The separate real-log estimate improves the asymptotic lower speed to more than \(0.1306\). The signed terminal grade \(q-2p_u(q)\) is retained in a sharper finite formula.

The new forward Pliss theorem turns the integer inequality into an exact count. At least \((N-2C)/15\) times \(s<N\) satisfy
\[
16\bigl(p_{T^s(n)}(b)-p_{T^s(u)}(b)\bigr)\ge b
\quad\text{for every }b\ge0.
\]
Thus these marks have lower time density at least \(1/15\). This full implication, including the infinite-future quantifier and finite count, is now kernel-checked in `CollatzShell.TernaryHead.discordant_mark_count`, in the module `DiscordantPliss`. A separate checked construction gives actual future height-minimum windows arbitrarily late. The two families of clocks need not coincide.

The marks may depend on future information. Their density in **time on one pair** is not a density among **original ordinary sources**. The current estimates show that, outside a power-small set of head sources, no such mark occurs before any fixed fraction less than one of the critical time
\[
\frac{\log_2R}{\log_2(2/\sqrt3)}.
\]
This identifies the remaining issue as control of later marked windows, rather than a missing elementary parity inequality. [Full proof and source-count criterion](BALLISTIC_COLOR.md) · [Physical orbit inequalities](BallisticColor.lean) · [Forward record count](ForwardPliss.lean) · [Actual pair instantiation](DiscordantPliss.lean).

## 2. A long descent can preserve quantitative information about the source

Fix \(0<\alpha<1\), put \(a=\log_2(2/\sqrt3)\), and use the actual common clock
\[
h=\left\lfloor\frac{(1-\alpha)\log_2R}{a}\right\rfloor.
\]
For \(\alpha<\log_2\sqrt3\), this is beyond the initial binary-digit window. At this clock orient the endpoints as \(z,3^s z+D\), retaining the orientation, exact odd counts and integer offset. A family of tests may choose a different forbidden set of binary residues for **every** resulting profile.

If each forbidden set has proportion at most \(2^{-\sigma b}\), where \(b=\lfloor\alpha\log_2R\rfloor\) and \(\sigma>0\) is fixed, the number of original head children that fail their assigned test is \(O(R^{1-\delta})\) for some \(\delta>0\). The estimate remains an absolute bound after intersecting with any original source selection. If that selection has \(R^{1-o(1)}\) members, division gives a power-small conditional fraction. No relative conclusion is asserted for an unspecified much smaller selection.

The proof gives a self-contained finite-stage form of the orbit estimates in Inselmann's 2024 paper. Its added joint argument controls the number of profiles and the actual preimage multiplicity. The exact bound
\[
1\le\frac{T^h n}{3^{p_n(h)}2^{-h}n}
\le\left(1+\frac1{3M}\right)^h
\]
holds when every preceding input is at least \(M>0\); its division-free form and the corresponding same-endpoint inequality are Lean-checked.

Two consumers give a power saving for failures that spend a fixed fraction of time in a finite collection of states with merger certificates, and for fixed linear changes in the signed odd-count difference. Neither consumer controls all forever-failed head edges. The explicit exponent can be extremely small and does not reach the previously required saving of more than \(0.16\). [Transfer, constants and proof](POST_DESCENT_TRANSFER.md) · [Formal fiber inequalities](PostDescentFibers.lean).

## 3. Actual first-passage times and the remaining joint distribution

The last attack extends source control to adaptive first entrances. For a first entrance below an integer height \(Y\), a source bounded by \(U\), and a clock \(t\le3Y\), the kernel-checked theorem gives the exact finite bound
\[
\#\{n:\text{specified first-entrance time, odd count and endpoint}\}
\le 1+\left\lfloor\frac{tU}{3Y}\right\rfloor.
\]
It is a count of original integers. No distribution on the landing values is assumed. Summing this estimate controls exceptional endpoint tests at first-passage clocks.

The written application is simultaneous over all short windows: for any fixed \(A>1\), suitable constants \(D,K\) give \(M=(\log_2R)^D\), \(b=\lceil K\log_2\log_2R\rceil\), and at most \(O(R/(\log R)^A)\) original-source exceptions. Outside them, each arm enters below \(M\) within \(O(\log R)\) clocks, and every \(b\)-step window starting before its entrance plus \(b\) has odd count within \(b/40\) of \(b/2\). The upper time constant can be arbitrarily close to the usual critical constant. This simultaneously excludes the paired Pliss marks through the smaller of the two actual entrance times, plus \(b\); it also treats a partner already on the terminal cycle while the other arm remains in that range.

Polylogarithmic descent and original-source first-passage counting have prior treatment in Shaik's 2026 manuscript. This packet credits that work and gives a coarse self-contained proof for its sliding-window application. The two landing values are retained together, with their actual multiplicities.

In particular, let \(W_j(v,w)\) count original head children landing at the ordered pair \((v,w)\in[M/2,M)^2\) within the stated time bound. The head's number of different-color edges equals
\[
\sum_{v,w} W_j(v,w)\,\mathbf1_{f(v)\ne f(w)}
+O(R_j/(\log R_j)^A).
\]
Under the separately source-qualified positive lower basin-density input, summability of this weighted count divided by \(R_j\) would settle the conjecture. The displayed error is already summable over \(R_j=81^j\). **The joint weighted estimate remains open.** A bound on the number of possible landing pairs alone does not control their source multiplicities. [First-passage and sliding-window proof](FIRST_PASSAGE_MARKS.md) · [Exact stopped-fiber count](FirstPassageMarks.lean).

## 4. A different closing target: collisions in one shrinking interval

Let \(f(n)\) be any binary color constant along ordinary orbits and set
\[
G_j(v)=f(\lfloor81^{j+v}\rfloor),\quad 0\le v<1,
\qquad \bar G_j=\int_0^1G_j(v)\,dv.
\]
For every circle interval \(W\) and every convergent denominator \(q\) of \(\log_{81}2\), the written proof establishes
\[
\left|\int_WG_j(v)\,dv-|W|\bar G_j\right|
\le C\left(\frac q{\sqrt j}+\frac1q\right).
\]
The input is the frozen PR 146 affine-pair merger estimate. All weak-star accumulation points are therefore spatially constant. This does not assert that the means converge or that the constant is zero or one. At \(j=q^4\) the discrepancy is \(O(j^{-1/4})\); an elementary denominator bound also gives an all-level rate \(O(1/\log j)\).

Using Mazur's **separately source-qualified** positive lower natural density theorem for fixed-target predecessor basins, this yields a new sufficient condition for full Collatz: in one such interval of relative width \(j^{-1/5}\), along any sequence \(j=q^4\), two independently sampled ordinary starts have a common future with probability tending to one. Each sample may even be restricted to its own prescribed residue modulo
\[
2^{\lfloor j^{1/4}\rfloor}3^{\lfloor j^{1/4}\rfloor}.
\]
The residues may differ and vary with the row. The merger probability is **not proved**. In particular, the existing parent-child certificates have a different joint sampling law. The written transfer argument also proves that independent samples do not typically meet with either arm still at a fixed precritical time, even if the other arm's clock is unrestricted.

The external positive-density theorem and its advertised 388-file verification were inspected at their primary publication record; this checkpoint did not reproduce that external build. With only the published Krasikov–Lagarias exponent, the [previous \(R^{0.84}\) closing criterion](../continuation/HEAD_EDGE_RIGIDITY.md) remains the available alternative. [Spatial theorem, residue streams and exact input boundary](MACROSCOPIC_PAIR_CLOSURE.md) · [Four checked finite bridges](PatchPairCounting.lean).

## 5. Stronger smaller partners in the exact critical fibers

For every fixed \(\beta>0\), there are arbitrarily high common octaves in which, in **each** exact nonempty critical fiber, all but an exponentially small fraction of sources have an actual common future with a critical partner \(m<n^\beta\), at \(O_\beta(\log n)\) clocks. The proof reparametrizes the sparse original fiber by its densely spaced odd endpoint before using the descent estimate. It then uses the previous four-clock inverse row.

The partner may change the eight-valued surplus, and the theorem is on the displayed common scales. The earlier [same-surplus compression](../continuation/CRITICAL_COMPRESSION.md) applies at every sufficiently large fiber with a weaker power improvement. Neither statement controls the mass arriving at exceptional failed roots. [Full construction](CRITICAL_SMALL_SCALE.md).

## Proof scope and reproduction

| Module | Public theorems | Kernel-checked content |
| --- | ---: | --- |
| `PostDescentFibers.lean` | 2 | Physical multiplicative correction and source-fiber comparison |
| `PatchPairCounting.lean` | 4 | Binary and mixed-residue affine lifts, cross-color failed-pair count, finite rotation averaging |
| `BallisticColor.lean` | 7 | Bad/good odd counts, all-clock separation, exact grade, future height minima, integer-walk laws |
| `ForwardPliss.lean` | 3 | Existence of integer tail minima and quantitative all-future record counts |
| `DiscordantPliss.lean` | 2 | Positive-density future marks on actual discordant Collatz pairs |
| `FirstPassageMarks.lean` | 3 | First-entrance band, exact source width and finite stopped-fiber cardinality |

The analytic probability estimates, rotation discrepancy, critical common-scale frequency and global deductions are written proofs. The formal modules do not import the external positive-density theorem as an axiom. Run [check_lean.sh](check_lean.sh) inside the pinned Mathlib environment. It rebuilds the six new modules and their complete three-module local dependency closure into a temporary directory. The [evidence packet](../../../reports/ayh-resource-reset-20261124/literature-step/README.md) records the exact build, source hashes, finite census and independent reviews. [Source and dependency pins](SOURCES.json).

The outstanding global step is quantitative control of the original-source mass at late parity marks, or an actual dominant-component result on the independent residue streams above. Positive time frequency, marginal equidistribution and small failure counts at a fixed early clock do not themselves supply either conclusion.
