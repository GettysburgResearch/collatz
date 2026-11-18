# First-landing capacity with the actual future minimum retained

**PROPOSED, source-qualified.** Let U be the positive odd Syracuse map, `m(x)` its ordinary future minimum, and `p_t` the natural-density law of m on all positive integers. Let A be any reachability antichain of positive odd ternary units. For every nonnegative weight f on the positive integers,

    Σ_{a∈A} f(m(a))/a ≤ C Σ_t f(t) p_t.                               (1)

For each a in a finite subset, use a common large shell `(X/4,X]` and apply [the prior uniform first-landing theorem, Theorem 14](https://rstation.ai/problems/collatz/papers/12/v1), at its own threshold a with its own target a. It supplies at least `cX/a` odd starts whose prior odd states exceed a. All these starts have exact global minimum m(a); even states between odd ones cannot lower the minimum. The certified sets for distinct a are disjoint since both targets on one trajectory would be comparable. For each of the finitely many labels, divide by X and take a limit using its natural density. Then take the supremum over finite subsets of A. This proves (1) without needing convergence of untruncated empirical moments.

In particular for an antichain whose entire futures exceed B we have `Σ 1/a≪ε(B)`, where `ε(B)=Σ_{t>B}p_t`, **even if** members have earlier low predecessors. This removes the low-reachability exception in [the earlier low-source argument](SINAI_LOW_ANCESTORS.md). The [prior power first-landing upper theorem, Theorem 1](https://rstation.ai/problems/collatz/papers/102/v1), gives `ε(B)≪exp(C√log B) B^(−g)` with `g=1−H₂(log₃2)+1/351`. The earlier lower and upper results use their externally stated inputs.

## Every inverse clock

Suppose y is nonperiodic and odd, its future remains strictly above B, and q≥1. In the notation of the low-source argument one now has

    0 ≤ g_q(y) − Σ_{ℓ∈L_B(y),d(ℓ)≤q} J(ℓ,d(ℓ))g_(q−d(ℓ))(ℓ)
      ≤ C ε(B)y.                                                        (2)

There is no waiting condition on q. Partition paths containing a low state by their last low ancestor ℓ. Every remaining q-level source has its entire future above B. Its unit sibling `4x+1` still has this property if 3 divides x, belongs to the same q-level, and replacing all such x costs at most a factor six in the harmonic sum. Nonperiodicity makes this level an antichain. Apply (1) and `J(x,q)≤y/x`. At q=0 the identity `g_0(y)=1` is handled separately.

For a nonperiodic unit y, put `M_q(y)=min{x odd: U^d x=y for some 0≤d≤q}` and `D=min(m(y),M_q(y))`. Combining (2) at B=D−1 with the earlier unit-minorization lower bound gives, for D≥3,

    c/M_q(y) ≤ g_q(y)/y ≤ C exp(C√log D) D^(−g).                        (3)

At q=0 this also holds directly. This improves the former two-parameter upper bound involving `B/M_q(y)`. A fixed low ancestor can still supply a linear-size density at all later clocks.

## Reciprocal correction on a genuinely high escaping tail

For a distinct odd escaping orbit `y_i`, choose an off-spine sibling `s_i=4y_i+1` when it is a unit, and `s_i=16y_i+5` otherwise. Each is a unit, `y_i<s_i≤21y_i`, and `U(s_i)=y_(i+1)`. It never lies on the spine, since two different spine states cannot share a successor. The siblings s_i form an antichain: after their first step their future lies wholly on the spine. Also `s_i>U(y_i)` and hence `m(s_i)=m(y_(i+1))`. Consequently (1) gives

    Σ_{i≥0} f(m(y_(i+1)))/y_i ≤ C Σ_t f(t) p_t.                        (4)

For any tail entirely above B≥2 this implies

    Σ_i 1/y_i ≪ exp(C√log B) B^(−g).                                   (5)

Here the sum is over that tail only; applying (4) to the indicator of minima above B proves it. This improves the exponent `1−h` from interval packing for the future correction on escaping high tails. In particular for `F(x)=x∏(1+1/(3U^i x))`, the same bound applies to `log(F(x)/x)` when the future minimum exceeds B. Substituting into [the neighboring phase discrepancy argument](PHASE_IMBALANCE.md) gives `1+|Δ| ≫ B^(g/13.3) exp(−C√log B)` for adjacent unbalanced inputs in the same escaping component with both future minima above B. The numerical gain in the exponent is `1/(351·13.3)`; it does not reach the exponent 1 needed for the unweighted first-moment target.
