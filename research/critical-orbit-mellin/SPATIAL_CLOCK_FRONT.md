# Logarithmic-time saturation and the Gaussian front of the signed spatial current

Write A_(T,k)(f)=U_(T,k)(f)−D_(T,k)(f) for the signed current of the
[ordinary edge formula](SPATIAL_EDGE_CURRENT.md) with k Syracuse steps
in place of one. Thus an edge x→y=U^k x carries the pushed k-step
fibre measure J_w (B↦β_w+J_wB)_*G_x divided by y. Set A_(T,0)=0,
ℓ=log(4/3), σ=(log 2)√2 and m_f=μ(f)−(ℓ/2)f(0). For f∈C¹[0,1]
and k/log T→λ<∞,

    A_(T,k)(f)/log T → min(λ,1/ℓ) m_f.                                (1)

For fixed k, A_(T,k)(f)→k m_f. More sharply, if k→∞ and
(log T−ℓk)/(σ√k)→u∈ℝ, then the single additional crossing level obeys

    A_(T,k+1)(f)−A_(T,k)(f) → Φ(u) m_f,                               (2)

where Φ is the standard normal distribution function. The one-clock
current is the same all-root conservation law that detects escape.
The front in (2) concerns its spatial truncation and is present on
the constant test even when every orbit is eventually periodic.

## Exact inverse-clock increment

Let d_f(y,B) stand for the one-step generator bracket

    f((B+1/3)/(y+1/3))/(y+1/3) − f(B/y)/y.

It is bounded by C_f/y², with Σ H(y)/y²<∞. At the canonical inverse
root y, let B₀ be its full real mark and X_j its depth-j inverse state.
Then for every j≥0,

    A_(T,j+1)(f)−A_(T,j)(f)
          = Σ_y H(y) E_y[1_(X_j≤T) d_f(y,B₀)].                        (3)

To verify (3), first express A_(T,j) as the sum over starts x≤T of
the difference between their pushed and initial tests. Interior edges
cancel exactly as for j=1; finite targets have finite full incoming
mass by harmonicity. In the difference of consecutive j, the initial
tests cancel. Push to the current state y, retaining the restriction
on the original start. By the harmonic inverse kernel the conditional
weight of an inverse prefix w at y is J_w H(x)/H(y), and the full
mark B₀ is the pushed mark from the conditional continuation at x.
This gives (3), including cycles and j=0. Ternary nonunits have zero
mass. Absolute convergence follows from the bracket estimate above.
The same series with the indicator removed equals m_f.

For each fixed y, log X_j/j→ℓ almost surely. For k≤b log T, b<1/ℓ,
the probability that any of the first k labels exceeds T tends to
zero. For j≥b' log T, b'>1/ℓ, the probability that any such label is
at most T tends to zero. Both assertions follow directly by eventual
pathwise bounds (ℓ±ε)j on log X_j, including the finitely many initial
labels. Summability in (3) makes these estimates uniform for the
summed increments in their respective ranges. The remaining
ε log T-sized transition interval has uniformly bounded increments.
This proves (1), including λ=0, and the fixed-j statement follows
from (3) directly. At the Gaussian scale the [fixed-root stable central
limit theorem](../native-pressure-20261118/INVERSE-BROWNIAN.md)
applies with the fixed bounded inverse-path observable d_f(y,B₀).
It multiplies that root's unrestricted expectation by Φ(u), and
summable domination proves (2).

## Concentration on power-sparse dyadic growth words

Here is a growing-clock consequence. Take, for example,
k=⌊0.01 log T⌋ (natural logarithm). If μ(1)>0 there exists an
absolute ρ>0, independent of the escaping component, such that

    liminf_(T→∞) [1/k] Σ_(x≤T<U^k x, H(x)>T^ρ) H(x)/x ≥ μ(1).          (4)

