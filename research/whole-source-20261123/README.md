# Whole-source collision, minimum flux, and nonlocal arithmetic

Date: 2026-11-23.

**Status: new written deductions and eight checked Lean core theorems.
Collatz remains unresolved.** The central new result concerns the actual
ternary time-limit laws of a hypothetical escaping ordinary orbit: each has
a collision exponent strictly below the previous critical exponent. The
improvement is process-dependent, and its finite-window version has an
explicit extra hypothesis. This packet supplies no matching upper estimate
and no nontrivial-cycle exclusion.

This pass started from published PR180 head
`fcdcdbadc6172e414f7282442a8a6b85587d7e70`. It surveyed the metadata of all
122 open and 23 closed PRs, read the integrated research map and its
qualifications, and inspected the new PR176, PR178 and PR182 heads together
with the source families used below. This is a repository-wide orientation
and a focused mathematical pass, not a proof audit of 145 PRs.
The [metadata snapshot](../../reports/2026-11-23-whole-source/PR_SNAPSHOT.json)
and [source ledger](SOURCES.json) preserve that distinction.

## 1. The strict collision improvement

Let `q_j=U^j(q_0)` be an escaping positive odd orbit, with
`U(n)=(3n+1)/2^{v_2(3n+1)}`, and let

\[
\pi_M=\frac1{M+1}\sum_{j=0}^M\delta_{q_j}.
\]

Regard this unchanged ordinary time law as a probability on ternary units.
Put

\[
\ell=\log_2 3,\qquad
\Phi(b)=b\log b-(b-1)\log(b-1),\qquad
\theta_0=\frac{\Phi(\ell)}{\log3}=0.949955527188\ldots .
\]

The new theorem in [COLLISION_CORE.md](COLLISION_CORE.md) states that **every
fixed ternary weak limit** `mu` of these actual time laws has constants
`epsilon_mu>0` and `m_mu` such that

\[
\operatorname{Col}_{3^m}(\mu)
\ge \exp[-(\Phi(\ell)-\epsilon_\mu)m]
\quad(m\ge m_\mu).
\]

Here collision is the sum of squared probabilities of the residue classes
modulo `3^m`. Equivalently,

\[
\limsup_{m\to\infty}
\frac{-\log\operatorname{Col}_{3^m}(\mu)}{m\log3}<\theta_0.
\]

The proof obtains a stationary law of reversed actual gap windows from the
same source subsequence. Its mean gap is at most `ell`, and its ternary
factor is exactly the chosen `mu`. It then uses an exhaustive dichotomy:

- A strict Shannon deficit at one finite block length propagates by
  stationarity and entropy subadditivity, giving an exponential collision
  improvement at every sufficiently large block length.
- If no block has a deficit, equality in the geometric maximum-entropy
  inequality forces the geometric iid process of mean `ell`. Its word
  collision exponent is
  `log(2 ell-1)/log3=0.705155598019...`, already strictly smaller than
  `theta_0`.

The geometric process appears only in that forced equality case. It does
not replace the actual source law. Grouping word masses by their exact
ternary endpoint can only increase collisions.

A separate exact identity connects the retained moving inverse law
`zeta_(M,r)` to the same time law. With the source-qualified harmonic
flow `v_j=nu(q_j) -> C`,

\[
\|\zeta_{M,r}-\pi_M\|_{\rm TV}
=
1-\frac1{M+1}\sum_{j=0}^M\frac{v_j}{v_{r+j}}
\le\frac1{M+1}\sum_{j=0}^M(1-v_j/C)\longrightarrow0
\]

**uniformly over every finite inverse clock `r`**. Inverse depth therefore
does not remove the asymptotically full original-spine mass.

### What this buys for the escape target

It would now suffice to prove, on one of those same actual limits,

\[
\operatorname{Col}_{3^m}(\mu)
\le \exp[o(m)]\,3^{-\theta_0m}.
\]

The new exponential improvement can absorb any subexponential loss in
that upper estimate. The upper estimate itself is still missing.

For the strict finite-Shannon-deficit branch, a literal mixture comparison
of empirical subblocks also gives the improvement at every growing
resolution `m=o(M)` along the same subsequence. The geometric equality
branch only supplies the time-limit-first conclusion. No convergence
modulus is assumed, and no uniform positive exponent gap over all
stationary processes is claimed. The note proves that last limitation
with stationary constant-composition block models; those models are not
asserted to be Collatz trajectories.

There is a second precise escape target. The same stationary process
cannot have an almost surely finite positive **real** Syracuse series:
its exact logarithmic recurrence would give

