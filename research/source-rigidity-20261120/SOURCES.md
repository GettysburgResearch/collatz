# Frozen sources, overlap, and dependency boundaries

The branch starts from `main` commit
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, tree
`1c25c17df24491de6187445f1a1d355d5a7660c3`. The latest-source check in
this pass observed the concurrent PR146 and PR157 heads below. These are
source identities, not wholesale review verdicts on those branches.

## Repository sources

| Source | Frozen full commit | Material used and limitation |
| --- | --- | --- |
| [PR145](https://github.com/GettysburgResearch/collatz/pull/145) | `dd245a712f985909f541590e3f6c179b7ba011e4` | `research/pointwise-run-defects/COMPRESSED_DESCENT.md`, final growing-number-of-powered-pieces consequence. Used only for the separately SOURCE-QUALIFIED stronger growth statement. Its proposed, ineffective Subspace-Theorem input is not independently proved here. |
| [PR146](https://github.com/GettysburgResearch/collatz/pull/146), earlier frozen source | `6863d298187af8b2619efbf78cc4b0aa8e627393` | `research/upper-bit-mergers/` variation/three-ray upper estimates, carry comparisons and neighboring basin criteria cited at their exact paths in the proofs. |
| PR146, latest inspected head | `e238c63a5d57f96bb063b7472498d1977df51951` | `DEEP_REVERSE_BASIN.md`, `BOUNDED_RANK_TRANSFER.md`, and `RANK_THREE_MERSENNE.md` in that directory. Credits the newer reverse-basin and bounded-rank/Mersenne results. The earlier analytic source files are unchanged. No external Lean run from that PR is claimed as an execution here. |
| [PR151](https://github.com/GettysburgResearch/collatz/pull/151) | `02a9f6ad17e5f1904cb4ff806fd0217d199e8437` | Single-index/thin-strip comparison context, as qualified in `SINGLE_LAYER_FIVE.md`. |
| [PR152](https://github.com/GettysburgResearch/collatz/pull/152) | `2391a9c1e4a7f77233b951d2eb6da92e76652e7c` | Actual unsafe transport and its source/domain boundary. No drift theorem for a fresh shell is transferred to an evolved source. |
| [PR153](https://github.com/GettysburgResearch/collatz/pull/153) | `eb04a5d79020cefa0ba46794095b5766c5ff66a4` | Prior adaptive `25 mod 64` coverage and finite-core context. No rediscovered overlap is presented as new coverage. |
| [PR154](https://github.com/GettysburgResearch/collatz/pull/154) | `fe40bb6f88e8094290ef01207d9bf7c4798d35d0` | `research/structural-reset-20261120/adelic/PRIME_HEIGHT_ESCAPE.md` and its closing ledger; prime height there concerns `n`, while the new core theorem concerns `n+1`. Also the earlier restricted five-ray criterion. |
| [PR155](https://github.com/GettysburgResearch/collatz/pull/155) | `92f499b9d340d1ff8cc643c3eef3477d61b477c1` | Ordinary Dirichlet coercivity below exponent one and the centered harmonic endpoint estimate. New countermodels preserve the exact hypotheses they satisfy and identify the odd-branch hypothesis they fail. |
| [PR156](https://github.com/GettysburgResearch/collatz/pull/156) | `c5cb84502c7289705d59a8781a65fd845b9b6b14` | `research/global-rigidity-20261120/SHIFTED_LINEARIZATION.md`, `FIXED_SOURCE_CLOSURE.md`, prior derivative-space operators and the Q-section certificate. The new harmonic operators live in a different space. Unknown algebraicity and a required power saving remain open. |
| [PR157](https://github.com/GettysburgResearch/collatz/pull/157) | `64361ecca770092d6c8242dc6211e38818af2e50` | `research/global-closure-20261120/merger.md`, `transport.md`, `arithmetic.md`, and `closing-attempts.md`. The one-way forward-five reduction already supersedes the global strength of our compact symmetric certificate. Its particular positive-occupation target remains open and is not refuted by our approximate invariants. |

Exact source paths and claim IDs at the points of use take precedence over
this route-level index. Source inspection and a new mathematical application
do not constitute an external formal build, complete corpus replay or
independent proof of every result on a source branch.

## Concurrent packets found in the final check

The final snapshot also found PR158 at
`cf49a68bf93e98c97a18dc3d1a4186faf534e422`, PR159 at
`0e7d2841b1591073c6399f91f3b6944ebcdbdbd5`, and PR160 at
`6d877e718f5ef9d57fe1830912c444359718747a`.
[LATEST_COMPARISON.md](LATEST_COMPARISON.md) records the exact paths read,
overlap and remaining distinctions. Their conditional compilers, unshifted
prime-support bounds and analytic constructions do not supply the missing
shifted-core or visit-count upper bound. No new theorem here depends on
their correctness, and their execution receipts are not relabeled as our
own runs.

## External theorem actually used

J.-H. Evertse, *The number of solutions of decomposable form equations*,
Theorem 3, printed page 7:
[primary author-hosted PDF](https://pub.math.leidenuniv.nl/~evertsejh/95-decforms.pdf).

The root and arithmetic author inspected the primary theorem, including
the arbitrary nonzero coefficients and the place-count convention. For
three variables over the rationals and a pool of `s` finite primes, it
gives the bound `(9*2^35)^(27(s+1))` used in SC1. Primes in the two fixed
core coefficients do not enlarge that pool. The exact nondegeneracy check
fails at valuation one, so those transitions are handled by the elementary
run clock instead.

This external input supports SC1--SC4 and the eventual-confinement clause
SS4. The elementary cycle and finite-basin clauses SS1--SS3 do not depend
on it. The optional PR145 strengthening is not needed for SS4.

## Identity and review

Each review names SHA-256 identities of its exact proof and checker files.
The publication artifact manifest maps those bytes into the committed
packet. Later edits require a new review boundary. No global novelty claim
is made from this limited source comparison.
