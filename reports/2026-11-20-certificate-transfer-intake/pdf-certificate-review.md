# Internal audit: certificate transfer, eligible classes, and exceptional inputs

Scope: uploaded eighteen-page manuscript `manuscript.txt`, updated ZIP `problem2.py`, and the exact PR146 sources at `e238c63a5d57f96bb063b7472498d1977df51951`. This audit did not modify either upload. The separate substantive proof is now in `collatz_intake_repo/research/certificate-transfer-intake-20261120/EXCEPTIONAL_FAMILY.md`.

## Main findings

1. The exponential certificate characterization (Lemma 1) is correct. The terminal identity enforces all intermediate divisions, and all intermediate values are positive odd. Nonminimal certificates append the two-halving odd loop at 1.
2. The exact eligible residues are correct: `x=128m+1`, `m>=1`, `4∤m` means `x mod512` belongs to `{129,257,385}`. These are the current PR146 reverse-basin criterion, not the older forward `16k+1 -> 32k+1` criterion.
3. The starting forms are correct: `T^7(x)=81m+2`, `T^6(y)=27m+1`, `y=(x+1)/2`. After reading `n` parameter bits, endpoint slopes are powers of three and the two branch parities are fresh fair bits under conditional Haar measure. This describes a residue-class distribution; it is not a randomization of one fixed ordinary integer.
4. The Lemma 2 suffix certificate transformation is correct, including when the common endpoint is even. The first `i-1` cumulative exponents on the target arm are fixed by the finite legal class prefix. Its `i`th odd iterate is obtained by finishing the remaining halvings from the common endpoint `N`. These extra `v2(N)` halvings can depend on the lift parameter, but they affect `A_i` and `B_i` equally, leaving `B_i=A_i-1`. No claim that `B_i` itself is class-fixed is needed.
5. The fixed prefix assertion can be justified concretely: when the aligned prefixes have already used `i` odd inputs, their first `i-1` complete odd-to-odd blocks have finished before their last odd input. All parities in these earlier blocks are determined by the coalescent cylinder. Only the final unfinished block can extend beyond the displayed common endpoint.
6. The compression is conditional on affine coalescence. Ordinary numerical merging alone is insufficient, and equal odd-index eventual values alone are also insufficient. The cumulative exponent difference must be exactly one.
7. The manuscript's `G` is exactly an all-lift affine-merger success set. Membership outside `G` does not mean that two ordinary orbits are unrelated. In particular the manuscript's own `129,65` example has convergent, intersecting numerical orbits. Its first common shortcut value is 20; 5 is its first common **odd/Syracuse** value. Clarify the map if retaining “first meet at 5.”

## Explicit eligible infinite exceptional family

The entire four-odd first-hit family from PR146 is outside the PDF's `G`:

`x_s=(2^(54s+8)-175)/81`, `s>=1`, with certificate `(0,2,4,6,54s+8)` and `x_s=257 mod512`.

Its partner `y_s=(x_s+1)/2` reaches `w_s=3^(27s)+1` at clock `54s+7` with `27s+4` odd inputs. The source grade is `K(x_s)=-54s`. If the partner converges, its grade is `K(y_s)=1+K(w_s)`. A lifted merger would require `K(y_s)=K(x_s)+1`, but `K(w_s)>=-log2(w_s)>-54s`. If the partner does not converge it cannot merge with the certified source either. Thus all `x_s` lie outside `G` unconditionally.

This is a synthesis of the source family's explicit paths and the prior phase bound, not a priority claim for either ingredient. It makes the paper's “infinite exceptional set” assertion concrete and shows that the exact first-layer handoff question is wholly outside its compression mechanism. It does not say other guarded repository methods cannot exclude the same inputs as least counterexamples.

## The example x=9

`x=9` is outside the requested domain and cannot refute the requested closure. Its partner is 5. Their shortest certificates are `(0,2,3,4,6,9,13)` and `(0,4)`; their iota values are 1 and 2. Thus `iota(x)=iota(y)+1` fails. Both ordinary orbits nevertheless meet at 5. This is a valid generic illustration that actual meeting does not imply the precise certificate-suffix shift. It is not a counterexample to Lemma 2, which assumes membership in `G`.

## One transfer versus two

The requested single transfer from `x_s` lands in the component of `3^(27s-1)`. The updated ZIP's section 4 makes the implication twice and obtains `z_s=(y_s+1)/2` in the component of `3^(27s-2)`. Both finite identifications are correct. Since `q_s=(2^(54s)-1)/81=3 mod4`, the intermediate `y_s=128q_s+1` is specifically `385 mod512`, so the second transfer is eligible. It remains conditional on establishing the first transfer's conclusion.

## Overclaims to correct

- Replace “the two orbits are unrelated” with the narrow absence of an all-lift affine merger certificate.
- Replace “no identity links the two orbits afterwards” with the same narrow statement. Actual ordinary meetings, adaptive maps, intervening comparison sources and different ranks have not been excluded.
- The sign or convergence of the integer exceptional set does not follow from Haar measure or a natural-density-one result.
- “Every step was checked numerically” is not a proof-validation claim for optional stopping, conditional expectations, or the all-source conclusion. The separate stochastic proof review must decide those steps mathematically.
- The negative example `-127,-63` witnesses failure of ordinary merger, since it reaches different negative cycles. It is not a counterexample to the literal implication `x in E => (x+1)/2 in E`: a negative `x` never belongs to the positive basin `E`, so that antecedent is false. The signed example illustrates the need to distinguish positive realization from the common 2-adic process, but should retain this logical qualification.
- The uploaded code's `w_certificate` is a partial routine. It constructs the entire known source certificate, then searches for the exact same-index and exponent-offset match with padding. Its finite search cap does not prove that an unaccepted input has no coalescent class; the phase invariant can certify that separately once both convergence certificates are known.

## Checks performed

Read the actual manuscript, `problem2.py`, `conv.c`, and the three pinned PR146 manuscripts. A short independent exact Python replay checked certificates/grades for 9, 5, 129, 65, 769, 385; confirmed that the first common shortcut value of 129 and65 is20; and checked the symbolic family certificates and checkpoint formulas for s=1 through5. Those finite checks corroborate the algebra and do not establish any missing all-input theorem.
