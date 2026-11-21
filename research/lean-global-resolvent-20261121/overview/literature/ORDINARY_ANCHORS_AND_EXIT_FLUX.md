# Ordinary anchors, predecessor density, and finite exit flux

## Status

This is a full-closure attempt using the new uniform predecessor-density input.
It yields an exact finite-anchor obstruction, a one-sided ordinary trace bound,
and a finite exit identity that retains cycles. It does **not** prove the
Collatz conjecture or the required upper bound on surviving exit flux.

[`HitPotentials.lean`](../lean/HitPotentials.lean) formalizes the generic Green identities, their minimality
and uniqueness statements, the actual Collatz 5/16 example, the finite trace
estimate with an explicit count hypothesis, exact invariance of the survivor
label, and the finite exit identity. The analytic density input itself is not
assumed as a Lean axiom. The density and capacity deductions below are written
proofs, with their hypotheses stated.

The file compiles with Lean 4.34.1 and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`, using warnings as errors.
The printed theorem axioms are only `propext`, `Classical.choice`, and
`Quot.sound`; there is no `sorryAx`. The final replay receipt is in
[`checkpoint7-lean.json`](../../../../reports/2026-11-21-lean-global-resolvent/checkpoint7-lean.json).

## 1. The density hypothesis and the useful trace it actually gives

Use the shortcut map on positive integers,

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd},\end{cases}
\qquad
P(a)=\{n\ge1:\exists k\ge0,\ T^k(n)=a\}.
\]

The input called **PD** here is the written analytic conclusion of PR180 at
`cf91e46fa9fbadba3df7942202a5197c134d0ce0`, in
`research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md`:
there exist absolute constants `c,C>0` such that

\[
3\nmid a,\qquad X\ge Ca
\quad\Longrightarrow\quad
\#(P(a)\cap[1,X])\ge cX/a.                       \tag{PD}
\]

PR180 proves a lower bound for odd predecessors, which suffices for this full
predecessor count. Its fixed-total renewal input remains an analytic input,
not a theorem formalized in the companion file.

For a function `g` constant on the **actual predecessor chains of `a`**, the
finite count immediately gives

\[
\boxed{\frac ca |g(a)|^2
\le M_X(g):=\frac1X\sum_{n=1}^{X}|g(n)|^2,\qquad X\ge Ca.}       \tag{1}
\]

Full ordinary invariance `g(Tn)=g(n)` suffices, but is stronger than needed.
The Lean theorem `predecessor_trace` proves the corresponding finite-set
inequality for arbitrary deterministic maps. `conditional_density_trace`
takes the population lower bound as an explicit hypothesis.

Let `H_1=1_{P(1)}` and `B=1-H_1`. Because `1` lies on the `1,2` cycle, `B`
is exactly invariant at every ordinary positive integer, including `1`.
If `B(a)=1` at a ternary unit, (1) gives

\[
\liminf_{X\to\infty}M_X(B)\ge c/a.                \tag{2}
\]

Since `B^2=B`, this is also a lower density bound. Every nonconvergent
component has a ternary-unit point: after removing factors of two, an odd
point divisible by three maps to a point congruent to two modulo three.
Thus a zero-density theorem for `B` would close the conjecture under PD,
including both extra cycles and escape. PD provides (2); it does not provide
the required upper bound tending to zero.

## 2. A finite ordinary defect can support nonvanishing bulk variation

For any deterministic map `f` and nonperiodic target `a`, put
`H_a(x)=1` when `x` eventually hits `a`, and zero otherwise. Then

\[
\boxed{H_a(x)-H_a(fx)=1_{\{a\}}(x).}              \tag{3}
\]

Away from `a`, reaching `a` is equivalent to reaching it after one more step.
At `a`, nonperiodicity says that the next point never returns to `a`.
Telescoping gives the exact finite Green identity

\[
H_a(x)=\sum_{j=0}^{k-1}1_{\{a\}}(f^j x)+H_a(f^k x).             \tag{4}
\]

Both (3) and (4) are formalized without any density assumption.

For the actual Collatz map, `5` and `16` both map to `8`, and then to the
`1,2` cycle. Neither reaches the other. Their predecessor sets are disjoint:
if one orbit hit both targets, their order along that orbit would make one
target reach the other. These facts are all proved in Lean.

Set

\[
p_X=\#(P(5)\cap[1,X])/X,\qquad
q_X=\#(P(16)\cap[1,X])/X.
\]

Conditionally on PD, for `X>=16C`,

\[
p_X\ge c/5,\qquad q_X\ge c/16,\qquad p_X+q_X\le1.
\]

Consequently the empirical variance of `H_5` satisfies

\[
V_X(H_5)=p_X(1-p_X)\ge p_Xq_X\ge c^2/80.          \tag{5}
\]

But its squared coboundary energy is exactly

\[
D_X(H_5):=\frac1X\sum_{n=1}^{X}|H_5(n)-H_5(Tn)|^2=\frac1X,
\qquad X\ge5.                                    \tag{6}
\]

Thus a finite-box Poincare inequality `V_X(g)<=K D_X(g)` for all bounded
ordinary `g` requires `K>=c^2 X/80`. No scale-independent such constant exists.
The extra anchor condition `g(1)=0` does not repair a bound of `M_X(g)` by
`D_X(g)`: `H_5(1)=0`, while `M_X(H_5)>=c/5`.

**Exact scope:** `H_5` is not exactly invariant at the ordinary point `5`.
This does not refute a theorem restricted to exactly invariant ordinary
labels. It refutes a route that first discards finite defects in a density
norm and then invokes an ambient spectral gap or ergodicity statement.
The distinction between ordinary invariance and invariance after ignoring
finitely many points is essential here.

## 3. Killing at the anchor retains all cycles

For any target `a`, periodic or not, define

\[
(K_ag)(x)=1_{x\ne a}g(fx),\qquad \delta_a(x)=1_{x=a}.
\]

The exact hitting function satisfies

\[
H_a=\delta_a+K_aH_a.                              \tag{7}
\]

It is the least nonnegative solution: every nonnegative solution equals one
at every point hitting `a`, and is nonnegative elsewhere. The constant
function one is also a solution. Their difference

\[
B_a=1-H_a,
\qquad 0\le B_a\le1,
\qquad B_a=K_aB_a                                  \tag{8}
\]

is the exact obstruction to uniqueness among bounded nonnegative solutions.
These statements, including the equivalence between universal hitting and
uniqueness, are formalized. This is a useful interface, not a new proof of
uniqueness: the actual homogeneous function (8) must still be ruled out.

## 4. An exact finite exit decomposition, with the trapped term retained

Let `D` be any domain and let

\[
(K_Dg)(x)=1_D(x)g(fx),\qquad e_Dg=1_{D^c}g.
\]

If `g(x)=g(fx)` on `D`, then, for every finite horizon `k`,

\[
\boxed{g=\sum_{j=0}^{k-1}K_D^j(e_Dg)+K_D^k g.}     \tag{9}
\]

This follows from `g=e_Dg+K_Dg` and finite telescoping. Each term in the sum
records the first exit at that exact time; earlier killing makes all other
terms zero. `finite_exit_green` and `finite_exit_green_sum` formalize (9)
pointwise and after summing over any finite ordinary sample. No limiting
measure, stationary distribution, or mixing assumption enters.

For Collatz use `D_R={2,...,R}` and `g=B`. Exit at `1` contributes zero.
Exit through the upper boundary lands in

\[
\partial^+D_R=\{q\in\mathbb N:R<q\le(3R+1)/2,\ q\equiv2\pmod3\}.
\]

For `1<=X<=R`, let `omega_{X,R}(q)` be `1/X` times the number of initial
points in `[1,X]` whose first exit from `D_R`, before time `R`, is at `q`.
Let `rho_{X,R}` be the proportion whose whole orbit stays in `D_R`.
There are only `R-1` states in `D_R`. A path staying there for the first `R`
states has repeated and must remain in an internal cycle. Therefore taking
`k=R` in (9) gives the exact finite identity

\[
\boxed{M_X(B)=\sum_{q\in\partial^+D_R}\omega_{X,R}(q)B(q)
                  +\rho_{X,R}.}                  \tag{10}
\]

Here `B^2=B` was used. The trapped term is the population feeding a cycle
contained in the box and avoiding `1`. It is not an error term that may be
dropped before extra cycles are excluded. The finite-domain specialization
and its pigeonhole interpretation are written deductions from the formal
generic identity.

For a fixed bad unit source `a`, combining PD with (10) yields, for every
`X>=Ca` and every `R>=X`,

\[
\frac ca\le
\sum_q\omega_{X,R}(q)B(q)+\rho_{X,R}.              \tag{11}
\]

This is the precise competing flux inequality. A closure proof needs an
independently established upper bound on this **survivor-weighted outgoing
flux plus trapped mass**, tending to zero along suitable large samples.
Neither PD nor the rowwise inverse Green estimate supplies that upper bound.
The unweighted first-exit mass cannot simply be substituted and declared
small: when `R=X`, about one sixth of the sample exits immediately through
odd integers above `2X/3`, irrespective of later convergence.

### Why a divergent spine does not fix the upper-bound problem

For an escaping spine `a_i=T^i(a)`, the sets `P(a_i)` increase to its entire
grand orbit. Each fixed low point in that component eventually belongs to
one of these predecessor sets. A fixed-floor tail estimate can bound paths
that avoid all low anchors; it does not bound the mass already carried by
the basins of those anchors. After deleting their contribution, precisely
the boundary term in (10) remains.

If predecessor densities `delta_i` exist, they can increase to a positive
component density while increments from side branches have a summable
lower bound of order `1/a_i`. Monotonicity and reciprocal packing therefore
give no contradiction. The fixed source cannot be replaced by a succession
of raised floors that remove its mass from the population being estimated.

## 5. The critical reciprocal-weight anchor estimate also fails

A tempting replacement for the refuted density-gradient estimate is

\[
\limsup_X M_X(g)
\stackrel{?}{\le}K\left(|g(1)|^2+
\sum_{n\ge1}\frac{|g(n)-g(Tn)|^2}{n}\right).       \tag{12}
\]

It keeps every ordinary defect, so the singleton example alone does not
refute it. However, the following elementary cutoff does. For `M>1`, put

\[
g_M(n)=\min\left(\frac{\log n}{\log M},1\right).
\]

Then `g_M(1)=0` and `lim_X M_X(g_M)=1`. For positive integers,
`n/2<=Tn<=2n`, hence the truncated logarithm gives

\[
|g_M(n)-g_M(Tn)|\le\frac{\log2}{\log M}.
\]

For `n>=2M` both values are one. Consequently

\[
\sum_{n\ge1}\frac{|g_M(n)-g_M(Tn)|^2}{n}
\le\frac{(\log2)^2}{(\log M)^2}
       \sum_{n\le\lceil2M\rceil}\frac1n
=O(1/\log M)\longrightarrow0.                    \tag{13}
\]

Thus (12) is false for every finite `K`, even independently of the truth of
Collatz. The reciprocal-weight ordinary anchor has zero capacity against
this class of slowly varying cutoffs. This correction was identified in the
root review and is included to prevent publishing a false analytic gate.

A heavier weight `n^(-1+epsilon)` avoids this particular cutoff, but a second
test imposes a much stronger necessary threshold. For positive even `L`,

\[
x_L=2^{L+1}-1,\qquad T^L(x_L)=q_L=2\cdot3^L-1,
\qquad 3\nmid x_L.
\]

The exact ascent follows from
`T^j(x_L)=3^j 2^(L+1-j)-1` for `0<=j<=L`.
Since `P(x_L)` is contained in `P(q_L)`, PD gives

\[
\underline d(P(q_L))\ge c/x_L
\asymp q_L^{-\log_3 2}.                           \tag{14}
\]

If `q_L` is nonperiodic, testing an all-function anchored estimate on
`H_{q_L}` forces its weight to be at least a constant times `1/x_L`.
If `q_L` is periodic, its cycle is different from `1,2`; the indicator of
that cycle's basin is exactly invariant, vanishes at `1`, and has positive
density by the same PD input, refuting any such estimate outright.
Consequently power weights `w(n)=n^(-theta)` with

\[
\theta>\log_3 2
\quad\text{or equivalently}\quad
\epsilon<1-\log_3 2\approx0.36907
\]

cannot work, conditionally on PD. Any fixed power of `log n` divided by `n`
also fails this test. This ascent correction was supplied by the root
closure pass; it is a written deduction here, not an extra theorem imported
into the Lean file.

Only weights with `epsilon>=1-log_3 2` survive this necessary test. A possible
new power-weight investigation would therefore use strictly
`1-log_3 2<epsilon<1`; no corresponding coercivity theorem is proved here.
Such an estimate, if established for all bounded `g`, would in
particular imply

\[
\overline d(P(a))\le K a^{-1+\epsilon}             \tag{15}
\]

by testing `g=H_a` at any nonperiodic target. Such a target is outside the
`1,2` cycle, so `H_a(1)=0`, and (3) leaves a single weighted defect.
The decay in (15) would exclude an escaping spine under PD: `P(a)` is
contained in every later `P(a_i)`, while `a_i` tends to infinity. Extra
cycles would still have to be controlled, or included through an estimate
applicable to the exactly invariant label `B`.

This identifies concrete demands on an energy route: retain the ordinary
anchors, and use enough weight or additional structure to overcome both the
logarithmic-cutoff capacity obstruction and the exact ascent density spikes.
No claim that the surviving heavier estimate holds is made.

## 6. Primary literature used, and its exact scope

Tao's published paper proves that the minimum falls below every prescribed
function tending to infinity for logarithmically almost every input. Its
Remark 1.4 retains a floor depending on the allowed exceptional proportion;
it does not give absorption at a single fixed floor. The introduction also
explains why exceptional sets cannot be repeatedly bypassed using an
unjustified invariant-distribution assumption. These distinctions support
the retained terms in (10), rather than removing them.

- Terence Tao, *Almost all orbits of the Collatz map attain almost bounded
  values*, Forum of Mathematics, Pi 10 (2022), e12:
  <https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F>

Assani constructs a finite invariant measure supported on the conservative
cycle part. That construction does not give positive mass to all ordinary
sources and does not exclude the dissipative part. His stronger finite
measure formulation, equivalent to counting measure and giving a power
bounded composition operator with conservative part `{1,2}`, is stated as
equivalent to the Collatz conjecture. It cannot be imported as an
unconditional recurrence theorem.

- Idris Assani, *Collatz map as a non-singular transformation*, Studia
  Mathematica 275 (2024), 249–261, DOI 10.4064/sm230913-14-12;
  primary preprint: <https://arxiv.org/html/2208.11675v3>.

The new conclusions in this note are the explicit finite 5/16 obstruction,
the finite trace formulation, and the retained ordinary exit identity. The
first unsupported global step remains the upper bound opposite (11), or an
alternative coercivity theorem that survives all the counterexamples above.
