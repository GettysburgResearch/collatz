# Root reconstruction of the second wave

Date: 26 November 2026. This review covers the second wave of the three-hour
research sprint. The source identities and integration changes are recorded in
[SECOND_WAVE_SOURCE_MAP.json](SECOND_WAVE_SOURCE_MAP.json). The preceding
[root review](ROOT_REVIEW.md) remains the review of the first checkpoint.

**Verdict:** the exact biased-pressure theorem and its operator consequences
have complete written arguments that survived root reconstruction and two
separately authored reviews. The new ordinary arithmetic controls, reference
capacity bound, and complete-excursion realization theorem also survived
reconstruction. The trace deductions retain their explicitly source-qualified
analytic premises. None of these conclusions settles Collatz. The full measure
and operator arguments are not Lean formalizations.

## 1. Exact biased pressure

The central source is
[EXACT_BERGMAN_PRESSURE.md](../../research/unconventional-20261126/operator/EXACT_BERGMAN_PRESSURE.md),
frozen at SHA256
`5e93fc264fdbf9fe287c90531bab5875d1d7f9745f2ecd4419e9be9edcf5194c`.
This digest also appears in the source map. For the legal ternary inverse
operator with geometric parameter $0<p<1$, the written theorem is

$$r(B_p)=\max(1,3p).$$

The independent reviews are
[the variational review](reviews/PRESSURE_VARIATIONAL_REVIEW.md) and
[the entropy review](reviews/PRESSURE_ENTROPY_REVIEW.md). Root separately
reconstructed the following potentially delicate steps.

### Variational passage and countable labels

The finite path law at a maximizing endpoint bounds the pressure by
$\log3-D(\eta_n\Vert\mu_n\otimes\operatorname{Geom}(p))$. The entropy
inequality with an exponential moment bounds the mean inverse exponent and
gives tightness. The limit uses lower semicontinuity of the **joint relative
entropy**. It does not assert uniform integrability of the means across the
finite path laws. The limiting stationary law has finite mean, so its
individual label entropy and logarithmic geometric weight are integrable.

Markovization retains the joint state/label flow. In an ergodic decomposition,
the invariant field is contained in the completed past; the conditional
transition residual remains zero. Consequently the same state transition
kernel is retained on the components used in the reward bound.

### The entropy dichotomy

For an ergodic inverse process let $\beta=H(E\mid X)$ and let $h_E$ be label
entropy rate. A word $W_n$ determines $B_n=X_0\bmod3^n$. The bound

$$I(W_n;X_0\mid B_n)
\le\sum_{d=1}^n\bigl(H(E\mid X\bmod3^d)-\beta\bigr)=o(n)$$

identifies the ternary dimension as $F=h_E-\beta$.

The conditional cylinder information uses actual cell-averaged Bayes
probabilities, rather than substituting a pointwise posterior at finite
precision. Its telescoping identity gives convergence in $L^1$ after a
triangular Cesàro estimate. Entropies of local state components concentrate at
$F$ only after averaging over the specified interval of scales. No unjustified
uniformity over all cells or scales is used.

For a fixed total exponent, the carry word is injective: successively taking
2-adic valuations decodes its labels. Its integer height is less than
$2^A3^n$. When $A\le Kn$, the carry noise therefore has distinct residues at
depth $Kn$ and contributes at least $n\beta-o(n)$ conditional entropy. The
discarded large-$A$ contribution is controlled by the ergodic $L^1$ theorem
within this one stationary process. Dependence of that noise and the residual
state is only $o(n)$ in mutual information.

The local product approximation conditions each marginal on **its own** lower
digits. The sum of the window relative entropies is at most the window length
times the full mutual information. Removing the total-exponent conditioning
costs $O(\log n)$. Pinsker and finite-alphabet entropy continuity then give a
total $o(n)$ error for each fixed window length.

On the finite group $\mathbb Z/3^m\mathbb Z$, a noise distribution with positive
entropy modulo 3 contains two offsets whose difference generates the group.
Strict concavity implies a strictly positive entropy gain for every base
distribution bounded away from maximal entropy. Compactness makes this gain
uniform with the displayed bounds fixed. This finite-group assertion is
proved in the source, rather than imported from an unchecked infinite
entropy-growth statement.

Finally, the entropy difference $g_j$ used in the argument is not asserted to
be nonnegative or monotone. Summing $g_{j+m}-g_j$ telescopes to the first and
last $m$ values. Those boundary terms are $o(n)$, whereas positive branching
and a dimension deficit would give a positive multiple of $n$. Hence
$\beta=0$ or $F=\log3$. Gibbs' inequality bounds the positive-branching reward
by zero, while the deterministic reward is at most $\log(3p)$. Haar averaging
and the inverse fixed point $-1$ supply the matching lower bounds.

This proof is the substantive advance. Exact finite checks exercise Bayes
posteriors, carry injectivity, window conditioning and strict entropy gains;
they do not replace the limiting argument. The earlier finite-memory entropy
paper cited by the author is a precedent. The steps needed in this extension
are presented in the new source.

