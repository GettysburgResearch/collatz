# Finite-window canonical entropy tradeoff and height growth

2026-11-24 continuation of PR189 (parent acbb126157c47c1e4de751ba0f9907f0de4c2594).
**PROPOSED written proof; Collatz remains OPEN.** Unlike S2, the following
inequality requires neither a rational scalar nor a stationary limit.
It controls the actual law at logarithmic and square-root precisions.

## 1. Setup and exact mean budgets

Fix one actual injective positive odd orbit q_i, gaps g_i, and actual scalar
h_i from pinned PR182 at f94a2ae1caba9a1857feda892ee1779695eea9d2,
research/carry-tower-round10-20261123/ACTUAL_SCALAR_FORMALIZATION.md.
Use p_i in (1/2,3/2], integer k_i>=0 and b_i=3p_i-p_(i+1) in {1,2,3},
so g_i+k_(i+1)=b_i+3k_i. No rationality or finite phase set is assumed.
The b_i-1 are the canonical ternary digits of p_0-1/2, with right-closed
endpoint convention, as independently used in PR188 at
beed685ab713923191ae40c9559bf7400298d2d3,
research/scalar-carry-cocycle-20261124/SCALAR_COCYCLE.md.

Let alpha=log_2 3 and beta_*=(alpha-1)/2. From
V_i=log_2 q_i-h_i>=-1 and its exact difference,

    V_(i+1)-V_i = log_2(3+1/q_i)-2h_i,

the distinct-state harmonic bound gives, for every M>=1,

    sum_{i<M} h_i <= alpha M/2 + C_0(1+log(M+1)),
    sum_{i<M} k_i <= beta_* M + C_0(1+log(M+1)).

The constant may depend on the fixed original source. In particular this
does not assume any arithmetic on the infinite scalar's digits.

For N>=2 and 1<=m<=N/2, choose J uniformly from {0,...,N-m}, with
L=N-m+1. Define the actual blocks B=(b_J,...,b_(J+m-1)),
K=(k_J,...,k_(J+m)), G=(g_J,...,g_(J+m-1)). Put

    A=E sum_{i=0}^{m-1} b_(J+i),
    C=E sum_{i=0}^{m-1} k_(J+i),
    E_end=E k_(J+m),
    R=1 + m(m+log(N+1))/L.

Summing b=3p-p' telescopes, giving
A+2C=2 E sum_{i=0}^{m-1} h_(J+i)+E(p_J-p_(J+m)).
Every source index is counted at most m times and |p_J-p_(J+m)|<1.
Consequently

    A+2C <= alpha m + O_{q_0}(R),
    C <= beta_* m + O_{q_0}(R),
    E_end <= (sum_{i=0}^N k_i)/L = O_{q_0}(1).

The second follows from A>=m. These are literal sliding-window estimates.

## 2. Conditional KL on the actual canonical word

Let Q be the product law of m+1 independent nonnegative geometric variables
with mean beta_*, NOT a law substituted for the actual orbit.
Write

    tau=log((1+beta_*)/beta_*),
    r=beta_* /(1+beta_*)^2,
    Psi(x)=(1+x)log(1+x)-x log x.

The cross-entropy of the actual K with Q is exactly
(m+1)log(1+beta_*)+tau(C+E_end).

Conditional on any fixed B=w, the actual carry vector is supported on the
event E_w that all edges with b=1 avoid a transition 0 -> positive.
This follows directly from g>=1 and the exact carry recurrence.
Select the more numerous parity of the b=1 edge indices. The selected
edges are disjoint, and their number is at least half the count n_1(w)
of ones in w. Under the product reference law, each avoids the forbidden
transition with probability 1-r. Thus

    Q(E_w) <= (1-r)^(n_1(w)/2).

By conditioning Q on E_w, the relative entropy
D(P(K|B=w)||Q) is at least -log Q(E_w). Average over the actual B law,
not over a fresh phase distribution. Since n_1(w)>=2m-sum w, we obtain

    H(K|B) <= (m+1)log(1+beta_*)+tau(C+E_end)
               + (2m-A)/2 log(1-r).

Here the sign is important: log(1-r)<0. Substituting
2m-A >= (2-alpha)m+2C-O(R), and then
C<=beta_* m+O(R), is legitimate because
tau+log(1-r)>0 (the exponential of this coefficient is
(1+beta_*+beta_*^2)/(beta_*+beta_*^2)>1).

Since (2-alpha)/2+beta_*=1/2 and G is a deterministic function of (B,K),

    H(G) <= H(B) + c_* m + O_{q_0}(R),                 (F1)
    c_* = Psi(beta_*) + (1/2) log(1-r),
    d_* = c_*/log 3 = 0.541528190506944... .

This is a finite bound on the actual fixed-source window. In particular
the constant is independent of m,N and the canonical word distribution.

## 3. Same-law finite collision consequence

