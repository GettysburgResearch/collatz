# Three global Collatz attempts: ordinary spectrum, arithmetic, and merger guards

**Collatz remains OPEN.** This packet develops three attempts at the
universal implication. It contains elementary structural theorems,
explicit ordinary witnesses, two new smaller-comparison identities,
and exact failed closing calculations. None excludes every positive
nontrivial cycle or every positive nonperiodic orbit.

The shortcut map is `T(n)=n/2` for even `n` and `(3n+1)/2` for odd `n`.
The accelerated odd map is

\[
U(n)=\frac{3n+1}{2^{a(n)}},\qquad a(n)=v_2(3n+1),
\]

on positive odd ordinary integers. Rational witnesses use the explicitly
stated extension by numerator parity with odd reduced denominator.
They are never substituted for a fixed ordinary source.

All new claims remain **PROPOSED**. Separate AI agents reconstructed the
other routes' written proofs at exact file hashes. The reviews are
included; no external referee acceptance or formal proof is claimed.
The frozen dependencies and corrected comparison with the preceding
pass are in [SOURCE_BOUNDARIES.md](SOURCE_BOUNDARIES.md).

## Results and the precise unfinished step

| Route | Result in this packet | First missing global implication |
| --- | --- | --- |
| Ordinary operators | The entire unit circle is essential approximate point spectrum for the two specified derivative-weighted operators, already on the basin of 1. Exact finite supports certify arbitrarily small residuals. | An estimate on the particular all-source moment, or regularity of the actual infinite product, is still needed to exclude escape. A spectral gap cannot provide it. |
| Arithmetic approximation | Positive noninteger rational cycles meet any prescribed neighborhood of a positive real number and any finite set of the stated arithmetic observations. Their full denominators grow. The natural fixed-source product has an exact obstruction; shifting by one yields a different conditional route. | The shifted route requires algebraicity of its limiting real number and a genuine power saving coupled to the actual future defects. Neither is supplied by local congruences. |
| Ordinary two-arm descent | Exact orientation-aware guards, two additional smaller-tripling equivalences, and a family surviving every fixed horizon of those guards. | Every fixed positive even source must eventually trigger a successful guard, or receive another certificate under one well-founded rank. No such termination theorem is proved. |

## 1. A spectral obstruction built entirely from convergent integers

On `l2` of all positive odd integers put

\[
(A_s f)(n)=\left(\frac3{2^{a(n)}}\right)^s f(U(n)),
\qquad s=1,2.
\]

These are the operators of frozen PR143 and PR144, with the spaces,
weights, and treatment of the state 1 kept intact. The theorem is
unconditional:

\[
\text{For every }|z|=1\text{ there are orthonormal }f_k
\text{ supported on the basin of 1 with }
\|(A_s-zI)f_k\|_2\longrightarrow0.
\]

The construction uses the explicit immediate predecessors

\[
t_k=\frac{2^{3^{k-1}+1}-1}{3},\qquad k\ge2.
\]

Each has a certified chain of `k-1` valuation-one odd steps entering it
from a much smaller integer, then one step to 1. Their full predecessor
basins are disjoint. Reciprocal-power profiles on these basins have
vanishing root leakage for the comparison operator
`B_s f(n)=(U(n)/n)^s f(U(n))`. The difference `B_s-A_s` is compact,
with explicit column norms. This transfers the approximate eigenvectors
without assuming any unknown orbit behavior.

The distinction from an actual fixed vector is essential. On the entire
basin supporting these witnesses, the exact unit-circle eigenspace of
`A_s` is zero. Thus a Fredholm or bounded-inverse estimate at 1 would
fail even if Collatz were true. This theorem does not refute strong
convergence on a specified vector or the proposed diagonal-moment bound.

The proof also gives a terminating finite-support construction for any
rational accuracy. Two compact, reproducible 512-state certificates give
these strict residual-norm bounds, simultaneously for every `|z|=1`:

| Root parameter | `A_1` | `A_2` |
| --- | ---: | ---: |
| `k=6` | `<93/1000` | `<16/1000` |
| `k=8` | `<41/1000` | `<31/10000` |

The complete infinite predecessor contribution is summed exactly by
residue-class geometric series; a finite matrix truncation is not used
as the operator. A separate verifier recomputes the residual as the
sum of root leakage, internal loss, and external-fiber terms, all
nonnegative, and obtains the same strict bounds.

Read [the proof](ORDINARY_ESSENTIAL_SPECTRUM.md) and
[its independent review](REVIEW_ORDINARY_SPECTRUM.md).
[The analytic follow-up](SMOOTHING_BOUNDARY.md) tests three possible
closing mechanisms. It proves that the natural finite-clock and positive
averaging profiles fail adjacent smoothing, and that the critical inverse
perpetuity is finite almost surely but has infinite mean. Its remaining
joint real/ternary moment estimate is displayed explicitly.

The [signed-filter extension](SIGNED_CLOCK_FILTERS.md) then checks a
loophole deliberately left outside that note. Among all fixed absolutely
summable real or complex linear combinations of the finite products,
adjacent smoothing holds exactly for filters supported on clocks 0 and 1.
The proof supplies adjacent ordinary witnesses for every finite landing
time. Bounded-total-variation signed averaging families moving to late
clocks retain a jump of at least one in the stated limit order. This
still makes no claim about regularity of the actual pointwise limit.
The [scoped annex review](REVIEW_ROOT_ANNEXES.md) reconstructs this proof
and the independent positive-residual verification.

