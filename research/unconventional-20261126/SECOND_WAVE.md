# Exact pressure, finite prediction and the single-source obstruction

26 November 2026, second checkpoint of the three-hour reevaluation.

**Collatz is still open.** The strongest result of this checkpoint is a
complete written calculation of the classical Bergman transfer radius,

$$\boxed{r(\mathcal T)=\frac{\sqrt{20}}3}.$$

This follows from an exact pressure theorem for ternary inverse dynamics.
The proof was reconstructed by the root reviewer and two independent
GPT-6.2 Astra reviewers. It is not yet a complete Lean theorem. The strict
Lean packet now has **121 audited local theorems in 16 modules**.

The most consequential negative result is equally concrete: every stationary
inverse process of mean exponent at most $\log_2 3$ can arise as a weak limit
of **complete first-descent excursions of terminating ordinary tripling
pairs**. This forces the next global argument to retain more information
about a single fixed source than its limiting stationary statistics.

[Root proof reconstruction and evidence boundaries](../../reports/unconventional-20261126/ROOT_SECOND_REVIEW.md)
· [source hashes and integration changes](../../reports/unconventional-20261126/SECOND_WAVE_SOURCE_MAP.json)
· [first checkpoint](README.md).

## 1. The exact pressure theorem

The inverse odd branch with label $e\ge1$ is

$$x\longmapsto\frac{2^e x-1}{3},$$

on the ternary states where that quotient is integral. Give its label the
geometric weight $3p(1-p)^{e-1}$, and call the resulting positive operator
$B_p$. On continuous ternary functions,

$$r(B_p)=\max(1,3p)\qquad(0<p<1).$$

The lower bounds come from Haar averaging and the fixed inverse code at
$-1$. The difficult direction shows that every stationary inverse process
with genuine conditional branching has full ternary dimension. A deficient
dimension and positive branching would create a positive entropy gain in a
positive proportion of finite windows; the available global entropy budget
is only sublinear. The proof handles countably many labels through joint
relative entropy, and controls state/noise dependence before applying the
finite-group entropy gain.

For the even and odd shortcut branches $U,J$ on $C(\mathbb Z_3)$ this yields

$$r(aU+bJ)=\max(a+b/3,b)\qquad(a,b>0).$$

The classical Bergman norm is then identified by exact inverse-fiber slopes.
At $(a,b)=(2,2/3)$ the squared radius is $20/9$.

[Full proof](operator/EXACT_BERGMAN_PRESSURE.md)
· [induced-operator comparison](operator/BIASED_PRESSURE.md)
· [weighted corollary](operator/WEIGHTED_SHORTCUT_PRESSURE.md)
· [independent entropy review](../../reports/unconventional-20261126/reviews/PRESSURE_ENTROPY_REVIEW.md)
· [independent variational review](../../reports/unconventional-20261126/reviews/PRESSURE_VARIATIONAL_REVIEW.md).

### The precise spectral conclusions

| Space and operator | Conclusion | Scope |
|---|---|---|
| Classical Bergman coefficient transfer, with degrees 0, 1, 2 removed | Radius $\sqrt{20}/3$ | Complete written proof; not fully formalized |
| Restriction of that transfer to any ordinary component | Spectrum and Fredholm essential spectrum are the closed disk of that radius | Includes the known basin of 1 |
| Same transfer | Infinite-multiplicity eigenvalues for $|\lambda|<\sqrt{207384761192/93324220975}$ | Exact positive-vector construction; slightly smaller disk |
| Coefficient sequences with the product topology | Conjugate to countably many unilateral backward shifts | A different topology, with all complex eigenvalues |

The component spectra agree even if other components exist. Computing these
spectra therefore does not decide whether every integer reaches 1.

[Disk proof](operator/BERGMAN_DISK.md)
· [point-spectrum construction](operator/BERGMAN_POINT_DISK.md)
· [product-topology conjugacy](operator/PRODUCT_SEQUENCE_SHIFT.md).

## 2. Finite rules now have exact asymptotics

For finite allowed exponent sets and a finite ternary weighting rule, the
pressure is exactly the larger of a normalized finite-matrix Perron radius
and the largest weighted cycle mean. For an arbitrary closed finite-alphabet
language $S$, the largest number of length-$n$ inverse words ending at one
ordinary integer has exponential rate

$$\max(0,h_{\rm top}(S)-\log3).$$

An all-interval coefficient-drop constraint gives such a language with
entropy below $\log3$. Its maximum fibers are consequently subexponential.
The condition has to hold on every internal interval; a floor relative only
to the starting integer does not imply it.

There is also an exact asymptotic for the unrestricted shortcut fibers. If
the fraction of odd branches is $\theta$, the maximum fiber rate is
$H(\theta)-\theta\log3$ up to $\theta=1/3$, and
$(1-\theta)\log(3/2)$ thereafter. The total inverse count has growth $4/3$.
These maxima range over endpoints that can depend on the length.

[Arithmetic fiber pressure](operator/ARITHMETIC_PRESSURE.md)
· [finite local rules](operator/FINITE_LOCAL_PRESSURE.md)
· [closed survivor languages](operator/LOCALIZED_SURVIVOR_PRESSURE.md).

## 3. A single finite predictor for all admissible ordinary words

Every finite-alphabet survivor language with entropy below $\log3$ admits,
for every prescribed positive error fraction, one predictor depending only
on finitely many ternary digits. It predicts the inverse exponent with that
error bound uniformly over all sufficiently long admissible ordinary words
and all their endpoints. The predictor does not depend on the chosen
stationary law.

