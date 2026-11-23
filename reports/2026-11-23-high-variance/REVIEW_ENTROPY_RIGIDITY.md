# Independent reconstruction: actual boundary and time information

Date: 2026-11-23. Reviewer: `analytic_gluing`, different from this note's author.

**Verdict: VERIFIED at the displayed new deductions, retaining all explicit
upstream source qualifications.** This is an in-session written proof
reconstruction, not external peer review or Lean verification.

Reviewed file: `research/high-variance-20261123/ENTROPY_RIGIDITY.md`.

SHA256: `5165d1dc167432bbefc7c758e50323ca7412c835930c59fc9aa16164b2edfc80`.

The companion coherent-boundary construction is a dependency. Its own
independent reconstruction is separate from this review; the present reviewer
authored that companion and does not purport to independently certify it here.

## 1. Full-path conditioning and uniform information comparison

The events `E_j={Q_j=q_j}` are increasing because their futures are the
literal deterministic forward ray. Their probabilities are `nu(q_j)/c_E`
under the ordinary reference. Under the fixed critical tilt `Z/s_E`, their
probabilities are exactly

\[
 p_j^G=\frac{y(q_j)h(q_j)}{c_Es_E}\longrightarrow1.
\]

The conditional laws are the actual ordinary and critical inverse laws,
respectively. There is no independent-gap resampling at this step.

On each labelled fibre, the density of the conditional law relative to the
unconditioned reference is `1_Ej/p_j`. Its relative entropy is `log(1/p_j)`
and its total variation distance, in the stated convention, is `1-p_j`.
Averaging the disjoint labels gives the exact identities (5) and (6).
Since `p_j` increases to one and `p_0>0`, the terms are bounded and Cesaro
convergence applies.

For any deterministic observation of the time label and any observation of
the **common** boundary variable `Z`, data processing and the entropy chain
rule give (7)--(8). The label marginal stays unchanged. One can first use
finite partitions and increase them, so the same finite entropy bound also
licenses the standard-Borel formulation. This argument is uniform in the
chosen finite ternary resolution because the initial inequality concerns the
entire path and label.

The note correctly excludes the root-dependent normalization
`T_j=1-Z/y(q_j)` from this all-resolution assertion. Bounded-Lipschitz
convergence of that rescaled real variable does not control relative entropy
at arbitrarily fine scales. This distinction is essential and explicitly
retained. The additional trace-law tilt is likewise kept distinct from the
`G`-law.

### Fixed-root nonatomicity addendum

The final addendum was reconstructed separately after the earlier review.
I read PR185's `ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`, Section 7, at
`39ba48e6a8af781193e28c679ea8ab64663c3aa6`. Its qualified fixed-basin
sublinearity states that `nu(n)` tends to zero through unbounded
predecessors of one fixed nonperiodic target. This is exactly the uniform
tail-supremum formulation used in the addendum.

For any finite height cutoff, there are finitely many possible predecessor
integers, each at a unique depth. Beyond their largest depth, no such small
integer remains in the target's inverse-depth level. The tail-supremum bound
therefore makes the largest complete-word probability
`sup nu(n)/nu(q)` tend to zero. Continuity on decreasing prefix cylinders
proves complete-path nonatomicity, and `H(W_r)>=-log sup P(W_r)` proves
divergence of the extended countable entropy. The bounded fixed-root
critical and trace likelihood ratios preserve both conclusions. Conditioning
on the countable root state proves nonatomicity of the whole two-sided
path law.

No rate or moving-root uniformity is obtained. The boundary pushforward
need not be injective, and the bounded overlap proved for the auxiliary
selected routing tree does not bound all fibres of the full canonical
path law. The addendum correctly leaves real-boundary nonatomicity and
its metric entropy unresolved.

## 2. The simultaneous moving trace selection

I read PR175's `MOVING_CESARO_FIBRES.md` at
`8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`, especially its definitions
(13), (20), and Theorems 1--2. The real finite measure is normalized by the
ordinary trace `h_tr(q)`, and has total mass `D_m(q)/h_tr(q)`; it is not
normalized independently to probability. The reviewed deduction respects
this normalization.

