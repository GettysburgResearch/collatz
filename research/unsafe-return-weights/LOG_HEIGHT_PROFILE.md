# Logarithmic height distribution of the finite Syracuse densities

**PROPOSED, source-qualified.** In the notation of the [signed harmonic identity](SIGNED_MASS.md), take ℓ=log(4/3), γ=log(3/2), and one fixed forward odd spine y_(C,j) for each escaping component C. For every compactly supported Lipschitz f on [0,∞),

    (1/q) Σ_(t odd) g_q(t) f((log t)/q)/t
      = (1/2)∫₀^∞ f(s) ds
        + Σ_(escaping C) (3/2)H_C · (1/q)Σ_(0≤j<q) f((log y_(C,j))/q)
        + o_f(1).                                                       (1)

There is no assumption of an asymptotic velocity for any diverging orbit. Changing the fixed representative in a component changes its empirical contribution by o(1), since the two forward paths have a common tail. The coefficients are summable by the signed mass identity. If a spine has log y_j/j→v>0 its limiting empirical contribution is uniform on [0,v]; for v=0 it is a point mass at zero. These velocity assumptions are optional.

For γ≤α<β, the left measure therefore has mass tending to (β−α)/2 on (α,β]. Indeed U(x)+1≤(3/2)(x+1), so log y_(C,j)≤γj+log(y_(C,0)+1). Any weak component limit is supported on [0,γ] and has no atom at γ: the number of j<q with log y_j/q>γ−ε is at most (ε/γ)q+O_C(1). Lipschitz approximation and summability also give, for every α≥γ,

    lim_(q→∞) (1/q) Σ_(1≤t≤exp(αq), t odd) g_q(t)/t
         = α/2 + Σ_(escaping C) (3/2)H_C.                               (2)

Thus the positive finite first-period escape test can use the cutoff (3/2)^q instead of 2·3^q. Above that cutoff all fixed logarithmic bands have their baseline mass, whether any escape occurs or not. The missing upper bound at or below the cutoff remains open.

## Sampling at the source

Write V_q(n)=∏_(i<q)(1+1/(3U^i n))^(-1). The exact level formula converts the left of (1) into

    (1/q) Σ_(n odd) (V_q(n)/n) f((log U^q n)/q).

The logarithmically weighted odd source measure in log coordinates s=(log n)/q has limit ds/2 on bounded intervals. Fix K large depending on the support [0,β] of f. Sources above exp(Kq) contribute o(1): if t=U^qn≤exp(βq), the total valuation A obeys n≤t·2^A/3^q. For a given t the omitted sum of path multipliers is at most 3^q Pr(G₁+…+G_q≥(K−β+log 3)q/log 2) for independent positive geometric letters Pr(G=a)=2^(-a). Choose K so a fixed exponential tilt makes this exponentially small and sum 1/t up to exp(βq). Enlarge K also beyond β+ℓ.

Fix 0<ε<ℓ/4. Sources with s<ε or |s−ℓ|<ε cost O_f(ε) after normalization. Fix R and restrict the rest to paths that visit [1,R]. The omitted harmonic proportion is O(K Pr(m>R))+o_R(1), by the fixed-threshold global minimum law or the [uniform failure bound](https://rstation.ai/problems/collatz/papers/102/v1); the relative odd minimum probability tends to zero. At a successful first landing Y≤R the label is a ternary unit for all these large starts. There are finitely many possible Y. Apply the [ordinary-shell first-hit estimates](FORWARD_FIRST_HIT_CLOCK.md) for the path to each such Y. Conditioning on the exact first-landing label is unnecessary: any violating path is included in the first-hit exceptional set for that label without that restriction. For fixed R, outside harmonic mass o(q) on ε≤s≤K, the first low time τ satisfies τ=(log n)/ℓ+o(q), and the prefix log heights up to τ equal log n−ℓm+o(q) uniformly. More precisely, these statements with errors ηq hold outside o(q) for each fixed η>0. This follows uniformly on each dyadic shell between exp(εq) and exp(Kq) since the smallest shell tends to infinity, the standard error is O_P(√(Kq)), and each shell has bounded reciprocal mass.

On s>ℓ+ε take η sufficiently small. Then q<τ, and every state up to q exceeds exp(εq/2) outside the exceptional set. Thus V_q(n)=1+o(1) there, and the resulting integral is (1/2)∫_(s>ℓ+ε) f(s−ℓ)ds up to the omitted minimum probability and an error tending to zero with η. Letting ε decrease gives the first term in (1).

## Sampling after the first low visit

On s<ℓ−ε the remaining time q−τ is at least a fixed positive multiple of q. For each fixed Y entering a cycle, V_q(n) tends to zero uniformly on its retained sources since subsequent complete laps multiply it by J_C<1. For each Y in an escaping component it satisfies V_q(n)=V_∞(n)(1+o_R(1)) because the reciprocal correction product on the future tail tends to one. All those Y in a single component C merge with the chosen spine in finitely many steps, so the endpoint is y_(C,q−τ+O_R(1)), with the fixed finite phase shifts allowed to depend also on the selected representatives.

Replace this index by j=⌊q−(log n)/ℓ⌋. An individual downward step could have large logarithmic size. The replacement nevertheless costs O_(R,f)(η)+o(1) in the normalized sum. Each predicted index j occupies a log-n interval of length ℓ and has uniformly bounded source reciprocal mass. Each actual index is within ηq+O_R(1) of it. For a fixed spine its log heights have total variation O_C(q) on the first 2q terms: all upward increments are at most log 2 and the total of downward increments is at most the sum of the upward ones plus log y_(C,0). For each predicted j bound the test error by Lip(f)/q times the variation over its whole candidate index window. Each step occurs in O(ηq+O_R(1)) windows. Summing over j and dividing by q proves the bound, then let η decrease for fixed R.

Only finitely many components are represented below R. For each retained component replace the restriction to starts hitting [1,R] by the entire component. The sum of the added masses is again bounded by the same minimum-failure proportion, since the components are disjoint. Reinsert the discarded endpoint intervals in s at cost O_f(ε). Let d_C be the normalized odd logarithmic mean of V_∞1_C, given by Valbuena's component formula δ d_C=(3/2)H_C, δ=ℓ/2. The increasing functions

    s ↦ (1/q) Σ_(n odd≤exp(sq), n∈C) V_∞(n)/n

converge uniformly on [0,ℓ] to s d_C/2, by pointwise convergence and continuity of the limit. The step test in s with values f(log y_(C,j)/q) has total variation O_(C,f)(1) by the same variation bound. Summation by parts therefore replaces the weighted source distribution by ds·d_C/2 with o(1) error. The resulting sum is δ d_C times the q-term empirical average in (1). Components not represented below R have total weighted mean at most Pr(m>R), by global minimum tightness. Taking q to infinity, then R to infinity and ε to zero, completes the comparison. The normalization uses [Valbuena's weighted basin and component formulas](https://doi.org/10.5281/zenodo.23025885).
