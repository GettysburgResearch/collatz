# Pass 3 self-audit, dependency boundaries, and execution record

**PROPOSED; same-author self-audit and implementation diversity, not independent
mathematical review or formal proof checking.** The four workers are ordinary
Python processes. No callable independent-agent launcher was available.

## Frozen context and exact scope

Repository `GettysburgResearch/collatz`, PR #140, branch
`research/novel-swarm-20261030`, frozen parent
`c8a5f1a391a10ef4927383e472bceebb2b04c5e7`, tree
`a3d1468e5d1cd3920595b2f4cb95a0998543c98b`.
The live PR and recent #141/#142 descriptions were read before this pass.
There was no exhaustive new audit of every historical PR.

Core dependencies at that frozen parent:
- `research/astra-three-routes/pass3/FINITE_RECORDS.md`, T-A3-651: finite
  simple-path packing and reciprocal budget. Its argument, including the
  discarded terminal q states, is reconstructed in B1. This is credited
  prior research; its numerical constants are not newly discovered.
- `research/astra-three-routes/pass2/ORBIT_MELLIN.md`, T-A3-401--403:
  context for orbit sparsity versus predecessor basins; no basin injectivity
  is imported from it.
- `research/novel-swarm-20261030/pass2/INVERSE_PRESSURE.md`, P1--P4:
  first-hit upper weights, exact cycle factor, odd reciprocal-square tail,
  and critical-resolvent upper growth.
- `research/novel-swarm-20261030/pass2/RIGIDITY.md`, R1--R4:
  finite-family compiler, inverse-ladder cone access, and binary invariant
  rigidity. W1's finite identity-test bound is independent of R4. Only W2's
  statement about EVERY NONCONSTANT model additionally uses R4, whose
  proposed status is not promoted here.

## Claim-by-claim self-audit

B1: The first-hit path must be simple; otherwise a repeat before the target
would prevent ever hitting it. The product includes preterminal odd states
only. The inherited bound is uniform over finite paths, so no convergence
assumption enters the lower weight bound. The rational constant follows
from ln2>2/3; it is intentionally very loose. Cycle loops are excluded here.

B2: All comparisons are termwise over actual first-hit sources. Extended
nonnegative sums justify rearrangement. The density exponent decides strict
sides of the abscissa only, not its endpoint. Targets divisible by three
have basin {t} and are treated separately. All-history pressure retains its
exact cycle factor instead of deleting hypothetical positive cycles.

B3: External positive-density releases are SOURCE-QUALIFIED inputs D/L, not
newly accepted facts in this project. The proof converts ordinary to odd
sources by truncating their initial powers of two; raw and odd clocks are
not identified. The conclusions assert growth comparability, not a pole,
a residue limit, or a full Collatz theorem.

B4: A certified total-pressure upper approximation plus a uniform positive
candidate contribution can decide a missing witness. Enumeration is fair
and duplicates are removed. A finite enclosure is not a computable-real
oracle of arbitrary precision. Decidable basin membership is not universal
membership.

Q1: Every small-source orbit is completely classified, not merely followed
to an arbitrary depth cap. A raw-clock reconstruction checks all entries.
The profile stores partial unnormalized H_2 and must be divided by t^2.
The infinite-domain error is the source tail, independent of the target.

Q2--Q4: Nonperiodic ordinary orbits are injective and tend to infinity. Each
positive coordinate in a nonzero cluster limit pins ONE fixed source, so
its targets really lie on an unbounded ordinary orbit; changing finite roots
cannot supply the proof. Coordinate domination gives compactness and l^2
convergence. Disjoint components give disjoint support. The criterion is
universal EVENTUAL PERIODICITY, explicitly not uniqueness of the 1-cycle.

Q5: Old-source normalized weights stay exactly fixed while new sources enter
nested basins. The source n and all clocks are retained. The global bound
uses the same simple-path product. A bounded increasing ledger is not
termination. Applying the statement past repeated cycles with G instead of
H is refuted by the exact fixed-point control. Its recorded cycle K is the
single-source-1 contribution, NOT the total G_2(1). A final manuscript audit
corrected that distinction before branch publication; executable bytes and
their successful outputs were unchanged.

W1--W3: The carry set is {0,1,2}; the final canonical 1 and residual carry
flush are included. The odd k=0 test follows from the even source2 test.
The reachable-space bound is field-independent; the executable corpus uses
only prime fields. Claimed operation complexity counts field operations,
not coefficient bit complexity. Constant outputs are certified directly
by a closed span, not accepted merely because the parent theorem predicts
constancy. This concerns invariant source classifiers, not rank functions.

## What actually ran

Python 3.13.5. Parent `pass2_check.py` freshly regenerated its full output in
11.60 seconds, exit zero; its SHA-256 equals the published
`55553f48298d17269068acdc3349ca9471f81c04ca9e16f7c5374f99a729ae18`.

Final pass-3 producer: normal four-process 11.60 seconds, normal serial 19.80
seconds, optimized four-process 15.72 seconds. Each exited zero. Both the
checks file and 1.4 MB profile were byte-identical across all three modes.
Verifier: normal 9.58 seconds and optimized 10.42 seconds, both zero, with
identical complete verification outputs. Times are execution observations,
not performance guarantees. Exact commands and file hashes are in receipt.json.

The producer checks 4,300 supplied linear models and returns 1,509 edge and
2,791 invariant/constant outcomes. The verifier reconstructs the EXPORTED
33 certificates (13 edge,20 closed-span constant), not the full census. It
uses direct MSB row evaluation and a separate elimination implementation.

The verifier independently reconstructs every one of the 52,063 rational
profile entries by following all 32,768 odd sources through 1 under the raw
shortcut map: 2,379,157 transitions, corresponding to 1,195,565 odd steps.
It also checks every one of the 296 transported ledger entries and 12,288
cohort memberships, and all 5,460 valuation words/16,380 positive lifts using
reversed inverse branches. Ten direct semantic/schema/duplicate-JSON controls
are rejected per mode. They are not separately resealed full-corpus mutations.
The finite Chernoff algebra checks in the producer are not independently
re-enumerated by the companion verifier.

The complete large checks/profile are regenerated, not committed. The small
verification output is committed. No statistical confidence level is inferred
for an infinite mathematical assertion from any of these finite counts.

## External-source limits and publication

Primary ProofAtlas versioned interface pages were inspected on 2026-10-31;
URLs and statements used are in B3. Their manuscript downloads were not
successfully recovered in this session and no external Lean project was
executed. An attempted screenshot of the classical Meinardus PDF failed at
fetch/cache protection; no detailed claim from that paper is a dependency.
No external novelty priority is claimed.

Direct git networking failed DNS resolution of github.com. Publication uses
the connected GitHub Git-data API, with an expected-head lease and later
remote tree/blob checks. This is not a complete checkout. No root
`tools/validate.py`, remote CI, Windows replay, external theorem prover, or
independent mathematical review is claimed. Earlier files, main, workflows,
licenses, settings and mathematical acceptance registries are unchanged.

## First unsupported step

The ordinary boundary theorem leaves an explicit decay obligation F(t)->0;
no argument here proves it. Nontrivial cycles remain a separate problem even
if that obligation is discharged. The occupation collision upper bound E5
also remains open. The matrix witness theorem supplies no representation of
the actual convergence indicator. None of these gaps is hidden by a passed
experiment, a published commit, or a new equivalence.
