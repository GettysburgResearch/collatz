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

## A stopped transfer identifies the full tail exponent

For every δ>0 there are positive constants c_δ,C_δ such that, for all u≥1,

    c_δ u^(−2−δ) ≤ m{g>u} ≤ C_δ u^(−2+δ).                         (4)

The same bounds hold for g_q for every fixed η in `(0,d)` once q is sufficiently large and `1≤u≤exp((d−η)q)`, where `d=log 3−(4/3)log 2>0`. Thus the logarithmic tail exponent tends to −2 on the infinite law and on all such finite-depth sequences with u→∞.

Define `H_q(u)=∫(g_q−u)_+ dm` and `G_q(u)=u H_q(u)`. The function `(x−u)_+` is superadditive on nonnegative arguments. Put `J_a=3/2^a` and `p_a=J_a²/3=3·4^(−a)`. The same change of variable as in (1) gives

    G_q(u) ≥ Σ_a p_a G_(q−1)(u/J_a).

The p_a sum to one. Draw independent exponents with law p_a and let `S_k=Σ log J_a`. These bounded-above increments have mean d and finite variance. Stop at the first k with `S_k≥log(2u)`. The entering argument `v=u exp(−S_k)` lies in `[1/3,1/2]` since each increment is at most log(3/2). At every remaining level s, convexity and ∫g_s=1 imply `G_s(v)≥v(1−v)≥1/6`. Iterating the inequality up to this stopping time or q, retaining only stopped paths, yields

    G_q(u) ≥ (1/6) Pr{max_{k≤q} S_k ≥ log(2u)}.                     (5)

The right side is bounded below by 1/12 uniformly on the finite-depth range above, by the law of large numbers applied to S_q. For fixed u, let q→∞; L¹ convergence gives `u ∫(g−u)_+ dm≥1/6`. In particular this also gives a direct proof of linear growth of E_q, even without the subcritical norm bound, by integrating `H_q(u)≫1/u` up through `exp(dq/2)` and using `∫_0^∞ H_q(u) du=E_q/2`.

For either law, `H(u)≤∥g∥_r m{g>u}^(1−1/r)` with the uniform norm at the appropriate depth. Choose r<2 close enough to 2 that `r/(r−1)≤2+δ`, and apply the lower bound on H. Markov's inequality with r sufficiently close to 2 gives the other side of (4). No equality of tail constants is asserted.