Let hat_pi_(N,m) be the law of q_(J+m) and pi_N the uniform law
on q_0,...,q_N. The complete affine word identity determines q_(J+m)
modulo 3^m from G, so its residue entropy is bounded by H(G).
Projection and Jensen imply

    Col_m(pi_N) >= (L/(N+1))^2
       exp[-H(B)-c_*m-O_{q_0}(R)].                   (F2)

For the exact moving inverse law of PR185 at
2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d,
research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md,
the same lower bound holds multiplied by (v_0/C_flow)^2, using its
pointwise domination under its original harmonic-flow hypothesis.
No new mixing claim or probability-law replacement is made.

If the actual scalar is rational, discard only the finite actual prefix
needed to clear factors of three in its denominator. The canonical word
is periodic with L_phase possible phases, so H(B)<=log L_phase.
For m^2=O(N) this yields the much stronger finite same-source lower bound

    Col_m(pi_N) >= c(q_0,L_phase,T) 3^(-d_*m),
    1<=m<=N/2, m^2<=T N,

and likewise for zeta under the pinned flow. Constants may depend on
the fixed source and its phase cycle. This is a genuine growing-precision
consequence, not just S2's stationary-limit bound.

If one could establish universal rationality of the actual scalar
(not necessarily triadic membership), then a same-law collision upper
bound at any fixed exponent >d_* would suffice for escape exclusion.
It still would not exclude nontrivial cycles, and neither ingredient
is proved here.

## 4. Ordinary height consequence and the new PR188 combination

Put H_N=1+max_{0<=i<=N}q_i. If H_N is at most polynomial in N along
a subsequence, set m=ceil(log_3 H_N)=O(log N). All endpoints
q_m,...,q_N are distinct and below 3^m. Their residue entropy is
exactly log(N-m+1), so (F1) gives

    log(N-m+1) <= H(B)+d_* log H_N+O_{q_0}(1).       (F3)

The same inequality applies to any subsequence with a specified fixed
polynomial upper bound; its constants may depend on that bound.

**F4 (rational-phase actual growth):** For a fixed escaping orbit with
rational scalar, H(B)<=log L_phase after the finite shift, hence

    H_N >= c(q_0,L_phase) (N+1)^(1/d_*),
    1/d_* = 1.846625932924865... .

Indeed if H_N already exceeds N^(2/d_*), the claim is immediate;
otherwise m=O(log N) and (F3) applies. The initial finite shift only
changes constants. This is a pointwise running-maximum restriction,
not a claim that every q_N grows at that rate.

**F5 (general low-complexity phases):** If P_b(m) denotes the number of
distinct length-m words in the one actual canonical sequence b, then
H(B)<=log P_b(m). If log P_b(m)=o(m), (F3) implies

    liminf_{N->infty} log H_N / log N >= 1/d_*.

This includes periodic and any subexponential canonical word complexity;
no such complexity hypothesis is asserted universally. If H_N<=N^s
on an unbounded subsequence, F3 conversely forces
log P_b(m)/(m log 3) >= 1/s - d_* - o(1) on the corresponding m.

Combine with the exact SC2 carry-cocycle height estimate from the
new PR188, head beed685ab713923191ae40c9559bf7400298d2d3,
SCALAR_COCYCLE.md:

    M_N <= D_N(q_0+N/3)(3/2+log_2 M_N/3)^(4/3),

where M_N=max q_i and D_N is the largest canonical coefficient drawup
3^(i-j)/2^(sum_{j<=t<i} b_t) over intervals [j,i) of the prefix.
If D_N=O(N^eta) on an unbounded subsequence, first use q_i<=2^i q_0
and this inequality to obtain a polynomial height bound, then reinsert
log M_N=O(log N). Thus H_N=O(N^(1+eta)(log N)^(4/3)) there.

**F6 (conditional exclusion, substantially enlarged range):** An actual
odd orbit with subexponential canonical word complexity and
D_N=O(N^eta) along an unbounded subsequence for any
eta<1/d_*-1=0.8466259329... must be eventually periodic.
This extends SC3's 0.0526808586... threshold under the stated additional
canonical-complexity hypothesis. It does not exclude arbitrary phases
or exponential drawups. PR187 at 099058f3f2602a48e109c964899f0a9a2a223338
addresses a different low-complexity hypothesis on actual gap words and
fixed-source repetition; do not conflate the canonical and actual words.

## 5. Boundary and handoff

The finite conditional-KL step retains the exact actual time and phase
distribution, allowing a general entropy/height tradeoff even when h
is irrational. It avoids any unproved rate of convergence of stationary
empirical measures. The remaining challenge is an arithmetic upper bound
on the actual scalar's canonical entropy or drawup, or the opposite
same-law collision estimate. Generic stationary symbolic measures,
including zero-entropy measures, do not supply these inputs.

The proof uses only the pinned actual scalar identity, exact finite
relative entropy and elementary mean estimates until the optional SC2
combination. The new written finite entropy estimates have NOT been
formalized in Lean here. CarryBudget.lean from the parent contains the
finite carry telescope and the exact forbidden transition as uncompiled
Lean source candidates. No theorem is accepted by fiat.
