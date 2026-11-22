# Actual excess-clock harmonicization and the remaining amplitude estimate

**Status: source-qualified written theorem and an arithmetic comparison test.
This does not prove Collatz.** The positive result below pays the moving
ordinary-time tail for the specified family of original sources. It uses the
monotone family `P^m V`, whose pointwise limit is established, rather than
assuming ordinary pointwise convergence of the finite densities `D_m`.

The attempted closing step fails at a precise place: the available finite
density horizon depends on the fixed ancestral floor, whereas the actual
inverse clock grows with the forward clock. The final section tests an
arithmetic sibling comparison that would address the surviving amplitude.

## 1. Pinned inputs

The following analytic inputs remain source-qualified; they are not new Lean
axioms or results proved here.

- PR180 at `ab3973099f0d285bbe88972382ad599bb02cd460`,
  `research/lean-joint-20261122/ORDINARY_BOUNDARY.md`, equations B28--B37:
  the finite common contact reference `sigma_*` and domination at every
  forward clock while retaining every original source label.
- PR185 at `53f01ca5b443ef57ef2160b4996dbb2cc87f7395`,
  `research/multiple-attacks-20261122/STOPPED_MIXING_INTERFACE.md`:
  the actual critical Doob law, the bound `V<=2 chi G`, and the stopped
  comparison for finite densities. Its associated ordinary harmonic-flow
  note supplies the bounded Radon--Nikodym comparison of the complete
  critical and ordinary inverse path laws.
- PR176 at `31c4a880ea4acf6eec4783e68bfc75e2cf8e7fe6`,
  `research/lean-global-resolvent-20261121/overview/literature/`
  `ABEL_CANONICAL_COMPARISON.md`: only
  `alpha V <= liminf D_m <= limsup D_m <= 2G` is established on ordinary
  integers. Neither convergence of `D_m` nor equality of a density limit
  with `G` is an available input.

Let `N` be the nonperiodic positive odd ternary units. Forward transport is
killed upon entering a periodic orbit. On `N`, let `U` be the accelerated
odd map, `P` its critical inverse operator, and

\[
G=\lim_{m\to\infty}P^mV,\qquad PG=G,\qquad
1\le V/G\le2\chi.
\tag{1}
\]

All actual inverse parents of a state in `N` remain nonperiodic. Parents
divisible by three contribute zero to `V` and `G`, so the restriction to
`N` is compatible with (1). Write `K_G` for the critical Doob kernel and
`K_nu(x,y)=nu(y)/nu(x)` on actual unit-parent edges.

Use `C_2={V<=2}` and first contact including time zero. Its endpoint laws
are `mu_q^G` and `mu_q^nu`; its actual inverse depth is `tau_q`. Put

\[
c_j=(j+1)^{-1/2}-(j+2)^{-1/2},\quad \kappa=3\delta/4,
\quad C(p)=\frac1{\kappa c_{\ell(p)}\nu(p)},
\tag{2}
\]

where `ell(p)` counts strict future contacts. The pinned common-reference
theorem and the path-law comparison give, for every retained forward state,

\[
\boxed{\mu^G_{U^kp}\le\delta^{-1}C(p)\sigma_*},
\qquad C(p)\le C_0p^{5/2},\qquad \|\sigma_*\|_1<\infty.
\tag{3}
\]

This is domination of the actual stopped law. No Haar law, independent
valuation sequence, or resampled source has been substituted.

## 2. The centered hitting depths are uniformly tight

Every connected component of the retained deterministic graph is acyclic.
Choose an integer coordinate `h_C` with

\[
h_C(Ux)=h_C(x)+1
\tag{4}
\]

on its retained edges. This works both in escaping components and in
components whose forward paths eventually leave `N`: in the latter case,
one can use minus the remaining distance to the exit. The additive choice
of coordinate will cancel.

If `q_k=U^kp` is retained and the actual inverse contact endpoint is `x`,
then `U^tau x=q_k`. Consequently

