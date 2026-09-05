# Scoped errata and pending replacement wording

This record implements the review boundary, not retroactive verification. The original source versions are preserved at their exact commits; the pre-correction versions of the seven D-affected reading surfaces are also archived locally. Active replacements and dependency warnings are identified below, rather than silently substituted for reviewed originals. **The two E-INTEGRATION endpoint replacements and the E-D replacements/qualifications below are PROPOSED pending narrow independent review of their exact wording.** An unrestricted original is not accepted through an adjacent passing result.

## E-INTEGRATION-001 — positive-beta timed bootstrap

Source: PR88 `c28922fb6d1c070bf86a76192f40bc9ea3edd67c`, `research/external/mazur-2026/fixed-height-forward-power-saving.md`, MZ-FH-005. Review: [A, RA-021/022 and RP-A1](../../reports/prepublic-2026-09-05/reviewer-a/ACTION_MAP.md).

Proposed restriction: retain every original descent, fiber, scale and horizon hypothesis and require **beta>0** as well as `beta>max(1-D,1-delta/(1-r))` for the timed conclusion. A reconstructed the intended positive-beta range; the printed unrestricted nonpositive endpoint requires a separate argument.

A dyadic sum of `2^(j beta)` has the required upper-scale power for positive beta. At beta=0 it retains the number of shells; at negative beta a fixed small-source contribution is not bounded by a vanishing large-X power. This does not instantiate the missing survivor-specific fiber hypothesis. The intended crossing application below 0.901 remains conditional.

## E-INTEGRATION-002 — zero affine remainder before logarithms

Source: PR92 `7bb6d36d3bc37dd09b52aa9a23c8e33973032359`, `research/astra-three-routes/pass2/SC_TAIL_AND_ECHO.md`, T-A3-453. Review: [B, F03](../../reports/prepublic-2026-09-05/reviewer-b/INTEGRATION_CHECKLIST.md).

Proposed guard: process `A_w=0` before the displayed logarithmic cutoff; use that cutoff only for `A_w>0`. Preserve all original positivity, integrality, displacement, full-denominator and prefix conditions.

A zero affine remainder has no odd contribution. A nonempty first coefficient-crossing word is therefore the one-letter word `0`. Its equation `A_w=D n+2^j d`, with `D=1`, `j=1`, `n>0` and `d>=0`, is impossible. Thus this no-descent displacement interval is empty, without evaluating the undefined zero logarithm. This is an endpoint repair, not an all-word ordinary exclusion theorem.

## E-INTEGRATION-003 — orbit terminology

The orbitwise counting and SC-tail summaries use **infinite distinct value set / non-eventually-periodic positive orbit**. A finite cycle repeated indefinitely is not an injective counting input. This is the scope retained by B for T-A3-403/451; neither the old periodic synthesis nor the SC*/FC* bridge is promoted.

## Software repairs are separate evidence

The affected active assertion-based verifier entry points reject optimized Python and authenticate preserved source bytes before delegation. PR88 regeneration uses a temporary directory and a uniquely named immutable report. Their implementation tests appear in [replay policy](../../docs/REPLAY_POLICY.md), not as independent review of a changed mathematical theorem.

## Reviewer D follow-up: scope and provenance

D reviewed main `cd1b3689e8d37fc4232945072e2faf6bd5ee47bd`; the complete final report is PR98 at `1c7744bcb9ded9336036919ffc7a19b5576ea58e`. Read [FINAL_HANDOFF](../../reports/prepublic-2026-09-05/reviewer-d/FINAL_HANDOFF.md) for the 44 original rows, six finishing rows, exact dependencies, and exclusions. The [separate D record](../../claims/followups/reviewer-d-2026-09-05.json) and [integration receipt](../../reports/prepublic-2026-09-05/integration-d/README.md) do not amend A/B's frozen assignment record.

The retained core results keep their existing statuses. **E-D-001 through E-D-008 are scoped replacement text or dependency qualifications, PROPOSED pending narrow independent review of their exact new wording.** The erroneous auxiliary statements are not admitted by their neighbors' verdicts. The [pre-correction archive](../../archive/reviewer-d-2026-09-05/README.md) preserves every changed source body and its Git blob. No periodic synthesis, old bridge, recent reference assembly, or external theorem is promoted here. D's inspection-only rows are not proof approvals.

## E-D-001 — signed digit example

**Finding FD-01; active surface:** [ordinary extraction](ordinary-extraction/README.md), adversarial example 4. The former inference from infinitely many nonzero appended blocks to nonordinariness is rejected. The correct conclusion excludes nonnegative ordinary values; a negative integer is still possible on an eventual maximal face.

For every `J>=0`, the residues of `-2^J` modulo `2^n` are zero when `n<=J`, and `2^n-2^J` afterward. Thus the appended binary digits are `J` zeros and then ones forever. To conclude nonordinariness one must exclude both eventual zero and eventual maximal tails. The two signed stabilization theorems are unchanged.

## E-D-002 — positive realization and controller scope

**Finding FD-02; active surface:** [periodic tails](periodic-tails/README.md). A nonempty word has a positive ordinary realization when `C_w>0`, `D=2^L-3^s>0`, the whole `D` divides `C_w`, and the branches replay. Nontriviality is an additional counterexample condition, not part of positive realization: `10` and `01` realize `1` and `2`. The all-zero word, signed realizers and exact preperiod replay remain separate.

The controller corollary requires deterministic autonomous finite-state evolution, fixed finite emitted parity blocks, and infinitely productive output. The eventual control cycle must emit at least one bit; a nondeterministic or externally driven finite graph alone does not force a periodic parity word. The exact integrated periodic synthesis remains PENDING NARROW INDEPENDENT REVIEW.

## E-D-003 — empty depth and high quotient normalization

