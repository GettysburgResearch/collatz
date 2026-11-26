# Current source comparison and literature interfaces

The intake fixes PR197 at `10d87fee615d1095990d6b7ea329126b4cf7aa5a` and reads the first forty open PRs ordered by most recent update. That is metadata coverage. The substantive comparisons below concern the named paths at their exact commits. Neither later heads nor all files in those branches inherit these verdicts. Machine-readable pins are in the scientific packet's `SOURCES.json` and `TOWER_SOURCES.json`.

## PR193: a global Fourier criterion with an open norm estimate

At `aa0b01234735683b413098b81afdf764de503730`, [global/README.md](https://github.com/GettysburgResearch/collatz/blob/aa0b01234735683b413098b81afdf764de503730/research/astra-closure-20261125/global/README.md) uses the actual nonconvergence indicator b, with b(0)=0 and the exact identities b(2n)=b(n), b(2n+1)=b(3n+2). Its symmetric Fejer sums are

    K_N(t) = sum_{|k|<N} (1-|k|/N) b(|k|) exp(2 pi i k t).

The proposed closing condition is a bounded subsequence of their L1 norms, equivalently a finite complex measure with these Fourier coefficients. Weak compactness gives the measure; the idempotent theorem then places the indicator in the coset ring of the integers. Such a set is eventually periodic. The exact ordinary branch identities force an eventually periodic basin coloring to be constant on the positive integers. I inspected [PeriodicColor.lean](https://github.com/GettysburgResearch/collatz/blob/aa0b01234735683b413098b81afdf764de503730/research/astra-closure-20261125/global/PeriodicColor.lean), including its removal of the eventual threshold and period factors. This is a source inspection, not an additional root Lean build of that upstream file.

The literature input has the correct form: Green and Sanders describe the Cohen–Helson–Rudin idempotent theorem for finite complex measures and give a quantitative bound for the number of cosets in terms of the measure norm. [Primary published abstract](https://annals.math.princeton.edu/2008/168-3/p09). Its hypothesis is precisely what remains to be established for the actual Collatz indicator; the theorem does not supply the measure or the norm bound.

For the dyadic refinement, put A_N(t)=K_N(2t) and H_N=K_{2N}-A_N. The even Fourier modes give the same A_N at t and t+1/2; H_N changes sign. Since both are real,

    ||K_{2N}||_1 - ||K_N||_1 = integral (|H_N|-|A_N|)_+.

The resulting overshoot is nonnegative. Summability of these actual overshoots would finish this route. The available finite-absorption ceiling still grows with N, and PR193 gives a one-branch-error control showing why that ceiling alone cannot imply boundedness. A quantitative idempotent theorem only becomes applicable after the missing uniform bound; it does not reverse this implication. The Berg–Meinardus functional-equation approach is relevant context, but the supplied identity mixes the binary and ternary arguments. It is not a pair of independent pure Mahler equations. [Primary publication record](https://www.math.uni-rostock.de/math/pub/romako/heft48/berg2.html).

**Verdict:** a precisely stated source-qualified analytic route; no norm or overshoot estimate closing it was found in this pass. No upstream analytic theorem is a dependency of the new Lean modules.

## PR201: polynomial-width bands retain the original ordinary gate

At `02fb390a76fb2ffb00fee612649ca23a82d99d31`, [thin-band/README.md](https://github.com/GettysburgResearch/collatz/blob/02fb390a76fb2ffb00fee612649ca23a82d99d31/research/killed-green-head-closure-20261124/thin-band/README.md) fixes a hypothetical bad unit a and its actual suffix to q_i. The lower construction puts many sources in bands centered at a 2^S/3^k, with k logarithmic in the balanced-row parameter b and additive width at most 2^(8k). It retains a single ordinary gate, a common clock and the relative carry from its actual suffix.

I reconstructed the displayed two-gap router, the cancellation of the long padding clock from the real width, and the point at which the existing finite simple-path estimate is used. The unconditional construction and its cofinal finite-test equivalence remain qualified by their named earlier elementary inputs. The source itself labels its new Lean file an uncompiled candidate; it was not imported into our proof build. The stronger linear-depth and block-count claims assume F and S separately, and the source says the primary manuscript for F was not retrieved. We do not promote F to an unconditional input.

The lower population is polynomial in b while its center has exponential size. It neither contradicts the known absorption ceiling nor establishes the Fourier bound above. A missing exclusion of these actual bands remains an actual mathematical obligation. The interaction of all the mixed cells in a supplied band is a promising further target, but counting existence alone does not provide a negative answer to the finite test.

**Verdict:** source-qualified constructive input; the global absence of the finite test is OPEN. No new upper bound is asserted.

## PR210: the Subspace Theorem needs one fixed limiting coordinate

At `592328fecf8ea2cf41736294856d95f890a1ba98`, [SUBSPACE.md](https://github.com/GettysburgResearch/collatz/blob/592328fecf8ea2cf41736294856d95f890a1ba98/research/critical-record-rational-rigidity-20261125/SUBSPACE.md) studies one infinite critical backwards script and its ternary coordinate. Its proposed three-place argument retains the two clock monomials and the unreduced numerator. An increasingly repeated prefix gives approximation to that one coordinate; under algebraicity, fixed linear forms and a controlled height exponent, the cited p-adic Subspace Theorem forces a rational relation. The source explicitly does not derive repeated prefixes, algebraicity or balanced clocks from the existence of a divergent ordinary orbit.

Our checkpoint units U and V are finite rational integers at the supplied ordinary source. Their shared power base gives no sequence of approximants to an algebraic critical-record limit with those hypotheses. The new all-earlier criterion instead uses an elementary small-error versus ternary-divisibility comparison, with exact physical carries. We checked that this argument does not silently assume the Subspace Theorem's missing hypotheses. We have not independently verified all of PR210's separate rationality-to-periodicity argument.

**Verdict:** the proposed source theorem has a relevant fixed-coordinate interface, but its application to a universal checkpoint rescue is BLOCKED. It is not a Lean dependency or a completed Collatz proof.

## PR192, PR195 and PR206: ordinary comparisons and clocks

The center reviewer read PR192 at `1f1d3d690d7517e1b2a44b5f2f4930bd45b63302`, specifically `cycle/README.md`, `transport/README.md` and `FINAL_PROPOSAL.md` under `research/astra-diagonal-closure-20261125/`. The root re-fetched and pinned those exact blobs. The inverse optimum retains bounded-cycle hypotheses; the supplied-hit surplus retains the actual upper certificate. Neither is an all-parameter smaller-query selector. Our new pump proves its actual positive lower and upper paths directly.

The tower lane reviews PR195's round12 arithmetic at `99a4ab3f808c01acd115ef08eee42a8b886d5d4c` and PR206's merger and rotation files at `45a6a111321f947a8482c9e96e898435b57cee09`. Finiteness of compensated common-clock merger classes concerns a finer relation than basin membership. A finite such class can lie inside an infinite basin. PR206's 513 vertices begin at a selected shifted rank; its supplied decrease is relative to that shifted value. The new lower-cone theorem proves the explicit clock restriction on using that endpoint to reach any smaller base. The new exact-deadline construction shows directly on the fixed tower based at 17 that arbitrarily delayed finite disjointness can coexist with subsequent genuine mergers. See [the mathematical packet](../../../research/ayh-resource-reset-20261124/unbounded-queries/FIXED_TOWER.md) and [independent review](INDEPENDENT_FIXED_TOWER_REVIEW.md).

## Continuing the Yolcu–Aaronson–Heule direction

The original mixed-base string system represents Collatz as termination; the published work obtains automated proofs of weakenings using matrix interpretations. [Yolcu, Aaronson and Heule, 2023](https://doi.org/10.1007/s10817-022-09658-8). The present addition works with physically realizable paired words and rational periodic centers. It obtains decreasing ordinary queries with unbounded word and denominator depth, and an exact carry language deciding a broader class of earlier-orbit comparisons. This is a semantic extension of the termination strategy. It does not produce an interpretation orienting all original rules or prove universal termination.

The first unsupported global step remains a source-specific successful selector or a sufficient ordinary descent for every surviving least reverse defect. The new finite carry decision is a decision of membership, not a theorem that membership occurs. The new unbounded family is cofinal in parameter height at each depth, not a cover of every parameter.
