# A lower-tail obstruction for ordinary height functions

**Proposed mathematical theorem.** Let `u(n)>0` on the ordinary positive integers. Assume the one-edge inequality

\[
 u(Tn)\ge w(n)u(n),\qquad w(n)=\begin{cases}1/4&n\mathrm{\ even},\\9/4&n\mathrm{\ odd}.\end{cases}
\]

It follows, in particular, from an inverse supersolution `u(y)≥Σ_{Tx=y}w(x)u(x)`. If `u(n)≤K n^α` for all sufficiently large `n`, where `α<2`, then within **every fixed positive arithmetic progression** the normalized values `u(n)/n^α` have this lower tail: for all small `ε>0`, their lower relative natural density below `ε` is at least

\[
                  c\,\varepsilon^{1/(2-\alpha)} .
\]

Here `c>0` can depend on `α,K` and the progression. Lower relative density means the lower density inside the progression divided by its ordinary density. The exponent improves the bound obtainable from one all-odd word. In particular on each such progression the Cesàro means of `(n^α/u(n))^q` tend to infinity for every `q≥1/(2−α)`.

No nonzero nonnegative lower-semicontinuous function on the profinite integers can serve as a lower asymptotic profile of these normalized values, even if the lower bound is required only in natural density. More precisely, if `F≥0` is lower-semicontinuous on the profinite completion and, for each `η>0`, the set of positive integers with `u(n)/n^α<F(n)−η` has zero upper natural density, then `F` is identically zero. The same holds on the 2-adic integers and for continuous periodic profiles. A uniform or a sequential asymptotic profile is a special case. A sequential profile means that for each profinite `ξ` and every sequence of positive integers tending to infinity in the usual sense and to `ξ` profinitely, the normalized values approach `F(ξ)`. Compactness then gives the uniform approximation when `F` is continuous.

## Proof from finite parity cylinders

Fix an initial progression `n≡r (mod m)`. Write `m=2^a b` with `b` odd. The first `a` parity bits are fixed and have some positive product of slopes `A₀`. After these steps, on the free higher binary digits, each length-`j` future parity word has probability exactly `2^{-j}`. This is an exact assertion on residues of the original positive inputs. The shortcut branch at a fixed initial bit replaces the free integer parameter by an odd-coefficient affine form, so recursively either next parity has exactly one of the two next input lifts. The odd part of the original modulus is compatible by the Chinese remainder theorem. Each cylinder of length `j` therefore has relative natural density `2^{-j}` on the original progression.

Write `A_j` for the slope product of these `j` fresh bits. The respective factors are `1/2,3/2`, with equal probabilities, so `A_j` is a nonnegative mean-one martingale. For `H>1`, stop at its first crossing `τ` of level `H`. On a hit, `H≤A_τ<3H/2`. For any fixed `0<θ<1` put `ρ_θ=((1/2)^θ+(3/2)^θ)/2<1` by strict concavity. At a finite horizon `J`,

\[
  1=\mathbb E(A_\tau;\tau\le J)+\mathbb E(A_J;\tau>J),\qquad
  0\le\mathbb E(A_J;\tau>J)\le H^{1-\theta}\rho_\theta^J .
\]

The stopping identity follows directly by averaging the two equal-probability continuations at each unfinished word. Thus the total cylinder probability of ever hitting `H` lies between `2/(3H)` and `1/H`. All uses for ordinary densities may be made at finite `J` before taking a limit.

For one successful word the true physical endpoint has the form `y=A₀A_τ n+B` with fixed nonnegative offset `B`. Multiplying the edge inequalities gives `u(n)≤(A₀ A_τ)^(-2)u(y)`. As `n` increases in that cylinder, `y/n→A₀ A_τ`. Consequently, on all its sufficiently large ordinary lifts,

\[
       u(n)/n^\alpha < 2K (A_0 H)^{\alpha-2}.
\]

