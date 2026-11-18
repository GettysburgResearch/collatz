# High-precision moving-rank repayment and the exceptional companion at −1/2

**Status: PROPOSED.** For a sufficiently deep ternary cancellation in a minimizing rank component, the only short *forward* repayments are whole aligned modules. Short *two-source* repayments admit an additional mechanism at the rational value −1/2. The mechanism gives positive recurrent-support sources with an arbitrarily long prefix above their starting number and a fixed 18-step/16-step lower-rank merger. The theorems concern stated high-precision regimes and do not give an all-source cover.

Use the positive shortcut map T and the moving rank R. Write d_a=3^a−2^{a+1}, c_a=3^a−2^a, z_a(x)=d_a x+c_a, and alpha_a=−c_a/d_a. At x>1, R(x) is the minimum of z_a(x)²/3^{v3(z_a(x))}, with candidate indices 0,1,2 and h(x)=v3(2x+1) if h(x)>=3. Also R(1)=0. A word v of length t and weight q_v acts affinely by F_v(x)=(3^{q_v}x+C_v)/2^t; the formula applies to arbitrary rational arguments even if the chosen word is not their legal parity itinerary. Legality is always required for the two positive source paths.

The [resident module and rank formulas](../astra-three-routes/pass4/MOVING_GHOST_RANK.md) are PR #92 (`7bb6d36d3bc37dd09b52aa9a23c8e33973032359`), T-A3-901/902. The [clock-defect theorem](../astra-critical-mass/CLOCK_DEFECT.md) T-ASTRA-030 in PR #90 (`78ac7c8489f1df81230402808b1f4b77b18fae73`) concerns the different single rank (2x+1)²/3^{v3(2x+1)}. Its exact defect method motivates the comparison here. T-A3-1051 in [MERGING_BARRIERS.md](../astra-three-routes/pass5/MERGING_BARRIERS.md) gives a peak cost on every diagram for an odd multiple of 3. The comparison with 9x+4 and symbolic common-remainder mechanisms also have [resident antecedents](../astra-critical-mass/REMAINDER_CANCELLATION.md).

## Forward classification

Fix n>1, a minimizing index a, A=|d_a| and H=v3(z_a(n)). For t>=1 assume

    3^H > 200 A³ 8^t.                                        (1)

Then R(T^t n)<R(n) if and only if the first t parity bits consist of one or more complete copies of 1^a0. Every other length-t prefix gives R(T^t n)>R(n). In particular an unsafe source for the enlarged region cannot use the aligned case, since its first complete maximal aligned module would decrease rank. Its entire early physical trajectory is more expensive within (1).

**The possible exact collisions.** Every alpha_a has odd denominator. Its legal 2-adic (rational) shortcut itinerary repeats 1^a0: alpha_0=0, alpha_1=1, and for a>=2 one has alpha_a+1=−2^a/d_a and the state after the a odd steps is 2 alpha_a, an even rational. This period has a single zero per primitive block (with the constant-zero case at a=0). A legal orbit can therefore coincide with a dictionary root alpha_b only for b=a at a whole number of periods. Equality of the rational states forces equality of all future parity bits. At the first illegal bit the shadow acquires denominator of exact dyadic order one. Each further bit increases this order by one. It can never again hit a dictionary root. Moreover no shadow can hit −1/2: a first illegal bit could produce it only from −1 or −2/3, whereas the legal orbit is nonnegative at a=0,1 and strictly below −1 at a>=2. Later illegal continuations have dyadic denominator of order at least two.

**Controlling approximate collisions.** Let v be the actual t-bit word, q=q_v, y=T^t(n) and B=2^{t-q}3^q. The odd-position formula gives 0<=C_v<=B−2^t, valid also at q=0. Put P=d_a C_v−3^q c_a. Then

    2^t d_a y=3^q z_a(n)+P,            F_v(alpha_a)=P/(2^t d_a).

We have |c_i|<=5|d_i| and |d_i|<=3^i for all indices i (check i=0,1,2, then c_i/d_i=1+2^i/d_i<=5). Hence |P|<=6AB. The nonzero integer 2P+2^t d_a has absolute value at most 13AB<3^{H+q} by (1), since B/3^q<=2^t. It follows that 3^{h(y)}<=13AB. Each candidate b for the rank at y satisfies 3^b<=13AB. If F_v(alpha_a) differs from alpha_b, then

    2^t d_a z_b(y)=d_b 3^q z_a(n)+E_b,
    0<|E_b|=|d_b P+2^t d_a c_b|<=11|d_b|AB<=143 A² B²<3^{H+q}.

The last bound uses B²/3^q=4^t(3/4)^q. Since d_a and d_b are ternary units, the ternary part of z_b(y) is at most 11|d_b|AB. Also |z_a(n)|<=A(n+5) implies n>=3^H/A−5>2^{t+1} and n>5. Therefore y>=3^q n/2^t>2, and |z_b(y)|>=|d_b|y/2 at every index (only b=1 needs the factor two). Each noncolliding component satisfies

    R_b(y) >= n²6^q/(44 A 8^t) > 4A²n²/3^H >= R(n).

If a collision occurs, the earlier parity argument forces v=(1^a0)^k. On this word z_a(y)=(3^a/2^{a+1})^k z_a(n). Since a minimized the initial rank, the output a-component is (3^a/4^{a+1})^k R(n)<R(n). This proves both directions. The precision condition suffices for the exclusion direction; exact aligned contraction itself needs no precision hypothesis.

## Two-source classification

Suppose a positive source m with R(m)<R(n) satisfies F_v(n)=F_w(m) on actual paths of lengths t,s<=M, respectively, allowing empty words. For M>=1 assume

    3^H > 1000 A³ 216^M.                                    (2)