Choose one nonnegative Lipschitz test supported in a fixed real interval
away from zero with positive limiting inverse-fibre integral. This is
permitted by the actual nonconstant positive boundary representation and
the fixed positive trace tilt. The two upstream uniform Cesaro statements
make the sum of the scalar and joint errors small over a fixed sufficiently
large finite excess-depth range. At least one excess depth has both errors
small. Since `h_tr(q_k)/q_k` has a positive finite limit, the lower and upper
bounds in (13) follow with one pair of constants, and
`m_k=k+O_{q_0}(1)`.

Thus the selection neither assumes pointwise convergence at every depth nor
drops the original-source clock. Its proof uses the stated fixed observable;
no entropy convergence at radius `3^(-m_k)` is smuggled into the BL theorem.

## 3. Both relative-entropy costs

Conditioning any probability on a positive-mass event costs precisely minus
the logarithm of its mass. From (13), the first cost is

\[
 m_k\log3-\log q_k+O(1).
\]

The actual growth bound `q_k+1 <= (3/2)^k(q_0+1)` makes this at least
`k log2-O(1)`. The displayed lower limit after normalization by
`m_k log3` is therefore correct.

The fixed-ratio real shell has probability comparable to `1/q_k` by the
qualified Goldie tail. Dividing the intersection bound in (13) by that shell
mass gives a cylinder probability comparable to `q_k^2*3^(-m_k)`. Its
conditioning cost is

\[
 m_k\log3-2\log q_k+O(1)
 \ge k\log(4/3)-O(1).
\]

This verifies (15), including the constant `log(4/3)/log3`. The compared
probability measures are named explicitly; these costs are not the vanishing
conditioning cost on the actual path space in Section 2. Comparing the cost
with the entropy deficit is appropriately described as a test of this
particular proposed bridge, not an impossibility theorem for all entropy
arguments.

## 4. Primary-source statement checks and the local-moment consumer

I opened the current primary pages, which identify **Paper 9 v2** and
**Paper 19 v2**, and checked the exact displayed inputs:

- <https://rstation.ai/problems/collatz/papers/9>, Appendix B, Theorem 16,
  (B1)--(B2): full ternary Haar normalization and the shell estimate
  `C_p B^(1-2/p) log(eB)^(1-1/p)` for `B>=1`.
- <https://rstation.ai/problems/collatz/papers/19>, Section 10, (S2), and
  Section 10.1, (S4)--(S6): uniform product-ball mass
  `C epsilon^2 log(e/epsilon)` for the independent stationary joint law.

These checks do not independently reconstruct either manuscript's complete
analytic dependency chain. Their use remains source-qualified as stated.

For the shell-moment application, the fixed shell in (13) is covered by
finitely many dyadic shells of sizes comparable to `q_k`. Hölder on a
ternary cylinder of Haar mass `3^(-m_k)` gives

\[
 q_k^{2/p}\le C\,3^{m_k/p}
                 [\log(e q_k)]^{1-1/p},
\]

and raising to the power `p` gives exactly (18). Since
`q_k^2*3^(-m_k)=O((3/4)^k)`, this does not contradict the actual growth
bound. The note correctly says the real-tail comparison already yields
the same exponential balance without the logarithm.

The tail citation was checked against PR180's
`research/deep-machinery-20261122/RENEWAL_TRANSPORT.md`, Section 1,
equation (2), at `5e29f56f6d44669a8aa9134e5617b78d65c074c2`.
That is the correct source location in the final reviewed bytes.

## 5. Boundary of the verdict

The elementary nonatomic-cylinder argument for the proposed early-height
criterion is correct: a compact nonatomic probability has maximum shrinking
ball mass tending to zero. The comparison that would apply it to ordinary
linear spikes is explicitly OPEN, and is not supplied by any of the proved
conditioning estimates.

The checked results neither prove absolute continuity of the moving integer
fibre, remove its source-clock cost, establish a canonical entropy lower
bound, exclude an escape, nor address nontrivial positive cycles. Full
Hausdorff dimension of a support is not treated as the metric dimension of
the canonical measure. These distinctions are part of the reviewed claim,
not exclusions added after the argument.
