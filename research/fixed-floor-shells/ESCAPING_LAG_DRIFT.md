# An escaping component forces recurrent large clock discrepancies on dyadic siblings

**Proposed, source-qualified.** Write T for the shortcut map. Suppose C is the merger component of a positive escaping orbit and δ its all-integer natural density. This density exists because C is invariant, and is positive by the supplied-unit predecessor-density theorem after advancing to an odd ternary unit on the spine. There is an absolute constant c>0 such that the set B of n for which the two starts 2n and 2n+1 never meet with clock difference at most cδ√(log₂ n) satisfies

    liminf_(X→∞) (1/log log X) Σ_(n≤X, n∈B) 1/n ≳ δ.

In particular any fixed allowable clock difference gives this lower bound, as does any allowance o(√log n). An upper bound o(log log X) for one such allowance would exclude every escaping component. The proof uses an integer time phase on a nonperiodic component. It does not exclude an additional periodic orbit from that weaker upper bound. [Positive unit predecessor density](https://rstation.ai/problems/collatz/papers/12/v1) · [Natural densities of invariant sets and terminal-clock law](https://doi.org/10.5281/zenodo.23252395)

Choose a forward spine y_j=T^j(y₀) in C and set κ(x)=j−a whenever T^a(x)=y_j. The lack of a repetition on the spine makes the definition consistent and κ(Tx)=κ(x)+1. If m(x) is the global minimum, attained first at shortcut time τ*(x), then throughout C

    κ(x) = κ(m(x)) − τ*(x).

Leen's terminal Brownian theorem gives τ*(x)/log x→μ=2/log(4/3) in probability and tightness of m(x) under uniform sources. Both hold on dyadic octaves by counting exceptional starts up to twice the cutoff. For m(x)≤R the phase term ranges over finitely many values on C. It follows that for every fixed η>0 the fraction of octave starts in C violating |κ(x)+μ log x|≤η log x tends to zero. This argument uses no absolute bound on the phase of an arbitrary small-minimum basin.

Take u uniform on [1,2) and n_i=floor(2^i u). At each depth i this is uniform on the positive octave [2^i,2^(i+1)), and n_(i+1) is either 2n_i or 2n_i+1 with an independent fair digit. An even observed edge always changes phase by −1 if its parent is in C, because T(2n_i)=n_i. For an odd observed edge, an equal-clock merger of 2n_i with 2n_i+1 gives precisely the same change. A merger with lag at most D gives a phase change differing from −1 by at most D. Every one of these successful edges preserves membership in C in both directions.

The probability that a given observed odd edge does not have an eventual equal-clock merger is O(i^(−1/2)), with an absolute constant. Indeed Leen's adjacent-pair balanced absorption by i shortcut steps fails on a fraction O(i^(−1/2)) of the full octave of starting positions at scale 2^(i+1), by its periodic discrepancy estimate and the absorption tail. Restricting to the even starting positions 2n_i costs at most two. Failure of an eventual equal-clock merger implies this finite balanced failure. [Leen, *Exact rates in Collatz synchronization*, adjacent absorption law and exact absorption-cylinder discrepancy](https://doi.org/10.5281/zenodo.23268751)

Fix K large, and allow D(n)=cδ√(log₂ n). Let S bound the cumulative phase slack by summing cδ√(i+1) over observed odd edges at depths K≤i<2K lacking an eventual equal-clock merger. Its expectation is O(cδK), with an absolute constant. If every observed edge permits the prescribed lag, and the upper endpoint n_(2K) is in C, the lower endpoint lies there too and

    |κ(n_(2K))−κ(n_K)+K| ≤ S.

The upper endpoint lies in C with probability δ+o(1). The probabilities of an atypical phase in C at either endpoint are o(1). On the remaining such event the two typical endpoint estimates instead give

    |κ(n_(2K))−κ(n_K)+K| ≥ [(μ log 2−1)−3η log 2] K−O(1).

Choose η absolutely small so the coefficient exceeds half of μ log 2−1. Then choose c absolutely small so Markov's inequality bounds the probability that S is even this large by at most δ/4. For every sufficiently large K the probability of at least one observed odd edge with no permitted merger is at least δ/2.

For each octave node n at depth i, the probability of observing its odd edge is 2^(−i−1)≤1/n. The union bound therefore gives Σ_(2^K≤n<2^(2K), n∈B)1/n≥δ/2. Taking K=2^r supplies disjoint height intervals. Their number through X is (log log X)/log 2+O(1), proving the claim.

## Unconditional first-minimum clock discrepancies

Set D_n=τ*(2n+1)−τ*(2n). Independently of how any orbit ends, there is an absolute c>0 such that D_n>c√(log₂ n) on a set with reciprocal mass ≫log log X through X. For every fixed p≥1 and sufficiently large K there is also the block estimate

    Σ_(2^K≤n<2^(2K)) [(D_n)_+]^p / n ≫_p K^((p+1)/2).

These positive clock jumps forbid any merger at lag at most c√(log₂ n) that occurs before or at each arm's respective first global minimum. From such a meeting both first minima would occur on the common suffix, forcing their clock difference to be exactly the meeting lag. This pre-minimum consequence was also obtained independently in the Gaussian-horizon investigation.

Indeed τ*(2n)=τ*(n)+1 exactly. At depth i the probability that D_(n_i)≠0 is O(i^(−1/2)). To see this, use the same equal-clock balanced absorption before i shortcut steps. Unless either first minimum was already reached by i, absorption makes the two first-minimum clocks equal. The probability of either early minimum is O(i^(−2)) by Leen's fixed-interior moderate-deviation estimate for the **capped** clock: choose s=1/2, for which μs log 2>1. A first minimum by i forces the capped passage no later than i, and this early event lies below any fixed Gaussian moderate-deviation level −A√log i eventually. The population estimate transfers to the even and odd samples by restriction of the full octave. [Fixed-interior capped-clock law](https://doi.org/10.5281/zenodo.23252395)

The difference τ*(n_(2K))−τ*(n_K)−K equals the sum of the observed odd-child jumps D_(n_i). By the two terminal-clock laws at the endpoints this difference is at least a fixed positive constant times K with probability 1−o(1), since μ log 2>1. The expectation of the sum of the positive jumps truncated from above at c√(i+1) is O(cK) by the preceding support estimate. Markov's inequality and the disjoint-block argument give the asserted harmonic mass for positive jumps above this threshold. For the moment estimate the expected sum of all positive jumps is ≫K while the expected number of their observed locations is O(√K). Apply Hölder on the disjoint union of the K levels with their observed-edge probabilities, then use 2^(−i−1)≤1/n to obtain the displayed bound. For p=1 the first-moment estimate suffices.
