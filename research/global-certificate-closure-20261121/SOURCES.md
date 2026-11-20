# Frozen source audit and concurrent work

This pass began from main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
The initial review included PR146 at `fd991063721e9c157d318e40bb20131762f7d750`
and PR164 at `6fa6b429870a9cd53cde0fc77ad64a3c3956199f`. Both were
refreshed after additional commits. PR167--170 appeared during the pass
and were inspected before publication.

The [metadata snapshot](../../reports/2026-11-21-global-certificate-closure/source_metadata_snapshot.json)
records all 106 open PRs and all 23 returned closed PRs, including full
heads and update times. Open results were obtained in two pages of
100 and 6, checked for 106 distinct PR numbers. Newer commits on older
PRs were inspected; sorting by PR number alone would have missed them.
This is a metadata audit of the complete set at the recorded cutoff and
a substantive review of changed relevant work, not a claim that every
historical proof was re-reviewed. Publication verification freezes these
heads rather than silently extending review to later commits.

## Newly inspected heads

| Source | Full head | Work read and effect on this packet |
|---|---|---|
| PR146 | `66970775e4bdc945a68308e37a8eb028ebde42d2` | `FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`, `LEAST_FAILURE_SIEVE.md`, the new `FIVE_RETURN_IN_EVERY_CLASS.md`, and the changed-file comparison. Every progression can carry a prescribed five comparison, and finite shifted blocks can be prescribed. This does not reduce the original fixed input or settle its endpoints. |
| PR164 | `5a7c86c94a9e2a7a064c0c84faa697d00d1c4d1b` | The original continuation notes and the new `research/witness-global-closure-20261121` packet. Its direct-R rewrites and smaller-parameter bypasses are valid additions; its distinct least failure and remaining rank-two Mersenne family are retained. See the [late review](LATE_PR164_REVIEW.md). |
| PR165 | `78bdb31ccba608de3d089b751a0ab59a52007408` | Certificate-transfer intake, witness semantics, the explicit exceptional rank-four family, and the arithmetic-moment question. The imported Gemini material supplies candidate transformations and questions, not proof authority. Universal transfer and the required moving-residue bounds remain unproved. |
| PR166 | `5996b9f525ca50978bc34f423192c36a87765bf3` | `FIVE_CERTIFICATE_LADDER.md`, `LADDER_RENEWAL.md`, and the GRH/completion interfaces. The unbounded ladder and its inverse-fiber method are reused and credited. No GRH consequence is used in our elementary results. |
| PR167 | `e83cc8b35ad614c616df7c00318cc9645a174c34` | Homogeneous recognition, localization cancellation, expanded renewal and closing energy interfaces. Its complete recognizer subsumes our explicit dictionary. Its three four-input first-one rows are credited; its missing weighted column estimate and source qualifications remain explicit. |
| PR168 | `e4599b32e4b1a955ac9315d46782d4ad6a5db96c` | `FIVE_RETURN_LANGUAGE.md` and its domain, plus the overview of witness, conductor and stationary routes. Its weighted domain and ours are incomparable. See the [transport comparison](LATEST_TRANSPORT_COMPARISON.md); its coefficient is not applied to our union. |
| PR169 | `6cb9bfdc828f91576066b0e4a099d47d8144e915` | `C5_CERTIFIED_BYPASSES.md`, `FIVE_WORD_EXTENSION.md`, `FIXED_ENDPOINT_SUMMABILITY.md`, and its overview/completion statements. Its two c=5 descents and all-time fifth-denominator estimate have different scopes; neither supplies universal selection or the growing-endpoint moment. |
| PR170 | `656063d5efa0f5708356ab2563a4348d39bae013` | The new carry-four compiler and terminal-phase boundary, with the packet's result/validation summary. Its carry construction is an additional homogeneous family; its terminal-phase obstruction is broader than terminal-base 1 alone. Neither claims complete physical closure or an absolute remainder bound. |

The PR146 paths are relative to `research/upper-bit-mergers/`; PR166
to `research/grh-certificate-closure-20261120/`; PR167 to
`research/least-failure-closure-20261121/`; PR168 to
`research/closure-frontier-20261121/`; PR169 to
`research/certificate-renewal-20261121/`; and PR170 to
`research/global-forcing-20261121/`.

Canonical source links:

