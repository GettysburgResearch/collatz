# Publication verification and inverse-frontier continuation

Agent: `astra-critical-mass-01` (GPT-6 Pro). Date: 2026-09-05.
Repository: GettysburgResearch/collatz. Research PR: #90; workspace issue: #89.

## The preceding bundle landed

The live PR metadata reports head

    b9a7b7ed0dd0cdf36d9dee578b1c75144ec9266d

at inspection. That commit is titled
`research(astra): inverse boundary fans and asynchronous bridges` and is a
child of the separate clock-defect commit

    a4b9b3a267e526f2b33ffd43c3b60d58be2aed5d.

It adds the six intended files with no deletions. The PR is OPEN and DRAFT;
publication on its branch is not a merge into main and not mathematical review.
The description's older embedded head is not the current head; the actual ref
and commit are authoritative for this continuation.

All six locally recomputed Git blob hashes match the remote commit/directory
metadata at b9a7b7ed. This verifies byte identity, not just filenames:

| File | Git blob SHA-1 |
|---|---|
| experiments/X-ASTRA-006-boundary-fan/README.md | 64461b50b84087df9cb7d6619286a1673b1cdebd |
| experiments/X-ASTRA-006-boundary-fan/results/canonical.json | d77fb4ebe1b8062e8edf39041e61e50776d40a4d |
| experiments/X-ASTRA-006-boundary-fan/run.py | 225eb546e385d6562eec1d57cc9c3fc6fb6dbe96 |
| experiments/X-ASTRA-006-boundary-fan/verify.py | 82dc3b185ee4df58f0db9a357fefbfc8cf715516 |
| reports/astra-critical-mass-01/2026-09-05-boundary-fan.md | 76d2c0aa31ae63f21c1f4a6d2240faf5c7a265a5 |
| research/astra-critical-mass/BOUNDARY_FAN.md | e9647cabda1ed5281f5ac3ac4e81edb70b561380 |

The separate supplied patch hashes to

    7bc9fe369c8d3c9640b09eaafd077679d652c64a5e4302dd5fbd941446f93439

and matches the patch inside the source bundle. Both old commands were rerun
successfully against the exact ZIP contents:

    run.py --check results/canonical.json
    verify.py results/canonical.json --self-test

The old semantic certificate remains

    3f06352e080db0c30281a9ebde34bbb21339f7feae4710072446b5737651d52e

with all eight resealed corrupt reports rejected.

## Read before continuation

I read the delivered BOUNDARY_FAN.md and current CLOCK_DEFECT.md. The former
had correctly refuted recursive boundary-only pruning. The latter imposes a
short-SHORTCUT-clock constraint, whereas the new pruning uses section-return
radius. A section edge may have unbounded shortcut length, so these scopes
must not be conflated.

The two parallel packets collide on some T-ASTRA-030 through 034 identifiers
and both call themselves the sixth pass. No source was silently renamed or
amended. The new packet uses the isolated AS7 identifiers and filename-qualified
provenance. Integration can resolve display aliases separately.

## What was attempted toward full closure

I tried to retain unresolved interior branches without restoring uncontrolled
fan-out at large ternary depth. The crucial observation is

    s_j = 2^(j+1)3^(h-j)u-2.

At sufficiently high remaining ternary precision, every bounded-depth inverse
branch from s_j follows the signed inverse tree rooted at the actual negative
integer -2. A rigorously computed precision cost determines how long that
correspondence lasts. During that interval every node is more expensive in P
than the original positive root. This yields a LOSSLESS pruning theorem for
every finite radius, with at most D^2+1 retained exits per node.

The precision boundary also has constructive content. A strict record in the
negative tree supplies an affine congruence where ordinary positive sources
acquire an arbitrary prescribed additional ternary depth. Sufficient excess
precision makes their rank smaller by a certified factor. This yields an
all-parameter family of new merging certificates rather than an unproved
uniform comparison of inverse tails.

I tested the proposed closing shortcut that reaching such a frontier itself
forces descent. It fails: y=139 has a corresponding interior ancestor 2965
with much LARGER rank. The actual excess valuation must be large enough.
I also tested whether unlimited pure inverse search could suffice on every
residual. It cannot: all lower-rank possible sources for 121 form a finite set
whose entire orbits avoid 121. Any lower-rank merger with 121 must first move
forward at least 54 shortcut steps; 40 attains that exact bound.

## Strongest new results and remaining obligation

See [INVERSE_SHADOW_FRONTIER.md](../../research/astra-critical-mass/INVERSE_SHADOW_FRONTIER.md).

- T-AS7-003: exact inverse-rank minimum at every finite radius with a
  depth-dependent frontier and a source-independent branching bound.
- T-AS7-004 and C-AS7-005: positive ordinary record-frontier families with
  strict rank loss, including an unbounded delayed interior-chain family.
- R-AS7-006: all-depth inverse impossibility and exact all-witness clock
  lower bound for the residual source 121.

Q-AS7-001 remains OPEN: prove a total selection of a finite forward endpoint
and a cheaper actual merging source. Per-radius termination and complete
finite search do not prove total termination. No Collatz proof was obtained.

## New validation

The new generator and separately written verifier agree on the exact full
payload, including 478 complete/pruned comparisons, 984 negative comparison
vertices, 48 entire-cone bijections, 1,632 ordinary rank reductions, ten delayed
families, and the exhaustive lower-rank witness pool for 121. Eight resealed
corrupt reports are rejected. Details and commands are in the new experiment
README. Both implementations have the same author; no independent mathematical
acceptance is claimed.

Semantic SHA-256:

    7fd1eab2f411c732f2af00b326bb36d67dcca0d1d46a73c1184b22041749b3d7

Full payload SHA-256:

    ab2cca5d69cbf1917317ca54334ed80802a9dcd00607adf6e6ce2de4624cfb60

## Publication boundary for this continuation

The GitHub connector in this session exposes read actions but no create/update
publishing action. Relevant plugin discovery found the already installed GitHub
connector, not an additional write capability. A direct `git ls-remote` attempt
failed with `Could not resolve host: github.com`; no authenticated checkout or
remote push was available.

This continuation is therefore delivered as six new files and an addition-only
patch based on b9a7b7ed, NOT as a remotely pushed commit. It does not overwrite
the branch's research README or any existing proof, artifact, registry, workflow,
setting or another contributor's PR. The supplied external manifest records
exact bytes and Git hashes for a subsequent publisher. Historical source
reports retain their original publication and review scopes.
