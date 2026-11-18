# Periodic approximation of ordinary conditional real fibres in spatial mean

Write λ for additive ternary Haar, σ for the stationary affine law of
(F,Z), and k_f=dE[f(F);Z∈·]/dλ. Let k_(m,f) be its conditional
expectation on the classes modulo 3^m, a specified periodic function.
For every continuous f on [0,∞) with |f(B)|≤C/(1+B), and 0<c<C'<∞,

    lim_(m→∞) limsup_(T→∞) (1/T) Σ_(x odd, cT≤x≤C'T)
                 |G_x(f)−k_(m,f)(x)| = 0.                              (1)

This includes compactly supported continuous tests. Thus the ordinary
fibre tests admit periodic approximations in the Besicovitch mean
seminorm. In particular the laws of any finite vector of these tests,
sampled at a uniform odd point of the shell and retaining its dyadic
and ternary labels, converge to the corresponding vector of stationary
conditional tests at a Haar ternary point and an independent odd Haar
dyadic label. For the reciprocal test f(B)=1/(1+B), the resulting
limit has all finite moments: on a dyadic real shell b≥1, the known
L^p bound for its ternary density is O_p(b^(1−2/p)log(eb)^(1−1/p))
for p≥2, and weighting by 1/b gives a summable series. This moment
assertion is about the limiting distribution; (1) itself concerns
first absolute moments. [Stationary real-shell bounds, Theorem 16](https://rstation.ai/problems/collatz/papers/9/v2).

## A signed microscopic comparison from positive incoming visits

First let f≥0 be Lipschitz with bounded support. Put a=1.001,
R=T^a, L=log R, Δ=(a²−a)L, N=⌊L/20⌋, ℓ=log(4/3), δ=ℓ/2. Let I be
the integer interval (4) of the [moving-shell proof](MOVING_ORDINARY_FIBRES.md).
It has |I|∼Δ/ℓ and all j∈I are less than N. Fix *arbitrary* selectors
0≤A_x≤1 in the shell, allowed to depend on T and every individual
output label. The earlier proof up to the incoming reciprocal proxy
uses only its exact landing label Y_R, the following bounded segment,
and the local real mark. Its errors remain uniform for these selectors:
changing the mark at an actual label leaves its selector exactly fixed.
The cap M on the weighted sum costs M·o_T(1) for the total-variation
comparison, and only O(1/M) for selected proxy visits at times in I.
For the latter bound it suffices to control the second moment of the
*number* of contributing visits, as in the previous proof, ignoring
all A_x. The rounding coupling to an independent log height is used
only for this count, whose shell may be enlarged slightly. It is never
used to replace individual selected integers by rounded real labels.

Consequently the marked source occupation gives a lower bound for
T⁻¹ Σ A_x G_x(f) by δ times the actual reciprocal-proxy expectation
of its selected (x/T) f(β_j) visits at j∈I, with lower-limit error
O(1/M), uniformly in A. Here β_j starts at zero at the proxy source.
Let w be an inverse-order word of length j, with real offset β_w,
multiplier J_w and D_w=log J_w. For each odd x in the shell the word
is legal exactly on its class modulo 3^j, and its source is exactly
n=(x−β_w)/J_w. When f(β_w)>0 and

    |D_w+ℓj|≤L^(2/3)/2,                                                (2)

the source n is odd positive and log n is in [aL,a²L] for the whole
shell by the definition of I. Its reciprocal-proxy probability is
(2+o(1))/(Δ n), with a common relative normalization. Multiplying
by δ x/T gives at least (2δ−o(1))J_w/(TΔ), uniformly. This performs
the microscopic comparison on the *original integer proxy*.

Put h_(j,f)(x)=Σ_(w legal at x) J_w f(β_w), a function modulo 3^j.
Omitting words that fail (2) has total loss o(1) in the normalized
comparison summed over I and the shell: the Haar mean of their
positive periodic function is at most ||f||∞ times their iid
probability O(exp(−cL^(1/3))). For any nonnegative function on this
quotient its sum in our odd shell divided by T is at most a fixed
multiple of its Haar mean, since 3^j≪T uniformly. This also bounds
the harmless common relative normalization errors. We obtain

    (1/T) Σ A_x G_x(f) ≥ (2δ/(TΔ)) Σ_(j∈I) Σ_x A_x h_(j,f)(x)
                            −O(1/M)−o_(T;M)(1).                        (3)

On Haar, ||h_(j,f)−k_(j,f)||₁≤E|f(β_j)−f(F)|→0, coupling the
inverse-order iid prefix with its infinite continuation. Moreover
k_(j,f) converges to k_f in L¹ by the conditional-expectation
martingale theorem. Thus for j≥m tending uniformly to infinity the
L¹ difference from the fixed k_(m,f) is bounded by
||k_f−k_(m,f)||₁+o(1). Both functions in the difference are periodic
modulo 3^j, so the same comparison to the Haar mean applies in our
shell, uniformly in A. Take T→∞ and then M→∞ in (3) and use
2δ|I|/Δ→1. Choosing A_x to select exactly the negative differences
bounds the mean negative part in (1) by O(||k_f−k_(m,f)||₁).
The *signed* mean difference tends to zero for each fixed m: the
ordinary mass converges by the [moving-fibre theorem](MOVING_ORDINARY_FIBRES.md),
and the periodic mean of k_(m,f) is exactly E f(F). The mean absolute
error is therefore bounded by twice the negative-part bound in the
limit. Sending m→∞ proves (1) for the initial tests.

Uniform approximation handles compact continuous tests by applying
the established spatial mass bound to a compact cutoff. Decompose
signed functions into positive and negative parts. Finally the
[critical inverse-mark tightness](INVERSE_MARK_TIGHTNESS.md) permits
removing the compact cutoff for every f in (1); the corresponding
periodic approximations have mean absolute cutoff error at most the
stationary real-marginal tail integral. The finite-vector convergence
follows by testing bounded Lipschitz functions and first using (1)
for each component, then equidistribution on every fixed product of
dyadic and ternary quotients, and then Haar martingale convergence.