\[
\boxed{\tau-k=h_C(p)-h_C(x).}
\tag{5}
\]

For one original source `p`, (3)--(5) imply

\[
\sup_{k:q_k\in N}\Pr^G_{q_k}(\tau>k+r)
\le\delta^{-1}C(p)
\sum_{\substack{x\in\operatorname{Comp}(p)\\h_C(p)-h_C(x)>r}}\sigma_*(x)
\longrightarrow0.
\tag{6}
\]

Here `Comp(p)` denotes the connected component of `p`.
The limit in (6) is continuity from above for a finite measure on a
countable set: the clock difference is finite at every individual endpoint.
There is no expected hitting-time hypothesis.

For the repository's original source family, retain the original label
`n`, weight `w_n=n^-4`, and projected odd unit `p_n=pi(n)<=2n`. Drop the
labels whose projected state is periodic. Set

\[
Z=\delta^{-1}\sum_n w_n C(p_n)<\infty
\tag{7}
\]

and define one finite measure on pairs of original labels and contact
endpoints by

\[
\Xi(n,x)=\delta^{-1}w_n C(p_n)\sigma_*(x)
\mathbf1_{\{x\in\operatorname{Comp}(p_n)\}}.
\tag{8}
\]

Indeed `w_n C(p_n)<=2^(5/2) C_0 n^(-3/2)`. With

\[
\Gamma(r)=
\sum_{\substack{n,x\\h_{\operatorname{Comp}(p_n)}(p_n)
                  -h_{\operatorname{Comp}(p_n)}(x)>r}}\Xi(n,x),
\tag{9}
\]

we have `Gamma(r)->0`. Let `I_k` be the labels still retained after `k`
forward steps and write `q_{n,k}=U^kp_n`. The actual aggregate tail obeys

\[
\boxed{
\sup_{k\ge0}\sum_{n\in I_k}w_n
  \Pr^G_{q_{n,k}}(\tau>k+r)\le\Gamma(r)\longrightarrow0.}
\tag{10}
\]

Each original label still has its original weight. Colliding labels are
summed, not replaced by a fresh probability distribution. Killing a label
can only decrease the left side. Thus (10) includes the terminating
components correctly and makes no assertion about excluded periodic
orbits.

## 3. Uniform harmonicization after an excess inverse clock

Define the nonnegative normalized error

\[
v_m(q)=\frac{P^mV(q)-G(q)}{G(q)},\qquad
B=2\chi-1.
\tag{11}
\]

Then `0<=v_m<=B`, `v_m` decreases pointwise to zero, and

\[
K_Gv_m=v_{m+1}.
\tag{12}
\]

Set

\[
A(m)=\sum_xv_m(x)\sigma_*(x)\longrightarrow0.
\tag{13}
\]

The convergence follows from bounded convergence against the one finite
reference, using established monotone harmonicization at each ordinary
endpoint.

**Theorem.** For all nonnegative integers `k,r,m`,

\[
\boxed{
\sum_{n\in I_k}w_n
 \left(\frac{P^{k+r+m}V(q_{n,k})}{G(q_{n,k})}-1\right)
\le Z A(m)+B\Gamma(r).}
\tag{14}
\]

In particular,

\[
\boxed{
\lim_{R\to\infty}\sup_{k\ge0}
\sum_{n\in I_k}w_n
 \left(\frac{P^{k+R}V(q_{n,k})}{G(q_{n,k})}-1\right)=0.}
\tag{15}
\]

**Proof.** At the actual root `q=q_{n,k}`, the process
`v_(k+r+m-j)(X_j)` is a bounded martingale up to time `k+r`, by (12).
Stop at `tau wedge (k+r)`. On `tau<=k+r`, its remaining index is at
least `m`, so its value is at most `v_m(X_tau)`. On the complement its
value is at most `B`. Therefore

\[
v_{k+r+m}(q_{n,k})
\le\int v_m\,d\mu^G_{q_{n,k}}
       +B\Pr^G_{q_{n,k}}(\tau>k+r).
\tag{16}
\]

