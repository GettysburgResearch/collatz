# Round twelve: large cycle factors and finite tower merger classes

**Status: PROPOSED written results, verified finite Lean kernels, and source-qualified trace implications. Collatz remains OPEN.** This pass adds a uniform obstruction to complete cycle-denominator cancellation, proves finiteness of a natural merger relation on every positive tower, extends the finite-template obstruction to both ordinary arms, and locates a possible escape in very narrow original-source intervals. The written global theorems have reconstructed peer and root reviews; their complete analytic proofs have not been formalized.

The map throughout the ordinary results is the shortcut map
\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]
The cycle result concerns the bounded least-tripling-disagreement branch in the existing reduction. Its rational controls are expressly separate from positive integer cycles.

## 1. A cycle's denominator must be carried by very large factors

The bounded branch has a coprime period pair \(p<h\le2p\), a near-critical height, and rank polynomial
\[
F(X)=\sum_{r=0}^{p-1}c_rX^{p-1-r},\qquad c_r\in\{1,2,4\}.
\]
Write \(D=2^h-3^p\). There is a unit \(u\bmod D\) with \(u^p=2\), \(u^h=3\). The exact reduced cycle denominator is
\[
d=\frac{D}{\gcd(D,F(u))}.
\]
An ordinary candidate requires \(d=1\); cancellation at one prime is insufficient.

For each irreducible factor write \(G(X)=H(X^t)\), with maximal \(t\), and call \(\deg H\) its compressed degree. For every sufficiently large ordinary candidate, at least one noncyclotomic factor has compressed degree
\[
\deg H\gg\frac{p(\log\log p)^3}{(\log p)^5}.
\]
For every fixed \(\epsilon>0\), the factors of compressed degree greater than \(p^{1-\epsilon}\), collectively, must absorb a divisor of \(D\) of size \(3^{p-o(p)}\). All smaller compressed factors and all cyclotomic factors together can absorb only \(\exp(o(p))\).

The main new finite estimate is
\[
\log\gcd(D,V(u))
\ll N+L+\sqrt{pN(1+L)},\qquad L=\log M(F)\le\log(4\sqrt p),
\]
for any selected product \(V\) of noncyclotomic irreducible occurrences, where \(N\) is the sum of their compressed degrees. Multiplicities and shared prime powers are included. An anisotropic integer box gives a short relation between \(p,h,t\). It supplies an auxiliary binomial with a common modular root and a nonzero integral resultant. Reduction modulo three excludes a common algebraic factor in one case; irreducibility of a positive-root binomial excludes it in the other. The resultant bounds the whole gcd. Dobrowolski's published Mahler-measure theorem then controls the number of factors, and Wu–Wang supplies the determinant's exponential scale.

This is a uniform bound for changing rank polynomials, rather than an application of a fixed-polynomial exceptional-set theorem. It permits arbitrary numbers of dilated factors. It still permits a legal irreducible polynomial of degree comparable to \(p\) to absorb all of \(D\). Excluding that possibility is the first unsupported cycle step.

[Full proof and literature](cycle/README.md) · [Finite Lean kernels](cycle/FactorObstruction.lean) · [Exact controls](cycle/check.py)

## 2. Finite augmented classes and ordinary mergers with bounded clock difference

Fix \(w>0\) and let \(x_r=3^rw\). Let \(P_h(x)\) count the odd departures in the first \(h\) shortcut steps. Link \(r,s\) when, for some common clock \(h\),
\[
T^h(x_r)=T^h(x_s),\qquad r+P_h(x_r)=s+P_h(x_s).
\]
**Every such equivalence class is finite**, for every fixed positive tower, whether the reference trajectory reaches 1, a hypothetical nontrivial cycle, or is nonperiodic. Hence every tower has infinitely many class-minimum exponents.

