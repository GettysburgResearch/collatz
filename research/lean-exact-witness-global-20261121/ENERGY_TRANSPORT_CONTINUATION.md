# The complete finite-Green transport profile

Date: 2026-11-22.

**Status: written deductions from the explicitly pinned canonical inputs and
the written S-unit return theorem.** No new analytic assumption is added as
a Lean axiom. The result resolves the two-parameter Green-truncation
calculation on actual ordinary orbits. It does not prove that the escaping
coefficient is zero, and does not exclude nontrivial cycles.

For the actual finite Green potential, the two directions of the energy
have the same limiting profile. If the Green depth is `M` and the physical
odd clock is `N`, each direction contributes

\[
 Wb_\infty\min(M/N,1).
\]

The convergence is **uniform over every finite Green depth**. For the full
Green potential, only one of these contributions remains. The other is a
real moving cutoff front, not a signed term that may be discarded in an
exchange of limits.

## 1. Frozen inputs and notation

The repository is `GettysburgResearch/collatz`. The source objects are:

| Source | Exact head and material used |
|---|---|
| PR177 | `e4ca639326bac73da8c2a698dec8a749e5efbe68`, `research/lean-exact-witness-global-20261121/LITERATURE_CANONICAL_ENERGY.md`, (3)--(12): retained ordinary domain, canonical reference and charge, source decomposition, summable absolute variation; (31) and (38)--(45): escaping component coefficient and run weights. |
| PR177 | The same head, `LITERATURE_ARITHMETIC_RETURN.md`, Theorem 3: bounded binary-run times have upper Banach density zero on each actual escaping odd orbit. Its deep input is Evertse--Schlickewei--Schmidt, Theorem 1.1, as cited and specialized there. |
| PR175 | `08fe1388ad63c758680b3695249aca319515c47d`, `research/lean-global-closure-20261121/machinery/EXACT_RUN_WEIGHT_COMMUTATOR.md`, (7)--(8): the boundary drift is uniformly negligible and the supremum of the previous commutator has an exact surviving escape coefficient. This is context for the attack; its proof is not a premise of the new profile calculation. |

Use the retained forest of nonperiodic positive odd ternary units. The
actual odd map is

\[
 U(n)=\frac{3n+1}{2^{v_2(3n+1)}},
\]

and a forward path is killed on its first periodic vertex. Its killing
time is `tau(x)`. The original positive reference and charge satisfy

\[
 L\nu=\nu,\qquad 0<\nu(x)\le A,\qquad d(x)\ge0,
 \qquad D=\sum_xd(x)<\infty.
 \tag{1}
\]

Here `L` transports counting-measure masses forward. Forward composition
`C` includes the killed indicator, and

\[
 Kf=\nu^{-1}L(\nu f),\qquad g=d/\nu,
 \qquad R_M=\sum_{i=0}^{M-1}K^ig,\qquad R=\sum_{i\ge0}K^ig.
 \tag{2}
\]

The canonical inputs give `0 <= R_M <= R <= 1`. All the original
predecessor-population, finite-envelope, and normalization qualifications
of the pinned construction remain in force.

For an escaping component `E`, let

\[
 C_E=\lim_{j\to\infty}\nu(U^jx)>0,\qquad
 D_E=\sum_{x\in E}d(x),\qquad F_E=D_E/C_E\le1,
\]

and retain the original coefficient

\[
 b_\infty=\sum_{E\text{ escaping}}\frac{D_E^2}{C_E}
 =\sum_{E\text{ escaping}}F_ED_E\le D.
 \tag{3}
\]

The reference is never renormalized after selecting finitely many sources.
In particular `C_E` in every approximation below is the same original
component constant as in (3).

Fix `rho > 1` and a positive integer `L_0`. Put

\[
 w(x)=\min(\rho^{R_{\rm bin}(x)},W),\qquad W=\rho^{L_0},
 \tag{4}
\]

where `R_bin` counts binary runs. The S-unit input gives, for every fixed
escaping ray `q_j=U^j q_0`,

\[
 \lim_{H\to\infty}\sup_{a\ge0}
 \frac1H\sum_{j=0}^{H-1}\bigl(W-w(q_{a+j})\bigr)=0.
 \tag{5}
\]

All the theorems also hold for `w=1`, `W=1`, without the S-unit input.
More generally, the proof uses only `0 <= w <= W` and (5) on each escaping
ray, together with the canonical inputs.

For any bounded function `f`, define the two nonnegative energies

