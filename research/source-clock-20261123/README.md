# Actual boundary dimension and the retained source clock

Date: 2026-11-23. Base: PR180 at
`04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`.

**Collatz remains OPEN.** This checkpoint develops three parallel attempts
against the actual-source step. Its strongest new result concerns the
probability law of the canonical real boundary: upper local dimension one
almost everywhere and a strictly positive lower Shannon information
dimension. The written infinite conclusions retain explicit analytic
inputs. Neither escape nor nontrivial positive cycles are excluded.

## 1. The actual boundary measure now has dimension bounds

[BOUNDARY_OVERLAP.md](BOUNDARY_OVERLAP.md) treats a fixed nonperiodic
positive odd ternary-unit root `q`, the supplied critical harmonic trace
`F`, and its actual inverse kernel

\[
 K_F(q,n)=\mathbf1_{Un=q}\frac3{2^{e(n)}}\frac{F(n)}{F(q)}.
\]

If `A_r` is the realized valuation total, put

\[
 a_r=3^r2^{-A_r},\qquad
 R_r=\sum_{j=1}^r3^{j-1}2^{-A_j},\qquad
 q=R_r+a_rX_r,\qquad R=\lim_rR_r.
\]

The probability of each exact prefix is `a_r F(X_r)/F(q)`. All measures
below retain these probabilities. With `mu_q=Law(R)`, the new theorem is

\[
 \overline{\dim}_{\rm loc}\mu_q(R)=1
 \quad\text{almost surely}.
\]

It also holds for the actual common component boundary law `mu_E` and its
bounded positive tilts. In particular these real measures are nonatomic.
The previous packet established dimension one for the support under its
routing input; the present statement concerns the supplied measure itself.
Upper local dimension is not being relabeled as lower local or Hausdorff
dimension.

The central new inequality is a floor for an entire inverse cone. At any
endpoint with `F(n)<=B`, an ancestor `u` contributes a positive term with
actual multiplier `omega`. Harmonicity, `F(u)>=alpha`, and the actual
path product lower bound imply

\[
 F(n)\ge\alpha\omega,
 \qquad \omega u/n\ge\delta,
 \qquad u\ge(\alpha\delta/B)n.
\]

Consequently every continuation has real tail at most `D a_r^(1/40)`.
At fixed depth and valuation total, integer endpoints separate the prefix
offsets by `2a_r`. Multiplying this exact count by the original cylinder
weights bounds the mass of a cell of width `t` by a constant times `t`.
A heavy-cell comparison and a geometric sum over all valuation totals
then give a summable bad-event bound. The full-event selection input and
the two short unit parents supply infinitely many suitable return depths.

The heavy-cell argument permits any fixed reference probability measure.
That additional quantifier transfers the conclusion to the original
component marginal by conditioning on its countably many ordinary roots;
no assertion that dimension survives a weak limit is used.

## 2. Mean real information grows at every fine scale

[EXTENSIONS.md](EXTENSIONS.md) strengthens the conclusion in a different
direction. At low-profile endpoints the exact clock obeys

\[
 \mathsf P_q\{F(X_r)\le B,\ A_r\ge6r\}
 \le\frac{B}{F(q)}(64/81)^r.
\]

This follows by counting compositions of the actual valuation total and
retaining each low-profile cylinder's original weight. There is no global
valuation moment assumption. Together with selection, it supplies a
positive amount of probability with a good return at every large horizon.
The corresponding real scales have deterministic exponential upper and
lower bounds. The heavy-cell argument then controls mean partition
information at every sufficiently fine scale in the liminf sense.

Reduce `alpha` to at most one and fix `B>2`. Define

\[
 \theta=\frac{1-2/B}{2/\alpha-2/B},\qquad
 \kappa=-\log\left(1-\frac{3\alpha}{64B}\right),\qquad
 d_B=\frac{\kappa\theta^2}{2(2-\theta)\log(64/3)}>0.
\]

For dyadic partition entropy `H_k`, the conclusion is

\[
 \liminf_{k\to\infty}\frac{H_k(\mu_q)}{k\log2}\ge d_B,
 \qquad
 \liminf_{k\to\infty}\frac{H_k(\mu_E)}{k\log2}\ge d_B.
\]

The bound holds for any fixed absolutely continuous reweighting of a
fixed-root trace path law. Full-event selection extends to its integrable
density, and vanishing bad-event probabilities transfer by absolute
continuity. Countable-root entropy concavity then gives the common-law
statement with the same constant. This is lower Shannon information
dimension, not lower pointwise local dimension or a uniform mass bound.

## 3. Direct attempts to use the new result to close the problem

