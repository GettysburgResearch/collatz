# A joint budget for real windows, mixed digits and first-hit clock residues

**Status.** Proposed analytic deduction from the external joint floor F, PR201's derived antichain, and a published linear-form estimate of Wu and Wang. The block variant additionally assumes the synchronization theorem S. Neither the infinite analytic inputs nor this asymptotic theorem are Lean-certified here.

## Statement

Write t₀=4.1163051. Fix σ,μ≥0 satisfying

    t₀ σ + (t₀+1)μ < 1/2.                                        (1)

For a prescribed positive odd unit a there are c>0 and a sufficiently large onset such that the following holds. For J=[Z,Z+W) contained in [X,2X], W≥X/(log X)^σ, integer 1≤m≤(log X)^μ, any residues u,v modulo m, and any residues r mod 2^h, l mod 3^k with h+k≤η log X,

    #{n∈J : n≡r (2^h), n≡l (3^k), n reaches a,
       (first shortcut clock, odd inputs before first hit)≡(u,v) mod m}
         ≥ c W / (2^h 3^k m²).                                   (2)

Here η>0 is absolute. The constant and threshold may depend on a, σ and μ, uniformly over the other displayed choices. To allow an arbitrary **fixed** m when μ=0 replace its upper bound by m≤m₀ for any fixed m₀, with allowed onset depending on m₀. The same proof permits multiplying the lower width by any fixed positive constant, and the modulus upper bound by any fixed constant. With fixed grades (2) reaches every σ<1/(2t₀), about 0.12147. With fixed relative window width it reaches every μ<1/(2(t₀+1)), about 0.09773.

