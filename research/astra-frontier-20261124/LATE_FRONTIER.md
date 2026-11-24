# Incoming work and combined conclusions

PR192–196 and substantive additions to PR188 arrived while the initial packet was under review. The frozen incoming heads are recorded in [late-frontier-pins.json](../../reports/astra-frontier-20261124/late-frontier-pins.json). We reviewed their main scientific claims before publication. Several overlap results obtained independently in this investigation; those shared results are credited below. All of these branches explicitly leave Collatz open.

## What the incoming results add

| Source | Conclusion retained after review | Consequence for a global proof |
|---|---|---|
| PR192, `be783656f0e889fe0d5318a2f7a9140099cb94b5` | Two-sided separation of the actual scalar phase from ternary grids; every finite canonical word occurs in an explicit path first reaching one two further odd steps after that word; a superlogarithmic residual polynomial degree; rational cycles saturating every component norm. | Fixed-source approximation restrictions coexist with complete finite canonical language. Polynomial survival and nonzero norms do not force a surviving denominator at the integer evaluation. |
| PR193, `c6cb5e66516a86c33a757154983bbddc822510de` | Unbounded guarded smaller partners, the full odd-count merger obstruction, its first-tier sharpening, translated-interval synchronization, and an ordinary density of sources needing larger cost at the first endpoint. | The least input in each merger fiber remains untreated; the guarded progression does not cover an arbitrary prescribed source. Its S3 combines with our even-input bound below. |
| PR194, `b1bf1f151a2da8936f80d229f132d0b7539ba42c` | The non-erasing binary gap-block substitution theorem; actual carry/occupation bounds and least-source residue restrictions. | The central binary theorem is shared work, not a priority claim of this packet. A universal itinerary presentation or a suitably low guarded visit is missing. |
| PR195, `a24ef018147a1e16bf314d14085e2d0d6c620d32` | A literal smaller partner on a reverse-closure section and examples there whose shortest walk to a smaller source has order log log n; a finite-state shadow obstruction. | This is a distinct successful section, with different dyadic and ternary shadows. Coverage of every possible least nonconverger remains open. |
| PR188, `f98262be4ea40068dc88c779a767a9400a8bcaa3` | Actual-source finite word packing, stronger necessary canonical multiplier growth, sharp local carry penalties, and translated-band cycle exclusions. | Low phases with exponential multiplier growth satisfy the new growth tests. Arbitrary cycle defect support need not lie in one excluded band family. |
| PR196, `10fcd50c45c219d8f794034f8d46d127d86e562c` | At least square-root edit separation from critical mechanical words, stronger growth for polynomial factor complexity, full-denominator rotation tests, and a guarded half-size merger. | No theorem forces all exceptional words close enough to a mechanical comparison, forces repeated half-period factors in every cycle, or forces access to the successful merger guard. |

Full claim-specific reconstructions: [PR192 and the PR189 correction](../../reports/astra-frontier-20261124/PR192_189_REVIEW.md), [PR193 and PR195](../../reports/astra-frontier-20261124/PR193_195_REVIEW.md), [PR194](../../reports/astra-frontier-20261124/PR194_REVIEW.md), and [PR188 and PR196](../../reports/astra-frontier-20261124/PR188_196_REVIEW.md). The reviews retain explicit source-qualified analytic inputs and distinguish independently rerun controls from upstream execution receipts.

## Substitution attribution and the formal addition

PR194 ABR-4 already proves the nonidentity non-erasing binary theorem for two nonempty physical gap blocks, including finite shifts. Its shared-center argument already explains periodic concatenation. Our independently developed proof reaches the same main conclusion. In the fixed-letter case its proof proceeds through a minimal polynomial, rational divisor orders and partial fractions; our proof uses high/low radix indices to obtain a constant recurrence and then a numerator/denominator degree argument.

The current packet explicitly includes erasing substitutions, empty codewords with infinite output, and raw shortcut-parity blocks. The erasing cases reduce to periodicity. The main formal addition is the exact determinant-commutation equivalence for all physical monomial iterates and its connection to an actual infinite substitution fixed sequence. PR194's finite Mahler module includes the original eight PR190 finite identities; it does not contain these two new formal interfaces. Neither packet formalizes the complete analytic transcendence theorem or proves that an arbitrary exceptional ordinary itinerary belongs to the class.

