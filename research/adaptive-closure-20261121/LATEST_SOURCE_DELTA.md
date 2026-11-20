# Source delta after the final PR167--169 refresh

**Status: scoped comparison, not a full-proof claim.**
The initial V1--V4 draft was produced from PR146, PR164--166. During
final review, newer independent packets were found. Their contents were
read at exact heads before retaining any novelty claim.

| Refreshed source | Full SHA | Inspected scientific paths |
| --- | --- | --- |
| PR167 | `e83cc8b35ad614c616df7c00318cc9645a174c34` | `research/least-failure-closure-20261121/EXPANDED_FIVE_RENEWAL.md`, ER1--ER4 |
| PR168 | `e4599b32e4b1a955ac9315d46782d4ad6a5db96c` | `research/closure-frontier-20261121/FIVE_RETURN_LANGUAGE.md`, FR1--FR5; `CLOSING_ATTEMPTS.md` |
| PR169 | `6cb9bfdc828f91576066b0e4a099d47d8144e915` | `research/certificate-renewal-20261121/FIVE_WORD_EXTENSION.md`, FW1--FW5; `FULL_THEOREM_ATTEMPT.md` |

## What overlaps

V1's block `(1,1,1,b>=6)` to `(1,2,5,b-5)`, its source cylinder
`271 mod512`, and its ordinary legality are already in all three
refreshed packets. PR168 FR2 also supplies the same complete first-hit
family with final exponent `28 mod54`. V1 is an independent reconstruction.

V2's A+B compiler and its arbitrary block concatenations are contained
in the broader PR168 balanced-word recognizer and in the PR169 compiler.
No enlarged successful language relative to those heads is claimed.

V3 independently proves a two-endpoint-class bound on the smaller A+B
domain. It needs no residue enumeration beyond the split `q=7 mod27`
versus its complement. Its coefficient is `405749/424576` and cutoff
`X/6`. The refreshed packets give these stronger or broader results:

| Source | Relative source density | 21/25 coefficient | Endpoint cutoff |
| --- | ---: | ---: | ---: |
| V3, A+B only | `35/768` | `405749/424576` | `X/6` |
| PR167 ER3 | `85/1536` | `91/100` | `X/3` |
| PR168 FR4 | `18319/393216` | `903/1000` | `X/2` |
| PR169 FW5 | `23/384` | `249/250` | `X/3` |

The kernels differ, so none of the larger-domain rows should be ranked
only by its coefficient. V3's benefit is a short analytic cross-check
and a stronger cutoff on its own smaller domain. It is not improved
coverage, an improved best contraction coefficient, or an absolute
bound for ordinary defect energy.

## Retained residual and boundary extensions

V4 gives a specific first-valuation-one, rank-two residual:

\[
z_k=(2^{6k+5}-5)/9,\qquad
T^{6k+8}(5z_k)=5(3^{4k+2}-1)/8.
\]

The source first-hit odd count is two, while every terminating target
certificate must have at least `4k+5` odd inputs. This explicit residual
and lower bound were not found in the inspected refreshed proofs or
their closing-attempt ledgers. The older general obstruction to a bound
depending only on source rank remains credited to PR157; V4 is a scoped
extension on a particular first-letter-one family, not discovery of
that general obstruction.

V5 specializes the already available complete correction decoder to
`(1,3 repeated r times,b)`. The target correction starts at
`3^(r+2)+2^(3r+4)`; its first `r+1` forced division exponents are one,
and its final normalized correction is `3+2^(2r+3)>1`. Thus none of
these prefixes admits a balanced five return, regardless of b.
This explicit family exclusion was not found in the inspected main
proofs. The decoder itself is already PR168 FR1 and PR169 FW1.

Neither extension proves convergence of its residual family. In the
least-failure Mersenne setting, the proposed two-antecedent step is still
the unproved transfer `u,5u in C => 5u-2 in C` on the exact stated domain.
All-source energy finiteness and full certificate transfer remain open.

## Validation actually performed

The local `check_valuation_one_transport.py` was run normally and under
`-OO`; the two JSON reports were byte-identical. It checks 999 paired
B blocks, 65,536 binary-cylinder inputs, 1,998 endpoint-partition cases,
nine exact fractional-power comparisons reduced to integers, twenty
complete certificates, thirty-three V4 residuals, 129 V5 decoder
boundaries, 1,666 two-antecedent identities, ten rejected malformed
controls, and thirty-six valid unresolved controls.

These are finite ordinary and exact arithmetic checks. The unbounded
statements rely on the accompanying algebra and inverse-fiber proofs.
The source audit above is a claim-and-domain comparison, not a claim
that the entire PR167--169 repositories were executed or independently
reviewed in this pass.
