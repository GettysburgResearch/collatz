# Conditional bit biases inside an exact ordinary future record

**PROPOSED written deduction.** Fix one retained good fiber S from the [ordered projection](https://github.com/GettysburgResearch/collatz/blob/6eb986b0ce0b1836a356474d25d709ed4e948b67/research/ayh-resource-reset-20261124/two-class-descent/ADAPTIVE_PAIRED_PROJECTION.md) and sample an actual source uniformly in S. Its complete ordered future record is given. Expose its source residue from least to most significant bit, up to any precision ℓ with 2^ℓ≤F. If π_i is the conditional probability of a one at bit i after the record and the preceding bits are known, then for every t≥0,

    P_S { sum_{i<ℓ} (π_i−1/2)^2 > log K + 2t } ≤ exp(−t),
    K=J(L+1).

Here |S|≥F/J and diam S≤LF. In the polynomial regime log K=O(log(h+2)), so with exceptional probability at most (h+2)^(−A), the realized sum is O_A(log(h+2)). For instance, the number of exposed positions with bias greater than a fixed ε in absolute value is at most ε^(−2) times this bound. An odd-slope arm's next parity at a known common-source prefix is the next source bit or its complement. The same absolute bias statement therefore applies to that arm.

**Predictable blocks.** At each revealed prefix choose the length of the next block, using only that prefix and the fixed record, without exceeding the remaining precision. Write p_i for the actual conditional law of that block and q_i for the uniform law on binary strings of its chosen length. In the displayed tail bound the sum of squared bit biases may be replaced by

    sum_i TV(p_i,q_i)^2,      TV(p,q)=(1/2) sum_x |p(x)−q(x)|.

The rule may stop early at a prefix-dependent time. It may also omit disjoint intervening blocks from the sum: expose those gaps under the same rule and drop their nonnegative contributions. Zero-length stopped blocks are deterministic. The assertion is for any one such predictable policy; different records may choose different policies.

**Proof.** Let P be the projected fiber law on the 2^ℓ complete words, and Q uniform. Each residue occurs at most 1+LF/2^ℓ times in S. Hence P(x)/Q(x)≤J(2^ℓ/F+L)≤K. The same bound holds for every positive-probability stopped transcript, since the corresponding ratio is an average of the full-word likelihood over its Q-completions. A transcript thus requires no lower bound on the probability of the particular prefix under P.

On each reached history define the Hellinger affinity ρ_i=sum_x sqrt(p_i(x) q_i(x)). It lies in (0,1]. For a block X_i drawn under p_i, the conditional expectation of sqrt(q_i(X_i)/p_i(X_i)) is ρ_i. Terms with p_i(x)=0 contribute zero to the affinity and are never sampled; no ratio on those branches is required. The product of these factors divided by their conditional affinities is consequently a nonnegative mean-one martingale under P. At a bounded block stopping time τ its value is

    Z_τ = exp(sum_{i≤τ} −log ρ_i) / sqrt(P(transcript)/Q(transcript)).

Indeed the block likelihoods telescope because the length and stopping rules are functions of the already observed prefix under both laws. There are at most ℓ nonempty blocks, so stopping preserves mean one. The pointwise cap then gives E_P exp(sum −log ρ_i)≤sqrt K. By Cauchy–Schwarz applied to the product of the difference and the sum of square roots, TV(p_i,q_i)^2≤1−ρ_i²≤−2 log ρ_i. Markov's inequality proves the stated tail. Extending a stopped rule to the precision limit also makes the same bound simultaneous over all partial sums of that fixed exposure, by their monotonicity.

For comparison, the relative-entropy chain rule and Pinsker's inequality in natural logarithms give the expectation estimate E_P sum TV(p_i,q_i)^2≤(1/2)D(P_transcript||Q_transcript)≤(1/2)log K. The Hellinger argument supplies the pathwise exponential tail above. Both estimates average over any mixture of retained records with their actual weights. Returning to all original sources adds the projection discard; within a further conditioning event of mass w, an absolute exceptional probability must be divided by w.

These are laws for bits in the **past** of the retained endpoints. They allow conditional bias at selected individual clocks and dependence between different arms. In particular, a cumulative squared bias of order log h is compatible with survival of a one-dimensional walk to time h. No new random bits or conditional transition law after the fixed record clock follow.
