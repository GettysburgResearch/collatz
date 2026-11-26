# Quadratic sign characters on one fixed ordinary orbit

**PROPOSED written proof.** A completely multiplicative quadratic sign character here means a homomorphism from `V=Q_{>0}^*/(Q_{>0}^*)²` to `{−1,1}`. Choose its value at each prime independently with equal probabilities, equivalently Haar probability on the compact dual of `V`. This probability space is a space of **characters**, with the actual positive integer starting value held fixed throughout. It assigns no probability to Collatz trajectories.

## A8. Almost every character codes every injective ordinary orbit normally

For Haar-almost every character `χ`, simultaneously for every positive odd starting value with an injective trajectory, each finite sign pattern of length `k` in the accelerated sequence `χ(x₀),χ(x₁),…` has limiting frequency `2^{-k}`.

Fix such a starting value `x₀`. Write `x_i=U^i(x₀)` and `A_N=∑_{i<N}v₂(3x_i+1)`, the number of shortcut steps covering its first `N` odd transitions. All shortcut states are distinct; a repetition would force eventual periodicity. Telescoping and the harmonic bound on distinct positive integers give

$$A_N\log2=N\log3+\log x_0-\log x_N+\sum_{i<N}\log(1+1/(3x_i))
\le N\log3+\log x_0+(1+\log N)/3.$$

In particular `N≤A_N≤2N` for all sufficiently large `N` depending on `x₀`.

Take `H=floor(√(log₂N)/4)` and partition these first `A_N` shortcut departures into `L=ceil(A_N/H)` disjoint consecutive blocks of length at most `H`. For large `N`, `2^{(3H+7)(H+2)}<√N`. Call a block low if its first shortcut value is at most `√N`. Distinctness bounds the number of low blocks by `√N`, hence their total number of odd departures by `H√N`. In every other block, A2 of [the squareclass argument](README.md) proves that its `m≤H` odd-departure values have physical squareclass rank at least `m−3`.

For these fixed values the joint `m` sign evaluations of the random `χ` are uniform on a subgroup of `{−1,1}^m` of size `2^rank`. The restriction map is surjective onto the dual of their span: a linear functional on that span extends to the full vector space. Thus expectation of any nonnegative function of that sign vector is at most eight times its expectation under `m` independent fair signs.

It is enough to prove decay of the averages of all nonempty Walsh monomials. Fix a nonempty subset `J⊆{0,…,k−1}` and put `Y_i=∏_{j∈J}χ(x_{i+j})`. Work initially with starts for which the entire length-`k` word lies inside the first `N` odd departures. Discard words meeting low blocks, or crossing a shortcut-block boundary. The number discarded is at most `H√N+(k−1)L+O(k)` when one first discards all boundary-crossing words and then the words wholly inside low blocks. This is `o(N)` for fixed `k`.

For a high block `b`, let `S_b` be the sum of its remaining internal `Y_i`; put `S_b=0` for a low block. Under independent signs, the distinct shifted monomials of this fixed nonempty `J` are themselves independent fair signs. Indeed their binary incidence vectors are independent by looking at the greatest index `i+max J` of the largest shift in a putative relation. Therefore, for each real `λ`,

$$\mathbb E\exp(\lambda S_b)\le 8 (\cosh\lambda)^H\le8\exp(H\lambda^2/2).$$

Hölder's inequality with `L` identical exponents applies even though all blocks use the **same character**. It gives `E exp((λ/L)∑S_b)≤8 exp(Hλ²/2)`. Markov's inequality and its negative counterpart, with `λ=εN/(LH)`, yield

$$\Pr\left(\left|\sum_bS_b\right|>\epsilon N\right)
\le16\exp\left(-\frac{\epsilon^2N^2}{2L^2H}\right)
\le16\exp(-c\epsilon^2H)$$

for an absolute `c>0` and large `N`, using `L≤3N/H`. On each geometric grid `N_j=⌊(1+1/r)^j⌋`, `r` a fixed positive integer, these probabilities are summable since `H` grows as `√j`. Borel–Cantelli and the deterministic discarded `o(N)` contribution give convergence to zero along that grid for every positive rational tolerance. Partial sums change by at most one per term. Interpolating and letting the integer `r` tend to infinity gives convergence along all `N`. The finitely many Walsh coefficients of each length-`k` pattern indicator now give frequency `2^{-k}`. The union of exceptional null sets over all finite patterns and all positive integer starting values is still null.

## A9. Three specified characters carry a compulsory bias

On odd integers define `χ₋₁(x)=(-1)^{(x−1)/2}`, `χ₂(x)=(-1)^{(x²−1)/8}`, and `χ₋₂=χ₋₁χ₂`. These are three fixed multiplicative characters, extending to positive rationals after assigning arbitrary signs to 2. Checking the four odd residues modulo 8 gives

$$a(x)\ge1+\mathbf1_{x=1\bmod4}+\mathbf1_{x=5\bmod8}
=\frac{7+3\chi_{-1}(x)-\chi_2(x)-\chi_{-2}(x)}4.$$

Consequently on **every** fixed injective ordinary orbit, with `⟨·⟩_N` the average of the first `N` odd departures,

$$3\langle\chi_{-1}\rangle_N-\langle\chi_2\rangle_N-\langle\chi_{-2}\rangle_N
\le 4\log_2 3-7+O((\log x_0+\log N)/N).$$

At each sufficiently large horizon the largest of the three absolute biases is at least `(7−4log₂3)/5−o(1)`, a positive constant greater than 0.13. At least one fixed character has absolute limsup at least this constant. Thus three named dyadic tests furnish a pointwise escape target. A8 gives no equidistribution for these three specific signs. Prescribing finitely many signs by Frobenius classes and then letting the number of prescribed signs increase also does not exchange these quantifiers.

A concrete fixed-root arithmetic comparison illustrates why the two normalized size records alone cannot supply that step. The positive ordinary affine orbit `y_i=8·3^i−1`, `y_{i+1}=3y_i+2`, has `3^{-i}y_i=7+(1−3^{-i})`: a bounded increasing real offset with `v₃(1−3^{-i})=−i` for each `i≥1`. Yet all its terms are `7 (mod 8)`. The positive binary clocks and their exact divisibility in the Collatz map are additional structure.

On the actual map, a rise has an exact equivalence from [A6](GROWTH.md): its triple of consecutive odd nodes is independent precisely when the third is nonsquare. The A4 private-prime bound gives zero natural density of square nodes along an injective orbit in odd time. To see this, first take its zero upper Banach density in shortcut time, then use `A_N≤2N`. Since `a_i≥2` outside the rises and `A_N≤N log₂3+O(log N+log x₀)`, independent rise triples have lower density at least `2−log₂3` in accelerated time. This is an orbitwise conclusion on an assumed escape, not an independently established upper bound.

The actual finite clocks link the named dyadic characters to the dynamics. For example, each physical edge satisfies `−3x_i+2^{a_i}x_{i+1}=1`, and each pair satisfies its exact affine congruence modulo its endpoint numerators. These identities accommodate fully independent local squareclasses on known convergent controls (A5). This attack has no argument making a specified dyadic character generic on a fixed positive escape and no proof of universal convergence.
