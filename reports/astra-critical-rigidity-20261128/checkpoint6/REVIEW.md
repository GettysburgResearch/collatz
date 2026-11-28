# Sixth coordinating review: a global ordered-carry reduction and an effective exception count

November 28, 2026. This is an intermediate checkpoint of the continuing nine-hour pass. Its preceding public head is `a837e10caac769b5b6344bac07d740f77531b978`, tree `7641e768552993b4548090db0a5465193a0d5381`. **Collatz remains unresolved.** All asymptotic statements below are proposed written theorems; their finite controls and formal kernels have narrower, explicit scopes. The exact reviewed sources are recorded in `SOURCE_MANIFEST.json`.

## Closing an arbitrary unmatched schedule

The coordinator independently reconstructed the complete proof of `ADJACENT_CYCLE_CLOSURE.md`, and the literature lane supplied a second independent review. The result covers arbitrary finite unmatched schedules, without a periodic-tail assumption and without the earlier 19,683-residue covering certificate.

For two equal-grade native words with carries \(C_U,C_V\), the static equation

\[
C_U-C_V=2^L-3^p
\]

preserves the relation \(A-B=1\). Final affine divisibility characterizes the entire physical parity word, so prescribing one arm forces the other word on the same nonempty dyadic cylinder. The actual initial class \(s\equiv3\pmod4\) reaches \(((9s+5)/4,(9s+1)/4)\), of difference one, in two native steps and three combined odd departures. Its lower coordinate ranges over every residue modulo every power of two. A final difference of one excludes every earlier synchronous collision. This proves \(M(P)+2\le K(2P+3)\), including the empty-maximum convention.

For the reverse direction, orient each actual affine relation as \(B=3^jA-a\). The level is at most \(G+1\), and the carry bound gives \(|a|\le3^{G+1}\). At positive level the translation is a ternary unit, justified by an ordinary representative of its full source cylinder. An initial U replaces the mandatory simultaneous odd departure and allows the given remaining calendar to be copied with one fewer combined odd departure.

Common even steps remove the two-adic valuation of \(a\). A D then lowers the level and sends \(a\) to \((a+3^{j-1})/2\). The only collapsing case \((1,-1)\) is replaced by the explicit U,E,D,D detour through \((2,-2),(2,-1),(1,1),(0,1)\). This lowers all levels at odd-grade cost at most \(j+2\), independently of the number of even steps. After restoring the original orientation, nonzero level-zero translations contract by either halving or \((3b\pm1)/4\), with the sign selected by exact divisibility modulo four. The absolute contraction is at most \(7/8\); the estimate \((8/7)^9>3\) supplies at most \(9(G+1)+1\) operations. A fixed nine-step physical word pair, taken from the source 7, reverses the remaining sign if necessary.

The resulting loop returns to translation one with equal arm grades \(p\le16(G+1)\) and native length at least the original prefix. This proves \(K(G)\le M(16(G+1))\). Every intermediate choice is a compatible physical refinement; the final nonzero translation rules out an intervening affine collapse. For long period-to-grade ratios the two rational word centers are positive and adjacent. Conversely, any pair of positive adjacent periodic phases lifts to infinitely many positive ordinary sources after excluding finitely many affine intersection roots. Thus the same global bound can equivalently be tested on positive adjacent rational cycles, and the equal-grade subfamily already suffices.

The central checker replays 7,927 actual positive prefixes, including 613 exceptional detours, 1,791 orientation swaps, 1,801 sign flips and 16,057 level-descent common-even steps. A negative adjacent-cycle control has native length 38 and equal grades 24. These tests support the routing identities; the universal reduction is the written induction and cylinder argument.

## Primitive examples at every exact grade

The coordinator independently reconstructed `PRIMITIVE_SPARSE_PAIR_CLOSURES.md`. At \(l=\lfloor\log_2p-2\log_2\log_2p\rfloor\), the thin center \(1/(2^l-3)\) has an entrance and exit of grade \(O(2^l)\). A common thin lap preserves the full relation \((j,a)\) exactly. Both outside calendars can therefore be fixed independently of the number \(R\) of inserted laps. Taking \(R=p-p_0\) gives exact grade \(p\) on each arm and length at least \((1-o(1))p\log_2p\).