Apply (3), sum with the unchanged original weights, and use (10).
This proves (14). Taking `m=floor(R/2)` and `r=R-m` proves (15).
All stopping times in this proof are bounded by `k+r`; no optional
stopping at an integrability-uncontrolled time is used. `QED`

The one-source version follows from (6) and the same proof. A strict
first return can also be used: its endpoints lie in contact layer
`ell(q)+1_C2(q)`, so replacing the scalar in (2) by
`C_plus(p)=1/(kappa c_(ell(p)+1) nu(p))` gives the corresponding
domination. Rebuild `Z_plus`, `Xi_plus`, and `Gamma_plus` using this
larger scalar; the identical proof applies with those quantities, not
with an asserted reuse of the smaller bounds in (7)--(10).

## 4. What does and does not extend to the actual density family

For `m>=1`, put

\[
o_m(x)=\sup_{a,b\ge m}\frac{|D_a(x)-D_b(x)|}{G(x)}.
\tag{17}
\]

These errors decrease and are bounded by `4 chi`. The exact stopped
density martingale gives, whenever `a,b>=k+r+m`,

\[
\frac{|D_a(q_{n,k})-D_b(q_{n,k})|}{G(q_{n,k})}
\le\int o_m\,d\mu^G_{q_{n,k}}
       +4\chi\Pr^G_{q_{n,k}}(\tau>k+r).
\tag{18}
\]

The remaining density horizons are at least one, so (18) avoids the
nonunit-parent defect at `D_0` identified in PR185. Equations (3) and
(10) pay the ordinary-time term. However the first term converges only
to the integral of the ordinary pointwise oscillation `o_infinity`.
The pinned sources do not prove that oscillation is zero. Haar almost
everywhere convergence cannot supply this assertion on the countable
actual endpoint set.

If ordinary convergence of `D_m` were proved separately, (18) would give
uniform moving-horizon Cauchy convergence for this original-source family.
Its limit would be a positive `P`-harmonic profile comparable with `G`;
identifying it with `G` would require a further normalization or uniqueness
argument. Neither assertion is inserted into (14).

## 5. Testing the proposed closing implication

Suppose one original source `p` escapes, with actual forward states
`q_k=U^kp`. Equation (15) compares `P^(k+R)V(q_k)` to the positive
canonical amplitude `G(q_k)`. It does not make that amplitude small.
For example, each retained term in

\[
\sum_{n\in I_k}w_n\frac{P^{k+R}V(q_{n,k})}{G(q_{n,k})}
\tag{19}
\]

is at least its original weight; an escaping original atom survives at
every clock.

More concretely, let `b` be the minimum ordinary unit in the escaping
component. The finite-floor certificate uses a precision `m` with
`9^m<=b` and a horizon bounded by `H_m^*`, a number fixed once the
component floor is fixed. The actual depth in (14) is `k+r+m`, which
eventually exceeds every such fixed horizon. The argument supplies no
choice of excess time that reverses this inequality as `k` grows.

Increasing the floor to a later forward minimum removes the unchanged
source `p` from the retained inverse tree. Its contribution then appears
in the genuine floor-boundary immigration term. Dropping that term would
drop precisely the original positive mass one is trying to exclude.
Thus the centered-clock theorem resolves a timing issue for a specified
source family; it does not resolve the remaining amplitude estimate.

## 6. Exact sibling precision averaging and its quantitative limitation

The ordinary unit-preserving sibling map is

\[
\mathcal B(n)=64n+21,\qquad U(\mathcal B(n))=U(n),\qquad
1+3\mathcal B^j(n)=64^j(1+3n).
\tag{20}
\]

Since `v_3(64^j-1)=2+v_3(j)`,

\[
v_3(\mathcal B^j(n)-n)=1+v_3(j).
\tag{21}
\]

