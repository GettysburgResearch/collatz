# A rational ordinary energy without a stopping-time hypothesis

**Status: exact finite proposal; the implication to the usual Collatz statement
is checked in [RationalEnergy.lean](RationalEnergy.lean). Its two premises are
open.** The written converse below shows that this criterion imposes no extra
logarithmic stopping-time requirement.

Use the actual positive odd map `U`, and define the rational multiplier

\[
 d(n)=\begin{cases}
  1/4,&n<13,\\
  1+1/(32n^2),&n\ge13.
 \end{cases}
 \qquad D_k(x)=\prod_{i<k}d(U^ix).
\]

For natural `K,H,y`, let

\[
 E_{K,H}(y)=\sum_{k=0}^K\sum_{\substack{1\le x\le H\\x\text{ odd}\\U^kx=y}}
                    \frac{D_k(x)}{x^3}.                         \tag{1}
\]

These are finite rational sums over actual ordinary trajectories, with every
visit counted. Values at zero and even targets are zero. The entire proposed
criterion is

\[
 \begin{split}
 &E_{K,H}(y)\le8 \quad\text{for every }K,H,y,                 \tag{2}\\
 &\forall\varepsilon\in\mathbb Q_{>0}\ \exists Y\in\mathbb N\
   \forall K,H\in\mathbb N\ \forall y\ge Y,\qquad
   E_{K,H}(y)\le\varepsilon .                                \tag{3}
 \end{split}
\]

In (3), **only the target `y` is required to be at least `Y`; both cutoffs
`K,H` are arbitrary natural numbers.** The explicit Lean definition is
`∀ ε : ℚ, 0 < ε → ∃ Y : ℕ, ∀ K H y : ℕ, Y ≤ y → ...`.

## Complete conditional implication

Suppose a positive odd source `n` never reaches an odd state below 13. Every
factor on its path is at least one. Its own term in (1) therefore gives
`E_(k,n)(U^k n)>=1/n³` at every depth. Apply (3) with `ε=1/(2*n³)`:
all its states must be below one fixed integer `Y`.

On this bounded set each multiplier is at least `1+1/(32*Y²)`. Consequently
`D_k(n)` increases by at least `1/(32*Y²)` per step and is unbounded. But its
own term and (2) give `D_k(n)<=8*n³`. This contradiction supplies a finite
visit below 13. Checked trajectories from 1, 3, 5, 7, 9 and 11, together with
exact halving to the odd part, finish the implication for the usual full map.

This proof handles both alternatives at once. It does not presume that the
orbit is periodic or escaping, nor call a density theorem. The Lean theorem
`energy_criterion_implies_collatz` retains (2) and (3) as its hypotheses.

## Why convergence would imply the criterion

There is an elementary bound on **every finite simple positive path**,
independent of its length. For every integer `m>=13`,

\[
 1+\frac1{32m^2}\le\frac{(m+1)^2}{m(m+2)}.
\]

The right side exceeds one. The product over any distinct set of such
integers, embedded in the full interval `13,...,N`, is therefore at most

\[
 \prod_{m=13}^N\frac{(m+1)^2}{m(m+2)}
       =\frac{14}{13}\frac{N+1}{N+2}<\frac{14}{13}<2.             \tag{4}
\]

The small-state factors are at most one. Thus each source contributes at most
`2/x³` to a nonperiodic target, which it can visit at most once. Since
`sum_(x>=1) x^-3 <= 2`, every nonperiodic target has `E_(K,H)(y)<=4`
**unconditionally**, even if some positive trajectory escapes.

At target 1, the first-hit path is simple and each later visit introduces
another factor `1/4`. The geometric sum is `4/3`. Hence
`E_(K,H)(1)<=16/3<8`, also unconditionally. If all positive orbits reach 1,
every other target is nonperiodic, proving (2). Conversely any additional
positive cycle has only states at least 13; its product of `d` factors is
strictly larger than one, and its repeated visits violate (2). Thus the
uniform bound in (2) is itself equivalent to uniqueness of the positive cycle.
These equivalence directions are written mathematics here; the current Lean
module formalizes the joint conditional implication.

Assume now that every positive source reaches 1, and fix an ordinary source
cutoff `M`. The finitely many trajectories from odd sources at most `M` visit
only finitely many targets. Choose `Y` above all of them. At `y>=Y`, only
sources larger than `M` can contribute, and each visits `y` at most once.
The uniform tail bound is

\[
 E_{K,H}(y)\le2\sum_{x>M}x^{-3}\le\frac1{M^2}\qquad(M\ge1).    \tag{5}
\]

The last estimate is the integral comparison for the decreasing function
`t^-3`. This proves (3), with no estimate on the time needed for the finitely
many small-source trajectories to finish. Therefore the displayed criterion
is equivalent to full positive convergence in ordinary mathematics.

## Connection to the integrable prefix-adaptive Green series

The [adaptive Green construction](../global/ADAPTIVE_GREEN.md) uses

\[
 b(r)=1+\frac1{2\max(r,13)}+\frac1{12\max(r,13)^2},\qquad
 w_x=\frac{3x}{3x+1}.
\]

For a prefix's least positive odd ternary representative `r<=x`, monotonicity
gives `b(r)>=b(x)`. For `x>=13`, an exact identity is

\[
 b(x)^2w_x^3-1
   =\frac{36x^2+20x+3}{16x(3x+1)^3}
   \ge\frac9{256x^2}>\frac1{32x^2}.
\]

For `1<=x<13`, `b(r)^2*w_x³ >= (3/4)³ > 1/4`. Thus the normalized square
of each unrounded adaptive word weight dominates the corresponding summand
in (1). Positivity also bounds the sum of these squares by the square of their
sum. Consequently, with the same finite restrictions,

\[
             E_{K,H}(y)\le \left(\frac{G(y)}{y^{3/2}}\right)^2.
\]

For the entirely rational rounded series `G^Q`, the one-time rounding factor
in that note gives instead `E_(K,H)(y)<=6*(G^Q(y))²/y³`. This supplies a
precise interface from an integrable finite-ternary-word construction to the
finite rational Lean proposal. Haar integrability alone does not provide its
ordinary-point finiteness or target decay. Those are the remaining estimates.

No instance of `EnergyCriterion` is supplied. In particular neither the
constant 8 nor the tail assertion is presented as an established bound at all
ordinary targets.
