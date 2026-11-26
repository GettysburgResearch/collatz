# Ordinary arithmetic, coupled cycles and operator spectra

**Collatz remains open.** This packet records the 26 November 2026 broad
reevaluation. Successive teams of GPT-6.2 Astra workers pursue independent
arithmetic, combinatorial and operator approaches, followed by independent
proof reconstruction and exact replays. The first-wave results below are
retained, with the current spectral and validation conclusions updated.

**Current checkpoint:** [three-hour final handoff](FINAL_SPRINT.md), covering
exact pressure, persistent reset divisors, shifted squareclasses and finite
positive escape gates. The classical Bergman radius is exactly
$\sqrt{20}/3$ in the reviewed written proposal. The strict Lean packet has
147 audited local declarations in 22 modules; the large written theorems
are not thereby formalized. The universal Collatz step remains open.

The most concrete positive outcomes are answers to specified questions about
Collatz operators in the published literature, a finiteness theorem for actual
integer returns with boundedly many valuation mismatches, and a construction
of rational pairs with different actual periodic fates avoiding any prescribed
finite set of denominator primes. The rational examples are controls for an
integer argument, not counterexamples to Collatz.

## Maps, spaces and evidence

The shortcut map is $T(n)=n/2$ for even $n$, and

$$
 T(n)=(3n+1)/2
$$

for odd $n$. The odd Syracuse map divides $3n+1$ by its *entire* power of
two. An odd step and a shortcut step are different clocks. On positive
rationals of denominator prime to six the same definitions use the parity
and valuation of the reduced numerator. This larger domain is explicitly
identified whenever used.

The composition operator $\mathcal U f=f\circ T$ and the coefficient
transfer $\mathcal T z^n=z^{T(n)}$ are different operators. Their weighted
spaces, quotients and directions must be retained in every assertion.

The [root review](../../reports/unconventional-20261126/ROOT_REVIEW.md) and
[source map](../../reports/unconventional-20261126/FIRST_WAVE_SOURCE_MAP.json)
pin narrow review verdicts. Author headers marked PROPOSED are preserved;
the later reviews identify what was independently checked. Written proofs,
finite exact computations and Lean kernels are separate evidence tiers.
The full analytic conclusions are not claimed as Lean theorems.

## 1. Positive answers to operator questions

### Béhani's classical Bergman spectral radius

For the classical Bergman coefficient norm

$$
 \|f\|^2=\sum_{n\ge3}\frac{\pi|c_n|^2}{n+1},
$$

with degrees $0,1,2$ removed, the specified transfer satisfies

$$
 \boxed{r(\mathcal T)=\frac{\sqrt{20}}3}.
$$

The value $\sqrt2$ proposed in Question 4.1 of Béhani's paper is excluded.
The second wave proves the exact radius through its biased-pressure theorem.
This answers the stated mathematical question without a claim of historical
priority over unexamined later work. The first-wave independently certified
upper bound $r(\mathcal T)\le\sqrt{5516102802/2482245023}$ remains a useful
finite control of the exact calculation.

The lower bound is analytic. A length-$k$ inverse word with $q$ odd branches
is legal in exactly one class modulo $3^q$ and contributes slope

$$
 2^k/3^q.
$$

Averaging over all endpoint residues gives

$$
 3^{-k}\sum_{r\bmod3^k}S_k(r)
 =\sum_{q=0}^k\binom{k}{q}2^k3^{-2q}=(20/9)^k.
$$

The maximum dominates this average. The earlier, slightly larger upper bound is certified by a
positive integer table on 59,049 residue classes. The exact upper bound
uses the written pressure theorem. An independently written
verifier checked the original transfer inequality on all 177,147 lifted
residues, with three deliberately corrupted cases rejected.

