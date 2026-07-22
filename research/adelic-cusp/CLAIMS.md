# Claim ledger: adelic cusp Fourier packet

This is an isolated `93xx` namespace for issue #15. It is not a replacement for any canonical root ledger and does not renumber claims on unmerged branches.

The status/reviewer entries below incorporate two independent review passes:

- `gpt56-review-9309-01`, frozen at PR #16 commit `e5383d44cfa9fb75f7e92ff0bf031a2a6ca529a6`;
- `gpt56-review-9315-01`, frozen at PR #16 commit `900ba417c968d8a41bc56a30d3ccc941284d8ce2`.

| ID | Type | Status | Reviewer | Short title | Dependencies |
|---|---|---|---|---|---|
| `D-9301` | Definition/construction | `PROPOSED` | — | Stationary survivor measure on `Z_2` | elementary 2-adic convergence |
| `D-9302` | Definition/construction | `PROPOSED` | — | Adelic natural extension and integer section | `D-9301`; elementary quotient algebra |
| `D-9303` | Definition/construction | `PROPOSED` | — | Stationary triadic mirror measure | elementary 3-adic convergence and separation |
| `L-9301` | Lemma | `PROPOSED` | — | Moving-character survivor Fourier identity | `D-9301`; issue-#4 notation crosswalk |
| `L-9302` | Lemma | `PROPOSED` | — | Conditional weighted shell tail from frequency-block means | elementary interval decomposition |
| `L-9303` | Lemma | `PROPOSED` | — | Phase energy controls the survivor Fourier product | `L-9301`; elementary cosine inequality |
| `L-9304` | Lemma | `PROPOSED` | — | Exact 2–3 phase reciprocity and valuation shift | elementary modular arithmetic; LTE reproved locally |
| `L-9305` | Lemma | `PROPOSED` | — | Moving-character triadic Fourier identity | `D-9303` |
| `L-9306` | Lemma | `PROPOSED` | — | Full-group absolute moments factor exactly | `T-9304`; CRT; Parseval for `p=2` |
| `L-9307` | Lemma | `PROPOSED` | — | Global rational diagonal and bilateral phase stitching | `L-9301`, `L-9305`, `T-9304`; circle reciprocity |
| `L-9308` | Lemma | `PROPOSED` | — | Complex bilateral phase stitching | `L-9307`; local character conventions |
| `L-9309` | Lemma | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9309-01` | Lift-digit prefixes are residue classes modulo `81^L` | `L-9307`; elementary modular lifting |
| `L-9310` | Lemma | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9309-01` | Completion-height rigidity for integral phase carries | elementary modular lifting and height separation |
| `L-9311` | Lemma | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9315-01` | Repeated itinerary factors are orbit-difference zero-carry chains | exact ordinary tail recurrence/growth interface; integer divisibility |
| `L-9312` | Lemma | `PROPOSED` | — | Centered `81/64` orbits force a three-state four-phase `3/2` schedule | `T-9315`; residue arithmetic modulo `64` |
| `L-9313` | Lemma | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9315-01` | Every itinerary has one bounded error path; ordinary realization is cylinder stabilization | elementary affine recurrence; `T-9315` crosswalk |
| `L-9314` | Lemma | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9315-01` | Exact appended base-`M` digit of the nearest-integer cylinder | `L-9313`; finite affine iteration |
| `L-9315` | Lemma | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9315-01` | Bounded-distortion morphic images preserve efficient recurrence | `T-9316`; elementary word-length accounting |
| `L-9316` | Lemma | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9315-01` | Small sequential transducers preserve enough Thue--Morse recurrence | `T-9316`; finite-state synchronization |
| `T-9301` | Conditional theorem | `SUPERSEDED` | — | Conditional polynomial-window reduction | superseded by self-contained `T-9308` |
| `T-9302` | Conditional theorem | `SUPERSEDED` | — | Conditional density-one full EQ | superseded by unconditional `T-9309` |
| `T-9303` | Theorem | `PROPOSED` | — | Valuation-stratified fixed-frequency depth-period decay | `L-9304`; exact cosine-grid second moment |
| `T-9304` | Theorem | `PROPOSED` | — | Stationary two-place CRT Fourier factorization | `L-9301`, `L-9305`; CRT |
| `T-9305` | Theorem | `PROPOSED` | — | Split collapse and weighted discrepancy equivalence | `L-9307`; cosine Lipschitz and product telescoping |
| `T-9306` | Theorem | `PROPOSED` | — | Complex coefficient and bounded test-sequence equivalence | `L-9308`; complex-mask Lipschitz and telescoping |
| `T-9307` | Theorem | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9309-01` | Low-energy lift prefixes have an explicit entropy deficit | count: `L-9309`; Fourier clause: `L-9305`, `L-9303`; survivor/CRT transfer: `T-9305`, `T-9306`; exponential moments |
| `T-9308` | Theorem | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9309-01` | Uniform harmonic high-frequency tail at every depth | `T-9307`, `T-9305`; geometric shell summation |
| `T-9309` | Theorem | `PROPOSED` | — | Unconditional full weighted EQ on density-one depths | `T-9303`, `T-9308`; valuation strata and Markov |
| `T-9310` | Theorem | `PROPOSED` | — | Weighted EQ converges in uniform density | `T-9303`, `T-9308`; translated-period Markov bounds |
| `T-9311` | Theorem | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9309-01` | Uniform pointwise cusp decay on every subexponential numerator window | `L-9310`, `L-9303`, `T-9305`, `L-9301` |
| `T-9312` | Theorem | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9309-01` | Complete weighted EQ at every depth | `T-9311`, `T-9308`; harmonic splitting |
| `T-9313` | Theorem | `PROPOSED` | — | Fixed-room equivalence and exact `C_j`/`R_j` minimum duality | `D-9302`, `D-9303`, `L-9301` |
| `T-9314` | Theorem | `PROPOSED` | — | Exact depth-46 minimum survivor; ordinary rooms exceed `2^227` | `T-9313`, `X-9303` |
| `T-9315` | Theorem | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9315-01` | Ordinary binary-chart orbits are exactly critical centered rational-power orbits | elementary nearest-integer arithmetic; exact `64 -> 81` recurrence crosswalk |
| `T-9316` | Theorem | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9315-01` | Efficient recurrence cone; Thue--Morse cylinder blocks do not stabilize | `L-9311`, exact `D-9302` growth interface, `L-9313`, `L-9314`, `T-9315` |
| `T-9317` | Conditional theorem | `INDEPENDENTLY_VERIFIED` | `gpt56-review-9315-01` | Exact threshold/equality bridge for Dubickas-type bounds | conditional implication from `T-9315`, `T-9316`, `L-9315`, `L-9316`; no source instantiation verified |
| `T-9318` | Theorem | `REFUTED` | `gpt56-review-9315-01` | Original unrestricted factor-complexity cylinder screen | `R-9304`; exact counterexamples `0^infinity`, `1^infinity` |
| `T-9319` | Theorem | `PROVED` | — | Correct nonconstant factor-complexity cylinder barrier | `T-9316`, `L-9313`, `T-9315`; pigeonhole |
| `R-9301` | Refutation | `PROPOSED` | — | Exact carry prefixes do not amplify to consecutive intervals | `L-9309` |
| `R-9302` | Refutation | `PROPOSED` | — | Matching repetition/carry criticalities do not contradict | `L-9310`, `L-9311` |
| `R-9303` | Refutation | `PROPOSED` | — | Pure real scheduled-cylinder emptiness cannot close the ordinary section | `L-9312`, `L-9313` |
| `R-9304` | Refutation | `PROVED` | — | Constant words refute the unrestricted `T-9318` screen | exact factor complexity and completion recurrence |
| `C-9301` | Historical conjecture | `SUPERSEDED` | — | Harmonic control of low-energy cylinders | superseded by `L-9310`, `T-9311`, `T-9312` |
| `Q-9301` | Open question | `IDEA` | — | Integer-section intersection | `D-9302`; issue-#4 M1 translation |
| `Q-9302` | Open question | `IDEA` | — | Fixed-room and active-cylinder nonstabilization | `D-9302`, `D-9303`, `L-9310`--`L-9316`, `T-9312`--`T-9317`, `T-9319` |
| `Q-9303` | Open question | `IDEA` | — | Centered nearest-integer cylinder nonstabilization and source specialization | `T-9315`--`T-9317`, `T-9319`, `L-9312`--`L-9316`, `R-9303`, `R-9304` |
| `O-9301` | Observation | `EMPIRICAL` | — | Bounded polynomial-window scattering census | `X-9301` |
| `O-9302` | Observation | `EMPIRICAL` | — | Bounded carry counts and zero-run census | `X-9302` |
| `O-9303` | Observation | `INTERNAL EXACT COMPUTATION` | — | Exact dual minima and survivor replays through depth 46 | `X-9303` |
| `O-9304` | Observation | `EMPIRICAL` | — | Exact finite-prefix centered reconstructions and phase schedules | `X-9304` |
| `O-9305` | Observation | `EMPIRICAL` | — | Exact finite Thue--Morse block and square replay | `X-9305` |
| `X-9301` | Experiment | `EMPIRICAL` | — | Exact cusp-scattering probe through depth 80 | standard-library exact modular arithmetic |
| `X-9302` | Experiment | `EMPIRICAL` | — | Exact completion-height carry audit through depth 80 | standard-library exact modular arithmetic and fractions |
| `X-9303` | Experiment | `INTERNAL EXACT COMPUTATION` | — | Meet-in-the-middle exact survivor-minimum certificate | exact modular subset sums and direct replay |
| `X-9304` | Experiment | `EMPIRICAL` | — | Exact centered-power reconstruction and four-phase replay | standard-library integers and fractions |
| `X-9305` | Experiment | `EMPIRICAL` | — | Exact Thue--Morse appended-block audit through index 1024 | standard-library exact integers |

## Status boundary after independent review

- `L-9309`, `L-9310`, `T-9307`, `T-9308`, `T-9311`, and `T-9312` were independently reconstructed by `gpt56-review-9309-01`.
- `L-9311`, `T-9315`, `L-9313`, `L-9314`, `T-9316`, `L-9315`, `L-9316`, and the conditional implication `T-9317` were independently reconstructed by `gpt56-review-9315-01`.
- `T-9318` is `REFUTED` as written. The constant words `0^infinity` and `1^infinity` have complexity slope zero and `q_K=0` for every `K`, contradicting its unrestricted screening clause.
- `R-9304` preserves the exact counterexamples and first invalid inference.
- `T-9319` is the separately numbered repair: the complexity nonstabilization screen requires the word to be nonconstant.
- The finite and asymptotic complexity lower bounds for an already nontrivial ordinary itinerary remain valid.
- `T-9317` remains conditional on an exact external theorem and equality-language classification; no Dubickas source is instantiated by either review.
- `T-9313`, `T-9314`, `X-9303`, and all issue-#4 downstream ordinary-room/counting consequences remain unreviewed here.
- No positive integer survivor, divergent orbit, cycle, universal Collatz-counterexample bound, or Collatz resolution is claimed.

## Corrected implication graphs

The Fourier/EQ chains are parallel until their final assembly:

```text
L-9309 -> T-9307 -> T-9308 --+
                              +-> T-9312 all-depth weighted EQ