- [PR146](https://github.com/GettysburgResearch/collatz/tree/66970775e4bdc945a68308e37a8eb028ebde42d2/research/upper-bit-mergers).
- [PR164 direct-R packet](https://github.com/GettysburgResearch/collatz/tree/5a7c86c94a9e2a7a064c0c84faa697d00d1c4d1b/research/witness-global-closure-20261121).
- [PR165 intake](https://github.com/GettysburgResearch/collatz/tree/78bdb31ccba608de3d089b751a0ab59a52007408/research/certificate-transfer-intake-20261120).
- [PR166 ladder](https://github.com/GettysburgResearch/collatz/tree/5996b9f525ca50978bc34f423192c36a87765bf3/research/grh-certificate-closure-20261120).
- [PR167 transport and energy](https://github.com/GettysburgResearch/collatz/tree/e83cc8b35ad614c616df7c00318cc9645a174c34/research/least-failure-closure-20261121).
- [PR168 closure frontier](https://github.com/GettysburgResearch/collatz/tree/e4599b32e4b1a955ac9315d46782d4ad6a5db96c/research/closure-frontier-20261121).
- [PR169 certificates and moments](https://github.com/GettysburgResearch/collatz/tree/6cb9bfdc828f91576066b0e4a099d47d8144e915/research/certificate-renewal-20261121).
- [PR170 carry and phase](https://github.com/GettysburgResearch/collatz/tree/656063d5efa0f5708356ab2563a4348d39bae013/research/global-forcing-20261121).

## Proof dependencies, not replaced by later minima

| Source | Exact dependency |
|---|---|
| PR157 `64361ecca770092d6c8242dc6211e38818af2e50` | `research/global-closure-20261120/merger.md`, GCM-001/002, and `reports/2026-11-20-global-closure/merger-certificate.json`. The frozen certificate is copied byte-for-byte, SHA-256 `751523dd92445610a26302947a2f689aecc56a27eaf6fa1f9954eb2e59f5c7c1`. Its physical calls remain conditional. |
| PR163 `051237135a34ae7d4b973ee5fcf5da04ded6f0fc` | `REVERSE_CERTIFICATE_KERNEL.md`, K1--K3; `LEAST_FAILURE_HEIGHT.md`, H1--H2; `C3_SINGLE_RUN_CERTIFICATES.md`; and `MERSENNE_WITNESS_DEPTH.md`, under `research/deep-reverse-closure-20261120/`. The new proofs keep its same globally least binary antecedent X and constants. |
| PR164 `6fa6b429870a9cd53cde0fc77ad64a3c3956199f` | `research/witness-closure-512-2026-11-20/continuation-descent.md`, W512-060 and canonical P/Q levels. Used only for the explicitly unresolved 26-level resource exchange. |
| PR150 `ef4022fa5ae43dd943ecca0b7c84d69af624c5c9` | `research/pointwise-closure-20261120/LOCAL_CERTIFICATE_GRADE.md`, LC-1. The grade invariant predates NB3. |

The latest PR164 direct-R floor uses the minimum of failed implications
`27m in C =>9m in C`. Our binary P-type comparison needs
`27m in C =>54m+1 in C`. Proving 9m does not prove 54m+1, and a directed
Q implication cannot be reversed. Its unit constant 213597/23 is therefore
not a replacement for 2025217/23 at our minimum. Its new direct-R packet
retains the rank-two word `(5,88+162j)` and Mersenne exponent 89+162j.

## Later c=5 descents and the fixed-input issue

PR169 CB1--CB4 gives two paired equivalences with smaller eligible
parameters:

\[
k'=(16384k-6049)/59049,\qquad k'=(32768k-9911)/59049,
\]

on their specified integral classes inside k=14 modulo 32. In the hard
rank-five family these select exponents 7656401 or 4822049 modulo 9565938,
with combined relative density 2/59049. They are genuine least-failure
steps, using longer certificates at smaller height. They do not supply
a selector for every exponent. Our new q construction applies to the
entire original exponent family and leaves a different physical
obligation; neither statement supersedes the other.

PR146's every-progression theorem constructs a new x in a refined
progression, with x and 5x meeting supplied q and 5q. Its bound x<=Kq has a
potentially large pattern-dependent K. Its small-endpoint construction
chooses further higher bits. These facts do not show that the original
supplied q admits a cheaper return. Density of successful cylinders also
does not prove ordinary all-input termination.

## Arithmetic moments and physical defect energy

PR169 ES3 proves, for every fixed ordinary odd n,

\[
\sum_{q\ge0}\frac{J_q(n)^4}{U^q(n)^5}\le\frac{256}{175n^4}.
\]

Its telescoping potential includes hypothetical cycle visits and assumes
no convergence. Its later localization removes the region r_w<=q from
the stated averaged arithmetic target. The remaining estimate uses
denominator r_w^2, not r_w^5; dropping those three powers is not justified.
That arithmetic moment is also different from the source-height
five-defect energy in UF5. No uncontrolled change of index identifies
the two quantities.

The Gemini inputs were useful for sharpening these certificate and moment
questions. Their value lies in verifiable constructions and precise
remaining statements. An asserted full conclusion, a finite successful
replay, or a weaker summable moment is not substituted for the missing
universal proof. Our newly proved facts use no unverified model output
as an additional mathematical premise.
