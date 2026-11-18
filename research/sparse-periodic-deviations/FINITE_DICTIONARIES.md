# Bounded dictionaries of repeated parity words on an ordinary divergent orbit

**PROPOSED.** Write T for the shortcut Collatz map and let x be a positive integer with a non-eventually-periodic orbit. Fix a finite list of nonempty binary words and a positive integer k. Consider any sufficiently late starting position t and any prefix of its actual parity sequence of the form

    w_0^{h_0} w_1^{h_1} ... w_(k−1)^{h_(k−1)},       h_i ≥ 1,

with words in the list. Its elapsed shortcut time satisfies, for every fixed ε>0,

    Σ_i |w_i| h_i ≤ (1+ε) log_2(T^t x).                         (1)

The cutoff may depend on the orbit, list, k and ε. The lengths, weights and directions of drift of the words may differ. In particular a repetition of any prescribed contracting word can be followed immediately by repetitions of an expanding word, and conversely. Consecutive words may even coincide. The assumption on the orbit handles contracting words whose signed fixed points are themselves positive cycles.

Let C_L(N) be the minimum number of powers of words of lengths at most L whose concatenation equals the first N parities of the orbit. For each fixed L,

    C_L(N) / log N → ∞.                                          (2)

This concerns the shortest parsing separately at each N. Consequently every divergent trajectory changes its aligned length-L parity block more than logarithmically often, for every alignment and fixed L. The ordinary universal convergence question is open.

## Changing signed fixed points

For a word w write its formal endpoint as (Px+C)/Q with P=3^wt(w), Q=2^|w|. Its rational fixed point c=C/(Q−P) exists and has odd denominator. Take one positive odd integer d clearing all these denominators. At the start of run i let x_i be the ordinary value, let y_i=d(x_i−c_i), and put m_i=(P_i/Q_i)^{h_i}. The end of this run in its own chart is m_i y_i, an integer. Thus Q_i^{h_i} divides y_i. At each transition before the final run,

    y_(i+1) = m_i y_i + b_i,    b_i=d(c_i−c_(i+1)).

A non-eventually-periodic ordinary orbit consists of distinct positive integers. Every value in its tail tends to infinity, so all the y_i are positive and tend uniformly to infinity as t tends to infinity. For one run the divisibility proves (1), since y_0 is within a fixed multiplicative factor of x_0.

## The integer product estimate

For k≥2, suppose (1) fails along infinitely many t for a fixed ε>0. By reducing ε slightly, write the offending inequality with y_0 in place of x_0. Pass to a subsequence fixing the words and making each internal h_i (1≤i≤k−2) fixed or tending to infinity. Put u_i=y_i/Q_i^{h_i} and B=∏_{i=1}^{k−1}Q_i^{h_i}. Iterating the transitions gives

    B u_(k−1) = X + Σ_(j=0)^(k−2) b_j Z_j,
    X = u_0 ∏_(i=0)^(k−2) P_i^{h_i},
    Z_j = (∏_(i=1)^j Q_i^{h_i})(∏_(i=j+1)^(k−2) P_i^{h_i}).

Group adjacent Z_j terms separated only by fixed internal h_i, replacing each group by a rational coefficient times its first Z_j. The ratios within such a group are fixed. Discard groups with coefficient zero. Between the surviving representative coordinates the differences in their increasing 2-adic valuations tend to infinity, since every intervening boundary contains an unbounded power of two and the P_i are odd. Further, for every j,

    X/Z_j = y_0 ∏_(i=0)^j m_i
          = y_(j+1) ∏_(i=0)^j (1−b_i/y_(i+1)) → ∞.

This uses physical divergence at the finitely many intermediate endpoints, including when an m_i tends to zero. It gives the required separation at the real place even when the different Z_j have comparable real size.

Apply the rational p-adic Subspace Theorem to the integer vector of X and the remaining Z representatives. At infinity and 3 take the coordinate forms. At 2 replace the X coordinate by the grouped sum on the right of the integer identity. The coefficient of X is one and these forms are independent. Every Z is a positive integer supported on 2 and 3; X is u_0 times a power of 3. The product of all form values over these three places is at most u_0/B, which is less than y_0^{-ε'} for a fixed ε'>0 by the offending inequality. If no Z survives, B divides X, hence B divides u_0, which already contradicts this bound.

The vector has height at most a fixed power of y_0. Indeed |w_i|h_i≤log_2 y_i and y_(i+1)≤3^{|w_i|h_i}y_i+|b_i|, for a fixed number k of runs. The Subspace Theorem now forces a fixed nonzero rational linear relation along an infinite subsequence. Its X coefficient must be zero since X/Z_j tends to infinity for every j. Among the remaining terms having nonzero coefficient, the first eventually has uniquely smallest 2-adic valuation. Their sum cannot vanish. This proves (1). The integer-vector theorem and its normalization are given in the [single-template proof](PROOF.md).

## From fixed budgets to arbitrary parsings

For any fixed k, (1) with ε=1 also applies to at most k runs, by taking the maximum of the finitely many cutoffs. Starting late at height z, a group of at most k runs therefore lasts at most 2 log_2 z steps. Each shortcut step maps a positive integer v to at most 2v. The end of the group has log-height at most 3 log_2 z. These bounds are independent of k once its cutoff is reached.

Choose a sufficiently late fixed position t_0 beyond that cutoff. Cut an arbitrary parsing of the first N bits at t_0. If the cut splits a word power, its remaining suffix is one partial word of length <L followed by a whole power, so the suffix admits a parsing with at most C+1 runs of words of length ≤L when the original had C runs. Group this suffix into batches of at most k runs. For g=ceil((C+1)/k) batches their times sum to at most (3^g−1) log_2(T^{t_0}x). Hence liminf C_L(N)/log N ≥ k/log 3 for each fixed k. This proves (2). All logs in the final liminf are natural.

The argument gives no effective global cutoff or positive frequency of switches. In particular it allows a hypothetical divergent parity sequence with a power-law number of short-word runs.