\[
 \mathcal Q_N^\pm(f;w)
 =\frac1N\sum_{\tau(x)>N}\nu(x)w(U^Nx)
       \bigl[(f(x)-f(U^Nx))_\pm\bigr]^2.
 \tag{6}
\]

The notation is `z_+=max(z,0)` and `z_-=max(-z,0)`. Thus the plus sign
records a decrease of the potential along the actual forward segment;
the minus sign records an increase. Set

\[
 \mathcal Q_{N,M}^\pm(w)=\mathcal Q_N^\pm(R_M;w),\qquad
 \mathcal Q_{N,M}(w)=\mathcal Q_{N,M}^+(w)+\mathcal Q_{N,M}^-(w).
 \tag{7}
\]

This total is exactly the physical finite-Green energy in (45) of the
frozen PR177 note. Every sum retains its actual source, endpoint, and
ordinary accelerated clock.

## 2. Main theorem: uniformity in all finite Green depths

### Theorem 1

Under the displayed inputs, for each fixed weight (4),

\[
 \boxed{\lim_{N\to\infty}\sup_{M\ge1}
 \left|\mathcal Q_{N,M}^{\pm}(w)
       -Wb_\infty\min\left(\frac MN,1\right)\right|=0.}
 \tag{8}
\]

The assertion holds separately for each sign. Consequently,

\[
 \boxed{\lim_{N\to\infty}\sup_{M\ge1}
 \left|\mathcal Q_{N,M}(w)
       -2Wb_\infty\min\left(\frac MN,1\right)\right|=0.}
 \tag{9}
\]

Along *any* choice of finite depths with `M_N/N -> lambda` in the
extended interval `[0,infinity]`, this gives

\[
 \mathcal Q_{N,M_N}(w)
 \longrightarrow2Wb_\infty\min(\lambda,1).
 \tag{10}
\]

This includes bounded `M_N`, unbounded `M_N=o(N)`, every finite positive
ratio, and `M_N/N -> infinity`.

### Theorem 2

For the full potential,

\[
 \boxed{\mathcal Q_N^+(R;w)\longrightarrow0,
 \qquad \mathcal Q_N^-(R;w)\longrightarrow Wb_\infty.}
 \tag{11}
\]

Moreover the omitted Green tail is uniformly non-negligible in this
energy whenever `b_infinity > 0`:

\[
 \boxed{\lim_{N\to\infty}\sup_{M\ge1}
          \mathcal Q_N^+(R-R_M;w)=0,}
 \tag{12}
\]

\[
 \boxed{\lim_{N\to\infty}\sup_{M\ge1}
 \left|\mathcal Q_N^-(R-R_M;w)-Wb_\infty\right|=0.}
 \tag{13}
\]

Thus no choice of a finite Green depth as a function of `N` approximates
the full potential in the averaged physical energy when an escaping
component carries positive canonical charge. This is a statement about
the original canonical potential and sources; no model kernel is used.

## 3. A source-wise variation bound that survives every truncation

For one original source `x`, write its actual retained ray as
`q_j=U^j x`, and set `v_j=nu(q_j)`. Harmonicity implies

\[
 0<v_0\le v_1\le\cdots\le A.
 \tag{14}
\]

Nonperiodicity makes the ray injective. For an interval `I` of nonnegative
integer times, finite or infinite, the source contribution is

\[
 p_{x,I}(q)=\frac{d(x)}{\nu(q)}
   \mathbf1_{\{q=q_j:\ j\in I,\ j<\tau(x)\}}.
 \tag{15}
\]

The intervals needed here are `[0,M)`, `[0,infinity)`, and `[M,infinity)`.
The source decomposition is exact:

\[
 R_M=\sum_xp_{x,[0,M)},\quad
 R=\sum_xp_{x,[0,\infty)},\quad
 R-R_M=\sum_xp_{x,[M,\infty)}.
 \tag{16}
\]

Each source is counted at its unique actual visit to a retained target.
Define actual-edge absolute variation by

\[
 \operatorname{Var}_\nu(f)=\sum_q\nu(q)|f(q)-Cf(q)|.
\]

If the nonempty support interval in (15) starts at index `s`, its incoming
parents contribute exactly `d(x)`. Along each internal edge, the change
on the displayed ray contributes `d(x)(1-v_j/v_(j+1))`. All other
incoming parents of its next vertex together contribute exactly the same
amount. A finite endpoint, including a killed endpoint, contributes one
further `d(x)`. Hence

