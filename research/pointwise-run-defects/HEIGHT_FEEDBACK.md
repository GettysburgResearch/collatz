# Real decision rules for the parity of one ordinary orbit

**PROPOSED.** Let T(x) be x/2 for even x and (3x+1)/2 for odd x. A positive integer orbit x_j=T^j(n) is eventually periodic if, from some point onwards, its next parity bit is predicted exactly by a fixed real semialgebraic rule using j and finitely many past and present states. Finite internal memory is allowed. A semialgebraic rule uses a fixed finite Boolean combination of real polynomial signs, or equivalently a formula over the real closed field with real constants. In particular any explicit rational-function recurrence of fixed order in the states and time forces eventual periodicity, including nonlinear recurrences.

The polynomial-coefficient linear recurrence case was previously proved for ordinary and odd clocks in [Paper 106](https://rstation.ai/problems/collatz/papers/106/v1). The result here concerns the shortcut clock and allows nonlinear real decision regions. The proof below uses no recurrence zero theorem or holonomicity argument. The integer parity predicate itself is definable using an integer congruence. A relation that allows both branches at each point also exists identically, for example (2x_(j+1)−x_j)(2x_(j+1)−3x_j−1)=0. Neither operation supplies a single-valued real semialgebraic decision rule.

## Entropy and prediction errors

In a more general predictor let g₁(j),…,g_H(j)>0 be arbitrary fixed threshold sequences such that g_l(j+1)/g_l(j)→1. No size restriction on the thresholds is needed in this subsection. A fixed finite-state machine sees the signs of x_j−g_l(j), outputs one predicted bit, and can update its internal state from the signs and the true bit. Write b_j=x_j mod 2 and let e_j be the exclusive-or of b_j and the prediction.

For any infinite simple orbit, each empirical subsequential stationary joint law of (b,e) satisfies

    h₂(b) = h₂(e) = h₂(b,e) ≤ H₂(ε),                              (1)

where ε is the limiting frequency of prediction errors, h₂ denotes entropy rate in bits, and H₂ denotes binary entropy. If on the same time subsequence x_j≤N^A at a fraction tending to δ among 0≤j<N, the [single-orbit entropy bound](FORWARD_ENTROPY.md) gives δ/A≤H₂(ε); if the b marginal is ergodic and δ>0, it gives 1/A≤H₂(ε).

To prove (1), fix a window length m. For each specified m-bit error word the number of compatible true m-words occurring jointly infinitely often is O_H,F((m+1)^(2H)), with the finite-state machine F fixed. The same bound holds with true and error words interchanged. To see this, along infinitely many occurrences of a joint word starting at j→∞ pass to a subsequence where the initial machine state is fixed and all x_j/g_l(j) have extended limits t_l∈[0,+∞]. A simple positive integer orbit satisfies x_j→∞. For i<m, after p ones in the first i letters the affine identity gives

    x_(j+i)/x_j → 3^p/2^i,         g_l(j+i)/g_l(j) → 1.

Only the comparisons of t_l with the at most (m+1)² positive numbers 2^i/3^p for i<m, 0≤p≤i, are needed. There are O((m+1)²) cells per coordinate including all cut points and both ends. For one choice of cells and initial state, simulate the machine with the specified word. All signs are determined except when t_l equals the current cut. For a fixed l this can happen at at most one time on each simulated path, since 2^i/3^p has a unique pair (i,p). Give an undetermined sign any of its three possible values. The resulting tree has at most 3^H leaves, as each such choice exhausts one coordinate. When the errors are supplied the true bit is recovered from prediction and error; when the true bits are supplied the error is recovered in the same way. This proves the two counting bounds.

Every word of positive measure in a limiting empirical law is recurrent in this sense. Both conditional m-block entropies, given the other word, are therefore at most O_F,H(log(2+m)). Divide by m and pass to the stationary entropy rates to get the equalities. The binary maximum-entropy inequality gives the final bound in (1). There is no assumption of mixing, genericity, or a computable convergence rate.

## Exact prediction with polynomially bounded thresholds

Suppose all g_l(j)≤C(j+1)^A for some fixed C,A, and the prediction is eventually always correct. Above this envelope every sign is positive. The machine then runs autonomously once it enters such an excursion. After at most its number of states s, it follows a periodic pattern of length at most s until the excursion ends. Such a pattern cannot last for more than log₂(x+1)+O_s(1) positions on a simple trajectory starting at x. Indeed if two starts separated by p≤s have L equal subsequent parity bits then their nonzero integer difference is divisible by 2^L. Their difference in absolute value is at most (3/2)^p(x+1), allowing a further O_s(1) if the comparison follows the initial transient. The congruence follows by induction on the parity cylinder, whose branch numerator slope is odd.

An excursion starting at time t>0 after a state below the envelope starts at x_t≤C'(t+1)^A. Its length is O(log(t+2)), hence the one-step growth bound T(x)+1≤(3/2)(x+1) keeps every state of the excursion polynomial in t+1. An initial excursion is finite by the same congruence. Thus x_j≤C''(j+1)^B everywhere for some B. On a simple orbit a subsequential empirical law exists, and (1) with δ=1 and any A'>B gives the contradiction 0≥1/A'. This proves periodicity for the general exact predictor under the stated envelope.

## Passage from real semialgebraic rules

For a rule using x_(j-r),…,x_j, refine the finite memory by storing the previous r branch bits. They express each preceding state as a rational affine function of x_j, by inverting that finite word. After substitution and splitting by memory state and sign, each decision and state update is a Boolean combination of membership in finitely many semialgebraic sets of (j,x_j).

For all sufficiently large real j their vertical sections have endpoints on a common finite list of continuous semialgebraic real functions. This is planar semialgebraic cell decomposition. The ordering and membership between endpoints and on endpoint graphs are fixed there. Each endpoint is eventually of constant sign, and each eventually positive one has a leading Puiseux asymptotic a j^c with a>0 and rational c (including a finite nonzero limit). It is therefore polynomially bounded and has unit successive ratio. Nonpositive endpoints can be discarded for positive states. Alternatively these endpoint facts follow directly by taking real roots of each defining polynomial as a polynomial in its second variable and using its finitely many Puiseux branches at infinity. Thus a machine of the preceding kind implements the rule. If x_(j+1) is prescribed by a real semialgebraic function of time and the preceding states, comparison with x_j/2 identifies its parity branch: the two next values are distinct for positive x_j. This proves the stated corollary.

An arbitrary ordinary itinerary always permits exact prediction with the integer parity test. The step from this arithmetic test to a finite real decision rule on that specific itinerary remains unproved.

The same statement applies to rules definable in any fixed polynomially bounded o-minimal expansion of the real ordered field. Planar cell decomposition and eventual monotonicity replace the semialgebraic Puiseux argument. For an eventually positive definable endpoint g, both g and 1/g are polynomially bounded. The definable ratio g(t+1)/g(t) has an extended limit by monotonicity. A limit greater than one would give geometric growth along integers, and a limit less than one would do the same for 1/g, so the limit is one. These are the only additional o-minimal facts used.

Ordinary integrality is essential even for a fixed constant threshold: start at 1/5 and choose the odd affine formula precisely when x≤1. This gives 1/5,4/5,17/10 and then bounded positive rationals. After the first negative binary valuation appears it decreases by exactly one at each step under either affine formula. All subsequent states are distinct. The second chosen branch disagrees with the dyadic parity of 4/5. Hence an ordinary proof cannot keep just the real recurrences and the predictor while discarding dyadic consistency.

## Some thresholds above polynomial scale

There is also a finite-window extension using only elementary approximation of log₃2 by continued fractions. For H≥1 suppose some

    0<β<min(1/3,1/(2H))

and fixed C satisfy for all sufficiently large n and every l

    log⁺ g_l(n) ≤ C n^β,       |log g_l(n+1)−log g_l(n)| ≤ C n^(β−1).

Then exact prediction again forces eventual periodicity. In particular the conclusion covers any finite number of quasipolynomial thresholds exp((log n)^a) with fixed real a>0, as well as a single threshold exp(n^β) for every fixed 0<β<1/3.

For a simple orbit above the envelope exp(C n^β), the same autonomous finite-state excursion estimate gives a length O(log(x_entry+1))=O(n^β) after first crossing. Therefore, globally, log(x_n+1)≤C' n^β eventually. Let K be an arbitrarily large continued-fraction convergent denominator of log₃2. Any two distinct cuts i log 2−p log 3 with 0≤p≤i<K are separated by at least c/K with absolute c>0. For unequal i, use the best-approximation bound ||d log₃2||≥||q_prev log₃2||>1/(K+q_prev) for 0<d<K; equal i is immediate. Choose N of order K^(1/β), with a small enough fixed proportionality constant that x_j<2^K for N≤j≤2N. There are therefore at least N distinct K-bit words starting in this interval.

The true logarithmic height at offset i≤K differs from log x_j+p log 3−i log 2 by at most E_j=Σ_(j≤v<j+K)1/(3x_v). Each globally distinct positive integer in the sum over N≤j≤2N is counted at most K times. Hence Σ_j E_j=O(K log(2N)), using only the harmonic bound for at most 2N+K distinct positive integers. Discard starts with E_j>c/(10K); at most O(K²log N)=o(N) are discarded. Each threshold's log changes by O(K N^(β−1))=o(1/K) throughout each window as β<1/3. Thus in simulating the K bits from a remaining start, the comparisons from log(x_j/g_l(j)) against the cuts are exact except in the disjoint c/(3K)-neighborhoods of the cuts. There can be at most one ambiguous time per threshold along a simulated branch. As before the possible words from these starts number O_F,H(K^(2H)), counting the cells including the cut neighborhoods. This is o(N) by 2Hβ<1, contradicting the distinct-word count. No effectiveness statement about onset is needed.

## A mistake count without a polynomial-height assumption

For a fixed real semialgebraic predictor on any nonperiodic ordinary orbit, the number E(N) of mistakes among the first N decisions satisfies

    E(N)/log N → ∞.

The proof permits fixed residue registers modulo any odd integer: division by two is invertible there, so the true bit updates each such register in finite memory. This strengthens the exact-prediction conclusion even on rapidly growing orbits.

For a contradiction take arbitrarily large N with E(N)≤M log N for fixed M. Reduce to H positive end graphs as above. Their Puiseux expansions give |log g_l(j+1)−log g_l(j)|=O(1/j) (differentiate the convergent Puiseux series). Every excursion above their common polynomial envelope starts at height polynomial in N through time N, apart from the fixed initial state. Within such an excursion, cut at every mistake. On each correct run the finite state supplies at most a bounded preperiod and a bounded period repeated some number of times, with a bounded terminal gap. The whole excursion, including a terminal prefix stopped at N if needed, therefore has a flat power description of width O_F(E(N)+1) and at most E(N)+1 powered pieces. Apply the [simple-segment bound with variable power count](COMPRESSED_DESCENT.md) with an arbitrarily small exponent η. It follows that every such excursion has length at most N^s for any prescribed s>0 once N on the chosen subsequence is large enough. Its entrance log height is O(log N), so max_(j≤N) log(x_j+1)≤N^s for every fixed s>0 eventually along this subsequence.

There is a fixed κ>0 for which distinct cuts i log 2−p log 3, 0≤p≤i<K, are separated by at least c K^(−κ); the nonzero difference is a linear form in the logarithms of 2 and 3. Only a finite irrationality measure is needed. [Rhin's bound and source comparison](../cyclic-shift-distance/README.md)

Take K=floor(N^s) with s>0 fixed small enough that s(κ+1)<1 and 2Hs<1. The preceding height result used with s/2 makes the K-symbol words from all starts j∈[N/3,N/2] pairwise distinct. Remove all windows containing a mistake, costing O(K log N) starts. As in the previous section the total logarithmic distortion over all windows is O(K log N), so at most O(K^(κ+1)log N)=o(N) windows have distortion greater than c K^(−κ)/10. Thresholds drift by O(K/N)=o(K^(−κ)). The disjoint cut-neighborhood argument now gives only O_F,H(K^(2H))=o(N) possible words on the surviving starts, contradicting their number. This argument uses the Subspace Theorem through the cited compression bound. It yields no effective onset or positive lower density of mistakes for an unrestricted escaping orbit.