The primitivity argument is material. Delete all common-even dates from the cyclic paired parity tape. Its \(R\) consecutive common-odd events outnumber all events outside that run, while the initial U supplies a mismatch. A nontrivial power containing a mismatch cannot have a mismatch-free interval longer than half its event period. The shortened word, hence the original native pair word, is primitive. This prevents repetition of a shorter paired cycle from explaining the bound.

The same physical closing construction works after any finite noncollapsed source cylinder. It produces distinct positive periodic phases at date one with equal density as small as desired and unbounded joint primitive period. Their odd rational preimage remains inside the supplied source cylinder. Conversely, a cylinder with identically merged terminal affine maps stays merged under every refinement. The survivor set is therefore exactly the closure of the specified thin periodic sources. A fixed generic merger word supplies an excluded subcylinder inside every survivor neighborhood, and the periodic constructions exclude isolated points. These are topological statements. Almost-everywhere paired coalescence is prior probabilistic work and is not claimed here as a new consequence or as an unresolved measure question. Further Hausdorff-gauge work is excluded from this checkpoint.

## Uniform origins, mean heights and arithmetic occupation

The coordinator independently reconstructed `UNIFORM_ROTATION_HEIGHT.md`. A wrapped length-\(L\) window sees, on average over all starts, \(Ls/p\) mismatches. Markov's inequality leaves a positive proportion with any chosen fixed mismatch budget. Applying the exact supplied-endpoint theorem to those actual windows, then letting the fixed budget grow after the period limit, forces paired height to exceed every fixed multiple of \(p/s\) outside a vanishing fraction of starts. The argument allows windows spanning several complete laps.

For the full rational denominator bound, sum or average the endpoint heights using their permutation across origins. Choose \(L\sim kp/s\), take budget slightly larger than \(k\), and retain a positive fraction of good starts. The exact denominator coefficient then gives \(\liminf s\log_2q/p\ge1/4\) whenever \(s\overline Z=O(p)\). The limits in the auxiliary slack, the fixed window multiplier and the period are kept in the stated order. The hypothesis involves the all-origin mean, not an unstated bound at mismatch events.

The balanced-minimum upgrade uses the exact PR213 source `5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128:research/astra-diagonal-frontier-20261127/arithmetic/ODD_HEIGHT_PRESSURE.md`. The coordinator re-read its pressure input: a constant \(u>0.0263\), less than one quarter, excludes low average cost on all but \(o(p)\) physical windows of the required logarithmic length. Its strict numerical certificate uses the exact rational \(209707481425/34359738368\).

For a fixed rotation order, the minimum-envelope joins split into two cases. Low joins propagate two distinct low states through a logarithmic forward buffer; the established occupation theorem makes the union negligible. A translated buffer also controls preceding window starts. High joins force cost at least \(1/2-o(1)\) on their backward buffers. The number of windows touching those buffers is at most twice their length. On all remaining windows the minimum envelope is an actual orbit segment, so the pinned pressure input applies. Since \(2u<1/2\), the high buffers cannot erase the pressure gain. This proves the strict fixed-order constant and the growing-budget divergence above ratio \(0.96355/2+\varepsilon\). The proof does not eliminate small balanced-minimum ratios.

The coordinator also reconstructed the two synthesis notes. Combining the all-origin mean theorem with the weighted rank-height inequality gives the whole-cycle rank/mismatch tradeoff. The divisor layer bound gives a vanishing captured mass for \(r^2s=O(p)\); a separate threshold argument gives negligible paired-date density. Positive occupation then bounds the number of low-cost translates by inclusion-exclusion. Hamming subadditivity bounds the orders of their generators, and a finite Cayley-graph path argument bounds their generated subgroup. A bounded-order near period remains possible and supplies no contradiction by itself. Weaver's prior whole-state rank estimate is credited separately from the new weighted-divisor and all-origin consequences.

The shared finite checker covers 456 genuine rational cycles, 14,812 all-origin length systems, 4,942 windows longer than a complete lap, 54,424 good-origin ledgers, 4,617 join buffers and 197 retained positive-pressure windows. It does not test an asymptotic limiting theorem.

