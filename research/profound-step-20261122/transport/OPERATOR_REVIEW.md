# Narrow independent reconstruction of the ordinary Wold channels

**Verdict: VERIFIED as written deductions from the displayed harmonic
reference (W1). This is not a verification of that upstream analytic input
or a proof of Collatz.**

Reviewed file: `research/profound-step-20261122/operator/WOLD_CHANNELS.md`.
SHA-256: `bb956069797987478ef3c691115b7292d7a964ac9963c9eed212321aca8f03ce`.
The review is a working-file review, to be bound to the published commit
by the root report. It does not extend automatically to a later file body.

Reviewer lane: the asynchronous transport agent. The class-mass argument
and the zero-frequency pair kernel were reconstructed separately before
reading the complete operator note. This review checks its full printed
W7--W13 statements, including complex amplitudes and uniform frequency
limits; agreement alone is not the evidence.

## W7: every integer clock class has exactly the component capacity

For a fixed class `h`, the inverse fronts
`F_r={x:U^(r-h)x=q_r}` are nested, because one further actual forward step
takes `q_r` to `q_(r+1)`. If `x` has lag `h`, an actual finite meeting
with the reference ray places it in all sufficiently late fronts. Thus
their union is exactly the synchronous class. Iterating the full parent
identity, including all positive unit parents, gives mass `nu(q_r)` to
every front. Monotone convergence gives `C_C`. No source-height cutoff or
inverse-word multiplicity has been omitted. The component has infinitely
many such disjoint classes, despite each class having finite mass.

## W8--W10: the range intersection and its orthogonal projection

For a source killed at time `t`, every vector in `ran S^k` for `k>=t`
vanishes there. If two sources meet at a common clock `k`, every vector
in `ran S^k` takes equal values at them. These prove the necessary
conditions on the range intersection pointwise, since every atom has
positive reference mass.

Conversely, a function constant on each lag class has norm
`sum_(C,h) C_C |b_(C,h)|^2`. Shifting the integer coordinate by any finite
`k` preserves this norm. The shifted function is a genuine preimage
under `S^k`. This proves sufficiency, including negative lag classes, and
gives one bilateral shift per escaping ordinary component.

For a finite-energy source density, the class integral is absolutely
convergent by Cauchy--Schwarz and the finite mass `C_C`. Its orthogonal
projection onto constants on that class is therefore `a(S_(C,h))/C_C`.
Summing the squared projected norms gives W10. Preperiodic sources do
not appear in this unitary projection.

## W11: independent clocks and the phase sign

If two source paths first meet at clocks `(p,q)`, their resolvent cross
kernel on the common escaping tail is

`r^(p+q) exp(i*(p-q)*theta) (1-r^2)
  sum_j r^(2j)/nu(U^j z)`.

The lag difference is `h(x)-h(y)=q-p`, so this phase is exactly the
cross term in `|sum_x a(x) exp(-i*theta*h(x))|^2`. The bounded inverse
reference values converge to `1/C_C`; their geometric Abel means have
that same limit. A finite killed common tail contributes zero after the
normalization. There are only finitely many source pairs for finite
support, so these limits are uniform in `theta`. This reconstructs the
frequency formula without an unproved law-of-large-numbers or spectral
mixing premise.

## W12--W13: the full-source extension and zero frequency

For a singleton source, monotonicity of the reference along its
nonrepeating segment gives normalized resolvent norm at most
`|a(x)|/sqrt(nu(x))`, uniformly in both `r` and `theta`. The sum of these
bounds controls every omitted source tail. The norm difference is thus
uniformly small, and its effect on squared energy is at most the norm
difference times the sum of the two uniformly bounded norms.

The limiting component-amplitude vectors obey the same tail estimate,
because `C_C>=nu(x)` for a source in `C`. Hence both sides of W11 pass
uniformly from finite support to W12. Absolute summability of `a` follows
from `nu<=A`, so the component amplitudes are well defined. Orthogonality
of integer characters gives W10 after circle integration. For nonnegative
sources, all phases equal one at zero frequency and no source mass can
cancel; W13 follows.

## Boundaries retained

- The kernel is killed on entering **any** periodic orbit. It does not
  classify the positive cycles.
- The reference has infinite total mass; a finite-measure ergodic theorem
  has not been substituted for it.
- The construction identifies a potential bilateral summand rather than
  proving that it is absent. Weak stability or lack of unit-circle
  eigenvectors would not remove such a summand.
- The imported positive bounded harmonic reference and its source-qualified
  population inputs were not independently re-proved in this review.
- The Hilbert-space and infinite-sum statements are written mathematics;
  `ClockLags.lean` proves only its declared finite-clock core.

No mathematical or quantifier gap was found in W7--W13 under W1 and the
stated injective-before-killing dynamics.
