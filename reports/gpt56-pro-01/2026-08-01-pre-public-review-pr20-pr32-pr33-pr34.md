# Pre-public independent review — PRs #20, #32, #33, and #34

**Reviewer:** `gpt56-pro-01` (`GPT-5.6 Pro`)  
**Review date:** 2026-08-01  
**Status boundary:** independent frozen-head review; no merge, no claim of a Collatz proof or counterexample

## Frozen commits and overall verdicts

| PR | Frozen head | Overall verdict |
|---:|:---|:---|
| #20 | `82ca2f932438a9fe0897704ba62959ca23ec830f` | **VERIFIED WITH FIXES** |
| #32 | `bc397f0f4c80cb001493beaebb170ea880f4a114` | **VERIFIED** |
| #33 | `c9d62bce3e93f5785f72e4520bc576863d9379eb` | **VERIFIED** within its exact frozen corrected-stage scope |
| #34 | `b7eec65ffb13c5a89415a888c0153f36a52f23e3` | **GAP/BLOCKED** as a monolithic pre-public merge; substantial claim subsets verified below |

## Review method

I froze the heads above before inspection. I rederived the principal identities, checked endpoint and sign conventions, traced dependencies to the frozen source blobs, inspected proof-producing and regression code, and used only small exact-arithmetic checks. I did **not** rerun the expensive enumerations.

The classifications mean:

- **VERIFIED:** the reviewed theorem chain and its declared scope survived independent reconstruction.
- **VERIFIED WITH FIXES:** the mathematics survives, but source, metadata, checker-independence, or scope text must be repaired before public promotion.
- **GAP/BLOCKED:** at least one load-bearing theorem in the merge unit is incomplete or has not crossed the proof boundary. Earlier claims that pass remain verified individually.
- **REJECTED:** a claimed implication is false in its stated form. No assigned PR received this overall verdict.

# PR #20 — delayed-window Padé

## Verdict: VERIFIED WITH FIXES

### Verified claims

The following chain survived reconstruction:

```text
L-9407 stack partial-theta normal form
L-9408 finite-prefix transfer
L-9418 delayed-window Gaussian-binomial Padé family
T-9422 native irrationality for minimal eventual periods 1,...,9
R-9410 exact ceiling for the complete period-10 delayed equal-phase family
R-9409 completion-limit firewall and withdrawal of T-9418...T-9421
```

For `L-9418`, the exponent identity

```text
beta(k)+r*k*(k+1)/2 = k*(k-1)/2+r*M*k
```

produces the exact finite-product coefficient, the factor with `h=rt+j` gives the complete zero window, and the phase-zero term at `N=M+n` is uniquely minimal at `2`. The odd evaluated denominator and common rational-height clearing are consistent with the displayed exponent.

For `T-9422`, the uniform choice `M=37n/2` on even orders is legal for every `r<=9`. At `r=9`, the exact checks are

```text
shape = 297/281,
64^93 > 81^88,
88*297-93*281 = 3.
```

The product-formula argument with the nonzero integer `a*q_n-b*p_n` is valid, including the bounded-height alternative. The finite-prefix transfer has a nonzero rational coefficient and therefore preserves irrationality.

For `R-9410`, the discriminant calculation proves

```text
f_10(alpha)<263/250
```

for every real delay, and

```text
log_81(64)<19/20,
mu_10 < 4997/5000 < 1.
```

This closes only the one-denominator consecutive delayed equal-phase root-product architecture; it does not exclude combined moments, Hermite–Padé, multiple orthogonality, or irrationality at period ten.

### Code and artifact audit

`experiments/X-9413-delayed-window-pade/run.py` uses exact integer/Fraction and polynomial arithmetic for the theorem-level identities. Decimal evaluations are orientation only. Its frozen counts are consistent with the declared finite scope.

The script is an author-side regression/audit, not a separately written independent verifier. The theorem is the symbolic proof, not the finite replay.

### Required fixes

1. The PR body says `M>=D`; `L-9418` states and proves the family under `M>=D+1`. Make these identical. The current applications use a much larger delay, so this does not affect `T-9422`.
2. Label `X-9413` explicitly as an author-side exact regression, or add a separately implemented verifier before promoting the computational artifact as independently checked.
3. Keep the period-ten conclusion scoped to the complete delayed equal-phase family. It is a method closure, not a period-ten irrationality theorem.
4. Add this frozen-head review to the reviewer/status metadata without rewriting author history.

