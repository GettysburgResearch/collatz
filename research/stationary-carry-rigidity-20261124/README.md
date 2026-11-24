# Stationary critical-gap rigidity and rational-scalar carry compression

Date: 2026-11-24. Status: **PROPOSED written mathematics; full Collatz OPEN.**
This packet gives three source-preserving deductions and a Lean proof candidate for
the finite carry arithmetic. The Lean candidate has not been compiled in this
environment. No source-qualified analytic theorem is upgraded to kernel verification.

## Attribution correction — 24 November 2026

S1 rederives the strict stationary collision-gap theorem already proved in
PR180 at `7cfd911d35382d9d3bc988060ba88ade78a4267e`,
`research/whole-source-20261123/COLLISION_CORE.md`, sections 3–4,
equations (16)–(17). Its conclusion is not a new theorem of this packet.
The sufficient contrary hypothesis using upper collision dimension in section
1.3 is an immediate corollary of that earlier upper-dimension conclusion.
S2, S3 and the finite-phase extension have separate statements and scopes.
This correction changes attribution only; the original proof is preserved below.

## Sources and notation

We use the actual accelerated positive odd map U(q)=(3q+1)/2^g(q),
g(q)=v2(3q+1)>=1, and literal orbit q_i=U^i(q_0). Let alpha=log_2(3),
Phi(a)=a log(a)-(a-1)log(a-1), Psi(c)=Phi(1+c), with 0 log 0=0.
Logs without subscripts are natural. Let theta=Phi(alpha)/log(3).

Frozen source heads inspected:
- PR182 f94a2ae1caba9a1857feda892ee1779695eea9d2:
  research/carry-tower-round10-20261123/ACTUAL_SCALAR_FORMALIZATION.md,
  ActualScalar.lean (the actual scalar construction);
  GENERAL_PHASE_RETURN.md and RETURN_TOWER.md (phase/carry conventions);
  research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md and
  OrbitCounting.lean (global separated-visit compression).
- PR185 2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d:
  research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md;
  research/rigidity-closing-20261122/SAME_SOURCE_INVERSE_ENTROPY.md and
  MOVING_INVERSE_WINDOW.md (fixed-source law and transfer, retaining the
  harmonic-flow hypothesis).
- PR180 7cfd911d35382d9d3bc988060ba88ade78a4267e, research/closing-step-20261123/README.md:
  distinguishes random affine models from actual ordinary sources.
- PR173 fa0c9e2a2851e6324391e39c17afcb5913185aec and
  PR184 366dab89ee9548084ab9b5e4e90ff82abf287a20:
  bounded forced bands and lower-source merger interfaces.
- PR186 1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493,
  literature/deep-machinery-20261122/01_problem_interfaces.md:
  exact closure boundaries.

The three theorems below concern the original orbit or a specified
forward-invariant injective set. No resampled source, harmonic-flow law
identification, or conjectural stationary distribution is assumed.
No literature-priority claim: in particular PR182 credits Paper 28 v3
for stronger general interval compression results. Our explicit power gain
below concerns finite scalar-phase classes and is not a new general record.

## 1. Strict critical collision gap for every stationary empirical limit

### 1.1 Fixed-source extraction

Assume q_0 is one positive odd ordinary source whose orbit is injective.
This is exactly the non-eventually-periodic case of a deterministic map.
Write A_M=sum_{i=0}^{M-1} g_i. The complete ordinary equations give

    A_M = alpha M + log_2(q_0/q_M)
          + sum_{i=0}^{M-1} log_2(1+1/(3q_i))
        <= alpha M + O_{q_0}(1+log M).

The last bound uses distinct positive integers and the harmonic-sum bound.
For each M sample J uniformly from {0,...,M-1} and form the actual
one-sided gap sequence (g_J,g_{J+1},...). For every fixed coordinate i,
its mean is at most A_{M+i+1}/M, so finite-coordinate laws are tight.
From any sequence M tending to infinity, diagonal extraction gives
consistent finite-block limits; they extend to a stationary process G on
positive integers. Stationarity follows because a one-position shift of
the original time window changes its law in total variation by at most
1/M. By truncation (or Fatou), E G_0 <= alpha. No moment convergence or
positive entropy premise is needed.

For a positive word w=(g_0,...,g_{m-1}), put A=sum g_i and a_i=sum_{j<i}g_j.
The complete affine identity is

    2^A q_{J+m} = 3^m q_J + sum_{i=0}^{m-1} 3^(m-1-i) 2^a_i.