## Full denominators on one ordinary itinerary

The coordinator and ordinary lane independently reconstructed `PREFIX_CLOSURE_DENOMINATORS.md`. For each actual prefix,

\[
q_t=\frac{|2^t-3^{g_t}|}{\gcd(|2^t-3^{g_t}|,x_t-n)}.
\]

Lagarias's original Lemma 2.2 gives the determinant lower bound with the stated all-length constant. On a prefix with distinct departure states, the positive-integer harmonic sum bounds the correction product by \(2t^{1/3}\). Once a state has repeated, the actual future stays in the already observed finite set. These two alternatives give \(q_t\ge2^t/(4800M(n,t)t^{14})\) at every nonreturn. At a return the denominator is one; this exception is indispensable. The bounded eventual parameter for a fixed source is not presented as a computable orbit maximum from the source alone.

Corvaja–Zannier's original Proposition 2 then excludes all off-clock modular relations in every fixed linear-size box after an ineffective onset. A proper fractional generator on the clock line would give \(q_t\le3^{t/2}\), contradicting the explicit denominator estimate; this part has a finite effective test. Geometry of numbers gives modular group order \(\omega(t^2)\). The classical p-adic bound is stated with Bugeaud–Laurent's exact parameters; the recent fixed-prime improvement of Chim is credited separately. No uniformity in an unbounded prime is imported from a fixed-prime estimate.

Chronological gcds satisfy \(\gcd(q_t,q_{t+d})\mid|2^d-3^{g_{t+d}-g_t}|\). Thus a short band has an effective large log-lcm after subtracting every pairwise gcd cost. The positive lower coefficient for bands of length \(\lfloor\sqrt N\rfloor\) was independently checked. This forces a large common merger gap if one gap is required for all centers in the band. It does not force the fixed ordinary orbit itself to make any prescribed merger.

The central finite replay checks 9,504 actual prefix closures, 1,730 negative centers, 72 source returns, 5,912 nonreturns after repetition, 337,392 chronological overlaps, 528 lcm bands and 924 small-modulus group computations. Large denominators also arise on the convergent trajectory from 3.

## An effective number of exceptions without effective locations

The coordinator and cycle lane independently reconstructed `COUNTED_CLOCK_RELATIONS.md`. Its theorem is uniform over one arbitrary binary itinerary and arbitrary selected divisors at each date. Only the eligibility condition \(q_t\ge2^{t/2}\) is required. The conclusion counts exceptional dates over the entire itinerary, rather than estimating their last possible location.

At a short independent relation, use \(U=2^t3^{-g_t}\), \(V=2^a3^b\), and the rectangle \(0\le i\le64B\), \(0\le j\le16\). The projective vector of \(U^iV^j-1\) has height at least \(2^{t-1}\). Choosing a minimum monomial at each of the three places gives a unimodular basis of difference forms. All factors of the full modulus survive in the product of norms outside \(\{\infty,2,3\}\). The exact normalized local-product margin is strong enough for a Subspace-Theorem exponent \(1/2\).

The coordinator checked Evertse–Ferretti's original Theorem 3.1, including the strict threshold \(H>k^{2k}\), the rational-field coefficient height, and the number of distinct forms. A fixed archimedean change of coordinates makes every normalized form ratio at most one. Clipping, rounding on a \(1/(16k)\) grid and scaling exponents produces at most \(\exp(O(k\log k))\) systems. The discarded small-height dates contribute only \(O(k\log k)\).

Every resulting exceptional polynomial has at most \(k+1\) terms. A minimal vanishing subsum gives a nondegenerate rational S-unit equation. The coordinator read Evertse's original 1995 Theorem 3 in the scanned primary paper: its bound \((2^{35}r^2)^{3r^3}\) is independent of the fixed rational coefficient heights. Selecting one coordinate leaves at most \(\exp(O(B^3\log B))\) translated torus equations. Their coefficients may remain effectively unlocated.

