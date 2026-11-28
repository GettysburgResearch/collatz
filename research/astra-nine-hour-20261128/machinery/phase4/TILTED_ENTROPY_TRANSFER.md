# From an absolutely continuous tilted Syracuse law to sharp ordinary fixed-total inverse counts

For 0<θ<1 let p_θ(e)=θ(1−θ)^{e−1} on e≥1, and set
\[
 a(\theta)=1/\theta,\quad H_\theta=-\log\theta-
           ((1-\theta)/\theta)\log(1-\theta),\quad
 b(\theta)=H_\theta-\log3,\quad g(\theta)=a(\theta)\log2-\log3.
\]
The tilted ternary Syracuse law μ_θ is the law of the infinite inverse offset β with iid p_θ gaps. This paper proves the following transfer under explicit external hypotheses.

**Theorem.** Suppose θ belongs to an open interval on which μ_θ is absolutely continuous with respect to ternary Haar, b(θ)>0 and g(θ)>0. Assume Weaver's supplied-state finite-policy theorem and the positive central row floor. With R_F as in the moderate-deviation note, for any sequence of integers n,s with n→∞ and s/n→a(θ),
\[
       \boxed{\quad \lim_{n\to\infty}\frac1n
         \log\inf_{y>0,\ y\ {\rm odd},\;3\nmid y}R_1(y;n,s)
                          = H_\theta-\log3.\quad}                    \tag{1}
\]
The admissible sources are actual positive odd units with n odd steps, exactly s shortcut steps into the prescribed y and real inverse offset β≤1. The lower bound is uniform in the *original* target before taking the infimum. The matching upper exponent concerns the infimum. The supplied-state theorem is Weaver 127 v1, Theorem 5 (finite-precision, capped, strictly positive legal branch probabilities). The central floor is the pure ternary fixed-total estimate. The literature reports absolute continuity on [1/2,0.550024] from Leen's tilted Syracuse preprint; thus the numerical application here uses its **open interior**. The source dependencies are written mathematical inputs. The primary Zenodo v1 record, PDF, TeX and checkpoint supplement were retrieved. The PDF SHA-256 is `73872cd4d195e7c4ad66778af2f016d7dbd2c754953255bf2c6516c348ddbaad`, the TeX SHA-256 is `3855fc67c0c30c0e8e78af3de93fd85279d4376f2cb7c1e5d63d24433ce70afc`, and the supplement SHA-256 is `d16dadd2cc39a3d78f28755d17dffa9301e69f30c2c357370b68c86393206e75`. Leen’s Theorem B(a) and the interval theorem in §4 establish the stated absolute continuity with finite relative entropy. The author reports the general scalar criterion kernel-checked in a then-unreleased Lean development. Its interval certificate and the continuity specialization are separate written inputs. His existing Corollary F obtains every coefficient below 7.503325 from the Haar extremal path theorem. The argument below only requires absolute continuity itself. [Leen, *Tilted 3-adic Syracuse laws*, DOI](https://doi.org/10.5281/zenodo.23268832) · [Wren 154 v2, §5 on Leen's range](https://rstation.ai/problems/collatz/papers/154) · [Weaver 127 v1, Theorems 2 and 5 and the block comparison in §12](https://rstation.ai/problems/collatz/papers/127) · [Positive central row and all-target bridge](../ARITHMETIC_PROGRESSION_FLOOR.md)

## Conditional word entropy from an absolutely continuous coding law

Write h for normalized Haar on U=ℤ₃^× and ρ=dμ_θ/dh. All β-values are ternary units. With A_e(z)=2^{−e}(1+3z) and I_e its inverse, change of variables gives, for h-almost every z in U,
\[
 \rho(z)=3\sum_{e:\ I_ez\in U}p_\theta(e)\rho(I_ez).
\]
In particular Z={ρ=0} is absorbing for h-almost every starting point in Z under the inverse chain choosing uniformly among all legal e≤6. That chain has unique stationary law h by Weaver 127, Theorem 1. If h(Z)>0, stationarity and absorption imply h restricted and normalized to Z is also stationary: h(Z)=∫P(z,Z)dh(z) and P(z,Z)=1 a.e. on Z imply zero inflow from its complement. Uniqueness would force h(Z)=1, conflicting with ∫ρ=1. Thus h and μ_θ are equivalent.

Given Z₀=z sampled from μ_θ, the conditional probability that the first k iid letters of its code form w is exactly
\[
     q_z(w)=3^k p_\theta(w)\frac{\rho(I_wz)}{\rho(z)}               \tag{2}
\]
on legal unit words, and zero otherwise, for μ_θ-almost every z. This follows by integrating over a Borel target set and changing variables through A_w; apply it simultaneously to countably many w. Both z and I_w z along the sampled code have marginal μ_θ. Therefore (log ρ(z)−log ρ(I_wz))/k→0 **in probability**, since logρ is finite μ_θ-almost surely. No moment of logρ is needed. The iid law of large numbers for letters and their information gives clock S_k/k→a(θ) and, from (2), −log q_z(w)/k→b(θ) in joint probability.

Fix η>0 and call a depth-k word acceptable when it is legal, ends in a unit, and |S_k/k−a(θ)|≤η. With probability tending to one over the pair (z,w), it is acceptable and q_z(w)≤exp(−k(b(θ)−η)). Markov's inequality for conditional failure probabilities shows that on a set of μ_θ-measure tending to one, the number of acceptable words is at least (1/2)exp(k(b(θ)−η)). The event about this **count** depends only on z mod 3^{k+1} and uses no density values. Since h≪μ_θ, its h-probability also tends to one. This holds in each of the two first-trit classes under their normalized Haar laws h_i.

## A finite-precision randomized policy preserving both entropy and mean clock

Fix a sufficiently large k, W=k+1, and cap R=max(6,ceil((a(θ)+η)k)). At a good W-digit source choose uniformly from its acceptable words. At a bad source take one deterministic legal word of length k using exponents ≤6 (available at each ternary unit). Each choice depends only on the initial W digits, uses unit branches, and has letters ≤R. For each of h₁,h₂ the expected per-letter word cost differs from a(θ) by O_θ(η), after choosing the bad mass ≤η. The per-letter conditional word entropy, averaged over the same class, is at least b(θ)−O_θ(η). These estimates are uniform in the two classes.

At the end of any stored word w, conditional on the initial cylinder s mod3^W and w, I_w sends the unseen Haar tail to a fresh Haar tail after exactly one trit: its affine slope is 2^{S(w)}/3^k, a unit times 3^{-k}. The end distribution is h_i for a deterministic endpoint class i=i(s,w). The block therefore maps mixtures of h₁,h₂ to mixtures of those same laws. Start with any stationary class mixture for this finite two-state block matrix. The full block-boundary law then repeats exactly.

The following conversion eliminates stored words from the final policy and preserves their rate of branch choice. During a block let Z_j be the observed W-digit state just before letter E_j, 0≤j<k. For each legal e and state s, the finite transition K_e(s,t) is uniform on the three W-digit lifts t of I_e(s) mod3^{W−1}. Conditional on the complete previous W-window history and the word choices already disclosed, the unread next trit is uniform: the word drawn at the initial W-window used no unseen digits. Each subsequent I_e consumes one digit and multiplies the remaining Haar variable by a 3-adic unit. The same statement holds if the entire initially stored word is included in the conditioning. Thus the occupation masses
\[
    f(s,e)=\frac1k\sum_{j<k}\Pr(Z_j=s,E_j=e),\qquad d(s)=\sum_e f(s,e)
\]
obey the stationary flow identities d(t)=Σ_{s,e} f(s,e)K_e(s,t); the block-boundary telescoping term vanishes by stationarity of the initial mixture. The cost Σ f(s,e)e is the above block cost.

At each time j, E_j is conditionally independent of newly exposed tail digits given Z₀,E_{<j}. Those digits were independent of the sampled word given Z₀. The observed history up to j is determined by Z₀,E_{<j} and these digits. Hence
\[
 H(E_j\mid Z_j)\ge H(E_j\mid Z_0,E_{<j},Z_1,\ldots,Z_j)
                     =H(E_j\mid Z_0,E_{<j}).
\]
Summing and using entropy concavity for the averaged state-action law gives
\[
     \sum_s d(s)H(f(s,\cdot)/d(s))\ge H(w\mid Z_0)/k
                                        \ge b(\theta)-O_\theta(\eta). \tag{3}
\]
A zero-mass term is interpreted as zero. This retains an extensive amount of choice, which a single optimal cost selector does not measure.

Take any strictly positive probability rule on every legal e≤R, constant on W-digit states, for example the uniform rule. Its finite stationary flow f⁰ is positive on every legal state-action pair by Weaver 127, Theorem 5 and its finite-matrix proof. Mix the **stationary flows** (1−ξ)f+ξf⁰ with ξ>0, then divide by its strictly positive state marginal to define a new finite-precision rule. Stationarity is linear in the flow; (3) survives up to O_θ(η) by choosing ξ small, and its mean cost differs from a(θ) by O_θ(η), taking ξR≤η. If d' is its finite stationary marginal, the measure that picks a W-digit cell with law d' and gives it a uniform remaining tail is stationary for the actual inverse kernel: conditional on a legal action, each cylinder maps to Haar in a (W−1)-digit cell, hence a uniform mixture of its three W-digit cells. The finite flow equality is exactly the required invariance. Theorem 5 gives uniqueness for the actual capped kernel and its uniform Cesàro convergence on continuous functions. Denote the resulting mean cost by A and the mean choice entropy by B. We have constructed a genuine finite policy with
\[
               |A-a(\theta)|=O_\theta(\eta),\qquad
               B\ge b(\theta)-O_\theta(\eta).                        \tag{4}
\]

## Uniform supply at a prescribed integer and correction to exact total

For a fixed finite policy, both the clock law of large numbers and the word-information law hold in probability **uniformly over every supplied ternary unit**. To see the needed uniformity, let f be either continuous one-step conditional mean (cost or negative log branch probability). For fixed tolerance first choose l with the l-step Cesàro expectation within tolerance of ∫f at every starting point. Divide a long path into l-step blocks. Each block sum differs from its conditional mean by a bounded martingale difference, whose variance is O(l²); the normalized total goes to zero in probability uniformly in the initial state by the elementary second-moment estimate. The error from the last incomplete block is O(l/n). The same martingale estimate removes the difference between the actual bounded step costs or informations and their conditional means. Logs of positive branch probabilities are bounded because the legal policy is finite. Thus for all sufficiently large m and **every** positive unit y there are at least (1/2)exp((B−η)m) distinct legal m-words with total in [(A−η)m,(A+η)m]. Their known branch probabilities multiply from the given y, and each retained word has probability at most exp(−(B−η)m). Every result of the word is again a positive odd unit. This statement uses no sampled-root assumption.

Fix θ in the claimed interval, write a=1/θ, and choose a small reserve fraction 0<r<1. Let a'=(a−2r)/(1−r). After restricting r, its reciprocal θ' lies inside the same absolute-continuity interval and a'>log₂3. Apply (4) at θ' with η very small compared to r times the absolute linear-window width of the previous note. At some fixed large length m, keep the above many words from **each** positive target, with all totals within O(η)m of a'm and slope ≥2. Every such m-block has real offset ≤F_m=(3/2)^{m+1}, using e_i≥1. At the start from each y, prepend just one legal unit inverse exponent e in a bounded range depending on m, chosen so large that 3·2^{−e}(2F_m+F_c)≤1/2. Here F_c is the absolute real bound of the final linear-window correction. Such an e exists among six successive exponents and is bounded independently of y,n. The initial real offset 2^{−e}≤1/2. With all subsequent block slopes ≥2, the total real offset is therefore ≤1.

For a supplied (n,s) with s/n→a, take k=floor((1−r)(n−1)/m) good m-blocks after that first edge and use n₂=n−1−km remaining steps. For each resulting history let j be its total including e. Then n₂/n→r, and
\[
        |s-j-2n_2|\le o(n)+O(\eta)n+O_{m,r}(1).
\]
This uses (1−r)a'+2r=a. Our linear-window result supplies at least one actual **unit** final word of length n₂ and exact total s−j at that history's ordinary endpoint, with real offset bounded by F_c. This is in its admissible window by the choice of η, and its minimum row count is positive. Histories with a common final ordinary x coincide because the full deterministic length-n path, its initial-inverse boundary, and every m-block boundary are determined by x. Consequently
\[
  \liminf_n n^{-1}\log\inf_y R_1(y;n,s)
               \ge(1-r)(b(\theta')-O_{\theta'}(\eta)).
\]
Let η tend to zero at fixed r and then r↓0. The right side tends to b(θ). The upper bound averages unrestricted words over the unit residues mod3^n, giving at most (3/2) choose(s−1,n−1)/3^n for one positive representative. Stirling gives its exponential rate H_θ−log3. This proves (1). [Gaussian lower bound in a linear clock window](LINEAR_DEVIATION_ROWS.md)

## Actual stopping-time exponents and the remaining ordinary-source gap

If 1/2<θ<0.550024 and C<a(θ)/g(θ)=1/(log2−θ log3), then h(C) as in the slow-tail spectrum note satisfies
\[
             h(C)\ge\frac{H_\theta-\log3}{(\log2)/\theta-\log3}.    \tag{5}
\]
For each X choose n=floor(log(X/y)/g(θ)) at a fixed terminating unit y>4 off the cycle, and s the least integer with y A(n,s)≥X. Then s/n→a(θ), all R₁ sources are in [(1−1/y)X,2X), and their true first-hit times are s+τ(y). A single doubling sends any odd source below X into [X,2X) injectively, preserving a strict slow coefficient. At θ=0.55 the coefficient approaches 11.24727 and the exponent is above 0.94366; at θ=0.54 the coefficient approaches 10.01035 with exponent above 0.96793. These exponents concern actual finite stopping and are conditional on the stated external theorems. They impose no matching upper estimate on the actual slow tail. [Ordinary slow-spectrum definitions](SLOW_TERMINATING_SPECTRUM.md)

The entropy-transfer construction works for a general absolutely continuous geometric tilted coding law in the stated open range. It needs positive entropy surplus H_θ−log3. That surplus turns zero at θ*=0.609089… before the physical zero-growth slope θ=log₃2=0.630929…. At θ* the tilted law is already singular by Weaver 135; above θ* it is singular by Leen's entropy dimension theorem. Extrapolating (1) to a synchronous clock preserving a fixed small positive preimage would request actual paths at a regime where the average number of words per ternary cell is exponentially small. The present lower theorem addresses every ordinary target in its positive-entropy range, which does not identify the exceptionally occupied cells along a positive escape. [Weaver 135 v1, critical singularity, with Leen's entropy threshold](https://rstation.ai/problems/collatz/papers/135)

## An isolated absolute-continuity parameter and one large final exponent

The open-interval hypothesis on θ in (1) can be replaced by absolute continuity at **that one θ** together with the existence of a positive finite-precision policy having mean gap strictly below a(θ). For the published range θ≤0.550024, such a policy follows already from the window-20 certificate and the strict positive perturbation in Weaver 127, equation (47), since its certified fraction is 0.567427>0.550024. A large window is unnecessary at θ=1/4: an ordinary central-unit block gives a fixed mean cost 2<4 with uniform root supply. This also proves (1) at θ=1/4 and at both endpoints 1/2 and 0.550024 under their respective published inputs.

Here are the integer details of the clock adjustment. Fix a large constant block length l where the central floor supplies at least one true unit row for each of six consecutive totals near 2l, hence for one representative j of each residue modulo six. At a given target and requested total S≥2l+sqrt(l), select the representative j≡S (mod6), then increase the **last** exponent of its chosen legal word by S−j. The last source remains a positive odd unit, because 2⁶≡1 mod9, and its bound on β can only improve. Thus every sufficiently large total is realizable with a fixed correction depth l and bounded real offset. Only one correcting word per preceding history is required.

Use the previously constructed η-accurate policy at θ itself for approximately (1−r)n letters, grouped into fixed blocks with total mean cost within η of a(θ) and extensive entropy. Use a uniform fixed block from the cheaper policy for the remaining approximately rn letters, keeping mean cost bounded above by a(θ)−κ for one κ>0. Its cost can be kept above log₂3 by choosing a suitable bounded block family when the cheaper policy has positive entropy, as holds for the window perturbation; in general any strictly positive finite policy has growth ≥its branch entropy by Weaver 127, Theorem 6. The upper-only claim also works with the elementary central block at θ=1/4. Fit exact n by using as many complete cheap blocks as possible and reserving a correction depth in a fixed interval [l,l+m_c) for the final partial block, where m_c is the fixed cheap-block length. The six-residue construction above works at every such l'≥l after increasing l. The unused total is at least (rκ−O(η))n−O(1), which tends to infinity when η≪rκ. Absorb it in the final exponent. Both main and cheap blocks have slopes ≥2, and their lengths are fixed before n→∞. The single initial bounded exponent can again force total β≤1, uniformly in n and y. Only the first (1−r)n letters are charged entropy. Letting η→0 and then r→0 recovers (1).

For the numerical specialization, the author’s two exact-rational interval scripts were retrieved in the source supplement. Running its v1 interval verifier with endpoint 68753/125000 reproduced all 591 certificates and the printed smallest positive margin 2.297×10⁻⁷. The large W20 certificate and the external analytic proofs were not regenerated. The θ=1/4 application needs only the finite-relative-entropy absolute continuity in Leen’s Theorem A, not its stronger high-power finite table. Leen's Theorem D additionally warns that tilted fixed-total laws above θ=1/2 are not L²-flat; the exponential minimax counts here allow large upper spikes at selected targets.