Thus the word determines q_{J+m} modulo 3^m. Its distribution differs
from that of q_J modulo 3^m by at most m/M. The word laws converge on
the countable finite-word space (tightness plus pointwise convergence);
pushforward to the finite residue space preserves convergence.
Every subsequential weak limit mu on Z_3 of the ordinary empirical
measures is therefore, at each precision m, the residue pushforward
of the same stationary gap process, after a further diagonal extraction.

For the collision Col_m(mu)=sum_a mu(a mod 3^m)^2, grouping nonnegative
word masses implies

    Col_m(mu) >= sum_w P(G_0,...,G_{m-1}=w)^2 >= exp(-H_m(G)).

The second inequality is Jensen, with H_m the Shannon entropy. It is
valid for the countable word alphabet, since its entropy is finite.

### 1.2 The equality dichotomy

For a positive-integer law of mean at most alpha, relative entropy against
the geometric law Q(k)=(1/alpha)(1-1/alpha)^(k-1) gives
H(G_0)<=Phi(alpha), with equality only at Q (including equality of means).
For a stationary process, subadditivity gives h=lim H_m/m=inf H_m/m.

Case A: h<Phi(alpha). Pick delta>0 with h<(theta-delta)log 3.
For all sufficiently large m, H_m<=(theta-delta)m log 3, hence
Col_m(mu)>=3^(-(theta-delta)m).

Case B: h=Phi(alpha). Then H_1=Phi(alpha) and H_m=m H_1 for all m.
Equality in Shannon subadditivity forces independent coordinates in
every finite block; G is iid with the displayed geometric law.
Its word collision is exactly

    (sum_{k>=1} Q(k)^2)^m = (2 alpha-1)^(-m).

Moreover log(2 alpha-1)<Phi(alpha), by strict Jensen for this nonuniform
law (its order-two Renyi entropy is strictly smaller than Shannon entropy).
Numerically log(2 alpha-1)/log 3=0.705155598..., whereas theta=0.949955527....

**Theorem S1.** Every empirical ternary limit mu extracted from any one
injective positive ordinary odd orbit satisfies

    limsup_{m->infty} [-log Col_m(mu)/(m log 3)] < theta.

This proof gives no uniform gap over stationary laws. At the level of
word laws, stationary processes made from independent uniform
constant-composition blocks of fixed length and a uniform block offset
can have collision-entropy rates approaching the Shannon bound as that
block length increases. This observation does not exclude a stronger
uniform gap for their ternary projections; that would require a separate
argument. Do not turn S1 into a uniform exponent improvement for all
finite clocks.

### 1.3 Exact connection to PR185

Let pi_M=(1/(M+1)) sum_{j=0}^M delta_{q_j}. The variant using M terms
above has TV difference at most 1/(M+1). Under the exact original
harmonic-flow hypothesis of PR185, its moving-root measures zeta_(M,r)
satisfy sup_r TV(zeta_(M,r),pi_M)->0. Thus any subsequential ternary
limit of zeta_(M,r_M), with arbitrary finite r_M, obeys S1 as well.

A **new sufficient target for escape exclusion** is to prove that one
such same-source stationary ternary limit has upper collision dimension
at least theta. This does not require a finite-window prefactor or
mixing rate, but it does require that exact limit. It is a different
order of limits from PR185's simultaneous precision-window theorem.
A diagonal sequence of slowly increasing precisions can transfer the
strict lower bound back to finite windows, but no prescribed faster
precision rate follows.

The hard missing implication is still a lower collision dimension for
the same ordinary-source law. A generic stationary affine model or
a freely chosen geometric inverse law cannot be substituted.

## 2. Rational scalar phases: forbidden-transition entropy bound

Use the actual scalar of PR182,

    h(q)=sum_{i>=0} g(U^i q)/3^(i+1),
    1/2<h(q)<=1+log_2(q)/3,
    h(Uq)=3h(q)-g(q).

Suppose an injective positive odd orbit has rational h(q_0).
After finitely many actual shifts its denominator is coprime to 3.
Let p_i be the unique representative of h(q_i) modulo integers in
(1/2,3/2]. Then p_i is periodic, say with period L; k_i=h(q_i)-p_i
is a nonnegative integer. Put b_i=3p_i-p_{i+1} in {1,2,3}. The exact
carry equation is

    g_i + k_{i+1} = b_i + 3k_i.                      (C1)

Let pbar be the phase mean. With V_i=log_2(q_i)-h(q_i)>=-1,
the complete physical equation gives

    V_{i+1}-V_i = log_2(3+1/q_i)-2h(q_i).

Summing from the fixed shifted source and using the distinct-state
harmonic bound gives limsup M^(-1) sum_{i<M} k_i <= beta,
where beta=alpha/2-pbar. If beta<0 the equality is impossible (as in
the existing phase rigidity). In the remaining case beta>0, since
pbar is rational and alpha is irrational. Also beta<=(alpha-1)/2.

