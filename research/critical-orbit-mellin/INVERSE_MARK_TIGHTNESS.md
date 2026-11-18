# Critical inverse-mark tightness on moving ordinary shells

Keep the [moving-ordinary-fibre notation and normalization](MOVING_ORDINARY_FIBRES.md).
For every fixed 0<c<C<∞,

    lim_(b→∞) limsup_(T→∞) T⁻¹ Σ_(cT≤x≤CT, odd)
                  ∫_(B>b) (1+B)⁻¹ G_x(dB) = 0.                        (1)

Thus the compact-offset limit also gives convergence against bounded
continuous tests on the whole real mark axis after multiplying by
(1+B)⁻¹, locally in positive x/T. This statement includes all cyclic
laps. Spatial convergence on fixed bounded marks and the separate
Stieltjes budget at each real scale alone would bound only powers
strictly above one by summing over dyadic mark bands.

Use the marked occupation formula (2) of the linked note. Constants
below can depend on c,C. For an arbitrary orbit use r_i=1−V_i and
B_i=x_i r_i. The following uniform estimates explain why the critical
weight is available. Restrict attention to indices x_i∈[cT,CT]. At
the k-th such index, prior counted steps each increased r by at least
V_i/(3CT+1), since V decreases. Thus V_i/(1+B_i)≤C'/k and a segment
with at most N steps costs O(log(2+N)). Without limiting the segment
length its cost is O(log(2+T)): at selected indices Δr_i=V_i/(3x_i+1)
and V_i/(1+B_i)≤C'TΔr_i/(1+Tr_i). Across one of the disjoint intervals
[r_i,r_i+Δr_i] the denominator changes by at most a constant factor,
since its absolute increase is O(1). Integration proves the bound. If
the selected visits are after a step from the global minimum m, then
r_i≥1/(3m+1), and the same integration costs at most O(log(2+m)).

## Near the observation shell

Put a=1.001, R=T^a, S=T^(1/a), L=log R and N=⌊L/20⌋. Passage from
R to S exceeds N steps with probability O(R^(−γ)) in the limiting
source law for some γ>0. Here and below use actual successful landing
labels, or charge a passage failure to the power-small failure atom
of the [setwise first-landing bound, Theorem 1](https://rstation.ai/problems/collatz/papers/102).
For detail, for a landing at an arbitrary s between S and R, all but
O(s^(1−γ₀)) labels y≤s pass below s^(1/a²) in at most ⌊log(s)/20⌋
steps. Until passage all inputs exceed s^(1/a²), so the additive
correction to log height is O((log s)/s^(1/a²)). Uniformly through
this horizon the centered iid geometric sums have size at most ε log s
except on probability O(s^(−γ₀)), for any fixed ε>0. The dyadic word
count transfers this bound to uniform odd labels y≤s, with bit budget
4⌊log(s)/20⌋+O(1). The expected log descent ℓ(log s)/20 exceeds
(1−a⁻²)log s with room for fixed ε. The setwise bound at s, with its
factor exp(O(√log s)), preserves a positive power saving. The same
argument controls an arbitrary lower threshold between s^(1/a²) and
s. In particular S=R^(1/a²) is covered. Before R there is no visit
to [cT,CT] once T is large.

The exceptional event costs o(1) by the O(log T) bound. On the
remaining segment there are at most N visits. Set the initial mark
at Y_R to zero. The prehistory estimate (3) of the moving-fibre note
holds outside O((log T)^(−γ₁)) for some γ₁>0, using the stated rate
in first-passage stabilization on the finitely many power-scale
segments (or the polynomial estimates just used). It changes each
mark at a shell visit by o(1/N). Its exceptional event costs o(1)
by the O(log N) bound. For the upper tail it now suffices to count
weight with B>b−1 in the new, zero-initial-mark segment. Its capped
length-N inverse-weighted sum is uniformly O(log N), so the
O(L^(−γ₁)) total-variation comparison with the reciprocal source
in [R^a,R^(a²)] has error o(1). In making that comparison one may
omit the V_i factor only on the proxy after the transfer: the
artificial segment's own V_i dominates the original V_i.

On this short source the initial passage to S occurs within N steps
outside exponentially small probability in L, by the same dyadic
estimate. The local mark after R is bounded above by the forward
affine offset β_j started at zero on the original source; hence a
contributing shell visit has β_j>b−1. Before first entry at S and
through N steps, V_j≥1−O(N/S), so log x_j differs from log z+D_j by
o(1), where z is the proxy input and D_j=log J_j. Use the continuous
independent log-uniform h and iid letters as in the moving-fibre
proof. The rounding error in log z is o(1). For any fixed first j
letters the shell condition locates h in an interval of bounded
length, of probability O(1/L). Also β_j has bounded s-moment,
uniformly in j, for each fixed 0<s<1, by reversal of the finite iid
perpetuity. Dropping the weight and summing through N gives an upper
bound O((b−1)^(−s)) for b>2. This handles all visits before S.

## Later returns

Let M=(log T)^D, with D chosen sufficiently large. Starting at S,
use successive power thresholds s,s^(1/a) down to M (shorten the
last gap). Except on O(M^(−γ₂)) source probability, each segment takes
at most (log s)/20 steps and its intermediate heights stay below
s^(1+0.0004). Indeed while the threshold has not been crossed, the
same uniform centered-sum bound and negligible affine correction give
log height ≤(1+ε')log s for any fixed ε'>0 outside O(s^(−γ₃)) on
limiting landing labels. Sum these bounds over the geometric sequence
of log thresholds, decreasing the power if necessary. Since
S^(1.0004)=o(T), no such good intermediate point is in the observation
shell. All bad events combined cost O(M^(−γ₂)log T)=o(1) upon fixing D.

After entry at M, except possibly at the entry point itself (below
the shell), r_i≥1/(3M+1). Up to the first repeated state the uniform
simple-orbit packing bound gives O(T^(19/20)) selected labels. Their
total weighted cost is O(M T^(−1/20))=o(1). This includes every
later visit of an escaping orbit. At any remaining repeated visit
the orbit has already passed through its global minimum m, either
on the transient prefix or on the first completed cycle. The weight
of these visits is O(log(2+m)) as proved above. The setwise landing
failure bound implies Pr(m>A)≤C A^(−γ₄) in the limiting ordinary
source law, hence the logarithmic majorant is uniformly integrable
there. More explicitly for m>A sum the dyadic tail bounds, or invoke
natural-density minimum cells and their finite-interval restrictions.
For m≤A, any cycles reached are among the finitely many eventual
cycles of the integers up to A. They have no vertex in [cT,CT] for
large T with A fixed. The finite-interval version of this domination
can also be used when taking the source mean: the entire observable
is O(log(2+T)) for fixed T, so the contribution of m>K in the defining
mean is O(log(2+T) K^(−γ₄)), tending to zero as K→∞ first. Thus all
repeated-label costs tend to zero as T→∞.

Adding the three time ranges proves (1). In particular no assumption
on how high a cycle of a given minimum might climb enters the argument.
