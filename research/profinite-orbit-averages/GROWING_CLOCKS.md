# Growing moduli for the two Collatz arrival clocks

**Proposed, using Leen's finite-horizon synchronization estimate and Rhin's lower bound for a linear form in two logarithms.** Write T for the shortcut map. Count even and odd inputs separately up to the first visit to a positive target b, allowing a visit at time zero. Let P_X be the subprobability measure on (Z/qZ)² obtained by counting these two residues for the successful sources in [1,X], with weight 1/X per source. Write p_X for its total mass and u_q for the uniform probability on that group. For each fixed 0≤α<1, uniformly for integers 1≤b≤X^α,

    ||P_X − p_X u_q||₁ ≪_α q (log X)^(−5/143).                    (1)

The left side is the sum of absolute differences of point masses. In particular q may grow as any fixed power of log X strictly smaller than 5/143. For a fixed target with positive lower basin density this also gives convergence in total variation conditional on eventual arrival. The same statements apply on any fixed proportional shell, with its own observed basin mass. They also apply to the pair consisting of ordinary and shortcut first-hit times, by an invertible integer change of the two count coordinates.

For any union A of complete positive merger components, put p_A(X)=X⁻¹|A∩[1,X]|. For t in a fixed compact subinterval of (0,∞),

    |p_A(tX) − p_A(X)| ≪ (log X)^(−5/143).                         (2)

The implied constant is uniform in the component union. Hence any interval [Y,Y+H] with Y comparable to X and H≫X/(log X)^η for fixed η<5/143 has component frequency p_A(X)+o(1), uniformly in its location. Equation (2) also applies to any of the above target basins.

## From synchronization to two dilation estimates

For q-th roots of unity U,V put f(n)=U^e V^o on hits and zero otherwise, where e,o count the even and odd inputs before first arrival. For (2) one can also let f be the indicator of the chosen union with U=V=1. Write F(Y)=Y⁻¹∑_{1≤n≤Y} f(n), using real cutoffs. For all Y with |log(Y/X)|=o(log X),

    Y⁻¹ ∑_{n≤Y}|f(n+1)−f(n)| ≪_α (log X)^(−1/2).                  (3)

