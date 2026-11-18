# An exact logarithmic endpoint mean for the nontrivial cycles

**Proposed, source-qualified.** This identifies the endpoint constant in the
[two-scale ordinary test](TWO_SCALE_TEST.md). Let H_Q(epsilon) be the raw phase-zero
sum J_w/t over odd targets 1<t<=2·3^Q whose distortion F_w/t is at
least 1-epsilon. Let C range over the nontrivial ordinary odd cycles,
d_C their odd periods, J_C their positive lap multipliers, and p_C the
ordinary densities of their predecessor basins. Write delta=ln(4/3)/2.
For all sufficiently small epsilon>0 the extended limit
H(epsilon)=lim_Q H_Q(epsilon) exists. Moreover its logarithmic mean is

    lim_(T→∞) (1/T) ∫_(s₀)^(s₀+T) exp(s) H(exp(-s)) ds
      = delta ∑_C d_C p_C/ln(1/J_C),

for any sufficiently large fixed s₀. If there are infinitely many
nontrivial cycles, H(epsilon)=+infinity at all fixed sufficiently
small epsilon. If none exist, H_Q(epsilon)=0 at all these thresholds
and every depth, irrespective of the existence of escaping trajectories.

## The marked first-hit limit

At a fixed cyclic t let W_t be the product of (1+1/(3u))^(-1) over
odd inputs before the first visit to t; set it to zero outside the
predecessor basin P(t). Use the ordinary limiting odd law, equivalently
its normalized logarithmic means here. No equal weighting between
different basins is assumed. All simple first-hit segments have
W_t>=c₀ for one absolute c₀>0 by uniform reciprocal packing. The same
bound holds for a single cycle lap because its input list is distinct.
[Simple-segment bound](HARMONIC_OFFSET_CONE.md)

The measures at exact first-hit depth q, with mass J_w/t placed at the
corresponding W_t, tend weakly to the finite measure

    nu_t(f) = delta E[W_t f(W_t) 1_(P(t))].

For total masses this is the canonical visit formula combined with
the first-hit subtraction g_q^*(t)=g_q(t)-J_C g_(q-d_C)(t) and
ordinary every-depth convergence. To obtain the marked result, fix
k>=d_C and use the last k steps of the forward first-hit path as inverse
cylinders. Each compatible cylinder not revisiting t has a nonperiodic
odd state x at depth k. Indeed a cyclic state with a first-hit clock
to t has clock at most d_C-1. For a word w from x to t, the mass at
depth q>=k on this cylinder tends to J_w g(x)/t as q→∞. At nonperiodic
x the visit formula gives g(x)=delta x E W_x. Multiplicativity then
makes J_w g(x)/t exactly delta E[W_t 1_(P(x))]. The predecessor basins
here are disjoint. They cover P(t) up to density zero: sources less
than k odd steps from t have zero density, by the fixed-depth
polylogarithmic count; inverse first-hit cylinders exhaust the natural
law (or first strip off the finitely many cycle vertices and use
first entrance at a nonperiodic odd state). For clarity, countable
additivity here is for the limiting path law: tightness of fixed
inverse suffixes follows also by fixing a first odd landing bound B,
whose failure tends to zero, and using its finitely many continuations
to t. The exceptional continuations of depth less than k are controlled
as follows. The possible prefixes with a last k-step ancestor above
H have all original odd states <=H in the finite union of first-hit
paths from those states to t. Taking the source's first landing
at H therefore leaves a fixed finite set of possible k-step ancestors
except when that landing is itself fewer than k steps from t. Those
few-depth states have O_k((1+log H)^k) labels up to H, so their total
first-landing mass tends to zero by the setwise bound of paper 102.
[Canonical visit formula](../unsafe-return-weights/SIGNED_MASS.md)
· [First-hit uniform bounds](../unsafe-return-weights/INVERSE_AGE_LAWS.md)
· [Setwise landing bounds](https://rstation.ai/problems/collatz/papers/102/v1)

Consequently the limiting cylinder masses sum to the total mass, and
pointwise convergence on these countably many cylinders is tight.
The omitted correction preceding the last k odd inputs tends to zero
uniformly as k grows: for any fixed H, a state <=H reaching t has a
fixed first-hit clock, so once k exceeds their finite maximum all
preceding odd states exceed H and are distinct. Apply the packing
tail. This proves the asserted weak limit. It is nonatomic: on
P(x) at any fixed allowed k>=d_C, W_t is a fixed positive multiple
of W_x, and the first-hit residue conditional on a nonperiodic unit
x is nonatomic by its boundedly equivalent natural/canonical boundary
and the full lower dimension of that fibre. Nonunit x have zero basin
density. [Natural first-hit law and fibre dimension](../terminal-residue/SINGULAR_FIBRES.md)

## Summing the full laps

For epsilon<c₀ every marked path repeats a vertex: otherwise its
reciprocal correction is at least c₀. Its target lies on a nontrivial
cycle, since t=1 was excluded. Any path to a given cyclic t splits
uniquely into a first hit followed by j>=0 laps. The lap multiplier
equals its correction product because its two endpoint states agree.
The unrestricted weight from such paths at depth Q is bounded by
K p_C J_C^j uniformly in Q, by the first-hit bound above. Thus for
each fixed t its limiting contribution is

    H_t(epsilon) = sum_(j>=0) J_C^j nu_t({W : W J_C^j<=epsilon}).

The indicator boundaries have zero mass by nonatomicity. Finite sums
over targets commute with the limit. If j₀ is the least integer with
J_C^j₀<=epsilon then J_C^j₀>=c₀ epsilon, and every path with at
least j₀ laps qualifies. At a fixed target the limiting mass is
therefore bounded below by c epsilon p_C/(1-J_C). Conversely every
qualifying j satisfies J_C^j<=epsilon/c₀, giving the matching upper
bound C epsilon p_C/(1-J_C). For cycle minimum m_C one has
p_C>=c/m_C and 1-J_C<=d_C/(3m_C). Thus each fixed cycle's whole
contribution divided by epsilon is bounded below by an absolute
positive constant. For infinitely many cycles, finite-subset lower
bounds already force the unnormalized depth limit to be infinite.

In the finite case put b=ln(1/J_C) and s=-ln epsilon>ln(1/c₀).
For each W set v=-ln W in [0,ln(1/c₀)]. Summing the geometric series
of admissible laps expresses exp(s)H_t(exp(-s)) as the integral of

    exp(v) exp(-[b ceil((s-v)/b)-(s-v)])/(1-exp(-b))

against nu_t. This is periodic in s with period b, and its mean
over a period is exp(v)/b. Therefore the mean at t equals
(1/b)∫ W^(-1) dnu_t=delta p_C/b. There are d_C targets on C.
Summing proves the formula, without requiring commensurable periods
from different cycles.