### Integration concern

PR #20 can be integrated independently of PR #34. Its period-ten open problem should cross-link, but not depend on, PR #34's combined-moment work.

# PR #32 — independent ADEL reconstruction

## Verdict: VERIFIED

PR #32 independently reconstructs the six-claim chain at source commit

```text
e5383d44cfa9fb75f7e92ff0bf031a2a6ca529a6
```

and its checker imports no author implementation.

### Verified claims

```text
L-9309 lift-digit cylinder bijection
T-9307 low-energy prefix entropy
T-9308 uniform harmonic tail
L-9310 completion-height carry rigidity
T-9311 uniform subexponential cusp decay
T-9312 all-depth weighted EQ
```

The hypotheses, translated intervals, terminal shells, signed frequencies, exact moduli, and low/high split were reconstructed correctly. `reports/gpt56-review-9309-01/check_adel_chains.py` is an independent implementation rather than an import wrapper.

### Current-head compatibility

All six source blobs are byte-identical on the current PR #16 head

```text
87478352e65c7b816dfc8b3b30894b71fb50f662.
```

The frozen/current blob SHAs are:

```text
L-9309  60c3fe6b5b1ef65eb9e26d236cd6a41ef1f03ccb
T-9307  af1cab3f9ba3c21e0bdc3f40238ff0bde832056b
T-9308  412ad9d5f2c722b4a06f8233e988916cb0f52367
L-9310  acf0226a16f159193925e79519fbfb88104b4433
T-9311  7be2cb773ed96e101812074839662c752b2bb97b
T-9312  3465e16f063c844a73ad8d002de2355ff128f7c5
```

### Integration actions

1. Cherry-pick or replay the review matrix, independent checker, and status metadata onto the current PR #16 branch. Do not merge an old source snapshot over newer `T-9313+` files.
2. Preserve the exact frozen reviewed source SHA in the status record.
3. Apply the metadata corrections already identified by PR #32:
   - `L-9309` and `L-9310` are parallel starts, not a dependency edge;
   - `T-9307` should distinguish counting dependencies from Fourier/transfer-corollary dependencies.
4. Do not infer ordinary-integer exclusion from weighted EQ. `T-9312` is a statistical/Fourier theorem; the ordinary-section claims added later require separate review.

# PR #33 — corrected 256-stage exclusion

## Verdict: VERIFIED within the frozen architecture

### Frozen dependencies

The verified conclusion is conditional on the exact source interfaces frozen by the PR:

```text
PR #33 head: c9d62bce3e93f5785f72e4520bc576863d9379eb
PR #3 tower/stage interface: f274dfeee3c9c391c48e58d8b57cb9f1759236f8
Evertse 1984, Corollary 1
```

### Verified chain

```text
L-9702 canonical composite cap
L-9703 normalized stage offset
T-9703 stage-quotient exhaustion
L-9704 connector-free stage coordinate
T-9704 cap-chain height collapse
L-9705 signed quotient dichotomy
L-9706 Evertse-admissible primitive tuples
T-9705 full ordinary exclusion
```

The lossless composite cylinder preserves every intermediate divisibility condition. The signed quotient is forced to the permanent cap `Y=0` or permanent co-cap `Y=-1`. The cap and co-cap share the same endpoint-height estimate.

The connector-free identity gives 258 coordinates with exactly one positive coordinate. Therefore no nonempty proper subsum vanishes. Primitive normalization has gcd at most

```text
2^3*3^3 = 216.
```

The endpoint outside-`{2,3}` product satisfies

```text
6498/346819 < 1/50,
```

while the projective norm contains the `2^E/216` contribution. The strict exponent gap yields Evertse's fixed `(n,c,d,S)=(257,1,1/50,{2,3})` inequality. The projective tuples are pairwise distinct, contradicting Evertse finiteness.

The Evertse normalization, absence of a pairwise-coprimality assumption, primitive representatives, and norm convention are independently reconstructed in PR #34 `T-9828`. PR #44 also independently reconstructed the exact PR #33 chain and supplied a separately written `X-8702` verifier.

