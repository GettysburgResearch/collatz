# A fixed-root functional central limit theorem at deterministic inverse depth

For every fixed positive odd unit root t of the canonical inverse law,
write d=log(4/3), S_i for the sum of inverse exponents, and X_i for
the odd states. The following two processes, linearly interpolated,
converge jointly in distribution on C[0,1] to the same standard
Brownian motion, as Q→∞:

    (S_(⌊Qu⌋)−2⌊Qu⌋)/√(2Q),
    (log X_(⌊Qu⌋)−d⌊Qu⌋)/(log 2 √(2Q)),       0≤u≤1.

The inference uses Leen's forward fate–clock invariance principle, in
particular its joint independence from terminal labels on arithmetic
progressions. The true entrance law at infinity transports this functional
result to the inverse boundary; the last-visit depths are then inverted.
The convergence is stable against each fixed bounded inverse-path observable.
At finitely many distinct positive times the realized prefix information
centered by d⌊Qu⌋ and divided by log 2 √(2Q) has the same joint limit.

[Leen, Brownian descent, terminal data, arithmetic progressions and clock dictionary](https://doi.org/10.5281/zenodo.23252395)
· [Last-visit and density-boundary identifications](ALMOST-SURE.md)
· [Tao stabilization to a short logarithmic source](ITERATED-LOG-BOUND.md).

## Exact frozen entrance

At nonperiodic t use the density boundary Q_t and define n(r) as the
last depth with X_i≤r, taking −1 if no such state exists. Y_r=X_(n(r))
for r≥t. For each label y≤R one has exactly

    Q_t(Y_R=y) = μ_R(y) 1_{y reaches t}/d_t,       R≥t.

Indeed the finite-depth cylinder bound gives ≤ on the right for every
label that reaches t. Others have zero Q_t mass. The sum of the right
side is one: for any odd source its first landing at or below R reaches
t if and only if the source reaches t. Here μ_R is the limiting odd
law with failure distinguished and d_t is the relative odd basin
density. Thus there is equality coordinate by coordinate. The proxy
in the stabilization estimate uses the default 1; changing this default
to a failure symbol costs at most the respective failure masses. The
limiting failure mass tends to zero by the setwise first-landing bound,
and the proxy failure probability tends to zero by Tao's first-passage
estimate. Consequently the law of Y_R under Q_t differs by o(1) in
total variation from the law of the first odd ≤R from z=Q_(R^a),
conditionally on z reaching t. Here a=1.001 and z is sampled with
reciprocal weights on odd [R^a,R^(a²)]. For an entire profile below R
one uses the deterministic forward orbit of this label up to its first
t, so the same total variation bound applies.

More precisely, for 1≤r≤R with r≥t the corresponding value n(r) on
that orbit is the odd first-hit time of t from z minus the odd first
passage time to ≤r. For 1≤r<t the value depends only on the finite
suffix after the first entry below t, if it is attained at all. The
possible entering states ≤t form a finite set, and their first-hit
suffixes to t have bounded lengths. Thus the small-threshold segment
is bounded independently of the incoming source. This suffices on
dividing by √log R.

## The Brownian last-visit process

Put L=log R and c=log z/L∈[a,a²]. On the short source conditioned to
hit t, Leen's theorem gives the normalized centered odd first-passage
profile in the source logarithm variable s as standard Brownian motion
W(s), independent of c in the limit. Here s runs from 0 to 1 and the
threshold is z^(1−s); the odd clock has drift 1/d per unit downward
log height and variance coefficient σ_J²=2(log 2)²/d³. In detail,
apply the forward Brownian terminal-data theorem on the odd progression
with the terminal label 1_{source reaches t}, whose limiting mass is
positive. The shortcut-to-odd clock dictionary costs at most
O(log(2+J_*)) uniformly in the profile, where J_* is the odd descent
clock to the minimum, O_P(log z) by the same theorem and dictionary.
The normalization conversion is σ_J=σ/log₂3. On the hit-t event,
first arrival at t and arrival at the global minimum differ from first
entry below t by bounded clocks after that entry: its label belongs
to a fixed finite set and its subsequent orbit is deterministic.
This justifies the capped profile convention at the bottom. To obtain
the logarithmically weighted short-source law jointly with c, partial
summation transfers the odd natural-source convergence to each fixed
subinterval of [a,a²] in log z/L. Its reciprocal mass tends to the
subinterval's length divided by a²−a. Partition this bounded interval
to obtain the independent uniform limiting c and Brownian profile.

Use the difference of the source's endpoint clock and its clock at
s=1−u/c, corresponding to threshold exp(uL). By the exact entrance
description, it follows under Q_t that

    (n(exp(uL))−uL/d)/(σ_J √L)  ⇒  √c (W(1)−W(1−u/c)),   0≤u≤1.

Evaluation at these continuously varying arguments is continuous at
continuous profiles. Given c, the displayed limit is standard Brownian
motion in u by reversal of Brownian increments and scaling. Thus the
mixture is also standard Brownian motion. The limit is in the uniform
topology with continuous limit, allowing the original step profiles.

Conditioning Q_t on a fixed prefix changes the root to its terminal
state x and adds a fixed prefix to the last-visit depths once the
threshold exceeds all prefix states. The smaller thresholds have bounded
last depths on each individual path since only finitely many labels
are involved. Applying the same limit at x and approximating bounded
path functions in L¹ by finite-prefix conditional expectations gives
stable convergence. In particular the bounded density dP_t/dQ_t
transfers the limit to the canonical law. For periodic t, condition
on its almost surely finite first exit from the inverse cycle; the same
finite-prefix argument transfers the result. Stability for all roots
also follows by conditioning the canonical Markov walk on fixed prefixes.

## Inverting the last-visit clock

Write K_i=min_(j≥i) log X_j. Then K_i≤v exactly when i≤n(exp(v)).
For the inversion on [0,1] first take the last-visit theorem on an
enlarged fixed time interval, by rescaling L. With L=dQ its centered
depth fluctuation divided by √Q converges to σ_J√d W. The generalized
inverse of this nondecreasing clock has centered fluctuation of opposite
sign. Explicitly, if
n(exp(dQu))=Qu+√Q Z_Q(u), the inverse argument for i=⌊Qv⌋ lies
v+O_P(1/√Q) uniformly, since Z_Q is tight in sup norm. Bracket this
argument using the two monotone sides of its inverse; the jumps of the
centered profile are o_P(1) and its modulus on O_P(1/√Q) intervals
is o_P(1) by convergence to a continuous limit. Thus
(K_(⌊Qv⌋)−dQv)/√Q converges to −d σ_J√d W(v). The initial bounded
threshold convention costs o(1). Since d σ_J√d=√2 log 2, this is
the claimed Brownian coefficient.

To replace K_i by log X_i, every product of m subsequent inverse
multipliers is ≤3B_i by the positive real affine series. Along that
segment the summed logarithmic affine correction is bounded by a finite
path constant since Σ 1/X_i<∞ almost surely. Hence
0≤log X_i−K_i≤max(0,log(3B_i))+O_path(1). The real-tail maximum law
gives O_path(log(2+Q)) simultaneously for i≤Q. Finally the exact
affine log identity gives log X_i−di=(log 2)(S_i−2i)+O_path(1)
uniformly in i. The common Brownian sign has no effect on its law.

For the information assertion the one-time endpoint h(X_i) is tight
at fixed root as i→∞. Indeed b=1/h is bounded upper semicontinuous on
the units. The arithmetic endpoint converges weakly to the stationary
law; E b(X_i)=L^i 1_units(t)/h(t)→1 equals its stationary expectation.
A subsequential limit of (endpoint,b(endpoint)) lies in the closed
hypograph of b, with the stated marginal and equal coordinate mean,
so it is the stationary graph law. That law puts no mass on b=0.
Consequently log h(X_(⌊Qu⌋))/√Q→0 in probability at each u>0,
and the exact telescoping prefix probability gives the finite-dimensional
claim.

[Real-tail maximum and physical affine series](REAL-TAILS.md)
· [Instantaneous endpoint limits](INSTANTANEOUS-RETURN.md).
