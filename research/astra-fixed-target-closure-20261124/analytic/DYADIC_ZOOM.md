# Exact ternary averaging over dyadic real scales

**PROPOSED written theorem.** The stationary geometric Syracuse law has an exact scale symmetry on the real region `(0,1]`. When the real coordinate is rescaled back to its original interval, averaging dyadic scales for one complete multiplicative period gives an *exact* product at every fixed ternary depth. An individual scale retains the original conditional dependence. These conclusions use the independent geometric first gap; no positive ordinary convergence assumption, mixing estimate, or fibre theorem is needed.

Take positive independent gaps with `P(e_i=t)=2^(−t)` and `S_i=e₁+…+e_i`. Evaluate `Σ_{i≥1}3^(i−1)2^(−S_i)` at the real and ternary places, obtaining `R` and `Z`. The real sum converges almost surely since `S_i/i→2`; the ternary sum always converges and is a unit by its first term. Write `ν` for this joint law. The normalization agrees with paper 9, §1 (1), and paper 19, §1. [Weaver, ternary Syracuse laws](https://rstation.ai/problems/collatz/papers/9) · [Weaver, joint affine law](https://rstation.ai/problems/collatz/papers/19)

## The first-gap bijection

For every Borel `I⊂(0,1]`, ternary Borel `A`, and integer `m≥0`,

\[
  \nu(2^{-m}I\times A)=2^{-m}\nu(I\times 2^mA).                           \tag{1}
\]

The remaining real tail `R′` is positive, so `R=2^(−e₁)(1+3R′)>2^(−e₁)`. Whenever `R≤2^(−m)` the first gap is at least `m+1`. Subtract `m` from it, keeping the remaining gaps fixed. Both evaluated series multiply by `2^m`. The inverse operation adds `m` to the first gap. Conditioning on that gap shows that the original event has exactly `2^(−m)` times the transformed mass.

For a finite word of length `b≥2`, the remaining tail is still strictly positive. The same bijection equates the number of words of total `s+m`, real offset in `2^(−m)I` and offset residue `r mod 3^j` with the number of words of total `s`, real offset in `I` and residue `2^m r mod 3^j`. A letter cap is transported by adding `m` to the first letter's cap alone. The exact-total atom probabilities also differ by `2^(−m)`. At `b=1`, `I={1}`, `m≥1`, the original one-letter word `(m)` ends at the boundary `2^(−m)`. Subtracting `m` would produce an inadmissible zero gap, which explains the nonempty-tail condition.

## The limit law and its finite periods

Fix `I⊂(0,1]` with `ν(R∈I)>0`, and denote by `λ_I` the law of `(R,Z)` given `R∈I`. For `m≥0` let `λ_{I,m}` be the law of **`(2^m R,Z)`** given `R∈2^(−m)I`. Only the real observation is rescaled here. Applying (1) to every real Borel subset of `I` gives

\[
       \lambda_{I,m}=((x,z)\mapsto(x,2^{-m}z))_*\lambda_I.                    \tag{2}
\]

At depth `j≥1` write `U_j=(ℤ/3^jℤ)^×`, `P_j=2·3^(j−1)`, and let `π_j` reduce the ternary coordinate. Then for every starting scale `m₀≥0`,

\[
 \frac1{P_j}\sum_{m=m_0}^{m_0+P_j-1}(\mathrm{id},\pi_j)_*\lambda_{I,m}
     =(\lambda_I)_{\mathbb R}\otimes\operatorname{Unif}(U_j).               \tag{3}
\]

Indeed `2` has order `P_j` modulo `3^j`. Its reduction modulo three has order two and `v₃(4^(3^k)−1)=k+1` for `k≥0`, by expanding `(1+3^(k+1)u)^3` with `3∤u` inductively. This gives all `P_j` units. For each particular `z`, the rotations in (2) visit each unit residue exactly once during the indicated period. Integrate that pointwise identity against `λ_I`, retaining any prescribed measurable real test set. In particular the real and ternary finite observations are independent *after averaging*.

The Cesàro averages of `λ_{I,m}` from any start converge weakly to `(λ_I)_ℝ ⊗ Haar(ℤ₃^×)`, with Haar normalized to probability on the units. For fixed `j`, the total-variation error after `M` consecutive scales at depth `j` is at most `min(1,P_j/M)` by removing full periods. This bound is uniform in `I,m₀`. One can also quantify convergence on the full unit group. For a bounded measurable real-dependent test `f(x,z)` with Lipschitz constant at most one in the normalized ternary metric, uniformly in `x`, the expectation error is `O((1+log M)/M)`. To see this, partition any run of `M` scales into at most two blocks of each length `P_j` and at most one singleton, using the ternary digits of `floor(M/2)`. In a full block of length `P_j`, couple a random rotated unit with unit Haar by leaving its residue modulo `3^j` fixed and sampling uniformly inside that residue. For each fixed base `(x,z)` the resulting unit is Haar and independent of the fixed `x`, and the test changes by at most `3^(−j)`. The contribution of that block to the unnormalized error is at most `P_j·3^(−j)=2/3`. A singleton contributes at most one since the ternary diameter is at most one and the real marginal stays fixed. Summing the `O(1+log M)` pieces proves the bound. At length exactly `P_j` the sharper bound is `3^(−j)`.

There is also an exact probabilistic formulation at the origin. Conditional on `R≤1`, let `m=floor(log₂(1/R))`. The intervals `2^(−m)(1/2,1]` are disjoint and cover `(0,1]`. By (1), `P(m=d | R≤1)=2^(−d−1)` and `m` is independent of `(2^mR,2^mZ)`, which has law `λ_(1/2,1]`. The event used for conditioning has positive probability: choose a bounded positive-probability set for the remaining real tail (finite almost surely), then a sufficiently large first gap. The dyadic partition is valid even if a boundary power of two has positive mass.

Paper 19's source-qualified pure singularity of `ν` relative to Lebesgue times ternary Haar is consistent with (3). The average uses many distinct annuli, and its real marginal is the original conditional one. The identity does not assert a pointwise fibre law at a supplied ordinary ternary integer or mix the deterministic forward orbit from that integer.

[zoom_check.py](zoom_check.py) checks the finite affine bijection against a separate complete enumeration at each shifted total, unit rotations against the product for finitely many labelled real offsets, and the boundary at word length one. The stationary distribution and asymptotic deductions are written proofs.