\[
 \operatorname{Var}_\nu(p_{x,I})
 \le2d(x)\left(1+\sum_{j\ge s}\left(1-\frac{v_j}{v_{j+1}}\right)\right)
 \le B_x:=2d(x)\left(1+\log\frac A{\nu(x)}\right).
 \tag{17}
\]

Only edges for which both displayed vertices are retained enter the sum.
An empty support has zero variation. The second inequality follows by
`1-a/b <= log(b/a)` and telescoping. It applies uniformly to all three
interval types and every cutoff.

The pinned canonical calculation supplies the finite budget

\[
 B_*:=\sum_xB_x
 \le2D(1+\log\kappa)+\frac{16000A}{3}<\infty,
 \qquad\kappa=\max(1,A/\gamma).
 \tag{18}
\]

This uses the specific original canonical charge. It is not an assertion
that every bounded Green potential has summable variation.

### Uniform approximation by finitely many original charges

Let `F` be a finite set of original sources, and replace each sum in
(16) by its sum over `x in F`. The omitted function `h` is nonnegative
and at most one. Equation (17) gives

\[
 \operatorname{Var}_\nu(h)\le B(F^c):=\sum_{x\notin F}B_x,
 \tag{19}
\]

uniformly in `M`, including the full and tail potentials. On a retained
`N`-step segment,

\[
 |h(x)-h(U^Nx)|^2\le|h(x)-h(U^Nx)|
 \le\sum_{j=0}^{N-1}|h-Ch|(U^jx).
\]

Since `C` is an `L1(nu)` isometry on nonnegative functions, summing gives

\[
 \mathcal Q_N^+(h;w)+\mathcal Q_N^-(h;w)
 \le W B(F^c).
 \tag{20}
\]

This is uniform in both clocks. The positive-part and negative-part maps
are 1-Lipschitz. The triangle inequality in the weighted space of actual
`N`-step pairs therefore implies, for either sign,

\[
 \left|\sqrt{\mathcal Q_N^\pm(f;w)}
       -\sqrt{\mathcal Q_N^\pm(f_F;w)}\right|
 \le\sqrt{W B(F^c)}.
 \tag{21}
\]

All relevant full and finite-source energies are at most `W B_*`.
Their absolute difference is therefore at most
`2W sqrt(B_* B(F^c))`. This is a genuine uniform finite-source
approximation. It does not approximate `R` by `R_M` in an infinite-mass
`L1` or `L2` norm.

## 4. Exact energy of one actual pulse

Fix an escaping actual ray `q_j`. Put

\[
 v_j=\nu(q_j)\uparrow C>0,\qquad
 a_j=D_0/v_j,\qquad a_\infty=D_0/C,
 \tag{22}
\]

where `D_0>0` is fixed. Consider the function supported only on this ray,

\[
 p_M(q_j)=a_j\mathbf1_{\{0\le j<M\}},
 \qquad p_M=0\text{ elsewhere}.
 \tag{23}
\]

Let `h=min(M,N)`. Each actual `N`-step pair belongs to one of three
nonzero cases.

1. It starts and ends on the pulse. It contributes the nonnegative
   decrease `a_j-a_(j+N)`, since `v_j` is increasing.
2. It starts on the pulse and ends past its cutoff. It contributes
   `a_j` to the positive part.
3. It starts outside the pulse and ends at a pulse vertex. It contributes
   `a_k` to the negative part.

All inverse ancestors of a pulse vertex are included in the third case.
Their total mass is exactly `v_k`, by `L^N nu=nu`. When `k>=N`, the
one displayed ray ancestor has mass `v_(k-N)` and is removed from that
case. The following formulas are therefore exact:

\[
\begin{split}
 \mathcal Q_N^+(p_M;w)
 ={}&\frac1N\sum_{0\le j<M-N}v_jw(q_{j+N})(a_j-a_{j+N})^2\\
 &+\frac{D_0^2}{N}\sum_{j=M-h}^{M-1}\frac{w(q_{j+N})}{v_j},
\end{split}
 \tag{24}
\]

\[
\begin{split}
 \mathcal Q_N^-(p_M;w)
 ={}&\frac{D_0^2}{N}\sum_{k=0}^{h-1}\frac{w(q_k)}{v_k}\\
 &+\frac{D_0^2}{N}\sum_{k=N}^{M-1}
       w(q_k)\frac{v_k-v_{k-N}}{v_k^2}.
\end{split}
 \tag{25}
\]

An upper limit below the lower limit means an empty sum. No branch is
replaced by an independent copy.

The first line of (24) is negligible uniformly in `M`. Since
`(a_j-a_(j+N))^2 <= a_0(a_j-a_(j+N))` and `v_j<=C`,

