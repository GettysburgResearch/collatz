# Latest-source comparison

This pass began by reading the current metadata for all **102 open pull
requests**, ordered by update time, and the twenty most recently updated
closed requests. A publication refresh found **105 open requests**,
including new PR167--169 and an advanced PR146. The
[metadata snapshot](../../reports/2026-11-21-global-forcing/source-heads.json)
records that later inventory. This is an inventory, not a mathematical
review of every branch. Main remained
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.

Changed research text for PR146 and PR161--166 was fetched at the heads
below. The mathematical dependencies and the actual comparison coverage
are narrower than those complete branches. In particular no external Lean
build, unrelated search corpus, or manuscript-upload archive was rebuilt.

## Frozen upstream heads

| PR | Full source head | Material used or compared |
|---|---|---|
| [146, initial](https://github.com/GettysburgResearch/collatz/pull/146) | `fd991063721e9c157d318e40bb20131762f7d750` | Five-comparison localization, sparse least-failure sieve, phase invariant and bounded-rank transfer used by the frozen proof notes. |
| [146, refreshed](https://github.com/GettysburgResearch/collatz/pull/146) | `66970775e4bdc945a68308e37a8eb028ebde42d2` | Every-progression five-return construction, simultaneous blocks, and bounded multiplication-link cost. |
| [157](https://github.com/GettysburgResearch/collatz/pull/157) | `64361ecca770092d6c8242dc6211e38818af2e50` | Existing forward-five criterion; exact rank-one target family and the 5/25 stopping-grade obstruction. |
| [161](https://github.com/GettysburgResearch/collatz/pull/161) | `4a0536b587fc91ee0c7bb1b160c06dda16ddbf23` | Shifted defect equation, finite-prime-pool transition count and fixed-source defect clock. |
| [162](https://github.com/GettysburgResearch/collatz/pull/162) | `2279da37ac612dbe049777354cdedb3c0aa03282` | Original physical block `(2,b)`; predecessor of the PR166 ladder, credited through that source. No new verdict on its whole occupation packet. |
| [163](https://github.com/GettysburgResearch/collatz/pull/163) | `051237135a34ae7d4b973ee5fcf5da04ded6f0fc` | Complete five-to-tripling energy comparison, shifted smooth classification, and explicit boundaries of previous closing attempts. |
| [164](https://github.com/GettysburgResearch/collatz/pull/164) | `6fa6b429870a9cd53cde0fc77ad64a3c3956199f` | Certificate team inspected the current 512-residue continuations. No result from them is an unstated premise here. |
| [165](https://github.com/GettysburgResearch/collatz/pull/165) | `78bdb31ccba608de3d089b751a0ab59a52007408` | Compared its explicit exceptional-family and phase attributions. Its preserved uploads were not independently replayed in this pass. |
| [166](https://github.com/GettysburgResearch/collatz/pull/166) | `5996b9f525ca50978bc34f423192c36a87765bf3` | Unbounded valuation-two ladder, exact inverse fibers and renewal coefficients; prior signed-template architecture; general-rank unit equations in a different inverse-certificate problem. |
| [167](https://github.com/GettysburgResearch/collatz/pull/167) | `e83cc8b35ad614c616df7c00318cc9645a174c34` | Fixed-defect returns, stronger prime-family excursions, and five-energy interfaces. |
| [168](https://github.com/GettysburgResearch/collatz/pull/168) | `e4599b32e4b1a955ac9315d46782d4ad6a5db96c` | General balanced-return recognizer, concurrent short identity, negative templates and stationary regularity boundary. |
| [169](https://github.com/GettysburgResearch/collatz/pull/169) | `6cb9bfdc828f91576066b0e4a099d47d8144e915` | Extended physical word families, gap-five bypasses, all-time endpoint telescope and explicitly conditional moments. |

## What is inherited and what this packet adds

### Arithmetic

PR161, `research/source-rigidity-20261120/SHIFTED_CORE_TRANSITIONS.md`,
SC1--SC3, already uses

`2^b + (3/2)m - 2^b m' = 1`, with `m=n+1` and `b=a(n)-1>=1`.

It proves the needed nondegeneracy and a bound controlled by a prescribed
prime pool. Its last paragraph in SC3 explicitly declines to claim a
rank-only bound for arbitrary rational generators. The present arithmetic
note substitutes the general finite-rank theorem of
Evertse--Schlickewei--Schmidt, with a precisely constructed rank-at-most
`2r+1` group. It handles arbitrary cosets without adding their prime
supports to that rank.

The conversion from a bounded number of increasing/decreasing cycle blocks
to a finite cycle ceiling is classical. The note cites Simons--de Weger and
reconstructs a coarse bound using the exact Lagarias inequality already
used in PR163. The addition is the **uniform shifted rank/coset interface**,
not discovery of classical fixed-block cycle finiteness or a sharper
logarithmic-form estimate. The unshifted rank results in rStation Paper
138 are explicitly separate. No broad literature priority is asserted.

### Physical certificates and renewal

PR166, `FIVE_CERTIFICATE_LADDER.md`, FL1--FL3, already compiles arbitrary
runs of valuation-two letters followed by a letter at least four. The new
carry mechanism enters `(y,5y+4)`, survives arbitrarily many valuation-one
steps, and exits back to `(q,5q)`. Its source starts with the specified
seven-letter entry word, whose first two letters are 2,1, outside the
old ladder. Explicit ordinary unit witnesses realize every resulting
source rank at least nine. The separate new short block starts with three
ones and has source cylinder `271 mod512`. The mixed compiler retains
every division and first-hit assertion. This is not universal coverage.

PR166, `LADDER_RENEWAL.md`, R1--R6, already supplies positive finite-cutoff
renewal and the coefficients `16/21` and `81744/82925`. Merely adding
independent worst-case subcritical bounds would lose contraction. The new
comparison uses the shared **actual endpoint modulo27**: the old ladder's
worst case forces substantially later inverses in the new families. In
the safe carry sublanguage `b>=r+2`, the forced exit congruence modulo18
also controls the entire sum over run lengths. The resulting contraction
holds on the larger disjoint union of all three families. The uncovered
defect still has no absolute finite-energy bound.

PR163, `FIVE_SLICE_ENERGY.md`, FE1 and section4, already closes the global
five-to-tripling transport question left open in PR160. This packet does
not claim that result anew and does not import its source-qualified
predecessor-density conclusion as an unconditional theorem.

### Phase and compiler completeness

PR146, `BASIN_PHASE.md`, already establishes the stopping grade and the
affine-edge invariant, including a finite-seed obstruction for a different
exponential family. Its `BOUNDED_RANK_TRANSFER.md` already develops the
signed rational template test. PR166 explicitly discusses that template
method for multiplication by five. Neither architecture is invented here.

PR157, `closing-attempts.md`, GCL-001, already gives the rank-one source
`(4^a-1)/3` and the long exact target prefix. GCL-002 already gives the
5/25 phase mismatch. The present phase note applies these mechanisms to
**every dictionary of proportional native affine rewrites**, including
reverse ordinary edges, with any bounded-below terminal phase library.
This is a limitation of that proposed completion strategy, not a
limitation on arbitrary source-dependent proofs or a refutation of the
published restricted-language compilers.

## Current PR146 changes were read, not inferred from its old number

Relative to the earlier PR160 pass's inspected PR146 head, the new source
adds `FIVE_STEP_SEEDS_AND_MULTIPLIERS.md` and `LEAST_FAILURE_SIEVE.md`, and
extends `DEEP_REVERSE_BASIN.md`. The root read these new notes in full.

The first constructs an ordinary lift of every prescribed five-comparison
into a single binary/ternary progression. Its lift into the already
covered `49 mod64` block has height cost below `2^17/9`. The second gives
a sparse sufficient set for the directed adjacent criterion. Neither
supplies the missing implication on every retained input.

Lifting an arbitrary comparison into a covered cylinder and then applying
that cylinder's physical reduction returns to the original comparison.
The two true statements therefore do not compose into a terminating proof.
Likewise, a relative sparsity estimate does not by itself bound an unknown
invariant-label moment. These are the exact handoff gaps retained here.

## Publication refresh: concurrent results and changed boundaries

The root read PR146's new `research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md`
at `66970775e4bdc945a68308e37a8eb028ebde42d2` in full. Sections1--3
extend physical localization to every prescribed arithmetic progression
and to simultaneous finite blocks. They construct ordinary representatives
with endpoints `q,5q`, and strict descent on a refined subprogression of
each given progression. They do not show that those refined cells contain
every supplied integer. Lifting a comparison and returning to its original
endpoints still does not decide that comparison. The new section4 also
gives an exact two-anchor multiplication-link cost and an unbounded-cost
obstruction on one-step antecedents. This is additional prior source for
the phase-budget boundary; our phase note is not a new invariant.

The three route-specific refresh comparisons are:

- [Arithmetic](arithmetic/LATEST_COMPARISON.md): PR167's fixed-defect
  return finiteness and stronger excursion bounds; PR169's all-time
  telescope and explicitly conditional moment criteria.
- [Certificates](certificates/LATEST_COMPARISON.md): PR168's complete
  balanced-return recognizer and PR169's expanded word families and
  certified gap-five bypasses.
- [Energy and regularity](energy/LATEST_COMPARISON.md): stationary
  approximation, source/endpoint weighting, and the remaining inputs
  needed to apply them to ordinary components.

**Originality correction from the refresh:** CF1, the `271 mod512`
block, already appears in PR168 FR2 and PR169 FW3(B). The frozen initial
proof is an independent reconstruction of that identity. CF5's finite
language is a concrete specialization of PR168 FR1--FR3's general
balanced-return algorithm. CF2--CF4's explicit carry-four entry, arbitrary
one-run, exit and all-rank ordinary unit realization were not found in
those inspected notes, although their general recognizer can certify
such a word once supplied.

The shared-endpoint kernel method also appears in the concurrent energy
arguments. PR168 FR4 proves coefficient `903/1000` with cutoff `X/2`
on its selected domain; PR169 proves `249/250` with `X/3` on another.
Both selected domains omit the new carry entry. Our CR3 domain adds every
safe carry run but omits some of their other families. These covered
domains are incomparable. We do not claim the best numerical contraction
coefficient, the largest known domain, or invention of endpoint
conditioning. The contribution is the exact all-run carry kernel and its
compatible combination with the two stated families.

Neither concurrent result supplies an absolute bound for our full Q.
An all-time endpoint telescope carries a different denominator and
Jacobian weight; a finite stationary model needs an unproved ordinary
approximation input. No such premise is silently substituted for the
missing global theorem. Frozen scientific files retain their original
source freeze; this refresh governs the packet's public attribution and
current comparison.

## Selected upstream file identities

| Source file | SHA-256 |
|---|---|
| PR146 refreshed `FIVE_RETURN_IN_EVERY_CLASS.md` | `0705056d3c91e1bf5f7c706189469c93cf76da364a5fa2d32ff24da729a7309b` |
| PR146 `FIVE_STEP_SEEDS_AND_MULTIPLIERS.md` | `62e84ecb23ee49ef93b9f5f6d2bffa8cc42e79d8d04b42d745396f6b120d4d66` |
| PR146 `LEAST_FAILURE_SIEVE.md` | `563d4626e09db89d2f954bf1fb999c878c2070d9bb90ae5974825ce9dddcf451` |
| PR146 `BASIN_PHASE.md` | `cf5a610370a7dbbff8bd120e3dacfced95a92997ceb462e6472430b1658b734d` |
| PR146 `BOUNDED_RANK_TRANSFER.md` | `1d96c0a77c65ff448255b5c804be03d73b6a76098364e73b14b9c93bb2ea05ee` |
| PR161 `SHIFTED_CORE_TRANSITIONS.md` | `f53846e08e1522058797c6cab57111cf9c7ed4385f39b0e055ab05264f7acb71` |
| PR163 `FIVE_SLICE_ENERGY.md` | `d1d6d2708f291f4b918004e7e2705bd1ceaa3d60c7e022d0f9c7bfbe2749fbb0` |
| PR166 `FIVE_CERTIFICATE_LADDER.md` | `d66dee00fb9ab089694363d2905f788f3d319c5a79ac3e8d9448efcb5cbb6dba` |
| PR166 `LADDER_RENEWAL.md` | `dbaff460c0a3f76f6cfa4947ba52d2511fb46ffedfac051baf3904c38402fa32` |

The scientific manifest and publication receipts separately identify this
packet's own final bytes and the commits on which its checks actually ran.
