# Full ordinary fibres at a spatially typical target

Let k_(m,f)(x)=3^m E[f(F);Z≡x mod 3^m], with stationary pair (F,Z)
and G_x as in the [periodic approximation theorem](ORDINARY_FIBRE_BESICOVITCH.md).
For every bounded continuous f on [0,∞), any ε>0, and 0<c<C<∞,

    lim_(m→∞) limsup_(T→∞) (1/T) #{x odd in [cT,CT]:
                            |G_x(f)−k_(m,f)(x)|>ε} = 0.                 (1)

In particular H(x)=G_x(1) admits the approximation (1) by the
*ordinary finite-depth densities* g_m(x). For a uniform odd target
in this shell, its unnormalized finite real measure G_x converges
in distribution, in the weak topology of finite measures, to the
random measure dσ(dB,dz)/dλ(z) sampled at ternary Haar z; retain
z and an independent odd dyadic label if desired. The limit is zero
on ternary nonunits. This is a spatial statement; controlling the
mean of unbounded exceptional target masses is a different question.

## A short common observation clock after deleting a sparse set

Put R=T^(1.00005), a=1.001, S=R^(1/a²), N=⌊log(R)/20⌋ and
H=⌈0.51log₂T⌉. Use actual first entrances at thresholds. Put
P=T^0.01. Delete targets on the forward orbits of any of the odd
integers y≤P. Uniform counting of distinct points of any single
orbit in the observation shell gives O_C(T^(19/20)) per source by
simple-orbit packing, including a transient and at most one full
period on cyclic orbits. The deleted fraction is O_C(T^(−0.04)).
Delete all other periodic targets as well: any such vertex has global
minimum >P (otherwise its cycle is among the first deletion). Their
relative number tends to zero, in fact with a power saving by the
finite-source failure bound in [the first-passage theorem](https://rstation.ai/problems/collatz/papers/102)
at threshold P and source octaves comparable to T.

Apart from a further power-small proportion, every remaining target
x is first reached from *every* odd y≤R that reaches it within H
shortcut steps. This is [FS-016, all comparable first hits](../fixed-floor-shells/QUANTITATIVE_PRESSURE.md)
on finitely many source-size shells [Y,2Y] with Y comparable to T:
R≤Y^(1+1/10000), and (log₂Y)/2≤H for T large. All later discussions
use first hits of these nonperiodic targets, so each can occur only once.

For any fixed integer M, make one more deletion: a target whose next
H shortcut steps (including the initial vertex) visit [cT,CT] more
than M times. The relative proportion of this deletion is O(exp(−c₀M))
plus o_T(1), with constants depending on the shell. Indeed within H
steps an initial label at least cT stays ≥cT/2^H. Hence, uniformly
through the entire horizon, log height differs from the initial log
height plus p log3−k log2 at clock k by o(1); here p is the odd count.
A shell visit requires that parity walk to occupy a fixed compact
interval about zero. The first H shortcut parities are fair independent
bits under dyadic Haar (fixing the very first bit for odd input), and
the whole residue dictionary of size 2^H is o(T). A negative-drift
walk with finite exponential moments visits a fixed bounded interval
an exponentially tight number of times. For example choose a fixed
downward run that takes it sufficiently far below the interval, after
which an exponential supermartingale bounds its probability of ever
returning by one half. At each visit there is thus a uniform positive
chance of at most a fixed number of further visits. The strong Markov
property proves an exponential tail. This verifies the deletion bound.

Call the retained set E_(T,M). On *any* ordinary orbit the total
number of retained shell targets is at most M if the orbit begins at
some y≤R. In fact any such hit is within H shortcut steps of y by
FS-016. From its first retained target there are at most M remaining
shell vertices through that horizon by the last deletion. On an orbit
from infinity every shell visit is after crossing R. No retained
target can occur after crossing P by the first deletion.

## Tightness in spatial probability

We claim, for every fixed M and b>2,

    limsup_(T→∞) (1/T) Σ_(x∈E_(T,M)) G_x((b,∞)) ≪_s (b−1)^(−s),       (2)

for any fixed 0<s<1. Bounds before the limit can depend on M. Use
the marked source occupation formula, or first bound the open tail by
a continuous cutoff supported above b−1/4. Each source orbit costs
at most a constant times M here. From R to S the proof of
[critical inverse-mark tightness](INVERSE_MARK_TIGHTNESS.md) applies
with this cap even without the inverse mark weight. More explicitly
the prehistory mark at shell points can be reset at entry to R with
absolute error o(1) off probability o(1); then the entire selected
segment can transfer in total variation through its exact landing
label. The cap applies also to every proxy trajectory after its entry
at R. On the original reciprocal proxy in [R^a,R^(a²)] its initial
passage down to S occurs within N steps off probability o(1). Before
that passage log height stays within o(1) of the continuous source
log height plus the iid multiplier log on the good coupled event.
The true proxy prefix mark β_j dominates the reset mark. At each
j≤N the condition of a shell visit therefore restricts the independent
log height to an interval of length O(1); its full interval has
length (a²−a)log R. The iid mark β_j has a uniformly bounded s-moment,
so the total expected number of visits with β_j>b−1 is O((b−1)^(−s)).
The good-event restriction can be dropped in this last upper bound.

After crossing S, down to P, use the same power ladder s,s^(1/a)
as in the critical-weight proof. The number of levels is bounded
independently of T here. Off a set of source probability o(1), every
intermediate height is at most S^(1.0004)=o(T). A failed passage
costs o(1) by the landing estimates, since its contribution is capped.
There are no later retained targets. This proves (2).

Since the nonretained relative proportion is O(exp(−c₀M))+o_T(1),
Markov's inequality on (2), followed by b→∞ and M→∞, proves tightness
of the real tails in *spatial probability*. Compact approximations
of f now give (1) by the periodic approximation theorem. The periodic
stationary tail has spatial mean bounded by ||f||∞ Pr(F>b) for each
fixed precision, which vanishes as b grows. For the finite-measure
assertion use compactly supported bounded Lipschitz tests from a
countable convergence-determining family together with total mass and
the preceding tight-tail bound. These identify the joint weak limit
by finite-vector convergence on each finite product quotient, as in
the periodic approximation proof.
