# Independent review of the stationary ternary information theorem

Date: 23 November 2026. Reviewer: the fixed-source-pressure lane,
independent of the author of `TERNARY_INFORMATION.md`.

Parent checkpoint: `cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`.

## 1. Source and verdict boundary

Reviewed source:
`research/closure-round5-20261123/TERNARY_INFORMATION.md`,
SHA256 `e254b24b199c94ac5832a095dc6c428eee2d8a6628dff05546bdc855287073f4`.

**VERIFIED as written mathematics for Sections 1--5:** an ergodic
stationary positive-gap process with finite mean at most `log_2 3`
has the stated exact ternary local dimension, residue entropy rate,
and sublinear conditional decoding entropy. No independence or mixing
hypothesis is required by the proof.

The direct ordinary-gap consequence retains the same source, endpoints
and stationary law, with its finite height-exponent and ergodicity
hypotheses explicit. The full final source was reread at this hash.
The infinite entropy and dimension theorem is not claimed as
kernel-checked. The external research papers cited for context are
not given a blanket independent-proof verdict by this review.

## 2. Hypotheses and finite entropy

The alphabet consists of positive integers. Finite mean gives finite
one-coordinate entropy by comparison with a positive geometric law;
block entropy is then at most the sum of the finite coordinate
entropies. Stationarity and ergodicity are exactly the hypotheses
needed for the almost-sure Shannon--McMillan--Breiman information rate
and for Birkhoff's gap average. The latter also uses the stated finite
mean. No regularity or independence of the gaps is hidden here.

