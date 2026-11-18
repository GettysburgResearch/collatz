# All nonconstant dyadic mantissa modes cancel in the ordinary cone

Let the positive-target arithmetic cone put at the pair
(r,θ)=(β_w/t, log₂(t) mod 1) the weight J_w/t of each compatible
q-word with its least positive odd representative t≤2·3^q. On
(0,∞)×(ℝ/ℤ), after division by q its measures converge vaguely to

    μ(dr) ⊗ dθ,                                                       (1)

where dθ is normalized Lebesgue measure and μ is the ordinary escape
distortion measure. Thus a nonzero escaping mass is equidistributed
in dyadic mantissa *jointly with every off-zero distortion test*.
The constant Fourier mode remains the escape problem.

For nonzero integer k put τ=2πk/log 2 and χ=3^(iτ). Then χ≠1 by
irrationality of log₂3. For a smooth real test f with compact support
away from zero define the complex stationary zero-cylinder evaluation

    A_q=Σ_(t odd positive) t^(−1+iτ) 3^q E[f(F/t); Z≡t mod 3^q].

Its difference from the Fourier-weighted physical cone test is
O_f(1) uniformly in q: use the [unweighted real-tail replacement](STATIONARY_ZERO_FLUX.md)
term by term, since all added phases have absolute value one.
Peeling the outer geometric letter a gives exactly

    A_(q+1)−χ A_q = χ Σ_(x odd positive) ∫
          [(x+1/3)^(−1+iτ) f((B+1/3)/(x+1/3))
                         −x^(−1+iτ) f(B/x)] G_(x,q)(dB).

Here G_(x,q)=3^q Pr(F∈dB,Z≡x mod 3^q). The digit phase 2^(−iτa)
is identically one, which is the reason χ is fixed across all legal
words. The bracket has absolute size O_(f,τ)(x⁻²) uniformly in B.
As in the ordinary generator proof, g_q(x)≪H(x) at q≥1, the majorant
is summable, and each ordinary real fibre converges. Thus the right
side tends to a finite complex constant D. Iterating the recursion,
the constant forcing contributes the bounded geometric sum of χ,
and the absolute Cesàro mean of the errors in the forcing tends to
zero. Consequently A_q/q→0. The constant mode is the ordinary
arithmetic cone limit. Approximation of compactly supported continuous
tests by finite sums of smooth real tests times circle trigonometric
polynomials proves (1), using the ordinary nonnegative marginal to
bound approximation errors on each compact real set.