L-9310 -> T-9311 ------------+
```

`L-9309 -> L-9310` is a recommended review order, not a logical dependency.

The reviewed ordinary-section chain is:

```text
exact ordinary recurrence/growth
  -> L-9311 orbit-difference zero carries
  -> T-9316 recurrence cone

T-9315 centered rational-power equivalence
  -> L-9313 full real shift + nearest-integer cylinder
  -> L-9314 exact appended block

T-9316
  -> L-9315 morphic recodings
  -> L-9316 finite-state recodings

T-9316 + L-9313 + T-9315
  -> T-9319 corrected nonconstant complexity screen

T-9316 + L-9315 + L-9316
  -> T-9317 conditional threshold/equality source bridge
```

The false route

```text
T-9318: low complexity alone -> nonstabilization for every binary word
```

must not be used.

## Generalization and literature crosswalk

`L-9313`, `L-9314`, and `T-9315` are stated for every coprime expanding pair `M<N`. `L-9311`, `T-9316`, and `T-9319` specialize to the ordinary `64 -> 81` section.

For an externally sourced equality language, screen in this order:

1. explicit efficient repeated factors -> `T-9316`;
2. bounded-distortion morphic presentation -> `L-9315`;
3. small deterministic sequential presentation -> `L-9316`;
4. certified factor-complexity slope below `1/log_64(81/64)` **and nonconstancy** -> `T-9319`.

No source formula, endpoint convention, or equality classification is inferred from an abstract.

## Branch crosswalk

- issue-#4 `C_j` recursion = reductions of `D-9303`;
- issue-#4 finite Cantor product = `L-9305`;
- exact CRT transform of `R_n x C_j` = `T-9304`;
- verified carry and entropy chains assemble into all-depth EQ = `T-9312`;
- one ordinary itinerary has one fixed room across every past/future split = `T-9313` (`PROPOSED`);
- finite Cantor minima transform into finite survivor minima = `T-9313` (`PROPOSED`);
- ordinary-section points are positive critical centered `81/64` orbits = verified `T-9315`;
- every itinerary has a real error lift but selects one nearest-integer completion cylinder = verified `L-9313`;
- the appended cylinder block is explicit = verified `L-9314`;
- efficient repeated factors obstruct nontrivial ordinary stabilization = verified `T-9316`;
- bounded-distortion morphic and small finite-state recodings remain obstructed = verified `L-9315`, `L-9316`;
- the corrected nonconstant factor-complexity barrier is `T-9319`;
- `R-9304` records why the former `T-9318` screen is false;
- the conditional source trichotomy is verified `T-9317`, with source acquisition still open;
- `Q-9302` and `Q-9303` target monotone minimum divergence and all-itinerary nonstabilization.