The linear-size antichain and the moving-anchor method are already due to PR201 at 2978d84f8a1fda9083593b26c6bf724d5976d859. Its prefix-density Theorems A–D give σ<5/133, fixed m, sublinear digit counts and subcritical block lengths. PR203 at 3f2c89f12b057b8bb8655bd6fc794c772aa8b65d gives proportional mixed depths and critical blocks on fixed-shape windows, including marking both clocks. The additions in (1)–(2) are the improved primary-source linear form, the simultaneous tradeoff between a shrinking real interval and growing clock modulus, and the proportional mixed-depth implementation on those same windows. [PR201 prefix density](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/prefix-density/README.md) · [PR203 fixed-target depth bank](https://github.com/GettysburgResearch/collatz/blob/3f2c89f12b057b8bb8655bd6fc794c772aa8b65d/research/mixed-adic-basin-density-20261124/fixed_target_depth_bank.md)

## The quantitative rotation input

Wu and Wang's Theorem 1 gives, for any ε>0 and all integers p,q₁,q₂ with H=max(|q₁|,|q₂|) sufficiently large depending effectively on ε,

    |p+q₁ log 2+q₂ log 3| ≥ H^(−4.1163051−ε).

The paper's Corollary 1 concerns the irrationality measure of log 3 alone. We use its three-term **Theorem 1**, whose proof uses the integral scheme for these three numbers. For α=log₂3 and j≥1 set p=0, q₂=j and q₁ minus the nearest integer to jα. Then H≤2j, and dividing by log 2 gives ||jα||≥c_κ j^(−κ) for every κ>t₀. Irrationality of α absorbs the finite height exceptions. No numerical onset or endpoint exponent is asserted. [Q. Wu and L. Wang, *On the irrationality measure of log 3*, J. Number Theory 142 (2014), 264–273, §1 Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007)

Choose κ>t₀ retaining κσ+(κ+1)μ<1/2. Write w=W/X. For a circle arc of length ℓ comparable to w/m, let D be the first convergent denominator of α at least C m/w. At the preceding denominator d, continued fractions give ||dα||≤1/D, while the preceding paragraph gives ||dα||≥c_κ d^(−κ). Hence D≪_κ (m/w)^κ. In each consecutive segment of D rotation steps the points differ from a translate of the permuted 1/D grid by at most 1/D: use the convergent numerator p, |α−p/D|<1/D², and compare the displacement at indices 0,...,D−1 within that segment. Discarding width 1/D at each edge leaves at least c ℓD grid points if the absolute C is large enough. The bound is independent of the initial phase and arc location.

## Ternary landing and original source digits

Use the unit convention and inverse-word floor from the first section of JOINT_REAL_FLOOR.md, with any fixed real-height cap F_* after the bounded spreading letter. We only need the existing cap here. A binary refinement H=h+1 of a prescribed residue can force its last shortcut step odd, giving the exact physical relation

    T^H(r'+2^H t)=z+3^p t,          1≤p≤H,     3∤z,   0≤r'<2^H.

This follows from the usual parity-prefix affine rule, since varying the next free binary bit changes the previous endpoint by an odd coefficient. At the canonical lift z+1≤3^H from T(x)+1≤(3/2)(x+1). To impose the original n≡l mod 3^k require the landing y≡z+3^p ((l−r')2^(−H) mod 3^k) mod 3^(p+k), a unit class. Put K=p+k and E=r'−2^H z/3^p; then |E|≤2^H+6^H. When a word of depth b, total s and offset β at target q gives that landing, the unique source in the binary class is

    n=L(q−β)+E,                L=2^(H+s)/3^(p+b).                  (3)

Use PR201 Theorem A at height Y=(log X)^2. It gives at least c_a Y pairwise incomparable ordinary units q in [Y,2Y), all reaching one fixed nonperiodic waypoint ahead of a. Its F from paper 37 at K=1 is covered by paper 48 Lemma 7 at K=1; PR201 section 2 proves the antichain from that interface without a separate basin-density hypothesis. In outline, a fixed nonperiodic waypoint has ≫_a Y/L₀ candidate starts when the admissible odd depths are spaced by a fixed L₀. Comparable candidates would require a biased binary prefix of length between L₀ and O(√log Y). Native parity counting removes O(Y exp(−cL₀)) candidates, smaller than the initial bank for a sufficiently large fixed L₀. Thus Σ_q 1/q≥c'_a and the entire ordinary ancestor sets of distinct q are disjoint. All these q are nonperiodic. No rate uniform in a is used.

Write t_q,p_q for the actual first-hit clock and odd count from q to a. Define B=log₂(Z3^p/(2^H q))/(2−α). Taking η sufficiently small gives c log X≤B≤C log X uniformly, since log q=O(log log X). Also K≤δ(b−1) for every b in [B,B+c₁√B] with small fixed c₁; this is exactly the gain from the fractional extra depth in paper 48. The same η ensures |E|=O(X^(1/2)) uniformly. Restrict b to v−p−p_q modulo m. At each such b look for s≡u−H−t_q mod m with

    Z+W/3 ≤ Lq ≤ Z+2W/3.                                         (4)

Any such s satisfies |s−2b|≤(2−α)|b−B|+O(1)≤√b for large X uniformly. After substituting b=b₁+mi and normalizing by m, (4) is a rotation by α with arbitrary phase and arc of length comparable to w/m. The number of available i is N comparable to √log X/m. The budget (1) gives D/N≪(log X)^(κσ+(κ+1)μ−1/2)=o(1), so complete D-blocks give at least c w√log X/m² successful depths. Pick one s per depth.

At each such b the floor supplies at least c 2^s/(3^(b+p+k)√b)≥c X/(q2^H3^k√log X) words. Formula (3) puts them inside J: uniformly L F_*=O(X/Y)=o(W), and |E|=o(W). The integer lift t is nonnegative for large X since n∈J. The full gap list reading from y proves injectivity at each b, nonperiodicity of q excludes overlap between odd depths, and incomparability excludes all overlap for different q. No visit to a can precede q since q reaches a and is nonperiodic (an earlier visit to a would force a and q onto the same cycle). The binary prefix itself also stays above a for large X since n≥X and T^j(n)≥X/2^H. Thus the selected (u,v) are actual first-hit residues. Multiplying the per-depth count by the number of successful depths and summing Σ_q1/q proves (2), absorbing the factor two since H=h+1. All comparisons are uniform for Y≤q<2Y, rather than an appeal to fixed-target convergence as q moves.

## A synchronized block consequence

Suppose also S, the complete-profile synchronization lower bound from PR146. There exist absolute c₀,η₁>0 such that for M=floor(exp(c₀√log X)), k≤η₁ log X and any l mod 3^k there are at least c W/(3^k m²) block starts n≡l mod 3^k with n,...,n+M−1 all in J and all with the specified first-hit grades at a. This statement does not impose a separate, arbitrary initial binary class on the entire synchronized block. S gives at least half the residues of depth H₀=ceil(C_S log²(2M)) on which the M physical profiles agree. Extend each by one bit forcing an odd step to make p≥1, as above. The refined classes have size at least 2^(H₀−1) in depth H=H₀+1. Choose c₀,η₁ so H+k fits the same η budget. Apply the proof of (2) to each fixed profile using its exact p,z and the interior margin in (4), which absorbs M=o(W). The first-hit grades are common to all members and the refined starting classes are disjoint. This proves the count; greedy packing supplies ≫W/(3^k m² M) disjoint blocks. [PR146 synchronization](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md)

## Additional scales and the limit of the conclusion

The continued-fraction proof also identifies favorable unbounded scales using no quantitative lower bound on ||jα||. Fix m. At any sufficiently large convergent denominator D choose log X in [C_m D²,2 C_m D²] with C_m large. The available progression length is at least 2D for every admissible affine profile. At width W≥C'_m X/√log X the target arc length is at least a large constant times 1/D. The same complete-grid argument then gives (2), with a constant independent of D, on all such favorable X. Infinitely many such bands exist. The assertion on *every* large X comes from Wu–Wang and (1).

Even on the favorable scales the guaranteed width is much larger than exp((log X)^β) for β<1, and concerns an unpaired marginal. PR195 round five selects windows of radius exp(j^β) around an ordinary child or its parent, where X is of size 81^j and β<1/12. No source-preserving bound proved here puts the third phase inside those neighborhoods conditional on that ordered discordant pair. [PR195 round-five head test](https://github.com/GettysburgResearch/collatz/blob/ef3496b577ed7525d5e0c82a9b782819457403d5/research/astra-global-closure-20261124/round5/head/README.md)
