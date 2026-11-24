# Principal reconstruction and verification boundary

23 November 2026. Parent checkpoint:
`cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`.

**Verdict: VERIFIED at the finite formal and stated written-proof scopes
below. Full Collatz and the required collision upper remain OPEN.**
This is an in-session research review, not outside peer acceptance.
Root authored the ternary-information argument, the rational verifier
and the combined same-source replay. Their independent reviews are
separate: `RATIONAL_SOURCE_REVIEW.md` and `TERNARY_PRESSURE_REVIEW.md`.
The entropy, rational-accounting and cycle notes were authored in
separate parallel lanes. `ENTROPY_CYCLE_REVIEW.md` supplies a second
independent reconstruction of the entropy and rational-accounting work.

All final files are bound in `SOURCE_BINDING.json`. The execution
receipts additionally bind every compiled input and replay source.
No verdict extends to later edits or to neighboring upstream claims.

## 1. Rational certificate and exact recognizer

Root reconstructed all sections of `TRIADIC_CONSTRUCTION.md` and read
every branch of its Lean core. The literal paired equations preserve
the positive ordinary source and signed numerator; q remains the full
fixed denominator in the general proof. Original 1 terminates the
argument. Before that event, odd inputs are at least 3, giving the
`5/6` potential bound. A near-neutral positive numerator step produces
a next numerator greater than `2q`, where the next compatible step
contracts by at least `7/8`. Negative numerators already have the
stronger `3/4` bound. Pairing requires both input clocks to be large
and both original input states at least 2; the stated countercontrol
shows why that guard cannot be dropped.

The signed small-state charge is not multiplied by the number of
excursions. Each nonzero signed magnitude occurs at most once before
the first small-numerator repetition. The full product is the square
of the central binomial coefficient; zero costs one further factor
two. The resulting M bounds both original sources at the repeated
numerator. With at most `2q+1` small clocks, at most `2q+2` large
runs leave at most that many unmatched clocks. The displayed budget
forces at least `7L` contracting pairs and contradicts positive
integrality. The final output state of a counted step may be 1;
its potential is still positive, and no contraction is applied from
that terminal state.

For the sufficient parity certificate, the extra L bits give equal
ordinary parity prefixes after the repeated numerator. Their complete
affine carries cancel, forcing source equality modulo `2^L`. Both
actual positive sources are below that modulus, so they coincide.
For exact candidate recognition, a repeated numerator with unequal
original states can instead be rejected: all-time compatibility would
force equal complete parity vectors and hence equality modulo every
power of two. This explains the smaller decision budget without
silently omitting the sufficient certificate's parity tail.

In mixed mode, reduction occurs once initially. Every original-even
step at a positive three-level removes exactly one factor of three.
The numerator remains a unit at three until exhaustion; its absolute
value stays below the initial B0 bound. Long original-odd runs cannot
divide that nonzero bounded integer indefinitely. The small-state
dictionary is used only after the denominator stops changing, so it
cannot confuse two equal numerators at different denominators.

Root also checked the actual CLI's state clocks and exact acceptance:
parity failure first, original 1 compared to `2*current_q`, repeated
small numerator compared with its stored ordinary source, and at most
`bound-1` transitions. A general/mixed budget violation raises an
error; it is not masked as rejection. The automatic triadic branch
uses the preceding strict necessary stopping bound. Zero, negative
and unreduced candidates retain their literal rational values.

**Formal scope:** eight public statements formalize the branch
estimates, exact product, signed bound and final numerical
contradiction. Visited-state counting, repetition selection, the
complete recognizer theorem and mixed-denominator consumer are written.
No successful universal selector or general positive-cycle exclusion
is inferred.

## 2. Same-source entropy and the direct odd-gap improvement

Root reconstructed the finite source congruence, endpoint normalizations
and the two stationary-limit passages in `FIXED_SOURCE_PRESSURE.md`.
Equal actual parity words have equal complete affine corrections and
therefore sources equal modulo the full binary clock. The finite Lean
module first proves that identity for its own definitions of the
ordinary shortcut and parity prefix. Height injection and the
arbitrary-height quotient-cell count then follow without changing the
source or choosing a new modular representative.

For a sampled long word, every internal k-window law is dominated by
the full empirical k-law with the exact factor
`(N-k+1)/(N-m+1)`. The final shorter remainder is a projection of an
internal k-window. Entropy subadditivity does not require independent
or disjoint comparison windows. Taking m at the actual height scale
before passing any limit yields the claimed tradeoff; only fixed-k
entropy is then passed to the stationary law. A further subsequence
realizing a finite liminf retains the same law, so zero entropy forces
the height exponent to tend to infinity on that original subsequence.

On the backward odd clock, the exact logarithmic identity gives a
uniform first-moment bound. The note does not confuse that bound with
uniform integrability of the gap. Instead it proves entropy tail
control using the linear integer cost and the geometric entropy bound.
For fixed tuple length, the tail entropy tends uniformly to zero even
if some first-moment mass escapes. This validates fixed-block entropy
continuity while retaining only `a<=ell` for the limiting mean.

