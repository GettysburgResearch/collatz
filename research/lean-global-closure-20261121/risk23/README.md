# High-variance attacks on full Collatz

**23 November 2026. Full Collatz remains OPEN.** This checkpoint directly
attempts full-basin rigidity, unrestricted cycle classification, and
ordinary escape exclusion. It does not supply a universal stopping theorem.

The strongest unconditional result is an infinite-dimensional theorem about
the actual Collatz operator: its unweighted Hardy fixed space is already
infinite inside the known basin of 1. The strongest source-qualified measure
result is total-variation convergence of the actual inverse real fibres
after exact radial renormalization. The packet then follows the proposed
closing implications far enough to identify their failed steps.

## 1. Actual inverse trees give an entire disk of Hardy eigenvalues

For the shortcut map `T`, define

\[
\mathcal T\left(\sum c_nz^n\right)=\sum c_nz^{T(n)}.
\]

The [complete written proof](HARDY_INVERSE_TREE.md) establishes

\[
\boxed{|\lambda|<2^{1/16}
\quad\Longrightarrow\quad
\dim\ker(\mathcal T-\lambda I)=\infty
\quad\text{on unweighted }H^2(\mathbb D).}
\]

Two strictly larger odd unit predecessors are available at every odd unit
root with shortcut exponents in `3,...,8`. Splitting coefficients across
this actual binary inverse tree, while adding shared even tails correctly,
produces a square-summable incoming flow with one exact root defect.
Subtracting two channels cancels that defect. An antichain gives infinitely
many disjoint supports. Every support can be chosen in the explicitly
generated basin of 1.

Consequently `I-T` is not Fredholm on unweighted Hardy space, and its index
cannot furnish a finite cycle count. The note distinguishes this construction
from the published Bergman-space dyadic-ray eigenvectors; it makes no
exhaustive priority claim. On unweighted coefficient `ell^1`, the fixed
vectors are cycle-supported, but an explicit sequence of dyadic chain
averages shows that the range of `I-T` is not closed there either.

Positivity is retained as a separate constraint: every nonnegative `ell^2`
fixed vector is supported on actual cycles. The signed eigenspace does not
classify that cone and does not prove or disprove Collatz.

[InverseBranching.lean](InverseBranching.lean) proves the universal arithmetic
two-child lemma using only Lean core/Std. The infinite-dimensional analysis
is a written, internally reviewed proof, not a Lean theorem.

## 2. Exact same-source fibre convergence in total variation

For one hypothetical escaping odd orbit `q_j` under the pinned actual
canonical inverse law, put

\[
\Lambda_j=\prod_{i<j}\frac{3q_i}{3q_i+1},\qquad
D_j=\Pr_{q_j}(\text{actual prefix back to }q_0),
\]

and let `nu_j` be the law of `(q_j-B_infinity)/(q_j Lambda_j)`.
The [measure proof](RENORMALIZED_FIBRE_ENTROPY_ATTACK.md) gives

\[
\nu_\infty\ge\frac{D_\infty}{D_j}\nu_j,
\qquad
\|\nu_j-\nu_\infty\|_{\rm TV}
\le1-\frac{D_\infty}{D_j}\to0.
\]

The exact scale permits arbitrary moving bounded tests, including rapidly
oscillating ones. The original source remains a positive submeasure.
PR180's concurrently published common-path theorem covers this convergence
in a stronger shared frame; the late-source comparison explicitly credits
that overlap rather than claiming unique priority.
The canonical analytic construction is inherited and source-qualified;
neither a fresh verification of all its inputs nor a formalization of this
measure theorem is claimed.

The attempted entropy closure then grants even the unproved conditional
solenoid mixing premise to test its strength. With the root retained, the
limit is Haar on the solenoid times the original low-entropy time law.
At precision `m`, the quotient label is `V=q-floor(B_infinity)`, whereas
the ordinary root is `Q=V+L`, with `L=floor(B_infinity)` modulo `3^m`.
The exact accounting gives

\[
H(Q)\ge H(V)-H(L\mid Q),\qquad
H(L\mid Q)\ge H(V\mid J).
\]

Conditional quotient mixing makes the subtracted term almost `m log 3`.
It therefore cannot supply the missing entropy of the actual root.

## 3. Full-basin Fourier rigidity was attacked directly

For the actual basin indicator `a(n)`, bounded `L^1` norms of its symmetric
Abel kernels would give a finite idempotent Fourier measure. Cohen's theorem
and the exact Collatz branch identities would then prove the full conjecture.
The [Fourier attempt](FOURIER_IDEMPOTENT_CLOSURE_ATTEMPT.md) does not assert
that bound. It computes why propagating the bound through the map fails.

Even an anchored, exactly doubling-invariant zero-one input with a finite
Fourier measure can lose that property after one fully odd-accelerated
positive-integer pullback. An explicit fifth-root residue is nonreal,
contradicting the real atom residue required of the proposed finite measure.
For the shortcut version the note calculates the exact logarithmic `L^1`
divergence coefficient. These are failures of the attempted regularity
propagation, not counterexamples to the actual basin fixed point.

## 4. Cycle positivity and all-scale height barriers

The [all-word polynomial attempt](ALL_WORD_POLYNOMIAL_ATTACK.md) keeps the
entire state polynomial and shows that its apparent dyadic cancellation
returns the full odd-cycle matching condition. It also gives a short exact
failure of the all-prime additive-potential substitute:

\[
25\to19\to29\to11,\qquad55\to83\to125,
\qquad25\cdot55=11\cdot125.
\]

No completely additive arithmetic potential can strictly decrease on all
five genuine edges. The source and image products agree, but the state sets
do not; the complete primitive word has numerator `581` and denominator
`13`, and the denominator does not divide the numerator.
[PrimeBalanceObstruction.lean](PrimeBalanceObstruction.lean) certifies the
integer-valued potential obstruction and the exact arithmetic.

The fourth [height-barrier attempt](TERNARY_POLE_BARRIER_ATTEMPT.md) tries
unbounded ternary corrections to a sublinear ordinary-height function.
Every finite positive pole correction fails on actual positive integer
approximants to a missing image pole. The proposed integrable all-scale
superharmonic construction has the wrong Haar mean multiplier. The note
explicitly leaves ordinary-only singular constructions and arbitrary
pointwise envelope upper bounds outside these exclusions.

## Latest source comparison and evidence

The initial refresh covered all 145 pull-request metadata records and
selected advanced source heads. Five further branches advanced during this
pass; [LATE_FRONTIER_SYNTHESIS.md](LATE_FRONTIER_SYNTHESIS.md) records their
exact heads, the new statements inspected, and their effect on these
closing attempts. This is targeted source inspection, not a claim to have
replayed every historical branch.

Two new Lean modules compiled, with all **21 public theorems** audited.
Only `propext`, `Classical.choice`, and `Quot.sound` occur. Three finite
controls passed: Fourier interface arithmetic, the cycle/prime-balance
witnesses, and the Hardy flow's shared-tail and leaf-defect identities.
No previous project modules were rebuilt.

Run only this packet's checks with:

```bash
python -X utf8 -B research/lean-global-closure-20261121/risk23/verify_risk23.py \
  --lean /absolute/path/to/lean \
  --receipt /absolute/path/outside/the/checkout/risk23-checks.json
```

Use Lean 4.34.1. There is no Mathlib dependency in these two modules.
See the [execution and review report](../../../reports/lean-global-closure-20261121/nov23/risk23/README.md)
for source hashes, actual outputs, internal review scope, and the separate
clean-checkout integrity gate. None of these checks proves the unproved
universal claims.
