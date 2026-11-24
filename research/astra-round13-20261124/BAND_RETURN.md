# A six-clock return with exchanged arms

For the shortcut Collatz map put n=2^(k+1)u−1, x=2^k u−1, b=3^k u−1, with k≥0 and u positive. The trajectories of x and n reach b and 3b+2 after k and k+1 clocks respectively. If D(b)=55b−8 is positive and v₂(D(b))=6L+1, those two tails first meet synchronously after **6L+2 additional steps**. Thus x=(n−1)/2 is a strictly smaller positive ordinary merger partner. The first-meeting assertion concerns synchronized clocks starting at b and 3b+2. Meetings with other clock offsets are possible.

## Proof

For b=64v+56, the two endpoints after six steps are 27v+26 and 9v+8. The finite itineraries at v=0 are 56,28,14,7,11,17,26 and 170,85,128,64,32,16,8. The two words have three and one odd clocks, and the high parts initially differ by a factor of three. Binary lifting gives the endpoints for every v. Writing b'=9v+8, the new pair is (3b'+2,b') with b'<b.

The inverse of 55 modulo 64 is 7, so 64 divides D(b) exactly when b≡56 modulo 64. On this branch 64D(b')=9D(b). A source with defect valuation 6L+1 undergoes exactly L returns. The final parameter is 2 modulo 4, say 4w+2. Its pair goes from (4w+2,12w+8) to (2w+1,6w+4) and finally to (3w+2,3w+2). The penultimate endpoints differ, so equality was impossible at every earlier synchronized clock. Reversing the order of the endpoints preserves the conclusion.

The infinite formal reset parameter is the nonintegral 2-adic integer 8/55. In normalization with denominator 55 the numerators traverse 8,4,2,1,29,71,134,67,128,64,32,16,8. The second arm starts at 134/55, six positions ahead on the same rational cycle. Positive ordinary inputs have only finitely many successive returns.

## Realization and coverage in the marked band

For every k,L the criterion on u is the single congruence 55·3^k u≡63+2·64^L modulo 4·64^L. The coefficient is odd. Hence exactly one odd residue class works, giving infinitely many positive ordinary sources for each prescribed k,L. The exceptional nonpositive defect at k=0,u=1 fails the congruence. With odd u the maximal rising prefix has length k+1=v₂(n+1).

The selector accounts for an asymptotic fraction **32/63 of all odd marked sources** in the dyadic octave of #173. Other sources may also have smaller partners. For fixed k≥0, odd u corresponds bijectively to even b modulo each binary power, and D also permutes the even residues. Conditional on even residues, valuation 6L+1 has fraction 2^−(6L+1). Summing over L gives 32/63. In an octave of exponent d the marked band width is asymptotic to 70·2^d/(d+1), which tends to infinity. Each fixed congruence is therefore asymptotically uniform in these intervals. The discarded k≥K are all in one class modulo 2^(K+1). At each fixed k the discarded L≥J satisfy D(b)≡0 modulo 2^(6J). Taking finite cutoffs first and sending them to infinity proves the stated density. This is a count of sources already inside the band.

## Finite mixed scripts remove 16/31 of marks

There is a second exact return: if b=2v+1, both arms are odd and one clock takes the pair to (3v+2,3(3v+2)+2). Accept a parameter when a finite sequence of this odd return and the six-clock swap ends at b≡2 mod4. The rules are disjoint. Each accepted integer has an actual synchronized tail merger by induction on the script. The valuation shells above form an explicit subfamily, obtained by using only swaps.

Each rule with j prescribed binary digits acts on the remaining free high coordinate v by v↦Av+B with A odd. It therefore preserves uniform residue frequencies at every finite remaining precision. With an unrestricted binary parameter, terminal, odd-return and swap-return cylinders have frequencies 1/4, 1/2 and 1/64. At depth R the parameters still following returns have frequency (33/64)^R. Finite cylinders have their prescribed densities in every interval whose length tends to infinity; the remainder bound permits passage to the infinite union. The accepted density is (1/4)/(1−33/64)=16/31. Conditional on even b, direct termination contributes 1/2 and swap followed by acceptance contributes (1/32)(16/31), again 16/31. The same canonical rising-cofactor and octave argument therefore gives **16/31 of all marked odd sources**. The remaining 15/31 are a count for this particular arithmetic test. A fixed positive source could in principle follow an infinite sequence of mixed resets; existence or impossibility of such a source has not been established. The residual predicate includes both finite rejections and any such infinite scripts. Pure six-clock returns terminate by defect valuation, and consecutive odd returns terminate by the valuation of b+1.

More explicitly, allowing at most R returns gives A_R accepted residues modulo 4·64^R, with A_0=1 and A_(R+1)=64^(R+1)+33A_R. The odd branch contributes 32A_R and the six-clock branch contributes A_R. Thus 31A_R=64^(R+1)−33^(R+1). This finite count and the infinite-branch upper bound are separate statements.

A fixed infinite mixed path would have infinitely many swaps: in an odd run the positive quantity b+1 loses one factor of 2 at each step. At a swap b=64v+56, let r be the number of subsequent odd returns before the next even parameter c. Then r=v₂(v+1) and 64·2^r(c+1)=9·3^r(b+8). If r≤4, this implies c+1≤729(b+8)/1024<b+1 since b≥56. Infinitely many swaps with only finitely many r≥5 would therefore give an infinite strictly decreasing tail of natural numbers. Every hypothetical infinite fixed mixed path must visit b≡2040 modulo 2048 infinitely often, immediately before runs of at least five odd returns. This is a necessary fixed-source condition, stronger than the zero-density statement for infinite scripts.

## Reduction to the residual marked sources

For every marked n accepted by a finite mixed script, take the positive partner x=(n−1)/2 and strip all powers of two from x to obtain its odd part y. Then y<n, it merges with n, and **y is marked**. To prove the last assertion, deleting either low binary digit of any positive integer 2q+e with q>0 and e∈{0,1} preserves section membership. Indeed if j=floor(log₂ q), then the new octave index is j+1 for 2q+e and its offset is 2(q−2^j)+e. The old inequality (j+2)(2(q−2^j)+e)≤140·2^j implies (j+1)(q−2^j)≤70·2^j. Delete the final 1 in n and then all trailing 0s of x. Each latter deletion is an actual even shortcut clock.

Thus **universal convergence is equivalent to convergence of all uncovered marked sources**. Forward implication is immediate. For the converse use strong induction on the positive marked source. An uncovered mark converges by hypothesis. A covered mark has the strictly smaller marked partner y just proved, whose convergence transfers along the ordinary merger. Now invoke #173's equivalence between all marked sources converging and all ordinary sources converging. This argument does not compare a later mark on an arbitrary source orbit with that original source.

## An uncovered family

Take K≡3 mod8, K≥11, d=2K+1 and n=2^d+2^K−1. This is marked because (d+1)(2^K−1)≤70·2^d, using K+1≤2^K. Also n≡0 mod3, and n=2^K u−1 with u=2^(K+1)+1 odd. The ordinary odd-run identity rules out strict descent in the first K steps. Now k=K−1≡2 mod8, so 3^k≡9 mod32, u≡1 mod32 and 55·3^k u−63≡16 mod32. Valuation 4 lies outside the swap-only selector. Here b≡8 mod32, so immediately neither terminal, odd-return nor swap applies. These facts do not determine whether an individual source converges.

## Source boundaries

- #173 at fa0c9e2a2851e6324391e39c17afcb5913185aec, research/lean-shell-cover/ForwardSection.lean, bounded_visit and section_iff_offset: each positive source has an actual odd marked visit before 4·floor(sqrt(n))+floor(log₂(n)) shortcut clocks. For x at octave d, the integer offset is at most floor(70·2^d/(d+1)).
- #184 at 366dab89ee9548084ab9b5e4e90ff82abf287a20, research/lean-band-coupling-20261121/lean/RisingMerge.lean, rising_smaller_partner: for the initial phase b≡2 mod4 it produces (3n−1)/4 when k+1≥2. The new arm is (n−1)/2 and the new return closes all shells v₂(D)=1 mod6. SourceBoundedMerge.lean, collatz_iff_source_bounded_section_merge, states the original-source induction requirement.
- #182 at cbec52dde5bed390a693310dd04e911033ba0cc9, research/lean-shell-cover/ShellCover.lean, odd_run, and research/lean-dyadic-descent-20261121/OffsetDescent.lean, affine_lift, are the local Lean dependencies.

Convergence on every residual mark remains open. Density in the band gives no deterministic conclusion for a missed fixed source, and a smaller partner below a later, larger marked value need not lie below the original source.
