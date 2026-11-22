# Actual return composition, full carry continuation, and ordinary Green tails

**Full Collatz remains OPEN.** This continuation starts from PR180 at
`bfba8feaefb3d0910456cdd92d2afcf9e8785b4d` and incorporates the latest
developments at PR175, PR176, PR178, PR182, PR185, and the PR186 literature
guide. Three parallel research lanes and a separate Lean analysis module
produce the results below. The [snapshot](SOURCE_SNAPSHOT.json) inventories
all **122 open PRs** at the initial refresh; the detailed source scope is
given in each proof note, rather than claiming a new audit of every branch.

## 1. One finite reference for the entire original entrance law

Let `U` be the accelerated odd map, `D` the existing constant-70 marked
band, `E` its first entrance, and `Q` its actual positive-return pushforward,
killed at 1. Original sources have weights `n^-4`. The new reference is

\[
\beta=\sum_{n\ge1}\sum_{j\ge0}n^{-4}
 e^{-[\log(j+2)]^2}\,
 \mathbf1_D(U^j(o(n)))\,\delta_{U^j(o(n))},
\]

where `o(n)` is the odd part of the original source. Every label, endpoint
collision, and repeated visit is retained. The reference has **every finite
logarithmic height moment**, as well as

\[
\sum_m\beta(m)\exp\{a[\log(1+\log m)]^2\}<\infty
\qquad(0<a<1).
\]

Using PR176's already established polylogarithmic access clock, the new
complete-fiber argument proves, for the same reference and all fixed
`k>=0`, `1<p<infinity`,

\[
\boxed{(Q^k\rho)/\beta\in L^p(\beta),\qquad
\rho=E_*\sum_{n\ge1}n^{-4}\delta_n.}
\]

This includes the entire entrance residual from original sources outside
the band. There is an explicit bound

\[
\|(Q^k\rho)/\beta\|_p^p\le B_{k,p}\zeta(7/2),
\qquad
\log B_{k,p}=O_p(25^k(k+1)^2),
\]

and truncating **original labels** above `N` costs at most
`(2/5) B_{k,p} N^(-5/2)` in the p-th power of this norm. These are complete
infinite-tail estimates. Their return-index growth is not the closing bound.

### Actual returns preserve a family with a quantified change of parameters

Replace the weights above by `n^-s exp(-a log(j+2)^2)` to obtain
`beta_(s,a)`. For `s>s'>1` and `a>25b>0`,

\[
\boxed{Q\beta_{s,a}\le K(s-s',a,b)\beta_{s',b}.}
\]

The proof uses the injective map from each original labeled marked
occurrence to its next marked occurrence. Thus it applies under actual
composition and includes cycles and all collisions.

The explicit parameter sequence gives the stronger all-time statement

\[
\boxed{Q^k\rho\le C\,
\beta_{\,2+2^{-k},\,50^{-k}}\qquad(k\ge0),}
\]

with **one finite constant `C` independent of `k`**. The cost is entirely
in the changing references. They increase to the full occurrence measure
with original weights `n^-2`: its atom at a nonperiodic marked target is
finite, but each periodic marked target has an infinite limiting atom.
Finite total mass or moment control does not survive this limit by the
proved estimates.

The fixed reference supplies a more permissive closing target: a bound

\[
\|(Q^k\rho)/\beta\|_2^2
\ll(k+1)\exp\{\gamma[\log\log(k+e^e)]^2\},
\qquad \gamma<1,
\]

would exclude distinct-endpoint survivors. Such a bound remains OPEN;
nontrivial cycles require a separate argument. The note preserves an exact
non-Collatz countermodel showing why access times and finite-depth moments
alone do not imply this estimate.

[Full return proof and parameter constants](RETURN_ATTACK.md) ·
[Finite collision and return-clock core](lean/ReturnCritical.lean) ·
[Lognormal moments and exact scalar absorption](lean/LognormalClock.lean)

## 2. Every carry transition now has an exact physical continuation

Represent the target as `x=3^p r-c`, with positive debt `c` and exponent
`p>=1`. For an actual source gap `3r+1=2^a u`, define the companion map

\[
F(c)=\begin{cases}c/2,&c\text{ even},\\(3c-1)/2,&c\text{ odd},\end{cases}
\]

and let `K_a(c)` count its odd steps in the first `a` transitions. The new
Lean reflection identity is

\[
x+c=2^a q\quad\Longrightarrow\quad
T^a(x)+F^a(c)=3^{K_a(c)}q.
\]

It gives the full carry update

