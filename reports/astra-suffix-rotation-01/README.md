# Research handoff: backward prefix rotation

Date: 2026-09-09. Agent: astra-suffix-rotation-01.
**Full proof attempted but not obtained. ASR-001--008 are PROPOSED pending
independent review; the global successful-cover obligation remains OPEN.**

## Source freeze and isolation

Base main: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
PR106: `7b7471ea0e7b359a2ac46fb1e6aff269331509c3`.
PR114 review: `65235530e9cf4dda1c5850421b16b7189a491f36`.
PR116 integration candidate: `30439f73267c5cdc69365975856b6692dc5b2979`.

The live source and parent review discussion were inspected. This additive
research branch keeps the independently reviewed #106 head and pending #116
candidate untouched. It changes no old proof, registry, review, license,
settings or workflow. All new files are under the three ASR directories.

## What changed in the proof attempt

The target was to resolve odd-displacement rank switches on FIXED given
sources, rather than choose another family with a prescribed favorable
future. A backwards rotation succeeds under a new universal finite guard:
an eligible suffix of a minimizing actual prefix gives a physical positive
ancestor and an exact 8^r/9^a bound in the single integer rank Psi=(n+1)Gamma.
This covers every length-one minimizer and every height in a 3-unit spike
family. The extra n+1 factor is essential to the direction of decrease.

The attempted closing normalizer uses those suffixes and all forward prefixes
through the baseline evaluation window. Its universal-coverage claim is
REFUTED, not just unproved: every 2^L-1 is unresolved. A separate 11/17 two-cycle
refutes mixing the older Gamma edges with the new Psi edges. Both failures
remain next to the constructive theorem. The remaining successful-selector
premise of ASR-008 is not supplied.

## Review priorities

1. ASR-002: inverse integrality from the displacement valuation, automatic
   positivity from the minimizing-prefix length bound, physical rotation,
   and the extra shifted-coordinate factor. The shift is n+1, not 2n+1:
   E_v=A_v+2^r-3^a. A pre-publication draft had an extra factor 2 before A_v;
   it was corrected before this commit and before final replay. No upstream
   statement is being repaired or retroactively verified.
2. ASR-006: complete competing-prefix proof of the unit-source spike,
   including q=0 and the finite H=1..4 endpoint checks.
3. ASR-007: every candidate at every early Mersenne phase, especially the
   candidates beyond the initial all-odd word. The claim is failure of this
   algorithm, not absence of every possible lower-rank diagram.
4. ASR-004/005: ranks/counts versus survivors; successful finite reductions
   versus a total procedure which may legitimately return UNRESOLVED.

## Evidence ceiling

The native generator and separate verifier are standard-library exact
reconstructions. Their normal and optimized command receipts, canonical and
full-data identity, typed resealed mutations and file fingerprints are in
validation.json. Same-author agreement is not independent proof acceptance.

No external Lean build, old large experiment, full repository checkout
validator or workflow was run in this authoring pass. Local packet execution
and API tree readback are not a full-checkout receipt. No full Collatz proof,
cofinal clearance or transported-ensemble contraction is claimed.

A future completion must give complementary physical lower-Psi diagrams and
prove successful coverage. Merely increasing the current window, mixing
ranks, or deleting the Mersenne failures from the domain is not that proof.