### Code and artifact audit

`experiments/X-9704-connector-free-power-sum/verify.py` independently rebuilds the connector-free constants and Evertse arithmetic rather than importing the derivation. PR #44's `X-8702` is a second independent exact interface audit. No expensive rerun was needed in this pass.

### Scope boundary

The theorem excludes every signed ordinary completion in the physically overlapping corrected 256-transition phase-`-34` class represented by the frozen interfaces. It does **not** cover adaptive linear-height schedules, cross-cycle transitions, or other architectures created later.

### Integration order

Merge or import the exact PR #3 source interfaces before PR #33, or preserve them as frozen external dependencies. PR #44's review metadata can follow. Do not detach `T-9705` from the source stage identities it audits.

# PR #34 — cross-direction and period-four forge

## Overall verdict: GAP/BLOCKED for monolithic pre-public integration

PR #34 contains substantial rigorous work, but it is not one uniformly verified merge unit. The following statuses must remain claim-specific.

## Verified claim subset

The following claims survived this review in their exact stated scopes:

```text
T-9828  source-qualified independent reconstruction of PR #33
T-9801  ordinary binary-chart itinerary complexity floor
L-9904  lossless compressed cycle summary, full divisibility-to-replay,
        primitive-root and rotation collapse
L-9906  commuting-block / cut-displacement collapse
L-9907  cycle circulant SNF and full-denominator lattice equivalence
L-9908  centered forced-tail lasso firewall
L-9910  centered sparse-defect identity and neutral-tail collapse
L-9911  bounded-run/Sturmian schedule complexity exclusion
L-9912  exact five-defect positive-cycle exclusion
L-9913  exact six-defect positive-cycle exclusion
L-9914  lossless cross-prime excess-path CRT compiler
L-9915  zero-tested additive one-counter periodic-output obstruction
```

For `L-9912` and `L-9913`, the checked-in programs generate all weak compositions, rotate a largest neutral gap to the terminal position, retain every high-letter placement, recompute both centered formulas, and keep a dormant exact replay path for any unexpected divisor hit. A small independent reimplementation in this review reproduced every printed finite-table row—candidate counts, maximum numerators, height-survivor counts, least circular remainders—and found zero divisor hits. The infinite ranges are removed symbolically before the finite tables.

### `L-9909` — VERIFIED WITH FIXES in the reviewed subclaims

The selected full prime-power silence family, the two-run closure obstruction, and the common-order alias obstruction through `ord_D(2)>A-k` survived algebraic reconstruction and the exact continued-fraction certificate.

The frozen file must add the exact Matveev citation and normalization. The later source audit `LIT-KTHM-0060` identifies Matveev 2000, Corollary 2.3. Its safe rational two-logarithm constant is smaller than the constant used by `L-9909`, so the finite cutoff is not invalidated. The source qualification must nevertheless be explicit before public promotion.

## Blocked or unverified load-bearing claims

### `L-9873` — GAP/BLOCKED

The arbitrary-order composite Hasse-jet descent relies on a period-product degree lemma that is only outlined. The checker through `Phi_m^3` does not prove the all-order statement. This is an explicit proof-completeness boundary and cannot be retroactively verified by later low-order experiments.

Before public integration, classify `L-9873` as `GAP/BLOCKED / CANDIDATE`, or move it to a clearly conjectural checkpoint. It must not appear in a verified period-four theorem chain.

### `L-9869` — not promoted in this pass

The two-jet theorem contains a long symbolic ledger. Its structural reduction and finite audits are coherent, but this pass did not independently reconstruct every jet identity line by line. Retain `PROPOSED` pending a separate symbolic review. Also remove the appendix's stale statement that the shared repository was not edited; the file is now committed.

### `L-9870`–`L-9872` and the remaining period-four ladder

No rejection was found, but these claims were not independently promoted here. Their exact low-jet scope must remain separate from the blocked all-order extension.

## Integration fixes

