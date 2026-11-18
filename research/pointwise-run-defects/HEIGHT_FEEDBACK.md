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
