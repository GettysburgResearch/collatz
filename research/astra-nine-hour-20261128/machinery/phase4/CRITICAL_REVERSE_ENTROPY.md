# The open optimal inverse-slope endpoint is equivalent to vanishing reverse entropy per ternary digit

Let θ* be the unique positive entropy-critical geometric parameter with H_{θ*}=log3, let a*=1/θ*, t*=−log(1−θ*), and let μ* be its ternary Syracuse law. For C_n(z), the minimum total exponent over all unit inverse words of odd length n from z, write Θ∞ for Leen's Haar-almost-sure optimal long-run odd fraction, L=1/Θ∞. Let h denote normalized unit Haar. We use h_{n+1}, μ*_{n+1} for their distributions on unit residues modulo 3^{n+1}. Define the **reverse relative entropy**
\[
       D_n^-=D(h_{n+1}\Vert\mu_{*,n+1}).
\]
Let I_*(a)=sup_{λ≥0}(λa−log E exp(λE)), the upper-tail Cramér rate for a positive geometric E of mean a*. It is zero at a*, positive for a>a*. Then
\[
  0\le I_*(L)\le \liminf_n D_n^-/n
     \le\limsup_n D_n^-/n\le t_*(L-a_*).                            \tag{1}
\]
In particular the following are equivalent:

1. Θ∞=θ*.
2. liminf D_n^-/n=0.
3. D_n^-=o(n).
4. Every unit cylinder has μ*_{n+1}(z)≥h_{n+1}(z) exp(−o(n)), with the error uniform in the cylinder.