## 2. Operator consequences and their domains

The positive induced-resolvent comparison in
[BIASED_PRESSURE.md](../../research/unconventional-20261126/operator/BIASED_PRESSURE.md)
converts the theorem to

$$r(aU+bJ)=\max(a+b/3,b),\qquad a,b>0,$$

on $C(\mathbb Z_3)$, with the precise $U,J$ defined in the source. For
$t>a$, the induced radius is
$\max\{b/[3(t-a)],b/t\}$, so the strict threshold follows directly.
The exact affine-slope representation for the classical Bergman transfer
then gives

$$r(\mathcal T)=\sqrt{20}/3.$$

The disjoint-fiber Hilbert norm identity and arbitrarily large ordinary
representatives of every needed unit residue are essential in transferring
the ternary norm calculation. The argument is not a blanket identification
of all operators called “Collatz operators.”

The rooted weighted-shift proof in
[BERGMAN_DISK.md](../../research/unconventional-20261126/operator/BERGMAN_DISK.md)
establishes the full closed disk as both spectrum and Fredholm essential
spectrum on each ordinary component. The finite nilpotent prefixes justify
the Riesz-projection step; disjoint forks give orthogonal singular sequences.
The same disk occurs on the known basin of 1.

The finite integer vector proves an additional **point-spectrum** disk of
infinite multiplicity, of radius
$\sqrt{207384761192/93324220975}$. Root checked the eigenflow contraction in
the $1/v$ energy and cancellation at the common parent of two child subtrees.
This is slightly smaller than $\sqrt{20}/3$; the source does not establish
the entire open spectral disk as point spectrum.

The product topology result is a different assertion. Its triangular dual
basis conjugates the coefficient map to countably many unilateral backward
shifts. The uniqueness of the dyadic root and the leading pivot give the
continuous inverse. Its all-complex eigenvalues and mixing do not describe
the Bergman norm topology.

## 3. Exact pressure for finite rules and survivor languages

The maximum ordinary shortcut inverse fiber with odd proportion $\theta$ has
exponential rate

$$\begin{cases}
H(\theta)-\theta\log3,&0\le\theta\le1/3,\\
(1-\theta)\log(3/2),&1/3\le\theta\le1.
\end{cases}$$

The lower bound in the second region uses a near-critical core followed by a
common all-odd outer segment. Each maximizing endpoint may change with word
length. Summing the fibers gives the rate $\log(4/3)$, but this is not a
termination-time estimate for a fixed source.

For finitely many allowed labels and a finite ternary rule, the exact radius
is the maximum of the normalized Perron radius of the finite weighted graph
and its largest cycle geometric mean. The periodic codes in the second term
are ternary rational codes, potentially negative or nonintegral. They are
not asserted to be positive integer cycles.

The extension to any closed finite-alphabet subshift $S$ has maximum common
endpoint fiber rate

$$\max(0,h_{\rm top}(S)-\log3).$$

The source handles a non-Markov stationary law by conditioning on the past.
For the maximizing finite fiber, different extensions of its words need
share only the known finite state residue. An interior state residue is
determined by the prefix and the common endpoint residue; finite-window
conditioning therefore survives the averaged limit. Root checked that no
common full ternary state of these extensions is silently assumed. The
separately authored [survivor review](reviews/SURVIVOR_REVIEW.md) reaches the
same conclusion and includes an explicit counterexample to that tempting
stronger assumption.

An all-interval coefficient-drop bound gives a finite-alphabet survivor
language of entropy below $\log3$, hence subexponential fibers. A bound only
relative to the initial point does not provide this all-interval hypothesis.

## 4. Uniform finite prediction, with one exact certificate

For every invariant law on a subshift of entropy less than $\log3$, the
conditional inverse-label entropy given the full ternary state is zero.
Markovization may leave the original subshift, but its state distribution
stays in the compact coded set. That set has dimension below one, excluding
the positive-branching alternative on every ergodic component.

At finite ternary precision the conditional entropy is continuous in the
invariant law and decreases to zero. Dini's theorem makes this convergence
uniform. Finite minimax gives one randomized predictor; argmax rounding costs
at most a factor two. Compactness of empirical laws then makes its long-word
error bound uniform over actual endpoints and finite admissible words. The
last, incompletely observed digits cost only a bounded number of errors.

The effective certificate uses residue depth 10 and the local coefficient
drop allowance $C=2$. All 4,111 admissible words and all corresponding graph
edges are checked. An integer potential satisfies
$9\,\mathrm{mistake}-1\le d(\mathrm{end})-d(\mathrm{start})$ on every edge,
with $0\le d\le10$. Consequently every actual ordinary word satisfying the
local conditions has

$$9\,\#\mathrm{mistakes}\le n+82.$$

This is a uniform, finite, checkable assertion. It neither proves that every
orbit satisfies the local conditions nor turns a prediction error bound
into descent. The abstract theorem also permits a terminating search through
finite supershifts when the subshift is effectively closed and its entropy
bound is supplied as a promise; it supplies no useful universal complexity
estimate.

