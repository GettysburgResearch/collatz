# A single explicit dyadic measure detects the entire positive basin

**Written theorem.** Let μ be the probability measure on Z₂ for which the successive binary shortcut parities are independent and odd with probability 2/3. These clauses specify consistent masses on ordinary binary congruence classes because each parity word of length k specifies a single residue modulo 2^k. No Collatz convergence information is used to choose μ. For a positive ordinary n its exponential valuation potential
    V(n)=∫ 2^{v₂(n−r)} dμ(r)
is finite exactly when n reaches one. For every nonconvergent ordinary n, its individual tail summands grow exponentially, with an explicit allowance depending on n.

Indeed if P_k counts the odd inputs of n through k shortcut steps, layer summation gives
    V(n)=1+(1/2) Σ_(k≥1) (2/3)^k 2^{P_k}.
On the trivial cycle the summand multiplier per two clocks is 8/9. Thus finite entry into that cycle gives finite V. Every nonconverger stays at least 5 because the four smaller positive starts converge by direct inspection. Its shortcut states therefore satisfy
    1 ≤ T^k n ≤ n (16/5)^{P_k} 2^(−k).
Since 2^23 < 5^10, (16/5)^10 < 2^17. Consequently 17P_k≥10k−10log₂ n, and
    (2/3)^k 2^{P_k} ≥ n^(−10/17) (2^(27/17)/3)^k.
The exponential factor is greater than one by 2^27>3^17. This covers positive cycles disjoint from one and divergent trajectories without an orbit-counting input. The measure has no atoms, since even its largest k-bit cylinder has mass at most (2/3)^k. It is singular to binary Haar by the law of large numbers in the parity code.

In particular the fixed measure does not provide an everywhere-finite rank without a new arithmetic proof that its singular potential is finite at *every* positive integer. Averaging over Haar is insufficient: every k-term in the displayed series has Haar mean one. A more geometric attempted bound samples the same parity bits and applies the two inverse affine maps z↦2z and z↦(2z−1)/3 to a negative starting point, composing outermost-first. Their mean log real slope is log 2−(2/3)log 3<0, so typical infinite inverse words have a finite negative real limit in addition to their dyadic coordinate. The latter assertion follows directly from the law of large numbers and summability of the products of earlier slopes multiplying each bounded affine translation. The negative real support does not separate its dyadic projection quantitatively from a positive n: the finite rational approximants have denominators up to 3^{P_k}. The elementary integer separation bound from 2^k | (3^{P_k}n+h) only limits approximation when the denominator and numerator are simultaneously small enough. On genuinely growing prefixes the denominator can already exceed 2^k. No bound on V at such an n is obtained.

For clarity, neither this exponential kernel nor this specific biased parity measure is the arbitrary diffuse valuation-kernel interpolation of DIFFUSE_RANK. The finiteness decision is nonetheless equivalent to the original convergence question. No novelty claim against broader literature is made.

## Kernel-checked source theorem and a sharper rational gap

With the independently kernel-checked convergence of the positive integers below 20, every nonconverging n remains at least 20. On any high prefix the exact step estimates imply
    2^(3k) (T^k n)^3 ≤ n³ 2^(5P_k).
For even inputs the cubed one-step bound is an equality; at odd inputs it follows by 3n+1≤(61/20)n and 61³<32·20³. On a nonconverger one obtains
    [(2/3)^k 2^{P_k}]^5 ≥ (256/243)^k/n³.
The companion `lean/BiasedParity.lean` imports the previously checked `QuarterShift` endpoint, odd count and finite floor. For every fixed positive natural it proves that boundedness of these real summands, summability of their series, and actual arrival at 1 are equivalent. It also checks the finite cubed estimate and the cleared fifth-power bound. The construction of the measure and the layer integral identifying this series are written mathematics.

## A finite-place obstruction in every prescribed ordinary cylinder

All negative ordinary inputs have infinite V: their shortcuts stay negative, and 1≤|T^k n|≤|n|3^{P_k}/2^k. In fact the sign of the real coordinate is insufficient in either direction. The positive rational 19/5 has cyclic shortcut states 19/5,31/5,49/5,76/5,38/5 and parity word 11100. Its term multiplier per period is 256/243>1.