As in S1, extract a stationary joint phase/carry process from any
empirical subsequence (carry means give tightness). Its phase is uniform
on the prescribed cycle, and E k_0<=beta. Its entire m-gap word is a
function of the initial phase and m+1 consecutive carries.

**New support restriction:** (C1) and g_i>=1 imply that if b_i=1 and
k_i=0, then k_{i+1}=0. This is an actual constraint, not an independence
assumption.

Use reference Q on the initial phase (uniform) and m+1 independent
nonnegative geometric variables with mean beta. Its cross-entropy with
the true joint word law P is at most log L+(m+1)Psi(beta).
Write f_1 for the fraction of positions in the phase cycle with b_i=1.
For each starting phase there are f_1 m+O(L) such edges, and selecting
one parity of edge indices gives at least (f_1 m-O(L))/2 disjoint edges.
Under Q each selected edge independently avoids the forbidden transition
with probability 1-r, where r=beta/(1+beta)^2.
Consequently the support event E has Q(E) <= (1-r)^(f_1 m/2-O(L)).
Since P(E)=1, D(P||Q)>=-log Q(E) (condition Q on E). Subtracting this
KL loss from cross-entropy gives

    H_m(G) <= log L+(m+1)Psi(beta)
                  +(f_1 m/2-O(L)) log(1-r).

Since the mean b_i is 2 pbar=alpha-2 beta and the other b's are at
least 2, f_1>=2-alpha+2 beta.

**Theorem S2.** For every stationary gap process extracted from such an
actual rational-scalar escaping orbit,

    h(G)/log 3 <= [Psi(beta)
         +(2-alpha+2 beta)/2 log(1-beta/(1+beta)^2)]/log 3
       <= 0.541528191... .

The exact final bound is the preceding expression at beta=(alpha-1)/2.
For monotonicity, on 0<beta<=1/3, Psi'(beta)>=log 4,
r<=3/16, 0<=r'<=1, and c=(2-alpha+2 beta)/2<=1/2 on the actual
interval. The derivative of Psi(beta)+c log(1-r) is at least
log 4-3/13-8/13>0. The endpoint beta=0, if considered abstractly,
has zero carry entropy by nonnegativity. Projection and Jensen give
the same bound on upper ternary collision dimension. This improves
the crude rational-phase bound Psi((alpha-1)/2)/log 3=0.629127436...
by using exact gap positivity.

The rationality of h is not proved. Nor is a positive lower bound on the
same ordinary-source entropy proved. This is a sharper obstruction for
rational phase candidates, not an irrationality or convergence theorem.

## 3. Global occupation improvement for finite scalar-phase classes

**Theorem S3.** Let S be a forward-invariant set of positive odd integers
on which U is injective. Suppose the actual scalar representative
p(q) in (1/2,3/2] belongs to a fixed finite set P of size L for every q in S.
Then, with an absolute constant C,

    # {q in S : q<=X} <= C L X^(47/50),   X>=1.

Thus the entire injective tail of an escaping rational-scalar orbit,
and the union of all periodic points in any specified finite invariant
scalar-phase class, satisfy an explicit 0.94 exponent. The dependence
on L is essential in this argument. It is not a count of a whole
branching basin, nor a bound on all positive cycles with unbounded phases.

Proof. Use the exact common odd-clock compression of PR182, but count
the low-clock lane using carry words. For X>=24 take K=floor log_2 X,
m=floor log_3(X/8)>=1. For each n in S with n<=X follow the same number
m of actual odd transitions, total binary clock A, endpoint q.
The full carry C_w satisfies

    2^A q=3^m n+C_w,    0<C_w/2^A <= (3/2)^m-1.

If A>=K, q<3*3^m<=3X/8<X/2. Injectivity of U^m on S charges all such
sources to S below X/2. No bound on intermediate heights is used.

For m<=A<K, q<=2*3^m X/2^A; indeed the additive carry is at most 3^m,
and the displayed main upper term 3^m X/2^A is at least 3^m.
Hence log_2 q<=alpha m+log_2 X-A+1. For the phase/carry word starting
at n, let B=sum_{i<m} b_i>=m, S_c=sum_{i<m} k_i. Summing (C1),

    A+k_m=B+2 S_c+k_0.                               (C2)

The actual scalar upper bound and p_m>1/2 give
k_m<=1/2+(log_2 q)/3. Using k_0>=0 and log_2 X=alpha m+O(1),

    S_c <= A/3+(alpha/3-1/2)m+O(1).                  (C3)