## 2. Finite arithmetic observations and a genuine fixed-source test

The rational-cycle construction can independently prescribe a neighborhood
of a positive real number, a binary residue, a ternary unit residue, and further
residues modulo any fixed integer coprime to six. Its positive cycles
also have positive repeated inverse score. Their denominators are
coprime to every controlled prime and necessarily grow without bound.
This does not produce a noninteger rational integral at every prime.

For a prescribed ordinary integer `n`, simultaneous precision forces
the exact cost

\[
\operatorname{den}(r)\,|r-n|\ge2^K3^M Q,
\]

where `Q` encodes the additional finite observations. The construction
pays that cost with its denominator. Real density alone is classical;
the source comparison explicitly credits it.

The attempted closure then keeps one ordinary source fixed instead of
changing witnesses. If its actual shortcut prefix ends at `n_K`, its
natural periodic pin satisfies

\[
r_K-n=\frac{2^K(n_K-n)}{2^K-3^q},
\qquad
\gcd(C,|2^K-3^q|)=\gcd(n_K-n,|2^K-3^q|).
\]

The local-height inequality reduces exactly to a positive integer factor
already present in the endpoint difference. It has not forced a return.

On a hypothetical nonperiodic odd-unit orbit, write
`lambda_j=2^{A_j}/3^j` and `L_j=lambda_j n_j`, with `L_j -> L` using
the identified simple-path reciprocal bound. The natural product for
the unshifted two-coordinate Subspace-Theorem attempt is strictly above
one. Shifting to `lambda_j(n_j+1)` cancels valuation-one affine defects
and changes that product to

\[
\mathcal P'_j=
\frac{\mathcal P_j-1}
 {2^{v_2(n_j+1)}3^{v_3(n_j+1)}}.
\]

The primitive height includes the exact common ternary cancellation.
This is a different architecture, but its two global hypotheses remain
unproved: `L` must be algebraic and the displayed expression must have
a power saving infinitely often. Replacing `L` with a fixed known
algebraic value different from it cannot supply that saving.

Read [joint density](ADIC_REAL_DENSITY.md),
[additional finite places](FINITE_PLACES.md),
[the fixed-source calculation](FIXED_SOURCE_CLOSURE.md),
[the shifted attempt](SHIFTED_LINEARIZATION.md), and
[the independent reconstruction](REVIEW_ARITHMETIC_ROUTES.md).

## 3. Physical orientation improves descent, but a fixed clock budget fails

Let `f(x)=f(y)` mean that the two ordinary forward orbits eventually
meet, allowing different clocks. Put `P(n): f(n)=f(3n)` and
`Q(a): f(a)=f(3a-1)`.

A least nonconverger must be `m=2a-1` with `a` even. In the pair
`(a,3a-1)`, the first arm converges and the second would not. This
orientation matters: some returns increase the canonical Q parameter
while sending the physical bad arm below the original floor `m`.
They are valid descents that a scalar-parameter rank would miss.

The exact section algebra also gives, for every `u>=0`,

\[
P(25+64u)\iff P(7+18u),\qquad
P(93+128u)\iff P(13+18u).
\]

Both comparison parameters on the right are smaller. These add two
explicit classes to the frozen source's smaller-comparison program;
they do not form a complete cover.

For any chosen horizon `H>=3`, however, the positive family
`a=2^H t-2` survives the stated physical guards through `H` clocks.
The designated second arm stays above `2a-1`, neither arm meets the
other at any pair of clocks up to `H`, and there is no simultaneous
numerical Q section at clocks `1,...,H`. A stated parity choice for `t` also keeps every
immediate odd-part guard above the floor.

The proof is by exact formulas and divisibility, not a longer census.
The compatible infinite code for this particular family represents
the signed source `a=-2`; the positive least representatives go to
infinity. This is therefore a bounded-horizon obstruction, not a
positive nonconvergent trajectory. It leaves source-dependent,
unbounded termination as the essential unsolved task.

Read [the complete guards, identities, and horizon proof](Q_SECTION_GUARDS.md)
and [its independent reconstruction](REVIEW_Q_SECTION_GUARDS.md).

## Evidence and use

The companion scripts use integer arithmetic, exact fractions, and
explicit rational outward enclosures. Ordinary Python and `-OO` replays
are compared byte for byte. Separate reviewer code reconstructs the
arithmetic witnesses without importing author arithmetic routines; the
independent spectral verifier reuses only the tree producer and computes
acceptance through a different positive-sum formula.

The [execution and publication record](../../reports/2026-11-20-global-rigidity/README.md)
contains exact commands, file hashes, review boundaries, and the clean
complete-checkout receipt. Repository validation establishes structural
integrity and the stated finite regressions; it does not certify the
infinite mathematical claims.

The next proof must supply an actual global estimate or a terminating
ordinary selector at the boundaries above. Neither more approximate
eigenvectors, more locally convincing rational cycles, nor longer
bounded merger searches is such a proof.
