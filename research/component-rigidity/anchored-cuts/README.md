# Anchored cuts: preserved continuation

**PROPOSED. No complete Collatz proof; no independent mathematical review.**
Read [PROOF.md](PROOF.md), FC-001--007. The predecessor is
[the original component-rigidity proof](../pass1/PROOF.md).
This is the previously unpushed in-chat cut packet, not the different
[residue-locked continuation](../pass2/PROOF.md) in PR #137.

The original proof and four executable sources are preserved byte-for-byte.
The two deterministic JSON payloads are regenerated rather than committed.
A new `replay.py` reproduces their original byte hashes and runs both checkers:

```sh
python -S -B research/component-rigidity/anchored-cuts/replay.py /tmp/cuts-normal
python -O -S -B research/component-rigidity/anchored-cuts/replay.py /tmp/cuts-optimized
```

Python 3.10+, standard library. The largest bounded corridor reconstruction uses
an in-memory graph on 2,239,488 vertices. The sparse continuation addresses that
representation cost; it does not supply the missing upper repair bound.

## Results and exact limit

FC-001/002 refute all-coloring regularity at polynomial observation exponents
below log_2(3). FC-003 gives exact cut/coarea duality with a fixed ordinary source.
FC-004/005 prove finite-energy Liouville rigidity and escape of anchored costs.
FC-006 is a terminating *disjunction*: convergence OR exclusion of a prescribed
energy budget, not a total successful convergence selector. FC-007 remains OPEN.
The 5x+1 two-cycle control has escaping separation costs but never merges its pins.

## Publication provenance

The source archive was supplied in this conversation as
`collatz_component_rigidity_continuation_2026-09-25.zip`, original directory
`research/arithmetic-component-rigidity/pass2/`. The previous attempted direct
Git pushes failed DNS. This import uses an authorized connector on a separate
branch based on PR #137 at `2911b53930cbd31f623d3e0586ca3613854f0143`.
It leaves that branch, main, canonical statuses and workflows unchanged.

`VALIDATION.json` records this import's executed checks, not peer review.
The original proof's execution narrative is historical; its claims are not
promoted by publication. No full-checkout validator, remote CI or formal proof
build was run. No external priority claim is made.