| Attack | Result | Remaining inference |
|---|---|---|
| Actual real boundary | The two dimension conclusions above, for the actual law | Control the original ternary inverse-time marginal at the required clock and resolution |
| Adaptive early trace | An exact bound for arbitrary inverse stopping rules, including independent randomization | Recover an order-one terminal payoff before the original-source clock |
| Target descent through the published semigroup theorem | An all-length nonnegative discrepancy identity and endpoint-one rigidity | Repair the first actual-target parity mismatch while retaining a descent endpoint |

[EARLY_TRACE.md](EARLY_TRACE.md) extends the latest PR178 deterministic
trace front to arbitrary adaptive stopping lines. On a hypothetical
escaping ray `q_k`, its stopped terminal-digit mass satisfies

\[
 \frac{\mathcal T_\sigma(q_k)}{F(q_k)}
 \le\varepsilon_L+C_g\left(1-d_k/d_L+
        \mathsf P_{q_k}(\sigma>k-L)\right).
\]

Here `d_k` is the actual reversed-spine probability product,
`d_k -> d_infinity>0`, and `epsilon_L ->0`. Recovering a fixed positive
fraction therefore requires a fixed positive probability of reaching
within a fixed distance of the original-source clock. A separate relative
entropy estimate quantifies a change of law that attempts to force an
early payoff. The terminal `D1` seed remains explicit.

[TARGET_DESCENT.md](TARGET_DESCENT.md) tests Applegate--Lagarias's complete
multiplicative semigroup theorem against the original target. For an
integral scaled-generator word shadowing all its actual parities, the
discrepancy from the shortcut orbit obeys

\[
 2^N D_N=\sum_{i:b_i=1}(m_i-1)2^i3^{h_i}\ge0.
\]

At multiplicative endpoint one every `m_i` must equal one; such a word
was already the actual orbit. A useful semigroup descent must consequently
repair the first parity mismatch. No such repair is asserted.

[COLLISION_TRANSFER.md](COLLISION_TRANSFER.md) tests the dimension route
against the latest PR185 collision lower bound. An explicit density
proportional to

\[
 x^{\theta_0/2-1}(\log(e/x))^{1/4}\quad(0<x<1)
\]

has exact local dimension one and Shannon information dimension one,
while its ternary collision sum is at least
`c sqrt(m) 3^(-theta_0 m)`. This is a model of the analytic nonimplication,
not a Collatz path law. Independently, the actual moving-root law retains
a fixed positive high-profile mass from the original forward source.
Thus discarding high-profile states does not supply the required upper
collision estimate.

## 4. Inputs, formal scope, and review

The new analytic proof uses the canonical critical harmonic trace, its
positive floor and full-path selection, and the distinct-state path
packing bound. Their source qualifications remain substantive. The exact
files are pinned in [SOURCES.json](SOURCES.json); primary statement use and
an already pinned route to selection are recorded in
[LITERATURE.md](LITERATURE.md). Metadata for all 122 open PRs was refreshed;
targeted mathematical reading concentrated on the six advanced peer
branches. This was not a whole-repository proof audit.

[BoundaryMass.lean](lean/BoundaryMass.lean) formalizes four finite
inequalities used in the new proof: the harmonic-term cone floor, the
selected-edge probability product, the actual cylinder multiplier bound,
and the arbitrary-reference heavy-cell mass comparison. The exact public
inventory is [THEOREMS.json](THEOREMS.json).
[BoundaryBorelCantelli.lean](lean/BoundaryBorelCantelli.lean) adds three
measure-theoretic declarations. They apply first Borel--Cantelli to retain
infinitely many good returns, extract an increasing subsequence, and obtain
arbitrarily small real balls satisfying the stated power bound. The bad-event
sum, recurrence, and scale convergence remain explicit hypotheses. The
canonical construction and dimension theorem are not encoded as new axioms.

The written notes have scoped independent in-session reconstruction
reviews in [reviews](reviews). These reviews bind exact source hashes and
preserve the upstream qualification. The fresh compiler output, binding
checks, source snapshot and validation scope are in
[the execution report](../../reports/2026-11-23-source-clock/VERIFICATION.md).
The three new formal modules are checked in fresh output, including all
seven public declarations and an axiom audit. Four missing pinned Mathlib
outer-measure dependencies are built in a temporary overlay; all other
installed dependencies are reused. Historical project proofs are not rebuilt.

## 5. The precise closing target still open

The current collision route would close its escape case with an upper
bound on the entire actual law `zeta_(M,r)` of the form

\[
 \operatorname{Col}_m(\zeta_{M,r})
 =o\!\left(\sqrt m\,3^{-\theta_0m}\right),
 \qquad m\to\infty,\quad m^2=O(M),
 \qquad\theta_0=0.949955527188\ldots,
\]

along a compatible sequence of clocks. The real dimension and information
theorems do not prove this estimate. The source clock and the retained
high-profile mass are kept in the failed transfer test. An actual legal
target descent remains a separate possible completion. Nontrivial cycles
also remain unresolved.