More strongly, fix any finite set S of primes, any finite positive floor B, and any finite parity prefix of an ordinary positive source. There is a *nonintegral* positive rational x implementing that same prefix, lying in Z_l for every l in S, and staying above B forever, with infinite biased potential. The statement imposes integrality at S, not arbitrarily specified residues at every prime in S. Its binary congruence prefix is exactly prescribed.

Let D₀ be a common multiple of l−1 for all l>3 in S, using 1 for the empty list. Choose a≥3 congruent to 1 modulo D₀; then 2^a−3 is odd, is not divisible by 3, and is −1 modulo each such l. Pick a prime h dividing 2^a−3. It is outside S and greater than 3. Let D₁=lcm(D₀,h−1). Choose p≡1 mod D₁ and k≡a mod D₁ with k log 2−p log 3 tending to zero from above and p,k tending to infinity. This is an irrational rotation: substitute p=1+D₁j into p log₂3 and select an integer k in the requested progression just above it with arbitrarily small positive error. Eventually k>p. The rational
    r=(3^p−2^p)/(2^k−3^p)
is a positive odd 2-adic integer. Its denominator before reduction is prime to 2 and 3, and is −1 modulo all l>3 in S; it is divisible by h whereas its numerator is 1 modulo h. It therefore remains genuinely nonintegral after reduction. Directly,
    r+1=2^p (2^(k−p)−1)/(2^k−3^p)
has exact binary valuation p, and p odd shortcut inputs take r to 2^(k−p)r. The following k−p halvings return to r. The minimum over this entire rational cycle is r, which tends to infinity since
    r=[1−(2/3)^p]/[2^k/3^p−1].
Take r sufficiently large for the needed floor and prefix. The same elementary high-prefix inequalities apply to this rational cycle (choose its minimum above 20 as well), or compute its period multiplier directly from p/k→log₃2; its tilted shortcut terms A_k=(2/3)^k2^{P_k} grow geometrically across laps.

For the prescribed word of length J and c odd inputs, write its forward affine map x↦(3^c x+C)/2^J. When c>0 the terminal congruence 2^J y≡C mod3^c is a unit class: the last odd addition contributes a power of two modulo three. Since 2 generates the units modulo every 3^c, choose t≥0 so y=2^t r lies in that class. For c=0 take t=0. Put x=(2^J y−C)/3^c. This is the exact 2-adic inverse word, so x has the prescribed prefix. The congruence makes x 3-integral; all other S-integrality is preserved and h remains in its reduced denominator since h is prime to six. Each fixed-prefix inverse affine expression has positive slope, hence all of its finitely many states exceed B once r is sufficiently large, uniformly since y≥r. The endpoint y subsequently halves to r. After the finite prefix and halvings, the positive term accumulator differs from that of r only by a fixed positive factor, proving divergence. This does not realize a counterexample in the positive ordinary integers.

For a small exact control take p=17,k=27. The resulting r=129009091/5077565 is greater than 25, is integral at 2,3,7 and is not integral at 5. A prefix 1110 is obtained by taking y=2^9 r, then x=(16y−19)/27. The future of that x reaches the stated positive rational cycle above 20.

## The remaining ordinary estimate

If S(n)=1+Σ_{k≥1} A_k(n), first-step splitting gives the extended-real equations
    S(2n)=1+(2/3) S(n),       S(2n+1)=1+(4/3) S(3n+2).
The detector V=(1+S)/2 is finite exactly where S is finite. A finite nonnegative supersolution of these inequalities on *all* positive integers would dominate every finite partial sum by iteration and prove finiteness. The raw Euclidean coordinate, the negative real stationary coupling, and any fixed finite set of integrality conditions do not furnish such a supersolution. In particular the preceding rational examples satisfy the identical deterministic recurrences in every prescribed parity cylinder while remaining above any prescribed floor. A proof of a uniform partial-sum bound for each one fixed positive ordinary n is still missing.