The ergodic strengthening first truncates the gap. The finite
`R(K-1)/m` comparison controls each m-window by its internal K-window
averages. The limit with K fixed precedes the ergodic K limit. Thus
the growing-window good fraction is obtained without assuming a
growing-block convergence rate. A good word's total binary clock
exceeds the actual source height, making that word unique among all
sampled occurrences, not merely unique within a selected subset.
Its exact mass is the full empirical `1/(M-m+1)`, and the blocking
argument gives `h(eta)>=a log(2)/beta`.

The critical mechanical control is also exact. Its positive gaps
lie in `{1,2}`, and these are decoded successively from ternary
residues. The irrational rotation gives exactly m+1 word cells with
vanishing maximal cell size. Hence the ternary law is nonatomic but
has zero dimension and collision at least `1/(m+1)`. The sparse
quadratic-growth modification preserves zero stationary entropy and
would violate the newly proved source-height inequality if one fixed
positive ordinary source realized it. It is not treated as an
escaping ordinary orbit.

**Formal scope:** seven public statements prove actual finite affine
coding, source congruence, height injection and finite cardinalities.
Shannon inequalities, stationary limits, ergodicity and entropy
continuity remain written proofs, independently reconstructed in the
cycle lane. No infinite entropy theorem was executed by Lean.

## 3. Ternary information theorem: root authorship and external checks

`TERNARY_INFORMATION.md` gives a direct proof for arbitrary ergodic
positive-gap processes of finite mean at most ell. Root checked its
finite arithmetic against the earlier complete-carry decoder and
credited the related fixed-total mechanism in Paper 9. The infinite
argument uses classical countable-alphabet SMB and martingale
convergence with their finite-entropy and sigma-algebra hypotheses
stated. It does not import an iid theorem into an arbitrary process.

The nonnegative drift gives a subexponential typical carry quotient.
The total clock remains linear. Bounding both gives subexponential
fibre multiplicity; neither coordinate is silently discarded. The
restriction-to-full-measure step uses the Radon--Nikodym density
martingale in the correct direction. A positive limiting density
transfers each restricted ball upper bound to the full ball mass.
The opposite local-dimension inequality follows from a whole word
cylinder mapping into the same ball. Fatou then gives the missing
entropy liminf and the conditional decoding entropy is o(m).

The final consumer uses the actual reversed odd-gap theorem directly,
without identifying two separately chosen stationary clocks. The
complete past affine equation identifies its ternary law at each
fixed depth. The result retains finite beta and ergodicity and covers
possible lost gap mean. Both the entropy lane and rational lane
independently reviewed the final proof. Their reports bind its bytes.

**Limit:** exact local and Shannon dimension do not imply the needed
untrimmed order-two collision bound. The typical-set complement has
no proved exponential mass rate. Neither height nor ergodicity is
established unconditionally for an escaping ordinary source. This
packet adds no Lean formalization of that infinite theorem.

## 4. Cycle obstruction and the source grid

Root reconstructed the circuit theorem using full C and D and the
exact equality `gcd(D,C)=gcd(D,2^h-1)`. The legal rational parities
follow from the displayed intermediate numerators, not from freely
chosen real branches. The two-run word is primitive, its rational
states are distinct and its least proper gap is `(m+1)/2`.

Fixing a small rotation interval after choosing B allows arbitrarily
large p; it does not require a changing source or unbounded continued-
fraction partial quotients in an unstated way. The lower bound on the
fully reduced denominator then exceeds any independently prescribed Q.
The near-critical ratio also ensures all proper prefix coefficients
exceed one while the full coefficient is below one. This disproves
the proposed small-gap implication under those hypotheses at all
thresholds.

For ordinary realizers, the leading odd run forces `n=-1 mod 2^p`.
In the selected range this source grid lies above the rational fixed
point, so the complete affine return descends. The distinction rules
out these words as ordinary cycles; it does not exclude all words.
The primary extremal-word and high-cycle results retain their actual
scopes and are not upgraded to universal integrality statements.

## 5. Source review of the executable controls

Root read both lane replay modules before executing the combined
checker. The rational oracle computes finite ordinary trajectories
to 1 and pulls terminal dual 2 backward with `Fraction`, independently
of the verifier's event/budget implementation. Nontriadic terminals
are pulled through proper actual prefixes; their entire prescribed
prefix and the observed paired trace are checked separately. The
trace checks literal rational edges and each exact factor-three
denominator drop. The report explicitly leaves nontrivial positive
repeated-pair acceptance unexercised.

The carry replay compares an explicit backward-gap sum with a
chronological shortcut recurrence. Its two injection keys retain the
total clock and full quotient, and exact collision witnesses show
why those coordinates cannot simply be dropped. The circuit replay
uses full gcds, legal reduced rational parities, all bounded rotated
carries and independently computed ordinary source residues. The
large fixtures use closed-form and whole-run divisibility checks;
their long trajectories are not falsely described as enumerated.

The combined source-pressure checks were independently source-reviewed
by the entropy lane. They test the complete ordinary and reversed-gap
identities, exact word multiplicity, and finite endpoint averaging
with `Fraction` arithmetic and center `3/2`. They do not test an
infinite entropy statement numerically. Every Python guard remains
active under `-O`; the two output files are compared byte for byte.

Fresh formal execution and exact numerical counts are in the separate
receipts and report README. A clean complete checkout's five-command
integrity gate is a structural check, not mathematical verification.
The final published checkout and remote tree are checked separately.