\[
\mathbb E G_1\log2-\log3
=\mathbb E\log\!\left(1+\frac1{3R}\right)>0,
\]

contrary to its mean bound. Clipping the logarithm justifies the stationary
coboundary integral without assuming `E |log R|<infinity`. Uniform real
tightness of these same limiting partial sums would suffice, but it has
not been obtained from ternary convergence or from the separately routed
real boundary.

## 2. One finite source for the actual outgoing current

[BOUNDARY_DESCENT.md](BOUNDARY_DESCENT.md) takes the newly attained
pressure maximum back into the actual two-sided ordinary path law.

Every such path has a unique minimum of the coherent scale `chi`:
the scale tends to infinity at both ends, and a nonempty segment cannot
have multiplier one because `3^h != 2^A`. Let `b_*(n)` be the actual
inverse probability of staying above `chi(n)`, restricted to states whose
entire deterministic future also stays above that scale. Then

\[
\sigma(n)=\nu(n)b_*(n),\qquad
\sum_n\sigma(n)=C.
\]

This is a finite measure of actual minimum states. At a global unit-domain
pressure maximizer `m`, its atom is exactly `sigma(m)=nu(m)>0`.

Writing `L` for ordinary forward mass transport, the current after the
minimum has the exact Green representation

\[
\nu_+=\sum_{j\ge0}L^j\sigma\le\nu,\qquad
(I-L)\nu_+=\sigma,\qquad
(L-I)\nu_-=\sigma,\quad \nu_-=\nu-\nu_+.
\]

Along the unchanged forward spine,

\[
\nu_+(q_j)\to C,\qquad \nu_-(q_j)\to0.
\]

Thus the entire late outgoing current is accounted for by one intrinsic
finite ordinary source. The harmonic flow itself is not incorrectly
identified with a positive-source Green potential.

The same whole-path accounting integrates the existing equal-depth
injective orbit count to

\[
\sum_{n\le X}\frac{\nu(n)}C\le4X^{39/40}.
\]

It supplies finite comparison measures

\[
\tau_s=\sum_{n\in E}\frac{\nu(n)}C n^{-s}\delta_n
\quad(s>39/40),
\]

including exponents below one. For `39/40<s<1`, their arithmetic-progression
tails have exponent `(s-39/40)/(1-39/40)`. At the endpoint, unequal modular
collisions satisfy

\[
\mathcal O_Q(\tau_1)=O((\log Q)/Q).
\]

These are bounds on specified actual component measures. They are not
claims that the weighted occupation measures are pressure eigenmeasures.
Their literal density comparison with the time law retains the factor
`H_M^s/(M+1)`, where `H_M=max_(j<=M) q_j`. That factor prevents the displayed
bounds from passing to the required stationary limit at a fixed modulus.
The finite source identity does not provide the missing bilinear bound.

## 3. An unrestricted arithmetic test of pressure improvement

[ARITHMETIC_MINIMUM.md](ARITHMETIC_MINIMUM.md) extends the pressure maximum
to the **whole positive odd component**, including multiples of three.
This is a new maximization on a larger domain, distinct from the
unit-domain maximizer in Section 2. Its least maximizer satisfies

\[
m\bmod12\in\{3,7\}.
\]

At every actual future endpoint, the original word maximizes its affine
carry among legal positive-source competitors with the same odd count,
clock and endpoint. The attempt was to violate that maximum by rearranging
a later part of the word.

Suppose a repair keeps the first `i` odd gaps, replaces the next `l` gaps
by another positive-gap word of the same length and total clock, preserves
the suffix and endpoint, and gives a different integral initial source.
The full carry range and ordinary divisibility force

\[
2^{i+l}<3^{l-1},
\]

or

\[
l>\frac{i+\log_2 3}{\log_2 3-1}
=1.7095\ldots\,i+2.7095\ldots .
\]

This has no alphabet cutoff and no bound on the full word's depth. It
excludes bounded-span same-clock repairs sufficiently late in the word.
It permits sparse changes across a long span, changed clocks or endpoints,
and entirely nonlocal constructions. The missing construction is still
an actual positive integral competitor violating the maximum.

## 4. Direct attempts to finish

The lanes tested their results against each other and against the latest work.

