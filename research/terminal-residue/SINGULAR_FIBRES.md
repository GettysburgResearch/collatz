# Singularity of the real offset at each supplied positive integer

**Proposed, source-qualified.** Let t be any fixed positive odd integer coprime to three. Start the canonical harmonic inverse Syracuse walk at X₀=t, with exponent a_i on its ith reverse edge, and set S_q=a₁+⋯+a_q. The real random variable

    B₀ = Σ_(i≥1) 3^(i−1) 2^(−S_i)

has a law singular to Lebesgue measure. This is the canonical real fibre identified in paper 19, §9.2, including at ordinary periodic and nonperiodic roots. That paper proves singularity and full dimension of the *joint* stationary real–ternary law, and a separate Cesàro description of fibres at the specified integers. A statement about almost every stationary ternary point would leave every ordinary integer untreated. The proof below transfers joint singularity to each of these countably many possible exceptional fibres.

The imported ingredients are joint stationary singularity in paper 19, the source-qualified strong inverse-path word law, and the finite-depth transfer limit. Paper 19's offset and exponents have the same orientation: a prefix ending in x has positive real slope A_w=3^q 2^(−S_q) and t=β_w+A_w x, where β_w is the truncated real series. Its h is our h times 3/2, which leaves the canonical transition unchanged. [Paper 19 v2, §§2, 6 and 9.2](https://rstation.ai/problems/collatz/papers/19/v2) · [Fixed-root strong path law and dependencies](../native-pressure-20261118/ALMOST-SURE.md) · [Every-depth transfer](../native-pressure-20261118/EVERY-DEPTH.md)

## The real and ternary observations on the same ray

Let B_q be the same infinite series formed from a_(q+1),a_(q+2),… with their partial sums reset to zero. The almost-sure drift or the ordinary telescoping identity makes these real sums finite simultaneously. We claim the time-empirical measures of (B_q,X_q in Z₃) on a canonical ray converge weakly almost surely to the joint stationary real–ternary affine law Σ of paper 19. Its description is the law of the *same* offset series in the two completions from one iid geometric exponent sequence. The fair-shortcut construction is equivalent: stopping its initial run of divisions at the first odd affine map gives F_a(x)=(3x+1)/2^a with probabilities 2^(−a). The real series converges almost surely under that law by its positive log drift, and ternary convergence holds for every sequence.

For a finite truncation at d, B_q^[d] is determined by the next d exponents. Moreover X_q≡B_q^[d] modulo 3^d because the remaining ternary multiplier is 3^d times a unit. Thus the time averages for all bounded continuous tests of the truncated real series and the ternary residue are precisely their iid expectations in the limit. Indeed each length-d valuation word has the iid limiting frequency by the strong path law; truncating to finitely many such words costs their complement probability. Here and below a single typical path can be chosen for all d and a countable family of convergence-determining tests.

We justify the infinite real tail when the observation time q varies. Cap a_i at a fixed large K and put u_i=min(a_i,K)log 2−log 3, with |u_i|≤M. The limiting sample mean m₀ is positive. Fix 0<γ<m₀/4. For each k, mark starts of k-blocks whose u-sum is below 2γk. Their limiting fraction p_k is the iid probability, tending to zero by the law of large numbers. If any interval of n≥Ck letters has u-sum less than γn, a fixed positive fraction η of its contained k-blocks must be marked. To verify this, sum over all n−k+1 blocks. The result differs from k times the interval sum by at most 2Mk². If fewer than fraction η were marked, the sum would be at least k(n−k+1)[2γ(1−η)−Mη]. Choose η small and then C large for a contradiction.

For q≤Q and Q large, an interval of length n≥Q beginning at q+1 cannot violate the drift bound. In fact the cumulative centered sums up to j are o(j), uniformly o(Q) for j≤Q and o(n) for j≤2n with n≥Q. Thus every violating interval from q≤Q ends by 2Q. The one-sided maximal inequality for the marked indicators on [1,2Q] bounds the number of starting points admitting a violating interval of length ≥Ck by O_η(1) times the total number of marked starts in that range. For completeness, each such interval contains at least a fixed fraction of marked starts, after adjustment for k at its boundary. A greedy disjoint subcollection in decreasing order of length has triples that cover all the original starting points, giving the stated count. The upper density of these exceptional q is therefore O(p_k).