Weaver 135 and Leen give D(μ*_{n+1}‖h_{n+1})=o(n) in the **other direction** (full entropy dimension), with a lower bound on the scale sqrt(n) and total variation tending to one. Weaver 150, §7, already explicitly asks whether the reverse entropy is o(n), and gives a logarithmic lower bound. The additions here are the quantitative two-sided comparison with the optimal cost, the equivalences above, and the uniform worst-cell formulation; the reverse-entropy research target itself is prior work. No comparison in the direction needed for (2) is presently established. [Leen, *Tilted 3-adic Syracuse laws*, Theorem C](https://doi.org/10.5281/zenodo.23268832) · [Weaver 135 v1, Theorem 1](https://rstation.ai/problems/collatz/papers/135) · [Weaver 150 v2, finite-window gap and minimum-cost estimates](https://rstation.ai/problems/collatz/papers/150)

## Uniform worst-target minimum and an infinite route from each target

One has the stronger global characterization
\[
    \lim_n\sup_{z\in U} C_n(z)/n=L,
       \qquad C_n/n\longrightarrow L\quad\text{in unit Haar probability}.
                                                                    \tag{2}
\]
The supremum is unchanged if restricted to actual positive odd units, since C_n is constant on each unit class mod3^{n+1}. Weaver 127, Theorem 11, proves max_i∫C_n dh_i/n→L for i=1,2. Their conditional means differ by at most an absolute constant: from source trit i pick, as a function of its second trit, one exponent e≤6 taking the source to any prescribed unit trit j. Each two-trit cylinder maps affinely to that trit with a Haar tail. Hence ∫C_{n+1} dh_i≤6+∫C_n dh_j. Dropping the last positive edge gives C_{n+1}≥1+C_n, so both means divided by n tend to L.

For each ε>0 the finite-window optimum and its positive finite-policy perturbation (Weaver 127, Theorems 9,11) give a strictly positive finite kernel with mean gap A≤L+ε. Indeed use a fixed-window bias with θ<Θ∞ close to Θ∞ and choose its noise level sufficiently small in (47). Conversely A≥L for every such policy: its finite stationary density is equivalent to h and its cost average equals A, and a Haar-typical source has maximal lower odd fraction Θ∞. The uniform original-state LLN proved in the tilted transfer note gives, for each fixed tolerance and all large n, from **every** z at least one real legal word with total in n[A−ε,A+ε]. Thus sup_z C_n/n≤L+2ε eventually. The limiting mean gives the matching lower bound and convergence in Haar probability: 0≤sup C_n/n−C_n/n has mean tending to zero. [Weaver 127 v1, equations (47), (51)–(57)](https://rstation.ai/problems/collatz/papers/127) · [Uniform supplied-state concentration](TILTED_ENTROPY_TRANSFER.md)

Every prescribed z also has an infinite legal inverse word of asymptotic mean cost exactly L. Select ε_j↓0 and, for each j, one finite block length m_j and bound R_j so from every state a word of length m_j, each exponent ≤R_j, has mean within 2ε_j of L. Choose a schedule of finitely many repetitions per stage, fixing all m_j,R_j beforehand, with cumulative previous depth N_{j−1}≥j m_j R_j for j≥2. This is possible by enlarging the number of blocks at stage j−1 to cover the next precision. In a complete block the cost error is ≤2ε_j m_j, and any incomplete last block costs at most R_j m_j=o(N_{j−1}). Weighted averaging gives the limit. From an ordinary positive odd unit the route stays positive at every step. This asserts existence of a route with mean L at each point. Some exceptional points have cheaper routes: −1 has C_n(−1)=n via the all-one word.

## The two directions of relative entropy

Set W_n(z)=μ*_{n+1}(z)/h_{n+1}(z), lifted to U. At the critical parameter every length-n word w satisfies
\[
                3^np_*(w)=\exp[-t_*(S(w)-a_*n)].                   \tag{3}
\]
For a supplied unit z, decompose the digit cylinder at n+1 into its length-n coding prefixes. A contributing word must be a legal unit word there, and its remaining first-trit mass is μ*(I_wz mod3), one of two fixed positive numbers. The normalizing h_{n+1}(z)=1/(2·3^n) gives
\[
    W_n(z)=2\sum_{w\ {\rm legal\ at}\ z}3^n p_*(w)
                           \mu_*(I_wz\bmod3).                        \tag{4}
\]
Both trit probabilities are positive since the geometric parity probabilities are positive. Keeping a minimum-cost word and using (3) proves W_n(z)≥c exp(−t_*(C_n(z)−a*n)). Equations (2) and (4) yield the uniform upper bound on −log W_n/n in (1), the integral upper bound, and implication (1)⇒(4) in the numbered list.

For the lower bound in (1), the case L=a* follows from nonnegativity. Otherwise fix u strictly between a* and L. On E_n={C_n≥un}, whose h-probability tends to one by (2), all the nonnegative prefixes of (4) have S(w)≥un. Integration there is at most the unconditional iid probability of this clock tail, since the integral is the μ* probability of E_n and its every represented code has that property. Cramér's bound gives ∫_{E_n}W_n dh≤exp(−n I_*(u)). For any v<I_*(u), Markov's inequality gives W_n≤exp(−nv) for h-almost all points of E_n except a set of mass tending to zero. The negative contribution to ∫−log W_n is bounded uniformly, since ∫log⁺W_n≤∫W_n=1. Hence liminf D_n^-/n≥v. Let v↑I_*(u), then u↑L. This also proves (2)⇒(1) in the numbered list because I_*(L)=0 exactly at L=a*, already known as a lower bound for L from the entropy ceiling. The remaining implications are immediate.

The unresolved analytic question is whether the critical law can be exponentially thin on a set of unit Haar mass bounded away from zero. If L>a*, the same argument shows it is exponentially thin on a set of Haar mass tending to one. If L=a*, (4) and (2) exclude exponential thinning even at the worst unit cell. The extreme alternative is compatible with the already established singularity of μ* until the direction of entropy in (1) is controlled.

## Two obstructions to upgrading positive entropy dimension to a cheap path

The cost C_n fails a uniform bounded-difference condition in a single input trit. In the ternary integers −1 and −7=−1−2·3 differ only in the coefficient of 3¹, which is 2 for −1 and 0 for −7. Their other ternary digits agree. The all-one word gives C_n(−1)=n. Every legal inverse unit word from −7 stays negative, and no vertex is −1: I_e(v)=−1 with v an odd integer requires e=1 and v=−1. Hence all its absolute values are at least 5. The identity 2^e|v|=3|x|−1≥(14/5)|x| gives C_n(−7)≥n log₂(14/5)−log₂(7/5). Both values of C_n are also attained at positive odd representatives of the corresponding classes modulo 3^{n+1}. The worst one-trit change is therefore linear in n even on physically represented cells. This does not preclude Haar concentration with rare large influences.

A universal dense-set steering assertion fails as well. Let B_n comprise the unit residues mod3^n whose standard representatives belong to [3^n/4,3^n/4+3^n exp(−sqrt(n))]. Then h(B_n) is comparable to exp(−sqrt(n)). Fix ξ>0. For a Haar unit root z, the probability that **any** legal inverse word of total ≤(log₂3−ξ)n can end in B_n tends to zero exponentially in sqrt(n), up to a polynomial factor. Indeed fix word length r and total S within this bound and let Z represent z mod3^{n+r}. At depth r an endpoint has, as a phase on the real unit circle,
\[
     (x\bmod3^n)/3^n=
      \{2^S Z/3^{n+r}-C_w/3^{n+r}\},\qquad C_w=2^S\beta_w.
\]
All r,S words share the first phase. Since all letters are positive, β_w≤(3/2)^r (sum the geometric series of its summands), so the correction is at most 2^S/3^n≤exp(−ξ(log2)n). The initial phase is uniform on the unit grid of denominator 3^{n+r} since 2^S permutes those residues. Its chance to lie within the enlarged real interval is O(exp(−sqrt(n))+exp(−ξ(log2)n)). Union over O(n²) possible r,S pays no word-count factor. In particular arbitrary sets of Haar density exp(−o(n)) can be inaccessible at **all** sublinear costs from almost every root. Any successful steering argument needs additional dispersion of the actual cheap-address cells.

The two obstructions use exact arithmetic. They leave open an exponential lower-deviation bound for C_n about its Haar mean. Such a bound, if L>a*, would contradict the already known forward-entropy result: μ* assigns probability tending to one to cells having a word of cost ≤(a*+ε)n by the iid law of large numbers, while D(μ*‖h)=o(n) forces the Haar mass of those cells to be exp(−o(n)) by the binary data-processing inequality. The special dispersion or concentration statement needed here does not follow from the general bounded-difference or dense-set assumptions just tested.