The elementary estimate behind the proof is uniform over every finite simple path:
\[
\#\{n\text{ on the path}:n\le X\}\le6X^{79/80},
\qquad
\sum_{\substack{n\text{ on the path}\\n\ge M}}\frac1n\le480M^{-1/80}.
\]
It bounds the multiplicative correction
\[
D_h(x)=\frac{2^hT^h(x)}{3^{P_h(x)}x}.
\]
For a nonperiodic reference, equality of corrections forces each linked source through a bounded set of small odd gates. If two such sources use the same gate, their elapsed times there must agree. Each fixed gate at a fixed time has finitely many ordinary preimages. For a periodic reference, the invariant
\[
L(r+P_h(x_r))-qh
\]
at a first visit to a designated cycle phase instead bounds \(r\), since \(2^L>3^q\).

A further unconditional written consequence dispenses with the odd-count condition. Fix any non-eventually-periodic positive reference \(y\), any \(w>0\), and any \(B\). Only finitely many exponents \(r\) can satisfy
\[
T^h(3^rw)=T^k(y),\qquad |h-k|\le B.
\]
Neither clock itself is bounded. The correction estimate leaves only finitely many possible relative clock and grade pairs; sources in each pair are augmented-linked.

An exact binomial calculation also bounds the reciprocal mass of odd departures above \(2^{64}\) by \(2.836949\), rounded upward. It makes ordinary same-clock meetings automatically augmented on such high simple paths. Extending that last identification to all hypothetical nonperiodic orbits additionally uses Bařina's published finite verification. The finite-class and bounded-lag theorems themselves need no external computational coverage.

[Finite-class proof](arithmetic/README.md) · [Ordinary bounded-lag theorem](arithmetic/HIGH_GATE.md) · [Ten Lean kernels](arithmetic/AugmentedMerger.lean)

## 3. A fixed finite template bank misses infinitely many required mergers

Fix an odd \(w\) prime to three, a finite bank of nonempty parity words, and a block budget \(K\) on each arm. Each block may repeat its word arbitrarily many times. For infinitely many \(r\), no two such actual ordinary trajectories merge from \(3^rw\) and any lower-cone start
\[
2^i3^sb,\qquad b<w\quad\text{or}\quad b=w,\ s<r.
\]
Both clocks, the initial halving factor and all repetition counts are unbounded.

The written proof uses Evertse–Schlickewei–Schmidt's finite-rank unit-equation theorem. Normalize the affine meeting equation by the arm with the greater total odd count. A minimal vanishing subsystem either bounds the primary source's ternary valuation or cancels exactly the two leading terms. In the latter case, sufficiently high sources force the same base, clock and augmented grade. Finiteness of augmented classes then supplies infinitely many misses. If the bounded-valuation arm is the competitor, bounded seeds have finitely many actual endpoints under the prescribed block budget; this treats the otherwise uncontrolled second arm. Initial halvings are handled separately, including a clock ending before they finish.

This does not identify those missed exponents as divergent. Even on the \(w=1\) tower, a convergent source can be a class minimum. It shows why a universal merger construction must go beyond a fixed bank with a bounded number of powered blocks. [Two-arm proof and all cases](arithmetic/README.md)

## 4. Retaining the original source in the trace problem

**The lower implications here assume the external, source-qualified renewal floor F** from Weaver–Wren paper 48 v2. They do not establish that analytic input or unconditional escape exclusion.

For an escaping odd unit \(a\), let \(q_i=U^i(a)\), let \(A_i\) be its accumulated odd-gap clock, and let \(D_i\) be its correction product. At balanced grade \(b\), put
\[
B_i=q_i(4/3)^b/D_i=a3^i2^{-A_i}(4/3)^b.
\]
For each selected actual endpoint \(q_i\), inverse words with high relative carry must have positive normalized mass in the original integer-source interval
\[
\frac1{a2^e}\le1-\frac{x}{B_i}\le\frac{1+3F_0}{a2^e},
\]
with mass at least \(c_a2^{-e}/\sqrt b\). This persists separately in every prescribed ternary unit class modulo \(3^k\), with the factor \(3^{-k}\), within F's depth range.

