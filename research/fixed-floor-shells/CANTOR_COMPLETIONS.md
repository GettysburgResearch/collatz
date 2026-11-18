# A product set of strict mixed completions

**Proposed, with an exact finite screen.** Use the [strict mixed-arm convention](MIXED_COMPLETIONS.md). Let E be the dyadic set whose odd valuation itineraries begin with 80 ones and then concatenate arbitrary blocks 1 and 2,1,1. There is a single set G of ternary units of additive Haar measure greater than 0.012 for which **every** pair in E × G is strict. Both ordinary ternary coordinates 0 and 1 also work for every dyadic point in E. The dyadic Hausdorff dimension of E is the positive solution of 2^(−s)+2^(−4s)=1. This constructs an obstruction with uncountably many forward itineraries and unrestricted reverse depth, without providing a positive ordinary dyadic point in E.

## Occupation of each reference suffix

Write S_j for the total valuation over the first j forward letters a_i, P_j=3^j/2^S_j, and P₀=1. Every nonempty forward prefix has P_j>1. This holds on the initial ones, and each later block has net multiplier 3/2 or 27/16. An initial factor 3/4 at the start of a three-letter block can cost at most a quarter of the accumulated multiplier, already at least (3/2)^80.

For each h≥0 define the real number K_h=Σ_(i≥h) P_h/(3P_i). The minimum for all-one letters is 1. Replace successive letters one by one by the additional powers of two at positions r₁,r₂,… relative to the start h. Each replacement increases the previously modified all-one sum by 2^(j−1)(2/3)^r_j. Monotone convergence evaluates the resulting infinite sum. Since r_j≥1+3(j−1),

    K_h ≤ 1+(2/3)/(1−2(2/3)^3) = 29/11 < 3.
    K₀ ≤ 1+(2/3)^80 (29/11−1) < 1+2^(−10).

The inverse real offset of a word is B=(1/3)Σ J_i, where J_i=3^i/2^A_i for its first i letters in inverse order. At matched forward/inverse endpoints, B/J equals the truncated occupation Σ_(i=0)^(q−1) 2^S_i/3^(i+1) in the corresponding forward order. In particular every word has B/J≥1−(2/3)^q.

## A first tie is arithmetically impossible

Cancel any exact inverse retracing of a terminal part of the forward arm. If l≥1 forward letters remain at the first departure, the first differing reverse exponent exceeds the paired reference letter by at least two. Indeed the reference exponent is either one or two, and ternary legality fixes its parity. Write b_q for the competing total minus the reference total on the last q reference letters, 1≤q≤l. It starts positive and drops by at most one per new letter.

Suppose q is the first zero. At all earlier reverse prefixes the reference multipliers strictly exceed the competing ones, and at q they coincide, with value J. Thus the equal-slope affine map between the two sources is a translation by c=(B_ref−B_w)/J>0. It is an even integer: multiply each offset by their common denominator 2^S. The two resulting numerators are odd, since the last summand has odd numerator and all earlier terms have an extra power of two. Legality at the same ternary target implies the numerator difference is divisible by 3^q. Moreover c≤K_(l−q)−1<2. Indeed one subtracts a competing truncated occupation of at least 1−(2/3)^q, and the omitted reference tail is at least (2/3)^q since all exponents are positive. This contradicts a positive even c. Consequently b_q≥1 throughout every nonshared prefix.

For q≤l the total relative slope is therefore 2^b_q P_(l−q)>1. At q=l, write b=b_l. The ternary state of the competitor is exactly s=2^b z+c with

    c a positive odd integer,       0<c<2^b K₀.

The reference multipliers strictly exceed their competing partners at every inverse prefix, giving positivity as above. With different totals the numerator of c is the reference odd numerator multiplied by 2^b minus the competing odd numerator, divided by 3^l; it is an odd integer by legality. The upper bound follows from B_w>0. A reducing or tying nonempty continuation must have multiplier D≤2^(−b). At z=0,1 the state s is a positive odd integer and its positive odd predecessor satisfies x<Ds<z+K₀<3. Thus x=1, which can reach only 1 and only with inverse multiplier at least one. The initial state itself admits no nonempty lowering or tying word at either z=0 or z=1. These arguments cover exact full cancellations followed by additional inverse letters as well.

## One finite set of tests works for the whole dyadic set

As in the [three-cycle calculation](MIXED_COMPLETIONS.md), remove an initial inverse screen of Haar mass below 0.517167, leaving initial passing units of mass at least 2/3−0.517167, all congruent to 1 modulo 3. A subsequent event after the affine map 2^b z+c costs at most the Haar mass of the inverse slope screen H_(2^−b), since 2^b is a ternary unit. For b>10 there are at most 2^b possible positive odd c since K₀<2. The [quadratic inverse screen](PREDECESSOR_MINIMA.md) therefore bounds all their costs combined by Σ_(b>10)2^(−b)=2^(−10).

For b≤10 put y=2^b−c. The initial occupation bound shows that this is a positive odd integer smaller than 2^b. We can discard any such pair for which 2^(b+1)−y≡0 modulo 3, since then s is a ternary nonunit on all of the initial passing units. Among the remaining labels a further necessary test is that the first 80 valuations of the positive mirror orbit from y have total excess Σ(e_i−1)≤b.

To see the latter fact when l<80, the whole reference is all-one. At the signed input −1 it ends at −1; the competing input at this phase is −y. It reaches −1 in l genuine odd steps with total l+b, and the subsequent loop takes one division each time. When l≥80 choose a positive odd n in the dyadic cylinder of the full reference word. Then n≡−1 modulo 2^81. At the actual positive terminal value after l steps the competing inverse path is integral, since legality through l depends only on that terminal residue modulo 3^l and the residue is determined by the reference word. Its ordinary source is 2^b n+c≡−y modulo 2^(81+b). Its initial 80 forward valuations have total at most 80+b. Indeed the excess over the reference on those letters is b−b_(l−80), with the cancelled-length convention b₀=0. The first 80 reference letters are ones. The dyadic valuation cylinder for these 80 competing letters has modulus at most 2^(81+b). The signed input −y therefore follows exactly those valuations, as claimed.

For the remaining finite costs improve the quadratic estimate slightly. On first passage of the multiplier 2^S/3^q below θ=2^(−b), the ternary word cost 3^(−q) equals the tilted geometric word probability times the square of the attained multiplier, as in FS-010. The tilted letter distribution assigns probability 3/4 to the exponent one. If h is the smallest positive integer with (2/3)^h≤θ, the all-one stopping prefix has tilted probability (3/4)^h and attained multiplier (2/3)^h. Every other stopped prefix has squared multiplier at most θ². Thus

    Haar(H_θ) ≤ θ² − (3/4)^h [θ²−(2/3)^(2h)].

The [exact checker](check_mixed_cantor.py) enumerates all remaining y for 1≤b≤10. Their respective counts are 0,2,1,2,3,4,6,8,13,20. Including the large-b tail, the sum of their Haar costs is below 0.137394. Removing their union from the initial passing units leaves one common G of additive Haar mass exceeding 0.012.

Finally the two inverse dyadic block maps contract by exactly 2^(−1) and 2^(−4). Their images are disjoint since their first valuations differ. The usual disjoint self-similar cylinder formula gives the stated dimension; explicitly one may assign the two letters masses 2^(−s) and 2^(−4s). The stopping cylinders at a dyadic radius have diameters between one sixteenth of that radius and the radius, so the mass of any ball is bounded by a constant times its radius to the power s, while the level covers give the reverse dimension inequality. The fixed initial word changes neither bound.
