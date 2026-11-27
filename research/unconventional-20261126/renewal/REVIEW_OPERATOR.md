# Independent check of the ordinary-graph operator packet

Reviewed on 26 November 2026 in the PR201 worktree based at
`94ce06ccbd312ccd0ce4450b567cc514a2f0b54a`. The sibling files were
uncommitted when inspected; these SHA-256 pins identify the exact
reviewed bytes. The results below apply only to those versions.

| File under `../operator/` | SHA-256 | Mathematical verdict |
|---|---|---|
| `LOCAL_SPECTRUM.md` | `18d958621d9065518ca00dffe4d45d3b15789bca7a55c7f3e5825154f174f22e` | VERIFIED for OP-L1--L4, with the all-moduli conclusion source-qualified to Monks |
| `CORE_HEAT.md` | `4c858682a8ab270d937b02f6036819cd6ba0936986e14e2abbff325d89c87d99` | VERIFIED for OP-G1--G3 on the stipulated unweighted multigraph |
| `IMPEDANCE.md` | `b7984a940c641f3b67fb7ae327a8ba665b1c65f689d0dbecf17f949b0abaa8a9` | VERIFIED for OP-I1--I4, including the ordinary off-cycle domain |
| `HEIGHT.md` | `f3a48e9fe0ecbfb5ba1fb920ac64bf0639570b1ab9adec5fafe57ad39798af92` | VERIFIED for OP-H1--H3 with the pinned finite inequalities |
| `controls.py` | `a42cc3f4e0fce399ac9f5c61171efdbe2c3d2cf75e1a16712ef86fdf5fc7f9a1` | Source inspected and replayed |
| `CONTROLS.json` | `77a752c7969ee0b3311fc8b051e9c73558d611f4130dd9912acf62319f5c28a4` | Replay output matched byte for byte |

**Local copies and spectrum.** A prescribed shortcut prefix of length
$K$ is unchanged on a residue modulo $2^K$ and translates its endpoint
by $3^qs$ when its source translates by $2^Ks$. The first odd step
removes a factor of three from the endpoint class even if the source
was a multiple of three. The primitive root 2 modulo $3^h$ permits
arbitrarily high powers of two in the prescribed unit residue. The
affine path formulas have positive slopes, so all transported vertices
eventually become positive. Nonidentical affine maps have at most one
coincidence, which handles possible extra edges, including the extra
parallel edge at the known cycle. Complete branch guards at all
interior vertices preclude unlisted neighbors. A finite tree
inspection around the whole output support therefore preserves the
entire residual norm of a finite-propagation Weyl test vector.

For OP-L3 I checked the partition-of-unity argument as a rowwise
estimate. Cauchy--Schwarz contributes at most $D_r$ matrix terms per
row. Summing over the localized centers uses squared Hellinger
distance at most the $\ell^1$ distance of the endpoint empirical
measures. A path of at most $r$ edges costs at most $2r/N$; the
remaining sum of squared matrix entries in a column is at most
$\|A\|^2$. A weighted average then supplies one nonzero localized
vector of the asserted residual cost. Distinct cycles in one
component would contradict coalescence; a ball containing a whole
cycle of length $p$ must have radius at least $\lfloor p/2\rfloor$.
Only finitely many cycles have bounded length by the parity-word
affine fixed-point equation. Removing a finite thickening of the short
cycles from a singular Weyl sequence leaves arbitrarily good
finite-support tests there. The localized ball is a tree even for
components surrounding an undetected long cycle. Simple extension by
zero proves the other essential-spectrum inclusion. Neither argument
transfers isolated eigenvalues associated with a cyclic defect.

