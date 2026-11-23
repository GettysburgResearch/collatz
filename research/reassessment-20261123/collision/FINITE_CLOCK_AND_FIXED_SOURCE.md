# Finite stationary normalizations force an explosive clock

23 November 2026. Author: `actual_collision`.

**Status: PROPOSED written theorems on the stated ordinary graph; the
infinite-series core is Lean-checked. No escaping Collatz orbit is asserted
to exist, and no same-source collision upper or Collatz closure is proved.**

The direct attempt was to combine the repository's finite weighted
occupation laws with the critical real-renewal contradiction. A finite
occupation law can be made formally stationary by speeding up the original
successor. Theorem 1 proves that every such finite normalization forces
explosion. Theorem 2 identifies its precise missing flux. This concerns the
same hypothetical ordinary component, not a replacement symbolic example.

The final section gives a separate uniform height payment for repeated
actual gap words, and states the first missing collision implication.

## 1. Map, one component, and the universal rate theorem

Let

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

on positive odd integers. Fix one hypothetical escaping ordinary forward
orbit, and let `E` be its eventual-meeting component. Restriction to units
modulo three is permitted and changes none of the argument. Every forward
orbit in `E` is injective and remains in `E`.

Assume a positive harmonic flow on this exact graph:

\[
0<\nu(q)<\infty,\qquad
\nu(q)=\sum_{n\in E:Un=q}\nu(n).
\tag{1}
\]

All sums in this note are over ordinary vertices. In particular
`nu(Un)>=nu(n)`. Choose **any** rate function `c:E→(0,∞)` whose values are
finite and for which

\[
0<M:=\sum_{n\in E}\frac{\nu(n)}{c(n)}<\infty,
\qquad \pi(n)=\frac{\nu(n)}{M c(n)}.
\tag{2}
\]

**Theorem 1 (every finite normalization explodes).** From every fixed
ordinary source `n∈E`,

\[
\boxed{
\sum_{j\ge0}\frac1{c(U^j n)}\le\frac M{\nu(n)}<\infty.}
\tag{3}
\]

Consequently the minimal continuous-time process which waits at `x` an
independent exponential time of rate `c(x)` and then takes exactly the
original edge `x→Ux` explodes almost surely. Its lifetime `T_infinity`
satisfies

\[
\mathbb E_n T_\infty
=\sum_{j\ge0}\frac1{c(U^j n)}\le M/\nu(n).
\tag{4}
\]

The probability `pi` solves all coordinatewise balance equations
`pi Q=0`, but is **not** stationary for the minimal process killed at
explosion. In fact its surviving mass tends to zero as time tends to
infinity.

**Proof.** Harmonicity and positivity give
`nu(U^j n)>=nu(n)>0`. Injectivity of this one orbit gives

\[
\nu(n)\sum_{j\ge0}\frac1{c(U^j n)}
\le\sum_{j\ge0}\frac{\nu(U^j n)}{c(U^j n)}\le M.
\]

This is an inequality of nonnegative series, proving (3). If `H_j` are the
holding times, Tonelli gives
`E(sum_j H_j)=sum_j 1/c(U^j n)<infinity`. A nonnegative random variable
with finite expectation is finite almost surely, proving (4) and explosion.

The finite-state rates are
`Q(n,Un)=c(n)`, `Q(n,n)=-c(n)`, with all other entries zero. There are no
self-edges on this escaping component. At each fixed state `q`,

\[
\sum_{n:Un=q}\pi(n)c(n)
=\frac{\nu(q)}M=\pi(q)c(q).
\tag{5}
\]

Each incoming sum is finite, so this coordinatewise equation is valid.
For the minimal killed transition kernel `P_t`, however,

\[
\sum_q(\pi P_t)(q)
=\sum_n\pi(n)\mathbb P_n(T_\infty>t)\longrightarrow0
\tag{6}
\]

by almost-sure explosion and bounded convergence under the probability
`pi`. Equation (6) rules out stationarity for that kernel. `QED`.