Let g=min(t,s), L=2^{s-g}3^{q_v}, B=2^{t-g}3^{q_w}, E=2^{s-g}C_v−2^{t-g}C_w. The physical merger is Bm=Ln+E. Define the virtual companion eta=(L alpha_a+E)/B, the unique rational companion whose w endpoint equals F_v(alpha_a). At any minimizing index b for m one of the following must hold:

1. **Exact root alignment.** eta=alpha_b. The component ratio is exactly
   (d_b/d_a)² 4^{s-t} 3^{q_v-q_w}.
2. **Moving-index resonance.** eta=−1/2, b=h(m)=H+q_v−q_w>=3. Write z_a(n)=3^H u and v_0=2^{1+s-t}u/d_a. Then 2m+1=3^b v_0, and with V=(d_b v_0+1)/2 one has R(m)=3^b V²/3^{v3(V)}. Lowering therefore requires this *actual* ternary valuation to make that number smaller than 3^H u².

These are exhaustive necessary tests for the specified precision. For a fixed n and clock pair all claimed successes must still use ordinary positive, physically legal paths. A matching virtual equation alone would not enforce them.

**Proof.** L,B<=6^M and |E|<=3^M: each scaled positive constant is at most 3^M since C_v<=3^t and 2^{s-t}3^t<=3^s for s>=t. Put P=E d_a−L c_a, so |P|<=6A6^M and B d_a m=L z_a(n)+P. From n>=3^H/A−5 we obtain n>2*3^M, n>5 and m>=n/(2*6^M)>2. Thus every |z_b(m)|>=|d_b|m/2.

If eta differs from −1/2, the integer 2P+B d_a is nonzero and bounded by 13A6^M<3^H. The identity for 2m+1 gives 3^{h(m)}<=13A6^M. In particular 3^b<=13A6^M for every candidate b. Now

    B d_a z_b(m)=d_b L z_a(n)+D_b,
    D_b=d_b P+B d_a c_b,        |D_b|<=11|d_b|A6^M.

When |d_b|<=13A6^M the last upper bound is below 3^H by (2). Thus nonzero D_b would imply 3^{v3(z_b(m))}<=11|d_b|A6^M. This forces

    R_b(m)>=m²/(44 A6^M)>= n²/(176 A216^M)>R(n),

as R(n)<=4A²n²/3^H. Consequently a minimizing b must have D_b=0, exactly eta=alpha_b. The exact merger gives z_b(m)=(d_b/d_a)(L/B)z_a(n), proving the ratio in case 1.

If eta=−1/2, every fixed candidate b=0,1,2 still has |d_b|<=13A6^M and D_b nonzero, so the same exclusion applies. Only the moving candidate remains. Now B d_a(2m+1)=2L z_a(n). The stated b and v_0 follow, with v_0 necessarily an odd positive ternary unit for an ordinary m. Substitution in z_b(m) gives z_b(m)=3^b(d_b v_0+1)/2, yielding precisely case 2.

## A positive no-descent family using the extra case

Fix any integer H>=21 and set b=H. Choose arbitrarily large positive u by the coprime congruences

    u = 60735 * 3^{-H} modulo 2^17,     d_b u+1 = 0 modulo 3^{2b}.

Then n=1+2*3^H u is 121471 modulo 2^18, and m=(n−3)/4 is 30367 modulo 2^16. Here h(n)=1, n=1 modulo 9, and the index-one component R(n)=(n−1)²/3^H=4*3^H u² is the unique minimum: index zero gives n² and index two gives (n+5)²/3.

The physical words are v=111111101100001101 and w=1111101110111100. They have the following parameters:

| word | length | odd count | affine constant | legal source residue |
| --- | ---: | ---: | ---: | ---: |
| v | 18 | 12 | 911729 | 121471 modulo 2^18 |
| w | 16 | 12 | 626513 | 30367 modulo 2^16 |

The constants verify F_v(n)=F_w((n−3)/4) identically. Equivalently F_v(1)=F_w(−1/2)=721585/2^17. The seed n has odd initial run length seven followed by one even step; the next run length is two, so its first A module has length eight. It is not an aligned 10 module. Condition (1) at t=8 holds for H>=21, hence n is unsafe. Its oddness and ternary-unit residue place it in the [actual re-entry support](REENTRY_SUPPORT.md).

On the companion side 2m+1=3^H u. The moving component obeys

    R(m)<=R_b(m)=3^H ((d_b u+1)/2)² / 3^{v3(d_b u+1)}
                 <=3^H u²/4=R(n)/16.

Here 0<d_b u+1<=3^b u and the selected congruence supplies 3^{2b} in the denominator. Thus the merger is both numerically cheaper (m<n/4) and cheaper for the moving rank. Its first arm stays above n throughout: the odd counts at lengths 1,...,18 are 1,2,3,4,5,6,7,7,8,9,9,9,9,9,10,11,11,12; each satisfies 3^{q_j}>2^j. For any further finite length, append that many odd bits to v. The resulting dyadic cylinder refines the displayed source class, and is compatible with the ternary congruence on u by CRT. All those additional steps increase the positive state. There is therefore no finite numerical-descent horizon for this family, even though the same fixed pair of merger clocks certifies a smaller source throughout.

For H sufficiently large (2) applies with M=18. The example then witnesses the exceptional alternative in the classification under its own high-precision hypothesis. None of these existence statements assumes that any of the sources converges. A complete lower-rank cover for arbitrary actual n remains open.

The [finite replay](check_mergers.py) exercises aligned repayment, deliberately mismatched prefixes, and both exact virtual alternatives against physical arithmetic.