\[
d=c+3^{p-1},\qquad c'=F^a(d),\qquad p'=p-1+K_a(d),
\qquad \boxed{T^a(x)+c'=3^{p'}u.}
\]

The total finite compiler handles arbitrary source gaps, debt states,
exponents, and word lengths while preserving the exact consumed prefix and
literal remaining certificate. A zero-exponent exit supplies a genuine
smaller target, and its use in the complete-source induction is checked.

The compiler also proves a larger successful language with states
`D1(r)=3r-1`, `D2(r)=9r-1`, and the new `E(r)=3r-2`. In particular,

\[
D_2\xrightarrow{1}E\xrightarrow{2^*}E\xrightarrow{4}D_2
\]

permits arbitrarily many gap-four letters before a successful exit, with
arbitrary runs of twos and an untouched supplied suffix. The proof is
induction over the complete accepted language, not bounded enumeration.

Total arithmetic continuation is distinct from universal successful
dispatch. At terminal source 1, repeated gap-two padding exactly simulates
`T^2` on every positive target. That fact, and the all-exponent fixed debt
states representing absorbed targets 1 and 2, are themselves Lean-checked.

[Carry proofs, grammar, and terminal boundary](WITNESS_ATTACK.md) ·
[WitnessCritical.lean](lean/WitnessCritical.lean)

## 3. A compact actual Green map with a proved infinite-output tail

On the nonperiodic positive odd units, kill forward transport upon entering
any periodic orbit. Let `L` retain actual original-source mass and put
`S=sum_(j>=0) L^j`. The new written estimate is

\[
\|Sa\|_{\ell^1(q^{-s})}\le C_s\|a\|_1,
\qquad
\|(I-Q_X)Sa\|_{\ell^1(q^{-s})}
\le C_s X^{39/40-s}\|a\|_1,
\quad C_s=\frac{5s}{s-39/40},
\]

for `s>39/40`, where `Q_X` truncates output height. Thus the complete Green
map is compact between those two specified spaces. At `s=1`, the constant
is 200 and the output tail is `200 X^(-1/40)`. The note also gives a
finite-source/finite-output approximation of the canonical immigration
correction `nu-h` with explicit errors.

The functional-analytic boundary is exact. The convergent ladder

\[
n_j=(40\cdot64^j-1)/3,\qquad U(n_j)=5,\qquad U^2(n_j)=1
\]

has vanishing input norm in `ell1(q^-s)` but constant output `delta_5`.
Hence `L` is **not closable** in the spatially weighted output space.
The same ladder proves that input-height and ordinary shortcut-clock
truncations have operator-norm error at least `5^-s`. The full note keeps
ordinary-clock and odd-depth truncations distinct.

The ladder and the vanishing-input/fixed-output implication are formalized;
Banach-space compactness and nonclosability are written arguments. No
finite-dimensional spectral calculation is substituted for the missing
critical estimate.

[Green map, approximation, and exact obstruction](POTENTIAL_ATTACK.md) ·
[PotentialCritical.lean](lean/PotentialCritical.lean)

## Formal scope and reproduction

Four new Lean modules contain **42 audited public theorems**:

| Module | Public theorems | Scope |
|---|---:|---|
| ReturnCritical | 4 | Actual return clock and complete-fiber quadratic accounting |
| WitnessCritical | 16 | Reflection, arbitrary-gap compiler, exact grade transfer, successful language, terminal behavior |
| PotentialCritical | 13 | Actual cofinal ladder, convergence, pushforward, vanishing-weight obstruction |
| LognormalClock | 9 | All polynomial clock moments, exact source absorption, completed-square parameter loss |

The [manifest](DEPENDENCIES.json) pins eight byte-identical local sources
to the published baseline. The replay rebuilds those eight, the four new
modules, and the combined audit into a fresh directory: **13 modules**.
It rejects nonstandard theorem axioms and treats warnings as errors.

```sh
python research/lean-critical-20261122/check_lean.py \
  --mathlib /path/to/built/mathlib4 --lean /path/to/lean \
  --report-dir reports/2026-11-22-critical-pass
```

Lean is pinned to 4.34.1 and Mathlib to
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The infinite measures, general
Lp arguments, return-family composition, imported Diophantine estimate,
and Green-operator analysis retain their written-proof status.

[Independent review record](REVIEW.md) ·
[Lean receipt](../../reports/2026-11-22-critical-pass/lean-check.json) ·
[Compiler log](../../reports/2026-11-22-critical-pass/lean-build.log)