This theorem does **not** rule out a nonminimal conservative extension
which admits entrances, returns, or resurrection at explosion. Such an
extension can agree with the same finite-state rate matrix. It adds
boundary behavior and a law for its flux; those are not part of the
original deterministic ordinary successor process. Formal balance alone
does not identify that additional behavior.

The distinction is also discussed in Anderson, Cappelletti, Koyama and
Kurtz, [*Non-explosivity of stochastically modeled reaction networks that
are complex balanced*](https://people.math.wisc.edu/~dfanderson/papers/ACKK_ExplosionsAugust28.pdf),
Section 3. Their finite-mean-jump sufficient condition is not invoked here:
our direct proof needs none of its additional rate hypotheses. Indeed

\[
\sum_n\pi(n)c(n)=M^{-1}\sum_n\nu(n)=\infty,
\tag{7}
\]

because a single injective forward spine has flow at least `nu(n)` at
every vertex. No conclusion about a general stationary extension is
imported from this reference.

## 2. The exact boundary flux and generator defect

Now use the supplied finite-capacity hypothesis of the fast-flow packet.
Fix its original spine `q_j=U^j(q_0)` and suppose

\[
v_j:=\nu(q_j)\uparrow C\in(0,\infty).
\tag{8}
\]

Let `S={q_j:j>=0}`, `S_J={q_0,...,q_J}`, `f=1_S`, and `f_J=1_{S_J}`.
Here `Qf(n)=c(n)(f(Un)-f(n))` is a pointwise expression; membership in a
closed semigroup generator domain is not assumed.

**Theorem 2 (explicit flux defect).** Under (1), (2), and (8),

\[
\boxed{
\sum_n\pi(n)Qf(n)=C/M>0,\qquad
\sum_n\pi(n)Qf_J(n)=0.}
\tag{9}
\]

Both displayed sums are absolutely convergent. Moreover

\[
\boxed{
\|f_J-f\|_{L^1(\pi)}\to0,
\qquad
\|Qf_J-Qf\|_{L^1(\pi)}=C/M\quad\text{for every }J.}
\tag{10}
\]

**Proof.** `S` is forward invariant, so `Qf` is nonnegative and is
supported exactly on parents outside `S` whose next vertex belongs to
`S`. All parents of `q_0` lie outside `S`, with total flow `v_0`. For
`j>=1`, the sole parent lying on `S` is `q_(j-1)`; the other parents have
total flow `v_j-v_(j-1)`. Distinct endpoint levels give disjoint parent
sets. Their total incoming flow is therefore

\[
v_0+\sum_{j\ge1}(v_j-v_{j-1})=C.
\tag{11}
\]

Multiplication by `pi(n)c(n)=nu(n)/M` proves the first equation in (9).
For `S_J`, the incoming flow is `v_J`, and the outgoing edge from `q_J`
has flow `v_J`. Thus its mean is zero, with absolute integral `2v_J/M`.

The indicators converge pointwise and are bounded under the probability
`pi`, so they converge in `L1(pi)`. Their pointwise generator expressions
differ on two disjoint sets: the outgoing cutoff state `q_J`, of weighted
magnitude `v_J/M`, and parents entering spine levels strictly after `J`,
of total magnitude `(C-v_J)/M`. This proves (10). `QED`.

Equation (9) isolates the flux which a conservative stationary extension
would have to compensate at infinity. It also shows why one cannot sum
coordinate balances after separating the spine's incoming and outgoing
infinite sums: each separated sum diverges. If an extension with invariant
law `pi` placed `f` in its `L1(pi)` generator domain with generator equal
to this pointwise `Qf`, stationarity would give `integral Qf=0`, contrary
to (9). Thus that domain assertion, or the uncorrected generator formula
at this observable, cannot hold. This is a statement about the proposed
extension's generator, not a claim that all conservative extensions are
impossible.

## 3. What this resolves in the proposed stationary construction

The fast-flow packet keeps the original root's entire inverse history law
and gives a positive harmonic flow with capacity `C`. Since every vertex
eventually joins the spine, `nu(n)<=C` everywhere. Therefore choosing
`c(n)=n^s` yields finite `M` for every `s>1`, without any new analytic
input. Theorem 1 applies to each of these ordinary normalizations.

If the supplied whole-path occupation identity and a bound

\[
\sum_{n\le X}\nu(n)\le KX^\kappa
\tag{12}
\]

are available, dyadic summation gives `sum_n nu(n)n^(-s)<infinity` for
every `s>kappa`. This retains those sources' domain and analytic
hypotheses. Lowering the admissible power does not repair the stationary
law: Theorem 1 applies to **every** rate for which the normalization is
finite, not just powers. No uniform coalescence estimate is used in its
proof.

PR180's critical real-renewal theorem requires the specified stationary
gap law and its real affine observable. A finite occupation weight,
formal balance, and a fast original clock do not supply a conservative
stationary process with that observable. The exact obstruction in this
attempt is (3), and its flux is (9). This does not refute a different
construction that supplies and verifies the necessary boundary law.

The complementary PR177 conditional Haar construction retains an
ordinary next endpoint `q` and the exact ternary phase graph

\[
u(3x+1)=q.
\tag{13}
\]

At its frozen source, `x` becomes Haar conditionally on `q`, but the
law of `q` remains the original `U_*mu`. Thus recovering the endpoint
through (13) recovers that same ordinary endpoint law; marginal Haar
for `x` is not an endpoint collision estimate. The physical valuation
tends to infinity in this averaging, and the binary source tends to
`-1/3`, where the ordinary forward map is discontinuous. The PR180
compact-fibre density result uses its own boundary/scenery law and gives
topological tail density, without a chronological occupation rate.
No joint invariant law preserving these different source weights,
valuation normalization, and original chronological endpoint has been
constructed here. Their conjunction therefore does not remove the flux
or produce the required same-source collision bound.

## 4. A uniform fixed-source budget for repeated ordinary words

This finite result strengthens the fixed-template height payment in
PR182 by allowing the template to vary while the positive source stays
fixed. It uses every affine carry and applies to either drift sign.

Let `w=(g_0,...,g_(d-1))` be any nonempty positive integer gap word, put
`A=sum g_i>=d`, `a_i=sum_(t<i) g_t`, and retain its complete carry

\[
C(w)=\sum_{i=0}^{d-1}3^{d-1-i}2^{a_i}.
\tag{14}
\]

Suppose an actual ordinary segment starting at a positive odd integer
`p` has its first `kd` gaps equal to `w^k`, where `k>=2`. Write
`p_j=U^(jd)(p)`, `0<=j<=k`.

**Theorem 3 (all-template repeat budget).** Either `p_1=p_0`, which
is an actual positive ordinary cycle, or

\[
\boxed{
2^{(k-1)A+1}\mid(p_1-p_0),\qquad
2^{(k-1)A+1}<(3/2)^d(p+1).}
\tag{15}
\]

In particular, if a nonperiodic source begins with a square `ww`, then

\[
\boxed{p+1>2(4/3)^d.}
\tag{16}
\]

**Proof.** The repeated full word gives, for `0<=j<k`,

\[
2^A p_{j+1}=3^d p_j+C(w).
\]

Subtract consecutive equations. With `delta_j=p_(j+1)-p_j`,

\[
2^A\delta_{j+1}=3^d\delta_j,
\qquad
2^{(k-1)A}\delta_{k-1}=3^{(k-1)d}\delta_0.
\tag{17}
\]

All `p_j` are odd, so `delta_(k-1)` is even. Coprimality of two and
three proves the divisibility in (15). If `delta_0` is nonzero, its
absolute value is at least `2^((k-1)A+1)`.

Every ordinary odd step satisfies
`U(x)+1<=(3/2)(x+1)`. Thus
`p_1+1<=(3/2)^d(p+1)`. If `p_1>p`,
`p_1-p<=((3/2)^d-1)(p+1)<(3/2)^d(p+1)`.
If `p_1<p`, `p-p_1<p+1<(3/2)^d(p+1)`.
This proves the strict inequality in (15). Finally set `k=2` and
use `A>=d` to get (16). `QED`.

For a repeat beginning at time `i` of the **same original source**
`p_0`, assume `U^(i+d)(p_0) != U^i(p_0)`; this condition holds
automatically on an escaping orbit. Then the same argument retains its
preperiod cost:

\[
2^{(k-1)A+1}<(3/2)^{i+d}(p_0+1).
\tag{18}
\]

Therefore arbitrarily long prefix squares cannot occur at one fixed
nonperiodic positive source, uniformly over all templates. At later
windows both the no-cycle condition and the factor `(3/2)^i` remain;
dropping either would be an invalid fixed-source strengthening. A
nonperiodic initial source may subsequently enter a cycle. This statement
neither excludes actual positive cycles nor bounds their number.

## 5. The first unproved collision implication

Let `q_j=U^j(q_0)` remain one fixed escaping ordinary source. For every
actual past window of length `m` ending at `j`, keep its total binary
clock `A`, complete ordered carry `C_w`, and literal source
`p=q_(j-m)`. The existing injective source boxes are

\[
B=\left(A,\left\lfloor C_w/3^m\right\rfloor,
            \left\lfloor p/2^A\right\rfloor\right).
\tag{19}
\]

No quotient is reduced away in this packet. For the retained labels
`m<=j<N`, let `N_B` be their box counts and

\[
\mathcal B_{N,m}
=\left(\sum_B\sqrt{N_B/(N-m)}\right)^2.
\]

The supplied finite consumer is

\[
\sqrt{\operatorname{Col}_{3^m}(\pi_N)}
\le\frac{\sqrt{(N-m)\mathcal B_{N,m}}+m}{N}.
\tag{20}
\]

Suppose `pi_(N_l)` converges to a fixed actual ternary law `mu`. For
each fixed `m`, the finite residue partition is continuous, so (20)
gives the precise sufficient condition

\[
\liminf_{\ell\to\infty}
\frac{\mathcal B_{N_\ell,m}}{N_\ell-m}
\le e^{-\Phi(\log_2 3)m+o(m)}
\quad\Longrightarrow\quad
\operatorname{Col}_{3^m}(\mu)
\le e^{-\Phi(\log_2 3)m+o(m)}.
\tag{21}
\]

The `o(m)` in this assertion concerns `m→infinity`, after taking the
displayed liminf for each fixed `m`; the source and limiting law stay
fixed. Here `Phi` is the collision exponent in the pinned PR180 source,
not a newly defined rate. Its same-limit strict lower exponent would
contradict this upper if (21)'s premise were proved.

**OPEN:** Persistent cross-box ternary collisions have not been shown
to force repeated exact gap words satisfying (15) at a source/time
whose budget (18) is violated. Equal endpoint residues alone do not
identify the two complete words, their ordered carries, or their
original source quotients. The all-template estimate therefore does
not establish (21). Likewise the finite-clock theorem closes a false
stationarity inference; it supplies no replacement collision upper.

## 6. Evidence boundary

`lean/FiniteClock.lean` proves the infinite-series statement (3) from
nonnegative weights on natural states, a strictly positive initial
flow, monotonicity along an injective orbit, positive finite rates, and
summability of the whole-state normalization. Extending weights by zero
off `E` and rates by one embeds the displayed ordinary graph in that
formal statement. Harmonic-flow existence, the exponential-process
construction, Theorem 2, Theorem 3, and the cited arithmetic/analytic
inputs have written-proof or source-qualified scope. They are not
claimed as formal consequences checked by that Lean module.

The exact source ledger and compiler/axiom receipts are in
`reports/2026-11-23-reassessment/collision-*`.