Indeed take h=⌊(1−α)log₂(X)/4⌋. The fraction of residues modulo 2^h where adjacent inputs have failed to merge at a common time with the same odd count by h is O((1+h)^(−1/2)). Complete periods and one incomplete period give at most O(Y/√h+2^h) failed pairs through Y. Inputs ≤2^h b cost at most 2^h b more. Above this cutoff all paths stay above b up to h, so the balanced common future gives identical labels. The indicated powers of X are absorbed into (3); it suffices more explicitly to use Y≥X^((3+α)/4) for the large-X estimates below. For component labels the target cutoff is unnecessary. [Leen, exact rates and finite-block counts](https://doi.org/10.5281/zenodo.23268751) · [Qualitative clock argument](CLOCK_CHARACTERS.md)

Writing each pair or triple of adjacent inputs as equal up to the sum of (3)'s differences lets one replace a full sum by two or three times the sum on one residue class. Apart from the first visit at b, the branch identities are f(2n)=U f(n) and f(2n+1)=V f(3n+2). They give

    F(2Y)=U F(Y)+O_α((log X)^(−1/2)),
    F(3Y)=W F(Y)+O_α((log X)^(−1/2)),       W=U/V.                 (4)

Floors and the one possible exceptional input per identity cost O(1/Y). Each use of (4) costs the same in the reverse direction, since both factors have modulus one.

## A quantitative real approximation

Set C=13.3. For each fixed B, every |z|≤B, and all H≥2, there are integers i,j with

    |i|+|j| ≪_B H,       |i log 2+j log 3−z| ≪_B H^(−1/C).          (5)

To verify this, let p/s be the last continued-fraction convergent to log 2/log 3 whose denominator is ≤H. The next denominator s' exceeds H. Rhin's estimate gives ||s log 2/log 3|| ≫ s^(−C) whereas convergence gives ||s log 2/log 3||<1/s'. Hence s≫H^(1/C). The points a p/s for 0≤a<s form the full 1/s mesh modulo one. Replacing p/s by the irrational ratio moves each by at most 1/s'. Round off the integer part of z/log 3 to obtain the two coefficients. Enlarged constants cover bounded H. [Rhin bound as stated by Rozier and Terracol, with source location](../cyclic-shift-distance/README.md)

For (2) use z=log t and (5), then iterate (4). A path of O(H) dilations can change log Y by at most O(H). Also |F(Y')−F(Y)|≪|log(Y'/Y)|+1/min(Y,Y') for nearby positive scales. The total error is O(H/√log X+H^(−1/C)). With H=(log X)^(C/(2(C+1))) this is O((log X)^(−1/(2(C+1)))) and the exponent is 5/143.

## Averaging translations in total variation

Let the value of f be a point mass at the two residues on a hit and the zero measure otherwise. Use its ℓ¹ norm throughout (3) and (4). A disagreement between two labels costs at most two, the same as for scalar labels. The multipliers for dilation by 2 and 3 are now translations by g₂=(1,0) and g₃=(1,−1). Both preserve ℓ¹ distances. The two vectors form an integer basis.

For any desired residue shift g, choose coefficients a,b in [0,q) with g=a g₂+b g₃ modulo q. In (5) take z=−(a log 2+b log 3)/q, which is bounded independently of q. The multiplier 2^(a+qi)3^(b+qj) has logarithm O(q H^(−1/C)), while its translation is exactly g. Iterating (4) costs O_α(q H/√log X) in ℓ¹. Take H as above. We may assume q (log X)^(−5/143) is bounded by a small constant since the total error is always ≤2. Then intermediate log-scale changes are O(qH)=O(√log X). Moving the endpoint by the remaining near-identity scale costs O(q H^(−1/C)+1/Y) in ℓ¹ by counting the affected sources. Consequently

    sup_g ||P_X − τ_g P_X||₁ ≪_α q (log X)^(−5/143).

Average over g; the average of all translations is p_X u_q. This proves (1). For shells, at each fixed nonzero endpoint one can expand α slightly to handle the cutoff, then difference and rescale the two cumulative laws. The same translation proof allows an arbitrary auxiliary label space on which translations act trivially, provided the auxiliary label agrees after the balanced meeting and satisfies its branch identities away from the small cutoff used in (3). All estimates are independent of the size of that label space.

## The unrestricted global minimum and its first arrival

For a uniform source n≤X, let m(n) be the smallest positive value on its whole forward orbit and record the even and odd shortcut counts up to its first visit. The minimum exists for every positive orbit, and taking the shortcut leaves its value unchanged. Write Π_X for the joint empirical probability of the minimum and both count residues, and p_X^min for the empirical distribution of the minimum itself. Then

    ||Π_X − p_X^min ⊗ u_q||₁ ≪ q (log X)^(−5/143).                  (6)

This estimate sums the errors over *all* minimum values and clock classes simultaneously. In particular it applies to every collection of minimum values, even one chosen afresh for each X. It describes the clock to an orbit's own minimum and imposes no hypothesis about its later orbit.

To see this, first suppress sources with m(n)>X^(19/20). On all remaining sources label by the actual minimum as well as the first-arrival clock. At inputs larger than X^(19/20) the minimum, conditional on inclusion, is strictly later, so the branch identities in (4) hold for this vector label. For inputs below the cutoff, allowing an exception for *every* input costs O(X^(19/20)/Y), still negligible at our intermediate scales. In (3), a synchronized pair starting above 2^h X^(19/20) has all pre-meeting values above the cutoff. Its common future therefore determines whether either is included and, if included, their shared minimum and the equality of both clock classes. The vector proof applies verbatim with α=19/20 and its constants.

The suppressed population has mass O(X^(−c)) for some c>0, by a direct binary-cylinder estimate. Take r=⌊(log₂ X)/2⌋. The first r parities on a complete modulus 2^r run through every binary word exactly once (induct on r using the invertible odd multiplier at each fixed parity). Except for at most O(X exp(−c₁r)+2^r) starts the odd count is ≤0.55r by the binomial tail bound. For such n,

    T^r(n) ≤ X (3^0.55/2)^r + (3/2)^r ≤ X^(19/20)

for sufficiently large X. The additive term bounds the affine bonus by maximizing all branches at each step. The two power exponents on the left are 1+(0.55 log₂3−1)/2 < 0.94 and (log₂3−1)/2 < 0.30. Adding back the discarded mass proves (6).

## A logarithmic sample

If a source in [X^a,X] is instead drawn with weight proportional to 1/n for fixed 0<a<1, both (1) and (6) improve to O_a(q/√log X), with fixed targets in (1), or uniformly for targets b≤X^β with fixed β<a. Use (4) on the range [X^a,X] with a synchronization horizon that is a sufficiently small fixed multiple of log X. The full minimum vector satisfies (3) and (4) at each local scale Y regardless of the target cutoff, since suppressing minima larger than Y^(19/20) on each of [1,Y], [1,2Y] and [1,3Y] costs O(Y^(−c)) by the same binomial bound. The latter estimate uses T^r(n)≤3Y (3^0.55/2)^r+(3/2)^r at r=⌊(log₂Y)/2⌋.

Average the resulting cumulative vector F(Y) with measure dY/Y on [X^a,X], dividing by (1−a)log X. A change Y↦2Y or 3Y now costs O_a(1/log X) from the endpoints. This mean differs from the normalized harmonic sample by O_a(1/log X) in ℓ¹, by partial summation. Thus each of the two translation generators changes the sample by O_a(1/√log X). Every group element uses at most 2q generator steps. Averaging its translations again gives the stated bound. In particular q=o(√log X) is allowed on these growing logarithmic windows.

The cited synchronization theorem controls source sampling. The real approximation is used to distinguish arrival residues on a single proportional shell.
