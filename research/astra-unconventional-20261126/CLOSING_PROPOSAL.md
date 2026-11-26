# Closing proposal from the three-hour unconventional attack

This pass pursued ordinary positive termination through three parallel attacks: mixed-base generating functions, persistent component boundaries, and the original finite inverse law. It does **not** establish the universal Collatz theorem. The twelve new Lean modules prove the finite arithmetic and orbit interfaces listed in the [audit](../../reports/astra-unconventional-20261126/LEAN.json); the analytic arguments below are written proposals with their imported hypotheses retained.

The universal target remains that for every positive integer the shortcut orbit reaches 1. There are two independent obligations: every orbit must eventually be periodic, and the only positive cycle must be the known cycle. The reductions below keep those obligations separate.

## 1. The exact escape test reached in this pass

Let the independent positive exponents have the original probabilities $\Pr(e=j)=2^{-j}$. Set $q_k=3^k$ and $\rho_k(y)=q_k p_k(y\bmod q_k)$, with whole-Haar normalization. Sum over the complete positive odd representatives $0<y<2q_k$, and put $\Phi(u)=u^2/(1+u)$.

Under the named ordinary trace, predecessor, and minimum-law inputs, the [component-energy theorem](global/COLLISION_ENERGY.md) proves

$$
\lim_{k\to\infty}\frac1k\sum_y\Phi\!\left(\frac{\rho_k(y)}y\right)
=\sum_{C\;\mathrm{escaping}}\Phi(H_C),\qquad H_C>0.
$$

The finite expression on the left uses only the original residue probabilities. It needs no first-hit test, cycle list, or classification of the input orbits. The proof first obtains all moments of the bounded first-hit amplitudes, then removes the aggregate effect of all periodic laps by a dominated-convergence argument over disjoint cycle basins. It permits any number of additional positive cycles. The full mass-weighted spectrum also has a zero atom of mass $(\log3)/2$ and an atom of mass $H_C$ at each positive amplitude $H_C$.

There is a smaller signed target. Define, on odd integers,

$$
W(y)=\frac34-\mathbf1_{v_2(3y+1)\ge2}-\mathbf1_{v_2(3y+1)\ge3}.
$$

Its values on residues $1,3,5,7\pmod8$ are respectively $-1/4,3/4,-5/4,3/4$, with mean zero. Nevertheless every actual escaping ray has lower mean at least

$$
\delta=\frac74-\log_2 3>0.
$$

Consequently the same trace arguments give

$$
\liminf_{k\to\infty}\frac1k\sum_y W(y)\Phi\!\left(\frac{\rho_k(y)}y\right)
\ge\delta\sum_{C\;\mathrm{escaping}}\Phi(H_C).
$$

**Unproved closing estimate:** a subsequence along which the signed expression has upper limit at most zero would exclude every escaping positive orbit, under those named inputs. Neither this estimate nor the zero limit of the unsigned statistic is established here. Even either estimate would still leave positive-cycle uniqueness to prove.