Indeed for f≥0 supported away from zero, (1) implies a lower bound
μ(f) for the k-normalized upward mass. Each upward source starts at
x≥(T+1)(2/3)^k−1, and every intermediate state satisfies the same
lower bound by the maximal positive forward growth. Thus the total
relative affine correction along its path is 1+o(3^(−k)). The final
height exceeds its starting height, so the pure multiplier J_w is
at least one: if J_w<1 then 1/J_w−1≥3^(−k). Its word total is at
most floor(k log₂3). Such words have aggregate odd Haar probability
≤exp(−I k) for some absolute I>0 by a geometric lower-tail Chernoff
bound, and their number is at most 3^k by the composition count.
Each specifies one odd progression modulo 2^(total+1). In the range
x_min≤x≤T its harmonic sum is at most C2^(−total)log T+C/x_min,
by counting the first term and integrating along the progression.
Consequently Σ_(upward sources)1/x ≪ e^(−Ik)log T+3^k/x_min=O(T^(−2ρ))
for some fixed ρ>0. Sources with H(x)≤T^ρ therefore have negligible
mass even before division by k, since J_w/U^k x≤1/x. Exhaust (0,1]
by f bounded by one to obtain (4).

At each fixed k the compact absolute-mark upward baseline has total
(1/2)E[(log J_k)_+] after taking T→∞ and then exhausting compact
marks. To check this, an upward k-word must have J_w>1 for T large,
so there are finitely many words. It tests one dyadic class of relative
odd weight 2^(−total) and x/T∈[J_w⁻¹,1] up to vanishing boundary
errors. Integrate du/(2u) in the compact spatial law. This baseline
decays exponentially in k since E J_1^s<1 for 0<s<1. In contrast,
the excess in (4) is order k. The proof does not give an upper bound
on those exceptionally large ordinary trace amplitudes.

## Retaining an individual component

All the clock-front identities hold after restricting every root to
one merging component C. The scalar m_f becomes

    m_(C,f)=δ E[1_C (V_∞ f(1−V_∞)−f(0))].                            (5)

Indeed every forward and legal inverse edge remains in the component,
so (3) still holds and is dominated by the same summable majorant.
For the value of the unrestricted generator, use the marked source
occupation formula to telescope V_i f(1−V_i) along each ordinary
source in C. Its total absolute variation is bounded uniformly for
C¹ tests, because V_i decreases in [0,1]. Interchanging the source
mean and the state sum is legitimate: on simple orbit portions the
reciprocal tail above Y is O(Y^(−1/20)). For repeated labels the
remaining variation is bounded, and components not reached from any
of a fixed finite set of global minima have total source mass tending
to zero. On each of the finitely many remaining cyclic components
there are only finitely many cycle labels. This gives the same tail
argument as the [signed mass formula](../unsafe-return-weights/SIGNED_MASS.md).

On an escaping component all inverse paths are simple, so V_i is
uniformly bounded away from zero by the reciprocal packing estimate.
The test 1/(1−r) may consequently be boundedly continued in C¹
outside the occurring range. This particular edge current is zero
*exactly*, before either limit: the one-step bracket vanishes, since
(y−B) is multiplied by precisely the same J as the fibre mass.
Equivalently, writing d_x for the relative odd predecessor-basin
density, one has the exact natural incidence identity

    Σ_(x∈C, x≤T<U^k x) d_x = Σ_(x∈C, U^k x≤T<x) d_x.

Indeed ∫(x−B)⁻¹G_x(dB)=δd_x by marked source occupation at a
nonperiodic root. Taking smooth nonnegative cutoffs of 1/(1−r) which
vanish near zero and exhaust its values at every positive occurring
r, (5) gives the stronger power-tail bound in (4) with numerator
δd_x in place of H(x)/x and lower constant δPr(C): the upward tests
are bounded above by δd_x. Sources with H(x)≤T^ρ still cost o(1)
since d_x≪H(x)/x by the uniform simple-path distortion bound. This
states the full component mass forced onto the rare growing words
in natural basin units.