1. Do not merge PR #34 wholesale as a pre-public verified theorem packet.
2. Split a reviewed cycle/method-boundary bundle (`L-9904`, `L-9906`–`L-9915`, with dependencies and certificates) from the still-developing period-four Padé bundle.
3. Mark `L-9873` explicitly `GAP/BLOCKED` and preserve the finite-check/nonproof distinction.
4. Add the source-normalized Matveev citation to `L-9909` and record the later `LIT-KTHM-0060` audit.
5. Preserve branch-qualified/frozen dependencies. Same-session internal lanes are useful audits but are not external independent review.
6. The PR title/body should not imply that all 160 claims have one verification status.

# Cross-PR connections

These are review observations, not new theorem claims.

## 1. Period ten requires ratio-level bulk cancellation

PR #20 proves that moving a complete equal-phase zero window cannot cross exponent one at period ten. PR #34's combined-moment work independently obtains the zero window, first nonzero survivor, odd denominator, and Casoratian/nonproportionality structure, while its height analysis shows that removing the visible Vandermonde still leaves a cubic Schur bulk.

The combined conclusion is precise: another raw determinant or another phasewise delay is not the missing object. A period-ten advance must control a **reduced determinant ratio / orthogonal- or biorthogonal-polynomial coefficient** in which the universal cubic height cancels, and then prove exponent greater than one. This connection sharpens the open route but does not complete it.

## 2. Completion-height decay becomes decisive only after finite-dimensional algebraization

PR #32 and PR #33 both use a completion-height squeeze. PR #32 obtains all-depth weighted Fourier decay, but that does not exclude one exceptional ordinary point. PR #33 becomes an ordinary nonexistence theorem because every hypothetical cap/co-cap tail creates infinitely many distinct tuples in one fixed 258-dimensional algebraic equation to which Evertse applies.

The missing bridge in statistical programs is therefore not merely stronger decay; it is a fixed-dimensional algebraic relation that captures the exceptional ordinary path.

## 3. Full-denominator factorization is lossless, not automatically simpler

PR #34 `L-9907` identifies the circulant/SNF condition with the complete denominator, and `L-9914` gives a lossless prime-power path compiler. These do not weaken the cycle problem: every factor must supply a compatible local path, the paths must reconstruct one monotone excess word, and every prime power must annihilate its numerator. Proper-factor hits and word decoding alone are not cycle progress.

## 4. Independent convergence on PR #33 is unusually strong

The same frozen PR #33 theorem chain is reconstructed in PR #33 itself, PR #34 `T-9828`, PR #44, and the present review. This is the strongest cross-agent verification convergence among the four assigned PRs.

# SERIOUS RESOLUTION PATH

## None is present at these frozen heads

No reviewed PR currently supplies a serious path that, with only a small number of clearly weaker missing lemmas, resolves the full Collatz conjecture.

- PR #20 closes fixed eventual periods through nine and isolates a period-ten Padé barrier. Even an all-period periodic-tail theorem would not decide genuinely aperiodic ordinary trajectories.
- PR #32 proves a genuine all-depth weighted-EQ theorem, but it does not control the exceptional ordinary section.
- PR #33 completely closes one strict corrected-stage architecture, not all divergent-orbit architectures.
- PR #34 gives exact full-denominator reformulations and substantial cycle-family exclusions, but universal full-denominator nondivisibility remains the positive-cycle problem itself, and positive-cycle exclusion would still leave divergent counterexamples.

The nearest serious **local** paths are:

1. **Period-ten combined moments:** prove a block/multiple-orthogonal factorization or recurrence-coefficient ratio with reduced global height below the `2`-adic gain, then make the constants uniform as the period grows. This would close a stack-tail architecture, not Collatz globally.
2. **Positive-cycle denominator:** prove that every admissible nontrivial valuation word has at least one full prime-power factor of `2^A-3^k` that does not divide `C_w`, or construct a complete compatible factor tuple and replay it. The negative result eliminates all positive cycles only; the positive result produces a finite cycle candidate.
3. **Ordinary divergent paths:** still require an independent ordinary-extraction/all-time-domain theorem. None of PRs #20, #32, #33, or #34 supplies it beyond the strict PR #33 class.

# Final status boundary

No PR was merged. No public README was edited. No Collatz proof, counterexample, positive cycle, or divergent seed is claimed.

Earlier frozen claims that independently passed are marked verified above. Every repair, cross-connection, or suggested strengthening remains separate and cannot retroactively verify a blocked original claim.
