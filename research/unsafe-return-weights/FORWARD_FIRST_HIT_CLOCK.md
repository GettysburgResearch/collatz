# First-hit clocks and arithmetic counts in ordinary source shells

**PROPOSED, source-qualified.** Let W_X be uniform on the positive odd integers in (X/4,X]. Let t be a fixed positive odd ternary unit, and sample conditionally on W_X eventually visiting t under the odd Syracuse map U. This conditioning has positive limiting probability by the fixed-target natural-density theorem. Put τ=min{i:U^i W_X=t}, ℓ=log(4/3), and a(x)=v₂(3x+1). For a fixed dyadic/ternary product-cylinder indicator f on the odd dyadic integers times the ternary integers let ν(f) be its stationary mean under normalized odd dyadic Haar times the Syracuse-offset law. As X tends to infinity, all the following random quantities are tight after division by √log X:

    τ−(log X)/ℓ,
    max_(0≤m≤τ) |Σ_(i<m) a(U^i W_X)−2m|,
    max_(0≤m≤τ) |Σ_(i<m) f(U^i W_X,U^i W_X)−mν(f)|,
    max_(0≤m≤τ) |log(U^m W_X)−log W_X+ℓm|.                             (1)

The same holds simultaneously for any fixed finite list of tests. In particular the shortcut time to t from odd W_X is (2/ℓ)log X+O_P(√log X), and fixed valuation-word frequencies along the first-hit path have errors O_P(1/√log X). The assertion concerns fixed targets, including cyclic t stopped at its first visit. It gives no central limit distribution or uniform waiting bound for large targets.

Leen already proved a stronger Gaussian limit for fixed-target shortcut first-hit times in natural density, the Brownian descent profile with terminal labels, and arithmetic progression transfer. In particular the clock tightness at the scale in (1) is prior. The proof below also bounds maximal cumulative errors for arbitrary fixed dyadic/ternary cylinder observables. [Leen, Invariant sets, Predecessor clocks, Terminal data, and Arithmetic progressions](https://doi.org/10.5281/zenodo.23252395)

Valbuena previously proved the two-sided leading first-hit clock in logarithmic density; Inselmann previously established natural-density trajectory approximation on its linear-log horizon. Here we use the [finite-to-limiting landing domination, Corollary 16](https://rstation.ai/problems/collatz/papers/12/v1) to transfer the [stabilized shell-segment estimates](https://github.com/GettysburgResearch/collatz/blob/4695ea99ee998c8a992c0ea23c2f2d98847312a5/research/native-pressure-20261118/ITERATED-LOG-BOUND.md) to an actual uniform odd source and sum fluctuation errors in probability. [Valbuena, first-hit time law and clock conversion](https://doi.org/10.5281/zenodo.23025885) · [Inselmann, Theorem 1.10](https://arxiv.org/abs/2402.03276)

## Transport at one threshold

Set b=1.001, R_j=exp(b^j), and L_j=log R_j. Thresholds may be real because entry tests use integer states. Let I be the largest index with R_I≤X/4. Thus L_I≤log(X/4)<bL_I. Let Y_j denote the first label at most R_j when reached. The initial path from W_X to Y_I is also allowed to be empty. For every j≤I, the cited Corollary 16 bounds the unconditional probability of a successful Y_j lying in any label set by an absolute constant times the limiting landing probability. It applies to any event concerning Y_j and its subsequent segment, since forward dynamics are deterministic. The cited stabilization argument bounds the latter by the corresponding probability from a log-weighted source in [R_j^b,R_j^(b²)] plus O(L_j^(-c)). Defaulting a failed passage to 1 in that argument only enlarges the probability assigned to sets of finite labels.

In particular fix a sufficiently small ε₀>0 depending only on b and the drift. Throughout √L_j≤u≤ε₀L_j, except on an unconditional event of probability

    O_f(exp(−c_f u²/L_j)+exp(−c_f L_j)+L_j^(-c)),                      (2)

every successful label Y_j has log height L_j+O(u); its first segment to R_(j−1) exists, takes (L_j−L_(j−1))/ℓ+O_f(u) steps, and every prefix has valuation and f sums within O_f(u) of its linear prediction. Indeed on the cited comparison source, the exponential maximal inequalities apply up to L_j/20 steps. The first entries of both thresholds occur within that horizon, and each entry has log overshoot O(u). The proof there uses u proportional to √(L_j log log L_j) for an almost-sure result. Its same exponential-martingale calculation gives (2) for this range of u: select a tilt of order u/L_j within a fixed neighborhood of zero. The dyadic bit-budget failure and counting error are O(exp(−c_f L_j)). With ε₀ small the ordinary log loss ℓL_j/20 exceeds (b²−1/b)L_j plus the maximal error, as required to hit the thresholds. The ternary memory of f consumes only a fixed number of initial terms.

The initial path from W_X down to R_I satisfies the direct maximal inequalities with L_I, without the stabilization error. Its integer counting error is O(2^(4(L_I/20+O_f(1)))/X). For all sufficiently large I the starting log height is between L_I and bL_I+O(1), so the direct high-to-low calculation in that proof applies. Its clock differs from (log W_X−L_I)/ℓ by O_f(u), and its maximal prefix errors are O_f(u).

## Summing errors in probability

Choose large fixed J with R_J≥t and B≥1. At j=J+1,…,I assign

    u_j = min(ε₀L_j, B(1+I−j)√L_j).

For sufficiently large fixed J these are in the declared range. The probability of any bad segment, also including the direct initial segment with u_I, is at most

    C_f [Σ_(j≥J) (L_j^(-c)+exp(−c'_f L_j))
         + Σ_(k≥0) exp(−c'_f B²(1+k)²)].

This follows by a union bound from (2), using exp(−min(v,w))≤exp(−v)+exp(−w). Given an arbitrary probability tolerance choose J and B to make the bound small compared with the positive limiting probability of the t-basin; this yields the corresponding conditional estimate. On that basin every passage down to R_J succeeds. Once at Y_J≤R_J its remaining first-hit path to t has bounded length, valuations and corrections, since there are only finitely many possible labels on this fixed basin. This finite bound may depend on J and t.

The geometric sum Σ_j u_j≤B√L_I Σ_(k≥0)(1+k)b^(−k/2)=O(B√log X) uniformly in I. Clocks from the complete segments telescope in log height. Prefix count errors add at complete segments and at most one last partial segment. Finally the true affine offset adds Σ log(1+1/(3U^i W_X))=O(1) on any first-hit prefix by the uniform simple-path reciprocal bound, so centered valuation sums also imply the last log-height estimate in (1). The fixed bounded cost below R_J and log W_X−log X=O(1) are absorbed as X grows. No assumptions about independence between successive actual landing labels are used.
