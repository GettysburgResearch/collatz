# Growing moduli for the two Collatz arrival clocks

**Proposed, using Leen's finite-horizon synchronization estimate and Rhin's lower bound for a linear form in two logarithms.** Write T for the shortcut map. Count even and odd inputs separately up to the first visit to a positive target b, allowing a visit at time zero. Let P_X be the subprobability measure on (Z/qZ)² obtained by counting these two residues for the successful sources in [1,X], with weight 1/X per source. Write p_X for its total mass and u_q for the uniform probability on that group. For each fixed 0≤α<1, uniformly for integers 1≤b≤X^α,
    
    ||P_X − p_X u_q||₁ ≪_α q² (log X)^(−5/143).                    (1)

The left side is the sum of absolute differences of point masses. In particular q may grow as any fixed power of log X strictly smaller than 5/286. For a fixed target with positive lower basin density this also gives convergence in total variation conditional on eventual arrival. The same statements apply on any fixed proportional shell, with its own observed basin mass. They also apply to the pair consisting of ordinary and shortcut first-hit times, by an invertible integer change of the two count coordinates.

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

## Removing a nontrivial character

Suppose at least one of U and W is nontrivial. Choose its generator G in {2,3}. There is an integer 1≤d≤q for which the corresponding phase to power d has distance at least one from 1. Apply (5) to z=−(d/q)log G, with B=log 3. Then the real scale multiplier G^d 2^(qi)3^(qj) has logarithm O(q H^(−1/C)), while its character phase is exactly the chosen phase to power d. Iterating (4) costs O_α(q H/√log X). With H as above, the total error is O_α(q (log X)^(−5/143)). One can assume this last quantity is small since |F(X)|≤1. Then all intermediate log-scale changes are O(qH)=O(√log X) and the near-identity real-scale comparison applies. Thus every nontrivial Fourier coefficient of P_X satisfies

    |F(X)| ≪_α q (log X)^(−5/143).                                   (6)

Cauchy–Schwarz and the finite-group Parseval formula bound the left side of (1) by the square root of the sum of squares of its nontrivial unnormalized Fourier coefficients. There are q²−1 such coefficients. This proves (1); in the trivial large-error regime use the absolute bound 2. At fixed nonzero proportional endpoints one can expand α slightly to handle the target cutoff; differences of the two cumulative laws and rescaling give the stated shell conclusions.

Neither conclusion requires the magnitude of p_X to converge as X grows. The cited synchronization input controls the source sampling and (5) distinguishes arrival characters through their two branch phases.
