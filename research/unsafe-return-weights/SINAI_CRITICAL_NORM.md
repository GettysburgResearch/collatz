# Critical Haar moments of the Syracuse offset density

**PROPOSED, source-qualified.** Write m for Haar probability on the 3-adic integers. Let `g_q=3^q μ_q` be the ternary cylinder densities of the independent geometric Syracuse offset, `g_0=1`. The [subcritical norm proof at d38541225127acf076879dfb180140e8491ffaa1](https://github.com/GettysburgResearch/collatz/blob/d38541225127acf076879dfb180140e8491ffaa1/research/native-pressure-20261118/ANTICHAINS.md) gives uniform L^r bounds for every 1<r<2 using Tao's fine-scale mixing theorem and the integer spacing second-moment bound. Consequently the martingale converges to a probability density g in each such L^r. The finite-depth second-moment upper bound there is `16(q+1)^2`.

For `L(z)=4z+1`, a Haar-preserving permutation, the transfer is

    g_(q+1)(y) = Σ_{a≥1} 3·2^(−a) 1_{2^a y≡1 mod 3} g_q((2^a y−1)/3).

For each fixed a the change of variable `y=(3z+1)/2^a` scales Haar measure by 1/3. Two terms with indices a<b have simultaneous support only for `b=a+2k`, k≥1, and their source arguments are z and L^k z. The diagonal square terms have total multiplier `3 Σ_a 4^(−a)=1`. Hence `E_q=∫g_q² dm` satisfies the exact identity

    E_(q+1)−E_q = 2 Σ_{k≥1} 4^(−k) ∫ g_q(z) g_q(L^k z) dm(z).        (1)

Let `A_q={g_q≥1/2}`. Its Haar probability is at least an absolute δ>0 since ∫g_q=1 and ∥g_q∥_(3/2) is uniformly bounded. Choose an integer K≥2/δ². For `S=Σ_{0≤i<K} 1_A∘L^i` we have `∫S²≥K²δ²`. The total of the diagonal terms is at most K, so at least one k in `[1,K)` gives `m(A∩L^(−k)A)≥δ²/2`. The corresponding term of (1) is uniformly positive. Thus `E_q≥1+cq`. For r>2, positivity and the diagonal r-powers alone give

    ∫g_q^r dm ≥ b_r^q,      b_r = 3^(r−1)/(2^r−1)>1.                (2)

The inequality follows since `(2/3)^r−(1/3)^r<1/3` for r>2: its derivative is negative for r≥2. Equations (1) and (2) make 2 the exact uniform moment threshold, with divergence already at the endpoint.

The limiting law has a quantitative moment singularity. The transfer is bounded on L¹ by positivity and preservation of integrals, so g satisfies the same fixed-point equation. Apply the overlap argument just used to `A={g≥1/2}`. Fix a k with positive overlap and take branches `a=1` and `b=1+2k`. On the image of `A∩L^(−k)A` both terms in the transfer of g are bounded below by a fixed positive η. For `3/2≤r<2`, the excess of their rth power of the sum over the sum of the individual rth powers is at least `(2^r−2)η^r`, by monotonicity in each term. The remaining branches have nonnegative excess by convexity. After integration this gives

    (1−b_r) ∫g^r dm ≥ c > 0                                              (3)

uniformly on that range. Since `b_2=1` and its derivative there is `log 3−4(log 2)/3>0`, (3) implies `liminf_(r↑2) (2−r)∫g^r dm>0`. In particular `limsup_(t→∞) t² m{g>t}>0`, allowing infinity: a tail o(t^(−2)) would make the displayed limit zero by integrating `r t^(r−1)m{g>t}` and splitting at a large fixed threshold.

On a divergent odd spine y_j, a depth-j cylinder of density at least a fixed multiple of y_j costs Haar measure `3^(−j)`. The available subcritical moments by themselves give `y_j≪3^(j/r)` for fixed r<2. Even the limiting exponential base √3 exceeds the elementary odd-step base 3/2. Linear-size density at a sparse collection of ordinary integers is compatible with these global Haar estimates.