The crucial chronological step removes any need to locate those coefficients. For one translate \(U^uV^v=c\ne1\), every admissible \(q_t\) divides the same integer numerator of \(c-1\). If its binary log is \(s\), all such dates lie in \([s/(176B),2s]\). Partition this interval into \(O(B^2)\) short boxes. The chronological gcd estimate and elementary lcm inequality show that a box cannot contain \(\lceil704B\rceil\) eligible dates: their lcm would exceed the containing integer. Thus each translate accounts for only \(O(B^3)\) dates regardless of its enormous unknown height. This proves the effective total count.

The resulting density consequence is an off-clock lower bound of order \(t(\log W/\log\log W)^{1/3}\), outside at most \(\sqrt W\) eligible dates in a length-\(W\) band. It also applies to the one-odd denominators \(2^t-3\). It leaves open individual exceptional locations and the exponential order bound needed for the sharp periodic frontier.

The recent Noubissie preprint `arXiv:2611.11341v1` was read directly, including Theorem 9 and Remark 3. It motivated the exceptional-hypersurface approach. The proof here relies on the two published theorems just described, not on the new manuscript. The finite replay checks 72 rectangles, 2,376 difference forms, 512 numerical margins and 286 divisor packs containing 1,373 eligible dates.

## Rank of signed closures, including convergent sources

The coordinator and literature lane independently reconstructed `PREFIX_CLOSURE_NUMERATOR_RANK.md`. The positive-cycle rank estimate transfers directly to the full odd numerator set. For negative closures, the relation \(2^e y'=3y-q\) gives \(q<3y\). Adding downward logarithmic variation to the genuine edge costs controls both endpoint height differences and gcds; its total stays below \((3\log_2 3-2)p\log2\). The same interval argument supplies the negative-sign rank bound. Combining either sign with the nonreturn denominator estimate and \(g_t\ge(t-\log_2 n)/2\) gives the uniform \(1/\sqrt3\) square-root coefficient.

For an eventually periodic source, its closure contains \(t/P+O_n(1)\) complete copies of one fixed ultimate word. All rational odd phases stay between positive constants depending on the source, so their numerators are comparable to \(q_t\). The moving additive recurrence constant is \(q_tc\). Removing \(\gcd(y_0,q_tc)=\gcd(y_0,c)\le c\) restores coprimality. Each repeated prime-power occurrence can then be charged to its distance from the first occurrence in the Lucas factors. The coordinator re-read Weaver Paper 161's original Lemmas 3 and 4 and checked this normalization independently. Its Lucas-factorial and maximal-volume lcm arguments are explicitly prior methods. Their transfer gives \(r_t\ge(1/2-o(1))t/P\), even on the already converged ordinary source 3.

The finite signed-rank replay includes 314 positive and 120 negative closures, 28 return controls, 442 repeated-boundary systems, 31 nonunit gcd normalizations and 147 nontrivial lcm-surplus divisibilities. No growth of the finite state set of the original convergent trajectory is claimed.

## Formal and publication evidence

`EventFactorRank.lean` was independently read and freshly compiled by the coordinator. Its three public roots prove independence of nonnegative weighted valuation rows under strict pair-overlap bounds, the shared-point interval gap, and the resulting actual finite-dimensional span obstruction. The module does not encode the full Collatz gcd argument or the circle integration theorem. A separate fresh import audited all three roots, finding only `propext`, `Classical.choice` and `Quot.sound`. Lean 4.34.1 and the pinned Mathlib cache were used; no cold dependency rebuild or independent LeanChecker run is claimed.

All five central Python replays succeeded in normal and optimized mode with identical output and unchanged source hashes. The cumulative local formal inventory is 45 central public roots plus the separately rebuilt motif specialization, for 46. A further four-root actual word-closure formalization has an author replay and awaits a separate central replay; it is excluded from this checkpoint and is not counted. A large direct finite-cover reflection attempt was killed under resource pressure and likewise supplies no formal claim.

The preceding exact-tree repository-validation receipt is included here. The selected new tree is validated in a clean complete checkout before publication. Its integrity receipt is archived after that validation and included at the next checkpoint to avoid a self-referential commit hash. Repository validation checks consistency, not the truth of the new mathematical theorems.
