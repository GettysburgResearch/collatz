# Independent review of the signed-route and query theorems

The reference branch is PR 197 at `156652e03fe7a78f9cd4442039779cc622fdf3de`. The new source bodies are identified by SHA-256 below. The map is the positive ordinary shortcut. Negative integer and odd-denominator rational paths are finite reference words used to evaluate ordinary affine lifts.

| Source | SHA-256 | Narrow verdict |
|---|---|---|
| SignedCycleDilation.lean | a39820fe4f81a30835047a3ae5321c314d52b0545ac467b6e1edfeed213758a3 | VERIFIED for the displayed two-arm cycle lift and the −1183 family. |
| DifferentCycleAnchors.lean | 318ba88a0a8297f20c80609ec1322c5176f278648c11ece163a0789ca801d866 | VERIFIED for equal finite signed endpoint and exact slope matching, the stated −127/−1807 family, and the arithmetic debt implication with its displayed hypotheses. |
| MersenneTwoCenter.lean | 200a72d44d14e7a28e6dd238da0573f030a9808c2dce6d63b98378df917026fe | VERIFIED on each of the 13 stated infinite rows for e=6. Their union has 17 common classes modulo 19,683. |
| GuardedResidueCover.lean | e15f066d09c85f05fa17e91d56b61a95f4361da3e103b3432c589aee62a2abfc | VERIFIED for the 16 progressions. Their union covers 55 of the 256 candidate residues per full 12,288 period. |
| check_signed_routes.py | 2832a94455f0281bbdee4aa414a95ff18b468b308efba518c38312a39d0d770f | Both the author replay on these bytes under optimized Python and the independent reconstructions below passed. |

## Source and label reconstruction

For n=2^h k+a, one shortcut step subtracts one factor of 2 from the lift and multiplies its running coefficient by 3 exactly when the signed seed is odd. Induction gives T^h(n)=3^p k+T^h(a). Equality needs both matching signed terminal constants and the correct odd-count-adjusted leading coefficients. Both conditions are present in the two cycle/anchor modules. Different signed input phases and different physical clocks do not cause a problem when the ordinary terminal values coincide. Badness of a positive lower source and goodness of its triple transfer back to the particular smaller w via these finite equalities. No leastness hypothesis on every smaller ordinary integer enters.

For the e=6 rows let j=11+162m and N=2^j. The ordinary formulas are z=(128N−271)/81 and w=(2^hN−num)/den, with h, num, den from the specified row. Independently computing the modular exponent at the first point and its update over each period establishes legality along every row. The source's finite affine checks show exactly T^7 z=T^h w=N−1 and T^(h+2)(3w)=N/4. The latter value is a positive power of two. The query is 17 modulo 48 and below z. Each row then excludes a least reverse defect without needing prior convergence on any neighboring Mersenne index. The closure of the 13 starting residues under their periods contains 17 distinct residues modulo 19,683. This is a result on the separate e=6 family.

The all-rank 55-residue claim uses only true ordinary links away from its marked query. On each of the five guarded rows, the smaller w has the same bad lower label as z. Under leastness its triple must be bad. The remaining word identifies that triple's label with the already good 3z, yielding a contradiction. The remaining eleven rows directly meet 3z. Neither count asserts that every source escapes.

## Independent ordinary executions and mathematical reconstruction

A fresh build using the pinned Lean 4.34.1 and Mathlib environment compiled all four modules into a separate object directory. The two-center public `progress` and `least_excluded` declarations use [propext, Quot.sound]. The three other modules' audited declarations use subsets of [propext, Classical.choice, Quot.sound]. The guarded census uses no axioms.

The independent script `review_rewrite.py`, SHA-256 `cd8104812f878bb47a37e55f99bd852e24446226a7a9f7d696a1c0800eac05fd`, executes both full ordinary positive starts at t=0 and t=1 in every e=6 row. It used 1,278 shortcut clocks on 26 cases, with largest exponent j=5,350,871. It also executes 10 ordinary paired-anchor instances and all 16 guarded words at each of t=0,1,1024,10^30. As a separate test it enumerates every integer a in the necessary range |a|≤136·2^H for H=0 through 11 and directly filters 81a+271≡0 (mod 2^H) and both signed target-cycle conditions. The results are exactly (H,a)=(0,0),(4,1),(5,1). None is 17 modulo 48.

For 7≤H≤u=j+7, z≡−271/81 modulo 2^H. Its rational center reaches −1 at clock seven with four odd inputs and thereafter takes only odd steps. If an integer a has the same initial H bits, then 81a+271=2^H k with nonzero integer k. Hence T^H(a)+1=3^(H−7)k. The assumed finite target cycles have radius 136, making H≥12 impossible in this range.

For H=u+v write a=z+2^H K/D with D positive and odd, K a nonzero integer. Then
$$T^u(a)+1=3^j(D+81·2^v K)/D.$$
The possible vanishing of the numerator corresponds to exactly a=−271/81. Outside that center, c=|D+81·2^vK|≥1 and 81·2^v≤D+c. An endpoint of magnitude at most M≥1 at clock H implies |T^u(a)|≤2^v M: under an inverse step n→2n or n→(2n−1)/3, the enclosing radius increases by at most two. Thus (3^j)c≤D(M·2^v+1). When 81·2^v≤2D the result follows using c≥1. Otherwise 81·2^v≤2c, yielding the asserted 81·3^j≤81D+2MD². In particular D=1 and M=136 are impossible for j≥11. The case a=z has K=0 and lies outside this claim. The exceptional rational center lies outside the nonvanishing case. A very large denominator, an arbitrary undisplayed cycle set, an inverse path, or a different ordinary rescue can evade this obstruction. The inequality is a necessary resource bound within the stated test.

The explicit constructions make no assertion that every supplied rank-three parameter, or every upper rank, has such a smaller query. No theorem here proves universal convergence.

The full written statement in `SIGNED_ROUTES.md` was reviewed at SHA-256 `88bf94083c79372604f03e983353420c6562b01ea6f5ff2dd10fce94fc377e2d`. The phase-alignment determinant argument is valid when the required phases, gains and all four binary precisions are imposed: nonnegative full turns on either reference realize each signed difference of turn counts. The residue, positivity, and height conditions remain separate from lattice solvability.

For the three exceptional small-clock source anchors the conclusion also holds without assuming the first anchor is 17 modulo 48. If a=0 at H=0, zero is its only integer ancestor and the target arm's gain is at most one. The physical coefficient ratio from source to target is therefore at least one. If a=1, then the compatible upper source clocks 4 and 5 for the start 3 have signed endpoint and gain respectively (2,9/16) and (1,9/32). In each case terminal value divided by gain is 32/9. Any target upper anchor 3b entering that phase is positive. Nonnegative affine intercept gives target endpoint divided by target gain at least 3b, hence the common gain ratio is at least 27b/32. For b≥2 this cannot shrink the lift. For b=1 equal lower phases require a ratio (3/4)^k. Strict shrinkage requires k≥1. Since 81(z−1)=32(4·2^j−11), one has v₂(z−1)=5, so an integral w=a+(3/4)^k(z−a) has v₂(w−1)≤3, excluding w≡17 modulo 48. These arguments check the stated integer-anchor obstruction on its full clock range. The review does not independently certify external literature claims in the concluding source inventory.