\[
 \frac1N\sum_{0\le j<M-N}v_jw(q_{j+N})(a_j-a_{j+N})^2
 \le\frac{WCa_0}{N}\sum_{j=0}^{N-1}(a_j-a_\infty)
 \longrightarrow0.
 \tag{26}
\]

The telescoping inequality also holds when the internal sum is empty.
The second line of (25) is negligible uniformly in `M`, because

\[
 \sum_{k=N}^{M-1}(v_k-v_{k-N})
 \le NC-\sum_{k=0}^{N-1}v_k.
 \tag{27}
\]

After division by `N`, the bound tends to zero. These estimates pay
both the changing reference on the ray and every incoming side branch.

Replacing `1/v_j` by `1/C` in the two main sums has an error tending to
zero uniformly in `M`: `1/v_j-1/C` is positive and decreasing, so its
sum over any interval of length at most `N` is bounded by its first
`N` terms. The first main sum in (25) is a prefix of at most `N` times.
The cutoff sum in (24) is an interval of length `h<=N` whose starting
point may move arbitrarily far forward.

Condition (5) implies the uniform partial-window statement

\[
 \omega_N:=\sup_{a\ge0,\ 0\le h\le N}
 \frac1N\sum_{j=0}^{h-1}(W-w(q_{a+j}))\longrightarrow0.
 \tag{28}
\]

Split `h<epsilon N`, costing at most `W epsilon`, from
`h>=epsilon N`, where (5) applies uniformly. First increase `N`, then
decrease `epsilon`. Each main sum therefore equals

\[
 W\frac{D_0^2}{C}\frac{\min(M,N)}N+o(1)
 \tag{29}
\]

with an error uniform in every finite `M`. This proves both profiles
for a single actual pulse.

## 5. The full ray and the omitted tail

For the full-ray profile `p_infinity(q_j)=a_j`, every nonzero positive
difference is internal to the displayed ray. Equation (26), now with an
infinite sum, gives

\[
 \mathcal Q_N^+(p_\infty;w)\longrightarrow0.
 \tag{30}
\]

Indeed the nonnegative telescoping series is exactly

\[
 \sum_{j\ge0}(a_j-a_{j+N})
 =\sum_{j=0}^{N-1}(a_j-a_\infty).
\]

The negative energy has the first `N` incoming terms in (25) and all
side-parent terms with `k>=N`. Their total side-parent mass obeys

\[
 \sum_{k=N}^{\infty}(v_k-v_{k-N})
 =NC-\sum_{k=0}^{N-1}v_k.
 \tag{31}
\]

It follows that

\[
 \mathcal Q_N^-(p_\infty;w)\longrightarrow W D_0^2/C.
 \tag{32}
\]

For the remaining tail put

\[
 t_M(q_j)=a_j\mathbf1_{\{j\ge M\}},\qquad t_M=0
 \text{ away from the displayed ray}.
 \tag{33}
\]

Its positive differences are internal and bounded by (26), uniformly in
`M`. For `M<=k<M+N`, every actual `N`-step ancestor of `q_k` lies
outside the tail: its displayed ray ancestor, when present, has index
`k-N<M`. For `k>=M+N`, remove that ray ancestor, whose mass is
`v_(k-N)`. This gives the exact formula

\[
\begin{split}
 \mathcal Q_N^-(t_M;w)
 ={}&\frac{D_0^2}{N}\sum_{k=M}^{M+N-1}\frac{w(q_k)}{v_k}\\
 &+\frac{D_0^2}{N}\sum_{k=M+N}^{\infty}
    w(q_k)\frac{v_k-v_{k-N}}{v_k^2}.
\end{split}
 \tag{34}
\]

The second line is bounded, uniformly in `M`, by a constant times
`C-(1/N) sum_(k<N) v_k`, using (31). In the first line, replacing
`1/v_k` by `1/C` costs at most its first-`N` average error, because
`1/v_k-1/C` is nonnegative and decreasing. Condition (5) applies
uniformly to the length-`N` interval starting at `M`. Consequently

\[
 \sup_{M\ge0}\mathcal Q_N^+(t_M;w)\longrightarrow0,
\]

\[
 \sup_{M\ge0}
 \left|\mathcal Q_N^-(t_M;w)-WD_0^2/C\right|
 \longrightarrow0.
 \tag{35}
\]

The tail tends to zero at each fixed vertex when `M` increases.
Equation (35) locates its nonzero energy at the actual moving cutoff.

## 6. Finite original sources, collisions, and killed paths

