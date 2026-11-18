# The physical clock and path information under the canonical inverse law

Fix any positive ordinary odd unit t and start the harmonic inverse
walk at X₀=t. Let a_i=v₂(3X_i+1), S_q=sum_(i=1)^q a_i, and let p_q
be the probability the walk assigns to its sampled length-q word. Then

    S_q/q → 2,
    log X_q/q → log(4/3),
    −log p_q/q → log(4/3)                                           (1)

in probability as q→∞. All logarithms in this note are natural. The
limits concern a fixed but arbitrary root; the proof gives no uniform
onset over moving initial roots and no moment bound on a single
physical parent.

Use h=(2/3)dμ/dλ in its ordinary harmonic representative. The inverse
transition for a compatible exponent a is J_a h(x)/h(t), J_a=3/2^a.
The preceding empirical return theorem gives convergence in probability
of the random state occupation on E=Z₂^odd×Z₃ to ν=Haar_odd×μ.

[Canonical state occupation and normalization](CANONICAL-RETURN.md).

## 1. The endpoint density costs sublinear information

On ternary units put b(z)=1/h(z), with b=0 where h=+∞; also set b=0 on
the clopen nonunit region. This is bounded and upper semicontinuous.
The mean empirical average of b converges to exactly ν(b)=1: its
qth expectation is L^q 1_units(t)/h(t), and (4) in the return theorem
applies to the unit indicator of Haar mean 2/3. In fact the augmented
random empirical measures of (state,b(state)) converge in probability
to the graph law of (state,b(state)) under ν. Indeed any subsequential
limit of their laws on the compact product has first marginal ν almost
surely and is supported on the closed hypograph u≤b(z). The limiting
expected integral of the continuous coordinate u is ν(b). Consequently
there is no deficit in that inequality almost surely, which forces the
entire graph law. In particular the occupation fraction where h>M
converges in probability to ν(h>M) at continuity thresholds, and that
limiting fraction tends to zero as M increases.

We claim log h(X_q)/q→0 in probability. Its negative part is uniformly
bounded before division since h≥c>0 on units. If h(X_q)>exp(εq),
the conditional probability that h drops below exp(εq/2) after s
further steps is at most exp(−εq/2) L^s1(X_q)≤exp(−εq/2)2^s.
Here the unrestricted one-step total J is at most 2. Take
δ=min(1,ε/(4 log 2)) and sum this bound for s≤δq. Except with
probability tending to zero, a large value at q then forces h>M
throughout [q,q+floor(δq)]. For fixed sufficiently large continuity
threshold M this contradicts empirical occupation with probability
tending to one, since ν(h>M)<δ/(2(1+δ)). This proves the claim.

The telescoping path formula is exact:

    p_q=3^q 2^(−S_q) h(X_q)/h(t).                                   (2)

On h(X_q)≤exp(q), discard integer compatibility in (2) to upper-bound
the probability of S_q≥16q by exp(q)3^q P_geom(S_q≥16q)/h(t),
where the comparison uses iid geometric exponents. Its exponential
moment E_geom[(3/2)^S_q]=3^q makes the bound tend to zero
(e·9·(2/3)^16<1). Thus S_q≤16q with probability tending to one.

## 2. A conditional code for the sampled inverse word

Fix K≥2, m≥1 and a smoothing parameter 0<τ<1. Under stationary ν,
form the probability table for the capped exponent B=min(a,K) given
the m-digit ternary residue of the forward target Y=U(X). Smooth each
row by mixing in τ times the uniform law on the K capped labels. At
each inverse step use the current target residue and this table to
encode B. If B=K, encode the excess j=a−K with the probability
1/((j+1)(j+2)), j≥0. This defines subprobabilities Q_t(w) on legal
length-q words; incompatible continuations can be discarded. Hence

    P_t{−log p_q > −log Q_t(w)+εq} ≤ exp(−εq),                     (3)

by summing p_q<exp(−εq)Q_t(w) on that event.

The capped per-letter code cost is bounded and continuous as a function
of the current child state except possibly at the ν-null dyadic point
−1/3, where the valuation is undefined. Its empirical average
converges in probability to the stationary cross entropy. This is at
most H_ν(B | Y mod 3^m)−log(1−τ). As m increases the finite-label
conditional entropies converge to H_ν(B | Y₃), by martingale
convergence; Y₃ denotes the complete ternary coordinate only.
This last quantity is at most H_ν(a | Y₃).

To evaluate it, under ν the child's ternary state has law μ independently
of its geometric exponent. For each a the change of variables
Y₃=F_a(X₃) shows the stationary conditional probability of a given
Y₃ is J_a h(X₃)/h(Y₃) on the corresponding branch, zero elsewhere.
Integrating its negative logarithm gives

    H_ν(a | Y₃)=2 log 2−log 3.

Indeed both endpoint and child have the same ternary marginal μ, and
log h is integrable for μ: its negative part is bounded on units and
h is in L^r(Haar) for 1<r<2. The two density logarithms cancel.

Let N_K count letters a_i≥K. By the empirical theorem N_K/q→2^(1−K)
in probability. On S_q≤16q the excess code costs at most

    2 N_K log(2+16q/N_K),

using concavity of log and zero cost if N_K=0. After division by q
the upper bound in probability tends to zero as K grows. Take K large,
then m large and τ small in (3). The conclusion is that the probability
of −log p_q/q exceeding 2 log 2−log 3+ε tends to zero for every ε>0.

By (2) and the established endpoint bound, this gives the same upper
bound 2 for S_q/q in probability after solving for S_q. The matching
lower bound follows from empirical convergence of min(a_i,K), whose
stationary means increase to 2. Equation (2) now also gives the
information limit in (1).

Finally, along the actual inverse path

    log X_q = log t + S_q log 2 − q log 3
              − sum_(i=1)^q log(1+1/(3X_i)).

The correction is uniformly bounded along every simple segment by
translated orbit packing. If t belongs to a cycle, the probability
of staying on it for j full turns is J_c^j, tending to zero. After
the inverse path first leaves the cycle it is simple. Thus the correction
divided by q tends to zero almost surely, giving the physical limit.

[Simple segment distortion](ORDINARY-DENSITIES.md).