The constant 2 allows either sign of `α`; `y>0` tends to infinity. At every finite horizon only finitely many disjoint successful cylinders occur; their finite exceptional heads do not affect density. Sending the horizon upward and then setting `2K(A₀H)^(α−2)=ε` gives the stated tail. The argument also gives a full smaller arithmetic progression, on which the displayed inequality holds for every sufficiently large lift, inside any given arithmetic progression: one may simply use a sufficiently long all-odd continuation.

For the moment consequence, the reciprocal variable `Z=n^α/u(n)` has lower relative density at least `c t^{-β}` above `t` for all large fixed `t`, where `β=1/(2−α)`. Apply the finite layer-cake integral to its empirical distribution up to any fixed truncation `R` and pass to a lower limit using Fatou. The resulting lower bound is proportional to `∫^R t^{q−β−1}dt`. Letting `R→∞` proves divergence, including the borderline case. For the profile consequence, if `F(ξ)>0`, lower semicontinuity gives a residue neighborhood on which `F>2η` for some `η>0`. The low-valued cells just constructed contradict a density-zero exceptional set on that neighborhood.

## Quantitative finite-height version

For any `0<δ<(3/4)log₂3−1` and all sufficiently large `X`, at least `c_m X^(1−δ)` starts in the given progression within `[X,2X]` satisfy

\[
             u(n)/n^\alpha \le C_{m,\alpha,K}\,X^{-\delta(2-\alpha)} .
\]

Take `H=X^δ` and `J=⌊log₂(X/(4m))⌋`. The complete modulus of every horizon-`J` joint test divides `m 2^J≤X/4`. At least a fixed fraction of the interval is covered by complete periods, including the original residue condition. Choose `θ<1` sufficiently close to 1 that `δ(1−θ)<−log₂ρ_θ`. This is possible because `−log₂ρ_θ/(1−θ)→(3/4)log₂3−1`, the derivative at 1. The preceding remainder bound is then `o(1)`, so by time `J` at least `(1−o(1))2/(3H)` of the admissible residues have crossed. For every such start, with full time `h=a+τ`, transporting `n+1` as in [the fiber interval](OPERATOR_SPECTRUM.md) gives `y+1≤A₀ A_τ(n+2^h)`. Here `2^h≤2^a2^J≤X`; also `y≥A₀ A_τ n`. These uniform bounds replace the per-cylinder limit and yield the quantitative statement.

## Why a height function would matter

If there exists a strictly positive `u(n)=o(n²)` satisfying the one-edge inequality, every ordinary positive trajectory is bounded. An escaping trajectory is simple, and the ordinary reciprocal packing estimate gives `T^k n=n A_k D_k` where `1≤D_k≤D_*` and `A_k` is the product of its unsquared slopes. Thus `u(T^k n)/(T^k n)²≥u(n)/(n²D_*²)>0` for all `k`, contrary to the subquadratic limit as its distinct integer states tend to infinity. This implication leaves the separate cycle question. The elementary edgewise criterion differs from the previously studied strict summable inverse supersolution for the killed map in `research/astra-critical-mass/CONTINUATION.md`, T-ASTRA-009. The present contribution is the quantitative restriction on the value distribution of any candidate.

In fact the unboundedness question admits an elementary extremal height `U(y)=sup{A_k(n)²:T^k n=y, n≥1, k≥0}`. The empty path gives `U≥1`, every positive endpoint law gives `U(y)≤y²`, and appending the next edge gives `U(Ty)≥w(y)U(y)`. If every ordinary trajectory is bounded, the least starting height among all paths to `y` tends to infinity as `y→∞`, since a finite set of sources then visits only finitely many vertices. Hence `U(y)=o(y²)` by the same endpoint law. There is no proved uniform subquadratic estimate for this extremum. The lower-tail theorem severely restricts how a replacement with a fixed subquadratic polynomial bound could depend on residues.