Fix a finite set `F` of original charges and partition it by actual
components. Charges in different components cannot share either endpoint
of a retained forward pair, so their energies add without cross terms.

In an escaping component `E`, choose one actual anchor downstream of
every selected source in `F intersect E`. It exists because a finite
collection of forward paths in one acyclic component eventually
coalesces. Let `t_x` be the actual number of steps from source `x` to
this anchor, and put

\[
 D_{F,E}=\sum_{x\in F\cap E}d(x).
 \tag{36}
\]

On the common forward ray the finite-Green source sum is exactly

\[
 \frac1{\nu(q_j)}
 \sum_{x\in F\cap E}d(x)\mathbf1_{\{j+t_x<M\}}.
 \tag{37}
\]

Compare it with (23), using `D_0=D_(F,E)` and the **original** reference
`nu`. Before the anchor they differ on a fixed finite set. After the
anchor they can differ only within `max_x t_x` times of the cutoff.
The squared `L2(nu)` norm of the error is bounded independently of `M`:
the reference is at most `A`, the strips have bounded cardinality, and
the finitely many required reciprocal reference values are bounded. If
`M` is shorter than one of the offsets, the same bound applies.

For any such error `e`, restriction to retained pairs and the
`L2(nu)` isometry of `C` give

\[
 \frac1N\sum_{\tau(x)>N}\nu(x)w(U^Nx)
 |e(x)-e(U^Nx)|^2
 \le\frac{4W}{N}\|e\|_{L^2(\nu)}^2.
 \tag{38}
\]

The positive-part Lipschitz bound from (21) makes the energy error tend
uniformly to zero. This handles all same-component cross terms: the
correct amplitude is the *sum* `D_(F,E)`, and its square is retained.
No replacement by a sum of squared charges is made.

The full-ray and tail comparisons work in the same way. For the tail,
(37) has `j+t_x>=M`; its difference from (33) is confined to a
fixed-width strip, again with the uniform bound (38).

If a selected source is killed, its entire forward support is finite.
For finitely many such sources every truncated, full, or tail potential
has an `L2(nu)` norm bounded independently of `M`. Equation (38) shows
that all these contributions tend to zero uniformly in `M`. Killing is
included rather than supplied as a negligible boundary assumption.

The single-ray calculation now proves all the profiles for finite `F`,
with coefficient

\[
 b_F=\sum_{E\text{ escaping}}\frac{D_{F,E}^2}{C_E}.
 \tag{39}
\]

## 7. Exhaustion of the actual original charge

Increase `F` through finite sets containing every original source.
Equations (18)--(21) make the error uniformly small in both clocks and
for either energy direction. Nonnegative convergence gives

\[
 b_F\uparrow\sum_{E\text{ escaping}}\frac{D_E^2}{C_E}
 =b_\infty.
 \tag{40}
\]

First fix `F`, apply the uniform pulse calculation as `N` increases,
then exhaust `F`. The error in (21) tends to zero independently of
all choices of `M`. This proves Theorems 1 and 2, including every
supremum over finite depths. No rate for the S-unit theorem is needed,
and no estimate uniform over all components is inserted before the
finite-source exhaustion.

## 8. Consequences for the closing attack

The former commutator calculation left an apparent choice between first
increasing Green depth and first increasing physical time. The uniform
profile now determines every diagonal choice.

- If `M=o(N)`, both finite-Green energy directions vanish. The omitted
  tail still has limiting energy `W b_infinity`.
- If `M/N -> lambda` with `0<lambda<1`, each finite-Green direction
  carries `lambda W b_infinity`.
- If `M>=N`, up to a vanishing error, the finite potential carries
  `W b_infinity` at each of its two fronts. The full potential carries
  only the incoming one.

The tail energy is not the difference of these energies: energy is
quadratic and the cross term matters. When `M>=N`, the artificial
decreasing front of `R_M` cancels the increasing front of `R-R_M` in
their sum `R`. The source-labelled proof keeps this cancellation visible.

This resolves the finite-Green approximation issue on the actual
canonical forest, more strongly than an iterated-limit statement. It
does not pay the remaining arithmetic sibling current or prove
`b_infinity=0`. The attempted direct sibling route still needs an
ordinary estimate for the canonical least-obstacle construction; its
harmonic identity alone does not compare mass at an actual source with
total mass at its distinct siblings. No such missing comparison is used
in Theorems 1 or 2.

All new infinite-sum, energy, and uniform-limit arguments in this note
are written proofs. The canonical hypotheses and the published S-unit
input have not been installed as extra Lean axioms.
