# Escape is the net marked current across ordinary height thresholds

At an odd positive input x put y=U(x), a=v₂(3x+1), J=3/2^a, and
B'=(3B+1)/2^a. Thus B'/y=(B+1/3)/(x+1/3). Use the unnormalized
ordinary fibres G_x and the escape distortion measure μ in the
[zero-cylinder increment identity](STATIONARY_ZERO_FLUX.md). Define
finite positive upcross and downcross measures on [0,1] by

    U_T(f)=Σ_(x≤T<y) (x+1/3)⁻¹ ∫ f(B'/y)G_x(dB),
    D_T(f)=Σ_(y≤T<x) (x+1/3)⁻¹ ∫ f(B'/y)G_x(dB).

For f continuously differentiable on [0,1],

    lim_(T→∞) [U_T(f)−D_T(f)] = μ(f)−δ f(0),  δ=(1/2)log(4/3).        (1)

The sign and both boundary terms matter. In particular, an escaping
component forces an excess of marked upward current at *every*
sufficiently large spatial threshold. All the upward sources then
belong to the single raw dyadic class x≡3 mod 4. No control of cycle
lengths or of the number of downward edges is required in (1).

Indeed harmonic transport of the real fibres is exact,
G_y=Σ_(Ux=y) J (B↦B')_*G_x. Divide by y and note J/y=1/(x+1/3).
For every finite set of positive targets its total incoming sum with
bounded f is finite. Subtract the source sum from the pushed sum over
all x≤T. Edges with both endpoints in the truncated region cancel
by the target harmonic identity, leaving exactly U_T(f)−D_T(f).
On the other hand the same difference is the partial sum over x≤T
of the generator in (1) of the linked note. Its terms have absolute
size O_f(H(x)/x²), summable over all x. For f(0)=0 the generator
equals μ(f): in the stationary-to-physical comparison, f=O(r) near
zero suffices exactly as for the resolvent tests. Equivalently use
smooth truncations away from zero with bounded derivatives, subtract
the zero value and apply dominated convergence to the generator;
G_x has no atom at zero since every finite first letter adds a strictly
positive real offset. The constant test gives μ(1)−δ by the signed
mass identity. These cases prove (1).

## A one-class trace-amplitude obstruction

For every fixed bounded nonnegative continuous ψ of compact support
on the *absolute* real mark, compact incoming mass on the upward
boundary has the exact limit

    lim Σ_(x≤T<Ux) [1/(x+1/3)] ∫ψ(B')G_x(dB)
          = [log(3/2)/4] E ψ((3F+1)/2).                                (2)

The upcrosses are exactly (2T−1)/3<x≤T, x≡3 mod 4. Apply the
[spatial compact-mark law with its independent dyadic label](MOVING_ORDINARY_FIBRES.md)
and integrate du/u over [2/3,1]. The fraction 1/4 uses all ordinary
integer coordinates. In particular

    liminf_(T→∞) Σ_(x≤T<Ux) H(x)/(x+1/3)
                    ≥ log(3/2)/4 + μ(1).                               (3)

To see this choose 0≤ψ≤1 compactly supported in B', and 0≤f≤1
smoothly supported away from r=0. Their supports on the upward
boundary are disjoint for T large, because y>T. The compact term
converges by (2), and U_T(f) has lower limit at least μ(f) by (1)
and D_T(f)≥0. Exhaust the real mark range and (0,1] separately.
Thus any upper subsequence at the baseline in (3) excludes escape.
Convergence in spatial probability of H(x) to the stationary density
only controls bounded truncations of this upcross sum.

The same class admits an explicit uniform-integrability defect:

    lim_(M→∞) liminf_(T→∞) Σ_(x≤T<Ux, H(x)>M) H(x)/(x+1/3) ≥ μ(1).     (4)

Indeed on each bounded height-ratio interval the [full-fibre spatial
probability law](FULL_FIBRE_IN_PROBABILITY.md) with the retained dyadic
label gives the limit of the truncated trace min(H(x),M). The limit
in (2) with ψ increasing to one is also the M→∞ limit of this
truncated trace, because the stationary density has Haar mean one.
The pointwise inequality H·1_(H>M)≥H−min(H,M) together with (3)
proves (4). This is an unavoidable concentration of the ordinary
trace amplitude itself on one dyadic class if any orbit escapes.

## Polynomial spatial resolution on an escaping component

Let C be one escaping merging component, let μ_C be its contribution,
and restrict the current to C. Set γ=1−η>0 for any uniform simple-orbit
shell packing exponent η<1, for example γ=1/20. For f∈C¹[0,1] with
||f||∞≤1 and f=0 on [0,a], 0<a<1/2, one has for T≥2/a

    |U_(C,T)(f)−D_(C,T)(f)−μ_C(f)|
                 ≤ C₀ (1+||f'||∞) a^(−1/γ) T^(−γ).                    (6)

All constants apart from the test and the fixed packing choice are
absolute. By the [component generator identity](SPATIAL_CLOCK_FRONT.md),
the error consists of its terms at x>T. A nonzero bracket requires
B/x>a/2 on its relevant support, since a single relative offset step
increases B/x by at most 1/(3x). On every canonical inverse path at
such an x the entire path is simple. If all vertices of that path
exceed R, the reciprocal packing bound gives B/x≤C₁R^(−γ), uniformly,
by multiplying the relative correction factors. Choose R comparable
to a^(−1/γ), with a sufficiently large constant depending only on γ.
A positive mass of the relevant marks therefore requires an ordinary
inverse ancestor ≤R. Consequently all contributing x belong to the
union of the forward orbits from integers up to R, restricted to C.
Each such orbit is simple and has total Σ_(x>T)1/x=O(T^(−γ)). Also
H(x)≤C₂x uniformly on nonperiodic targets by natural-density source
occupation. Summing the O((1+||f'||∞)H(x)/x²) bound proves (6).

One concrete instance approximates L_C(c)=∫(1+cr)⁻¹μ_C(dr). Choose
a power g>0 with Pr(m>M)≪M^(−g) for the ordinary global minimum,
by the [first-passage failure estimate](https://rstation.ai/problems/collatz/papers/102).
Since r=1−V_∞≥1/(3m+1) on an escaping orbit, μ_C((0,b])≪b^g.
Fix a smooth cutoff χ with 0≤χ≤1, zero on [0,1] and one on [2,∞).
With a=c^(−2/g), let f_c(r)=χ(r/a)/(1+cr). For every sufficiently
large c one has, uniformly for T≥c^K,

    U_(C,T)(f_c)−D_(C,T)(f_c)=L_C(c)+O(c⁻²),                         (7)

where K is an absolute sufficiently large constant. Indeed the
cutoff costs O(a^g), ||f'_c||∞≪c+a⁻¹, and (6) applies. In particular
the [disjoint-sibling lower bound](https://github.com/GettysburgResearch/collatz/blob/88ee79f/research/critical-orbit-mellin/COMPONENT_STIELTJES.md)
forces the left side of (7) to be at least a component constant times
(log c)/c on this joint range. The lower bound now concerns a signed
current across ordinary spatial edges with marks uniformly separated
from the bounded-offset bulk, even when c grows as a power of height.