The classical countable-alphabet information theorem used is Chung's
finite-entropy extension. Its precise hypothesis is also stated in
the introduction of Algoet--Cover's primary paper,
[*A sandwich proof of the Shannon--McMillan--Breiman theorem*](https://isl.stanford.edu/~cover/papers/paper83.pdf).
Chung's [authorized original reprint](https://celebratio.org/media/docs/MR0131782.pdf)
is separately available. This review checks that the named theorem's
hypotheses are supplied; it does not claim a new proof of that classical
ergodic theorem. The geometric comparison here is an entropy bound,
not a replacement of the actual process by independent geometric gaps.

## 3. Complete-carry ambiguity

I reconstructed the exact numerator and its clock orientation:

\[
 C_m=\sum_{i=1}^m3^{i-1}2^{A_m-A_i},\qquad
 Z\equiv C_m2^{-A_m}\pmod{3^m}.
\]

The inverse-coded gap word is reversed before it is read as a
chronological ordinary shortcut word. That word has total length
`A_m`, odd count `m`, and complete carry `C_m`. The earlier decoder
therefore proves uniqueness when all three coordinates are retained.
For instance, at depth two `C_2=2^(G_2)+3` determines `G_2`, and
`A_2` supplies the otherwise missing `G_1`. Dropping `A_m` would fail.

At fixed total clock and ternary residue, the numerator lies in one
residue class modulo `3^m`. Restricting `0<C_m/3^m<=Q` allows at
most `floor(Q)+1` values. Summing over at most `D+1` allowed clocks
gives the asserted fibre bound. This concerns words with their
original probabilities, including every carry term.

With `S_j=j log 3-A_j log 2=dj+o(j)` and `d>=0`, the identity

\[
 C_m/3^m=\frac13\sum_{i=1}^m e^{S_i-S_m}
\]

has the correct sign: `d(i-m)<=0`. The maximum of the sublinear
prefix errors through `m` is itself `o(m)`, so the complete carry
quotient is at most exponential in `o(m)`. Also `A_m=O(m)`.
This proves subexponential typical fibre size while retaining both
the binary clock and carry quotient. It is not a uniform bound over
all words.

## 4. Restriction and the original measure

The increasing sets `E_N` combine the eventual clock/carry bounds
with the eventual Shannon--McMillan--Breiman upper bound on prefix
probabilities. Their union has full process measure. For each
unnormalized pushforward restriction `nu_N<=mu`, the finite fibre
count gives the displayed uniform depth-`m` ball bound for `m>=N`.

The proof correctly avoids transferring this bound in the wrong
direction merely from `nu_N<=mu`. On residue partitions, the ball
mass ratio is the conditional expectation of `dnu_N/dmu`. The
increasing finite partitions generate the ternary Borel sigma-field,
so martingale convergence gives that density almost everywhere.
Because the restrictions increase to the full measure, their densities
increase to one after choosing compatible versions. Almost every
point therefore has positive limiting density for some restriction.
At such a point its original `mu`-ball mass is bounded by a fixed
multiple of the restricted ball mass for all sufficiently fine depths.

That supplies the lower local dimension for the original measure.
Taking a countable sequence of decreasing tolerances retains a common
full-measure set. Neither exponential exceptional-set tails nor an
unproved interchange of limit orders is needed for this local result.

## 5. Upper dimension and entropy identities

All continuations of a gap prefix belong to its depth-`m` ternary
ball: every omitted series term is divisible by `3^m`. The original
ball mass is therefore at least the prefix probability. The same
information theorem gives the matching upper local dimension.

For finite-depth Shannon entropy, the residue is a deterministic
function of the gap word, yielding the upper entropy-rate bound.
The normalized ball information is nonnegative and has the established
pointwise limit. Fatou's lemma yields the matching lower liminf of its
expectation. Subtracting the two finite block entropies then gives
the claimed `o(m)` conditional entropy. This last passage needs no
uniform integrability assumption beyond the already supplied finite
word entropies and the separate data-processing upper bound.

## 6. Direct same-source consumer

The final Section 5 uses the original backward odd-gap law directly.
Its dependency is Theorem 3 of `FIXED_SOURCE_PRESSURE.md`, SHA256
`09b9cb3a1bd7daf1bc77b70e5010c8591b3d1fa7965e59a63dff6efc1dbe5c76`,
independently reconstructed by the cycle lane in
`ENTROPY_CYCLE_REVIEW.md`, SHA256
`ead2c1a8aeeebf2d0878402e49684f155d6082620bd5df0d32ca08a61d92f93b`.

I checked the composition, rather than describing the dependency's
author review as independent. A further subsequence realizing the finite
height liminf retains exactly the chosen fixed-block gap limit. Replacing
`log H` by `log(H+1)` does not change that exponent. The direct theorem
gives `h(eta)>=a log 2/beta` with `1<=a<=ell`, including possible
loss of the first gap moment under weak convergence.

The same reversed word gives the ordinary endpoint identity

\[
 2^{A_m}q_j=3^m q_{j-m}+C_m.
\]

Modulo `3^m`, this identifies the actual endpoint law with the coded
law at every fixed depth, after discarding at most the initial `m`
endpoints. The function from a fixed gap word to its finite residue is
bounded and continuous on the discrete word space. Its law therefore
passes under the fixed-depth weak convergence. No growing-resolution
exchange and no return-map identification between different empirical
laws is needed.

The exact dimension formula now gives `d>=a/(ell beta)>0`. The
stronger critical expression `d>=1/beta` is asserted only if `a=ell`.
The necessary height bound using the geometric maximum one-letter
entropy at mean `a` follows with the correct clock normalization.
The endpoint `a=1` forces all gaps to equal one and entropy zero,
contradicting finite `beta`; the displayed positive denominator is
therefore justified. Ergodicity and finite height exponent remain
hypotheses, not consequences of hypothetical escape.

## 7. Remaining pressure boundary

Exact dimension and the Shannon entropy identity do not give a
Renyi-2 upper bound. The restrictions have no rate for their omitted
mass, which can dominate the square sum. A biased Bernoulli measure
already separates its Shannon and Renyi-2 dimensions; no Collatz
specific independence model is being imported by that control.

The theorem therefore removes a projection-entropy ambiguity in its
stated ergodic drift range. It does not prove polynomial height,
ergodicity of an actual limiting law, critical mean without an
additional argument, or the same-source collision decay needed to
close the existing pressure contradiction. The known source weights,
diagonal mass and the order of the time and precision limits remain
unchanged.

## 8. Independent evidence and author boundaries

This reviewer authored `FIXED_SOURCE_PRESSURE.md`; its independent
mathematical review is instead the cycle lane's
[`ENTROPY_CYCLE_REVIEW.md`](ENTROPY_CYCLE_REVIEW.md).
No self-review of that dependency is described as independent here.
The present reconstruction is of the root-authored ternary coding
theorem, with its classical ergodic inputs stated explicitly.

No new executable test or fresh Lean compile is claimed by this
review. Root integration has its own complete replay receipt.

## 9. Separate source review of the exact finite replay

Reviewed checker: `research/closure-round5-20261123/exact_replay.py`,
SHA256 `6c14e08098142e1106db99cbe2cf3bcda3e56133ad13788da8c9f770a28c035b`.

**VERIFIED by source reconstruction:** `source_pressure_checks()` and
the integration wrapper implement their stated bounded arithmetic
controls. This is a source review, not an execution receipt. The
imported rational and carry/cycle checkers have their own author and
review boundaries; this paragraph does not claim their execution.

The chronological `forward_carry` recurrence was checked directly:
an odd step changes the complete numerator from `C` to `3*C+2^clock`,
while an even shortcut step leaves it unchanged. The odd count is
incremented only on the odd branch. This is the full affine numerator
for the actual bit word. The convergent fixtures are stopped at their
first ordinary one, and explicit runtime guards retain distinctness
of every sampled state and the finite cap.

The source-word tests retain their original ordinary values. Their
residue congruence, bound `floor(H/2^m)+1`, and long-word image and
collision counts use exactly `N-m+1` sampled starts. The collision
comparison checks the numerator of the uniform word collision; it is
not a ternary endpoint collision claim.

The odd-gap fixture is extracted from the same literal shortcut path.
For each actual endpoint, its gap word is reversed before computing
`C=sum_i 3^i 2^(A-prefix_i)`. This gives the full numerator in
`2^A*q_endpoint=3^m*q_source+C`, with the correct original source
`m` odd steps earlier. The modular inverse of `2^A` exists modulo
`3^m`, and the tested endpoint residue is consequently the correct
one. Good-word uniqueness compares the full binary modulus `2^A`
to the actual maximum odd height.

For the finite truncated-window inequality, all arithmetic uses
integers and `Fraction`. The fixtures use center `3/2`, truncations
`1,2,5`, and the explicitly selected positive lengths. The deviation
means have respectively `M-m+1` and `M-K+1` terms. The right side
retains the exact ratio `(M-K+1)/(M-m+1)` and boundary allowance
`R*(K-1)/m`. Reversing each gap window leaves its truncated average
unchanged, so these forward index slices test the same inequality
as the backward-word statement. This verifies the finite formula's
normalization, not growing-window convergence or ergodicity.

The wrapper hashes its selected round-five Python, Lean and named
mathematical source files at entry to `main`, and re-reads the same
selected paths after every checker returns. A changed byte causes
an exception before a success JSON object is printed. The guard uses
`require`, so optimization does not remove it. The digest map is a
binding to those selected file bytes, not a full-checkout identity;
the selection and initial snapshot occur after Python imports. The
root's replay therefore correctly requires the source files and
imported checkers to be complete and frozen before execution. No
additional optional test was run by this reviewer.