Consequently the first `N_t=3^(t-1)` siblings form exactly one complete
residue class modulo three at ternary precision `t`. Ternary martingale
consistency proves the exact identity

\[
\boxed{
\frac1{N_t}\sum_{j=0}^{N_t-1}D_t(\mathcal B^j(n))=D_1(n).}
\tag{22}
\]

For a unit `n`, the right side is one or two. The canonical sibling
flow, however, weights the `j`th sibling by `64^-j`. Periodicity gives
the different identity

\[
\sum_{j\ge1}64^{-j}D_t(\mathcal B^j(n))
=\frac{\sum_{j=1}^{N_t}64^{-j}D_t(\mathcal B^j(n))}
       {1-64^{-N_t}}.
\tag{23}
\]

The guaranteed return of the original spike in (23) costs
`1/(64^N_t-1)`. This is doubly exponential in the precision. It is
not the inverse-logarithmic comparison needed to force nonsummable
sibling loss along a hypothetical escaping orbit. Equation (22) alone
does not improve that weighted recurrence cost.

There is also a literal inverse-word obstruction. If a fixed inverse
prefix of depth `r` has forward affine expression
`F_W(x)=(3^r x+C)/2^A=n`, applying the identical valuation prefix at
`mathcal B(n)` would give

\[
x'=64x+\frac{21(3C+2^A)}{3^r}.
\tag{24}
\]

The numerator `21(3C+2^A)` has ternary valuation exactly one.
Thus for `r>=2` the candidate is not an integer. A successful comparison
must repair the actual valuations or ternary carries; copying the prefix
does not define an ordinary sibling path.

More generally, the same formal inverse prefix at `mathcal B^j(n)` has
source

\[
x_j=64^jx+
\frac{(64^j-1)(3C+2^A)}{3^{r+1}}.
\tag{25}
\]

For positive `j`, this is an integer exactly when `3^(r-1)` divides
`j`. The first possible copied integer word therefore has height factor
`64^(3^(r-1))`. Preserving a ternary-unit endpoint can require one more
ternary digit: `j` divisible by `3^r` suffices, matching the precision
`3^(r+1)` of the finite obstacle profile `V_r` with seed `g=1_unit`.
Integer-word integrality alone must not be substituted for this endpoint
condition. These calculations are the concurrent universal-source attack's
obstruction, recorded here to fix the arithmetic required of a witness
map rather than presume an ordinary tree embedding.

### An actual finite-density diagnostic

Full rational valuation sums, using the existing
`research/lean-joint-20261122/finite_density_certificate.py`, give

\[
\boxed{D_6(1457)>16,\qquad
\mathcal B(1457)=93269,\qquad D_6(93269)<1.}
\tag{26}
\]

The exact comparisons in (26) were checked with integer common
denominators, including the complete geometric valuation tail. Approximate
values are `16.5269829337` and `0.9257914476`; the ratio is below `1/16`.
These are actual positive integers, obtained from the residues `-1` and
`-43` modulo `3^6`.

The reproducible checker [verify_stopped_arithmetic.py](verify_stopped_arithmetic.py)
also verifies (22) exactly for both unit classes at each depth one through
six. The complete rational values and twelve residue-average checks are in
[stopped-arithmetic.json](../../reports/2026-11-22-central-step/stopped-arithmetic.json).
From the repository root, regenerate the checks with

```sh
python research/central-step-20261122/verify_stopped_arithmetic.py \
  --check reports/2026-11-22-central-step/stopped-arithmetic.json
```

This does **not** disprove a comparison for `G`, or a comparison restricted
to high-linear spikes `G(n)>=eta n`. It demonstrates why a finite-density
spike cannot simply be assigned a fixed fraction at its first sibling
without an arithmetic argument. The companion
[CRITICAL_BOUNDARY.md](CRITICAL_BOUNDARY.md), Section 6, formulates the
weaker inverse-logarithmic sibling-loss estimate and the finite-obstacle
comparison that would actually exclude a positive escaping amplitude.
