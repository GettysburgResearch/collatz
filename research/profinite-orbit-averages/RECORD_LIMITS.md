# The ternary limit set forced by coefficient records

**PROPOSED.** On an odd Syracuse orbit write U(x)=(3x+1)/2^a, where a=v_2(3x+1). At a target z in the ternary integers, a legal reverse step of label a≥1 is z↦(2^a z−1)/3 in the ternary integers. Define K to consist of ternary targets admitting an infinite reverse path on which every prefix of length q satisfies

    2^{a_1+...+a_q} ≤ 3^q.

K is compact, has ternary Hausdorff dimension h=H_2(log_3 2)=0.9499555... and contains no positive odd ordinary integer. Every nonperiodic positive odd orbit has coefficient records tending to infinity, and their ternary distance from K tends to zero. The conclusion localizes all accumulation points of these record times; it does not imply that an ordinary target lies in K.

## Compactness, ordinary exclusion and record convergence

At finite depth q the prefix-sum restriction gives a finite set of exponent words; the domain of each is a single closed ternary ball of depth q. Their unions K_q are decreasing. The finite-branching path tree shows K equals their intersection. If z is a positive odd integer, every legal reverse step gives another positive odd integer: 2^a z−1 is a positive odd multiple of three. The reverse endpoint after q steps is strictly less than (2^{Σa}/3^q)z≤z. Therefore an infinite such path stays in a finite set. An infinite backward path in this finite set must eventually run around a cycle: on odd positive integers every state has a unique forward successor, and on the eventual recurrent states each vertex has its cyclic predecessor. Every positive cycle has product 2^{Σa}/3^q=∏(1+1/(3x))>1 per period. Repetition contradicts the uniform prefix bound. In fact the path can never leave its eventual backward cycle and then return to it without repeating that same cycle.

On a nonperiodic ordinary orbit define J_j=3^j/2^{Σ_{i≤j}a_i}. The physical value x_j=x_0 J_j ∏_{i<j}(1+1/(3x_i)) tends to infinity, and the product is bounded by the [distinct-orbit reciprocal estimate](../integrated/orbitwise-boundaries/README.md). Hence J_j has infinitely many increasing record times. At a record j every backward prefix of length q≤j has inverse multiplier J_(j−q)/J_j≤1. Its endpoint belongs to K_j as a ternary target, meaning x_j∈K_j. If any record subsequence stayed a fixed distance from K, ternary compactness and closedness of each fixed K_q would put a subsequential limit in K, a contradiction.

## Exact dimension

Put b_*=log_2 3. The allowed depth-q cylinders number at most binom(floor(b_* q),q), by summing the positive compositions. Stirling's formula gives their log-count divided by q log3 at most h+o(1). This proves the upper bound.

For the lower bound fix 1<b<b_* and take the inverse alphabet of [the bounded-intercept construction](../critical-orbit-mellin/SHIFT_ESCAPE_DIMENSION.md). For large q it consists of M≥c_b binom(floor(bq)−1,q−1) distinct ternary cylinders of depth q, one labeled block per cylinder, all with the same real inverse slope D=2^{floor(bq)}/3^q<1. The largest inverse slope of any prefix inside this finite alphabet is a finite number H. Prepend one fixed run of a=1 letters of length l with (2/3)^l H≤1. After that run, every concatenation of alphabet blocks satisfies every prefix bound: whole blocks only multiply the preceding slope by D. The domains nest as M disjoint children at each block because inversion on a legal prefix is an affine bijection from its ternary cylinder onto the ternary integers. Uniform child mass gives dimension at least log M/(q log3), with the fixed initial run causing no change. Let q tend to infinity and b increase to b_* to obtain h.

K is thus a closed nowhere-dense null set allowing arbitrarily accurate ternary approximation by actual finite record histories, while an infinite bounded-slope reverse path at one positive ordinary target is impossible. Neither fact bounds how close a growing ordinary target can be to K in terms of its height.