## A stronger combined merger bound

Use the shortcut map T, positive integers x<n, nonnegative clocks a,b, and let p count odd inputs on the first a steps from x. Assume

\[
2^b\mid n+1,\qquad T^a(x)=T^b(n),\qquad e=v_3(n)\ge1.
\]

PR193 S2 contains both p>b+e and the same CRT obstruction with a representative below 6^H. Our frozen odd-input proof is an independent reconstruction of these results. PR193 S3 further rules out p=b+e+1. Its signed comparison state would have exact denominator three. If it is negative, becoming nonnegative forces the first odd step from minus one third to zero, and all remaining odd inputs must lie in the final source-length suffix, contradicting e>=1. If it is positive, the only possibilities below one are one third and two thirds; their subsequent ordinary one-two cycle cannot fit the required odd count without making the comparison slope exceed one. Thus

\[
p\ge b+e+2.
\]

Our [even-input refinement](EVEN_INPUT_REFINEMENT.md) independently proves a-p>e log2(3/2) by translating the remaining finite history to a positive integer and using its strict terminal carry bound. Adding the inequalities yields the combined written corollary

\[
\boxed{a>b+2+e\log_2 3.}
\]

The review independently checked this stronger combined inequality on all 577 applicable mergers in the specified finite box. The unrestricted statement rests on the two written proofs; no Lean proof of the combined inequality is claimed.

The positive constructions can also coexist. CRT intersects PR193's unbounded guarded smaller partner with our progression having H initial odd steps followed by s=ceil(H log2(3/2)) even steps. Each member then has both a smaller partner at its first forward endpoint and its own first descent exactly at H+s. This is an infinite progression, not a covering of every integer.

For the shortest undirected ordinary walk length D(n) and the two-arm horizon tau(n), reducing a walk gives tau<=D<=2 tau. Our least descending representatives therefore satisfy D(n)=Theta(log n). PR195 supplies a different family on its reverse-closure section with D(n)=Theta(log log n) and a specified partner. These are different domains and bounds; neither construction can substitute its new source for one arbitrarily prescribed in advance.

## A concrete surviving phase comparison

The new necessary growth conditions and edit-separation conditions do not contradict each other. For the low canonical phase b=(2,1) repeated indefinitely,

\[
p_b(m)\le2,\qquad P_{2k}=(9/8)^k.
\]

This exponential growth exceeds every polynomial and meets the stronger subexponential growth demanded for bounded factor complexity. Its discrepancy from the critical slope ell=log2(3) is (ell-3/2)N+O(1). The edit comparison itself therefore forces a linear number of edits, more than the new square-root lower bound. These conditions are mutually compatible.

This calculation does not produce an ordinary source realizing that phase. The canonical digit word is also not the physical parity or gap word to which the substitution theorem applies. The actual carries may retain the unresolved information. This is a specific interface where combining the latest necessary conditions still stops.

## Cycles, same-source laws and attribution

Our minimum-arc theorem constrains one contiguous first-crossing segment. PR196 constrains repeated half-period factors, and PR188 excludes certain localized defect profiles. No reviewed argument makes a sufficiently long minimum arc force either of those prohibited configurations. PR192's explicit rational cycles show why surviving polynomial degree and nonzero component norms alone cannot exclude numerical cancellation. They are rational controls, not integer counterexamples.

PR189's change from `a0be70b1ffa075cbc50755ac76036108c028d120` to `a390a1a4c75ee95db98b4b683d17c503f4e4a118` is attribution only. PR180 `7cfd911d35382d9d3bc988060ba88ade78a4267e`, `research/whole-source-20261123/COLLISION_CORE.md`, sections 3–4, equations (16)–(17), first proves the stationary collision-dimension deficit that PR189 S1 rederives. This deficit means larger collision probability and agrees in direction with PR185's empirical lower bound. An opposing ordinary endpoint estimate on the same law is still absent.

The late review independently compiled PR193's `ShadowCore.lean` and PR195's `CycleShadows.lean`, with 10 and 9 reported axiom dependencies respectively, and reran specified arithmetic controls. Those incoming modules are not counted among this packet's ten delivered modules or 90 reports. The other incoming Lean graphs are source-qualified by their pinned receipts. No incoming result converts the current collection into a universal Collatz proof.