For OP-L4 I checked the primary statement and definition of
sufficiency in Kenneth M. Monks, *The sufficiency of arithmetic
progressions for the 3x+1 conjecture*, Theorem 1.1. It concerns the
same ordinary shortcut and intersects every forward-merging class via
a representative of each progression. Shifting the progression gives
arbitrarily large representatives. This checks the cited interface;
it is not a new proof of Monks's theorem.
[Primary paper](https://monks.scranton.edu/content/pubs/SufficiencyRev4.pdf)

**Core, half-lines and heat.** The odd inverse stays a unit precisely
at residues 2 and 8 modulo 9 and supplies the unique nonunit hair at
5. The doubling cycle of six unit residues gives at most three unary
doublings to the first branch and five to the first attachment.
Depth-three and depth-four levels at 7 certify both sharp cases.
Summing unit indegree minus outdegree over a finite set counts the
branch vertices by oriented boundary flux, including both directions
of the $1,2$ bigon. A doubling segment charges any branch at most four
times or any first outgoing boundary edge at most three times. This
gives boundary at least $|S|/7$. Coarea and maximum degree three
give $\langle f,L_U f\rangle\ge\|f\|^2/294$ with multiplicities retained.

For the full resolvent each half-line contributes $1-\rho$ on its
attachment, where the square-summable root has $\rho+\rho^{-1}=2+z$.
Solving the finite Dirichlet recurrence separately at $z=1/2$ gave
$f_1/f_0=\rho(1-\rho^{2m})/(1-\rho^{2m+2})$ for
$m=1,2,3,7,15,23$, exactly as rational numbers. The limiting
resolvent has the singular term $-\sqrt z\,G1_HG$ with the sign needed
for a positive spectral density. The bounded inverse of $L_U$ gives
norm analyticity in $\sqrt z$ near zero. Self-adjoint coefficients kill
the imaginary parts of all even powers on the upper lip of the cut.
The scalar Stieltjes inversion argument identifies the continuous
density, with no compressed zero atom. Integrating the bound uniformly
gives the displayed $t^{-3/2}$ coefficient and $O(t^{-5/2})$
remainder after restriction to the units. No inference about full
semigroup-norm decay enters. The geometric series for $G$ uses the
nonnegative symmetric uniformized kernel; bounding the upper form of
$|f|$ also bounds the absolute value of the lower spectral edge.
One attachment within five edges gives the lower Green-square
estimate, and finite propagation in the two powers of that kernel
gives the upper one.

**Impedance, hitting probabilities and error bounds.** Splitting current
equally down a binary tree with branch-to-branch distance at most four
uses at most four energy units beyond the first branch plus at most
three initial units. At most $2^k$ edges at depth $k$ force energy
at least one by flux conservation. The unit-parent and descendant
resistances in parallel give $h=R/(1+R)$. Killing at depth $r$ misses
at most the product of $r+1$ upward hit probabilities, each at most
$7/8$. An odd inverse loses just one ternary digit, and a branching
test uses two. Thus a residue modulo $3^{r+1}$ determines the needed
finite probability. The resulting Hölder and flux identities follow
with their claimed powers. As a separate check I evaluated exact
rational depth-ten parent bounds with leaf conditions $1/2,7/8$ at
ten ordinary roots; at 1 the interval was approximately
$[0.758045,0.774896]$ and at 7 $[0.833980,0.849240]$.

The descendants of an off-cycle ordinary unit truly form the unfolded
tree, since a coincidence at different depths would put the root on
a cycle. The hitting product therefore stops at 2; the initial state
1 has hitting probability one by its two parallel edges to 2. The
tree-separator identity gives the projection decomposition of $Q/G$.
For its lower bound an attachment serves at most eleven vertices of
the geodesic, and its projection is within five edges, which gives
the stated factor. Along doubling, a complete modulo-$3^r$ orbit
averages uniformly over the units. The martingale-difference tail
and partial-period costs give the stipulated $O(k^{1-\alpha})$.
The superlevel tree argument uses conservation of $Cf$ and overshoot
between $t/2$ and $t$; contraction of unary strings gives the two-sided
cardinality, and the factor of distance contributes exactly the
logarithm for $Q$.

**Finite certificates and extra height clauses.** The pinned checker
uses floating decimal powers only to propose two rational multipliers;
integer powers certify both outward directions. The Riccati recursion
is increasing in every child. Class lifts, denominator directions and
outward floors/ceilings are correct. The atanh remainder uses the
first omitted odd exponent 33. I checked the edge telescope, including
the odd-child ratio strictly below $2/3$. At a cyclic target at most
one fixed-depth ancestor can itself be cyclic. The explicit
all-odd good sources have the stated divisibility by LTE or the cubic
factorization and the stated double-log scale. In OP-H3 the inverse
odd map is a bijection from branching level-$r$ classes to unit
level-$(r-1)$ classes, which is required for the summed oscillation
bound. Subdivision of a cylinder accounts for the factor three in
the partial-period estimate. The optimized discrepancy exponent is
below $1/6$ because $(19/40)(29/25)^5<1$.

**Boundary.** These checks support the named local and ordinary-graph
statements, including their counterexamples to particular local proof
strategies. No estimate establishes that a prescribed vertex belongs
to the known basin. No later version, source outside these named
interfaces, or whole repository receives a review verdict here.