Summing disjoint intervals at \(e\asymp\sqrt b\) forces a positive one-sided inverse-distance moment inside relative radius \(O_a(2^{-\sqrt b/8})\), at each selected terminal separately. An upper bound tending to zero for that exact moment would exclude escape under F. No such upper bound is proved here.

There is also an unconditional limit on a uniform strengthening of F. At prefix grade \(n\) and clock \(s\), covering every unit terminal with even one fixed source residue modulo \(3^k\) requires
\[
2\cdot3^{n+k-1}\le {s-1\choose n-1}.
\]
At \(s=2n\), this forces
\[
k\le n\log_3(4/3)-\tfrac12\log_3 n+O(1).
\]
Even that maximum uniform depth leaves the residue mesh smaller than the absolute source interval. A contradiction based only on making a globally uniform ternary mesh finer cannot complete this route.

The note separately proves actual-path phase discrepancy using bounded variation and translated interval sparsity. Under F it yields positive mass proportional to every sufficiently wide moving mantissa interval after both integer endpoint cutoffs: cofinally at widths \(Cb^{-1/4}\), or at every large depth with widths \(Cb^{-4/41}\) using Wu–Wang.

[Trace proof and qualification of F](trace/README.md) · [Seven Lean kernels](trace/TraceWindow.lean)

## Final Lean proposal, evidence and remaining obligation

The existing [FinalProposal.lean](../round11/formal/FinalProposal.lean) is retained and rebuilt. Its universal conclusion still requires the explicitly open hypothesis

    remaining : FrontierMerger

The exact predicate is in [SmoothCore.lean](../round10/vendor/SmoothCore.lean): it requests an actual merger to a smaller base or earlier same-base power in each surviving arithmetic case. No new assumption is hidden in an axiom or renamed as a proved input. The new kernels do not discharge this predicate.

The root rebuilt **13 project modules from source in an empty project output cache**, including ten unchanged dependencies and the retained final proposal. **109 selected transitive axiom inventories passed, 26 in the three new modules.** Only the allowed standard axioms appeared. The pinned compiler and Mathlib/package binaries were reused. Full asymptotic results, external analytic proofs and published exhaustive computations were not rebuilt.

Three exact control programs were replayed in normal and optimized Python, with explicit failures active in both modes and byte-identical outputs. They include 81 small rank words, prime-power cancellation \(7675=5^2\cdot307\), 178 literal source-shell identities, finite tower class checks, and the 1,936-term reciprocal certificate. A rational basin control closes all 17,076 visited numerator states, giving an all-depth conclusion for its finite list of starts; it supplies no ordinary counterexample.

[Source and toolchain ledger](SOURCES.json) · [Root review](../../../reports/astra-global-closure-20261124/round12/ROOT_REVIEW.md) · [Intake and source pins](../../../reports/astra-global-closure-20261124/round12/INTAKE.md) · [Lean receipt](../../../reports/astra-global-closure-20261124/round12/lean/receipt.json) · [Control receipt](../../../reports/astra-global-closure-20261124/round12/controls/control-replay.json)

Reproduce the finite kernels and controls from a complete checkout:

    python -B research/astra-global-closure-20261124/round12/check_lean.py \
      --lean /absolute/path/to/lean \
      --mathlib /absolute/path/to/mathlib4 \
      --report-dir /absolute/path/to/lean-reports
    python -B research/astra-global-closure-20261124/round12/check_controls.py \
      --report-dir /absolute/path/to/control-reports
    python -X utf8 -B tools/validate.py --receipt /outside/checkout/validation.json

The exact unresolved step is pointwise: construct an unrestricted ordinary merger for each first failure, or exclude both a surviving large-factor cycle and an escaping orbit on their actual integer sources. Neither density-one merger coverage, rational basin separation, finite template catalogues nor a Haar-average trace replaces that step.
