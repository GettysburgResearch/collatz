# Finite-entropy absolute continuity of the tilted Syracuse laws from 0.21 to 0.550024

For every geometric gap parameter
\[
                   21/100\le\theta\le 68753/125000
\]
the ternary Syracuse law μ_θ is absolutely continuous with finite relative entropy with respect to Haar. For each such θ its ternary chi-square refinement information in Leen's notation satisfies I_n=O_θ(n^{−κ_θ}) with κ_θ>1. The new certified range here is [21/100,1/2]. Leen v1 states the isolated parameter 1/4 and the interval [1/2,0.550024], and explicitly leaves other points below 1/2 unclaimed. The extension uses the author's *general* scalar criterion together with the exact interval calculation below. It gives no new value above 0.550024. [Leen, *Tilted 3-adic Syracuse laws*, Theorem B and §4; v1 source record](https://zenodo.org/records/23268832) · [Independent integer verifier](check_tilted_interval.py)

Write Δ(θ)=−log θ−(1−θ)log(1−θ)/θ−log3 and c*(θ)=log2/(θ log3). Leen's Theorem B and Theorem 3.7 require c>max(1,c*(θ)) with Φ_c(1)<Δ(θ), where
\[
          \Phi_c(1)=\int_1^c \overline{\mathcal E}(1-1/t)\,dt.
\]
The strict inequality then persists for some κ>1 by continuity. The decreasing concave envelope at k∈[0,1] equals log3−(4/3)k log2 at k≤1/4. At k≥1/4 it is the entropy of the ternary vector ((1+2√k)/3,(1−√k)/3,(1−√k)/3). That entropy decreases with √k. These formulas and monotonicities are Leen's ternary entropy envelope lemma. The argument below directly integrates this envelope beyond c=4/3, where the high-parameter source interval no longer needs the nonlinear branch.

Divide [0.21,0.5] into 2900 intervals [a/10000,(a+1)/10000]. For each a choose c=1+j/4096 by rounding c*(a/10000) strictly upward using rational bounds for log2,log3. Since c* and Δ decrease with θ, it suffices to verify Φ_c(1)<Δ((a+1)/10000). The integrand is decreasing, so its left Riemann sum on the time grid of mesh 1/4096 is an upper bound. The largest interval of integration uses 8211 rectangles. To bound the nonlinear branch above, replace √k with floor(2³²√k)/2³², using integer square root; evaluate the two positive entropy terms with upper logarithm bounds.

The program works in integer units 2⁻⁸⁰. Range reduction takes every positive rational logarithm to k log2+2 atanh(t) with 0≤t≤1/3. It encloses each of the first 28 positive Taylor terms using integer division rounded outwards, and adds an upper remainder 9/[4·57·3⁵⁷]. The same series at t=1/3 gives the two bounds for log2. All comparisons deciding the result use integers. The smallest lower gap in the 2900 cells is
\[
             597872500555307996517/1208925819614629174706176>1/10000,
\]
attained in the tested grid cell whose left endpoint is 0.21. This proves the extension. For the higher interval we also replayed Leen's unmodified author verifier on endpoint 68753/125000; it passed 591 adaptive rational cells and reproduced the reported printed margin 2.297×10⁻⁷. The main analytic criterion, including its continuity step, remains imported from the linked primary manuscript. Its v1 TeX SHA-256 is `3855fc67c0c30c0e8e78af3de93fd85279d4376f2cb7c1e5d63d24433ce70afc`.

In particular the ordinary entropy-transfer theorem in this pass now applies throughout the open range 1/0.550024<s/n<100/21 of limiting exact physical-clock slopes, with both endpoints handled by the cheap-reserve argument. It gives the full combinatorial exponential rate at the worst actual integer target throughout this range. For θ<1/2 the resulting slopes concern faster physical stopping relative to the usual inverse word clock, so the extension principally enlarges the joint slice theorem on that side. [Supplied-target entropy transfer](TILTED_ENTROPY_TRANSFER.md)

## Optimized lower dimension of every ordinary escaping grade

Let Γ be any fixed ordinary odd grade in an escaping component, let σ be its upper counting exponent and γ=liminf_v log H_v/v the growth of its least unit at subsequent grade v. With the normalization of the fractional-grade note, 0≤γ≤log(3/2). Then
\[
  \boxed{\quad \sigma\ge s(\gamma),\qquad
       (2^{s(\gamma)}-1)\,3^{1-s(\gamma)}\,e^{\gamma s(\gamma)}=1,
       \quad \log_2(3/2)\le s(\gamma)\le1.\quad}                    \tag{1}
\]
In particular every such actual ordinary grade has upper counting exponent at least log₂(3/2)=0.5849625…, including the fastest possible lower growth of its grade heights. The balanced-total estimate alone gives log₂(4/3)=0.4150375… at that growth.

Fix a tilt θ between 1/3 and 1/2, a=1/θ, g=a log2−log3. At y=H_v, the supplied-target theorem at n=v, total nearest av gives exp[(H_θ−log3−o(1))v] genuine grade-zero unit sources ≤H_v exp(gv+O(1)). Along a subsequence attaining γ this implies σ≥(H_θ−log3)/(g+γ). For 0<s≤1 the supremum over geometric mean costs a>1 of H_{1/a}−sa log2 is log(Σ_{e≥1}2^{−se})=−log(2^s−1), attained at θ=1−2^{−s}; this is the geometric entropy identity, or follows by nonnegativity of relative entropy against that geometric law. Choose s solving (1). Its logarithmic left side is strictly increasing on [log₂(3/2),1]: the derivative there is (log2)2^s/(2^s−1)−log3+γ≥log(4/3)>0. Its value at 1 is γ, and at s₀=log₂(3/2) it is (γ−log(3/2))s₀≤0. Thus the solution is unique in this interval, and its maximizing θ is in [1/3,1/2], where the needed absolutely continuous laws have just been certified. The corresponding ratio equals s. This proves (1) for the ordinary sources in the component. Its upper box dimension of the corrected grade support is at least the same bound by the earlier identity with the nonnegative-grade counting exponent. [Fractional grade and exact box classification](../phase3/FRACTIONAL_GRADE_CLASSIFICATION.md)
