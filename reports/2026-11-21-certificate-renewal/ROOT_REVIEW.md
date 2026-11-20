# Root mathematical reconstruction

This is an independent internal mathematical review, not formal verification or external referee acceptance. The source reading included the latest PR146 additions at `fd991063721e9c157d318e40bb20131762f7d750`, the complete PR153 occupancy proof, and the current PR164 and PR166 manuscripts. Source-qualified implications are not presented as newly rebuilt Lean proofs.

## Paired contractions: CB1–CB4

Reviewed manuscript SHA-256: `dc846bbce7fa74f1235cab5049a8ac7fd269bab666abde656c51c86c977cb258`.

Reviewed checker SHA-256: `0437e87b861c17423706eca4b994181460a108f173baef121112b2004fd4b805`.

**VERIFIED within the stated two progression domains.** I reconstructed the four-start affine equations, correction constants, exact valuation lifting, and certificate replacement argument. The common endpoints are `(81k+2)/16` and `(243k+14)/8`. The two Chinese-remainder classes give positive eligible child indices and strict numerical decrease for every nonnegative parameter. Each new source path contains ten more odd inputs, which is compatible with height induction and does not justify a rank induction.

The source correction identity `Cs=2Ct+3^15+2^S` gives the claimed pair, and the source endpoint after fourteen odd steps is `(P/2−1)/3`. The final rank-five specialization retains exponent `e−1`. The specified exponent classes lie in `119 mod162`, and their period is the full order `2·3^14` of 2 modulo `3^15`.

The updated note correctly credits the prior sieve's excluded subprogressions. Its new contribution is a concrete paired equivalence and complete supplied-certificate conversion without using the least-failure initial-interval constant. The two-class density is exactly `2/59049`; it is not a complete cover.

Both normal and optimized executions of the author checker were also run during this review. The separate reviewer reconstructs the paths using independent code in `review_c5_affine.py`; its record is preserved alongside this report.

## Five-word transport: FW1–FW5

Reviewed manuscript SHA-256: `1969be619e2fe2b42fd2cad65d0bc0a50eb0f2c008154a652dfdf4934ebb9461`.

Reviewed checker SHA-256: `7648405fc2446f3ac857e23e79bb9923fca7e8b919ca31185d4977c80e0c7232`.

**VERIFIED for the stated dictionary, language and renewal.** The full numerator congruence forces all successive inverse divisions to be integral; positivity and oddness then establish ordinary legality. The correction-decoding recursion is complete because its remaining correction is odd. The unbounded two-run extension follows by the displayed correction identity and induction, not by the finite extension fixtures.

The eight prefix families are disjoint, including different two-run lengths. Their binary cylinder masses and ternary-unit restriction give relative density `23/384`. The special small-source guards for rows C and H are needed when establishing `3q≤x`; the other rows have the direct inverse-height bounds stated in the proof. The compiler consumes the known finite source certificate and correctly distinguishes unresolved valid words from malformed words.

For the energy proof, endpoint one has zero five defect; every other odd ternary-unit endpoint is at least five. This validates the denominator bound using `C/5`. A partial ternary residue supplies a lower bound on the first inverse exponent, while the geometric sum retains the full actual exponent period. The extra source-unit digit is used only when available. In the two-run tail, integrality supplies the stated necessary congruence and the exponent period is at least `2·3^k`. Both infinite tails are upper bounded, including excluded or incompatible terms conservatively. The tiny-term branches use positive rational upper bounds and do not discard terms.

The residue tree covers every unit class by replacing each parent with its three disjoint children. Exact rational power enclosures and finite leaf inequalities give the claimed column coefficient. The finite-cutoff energy proof avoids subtraction of infinite quantities. Independent review of the coefficient proof and actual executions are recorded in `REVIEW_FIVE_WORD_EXTENSION.md`.

The latest sufficient omitted progression starts `(1,3,3,3,3,3,3)` and is not covered by any new row. The broader domain has a weaker contraction coefficient. No total five-closure or absolute complement-energy bound follows.

## Arithmetic moments

I reconstructed the ordinary primitive-source identity and the pinned simple-path occupancy proof before using the moment implications. Nonperiodicity ensures distinct integer states, a uniformly bounded multiplicative correction, and consequently the fixed-source lower bound on the all-source moment. Sorting a finite selection of orbit states proves the quantile and harmonic estimates. A cycle cannot be substituted into that argument.

The final manuscript and endpoint extension have separate independent review records at their exact hashes. The all-time endpoint telescope uses ordinary identities and positivity only, and remains valid on repeated cycles. It controls the fifth-denominator moment, not the unproved second-denominator moment. Finite numerical enclosures do not prove any of the new asymptotic closing criteria.

## Overall verdict

The new partial theorems survive these reconstructions within their specified domains. The full Collatz theorem remains unproved. No all-input certificate dispatcher, finite actual five-energy estimate, new moment closing estimate, or full positive-cycle exclusion is supplied by this packet.

## Exact formatting import

The endpoint manuscript was imported with one nonmathematical change: the trailing space after its display delimiter on line 51 was removed. The reviewed author hash is `cbd8e00d73c0da06a063e7334a96ab27145a58ffcc3bd56604a3c8370d8663bd`; the published hash is `8a5aac44693c4755dcf16287e0129b4918f3db1e204daee84fb35668db631c56`. A byte comparison verifies that these are the only differing bytes, recorded in `import-normalization.json`. The independently reviewed equations and proofs are identical. Root verifies this formatting-only import; the earlier reviews retain their original explicit hash boundaries.