**Finding FD-03; active surface:** [L-0041](../../claims/lemmas/L-0041-six-branch-root-cap-recurrence.md). The positive empty-depth minimum is `m_0=1`, while `R_empty=S_empty=0` are canonical residues. The identity `m_n=min R_w` over length-n words applies only for `n>=1`. The append recurrence at `n=0` follows directly, without identifying those two different minima.

Increasing the initial value by `Q^(n+1)h` increases the pre-final value by `P^n Qh`, its high quotient by `P^n h`, and its next output by `P^(n+1)h`. The old quotient sentence had an extra factor Q. The append/output recurrence and positive-depth least-root argument survive.

## E-D-004 — efficient repeats and the zero completion

**Finding FD-04; active surfaces:** the [factor-complexity dependency table](factor-complexity/README.md#dependency-provenance) and [centered/adelic catalog entry](../RESULTS_CATALOG.md#centeredadelic-ordinary-sections-and-weighted-eq). A claim of appended-block nonstabilization for efficient-repeat codes must exclude constant codes. Both constants have efficient repeats, zero completion, and all appended blocks zero. The strict recurrence cone for nontrivial ordinary itineraries, the separate nonconstant repair, and the Thue–Morse application survive.

Affected source: `research/adelic-cusp/claims/T-9316-efficient-recurrence-thue-morse.md`, Git blob `6b8b480a2b8dee84ff91a3eb3e67f957943f88a1`, at both PR16 pins `900ba417c968d8a41bc56a30d3ccc941284d8ce2` and `87478352e65c7b816dfc8b3b30894b71fb50f662`. D's final identity check extends the warning to those two exact bodies only, not the whole branch. Historical PASSED labels in the dependency table are explicitly clause-limited.

## E-D-005 — closed strips, endpoints and open cylinders

**Finding FD-05; same active surfaces as E-D-004.** For arbitrary binary codes, retain the closed strip `|u_n|<=1/N` and the explicit convergent series. From `u_n=(e_n-x_(n+1))/N`, the current codes `1000...` and `0111...` attain `+1/N` and `-1/N`. A nonconstant current tail does not suffice for strictness. Codes not eventually constant have strictly interior, nonzero errors at every time; positive ordinary centered orbits have a separate endpoint-exclusion argument.

When `0<M/N<1`, the nonempty nested open cylinders `(0,(M/N)^k/N)` have empty infinite intersection. Their closures meet at zero. Open-interval invariance is not an infinite-support theorem. The closed-strip construction, cylinder arithmetic, and positive ordinary bridge remain valid. **The resident factor screen still requires only nonconstancy**, not aperiodicity or non-eventual constancy: its ordinary bridge supplies the stronger endpoint facts when needed.

Affected source: `research/adelic-cusp/claims/L-9313-centered-error-full-shift-cylinder.md`, blob `cddc4825d373ee7234e34b602a7add7feb39e324`, at the same two PR16 pins. No entire source file is approved by this qualification.

## E-D-006 — polynomiality is not full tree rigidity

**Finding FD-06; active surface:** [L-0042](../../claims/lemmas/L-0042-syndetic-integral-algebraic-branches.md). The rational-polynomial conclusion for the stated analytic branch and bounded-gap integer domain survives. The unconditional transfer to full-tree rigidity is GAP-BLOCKED.

The polynomial `X/2` is integral on even inputs, a syndetic set, but not on all late integers. Full-tail integrality, eventual positivity, finite control, all-six-child coverage and the exact section laws must still be established before applying the appropriate rigidity theorem. A proper sublanguage need not provide them. The narrower resident affine/rational theorem is unchanged; there is no new theorem requiring every escaping sublanguage to have unbounded gaps.

## E-D-007 — overlap quantifiers

**D-038 clarification; active surface:** [T-0046](../../claims/theorems/T-0046-two-sided-cap-root-overlap.md), section 5. For a fixed candidate `x>0`, let `[L_n(x),U_n(x)]` be its proved growth window and let `E_n(x)` be all integer lengths `ell>=1` whose bands `[Q^(ell-1),Q^ell)` meet that window.

The OPEN sufficient target quantifies: **for each fixed candidate x**, at cofinally many times with `Q^n>x`, exclude `B_(n,ell)` for **every ell in E_n(x)**. An actual surviving orbit would supply a bridge at its actual feasible length, giving the conditional contradiction. One chosen sequence of lengths with the right limiting ratio is insufficient. The alternate chain target must keep one stabilized initial root and every physical extension law. Neither target is proved empty here.

## E-D-008 — historical PR65 repair boundary

**Prior review conditions preserved, not a new D discovery; active surfaces:** [six-branch extensions catalog](../RESULTS_CATALOG.md#six-branch-extensions-beyond-the-resident-rigidity-packet) and L-0042's audit note. Source: PR65 `2183dc7e66162684e464913a4ae1a222b41b30f3`, `research/six-branch-extraction/claims/T-7501-finite-algebraic-section-rigidity.md`, blob `f43db5aab077f2e5c809274041ac45c1e9035cb6`.

The prior [review at 591a06ad](https://github.com/GettysburgResearch/collatz/blob/591a06ad914b63dddfd65ee658dbec36291ffbc0/reports/gpt56-cartographer-01/2026-08-01-pre-public-review-pr64-pr65-pr66.md) already required the constant-branch case, rigorous finite differences via derivative control, an explicit coefficient field for broader semialgebraic claims, and the exact Newton–Puiseux input/reference. Those obligations remain visible before any import. Constants cannot satisfy all six distinct child congruences; this observation does not silently complete the printed proof. An arbitrary real-semialgebraic branch is not automatically over `Q(X)`. No unlocated L-0040/T-0044 variant or later algebraic delta inherits a verdict from this record.