The positivity of $H_C$ uses the imported ordinary atom/predecessor input. It is not a consequence of logarithmic-density-one convergence alone. The fixed-target limit comes from [Weaver's Theorem 2](https://rstation.ai/problems/collatz/papers/176), with the normalization and dependence on Valbuena stated there. The all-residue atom floor is a separate [Input D](https://rstation.ai/problems/collatz/papers/12). These sources are not among the declarations checked by the new Lean build.

## 2. What the exact transfer contributes

The [two-copy source identity](boundary/COLLISION_SOURCE.md) operates on actual nonperiodic positive vertices. With $U$ the odd map and $w_x=3x/(3x+1)$, define

$$
(A\mu)(y)=\sum_{Ux=y}w_x^2\mu(x),
$$

killing mass on entry to a periodic vertex. Squaring the ordinary one-copy recurrence yields

$$
u_{k+1}^2=A(u_k^2)+b_k,
\qquad
b_k(y)=\sum_{\substack{Ui=Uj=y\\i\ne j}}w_iw_j u_k(i)u_k(j).
$$

The distinct-parent sources converge in $\ell^1$. Their sum is controlled by disjoint first-merger events for ordered pairs of ordinary sources, not by an independence assumption on incoming branches. Their surviving contribution is exactly $\sum_C H_C^2$. This identifies the part missed by an estimate that counts only two identical inverse words.

The direct proof also restores every periodic first-hit target without a global harmonic moment estimate: decompose paths by their last parent outside the cycle, use disjoint predecessor basins at those parents, and apply the uniform reciprocal sum bound on a single cycle. Dominated convergence over all cycle basins removes their aggregate contribution. The nonperiodic energy detector therefore needs no minimum-law exhaustion or global Haar energy estimate. The finer identification by the amplitudes $H_C$ uses the additional trace-profile inputs stated in that section.

It also gives the raw clipped zero criterion directly. Uniform boundedness of the first-hit amplitude makes its square comparable to $\Phi$; the periodic-lap correction has total mass $o(k)$. Thus the finite raw clipped sum is $o(k)$ exactly when there is no ordinary escape, using the direct source theorem and its stated local inputs. The explicit component spectrum is stronger information and uses the additional global inputs.

The [dyadic increment identity](arithmetic/DYADIC_INCREMENT.md) gives another exact interface. For every positive integer $z$,

$$
u_k(z)-u_k(2z)
=\mathbf1_{z\equiv2\ (3)}\left(1-\frac1{2z}\right)
u_{k-1}\!\left(\frac{2z-1}{3}\right).
$$

Linear increments telescope within each dyadic tower. Convex clipping exposes a nonnegative splitting cost whose Cesàro mean is finite and is explicitly computed in that note. A large amplitude can be carried by one predecessor while other predecessors carry arbitrarily small mass. The actual sibling relation is $x\mapsto4x+1$. The needed lower comparison between substantial sibling amplitudes is not supplied by their reciprocal atom floors.

Two controls prevent unjustified final steps:

* The [signed-test control](global/COLLISION_ENERGY.md) constructs consistent ternary laws with a positive ordinary unit floor, critical weak-$L^2$ regularity, linear finite Haar energy, exponential approximation in $L^1$, and a positive signed statistic. Any prescribed finite set of exact Syracuse quotients can also be preserved. The density need not satisfy the exact affine fixed-point equation. Thus these regularity statements do not themselves prove cancellation.
* The [ordinary transient construction](boundary/COLLISION_SOURCE.md) realizes any finite valuation word at arbitrarily large positive heights and then reaches 1. Balanced words have a linearly positive $W$-sum while staying in a fixed multiplicative height interval. They rule out the proposed uniform upper coboundaries with bounded, logarithmic, or increasing sublinear-height potentials, even within the known basin of 1. They do not rule out an estimate using the particular summable source weights $b$.

## 3. The generating-function classification

Fix any finite upper bound $E$ on the exact division exponent. In the coordinate $t=(x-1)/2$, the ordinary branch of exponent $e$ has the form

$$
2^e v+r_e\longrightarrow3v+d_e.
$$

The [all-gap section theorem](arithmetic/ALL_GAPS_MAHLER.md) retains every incoming branch and every cancellation. A ternary coefficient section of depth $k$ is a finite sum of binary sections of depths between $k$ and $Ek$. Its coefficient identities and depth bounds are formalized in [AllGapSections.lean](arithmetic/AllGapSections.lean).

The [holonomic argument](arithmetic/HOLONOMIC_RIGIDITY.md) uses this exact transfer at three places. Levelt–Turrittin slopes at zero vanish by multiplicative independence of 2 and 3, so even initially divergent formal D-finite solutions converge. Their actual finite nonzero singularities must be roots of unity of odd order; the missing dyadic cylinder removes those singularities. The corresponding slope argument at infinity gives polynomial growth. Thus every formal complex D-finite flow solution is polynomial, and its finite support is a sum of actual finite directed cycles.

This classifies all holonomic solutions at every finite exponent ceiling. It applies to signed and complex coefficients as well as nonnegative ones. It does not discard polynomial cycle indicators. The weighted homogeneous equation with edge ratios $3/2^e$ has zero holonomic kernel, but multiplying an unweighted cycle by height introduces an inhomogeneous carry. Dropping that carry would invalidate a claimed proof of cycle exclusion.

The same section mechanism gives rational, automatic, and finite-kernel classifications through the cited two-base results. Infinite signed flows are explicitly constructed to show that the unrestricted kernel is nontrivial. The [small signed carry](arithmetic/SMALL_SIGNED_CARRY.md) is a separate arithmetic consequence for the bounded candidate family: an invertible signed stencil compresses the actual phase heights to $O((\log p)^3)$ while preserving a forced recurrence. Its signed forcing prevents interpreting it as a smaller positive Collatz cycle.

## 4. What the boundary attack excludes

A persistent ordinary component boundary has very restrictive low-bit dynamics. The [dyadic kernels](global/DYADIC_BOUNDARY.md) prove the unique-child rules, missing patterns, and the precise failure of naive multiplication-by-three invariance. They identify the actual midpoint at which a transported boundary germ ceases to be a persistent boundary.

The [paired-boundary theorem](boundary/PAIRED_BOUNDARY.md) excludes a rational persistent boundary when its two signed reference arms are eventually nonzero periodic. The proof aligns odd counts at different physical clocks, returns to actual positive integer lifts, and applies counted coalescence on a dyadic residue cylinder. A uniform forbidden-power consequence excludes specified periodic words from tail limits. One explicit necklace has a fully replayed finite certificate.

The [zero-arm calculation](global/ZERO_ARM.md) treats the missing rational cases separately. It produces a geometric-ray color obstruction, and its magnifications can leave an isolated ordinary center in a signed limit. This prevents a conclusion based solely on local limiting color relations. General aperiodic boundaries and the required geometric return remain open in this pass.

## 5. Formal and publication boundary

The [common driver](check_lean.py) compiles all twelve new modules with fresh project objects, Lean 4.34.1, pinned Mathlib, implicit variables disabled, and warnings treated as errors. Its [receipt](../../reports/astra-unconventional-20261126/LEAN.json) records source hashes and audits all **77 public theorem declarations**. Their only audited axioms are `Classical.choice`, `Quot.sound`, and `propext`.

The analytic classifications, stationary laws, energy limits, and periodic-boundary exclusion are not represented as Lean-certified universal theorems. The independent root review is in [REVIEW.md](../../reports/astra-unconventional-20261126/REVIEW.md); new exact controls and publication receipts are beside it. The earlier [overview](README.md) preserves the joint residue, moving-center, record, posterior, and ordinary-measure attacks from the first two checkpoints.

The final proposal therefore consists of a source-qualified exact escape statistic, exact ordinary transfer identities, a general holonomic classification, and boundary exclusions, with explicit unsupported closing estimates. There is no `sorry`, new axiom, or renamed hypothesis presented as a solution of universal Collatz termination.