Off this exceptional set, every length i≥Ck has physical drift (S_(q+i)−S_q)log 2−i log 3≥γi, since the cap only lowered the increments. For d=⌈Ck⌉ this bounds B_q−B_q^[d] by O(exp(−γd)). Approximate any bounded Lipschitz test, then let k grow. The iid truncations converge to the stationary observations, the exceptional fraction tends to zero, and the ternary cylinder error tends to zero. This proves the claimed joint time-empirical law. It also holds when tested in expectation after restriction to any fixed measurable path event, by dominated convergence.

## A real density would force a joint density

If the law of B₀ has any nonzero absolutely continuous part, there is a real Borel set E such that α=Pr(B₀∈E)>0 and Pr(B₀∈E∩D)≤K₀ Leb(D) for every Borel D. Remove a null carrier of the singular part and truncate the density of the remaining part to a finite bound to obtain E.

For every inverse word of length q, B₀=β_w+A_w B_q on that word's cylinder. Hence for a real interval I and a ternary residue cylinder C,

    Pr(B₀∈E, B_q∈I, X_q∈C)
       ≤ K₀ |I| Σ_(w at t ending in C) A_w
       = K₀ |I| L^q 1_C(t).                                           (1)

Each word bound uses only the original law on E; different words' real intervals may overlap. The sum over all legal positive odd inverse words can include terminal nonunits, which only enlarges the bound when C includes them. The transfer proof gives L^q 1_C(t)→(3/2)h(t)λ(C) with λ ternary Haar probability. To see this directly, apply its positive-test liminf to both 1_C and 1−1_C, whose transfers sum to g_q(t)→(3/2)h(t).

Average (1) over q. For open I, the joint empirical law and the open-set lower bound give

    α Σ(I×C) ≤ (3/2) K₀ h(t) |I| λ(C).

Intervals and ternary cylinders generate the product Borel sets. Covering open sets by countably many such rectangles, or using dyadic interval partitions followed by regularity, gives Σ≪Leb×λ. This contradicts the stationary joint singularity theorem. Therefore every supplied ordinary canonical real fibre is purely singular.

## Hausdorff dimension of the canonical fibre

Write d₀=log(4/3). Almost surely log X_q=d₀q+o(q), log(1/p_w)=d₀q+o(q) for the probability p_w of the sampled prefix, and S_q=2q+o(q). Put W=t−B₀. The finite deficit is W_q=t−β_w=A_w X_q. Dividing its telescoping expressions at successive depths gives

    W = W_q ∏_(i>q) (1+1/(3X_i))^(−1).

Indeed t−B_j=A_(w_j)X_j and each additional factor equals 3X_i/(3X_i+1). Thus 0≤W_q−W≤t Σ_(i>q) 1/(3X_i). Fix a small ε>0 and restrict to paths on which for every q≥K the three strong-law errors above are bounded by εq. On these paths W_q−W≪ exp(−(d₀−ε)q). For a fixed total S_q the possible centers W_q lie on a grid of spacing A_w=3^q/2^(S_q)≥exp(−(d₀+ε log 2)q). There are O(q) totals. Each allowed endpoint X_q corresponds to exactly one length-q inverse word, by its deterministic forward trajectory; this remains true for a periodic root at fixed depth. Each such cylinder has probability ≤exp(−(d₀−ε)q). A real interval of length exp(−d₀q) consequently has restricted probability at most exp(−(d₀−O(ε))q). Let K grow, then ε decrease. The same interval-cover argument as for the natural terminal residue proves full lower Hausdorff dimension one for each canonical fibre. Translation between W and B₀ preserves dimension.

[Strong physical and information estimates](../native-pressure-20261118/ALMOST-SURE.md) · [Natural terminal dimension and the separate small-ball estimate](REAL_DIMENSION.md)
