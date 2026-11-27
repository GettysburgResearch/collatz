# A nonlinear comparison at the same ordinary source

**Open proposal, with a proved conditional consequence.** The new
[critical sibling identity](../global/CRITICAL_SIBLING_SCENERY.md) reduces
the escape attack to a lower comparison between two cells of the very same
finite ternary law. This note records a stronger, particularly concrete
candidate and an exploratory calculation directed at it. No lower comparison
in this note has been established.

Let `rho_j(y)` be the original geometric-word ternary density at depth `j`,
normalized to have Haar mean one. For a positive odd ternary unit `y`, let
`s(y)` be the unique ternary unit among `4y+1` and `16y+5`. Each is a true
odd parent of `U(y)`, with the same forward successor as `y`.

The proposed inequality is the existence of an absolute `c > 0` such that

\[
              \rho_j(s(y))\ \ge c\,\frac{\rho_j(y)^2}{y}
                    \qquad(j\ge0,\ y>0\text{ odd},\ 3\nmid y).       \tag{Q}
\]

The actual positive integer in the denominator is essential. This is not a
uniform comparison on arbitrary ternary points, and no extension to negative
integer pins is proposed. At a moving source `a_j=U^j(a)` of one hypothetical
escape, its original word guarantees `rho_j(a_j)/a_j >= 1/P(a)`.
Thus (Q) would give a positive uniform lower bound for the ratio of side mass
to trunk mass. Their exact sum is finite, by the linked critical identity,
which would exclude escape. The weaker bound

\[
 \frac{\rho_j(s(a_j))}{\rho_j(a_j)}
           \ge\frac{c_a}{j\log(j+2)}
\]

for all sufficiently large `j` would already suffice. It concerns the
unmodified original word measure and one fixed ordinary starting integer.

## Why the quadratic form is a full-scale target

Along an ordinary path set `G_j=3^j/2^{S_j}` and
`Q_j=rho_j(a_j)/G_j`. Before a repeated state, the exact side partition gives

\[
 Q_{j+1}-Q_j\ge4^{-d_j}\frac{\rho_j(s(a_j))}{G_j},\qquad d_j\in\{1,2\}.
\]

The finite-simple-path reciprocal product gives `a_j/G_j <= C_0 a`.
At nonperiodic targets the published first-hit bound is
`rho_j(y) <= K y`. It follows that `1 <= Q_j <= C_0 K a`, while (Q) would give
`Q_(j+1)-Q_j >= (c/(16 C_0 a)) Q_j^2`.
For any positive sequence bounded by `M` and satisfying a quadratic gain
`q_(j+1) >= q_j + delta q_j^2`, the exact reciprocal estimate is

\[
 \frac1{q_j}-\frac1{q_{j+1}}
       \ge\frac{\delta}{1+\delta M},\qquad
 K<M+\frac1\delta\quad(q_0\ge1).                                  \tag{1}
\]

The resulting nonperiodic duration is `O(a)`, rather than a prescribed
logarithmic clock. [ReciprocalGrowth.lean](ReciprocalGrowth.lean) contains
the explicit finite inequality and horizon statement; its hypotheses
retain the upper bound and quadratic gain.

For an eventually periodic path with preperiod `r` and period `L`, apply
the same argument only while `j < max(r,L)`. If `j<r`, the target is
nonperiodic. Otherwise `j<L`, so every depth-`j` path ending at that
cycle point is a first visit: no complete lap fits. The uniform first-hit
bound still applies, with its stated factor two. This bounds both `r` and
`L` by `O(a)`. The unrestricted raw bound at a periodic target has a lap
factor and is not substituted for the first-hit bound.
[Weaver, *First-landing bounds and canonical inverse laws for Collatz*,
Corollary 5 and its first-hit proof](https://rstation.ai/problems/collatz/papers/12).

The cycle consequence of (Q) is recorded in the companion critical note:
the canonical trace, an absolute reciprocal predecessor floor, and the
ordinary reciprocal tail force a positive lower bound for the loss around
any cycle. That bounds the minimum of every cycle. A complete proof by this
route would therefore need (Q), effective constants sufficient for the
remaining finite range, and exact convergence checks on that range. Neither
the proposed inequality nor those effective constants are supplied here.

## A finite probe of the actual rows

The [exploratory C++ program](probe_sibling.cpp) computes the original
ternary rows by the exact functional recurrence

\[
 \rho_j(y)=\tfrac12\rho_j(2y)
     +\tfrac32\mathbf1_{y\equiv2\ (3)}\rho_{j-1}((2y-1)/3),
       \qquad \rho_0=1.
\]

The doubling map runs through every unit modulo `3^j`; a cyclic backward
geometric sum supplies the row. The implementation uses floating point,
so it is a hypothesis probe, not a certified inequality. It compares the
same row at both actual positive odd representatives and their specified
siblings. The [retained output](../../../reports/astra-diagonal-20261127/operator/SIBLING_EXPLORATORY.json)
scans all positive odd representatives below `2*3^j` for `j=1,...,16`.

The minimum of `y*rho_j(s(y))/rho_j(y)^2` is about `0.0211187` in the last
row, attained at `y=593`, `s(y)=9493`. This forces any constant in (Q) to
be no larger than that value, if the numerical row is accurate. The source
593 lies on the known trajectory from 27. The smallest raw side/trunk
ratio in that row is approximately `0.000212631`; a large comparison
constant is therefore already implausible. The mean-density error was
below `2.1e-13`, and the largest recurrence residual below `4.3e-14`.
These diagnostics do not turn floating-point output into an exact proof,
nor do sixteen finite rows establish a positive all-depth constant.

The first-power Haar lower bound in
[FIRST_POWER_HAAR.md](../escape/FIRST_POWER_HAAR.md) supplies an absolute
positive floor for each fixed terminal cylinder. Once normalized by
`rho_j(a_j)`, it loses precisely the growing trunk density. The target
here is a nonlinear estimate that recovers that density from the exact
ordinary arithmetic; the general positive-cone uniqueness argument alone
does not supply it.
