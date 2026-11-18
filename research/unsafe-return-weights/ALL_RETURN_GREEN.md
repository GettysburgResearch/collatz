# A Green bound across all actual unsafe returns, with the cycle term isolated

**Status: PROPOSED corollary of the [critical physical occupation theorem](PHYSICAL_OCCUPATION.md).** Write K_F for the positive pushforward on the enlarged unsafe set U_F killed at the fixed floor F at every physical step. Let C_F consist of states on surviving periodic J_F cycles, let beta=H_2(log_3 2)/2, and put

    w(x)=exp(L(x)/32) R(x)^{-beta},

where L(x) counts the physical shortcut steps in the first A module. For *every* nonnegative summable input f the actual transported masses satisfy

    sum_{j>=0} ||1_{U_F outside C_F, R>=B} K_F^j f||_w
        <= C ||f||_1 / sqrt(log B)                          (B>=16). (1)

Without the rank restriction the right side is C'||f||_1. There is no post-return envelope hypothesis. This is a bound into a weighted output space, not a contraction of surviving unweighted mass. On large-rank states with a short first module the output weight is small. Thus (1) permits a nonperiodic trajectory to escape to infinite height.

**Proof.** Follow any one positive source. Every nonperiodic state along its J_F path is visited at most once, since a second visit with all intervening steps surviving would put that state on a surviving cycle. Each such state is also a distinct point on the same ordinary raw shortcut orbit. Its total w-weight above rank B is bounded by the critical Mellin tail of the physical occupation theorem, uniformly in the source. The deterministic pushforward identity and Tonelli's theorem give (1) by multiplying by the initial source masses. The same proof without the critical weighting gives

    sum_{j>=0} ||1_{U_F outside C_F, R<=Y} K_F^j f||_1
        <= C ||f||_1 Y^beta/(log Y)^{3/2}                   (Y>=16). (2)

The projection onto C_F is mathematical and need not be decidable. An alternative directly computable finite-path version counts each state only on its *first* visit by each source. It satisfies the same bounds with no periodicity test, since even the first traversal of a cycle consists of distinct states of the raw orbit.

**Retaining actual cycles at finite horizons.** For a source that enters a surviving induced cycle gamma at first-return index t_0, let d be its period and W_B(gamma) the sum of w over its cycle vertices of rank at least B. For a horizon N the number of complete traversals after entry is max(0,floor((N−t_0)/d)); use zero for a source not entering a cycle by N. In the sum of weighted high-rank occupation through j=0,...,N−1, subtract this count times W_B(gamma) separately for every source and then average by f. The remainder is nonnegative and at most C||f||_1/sqrt(log B), uniformly in N: the preperiod plus the last incomplete cycle traversal uses each state at most once. This formula is valid whether or not any nontrivial positive cycle exists. It separates recurrent mass from a uniform error without claiming that the recurrent contribution vanishes.

**Consequence for a hypothetical infinite return orbit.** For any epsilon>0, a constant c_epsilon>0 exists such that for all large N, at least (1−epsilon)N of its first N unsafe states have

    R(x_j) > c_epsilon N^{1/beta}(log N)^{3/(2 beta)}.        (3)

Apply (2) to a unit source and choose Y equal to the right side with sufficiently small c_epsilon. In particular, dividing the expression N^{1/beta}(log N)^{3/(2 beta)} by any positive function tending to infinity gives a lower bound that holds at indices j=N on a set of natural density one. To see this, on the block [N/2,N] use the minimum of that function over the block and the common upper threshold N^{1/beta}(log N)^{3/(2 beta)}; the resulting bad count is o(N) (or bounded if the threshold stays bounded). Cover the initial indices by dyadic blocks. The same argument using R(x)<=x² yields the ordinary numerical threshold with beta replaced by h=2 beta in (3). No pointwise rate is asserted at every index.

The global bootstrap still needs unweighted mass control or an independent obstruction to both escape and surviving cycles. Even a positive, uniform, all-return Green bound in the displayed decreasing output observable cannot provide either alone.
