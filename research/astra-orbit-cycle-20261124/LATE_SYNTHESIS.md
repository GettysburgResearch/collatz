# Consequences of the concurrent carry and merger packets

**Status: written deductions from the exact source pins below. Collatz remains OPEN.** PR194 and PR195 appeared during publication of the initial PR196 packet. The original eleven Lean files, their hashes and their 83-declaration replay are unchanged. The deductions in this note are not additional Lean theorems.

## LS-A. Transfer of the improved restricted occupation exponent

PR194 at `b1bf1f151a2da8936f80d229f132d0b7539ba42c`, `research/astra-birth-rigidity-20261124/OCCUPATION.md`, ABR3 and its final subsection, proves the following on the set of states of one injective actual odd orbit: if its canonical factor complexity satisfies log p_b(m)=o(m), then

\[
F(X)=\#\{n:q_n\le X\}=O_{q_0}(X^{17/25}).
\]

Its strict counting margin absorbs the subexponential number of canonical words. Whole-set forward invariance and injectivity are essential. The finite-phase variant has the factor L for L actual phases. The source-dependent bound for a single orbit is all that is needed here; no estimate over a translated interval is inferred.

Apply [the exceptional-clock inequality](occupation/CARRY_OCCUPATION.md), equation (3), to this **same** orbit. With C=q_0 E_* finite, for X>=1 it gives

\[
\#\{n:P_n\le X\}\le F(CX)+O_{q_0}(1+\log\log(3X))
=O_{q_0}(X^{17/25}).
\]

Equivalently the anchored quantities q_0 P_n have this exponent, with a source-dependent constant. No logarithmic loss in the physical exponent is needed. The reciprocal correction bound used to define E_* was already available unconditionally on injective orbits, so this combination is not circular.

The conclusion supplies a stronger restricted occupation bound. It does not force enough low multipliers to contradict that bound. PR194's convergent inverse tree cannot be inserted into this counting step, since distinct basin sources coalesce at the common clock. The [carry review](../../reports/astra-review-20261124/ADDENDUM_PR194_CARRY.md) reconstructs the partition, entropy, occupation and conditional collision statements and this transfer.

## LS-B. A later merger inside the complementary half-size class

PR195 at `a24ef018147a1e16bf314d14085e2d0d6c620d32`, `research/astra-global-closure-20261124/structural/README.md`, supplies the guarded family with positive integers k and u:

\[
k\equiv148\pmod{256},\qquad
n=2^{33k}u-17,\qquad m=2^{21k}u-1,\qquad u>0.
\]

Under its stated member-endpoint divisibility guard, 0<m<n and

\[
T^{33k+10}(n)=T^{21k+10}(m),
\]

with exactly 21k+3 odd inputs on each arm. These are actual ordinary identities, not a merely 2-adic meeting.

For every source in this family,

\[
v_2(n+1)=4,\qquad
M=(n+1)/16=2^{33k-4}u-1\equiv3\pmod4.
\]

Thus 3^4 M is 3 modulo 4. **The entire guarded PR195 family lies in the complementary class left open by our half-size rule.** It supplies a new explicit subfamily of that complement, without covering every member of the class.

The PR195 lifting construction permits simultaneously imposing n=1 modulo 3^(33k). On these lifts our [two-anchor theorem](mergers/TWO_ANCHOR_MERGERS.md) applies with H=4 and A=33k. Consequently every smaller partner at forward clock h<=4 needs at least h+33k+1 odd inputs, whatever its own clock. At forward clock 5 the lower bound is 33k+5. Nevertheless the displayed later merger at forward clock 33k+10 uses only 21k+3 odd inputs on the partner arm and has zero odd excess. The comparison concerns the same supplied source at different forward clocks.

PR195's separate all-walk theorem bounds total forward-plus-inverse edge length on its selected lifts. Our barrier bounds odd inputs at a specified target clock; these are different quantities. Both allow the later ordinary merger. The [merger review](../../reports/astra-review-20261124/ADDENDUM_PR195_MERGERS.md) reconstructs the negative-cycle shifts, the ten-step bridge, the lift conditions, and the finite-state affine obstruction with their formal boundaries.

## What the combined work still needs

The carry bounds remain upper bounds on occupation or lower bounds on growth and separation. The merger families remain guarded ordinary constructions. Their combination does not force an arbitrary least nonconverger into a successful guard with a partner smaller than that original source.

The companion [cycle review](../../reports/astra-review-20261124/ADDENDUM_PR194_CYCLES.md) keeps top-component nonvanishing separate from survival of the complete numerical denominator. Its exponential denominator bound on a mixed-prime family and our rotational divisor both need a specified matching structure. The [analytic review](../../reports/astra-review-20261124/LATE_ANALYTIC_REVIEW.md) confirms the clock-series criterion and the overlapping reducible substitution proofs at written scope. Neither provides the required analytic structure for every ordinary itinerary. Universal convergence and unrestricted nonstandard-cycle exclusion remain unproved.