| Attempt | Result at the exact interface |
|---|---|
| Transfer PR178's ordinary pressure upper bound to the improved stationary target | The comparison bound is at least `2 c_0 H_M/((M+1)Q)` once `H_M>=Q`, uniformly for every pressure parameter `s>1`. It diverges at fixed `Q`; this concerns the comparison expression, not a new lower bound on actual collisions. |
| Transfer minimum-conditioned boundary information to the late time law | The source decomposition retains all capacity, but its randomness is in the inverse past. Forward transport has not supplied residue anti-concentration on the common deterministic future. |
| Use the new subcritical weighted measures | Their arithmetic upper bounds are proved. The actual density factor and, for positive inverse clocks, its unbounded supremum are retained explicitly. |
| Obtain a finite real realization of the stationary ternary series | The drift contradiction is proved conditionally on that same-law real realization. Uniform real tightness is not proved. |
| Apply independent Mahler rigidity to PR176's positive kernel | The available equation mixes dyadic and triadic substitutions. It does not supply the two separate Mahler equations required by the literature theorem. |
| Construct a smaller ordinary source from the full pressure maximum | The carry range proves that a same-clock repair must have the long span above. No all-source nonlocal construction was found. |

For the Mahler check, the primary reference inspected was Schäfke and Singer,
[Mahler equations and rationality](https://singer.math.ncsu.edu/papers/vshort2-5.pdf),
Theorem 1. Its hypothesis is a separate `p`-Mahler and `q`-Mahler equation
for multiplicatively independent bases. It is not applied here under a
weaker mixed-equation hypothesis. The
[dreamcatcher paper](https://arxiv.org/abs/1909.09733) was also inspected for
its stated finite-support restriction; no such restriction or resulting
classification is imported into these proofs.

The first two successful routes above concern **escape**. Even a successful
same-law upper bound would leave the separate exclusion of nontrivial
positive cycles to be supplied for full Collatz.

## 5. Formal scope, review, and reproduction

The [theorem inventory](THEOREMS.json) lists eight public declarations:

- Four in `lean/StationaryCollisionGap.lean` prove the subadditive
  blocking, exact finite-block deficit, eventual strict rate, and
  deficit-or-rigidity sequence argument.
- Four in `lean/ArithmeticRepair.lean` prove the finite carry-range and
  divisibility implications, their composition with actual prefix
  expansion, and an integer span corollary.

The stationary extraction, entropy identifications and equality cases,
real-series drift, minimum-source Green decomposition, infinite weighted
sums, pressure construction, and affine carry derivation remain explicit
written proofs. The Lean files take their finite arithmetic or entropy
sequence premises as theorem parameters. They do not assert those
identifications or a Collatz closure theorem as axioms.

Both modules and both audit modules were freshly compiled with Lean 4.34.1,
compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Warnings were errors; all
eight declaration audits use only standard axioms. Installed pinned
dependencies were reused, and no historical proof suite was rebuilt.

The commands below rebuild only these new cores. Set `LEAN_BIN` to the
pinned Lean executable and `MATHLIB_ROOT` to its pinned Mathlib checkout.
Keep new receipts outside the tested checkout.

```bash
python -X utf8 -B research/whole-source-20261123/check_collision_lean.py \
  --lean "$LEAN_BIN" --mathlib "$MATHLIB_ROOT" --report-dir /tmp/collatz-collision-check
python -X utf8 -B research/whole-source-20261123/check_arithmetic_lean.py \
  --lean "$LEAN_BIN" --mathlib "$MATHLIB_ROOT" --report-dir /tmp/collatz-arithmetic-check
python -X utf8 -B research/whole-source-20261123/check_packet.py \
  --receipt /tmp/collatz-whole-source-packet.json
python -X utf8 -B tools/validate.py \
  --receipt /tmp/collatz-whole-source-integrity.json
```

The packet checker binds the new files, exact proof reviews, compiled
sources and theorem inventory. Add `--check-sources` to verify pinned peer
files against their Git objects; fetch the exact commits listed in
`SOURCES.json` first if they are not present locally. This checks identity,
not mathematical truth.

Independent reviews are bound to exact file hashes:

- [Collision review](../../reports/2026-11-23-whole-source/reviews/REVIEW_COLLISION.md):
  original-source extraction, entropy dichotomy, finite-window scope,
  stationary sharpness, clipped real-series drift and formal scope.
- [Boundary and arithmetic review](../../reports/2026-11-23-whole-source/reviews/REVIEW_BOUNDARY.md):
  minimum partition, both Green signs, weighted occupation, progression
  constants, actual-law transfer and unrestricted repair inequalities.
- [Additional collision challenge](reviews/COLLISION_REVIEW.md):
  independent reconstruction of the stationary and moving-window core.

The previous PR description is preserved exactly as
[JSON](../../reports/2026-11-23-whole-source/PR180_PREVIOUS.json).
Earlier packets remain at their original paths and retain their original
claims and qualifications.