The proof combines the pressure dichotomy with compactness, Dini's theorem
and finite minimax. An effective finite-state search is available when the
closed language can be enumerated by forbidden words and the strict entropy
bound is known.

The packet includes one explicit certificate: for the local allowance
$C=2$, a rule modulo $3^{10}=59,049$ obeys

$$\boxed{9\,\#\text{prediction mistakes}\le n+82}.$$

All 4,111 admissible length-ten words are checked. A bounded integer
potential makes every graph edge satisfy the claimed error inequality, so
the long-word bound follows by telescoping. This is a proof for the stated
local language, not a sampled success rate.

[Uniform theorem](trace/UNIFORM_DECODER.md)
· [explicit rule and proof](trace/EFFECTIVE_DECODER.md)
· [exact executable check](trace/check_decoder.py)
· [record](../../reports/unconventional-20261126/DECODER_CONTROLS.json).

## 4. What ordinary terminating integers can imitate

Let $\alpha=\log_2 3$. The stationary weak limits of complete first-descent
excursions of arbitrarily large ordinary tripling pairs $q,3q$, with both
members ultimately reaching 1, are exactly all stationary legal inverse
processes of finite mean at most $\alpha$. The construction can obey any
prescribed gap bound tending to infinity. With a fixed cap $M\ge2$, the
exact limit class consists of the processes supported at most $M$ with
mean $\alpha$.

The sufficiency proof combines cyclic rotation of sampled exponent blocks,
a negligible compensation segment, strict affine floors and an elementary
binary fusion algorithm. It preserves every earlier state above the source
and forces the final step below it. It then selects a larger ordinary source
in the required congruence class whose two arms fuse and reach 1.

The pressure theorem forces any hypothetical injective ordinary orbit to
have a stationary limit with more than 8.85% of its ergodic mass in
zero-branching components. The terminating constructions can realize these
same statistics. Thus zero branching is a useful structural restriction,
but it is not itself a contradiction or a periodicity theorem.

[Complete-excursion theorem and construction](arithmetic/ORDINARY_STATIONARY_EXCURSIONS.md)
· [independent review](../../reports/unconventional-20261126/reviews/EXCURSION_INDEPENDENT_REVIEW.md)
· [actual fusion Lean kernel](arithmetic/FusionControl.lean)
· [first-descent Lean kernel](arithmetic/FirstDescentFloor.lean).

A separate all-depth capacity theorem limits a proposed smaller-reference
method: with reserve $s$, eligible upper-arm witnesses cover relative odd
density at most $1/(6\cdot2^s)$. The exact depth-40 two-arm calculation gives
reserve-two density between approximately $0.0165748804$ and
$0.0165749043$. An explicit family reaching 1 fails every reserve-one
upper-arm witness. Rational references in the basin of 1 do not enlarge the
specified integral affine route.

[Capacity theorem and exact intervals](arithmetic/REFERENCE_BARRIER.md)
· [independent odd-gap and trie check](../../reports/unconventional-20261126/reviews/review_reference.py).

## 5. A nonlocal quantity that would detect escape

The trace analysis retains the pinned canonical-density inputs from the
external sources listed in its papers; their complete analytic development
was not rebuilt here. With those inputs, an escaping component has a
positive charge $b_C$. If $L_n(a)$ is the actual weighted first-hit mass at
odd target $a$, then for every $p>1$,

$$\lim_{n\to\infty}\frac1n\sum_{a\text{ odd}>0}
\left(\frac{L_n(a)}a\right)^p=\sum_{C\text{ escaping}}b_C^p.$$

The corresponding time-averaged expression has limit
$\sum_Cb_C^p/(p+1)$. Repeated visits to cycles are explicitly removed. The
proof controls all targets, not just a fixed finite sample.

An $o(n)$ upper bound on one of these actual first-hit power sums would
exclude escaping components. Such an upper bound has not been proved.
Finite positive cycles have zero contribution here and need an independent
exclusion argument.

[Escaping-ray depth profile](trace/ESCAPE_TRACE_PROFILE.md)
· [global first-hit moment theorem](trace/FIRST_HIT_SPECTRUM.md).

## 6. Reproduction and the remaining proof obligation

The strict Lean replay rebuilt 16 modules and audited all 121 local theorem
declarations, including private lemmas. It uses only standard Lean axioms.
Two missing dependencies were rebuilt from the pinned Mathlib source in a
temporary mirror. The older eleven closing-interface declarations remain
conditional on their explicit global hypotheses.

```bash
python -B research/unconventional-20261126/replay_lean.py \
  --mathlib /path/to/pinned/mathlib4 --lean /path/to/pinned/lean \
  --check reports/unconventional-20261126/SECOND_LEAN_RECEIPT.json
python -B research/unconventional-20261126/replay_second_wave.py
```

[Strict Lean receipt](../../reports/unconventional-20261126/SECOND_LEAN_RECEIPT.json)
· [normal and optimized complete finite replay](../../reports/unconventional-20261126/SECOND_CONTROL_REPLAY.json).

The remaining global task has two parts: exclude every nontrivial positive
integer cycle, and exclude an injective infinite ordinary orbit. None of
the entropy, spectral, density or formal-interface statements above supplies
both. The final wave is directed specifically at arithmetic information that
persists for one fixed integer, full-denominator cycle restrictions and the
nonlocal first-hit trace.