The implicit constant is absolute and independent of the phase.
For given A and initial phase, b_0,...,b_(m-1) are fixed.
The m-vector (k_0,...,k_(m-1)) determines S_c, and (C2) recovers k_m;
(C1) then recovers the complete gap word. Thus for a=A/m the number of
candidate words at clock A is at most

    min{ binom(A-1,m-1),
         L binom(m+floor(m c(a)+O(1)),m) },
    c(a)=(a+alpha)/3-1/2.

Here the first count is positive compositions and the second is weak
compositions of bounded total. The first remains valid even if multiple
phases yield one word. For each word there is exactly one odd source
residue modulo 2^(A+1), by the ordinary shortcut parity-prefix bijection
with the terminal odd bit included. Because A<K, each contributes at
most X/2^A sources. This gives, up to absolute factors in the second
bound and polynomial factors when summing clocks, a normalized exponent

    F_1(a)=1-a/alpha+Phi(a)/log 3,
    F_2(a)=1-a/alpha+Psi(c(a))/log 3,

using the usual binomial upper bound exp(N H(k/N)). All a lie in
[1,alpha+O(1/m)]. For a<=t=77/50, F_1 is increasing (a<2).
For a>=t, c(a)>1/2 and
F_2'(a)=(-log 2+(1/3)log(1+1/c(a)))/log 3<0.
At the split, use alpha<317/200 and c(t)<13/24, while
Phi(t)=Psi(t-1)<Psi(13/24). Thus both lanes are bounded by

    beta0 = 1 - 308/317 + Psi(13/24)/log 3 < 47/50.

The strict comparison, and 47/50<theta, have a rational log-interval
certificate in check.py. The O(1) in (C3) costs O(1) in the entropy
exponent, since c(a)>1/2 in its lane. For the standard composition lane
the binomial entropy bound is uniform down to a=1.
After summing O(m) clocks we obtain O(L m X^beta0)=O(L X^(47/50)).
Therefore F_S(X)<=F_S(X/2)+O(L X^(47/50)); iteration of this geometric
scale bound proves S3, including bounded X by changing the constant.

This is a complete written separated-visit bound: it does not replace
injectivity by a predecessor count. Its finite arithmetic core is in
CarryBudget.lean (uncompiled here).

## 4. What a complete proof would still require

The strict stationary gap S1 is unconditional as a statement on an
injective ordinary orbit. S2/S3 retain rational/finitely many scalar
phases and do not establish universal scalar rationality.

The natural next high-risk attempt is an arithmetic theorem forcing
a critical lower collision dimension on the original ordinary diagonal
embedding, not a theorem about abstract 2-adic symbol shifts. Stationarity
alone is insufficient: even the constant-one gap process has mean one
and gives an atomic ternary law (its all-one completion is -1, not a
positive ordinary source). General stationary symbol measures may have
zero entropy. The missing bridge must use ordinary positivity/integrality,
rather than only local symbolic legality or leading logarithmic rotation.

For cycles, S3 counts fixed phase classes but does not eliminate one
cycle or bound its phase denominator. The complete numerical divisibility
in PR185 remains open. The merger and band routes similarly lack a
universal smaller-source construction. No complete Collatz proof is
claimed.

## 5. Verification boundary

- check.py: normal and optimized Python runs returned identical output,
  exact rational exponent comparisons, 13,362 legal finite carry-word
  cases, and 40 weak-composition count cases. These are finite checks,
  not evidence that every actual orbit has rational scalar.
- CarryBudget.lean: source candidate, explicit hypotheses, no admissions.
  Lean/lake unavailable locally; network download unavailable. Do not
  report kernel validation until compilation and axiom audit at a pinned
  Mathlib checkout.
- Full repository checkout/validate not performed; the connector supplies
  source reads and Git objects, not a local complete checkout.


## Continuation: finite-window canonical entropy and PR188

See [FINITE_PHASE_ENTROPY.md](FINITE_PHASE_ENTROPY.md) for the extension beyond rational phases and stationary limits. For the original actual gap-word law G and canonical phase-word law B, H(G) <= H(B) + (0.5415281905... log 3)m + O(R), with R explicit and bounded at square-root precision. Rational phases therefore give finite-window collision lower bounds at exponent 0.5415281905... and a necessary running-height exponent 1.8466259329... for escape. Combining with pinned PR188's canonical drawup inequality excludes escape when canonical word complexity is subexponential and drawup is O(N^eta) along an unbounded subsequence with eta < 0.8466259329.... These are proposed written deductions, not Lean-verified or unconditional convergence. PR187's actual-gap complexity condition is distinct from the canonical complexity condition here.
