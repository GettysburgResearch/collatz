# Arithmetic progressions have the same logarithmic component frequencies

**PROPOSED, with an external fine-scale mixing input.** Let f be a bounded real function on the positive integers, T the shortcut Collatz map, and take any sequence of windows [A,B] with 1≤A≤B and log(B/A) tending to infinity. Normalize sums with weight 1/n by log(B/A). Suppose the normalized average of |f(Tn)−f(n)| tends to zero on these windows. For every fixed modulus q and residue a,

    avg f(n)·(1_(n=a mod q)−1/q) → 0.

In particular this holds for each merger-component indicator and each fixed-target predecessor indicator, including a target lying outside a cycle. It requires no existence of a global logarithmic density. A single defect at the target has vanishing average. The conclusion concerns a fixed residue progression, not a modulus increasing with the cutoff.

## 1. The stationary law is equivalent to Haar measure on ternary units

Use the ordinary random affine maps D(x)=x/2 and E(x)=(3x+1)/2 on the 3-adic integers, chosen independently with probability one half each. Write h_3 for normalized additive Haar measure. Tao's Syracuse offset law μ on the 3-adic units is stationary:

    μ = Σ_(a≥1) 2^(−a) [(3x+1)/2^a]_* μ
      = (D_* μ + E_* μ)/2.

The second equality follows by shifting the summation index. Tao's Proposition 1.14 bounds in total variation the distance between its reduction modulo 3^n and the lift of its reduction modulo 3^m with uniform upper digits, by O_J(m^(−J)), uniformly for n≥m. The lifted measures on the full 3-adic space are thus Cauchy in total variation: for two levels this is precisely the same finite sum, since both have uniform higher digits. Their limit has the finite marginals of μ and is absolutely continuous with respect to h_3. We use the proposition as a published input. [Terence Tao, Proposition 1.14 and equations (1.25)–(1.27)](https://arxiv.org/abs/1909.03562)

Conversely μ≥D_*μ/2. For the positive set P of its density, D(P) is contained in P up to Haar null sets. D is Haar-measure preserving on the units, so the sets agree modulo null sets. Multiplication by 2 is ergodic there: 2 is primitive modulo 3^m for every m (the order starts at 2 modulo 3 and v₃(4^(3^j)−1)=j+1 by binomial expansion). A D-invariant set has therefore equal conditional Haar frequencies on all unit cylinders at every level. Martingale convergence makes its indicator constant almost everywhere. P has positive measure, so μ and h_3 restricted to units have identical null sets.

## 2. An equation for the actual source averages

First fix an integer m coprime to 6. Put K=Z_3 × Z/m and let λ be product Haar probability. Ordinary positive integers embed diagonally and are Haar equidistributed under our logarithmic averages. On finite congruence classes this follows from bounded partial sums of a mean-zero periodic function and summation by parts. On any subsequence where the signed measures given by f(n)/n converge weakly on K, the limit is hλ with |h|≤sup|f|, by domination and the reference equidistribution. One can extract such a subsequence by a diagonal selection on finite cylinders.

Even sources n=2v transfer to v with weight 1/2. Odd sources n=(2v−1)/3 transfer to v≡2 mod3 with weight 3/2 up to a summable error. The replacements of f(n) by f(Tn) cost o(1) by hypothesis. Multiplying window endpoints by fixed constants changes normalized logarithmic sums by o(1); bounded shifts have the same property. Thus, against every locally constant test φ on K, the limit satisfies

    ∫φ h dλ = (1/2) ∫φ(2v)h(v)dλ(v)
             + (3/2) ∫_(v=2 mod3) φ((2v−1)/3)h(v)dλ(v).

The affine change of variables in the second integral maps K onto a coset of Haar mass 1/3; in the Z/m coordinate 3 is invertible. Hence in the input variable x,

    h(x) = [h(Dx)+h(Ex)]/2   λ-almost everywhere.                 (1)

This derives a harmonic equation for densities of ordinary observations. It does not assume f itself extends to a continuous or measurable 3-adic invariant.

## 3. Only constant bounded densities satisfy (1)

On the unit part of K, μ times the uniform probability on Z/m is stationary: both maps induce permutations on Z/m, and Section 1 gives stationarity on Z_3. This product measure is equivalent to the reference there. Its Markov operator Pφ=(φ∘D+φ∘E)/2 has Cesàro powers tending in L¹ to the stationary mean.

Here are details. On the finite factor the random walk is irreducible. D and E generate a permutation group containing translation by a unit: D∘E and E∘D have the same slope and their outputs differ by 1/4. Consequently any finite residue reaches any other. D fixes 0, so this finite walk is aperiodic and its powers converge to uniform. For a test depending only on the first s ternary digits and on Z/m, split a long word into a prefix and a terminal block of length l. With probability tending to one as l increases, the terminal block contains at least s copies of E. Its slope is then divisible by 3^s, so its final ternary digits are independent of the initial point. Conditional on the terminal block, the preceding long random walk mixes the finite residue independently of these prescribed final ternary digits. Let the prefix length tend to infinity, then l tend to infinity. Stationarity identifies the limiting mean. This proves convergence for cylinder tests, even without Cesàro averaging. The operator is an L¹ contraction by stationarity, so density extends convergence to L¹. Every bounded harmonic h is therefore constant on units, up to Haar null sets.

For x a ternary multiple, E(x) is always a unit and E is nonsingular for Haar null sets. Subtracting the unit constant from (1) gives h(x)−c=(h(Dx)−c)/2 almost everywhere there. Iteration and boundedness give h=c. Thus *every* subsequential limit on K is a constant density; the constant may depend on the subsequence. This proves the assertion for all odd moduli, by separating the power of three and the coprime factor.

## 4. Restore fixed binary digits

For n=r mod 2^j, the first j parities are fixed. If they contain l odd steps, T^j(r+2^j t)=v+3^l t for one integer v. Additional restriction to a residue mod an odd number d restricts the endpoint to one class modulo 3^l d. The departure from f-invariance through j steps is still negligible: each fixed iterate has finitely many affine inverse branches, comparable positive weights and only fixed multiplicative changes to the windows. On this source progression the reciprocal weight transforms into (3^l/2^j) times the endpoint reciprocal, with a summable error away from finitely many small inputs. The preceding odd-modulus result gives the relative mass 1/(2^j d), as required.

This theorem strengthens a finite-period predictor obstruction. The [PR #142 predecessor](https://github.com/GettysburgResearch/collatz/blob/b21f94f5772df5cfcaa5f5afd073d5889e75d294/research/beeping-density-swarm-20261030/REGULARITY_BRIDGE.md) assumed mean approximation by binary-periodic functions for its Liouville implication. Here orthogonality to every fixed nonconstant periodic character follows directly, even for indicators of different pure basins with a finite invariance defect. Such orthogonality alone cannot identify the full observable with its constant projection.