[Proof and exact operator identification](operator/BERGMAN_RADIUS.md) ·
[exact pressure proof](operator/EXACT_BERGMAN_PRESSURE.md) ·
[primary paper, Question 4.1 and Proposition 4.2](https://arxiv.org/pdf/2303.03203) ·
[independent certificate receipt](../../reports/unconventional-20261126/BERGMAN_INDEPENDENT.json).

### An explicit vanishing weight with mixing dynamics

Question 4.3 asks what can happen when the coefficient weight has liminf zero.
For $u$ odd, set

$$
 \omega(2^j u)=2^j
 \begin{cases}u,&3\nmid u,\\u^{-1},&3\mid u.\end{cases}
$$

The transfer is bounded, topologically mixing, has dense periodic points,
and preserves a full-support strongly mixing Gaussian probability. The
proof constructs a contracting right inverse and a dense generalized
kernel using actual ordinary monomials; it does not assume Collatz.

The remaining existential adjoint-eigenvalue question has a different scope:
for some admissible weight, such an eigenvalue exists exactly when there is
an ordinary component outside the $1,2$ cycle. This equivalence does not
decide which alternative holds.

[Construction and complete proof](operator/BERGMAN_VANISHING_WEIGHTS.md).

### Exact spectra on every ordinary component

For every weak component $C$, $1\le p<\infty$, and
$\sigma\ge\log_3 2$, the spectrum and Fredholm essential spectrum of
composition on $\ell^p(C,n^{-\sigma})$ are both

$$
 \{z:|z|\le (3/2)^{\sigma/p}\}.
$$

The proof uses ordinary inverse-fiber counts and two arbitrarily long
ordinary inverse arms. For $\sigma>1$, powers normalized by this radius
converge strongly to zero although their essential norms stay at least one.
The same conclusions hold on the known basin of 1, so this scalar spectral
data cannot certify that there are no other components.

[Power spectrum proof](operator/POWER_SPECTRUM.md).

## 2. Restrictions on actual integer trajectories

### Finite returns with a bounded number of mismatches

Fix any periodic positive valuation template $m_i$, with its rational
periodic centers $c_i$. A mismatch is an actual odd transition whose
valuation differs from the template. For fixed $R\ge1$ and fixed
finite-rank multiplicative families of **nonzero** endpoint distances

$$
 q_0-c_0,\qquad q_h-c_h,
$$

there are only finitely many ordinary source/phase/length triples with
between one and $R$ mismatches. There is no bound assumed on the physical
length or on individual division exponents. With fixed rank and number of
cosets, visits also have uniformly vanishing density when time is measured
at mismatches, even when the groups are selected after observing the path.

The proof combines real domination of correction terms with a unique least
dyadic term, then applies Evertse–Schlickewei–Schmidt. It includes the first
small-state cutoff and the conversion from a finite set of mismatch states
back to actual sources. Zero endpoint displacement and zero mismatches
cannot be silently included.

[Statement, proof, counterexample to zero-mismatch extension](defects/CENTERED_DEFECT_RETURNS.md).

### Uniform lower heights after the Mersenne ascent

After the first reset from $2^m-1$, every sufficiently large $m$ has all
odd states of size $3^{m+o(m)}$ through at least

$$
 (1/2-\epsilon)\frac{\log m}{\log\log m}
$$

additional complete ascent runs ending in strict decreases. A corresponding
bound has coefficient $1-\epsilon$ for individual odd transitions. This
follows from a uniform theorem for low-height affine shifts of integers
supported at a fixed finite set of odd primes, using Yu's published dyadic
logarithmic-form estimate. These are lower bounds on the progress required
before a descent; they do not prove a later descent happens.

[Shifted-smooth theorem and exact clock conventions](defects/SMOOTH_SOURCE_PREFIX.md).

The completely classified Mersenne-to-Mersenne paths with exactly one reset
are $1\to1$ and $3\to5\to1$, in the odd map. The actual path theorem,
not only its exponential equation, is kernel-checked.

[One-reset theorem](defects/MERSENNE_ONE_RESET.md) ·
[Lean classification](defects/MersenneReset.lean).

### A joint clock for the tripling pair

If the odd orbits of $x$ and $3x$ are disjoint, and $S_K,T_K$ denote
their first $K$ cumulative division clocks, then

$$
 \min(S_K,T_K)<(2K-1)(K+1)\log_2 3.
$$

The result is uniform in the source and holds for positive odd rationals
as well as integers. At each cut in the union of their actual odd dates,
either an integer cross-difference forces the next clock bound, or its
vanishing forces a literal common ordinary/rational state. The good leg
may be the one with the smaller clock; no descent follows just from this
estimate.

[Joint-clock proof and finite alternative](arithmetic/TRIPLING_CLOCK.md).

## 3. Rational controls that survive all depths

For every finite prime set $S$ and $0<\eta<2/5$, infinitely many pairwise
coprime reduced denominators $d>1$, avoiding $S\cup\{2,3\}$, each support
at least $d^{2/5-\eta}$ tripling-coupled pairs of distinct positive cycles.
Tripling at the marked minimum of either cycle enters the other cycle.
The resulting basin disagreements use actual full forward fates, not a
finite-depth coloring.

The construction concatenates three paired parity words whose affine maps
intertwine $Y=3X-1$. Unique markers prove different cycles; congruences
exclude the prescribed primes; divisor counting concentrates many cycles
at one *reduced* denominator. Four small fixed words also passed a complete
least-disagreement fate check: 23,009 candidate starts and 653,953 new odd
transitions. Together with the six inherited models their denominators are
pairwise coprime, so any nine primes miss one such full least model.

The infinite arbitrary-$S$ family has reciprocal disagreements and cycle
minima. Full leastness throughout its basins is proved only for the stated
finite models. None is an ordinary counterexample.

[Construction, reciprocal minima and finite least-model boundaries](arithmetic/COUPLED_CYCLES.md) ·
[complete finite control output](../../reports/unconventional-20261126/COUPLED_CONTROLS.json).

A different near-critical mechanical family has full denominator

$$
 D=2^A-3^p,
$$

large real minimum $p^{2-o(1)}$, and simultaneous dyadic/ternary agreement
exceeding every polynomial in its real size. Its denominators also avoid
arbitrary fixed prime sets. Ordinary integers satisfy the effective upper
bound $O(X^2/(\log X)^{2/4.117})$ at a common two-sided mechanical cut.
The stronger $X^{3/2+\eta}$ bound is separately **SOURCE-QUALIFIED** to
Weaver's recent Paper 140; its full analytic dependency chain was not
rebuilt here. Arbitrary actual orbits need not supply mechanical windows.

[Ordinary simultaneous approximation](arithmetic/MIXED_MECHANICAL.md) ·
[rough full-denominator construction](arithmetic/ROUGH_DENOMINATORS.md).

## 4. What the operator analysis rules out

The unital C* algebra generated by both branch partial isometries and all
periodic diagonal multipliers has identical norms and essential norms on
every ordinary merge component. Its commutative quotient is $C(\mathbb T)$.
After any nonzero polynomial height weighting, the algebra is exactly

$$
 \mathcal A+\bigoplus_C^{c_0}\mathcal K(\ell^2(C)),
$$

with a split quotient back to $\mathcal A$. Nonconstant component
indicators remain distance $1/2$ from the unweighted algebra even after
arbitrary compact perturbations. Information about the number of components
lies in the compact ideal, whose simplicity has not been proved.

The same finite-chart analysis gives effective norm computation and
Hausdorff approximation of selfadjoint spectra for rational finite
polynomials. It gives no algorithm deciding the component of an integer.

Actual convergent funnels further rule out a uniform anchored residual gap
for all decreasing summable weights, and for powers of height corrected by
finitely many local factors with finitely many singularities. The positive
rooted-tree weight criterion is proved with its root and domain retained.

[Component norm theorem](operator/COMPONENT_OPERATORS.md) ·
[algebra structure](operator/OPERATOR_STRUCTURE.md) ·
[finite spectral computation](operator/FINITE_SPECTRUM.md) ·
[weighted gap criterion](operator/WEIGHTED_GAP.md) ·
[local arithmetic weights](operator/LOCAL_WEIGHT_OBSTRUCTION.md).

## Formalization and reproduction

The strict current replay rebuilt **22 modules and audited all 147 local
theorem declarations**, including private lemmas. The first checkpoint had
10 modules and 70 declarations. They use only the standard
axioms `propext`, `Classical.choice`, and `Quot.sound`, or no axioms. Eleven
of those declarations are repaired copies of earlier uncompiled closing
interfaces; their unproved global premises remain parameters. The earlier
seven-module baseline was rebuilt separately and matched all 46 existing
axiom reports.

| Modules | Audited declarations | Formal scope |
|---|---:|---|
| `AffineClock`, `Funnel`, `CarryMass` | 28 | Affine clocks, actual ordinary funnels, carry bounds and injectivity, exact binomial mass |
| `MixedWordSpacing`, `TriplingCut`, `CoupledCycles` | 13 | Ordinary divisibilities, local merger-or-gap, paired affine words and reciprocal identities |
| `MersenneReset`, `DefectArithmetic` | 18 | Complete one-reset physical classification and centered correction arithmetic |
| `verified/MinimumClosure`, `verified/TraceProposal` | 11 | Repaired earlier arithmetic and explicitly conditional global consumers |
| `ReferenceBarrier`, `FirstDescentFloor`, `FusionControl` | 29 | Reference capacity, actual first descent and synchronized binary fusion |
| `SequencePivot`, `PressureWindows`, `TraceFront` | 22 | Triangular pivots, carry and window arithmetic, conditional trace-front interfaces |
| `ModularCarry`, `RelativeReset`, `PersistentDivisor` | 16 | Exact finite carry perturbations and ordinary reset identities |
| `ResetDepthRatio`, `TwoBlockSwap`, `AnnularCut` | 10 | Divisor transport, finite transposition exclusion and annular cancellation |

Use the pinned Lean and Mathlib versions recorded in the receipt. The replay
reuses their external library build and creates fresh project objects.

```bash
python -B research/unconventional-20261126/replay_lean.py \
  --mathlib /path/to/pinned/mathlib4 --lean /path/to/pinned/lean \
  --check reports/unconventional-20261126/THIRD_LEAN_RECEIPT.json
python -B research/unconventional-20261126/replay_controls.py
python -B research/unconventional-20261126/replay_second_wave.py
python -B research/unconventional-20261126/replay_third_wave.py
```

For the independent upper certificate check:

```bash
python -B research/unconventional-20261126/operator/check_bergman.py \
  --depth 10 --write-vector /tmp/collatz-bergman-vector.txt
python -B research/unconventional-20261126/check_bergman_certificate.py \
  /tmp/collatz-bergman-vector.txt
```

All first-wave primary controls were replayed in normal and optimized Python
with complete JSON equality. The second wave adds five primary and four
independent exact controls, all replayed in both modes, and regenerates the
depth-ten integer vector. The third wave adds seven primary and two independent
root controls, all compared in both modes. Assertion-based first-wave supplemental scripts
reject optimized execution before doing work. Full-checkout structural
validation has its own receipt; it is not mathematical verification.

[current Lean receipt](../../reports/unconventional-20261126/THIRD_LEAN_RECEIPT.json) ·
[second finite replay](../../reports/unconventional-20261126/SECOND_CONTROL_REPLAY.json) ·
[finite replay receipt](../../reports/unconventional-20261126/CONTROL_REPLAY.json) ·
[legacy repairs](verified/README.md).

## The remaining global obligation

No theorem here proves that every positive integer has a smaller merging
witness, that every ordinary orbit enters a rigid template, or that the
canonical ordinary trace has the uniform bound needed to exclude escape.
The precise universal descent and cycle/escape premises in the closing
Lean interfaces remain open. The final wave restricts information retained by
one fixed integer, classifies fixed-modulus cycle restrictions and expresses
escape charge through finite positive exit gates; the required zero limit is unproved. The [second-wave review](../../reports/unconventional-20261126/ROOT_SECOND_REVIEW.md)
records why the completed pressure and excursion theorems do not close
those obligations.