## 5. Reference capacity and complete first descents

The reference-capacity proof is an all-depth Kraft argument on the actual
inverse tree of 1. The initial odd triple leaves cost at most $1/12$ and later
branches contract mass by at most $2/3$. The lower-reference constraint
$m<q$ removes the otherwise dangerous endpoint count. For reserve $s$, the
eligible upper-arm references have relative odd density at most
$1/(6\cdot2^s)$. Root independently regenerated the depth-40 tree by odd gaps
and computed binary unions by a low-bit trie, reproducing all six exact
intervals in the source. The strict reserve is genuinely restrictive: the
explicit terminating family in the source is outside reserve one while
remaining inside the zero-reserve two-arm class for sufficiently late terms.

Allowing positive rational references in the basin of 1 does not enlarge the
specified integral affine shortcut: its denominator must both divide a
number prime to 3 and be a power of 3, hence is one.

The more substantial stress theorem constructs **complete first-descent
excursions**, not merely selected prefixes. Their stationary weak limits
are exactly all legal stationary inverse laws of finite mean at most
$\alpha=\log_2 3$. With a fixed gap cap $M\ge2$, the limits are exactly those
supported at most $M$ with mean $\alpha$.

Necessity follows from the exact affine product and the last-state bound
$n/2\le x_k<n$. Sufficiency samples long blocks from the desired stationary
law, rotates at a maximal partial deficit, and adds a negligible number of
compensating labels. Every proper coefficient stays above one; the final
coefficient falls below one. At a sufficiently large source, the positive
affine offsets preserve every proper strict inequality and the final
descent. Slowly diverging allowed gap caps are achieved by repeating the
block sufficiently many times before compensation.

The ordinary realization uses an elementary binary fusion algorithm for
the two affine rays $q,3q$. It reduces the power-of-three slope and then the
integer offset. After fusion, a ternary congruence chooses a common terminal
state of the form $(2^{2j}-1)/3$, so both original sources reach 1. Root
checked positivity, arbitrary large representatives and the prescribed
ternary constraints. The multi-ray extension is restricted to slopes
$3^d$, as required by that reduction. It does not cover arbitrary odd slopes.

The independent [excursion review](reviews/EXCURSION_INDEPENDENT_REVIEW.md)
and raw-integer replay use sources of 204–381 bits and independently check
first crossing and termination of every displayed ray.

As a corollary of the pressure theorem, an injective ordinary orbit would
have a stationary limit with at least $5680/64179>0.0885$ of its ergodic mass
in zero-branching components. A zero-branching component is a deterministic
measurable inverse rule, not necessarily a constant or periodic rule. The
complete-excursion construction realizes such limiting statistics using
terminating sources. This identifies why stationary statistics alone have
not closed the one-source argument.

## 6. Trace deductions retain their inputs

The canonical trace and its positive density inputs come from the precisely
pinned external sources cited in the two trace papers. Their full analytic
dependency chain was not rebuilt here. With those inputs retained, the new
deductions are valid:

- An injective ray has a positive limiting charge $b_C$ and a uniformly
  convergent centered inverse-depth profile.
- The Cesàro profile is a ramp, with the threshold clock asymptotic
  $i/(1-\eta)$; the stronger pointwise lower-envelope input gives a raw
  transition at $i+O(1)$.
- For every $p>1$, the normalized first-hit power sums tend to
  $\sum_C b_C^p$, and their averaged counterparts tend to
  $\sum_C b_C^p/(p+1)$.

Root checked the cyclic first-hit correction, the total harmonic mass bound,
the infinite-target tail, the small-ancestor cutoff and the passage from
finitely many represented rays to all components. The finite-cycle
contribution vanishes in these limits. Consequently even a proof of vanishing
escape charge would leave positive-cycle exclusion to a separate argument.

The unknown step is an actual $o(n)$ upper bound on a first-hit power sum, or
another argument forcing every escape charge to vanish. The trace formulas
identify that obligation; they do not prove it.

## 7. Formal and executable boundaries

[SECOND_LEAN_RECEIPT.json](SECOND_LEAN_RECEIPT.json) records a fresh strict
build of 16 project modules and audits all 121 local theorem declarations,
including private lemmas. Only `propext`, `Classical.choice`, and `Quot.sound`
occur, or no axioms. Two missing modules from the pinned Mathlib source were
rebuilt in a temporary mirror; no toolchain source was changed. The eleven
previously repaired closing interfaces still have their global premises as
explicit parameters.

The new Lean contributions cover first-descent floors, actual synchronized
binary fusion on full arithmetic cylinders, reference capacity arithmetic,
triangular pivots, carry injectivity and finite entropy-window algebra.
They do not formalize the full pressure theorem, ergodic theory, analytic
trace inputs or Collatz.

The second control replay compares every complete recorded JSON payload in
normal and optimized Python, including four independently authored control
scripts, and regenerates the 59,049-entry integer vector. The root structural
validator has a separate clean-checkout receipt. These evidence layers are
kept distinct throughout the scientific front door.
