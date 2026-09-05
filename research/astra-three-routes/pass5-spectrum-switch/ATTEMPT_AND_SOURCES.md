# Fifth-pass attempt log, source boundary, and review targets

Agent: `astra-three-routes-05` (GPT-6 Pro), 2026-09-05.
**All new theorem-level claims are PROPOSED pending independent review.**

## 1. Frozen inputs actually inspected

- Existing PR #92 head: `6266bd8f73ce2f8488c02fbe29f34fd2b4f289bc`.
  Branch: `agent/astra-three-routes-01/three-route-offense`.
- Main re-queried at `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`.
- The current PR metadata and AGENTS.md were read through the GitHub connection.
- Parent proof read in full:
  [MOVING_GHOST_RANK.md at the frozen head](https://github.com/GettysburgResearch/collatz/blob/6266bd8f73ce2f8488c02fbe29f34fd2b4f289bc/research/astra-three-routes/pass4/MOVING_GHOST_RANK.md).
  The exact A acceleration, four-entry collapse, properness, and high-precision
  component-minimum lemma are the parent dependencies used here. Their proofs
  are elementary and their repository status remains PROPOSED.
- Parent related interfaces:
  [RESONANT_SOURCE_FAN.md](https://github.com/GettysburgResearch/collatz/blob/6266bd8f73ce2f8488c02fbe29f34fd2b4f289bc/research/astra-three-routes/pass4/RESONANT_SOURCE_FAN.md) and
  [RENEWAL_MASS.md](https://github.com/GettysburgResearch/collatz/blob/6266bd8f73ce2f8488c02fbe29f34fd2b4f289bc/research/astra-three-routes/pass4/RENEWAL_MASS.md).
  The finite rank fiber and e=4 mod8 power family are credited, not relabelled
  as discoveries of this pass. The new obstruction narrows e to 4 mod16 to
  prove failure AFTER inducing on the enlarged unsafe set.
- PR #90 was checked for overlap. Its metadata head was
  `b9a7b7ed0dd0cdf36d9dee578b1c75144ec9266d`; the body still named the older
  `a4b9b3a267e526f2b33ffd43c3b60d58be2aed5d`. The latest commit's inverse-boundary
  and asynchronous-bridge diff was inspected. Its rank P=(2n+1)^2/3^h is not
  the present R. No new result on that branch is used as a proof dependency,
  independently verified here, or merged into this packet.

A targeted external web search was performed for transfer-operator and
termination connections. No external theorem was imported into these proofs.
The abstract positive-mass and minimum-rank closing criteria are credited to
the preceding repository work and are not claimed novel. No broad external
priority claim is made for the new elementary arguments either.

## 2. The actual full-closure attempts

### Mass attempt

The hoped-for proof was: eliminate all nonincreasing-rank excursions, use
R^(-p) as a summable weight on the remaining process, establish inverse
contraction there, and sum over an exceptional invariant set.

The rank-spectrum and plateau theorems complete the first two preparatory
steps with explicit all-source tails. The candidate contraction is FALSE:
x=3^(4+16j) and y=(9x+7)/16 are consecutive unsafe states and make its ratio
unbounded. This is not an unknown numerical failure or an issue at a finite
floor. The exact counterfamily is proved in INDUCED_MASS.md.

The next missing theorem is an induced weight with a proved correction, or an
aggregate estimate for the actual transported mass. The summability of the
bad source family shows why a pointwise failure does not rule out that route.
No total occupation estimate on the unsafe process is claimed.

### Source-separation attempt

The hoped-for proof was: choose the least refined-rank exceptional source,
enumerate all its possible smaller witnesses, and force one finite merging
diagram. The new spatial list is complete and O(sqrt(R(n))). The bounded
clock compiler is exact and tested by a separate inverse-tree method.

The gap is temporal, not an omitted source range: at a fixed cap there can
be no meeting among these candidates, even for familiar convergent integers.
The tested cap six leaves 9,27,703,2223 unresolved. No claim that every source
has a bounded-cap certificate survives this test. An unbounded search is not
assumed total. The all-source merging cover remains OPEN.

### Termination attempt

The hoped-for proof was: orient the old flat-rank cases, then pay each adverse
mode switch by a later component-aligned block, using one common integer
rank throughout. Flat steps are now uniformly oriented. A two-mode theorem
proves repayment on genuine initially misaligned ordinary families, with an
unbounded common-rank spike in the sharp 3->2 family.

The first unsupported inference would be that high ternary precision forces
the required next mode and residence. It does not: n=103 has the requested
ternary depth three and initial mode three, but next mode four. CRT preserves
such freedom at arbitrary depth. The repayment family's domain is retained
as a condition, not a global dynamical conclusion. Universal coverage remains
OPEN even though every supplied certificate is finite and strictly descending.

## 3. Claim matrix

| ID | Statement | Status / boundary |
|---|---|---|
| T-A3-1001 | Complete rank sublevel has sharp square-root exponent; exact enumerator | PROPOSED, all positive ordinary sources |
| T-A3-1002 | Summability iff p>1/2; explicit rank and ordinary-source tails | PROPOSED, no convergence assumption |
| T-A3-1003 | Polynomial all-source safe-resolvent bound on enlarged G | PROPOSED; killed on unsafe exit as well as 1 |
| R-A3-1004 | Pure reciprocal-rank weights fail on the induced unsafe operator | PROPOSED exact refutation, not all weights |
| T-A3-1051 | Equal-rank A steps strictly increase the ordinary source | PROPOSED all-height direction, not a complete flat-edge classification |
| T-A3-1052 | Strict integer refinement and finite enlarged-safe clock | PROPOSED; exit may be unsafe |
| T-A3-1053 | Complete lower-Phi spatial list and bounded-clock search | PROPOSED; full temporal cover OPEN |
| T-A3-1101 | Exact cross-mode affine defect and ternary precision reset | PROPOSED, stated modes and valuations |
| T-A3-1102 | General two-mode repayment with explicit sufficient residence | PROPOSED infinite ordinary families, not a total cover |
| T-A3-1103 | Sharp 3->2 family with arbitrarily large common-rank spike and net decrease | PROPOSED all t>=3, future-word hypothesis retained |
| X-ASTRA3-005 | Exact finite interfaces and outward source-tail intervals | Reproducible same-author evidence, not independent proof review |

## 4. Adversarial mathematical review order

Check the complete rank-sublevel count, especially e>=a for a minimizing moving
index and duplicate counting. Check the equal-rank contraction exclusion: the
rank-fiber sign and parity conventions, all three small exceptional solutions,
and the distinction between a candidate component and the actual minimum.
Check the scalar Phi ordering when rank drops by one and when it stays flat.

For mass, verify that G is defined at the CURRENT state, that arrival at 1 is
killed, and that the r+1 distinct source count is valid. The induced spike
must have both endpoints unsafe; this is why e=4 mod16, not merely 4 mod8.

For repayment, verify the sign of Delta_ab, its exact v3, the unequal-valuation
step, the real bound (6), the shared minimizing component at the initial point,
and the extra final parity bit used for exact maximality. The sharp family's
initial and intermediate COMMON minima must both be checked; a component-only
spike would be a weaker statement.

## 5. Checks and operational limits

Both programs passed locally, with byte-identical generated reports. The
verifier passed with Python -O and rejected eight altered, resealed reports.
They have separate source, dictionary evaluation, parity lifting and merging
search methods but the SAME author: this is not independent mathematical
acceptance. Universal statements rely on the proofs, not finite extrapolation.

No parent large inverse-cone computation, external Lean build or large payload,
full-repository structural validator, or GitHub workflow was run. This session
could not publish: all 48 exposed GitHub actions were reads; plugin discovery
found the already-installed connection; git ls-remote failed with "Could not
resolve host: github.com". No write, remote commit, branch update or PR edit
is claimed. The package is an addition-only patch against the exact frozen PR
head; application was checked on a local deterministic fixture, not a full
private checkout. The publication helper itself is NOT executed here.
